"""The worker's real NATS operations against a nats-server that grants exactly
cairn-core's StandardPermissionTemplate (auth-callout), so a subject the
template lacks fails here instead of in production."""

import asyncio
import json
import logging
import os
import shutil
import socket
import subprocess
import threading
import time
from collections.abc import Awaitable, Callable, Iterator
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, ClassVar, cast

import nats
import pytest
from nats.aio.client import Client as NATS
from nats.aio.msg import Msg
from nats.js.api import RetentionPolicy, StreamConfig

from cairn_garmin import config as C
from cairn_garmin import runtime
from cairn_garmin.garmin_client import GarminClient

PROVIDER = C.PROVIDER
WORKER_KEY = f"{C.WORKER_NAME}-{PROVIDER}"
ACCOUNT = "acc-1"
JOB_STREAM, WEBHOOK_STREAM = "CAIRN_JOBS", "CAIRN_WEBHOOKS"
BUCKETS = ["cairn_worker_presence", "cairn_worker_manifests", "cairn_rate_limits"]


def standard_template(p: str, wk: str) -> tuple[list[str], list[str]]:
    """Mirror of cairn-core domain.StandardPermissionTemplate(p, wk); keep in sync."""
    jobs = [f"cairn.jobs.{t}.{p}" for t in ("fetch_source", "parse_blob", "backfill", "reconcile", "import_metrics")]
    webhook = f"cairn.webhooks.{wk}.event"
    js = ["$JS.API.STREAM.NAMES"]
    js += [f"$JS.API.CONSUMER.CREATE.{JOB_STREAM}.*.{f}" for f in jobs]
    js += [f"$JS.API.CONSUMER.DURABLE.CREATE.{JOB_STREAM}.*", f"$JS.API.CONSUMER.CREATE.{WEBHOOK_STREAM}.*.{webhook}"]
    for st in (JOB_STREAM, WEBHOOK_STREAM):
        js += [f"$JS.API.CONSUMER.INFO.{st}.*", f"$JS.API.CONSUMER.MSG.NEXT.{st}.*", f"$JS.ACK.{st}.>"]
    for b in BUCKETS:
        js += [f"$JS.API.STREAM.INFO.KV_{b}", f"$JS.API.DIRECT.GET.KV_{b}.>", f"$JS.API.STREAM.MSG.GET.KV_{b}"]
        js += [f"$KV.{b}.>"]
    publish = [
        f"cairn.results.fetch_source.{p}",
        f"cairn.results.parse_blob.{p}",
        f"cairn.results.backfill.{p}",
        f"cairn.results.reconcile.{p}.*",
        f"cairn.results.import_metrics.{p}",
        f"cairn.jobs.fetch_source.{p}",
        f"cairn.workers.{wk}.>",
        f"cairn.tokens.{p}.>",
        f"cairn.creds.{p}.get",
        f"cairn.blobs.presign_upload.{p}",
        f"cairn.blobs.presign_download.{p}",
        "cairn.accounts.lookup_by_provider_ext",
        "_INBOX.>",
        *js,
    ]
    subscribe = [*jobs, f"cairn.cmd.worker.{wk}.>", f"cairn.discover.{p}", webhook, f"cairn.webhooks.{wk}.verify"]
    return publish, [*subscribe, "_INBOX.>"]


def _nats_server_bin() -> str:
    found = shutil.which("nats-server")
    gobin = Path(os.environ.get("GOPATH", Path.home() / "go")) / "bin" / "nats-server"
    if found:
        return found
    if gobin.exists():
        return str(gobin)
    if os.environ.get("CI"):
        pytest.fail("nats-server not installed; run `make tools`")
    pytest.skip("nats-server not installed; run `make tools`")


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


@pytest.fixture
def nats_url(tmp_path: Path) -> Iterator[str]:
    publish, subscribe = standard_template(PROVIDER, WORKER_KEY)
    port = _free_port()
    conf = {
        "host": "127.0.0.1",
        "port": port,
        "jetstream": {"store_dir": str(tmp_path / "js")},
        "authorization": {
            "users": [
                {"user": "admin", "password": "admin"},
                {
                    "user": "worker",
                    "password": "worker",
                    "permissions": {"publish": {"allow": publish}, "subscribe": {"allow": subscribe}},
                },
            ]
        },
    }
    path = tmp_path / "nats.conf"
    path.write_text(json.dumps(conf))
    proc = subprocess.Popen([_nats_server_bin(), "-c", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # noqa: S603
    deadline = time.monotonic() + 10
    while True:
        try:
            socket.create_connection(("127.0.0.1", port), timeout=0.2).close()
            break
        except OSError:
            if time.monotonic() > deadline or proc.poll() is not None:
                proc.kill()
                pytest.fail("nats-server did not start")
            time.sleep(0.05)
    yield f"nats://127.0.0.1:{port}"
    proc.terminate()
    proc.wait(timeout=10)


class BlobStore(BaseHTTPRequestHandler):
    """Stands in for S3 behind the presigned URLs."""

    blobs: ClassVar[dict[str, bytes]] = {}

    def do_PUT(self) -> None:
        self.blobs[self.path] = self.rfile.read(int(self.headers["Content-Length"]))
        self.send_response(200)
        self.end_headers()

    def do_GET(self) -> None:
        body = self.blobs.get(self.path)
        self.send_response(200 if body is not None else 404)
        self.end_headers()
        self.wfile.write(body or b"")

    def log_message(self, *_: Any) -> None:
        pass


@pytest.fixture
def blob_url() -> Iterator[str]:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), BlobStore)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()


class RecentClient:
    """Garmin API stand-in with one activity inside the reconcile window."""

    def __init__(self) -> None:
        self.start_ms = int(datetime.now(UTC).timestamp() * 1000) - 3_600_000

    def list_activities(self, start: int, limit: int) -> list[dict[str, Any]]:
        return [] if start else [{"activityId": 7, "beginTimestamp": self.start_ms}]

    def get_activity(self, ext_id: str) -> dict[str, Any]:
        return {"activityId": ext_id, "beginTimestamp": self.start_ms, "activityType": {"typeKey": "running"}}

    def get_activity_details(self, ext_id: str) -> dict[str, Any]:
        return {
            "metricDescriptors": [{"key": "directTimestamp", "metricsIndex": 0}],
            "activityDetailMetrics": [{"metrics": [self.start_ms]}],
        }

    def daily_health(self, day: str) -> dict[str, float]:
        return {"Steps": 100.0}


async def _until(cond: Callable[[], Awaitable[bool]], what: str) -> None:
    try:
        async with asyncio.timeout(15):
            while True:
                if await cond():
                    return
                await asyncio.sleep(0.05)
    except TimeoutError:
        raise AssertionError(f"timed out waiting for {what}") from None


async def _admin(url: str, blob_url: str) -> tuple[NATS, list[str], list[bytes]]:
    """Bootstrap streams/KV like core and serve the server-side request/reply subjects."""
    nc = await nats.connect(url, user="admin", password="admin")
    js = nc.jetstream()
    await js.add_stream(StreamConfig(name=JOB_STREAM, subjects=["cairn.jobs.>"], retention=RetentionPolicy.WORK_QUEUE))
    await js.add_stream(StreamConfig(name="CAIRN_RESULTS", subjects=["cairn.results.>"]))
    await js.create_key_value(bucket="cairn_worker_presence")
    results: list[str] = []
    bodies: list[bytes] = []
    n = 0

    async def on_result(m: Msg) -> None:
        results.append(m.subject)
        bodies.append(m.data)

    async def presign(m: Msg) -> None:
        nonlocal n
        n += 1
        await m.respond(json.dumps({"url": f"{blob_url}/b{n}", "blob_id": f"b{n}"}).encode())

    async def presign_download(m: Msg) -> None:
        await m.respond(json.dumps({"url": f"{blob_url}/{json.loads(m.data)['blob_id']}"}).encode())

    async def creds(m: Msg) -> None:
        await m.respond(json.dumps({"email": "e@x", "password": "pw"}).encode())

    await nc.subscribe("cairn.results.>", cb=on_result)
    await nc.subscribe(f"cairn.blobs.presign_upload.{PROVIDER}", cb=presign)
    await nc.subscribe(f"cairn.blobs.presign_download.{PROVIDER}", cb=presign_download)
    await nc.subscribe(f"cairn.creds.{PROVIDER}.get", cb=creds)
    await nc.flush()
    return nc, results, bodies


def _violations(caplog: pytest.LogCaptureFixture) -> list[str]:
    return [r.getMessage() + str(r.exc_info) for r in caplog.records if "ermission" in str(r.exc_info) + r.getMessage()]


def test_worker_runs_under_standard_template(nats_url: str, blob_url: str, caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG)

    async def scenario() -> None:
        admin, results, _ = await _admin(nats_url, blob_url)
        ajs = admin.jetstream()
        wk = runtime.Worker(
            C.Config(nats_url=nats_url, nats_user="worker", nats_password="worker", garth_home="/nonexistent")
        )
        wk.MAX_DELIVERIES = 1
        wk._clients = {ACCOUNT: cast(GarminClient, RecentClient())}
        run = asyncio.create_task(wk.run())

        async def consumers_ready() -> bool:
            names = {c.name for c in await ajs.consumers_info(JOB_STREAM)}
            return names >= {f"garmin-{s}" for s in ("fetch", "metrics", "parseblob", "reconcile")}

        await _until(consumers_ready, "durable consumers")
        presence = await ajs.key_value("cairn_worker_presence")

        async def heartbeat() -> bool:
            try:
                await presence.get(f"{C.WORKER_NAME}.{wk.cfg.instance_id}")
            except Exception:  # noqa: BLE001
                return False
            return True

        await _until(heartbeat, "presence heartbeat")

        reply = await admin.request(f"cairn.discover.{PROVIDER}", json.dumps({"account_id": ACCOUNT}).encode(), 5)
        assert json.loads(reply.data)["items"][0]["external_id"] == "7"
        assert await wk._fetch_creds(ACCOUNT) == ("e@x", "pw")

        job = {"job_id": "j1", "account_id": ACCOUNT, "user_id": "u1", "provider": PROVIDER}
        # reconcile enqueues fetch_source for activity 7, whose result is claim-checked.
        await ajs.publish(f"cairn.jobs.reconcile.{PROVIDER}", json.dumps(job).encode())
        now = int(time.time())
        await ajs.publish(
            f"cairn.jobs.import_metrics.{PROVIDER}", json.dumps({**job, "since_unix": now, "until_unix": now}).encode()
        )
        await ajs.publish(f"cairn.jobs.fetch_source.{PROVIDER}", json.dumps(job).encode())  # no ext_id → term

        async def all_results() -> bool:
            return {
                f"cairn.results.reconcile.{PROVIDER}.{ACCOUNT}",
                f"cairn.results.fetch_source.{PROVIDER}",
                f"cairn.results.import_metrics.{PROVIDER}",
            } <= set(results)

        await _until(all_results, "results")

        # parse_blob re-presigns the archived blob from its handle (the first upload).
        blob = {"url": "", "fallback_handle": "b1"}
        await ajs.publish(
            f"cairn.jobs.parse_blob.{PROVIDER}", json.dumps({**job, "ext_id": "7", "blob": blob}).encode()
        )

        async def reparsed() -> bool:
            return results.count(f"cairn.results.fetch_source.{PROVIDER}") >= 2

        await _until(reparsed, "parse_blob result")

        async def drained() -> bool:
            return (await ajs.stream_info(JOB_STREAM)).state.messages == 0

        await _until(drained, "acked jobs")
        wk.stop()
        await asyncio.wait_for(run, 15)
        await admin.close()

    asyncio.run(scenario())
    assert _violations(caplog) == []


def test_template_rejects_foreign_subjects(nats_url: str, caplog: pytest.LogCaptureFixture) -> None:
    """Control: the server really enforces the template."""

    async def scenario() -> None:
        nc = await nats.connect(nats_url, user="worker", password="worker")
        await nc.publish(f"cairn.jobs.reconcile.{PROVIDER}", b"{}")
        await nc.publish("cairn.creds.strava.get", b"{}")
        await nc.flush()
        await asyncio.sleep(0.3)
        await nc.close()

    asyncio.run(scenario())
    assert len(_violations(caplog)) == 2
