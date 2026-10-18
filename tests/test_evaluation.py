from datetime import datetime, timedelta, timezone

import pytest

from radar.analysis.evaluation import evaluate
from radar.contracts import Candidate, Review

NOW = datetime(2026, 10, 18, tzinfo=timezone.utc)


def candidate(name, days=0, entity=None):
    return Candidate(id=name, entity_id=entity or name, kind="new_term", first_seen_at=NOW - timedelta(days=days),
                     reasons=[], evidence_ids=[name], review_status="proposed")


def review(name, useful=True, minutes=2, days=0):
    return Review(candidate_id=name, reviewed_at=NOW + timedelta(days=days), already_known=False,
                  relevant=True, distinct=True, useful=useful, minutes_spent=minutes)


def test_unmatched_baseline_has_no_invented_lead():
    result = evaluate([candidate("new")], [], [])
    assert result["comparisons"][0]["lead_days"] is None
    assert result["comparisons"][0]["additional_discovery"] is True
    assert result["median_lead_days"] is None


def test_metrics_latest_review_duplicates_and_signed_lead():
    candidates = [candidate("a", 4), candidate("b", 2), candidate("copy", entity="a")]
    baseline = [candidate("base-a", 1, "a"), candidate("base-b", 3, "b")]
    reviews = [review("a", False), review("a", True, days=1), review("b", False), review("copy")]
    result = evaluate(candidates, baseline, reviews)
    assert result["precision_at_5"] == pytest.approx(2 / 3)
    assert result["duplicate_rate"] == pytest.approx(1 / 3)
    assert result["median_lead_days"] == 1  # median of +3 and -1, entities counted once
    assert result["review_minutes"] == 8  # all review events are work
    assert result["median_daily_review_minutes"] == 4


def test_unknown_reviews_are_not_negative_or_perfect_precision():
    result = evaluate([candidate("a"), candidate("b")], [], [review("a")])
    assert result["precision_at_5"] is None
    assert result["reviewed_at_5"] == 1
    assert result["status"] == "inconclusive"
    assert evaluate([], [], [])["duplicate_rate"] is None
    assert evaluate([], [], [])["review_minutes"] is None


def test_negative_review_duration_rejected():
    with pytest.raises(ValueError):
        evaluate([candidate("a")], [], [review("a", minutes=-1)])


def test_equal_top_five_budget_and_incomplete_review_time():
    candidates = [candidate(str(i)) for i in range(6)]
    reviews = [review(str(i)) for i in range(5)]
    result = evaluate(candidates, candidates, reviews + [review("unrelated", minutes=100)])
    assert result["precision_at_5"] == result["baseline_precision_at_5"] == 1
    assert len(result["comparisons"]) == 5
    assert result["review_minutes"] == 10
    assert result["status"] == "reviewed"
    reviews[0] = review("0", minutes=None)
    assert evaluate(candidates, [], reviews)["review_minutes"] is None
