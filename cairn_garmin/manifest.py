"""Garmin capability manifest (advertised in the presence heartbeat).

Garmin's value over Strava is health data: HRV, sleep, weight, steps, resting HR.
Keys are canonical DataType identifiers (internal/domain/capability).
"""

from __future__ import annotations


def manifest() -> dict[str, dict[str, bool | str]]:
    return {
        "Activity": {"read": True, "backfill": True, "granularity": "per-activity"},
        "HRV": {"read": True, "backfill": True, "granularity": "daily"},
        "Sleep": {"read": True, "backfill": True, "granularity": "daily"},
        "Weight": {"read": True, "backfill": True, "granularity": "daily"},
        "Steps": {"read": True, "backfill": True, "granularity": "daily"},
        "RestingHR": {"read": True, "backfill": True, "granularity": "daily"},
        "Gear": {"read": True, "backfill": True, "granularity": "per-account"},
    }
