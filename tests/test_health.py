"""Pure health-extraction tests (cairn_garmin.garmin_client.extract_daily_health)."""

from cairn_garmin.garmin_client import (
    _latest_weight_kg,
    _sum_steps,
    extract_daily_health,
)


def test_full_extraction() -> None:
    out = extract_daily_health(
        hrv={"hrvSummary": {"lastNightAvg": 62}},
        sleep={"dailySleepDTO": {"sleepTimeSeconds": 27000}},
        rhr={"restingHeartRate": 48},
        steps={"totalSteps": 8421},
        wt={"dateWeightList": [{"weight": 81000}]},
    )
    assert out == {
        "HRV": 62.0,
        "Sleep": 27000.0,
        "RestingHR": 48.0,
        "Steps": 8421.0,
        "Weight": 81.0,
    }


def test_resting_hr_fallback_to_wellness_map() -> None:
    # Direct restingHeartRate absent → fall back to the WELLNESS map (real bug fix).
    out = extract_daily_health(
        hrv=None,
        sleep=None,
        steps=None,
        wt=None,
        rhr={"allMetrics": {"metricsMap": {"WELLNESS_RESTING_HEART_RATE": [{"value": 51}]}}},
    )
    assert out == {"RestingHR": 51.0}


def test_missing_metrics_are_omitted() -> None:
    assert extract_daily_health(hrv=None, sleep=None, rhr=None, steps=None, wt=None) == {}
    # Present-but-empty shapes must not produce keys.
    assert (
        extract_daily_health(
            hrv={},
            sleep={"dailySleepDTO": {}},
            rhr={},
            steps=[],
            wt={},
        )
        == {}
    )


def test_steps_list_sums_intervals() -> None:
    assert _sum_steps([{"steps": 100}, {"steps": 250}, {"steps": 0}]) == 350
    assert _sum_steps({"totalSteps": 999}) == 999
    assert _sum_steps([]) is None  # 0 total → omitted
    assert _sum_steps(None) is None


def test_weight_grams_to_kg() -> None:
    assert _latest_weight_kg({"dateWeightList": [{"weight": 75500}]}) == 75.5
    # latest entry wins (last in the list)
    assert _latest_weight_kg({"dateWeightList": [{"weight": 80000}, {"weight": 79250}]}) == 79.25
    # totalAverage fallback when no per-day rows
    assert _latest_weight_kg({"totalAverage": {"weight": 70000}}) == 70.0
    assert _latest_weight_kg({}) is None
