"""GarminClient: token-store resume, fresh-login token dump, metric error handling."""

from types import SimpleNamespace
from typing import Any, ClassVar

import pytest
from garminconnect import GarminConnectAuthenticationError

from cairn_garmin import garmin_client
from cairn_garmin.garmin_client import GarminClient, _http_status, _safe


class FakeStore:
    def __init__(self, fail: bool = False) -> None:
        self.fail = fail
        self.dumped: list[str] = []

    def dump(self, path: str) -> None:
        if self.fail:
            raise OSError("read-only")
        self.dumped.append(path)


class FakeGarmin:
    """Records logins; a tokenstore login fails unless `resume` is set."""

    instances: ClassVar[list[FakeGarmin]] = []
    resume = True
    dump_fails = False

    def __init__(self, email: str, password: str) -> None:
        self.logins: list[str | None] = []
        self.client = FakeStore(self.dump_fails)
        FakeGarmin.instances.append(self)

    def login(self, tokenstore: str | None = None) -> None:
        self.logins.append(tokenstore)
        if tokenstore and not self.resume:
            raise FileNotFoundError(tokenstore)

    def get_activities(self, start: int, limit: int) -> Any:
        return [{"activityId": 1}, "junk"]

    def get_activity(self, activity_id: str) -> dict[str, Any]:
        return {"activityId": activity_id}

    def get_activity_details(self, activity_id: str) -> dict[str, Any]:
        return {"metricDescriptors": []}

    def get_hrv_data(self, day: str) -> dict[str, Any]:
        return {"hrvSummary": {"lastNightAvg": 60}}

    def get_sleep_data(self, day: str) -> dict[str, Any]:
        raise RuntimeError("no sleep data")

    def get_rhr_day(self, day: str) -> dict[str, Any]:
        return {"restingHeartRate": 50}

    def get_steps_data(self, day: str) -> list[dict[str, Any]]:
        return [{"steps": 10}, {"steps": 5}]

    def get_body_composition(self, start: str, end: str) -> dict[str, Any]:
        return {"dateWeightList": [{"weight": 80000}]}


@pytest.fixture(autouse=True)
def fake_garmin(monkeypatch: pytest.MonkeyPatch) -> None:
    FakeGarmin.instances = []
    FakeGarmin.resume = True
    FakeGarmin.dump_fails = False
    monkeypatch.setattr(garmin_client, "Garmin", FakeGarmin)


def test_resumes_cached_tokens_once() -> None:
    c = GarminClient("e", "p", "/tokens/acc")
    c.get_activity("1")
    c.get_activity_details("1")
    (api,) = FakeGarmin.instances
    assert api.logins == ["/tokens/acc"]
    assert api.client.dumped == []


def test_fresh_login_persists_tokens() -> None:
    FakeGarmin.resume = False
    GarminClient("e", "p", "/tokens/acc").get_activity("1")
    (api,) = FakeGarmin.instances
    assert api.logins == ["/tokens/acc", None]
    assert api.client.dumped == ["/tokens/acc"]


def test_token_dump_failure_is_not_fatal() -> None:
    FakeGarmin.resume = False
    FakeGarmin.dump_fails = True
    assert GarminClient("e", "p", "/ro").get_activity("7") == {"activityId": "7"}


def test_list_activities_keeps_dicts_only() -> None:
    assert GarminClient("e", "p", "/t").list_activities() == [{"activityId": 1}]


def test_daily_health_skips_failed_metrics() -> None:
    out = GarminClient("e", "p", "/t").daily_health("2026-01-01")
    assert out == {"HRV": 60.0, "RestingHR": 50.0, "Steps": 15.0, "Weight": 80.0}


def _http_error(status: int, wrapped: bool) -> Exception:
    e = RuntimeError("http")
    resp = SimpleNamespace(status_code=status)
    if wrapped:
        e.error = SimpleNamespace(response=resp)  # type: ignore[attr-defined]
    else:
        e.response = resp  # type: ignore[attr-defined]
    return e


def test_http_status_reads_wrapped_and_direct_errors() -> None:
    assert _http_status(_http_error(429, wrapped=True)) == 429
    assert _http_status(_http_error(404, wrapped=False)) == 404
    assert _http_status(RuntimeError("plain")) is None


def _raise(e: Exception) -> None:
    raise e


@pytest.mark.parametrize(
    "err",
    [GarminConnectAuthenticationError("expired"), _http_error(401, wrapped=True), _http_error(403, wrapped=False)],
)
def test_safe_surfaces_auth_failures(err: Exception) -> None:
    with pytest.raises(type(err)):
        _safe(lambda: _raise(err))


def test_safe_maps_other_failures_to_none() -> None:
    assert _safe(lambda: _raise(_http_error(500, wrapped=False))) is None
    assert _safe(lambda: 3) == 3
