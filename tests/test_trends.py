from datetime import datetime, timedelta, timezone

import pytest

from radar.analysis.trends import compute_trends
from radar.contracts import Document, Observation

CUTOFF = datetime(2026, 10, 18, tzinfo=timezone.utc)


def document(index, days=1, title="Robot learning", **updates):
    stamp = CUTOFF - timedelta(days=days)
    data = dict(id=str(index), source="arxiv", source_id=str(index),
                canonical_id=str(index), title=title, abstract=None,
                url=f"https://example.org/{index}", version=None,
                published_at=stamp, first_public_at=stamp,
                observed_at=stamp, available_at=stamp, status="preprint")
    data.update(updates)
    return Document(**data)


def observation(entity, value, days=0, coverage="robotics-v1", **updates):
    stamp = CUTOFF - timedelta(days=days)
    data = dict(entity_id=entity, metric="count_28d", value=value,
                available_at=stamp, observed_at=stamp, source="arxiv",
                coverage_id=coverage, state="ok")
    data.update(updates)
    return Observation(**data)


def snapshots(current_coverage="robotics-v1"):
    return [observation("robot-learning", 2, coverage=current_coverage),
            observation("__all__", 10, coverage=current_coverage),
            observation("robot-learning", 1, days=28),
            observation("__all__", 10, days=28)]


def test_share_denominator_same_coverage():
    trend = compute_trends([], snapshots(), CUTOFF)[0]
    assert trend.count_28d == 2
    assert trend.share_28d == .2
    assert trend.share_change == pytest.approx(.1)
    assert compute_trends([], snapshots("robotics-v2"), CUTOFF)[0].share_change is None


def test_missing_is_not_decline():
    items = [observation("robot-learning", None, state="missing"), observation("__all__", 10)]
    trend = compute_trends([], items, CUTOFF)[0]
    assert trend.support == "missing"
    assert trend.share_28d is None and trend.share_change is None
    items[0] = observation("robot-learning", 4)
    assert compute_trends([], items, CUTOFF)[0].support == "low_support"


def test_future_feature_ignored():
    original = snapshots()
    future = [observation("robot-learning", 100, days=-1), observation("__all__", 100, days=-1)]
    assert compute_trends([], original, CUTOFF) == compute_trends([], original + future, CUTOFF)


def test_denominator_requires_same_source_coverage_and_snapshot():
    for change in ({"source": "openalex"}, {"coverage_id": "different"},
                   {"available_at": CUTOFF - timedelta(hours=1)}, {"state": "unknown"}):
        result = compute_trends([], [observation("robot-learning", 2), observation("__all__", 10, **change)], CUTOFF)
        assert result[0].share_28d is None
        assert result[0].support == "missing"


def test_document_windows_deduplicate_and_exclude_late_versions():
    docs = [document(1), document(2, days=28), document(3, days=56),
            document(4, days=0), document(5, available_at=None),
            document(6, available_at=CUTOFF + timedelta(days=1)),
            document(7, canonical_id="1"), document(8, days=29)]
    trend = next(t for t in compute_trends(docs, [], CUTOFF) if t.entity_id == "robot-learning")
    assert trend.count_28d == 2  # (cutoff-28d, cutoff], unique canonical IDs
    assert set(trend.evidence_ids) == {"1", "4"}
    assert trend.share_28d is None  # no collection-completeness snapshot


def test_unknown_invalid_or_stale_snapshot_is_not_zero():
    for value, state in [(None, "unknown"), (-1, "ok"), (1.5, "ok"), (20, "ok")]:
        trend = compute_trends([], [observation("x", value, state=state), observation("__all__", 10)], CUTOFF)[0]
        assert trend.support == "missing" and trend.share_28d is None
    assert compute_trends([], [observation("x", 1, days=28)], CUTOFF)[0].support == "missing"


def test_naive_cutoff_rejected():
    with pytest.raises(ValueError):
        compute_trends([], [], CUTOFF.replace(tzinfo=None))


def test_future_observed_snapshot_and_unrelated_metric_do_not_change_result():
    items = snapshots()
    additions = [observation("robot-learning", 99, metric="citations"),
                 observation("robot-learning", 99, observed_at=CUTOFF + timedelta(days=1)),
                 observation("robot-learning", 99, available_at=None)]
    assert compute_trends([], items, CUTOFF) == compute_trends([], items + additions, CUTOFF)


def test_evidence_uses_snapshot_source_and_conflicts_are_unknown():
    docs = [document(1), document(2, source="openalex")]
    trend = compute_trends(docs, snapshots(), CUTOFF)[0]
    assert trend.evidence_ids == ["1"]
    conflict = snapshots() + [observation("robot-learning", 3)]
    assert compute_trends([], conflict, CUTOFF)[0].share_28d is None


def test_previous_window_and_low_support_threshold():
    docs = [document(1, days=28), document(2, days=55), document(3, days=56)]
    previous = compute_trends(docs, [], CUTOFF - timedelta(days=28))[0]
    assert previous.count_28d == 2
    assert compute_trends([], [observation("x", 5), observation("__all__", 10)], CUTOFF)[0].support == "ok"
