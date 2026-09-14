"""Shared fakes for runtime tests: an in-memory JetStream stub and a Worker
built without a NATS connection."""
from cairn_garmin import runtime


class FakeJS:
    """Records (subject, data, headers) for every publish."""

    def __init__(self):
        self.published = []

    async def publish(self, subject, data, headers=None):
        self.published.append((subject, data, headers or {}))


def make_worker(client=None, account_id="acc-1") -> runtime.Worker:
    wk = runtime.Worker.__new__(runtime.Worker)
    wk.js = FakeJS()
    wk.nc = object()
    wk._clients = {account_id: client} if client is not None else {}
    wk._reconciled_at = {}
    return wk
