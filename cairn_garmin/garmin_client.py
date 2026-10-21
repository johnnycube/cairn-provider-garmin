"""Thin wrapper over garminconnect with token-store resume.

Garmin has no public activity OAuth API; garminconnect uses Garth SSO
(email/password → cached OAuth1/2 tokens). Tokens are persisted under garth_home
so we don't re-login per job. MFA accounts need a one-time interactive login to
seed the token store.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from typing import Any

from garminconnect import Garmin, GarminConnectAuthenticationError

log = logging.getLogger("cairn.garmin")

JSON = dict[str, Any]


class GarminClient:
    def __init__(self, email: str, password: str, garth_home: str) -> None:
        self._email = email
        self._password = password
        self._garth_home = garth_home
        self._api: Garmin | None = None

    def _client(self) -> Garmin:
        if self._api is not None:
            return self._api
        api = Garmin(self._email, self._password)
        try:
            api.login(self._garth_home)  # resume cached tokens if present
        except Exception:  # noqa: BLE001
            api.login()  # fresh SSO
            try:
                api.client.dump(self._garth_home)
            except Exception as e:  # noqa: BLE001
                log.warning("could not persist Garmin tokens to %s (next job logs in again): %s", self._garth_home, e)
        self._api = api
        return api

    def list_activities(self, start: int = 0, limit: int = 50) -> list[JSON]:
        acts = self._client().get_activities(start, limit)
        return [a for a in acts if isinstance(a, dict)] if isinstance(acts, list) else []

    def get_activity(self, activity_id: str) -> JSON:
        return self._client().get_activity(activity_id)

    def get_activity_details(self, activity_id: str) -> JSON:
        # maxchart/maxpoly default to full resolution.
        return self._client().get_activity_details(activity_id)

    # --- gear ---
    def _profile_number(self) -> str:
        api = self._client()
        pid = api.profile_id or (api.get_user_profile() or {}).get("id")
        if not pid:
            raise RuntimeError("garmin profile id unavailable")
        return str(pid)

    def gear(self) -> list[JSON]:
        """The account's gear list, retired included."""
        return _as_list(self._client().get_gear(self._profile_number()))

    def gear_defaults(self) -> list[JSON]:
        """Per-activity-type default gear entries."""
        return _as_list(self._client().get_gear_defaults(self._profile_number()))

    def activity_gear(self, activity_id: str) -> list[JSON]:
        """Gear recorded on one activity (usually zero or one item)."""
        return _as_list(self._client().get_activity_gear(activity_id))

    # --- health metrics (daily) ---
    def hrv(self, day: str) -> JSON | None:
        return _safe(lambda: self._client().get_hrv_data(day))

    def sleep(self, day: str) -> JSON | None:
        return _safe(lambda: self._client().get_sleep_data(day))

    def resting_hr(self, day: str) -> JSON | None:
        return _safe(lambda: self._client().get_rhr_day(day))

    def steps(self, day: str) -> list[JSON] | None:
        return _safe(lambda: self._client().get_steps_data(day))

    def weight(self, start: str, end: str) -> JSON | None:
        return _safe(lambda: self._client().get_body_composition(start, end))

    def daily_health(self, day: str) -> dict[str, float]:
        """Return {canonical DataType: scalar} for one YYYY-MM-DD."""
        return extract_daily_health(
            hrv=self.hrv(day),
            sleep=self.sleep(day),
            rhr=self.resting_hr(day),
            steps=self.steps(day),
            wt=self.weight(day, day),
        )


def extract_daily_health(
    *,
    hrv: JSON | None,
    sleep: JSON | None,
    rhr: JSON | None,
    steps: list[JSON] | JSON | None,
    wt: JSON | None,
) -> dict[str, float]:
    """Pure extraction of {canonical DataType: scalar} from raw Garmin responses.

    Defensive — Garmin response shapes vary by version; missing metrics are
    simply omitted.
    """
    out: dict[str, float] = {}
    if hrv and (v := _dig(hrv, ["hrvSummary", "lastNightAvg"])) is not None:
        out["HRV"] = float(v)
    if sleep and (v := _dig(sleep, ["dailySleepDTO", "sleepTimeSeconds"])) is not None:
        out["Sleep"] = float(v)
    if rhr:
        v = _dig(rhr, ["restingHeartRate"])
        if v is None:
            rows = _dig(rhr, ["allMetrics", "metricsMap", "WELLNESS_RESTING_HEART_RATE"])
            if isinstance(rows, list) and rows and isinstance(rows[0], dict):
                v = rows[0].get("value")
        if isinstance(v, (int, float)):
            out["RestingHR"] = float(v)
    total = _sum_steps(steps)
    if total is not None:
        out["Steps"] = float(total)
    if wt and (v := _latest_weight_kg(wt)) is not None:
        out["Weight"] = v
    return out


def _as_list(raw: object) -> list[JSON]:
    """The gear endpoints are typed as dicts but return lists (or a dict wrapping one)."""
    if isinstance(raw, list):
        return [x for x in raw if isinstance(x, dict)]
    if isinstance(raw, dict):
        for v in raw.values():
            if isinstance(v, list):
                return [x for x in v if isinstance(x, dict)]
        return [raw] if raw else []
    return []


def _dig(d: Any, path: list[str]) -> Any:
    cur = d
    for k in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return cur


def _sum_steps(steps: object) -> int | None:
    if isinstance(steps, list):
        total = sum(int(s.get("steps", 0)) for s in steps if isinstance(s, dict))
        return total or None
    if isinstance(steps, dict):
        v = steps.get("totalSteps") or steps.get("steps")
        return int(v) if isinstance(v, (int, float)) else None
    return None


def _latest_weight_kg(wt: JSON) -> float | None:
    rows = wt.get("dateWeightList") or wt.get("dailyWeightSummaries") or []
    grams = None
    if rows and isinstance(rows, list):
        last = rows[-1]
        grams = last.get("weight") if isinstance(last, dict) else None
    if grams is None:
        grams = _dig(wt, ["totalAverage", "weight"])
    return round(float(grams) / 1000.0, 2) if isinstance(grams, (int, float)) else None


def _http_status(e: Exception) -> int | None:
    # garth wraps the requests error in .error; garminconnect >= 0.3 and
    # requests expose .response directly. Explicit None checks: a non-2xx
    # requests.Response is falsy.
    resp = getattr(getattr(e, "error", None), "response", None)
    if resp is None:
        resp = getattr(e, "response", None)
    return getattr(resp, "status_code", None)


def _safe[T](fn: Callable[[], T]) -> T | None:
    """Treat a failed metric call as "no data" — except auth failures, which
    must surface so the job fails instead of importing an empty day."""
    try:
        return fn()
    except GarminConnectAuthenticationError:
        raise
    except Exception as e:
        status = _http_status(e)
        if status in (401, 403):
            raise
        log.debug("garmin metric call failed (status %s): %s", status, e)
        return None
