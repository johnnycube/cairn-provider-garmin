"""Claim-check publish path: event-carrying results spill to the blob store
and publish a payload_ref envelope; terminal failures publish a failure
envelope so the server fails the queue item with the true reason."""
import asyncio
import hashlib
import json

from google.protobuf import json_format

import cairn_garmin  # noqa: F401 (proto path bootstrap)
from cairn.worker.v1 import worker_service_pb2 as w
from cairn_garmin import runtime
from conftest import make_worker


def test_publish_result_claim_checks_events(monkeypatch):
    wk = make_worker()
    uploaded = {}

    async def fake_upload(nc, body):
        uploaded["body"] = body
        return {"blob_id": "transfer/garmin/x.json", "size": len(body),
                "sha256": hashlib.sha256(body).hexdigest()}

    monkeypatch.setattr(runtime.archive, "upload_result", fake_upload)

    jr = w.JobResult(
        worker_name="garmin-fetcher",
        events=[w.WorkerEvent(type=w.WORKER_EVENT_TYPE_ACTIVITY)],
    )
    asyncio.run(wk._publish_result("cairn.results.fetch_source.garmin", jr))

    ((subject, data, _),) = wk.js.published
    assert subject == "cairn.results.fetch_source.garmin"
    env = json_format.Parse(data, w.JobResult())
    assert env.payload_ref.blob_id == "transfer/garmin/x.json"
    assert env.payload_ref.size_bytes == len(uploaded["body"])
    assert not env.events

    full = json_format.Parse(uploaded["body"], w.JobResult())
    assert len(full.events) == 1


def test_publish_result_inline_when_no_events():
    wk = make_worker()
    jr = w.JobResult(worker_name="garmin-fetcher")
    asyncio.run(wk._publish_result("cairn.results.fetch_source.garmin", jr))

    ((_, data, _),) = wk.js.published
    env = json_format.Parse(data, w.JobResult())
    assert not env.HasField("payload_ref")


def test_publish_failure_envelope():
    wk = make_worker()
    body = json.dumps({"ext_id": "99", "account_id": "a1", "user_id": "u1"}).encode()
    asyncio.run(wk._publish_failure("cairn.jobs.fetch_source.garmin", body, RuntimeError("boom")))

    ((subject, data, _),) = wk.js.published
    assert subject == "cairn.results.fetch_source.garmin"
    env = json_format.Parse(data, w.JobResult())
    assert env.failed_ref.external_id == "99"
    assert env.failed_ref.external_account_id == "a1"
    assert env.error.message == "boom"
    assert env.error.code == "RuntimeError"
