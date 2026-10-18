"""Personal discovery utility metrics; no prediction probabilities.

Input order is rank order. Precision uses latest useful labels and is unknown
until every available top-five row is reviewed. Lead matches exact entity IDs
only (no acronym inference), deduplicated to earliest detection per entity.
"""

from __future__ import annotations

import math
from collections import defaultdict
from statistics import median

from ..contracts import Candidate, Review


def evaluate(candidates: list[Candidate], baseline: list[Candidate], reviews: list[Review]) -> dict:
    """Evaluate equally budgeted top-five lists; missing labels stay null."""
    latest = {}
    for review in sorted(reviews, key=lambda r: (r.reviewed_at, r.model_dump_json())):
        if review.minutes_spent is not None and (not math.isfinite(review.minutes_spent) or review.minutes_spent < 0):
            raise ValueError("minutes_spent must be finite and nonnegative")
        latest[review.candidate_id] = review

    def precision(items):
        labels = [latest[c.id].useful if c.id in latest else None for c in items[:5]]
        reviewed = sum(label is not None for label in labels)
        return (sum(labels) / len(labels) if labels and reviewed == len(labels) else None), reviewed

    system_precision, reviewed = precision(candidates)
    baseline_precision, baseline_reviewed = precision(baseline)

    def earliest(items):
        result = {}
        for item in items:
            if item.entity_id not in result or item.first_seen_at < result[item.entity_id].first_seen_at:
                result[item.entity_id] = item
        return result

    system_entities, baseline_entities = earliest(candidates[:5]), earliest(baseline[:5])
    comparisons, leads = [], []
    for entity, item in sorted(system_entities.items()):
        match = baseline_entities.get(entity)
        lead = (match.first_seen_at - item.first_seen_at).total_seconds() / 86400 if match else None
        if lead is not None:
            leads.append(lead)
        comparisons.append({"candidate_id": item.id, "entity_id": entity,
                            "lead_days": lead, "additional_discovery": match is None})
    relevant_ids = {c.id for c in candidates[:5] + baseline[:5]}
    events = [r for r in reviews if r.candidate_id in relevant_ids]
    durations = [r.minutes_spent for r in events if r.minutes_spent is not None]
    daily = defaultdict(float)
    for review in events:
        if review.minutes_spent is not None:
            daily[review.reviewed_at.date().isoformat()] += review.minutes_spent
    time_complete = bool(events) and len(durations) == len(events)
    return {"precision_at_5": system_precision, "reviewed_at_5": reviewed,
            "baseline_precision_at_5": baseline_precision, "baseline_reviewed_at_5": baseline_reviewed,
            "duplicate_rate": 1 - len(system_entities) / len(candidates[:5]) if candidates else None,
            "median_lead_days": median(leads) if leads else None, "comparisons": comparisons,
            "review_minutes": sum(durations) if time_complete else None,
            "median_daily_review_minutes": median(daily.values()) if time_complete else None,
            "status": "inconclusive" if system_precision is None or baseline_precision is None else "reviewed",
            "limitations": ["Personal utility labels; not technology success prediction.",
                            "Additional discovery means absent from the supplied baseline, not absent forever.",
                            "Review days use UTC; missing review durations remain unknown."]}
