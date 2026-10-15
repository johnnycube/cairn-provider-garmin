"""Shared fakes for runtime tests: in-memory NATS/JetStream stubs and a Worker
built without a NATS connection."""

import json
from collections.abc import Callable
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, cast

from nats.aio.client import Client as NATS
from nats.errors import TimeoutError as NatsTimeout
from nats.js import JetStreamContext

from cairn_garmin import config as C
from cairn_garmin import runtime
from cairn_garmin.garmin_client import GarminClient

Published = tuple[str, bytes, dict[str, str]]


class FakeKV:
    def __init__(self, on_put: Callable[[], None]) -> None:
        self.puts: list[tuple[str, dict[str, Any]]] = []
        self.on_put = on_put

    async def put(self, key: str, value: bytes) -> None:
        self.puts.append((key, json.loads(value)))
        self.on_put()


class FakeMsg:
    """A JetStream message that records how it was settled."""

    def __init__(self, data: bytes, num_delivered: int = 1) -> None:
        self.data = data
        self.metadata = SimpleNamespace(num_delivered=num_delivered)
        self.settled: list[str] = []

    async def ack(self) -> None:
        self.settled.append("ack")

    async def nak(self, delay: float | None = None) -> None:
        self.settled.append(f"nak:{delay}")

    async def term(self) -> None:
        self.settled.append("term")

    async def in_progress(self) -> None:
        self.settled.append("in_progress")


class FakePullSub:
    """Hands out queued batches, then calls `on_drained` and times out."""

    def __init__(self, batches: list[list[FakeMsg] | Exception], on_drained: Callable[[], None]) -> None:
        self.batches = batches
        self.on_drained = on_drained

    async def fetch(self, batch: int, **_: Any) -> list[FakeMsg]:
        if not self.batches:
            self.on_drained()
            raise NatsTimeout
        b = self.batches.pop(0)
        if isinstance(b, Exception):
            raise b
        return b


class FakeJS:
    """Records (subject, data, headers) for every publish; serves a KV bucket and pull subscriptions."""

    def __init__(self) -> None:
        self.published: list[Published] = []
        self.kv: FakeKV | None = None
        self.psub: FakePullSub | None = None

    async def publish(self, subject: str, data: bytes, headers: dict[str, str] | None = None) -> None:
        self.published.append((subject, data, headers or {}))

    async def key_value(self, bucket: str) -> FakeKV:
        assert self.kv is not None
        return self.kv

    async def pull_subscribe(self, subject: str, **_: Any) -> FakePullSub:
        assert self.psub is not None
        return self.psub


@dataclass
class Reply:
    data: bytes


class FakeNC:
    """Request/reply stub: answers each subject with a canned JSON object, or raises it."""

    def __init__(self, replies: dict[str, dict[str, Any] | Exception] | None = None) -> None:
        self.replies = replies or {}
        self.requests: list[tuple[str, dict[str, Any]]] = []

    async def request(self, subject: str, payload: bytes, **_: Any) -> Reply:
        self.requests.append((subject, json.loads(payload)))
        reply = self.replies.get(subject)
        if reply is None:
            raise TimeoutError(subject)
        if isinstance(reply, Exception):
            raise reply
        return Reply(json.dumps(reply).encode())


def as_nats(nc: FakeNC) -> NATS:
    return cast(NATS, nc)


def make_worker(
    client: object | None = None,
    account_id: str = "acc-1",
    nc: FakeNC | None = None,
    cfg: C.Config | None = None,
) -> tuple[runtime.Worker, FakeJS]:
    """A Worker wired to a FakeJS; `client` duck-types GarminClient."""
    js = FakeJS()
    wk = runtime.Worker(cfg or C.Config(garmin_email="", garmin_password="", garth_home="/nonexistent"))
    wk.js = cast(JetStreamContext, js)
    wk.nc = as_nats(nc or FakeNC())
    wk._clients = {account_id: cast(GarminClient, client)} if client is not None else {}
    return wk, js
