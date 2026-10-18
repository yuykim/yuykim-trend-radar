"""28-day counts with explicit collection coverage.

Observation protocol: metric='count_28d' is a complete window snapshot,
entity_id='__all__' is its corpus denominator. A topic and its denominator
must have identical (source, coverage_id, available_at). The previous window
snapshot must be exactly 28 days earlier, with unchanged coverage and source.
Missing/unknown or invalid snapshots never produce a share or a decline.

Without snapshots, seed text matches still supply unique document counts and
evidence, but support='missing' and shares are null: documents alone cannot
prove collection completeness. A count of 0 with missing support is only the
non-nullable contract placeholder, never evidence of zero research activity.
"""

from __future__ import annotations

import math
import re
from datetime import datetime, timedelta
from pathlib import Path

import yaml

from ..contracts import Document, Observation, Trend

WINDOW = timedelta(days=28)
MINIMUM_SUPPORT = 5


def _check_cutoff(cutoff: datetime) -> None:
    if cutoff.tzinfo is None or cutoff.utcoffset() is None:
        raise ValueError("cutoff must be timezone-aware")


def _visible_documents(documents: list[Document], cutoff: datetime) -> list[Document]:
    """Earliest usable version per canonical ID; no future/undated features."""
    _check_cutoff(cutoff)
    visible = [d for d in documents if d.available_at is not None
               and d.available_at <= cutoff and d.observed_at <= cutoff
               and d.first_public_at is not None and d.first_public_at <= cutoff
               and (d.published_at is None or d.published_at <= cutoff)]
    unique = {}
    for doc in sorted(visible, key=lambda d: (d.available_at, d.id)):
        unique.setdefault(doc.canonical_id, doc)
    return sorted(unique.values(), key=lambda d: (d.first_public_at, d.id))


def _text(doc: Document) -> str:
    return doc.title + " " + (doc.abstract or "")


def _contains(text: str, term: str) -> bool:
    return bool(term.strip()) and re.search(r"(?<!\w)" + re.escape(term.strip()) + r"(?!\w)", text, re.I) is not None


def _seed_aliases() -> dict[str, list[str]]:
    config = Path(__file__).resolve().parents[3] / "config" / "topics.yml"
    with config.open(encoding="utf-8") as stream:
        return {topic["id"]: [topic["label"], *topic["aliases"]]
                for topic in yaml.safe_load(stream)["seed_topics"]}


def _valid_count(item: Observation | None) -> bool:
    return (item is not None and item.state == "ok" and item.value is not None
            and math.isfinite(item.value) and item.value >= 0 and item.value.is_integer())


def compute_trends(documents: list[Document], observations: list[Observation], cutoff: datetime) -> list[Trend]:
    """Return coverage-safe trends, sorted by count then entity ID, never probability."""
    docs = _visible_documents(documents, cutoff)
    aliases = _seed_aliases()
    visible = [o for o in observations if o.metric == "count_28d"
               and o.available_at is not None and o.available_at <= cutoff and o.observed_at <= cutoff]
    entities = {o.entity_id for o in visible if o.entity_id != "__all__"}
    entities.update(entity for entity, names in aliases.items() if any(
        any(_contains(_text(d), name) for name in names) for d in docs))

    def latest(entity, end):
        matches = [o for o in visible if o.entity_id == entity and end - WINDOW < o.available_at <= end]
        if not matches:
            return None
        newest = max(o.available_at for o in matches)
        matches = [o for o in matches if o.available_at == newest]
        # Conflicting simultaneous snapshots are unknown, not arbitrarily selected.
        fingerprints = {(o.source, o.coverage_id, o.state, o.value) for o in matches}
        return matches[0] if len(fingerprints) == 1 else None

    def share(topic):
        if not _valid_count(topic):
            return None
        totals = [o for o in visible if o.entity_id == "__all__"
                  and (o.source, o.coverage_id, o.available_at) ==
                  (topic.source, topic.coverage_id, topic.available_at)]
        if not totals or len({(o.value, o.state) for o in totals}) != 1:
            return None
        total = totals[0]
        if not _valid_count(total) or not total.value or topic.value > total.value:
            return None
        return topic.value / total.value

    trends = []
    for entity in sorted(entities):
        matching = [d for d in docs if cutoff - WINDOW < d.first_public_at <= cutoff
                    and any(_contains(_text(d), name) for name in aliases.get(entity, []))]
        current = latest(entity, cutoff)
        previous = latest(entity, cutoff - WINDOW)
        if current is not None:
            matching = [d for d in matching if d.source == current.source]
        current_share, previous_share = share(current), share(previous)
        count = int(current.value) if _valid_count(current) else len(matching)
        comparable = (current_share is not None and previous_share is not None
                      and current.source == previous.source and current.coverage_id == previous.coverage_id
                      and current.available_at - previous.available_at == WINDOW)
        trends.append(Trend(entity_id=entity, count_28d=count,
                            share_28d=current_share,
                            share_change=current_share - previous_share if comparable else None,
                            support="missing" if current_share is None else
                            "low_support" if count < MINIMUM_SUPPORT else "ok",
                            coverage_id=current.coverage_id if current else None,
                            evidence_ids=sorted(d.id for d in matching)))
    return sorted(trends, key=lambda t: (-t.count_28d, t.entity_id))
