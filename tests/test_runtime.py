"""Worker handlers end to end against the NATS/JetStream fakes."""

import asyncio
import json
from datetime import UTC, datetime
from typing import Any

import pytest
from google.protobuf import json_format

import cairn_garmin  # noqa: F401 (proto path bootstrap)
from cairn.worker.v1 import worker_service_pb2 as w
from cairn_garmin import archive, runtime
from cairn_garmin import config as C
from cairn_garmin.archive import ResultRef
from tests.fakes import FakeJS, FakeKV, FakeMsg, FakeNC, FakePullSub, make_worker

START_MS = 1_700_000_000_000


class FakeClient:
    def __init__(self) -> None:
        self.days: list[str] = []

    def list_activities(self, start: int, limit: int) -> list[dict[str, Any]]:
        if start:
            return []
        return [{"activityId": 7, "beginTimestamp": START_MS}, {"activityName": "no id"}]

    def get_activity(self, ext_id: str) -> dict[str, Any]:
        return {"activityId": ext_id, "beginTimestamp": START_MS, "activityType": {"typeKey": "running"}}

    def get_activity_details(self, ext_id: str) -> dict[str, Any]:
        return {
            "metricDescriptors": [
                {"key": "directTimestamp", "metricsIndex": 0},
                {"key": "sumDistance", "metricsIndex": 1},
            ],
            "activityDetailMetrics": [{"metrics": [START_MS, 0.0]}, {"metrics": [START_MS + 1000, 3.0]}],
        }

    def daily_health(self, day: str) -> dict[str, float]:
        self.days.append(day)
        return {"Steps": 100.0}


class Responder:
    def __init__(self, data: bytes) -> None:
        self.data = data
        self.response: dict[str, Any] = {}

    async def respond(self, payload: bytes) -> None:
        self.response = json.loads(payload)


def discover(wk: runtime.Worker, req: dict[str, Any]) -> dict[str, Any]:
    msg = Responder(json.dumps(req).encode())
    asyncio.run(wk._on_discover(msg))  # type: ignore[arg-type]
    return msg.response


def results(js: FakeJS, subject: str) -> list[w.JobResult]:
    return [json_format.Parse(d, w.JobResult()) for s, d, _ in js.published if s == subject]


@pytest.fixture
def uploads(monkeypatch: pytest.MonkeyPatch) -> list[bytes]:
    """Captures claim-check uploads; the raw archive is a no-op returning a blob id."""
    bodies: list[bytes] = []

    async def fake_upload(nc: object, body: bytes) -> ResultRef:
        bodies.append(body)
        return {"blob_id": f"transfer/{len(bodies)}", "size": len(body), "sha256": "x"}

    async def fake_archive(nc: object, *args: Any) -> tuple[str | None, int]:
        return "raw/7.json", 99

    monkeypatch.setattr(archive, "upload_result", fake_upload)
    monkeypatch.setattr(archive, "archive", fake_archive)
    return bodies


def test_discover_lists_a_page() -> None:
    wk, _ = make_worker(FakeClient())
    resp = discover(wk, {"account_id": "acc-1", "start_page": 1})
    assert resp["next_page"] == 2
    assert resp["items"] == [
        {
            "item_type": "activity",
            "external_id": "7",
            "item_time": datetime.fromtimestamp(START_MS / 1000, UTC).isoformat(),
        }
    ]
    assert discover(wk, {"account_id": "acc-1", "start_page": 2}) == {"items": [], "complete": True}


def test_discover_reports_errors() -> None:
    wk, _ = make_worker()  # no client, no creds
    assert "no Garmin credentials" in discover(wk, {"account_id": "acc-9"})["error"]


def test_creds_come_from_the_server() -> None:
    nc = FakeNC({runtime.CREDS_SUBJECT: {"email": "a@b", "password": "pw"}})
    wk, _ = make_worker(nc=nc)
    client = asyncio.run(wk._client_for("acc-2"))
    assert client._email == "a@b"
    assert client._garth_home == "/nonexistent/acc-2"
    assert asyncio.run(wk._client_for("acc-2")) is client  # cached
    assert len(nc.requests) == 1


@pytest.mark.parametrize("reply", [{"error": "revoked"}, RuntimeError("no responders")])
def test_creds_fall_back_to_env(reply: dict[str, Any] | Exception) -> None:
    cfg = C.Config(garmin_email="dev@b", garmin_password="pw", garth_home="/t")
    wk, _ = make_worker(nc=FakeNC({runtime.CREDS_SUBJECT: reply}), cfg=cfg)
    assert asyncio.run(wk._fetch_creds("acc-3")) == ("dev@b", "pw")


def test_fetch_source_publishes_activity_with_stream(uploads: list[bytes]) -> None:
    wk, js = make_worker(FakeClient())
    job = {"ext_id": "7", "account_id": "acc-1", "user_id": "u1", "fetch_streams": True}
    asyncio.run(wk._handle_fetch_source(json.dumps(job).encode()))

    (env,) = results(js, C.RESULT_SUBJECT)
    assert env.payload_ref.blob_id == "transfer/1"
    full = json_format.Parse(uploads[0], w.JobResult())
    act = full.events[0].activity
    assert act.ref.external_id == "7"
    assert act.raw_blob_id == "raw/7.json"
    assert list(act.stream.distance_m) == [0.0, 3.0]


def test_fetch_source_requires_ext_id() -> None:
    wk, _ = make_worker(FakeClient())
    with pytest.raises(ValueError, match="ext_id"):
        asyncio.run(wk._handle_fetch_source(b"{}"))


def test_parse_blob_remaps_archived_envelope(uploads: list[bytes], monkeypatch: pytest.MonkeyPatch) -> None:
    client = FakeClient()

    async def fake_fetch(nc: object, url: str, fallback: str) -> dict[str, Any]:
        return {"activity": client.get_activity("7"), "details": client.get_activity_details("7")}

    monkeypatch.setattr(archive, "fetch", fake_fetch)
    wk, _ = make_worker()
    job = {"ext_id": "7", "user_id": "u1", "blob": {"url": "https://s3/x", "fallback_handle": "raw/7.json"}}
    asyncio.run(wk._handle_parse_blob(json.dumps(job).encode()))

    act = json_format.Parse(uploads[0], w.JobResult()).events[0].activity
    assert act.raw_blob_id == "raw/7.json"
    assert act.stream.sample_count == 2


def test_import_metrics_emits_one_event_per_day(uploads: list[bytes]) -> None:
    client = FakeClient()
    wk, _ = make_worker(client)
    day = 86_400
    job = {"account_id": "acc-1", "user_id": "u1", "since_unix": 0, "until_unix": 2 * day}
    asyncio.run(wk._handle_import_metrics(json.dumps(job).encode()))

    assert client.days == ["1970-01-01", "1970-01-02", "1970-01-03"]
    events = json_format.Parse(uploads[0], w.JobResult()).events
    assert [e.metric.key for e in events] == ["Steps"] * 3


def test_import_metrics_without_data_publishes_nothing() -> None:
    class Empty(FakeClient):
        def daily_health(self, day: str) -> dict[str, float]:
            return {}

    wk, js = make_worker(Empty())
    asyncio.run(wk._handle_import_metrics(json.dumps({"account_id": "acc-1"}).encode()))
    assert js.published == []


@pytest.mark.parametrize("body", [b"not json", json.dumps({"user_id": "u1"}).encode()])
def test_failure_envelope_needs_a_job_with_ext_id(body: bytes) -> None:
    wk, js = make_worker()
    asyncio.run(wk._publish_failure("cairn.jobs.fetch_source.garmin", body, RuntimeError("x")))
    assert js.published == []


def test_consume_settles_each_message() -> None:
    wk, js = make_worker()
    ok, retry, dead = FakeMsg(b'{"ok": true}'), FakeMsg(b"{}"), FakeMsg(b'{"ext_id": "9"}', wk.MAX_DELIVERIES)
    js.psub = FakePullSub([RuntimeError("flaky"), [ok, retry, dead]], wk.stop)

    async def handler(body: bytes) -> None:
        if not json.loads(body).get("ok"):
            raise RuntimeError("boom")

    async def run() -> None:
        wk.ACK_EXTEND_S = 0
        await wk._consume(C.SUBJ_FETCH, "fetch", handler)

    asyncio.run(run())
    assert ok.settled[-1] == "ack"
    assert retry.settled[-1] == f"nak:{wk.NAK_DELAY_S}"
    assert dead.settled[-1] == "term"
    (failure,) = results(js, C.RESULT_SUBJECT)
    assert failure.failed_ref.external_id == "9"


def test_heartbeat_publishes_presence() -> None:
    wk, js = make_worker()
    js.kv = FakeKV(wk.stop)
    asyncio.run(wk._heartbeat_loop())
    ((key, payload),) = js.kv.puts
    assert key == f"{C.WORKER_NAME}.{wk.cfg.instance_id}"
    assert payload["capabilities"]["HRV"]["read"] is True
    assert payload["worker_key"] == wk.worker_key


def test_unconnected_worker_refuses_io() -> None:
    wk = runtime.Worker(C.Config())
    with pytest.raises(RuntimeError, match="NATS"):
        _ = wk._nats
    with pytest.raises(RuntimeError, match="JetStream"):
        _ = wk._js
