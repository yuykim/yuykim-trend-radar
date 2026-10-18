"""Shared, versioned data contracts for the trend radar."""

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    @field_validator("published_at", "first_public_at", "observed_at", "available_at", "started_at", "finished_at", "reviewed_at", "generated_at", mode="before", check_fields=False)
    @classmethod
    def normalize_datetime(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("timestamps must include a timezone")
        return value.astimezone(timezone.utc)


class Document(Contract):
    id: str
    source: str
    source_id: str
    canonical_id: str
    title: str
    abstract: str | None
    url: str
    version: str | None
    published_at: datetime | None
    first_public_at: datetime | None
    observed_at: datetime
    available_at: datetime | None
    status: Literal["preprint", "accepted", "retracted", "unknown"]


class Observation(Contract):
    entity_id: str
    metric: str
    value: float | None
    available_at: datetime | None
    observed_at: datetime
    source: str
    coverage_id: str
    state: Literal["ok", "missing", "unknown"]


class EvidenceEdge(Contract):
    id: str
    source_id: str
    target_id: str
    relation: str
    evidence_url: str
    evidence_location: str | None
    available_at: datetime | None
    review_status: Literal["proposed", "verified", "rejected"]


class SourceRun(Contract):
    source: str
    started_at: datetime
    finished_at: datetime | None
    status: Literal["ok", "partial", "failed", "disabled"]
    coverage_id: str | None
    item_count: int
    error_code: str | None


class Trend(Contract):
    entity_id: str
    count_28d: int
    share_28d: float | None
    share_change: float | None
    support: Literal["ok", "low_support", "missing"]
    coverage_id: str | None
    evidence_ids: list[str]


class Candidate(Contract):
    id: str
    entity_id: str
    kind: Literal["new_term", "new_cluster", "new_combination", "rename_or_alias"]
    first_seen_at: datetime
    reasons: list[str]
    evidence_ids: list[str]
    review_status: Literal["proposed", "verified", "rejected"]


class Review(Contract):
    candidate_id: str
    reviewed_at: datetime
    already_known: bool | None
    relevant: bool | None
    distinct: bool | None
    useful: bool | None
    minutes_spent: float | None


class GraphNode(Contract):
    id: str
    label: str
    type: str


class GraphPayload(Contract):
    nodes: list[GraphNode]
    edges: list[EvidenceEdge]
    generated_at: datetime


class DashboardPayload(Contract):
    as_of: datetime
    trends: list[Trend]
    candidates: list[Candidate]
    community_candidates: list[Candidate]
    growth_watchlist: list[Candidate]
    source_runs: list[SourceRun]


class TopicDetail(Contract):
    entity_id: str
    label: str
    aliases: list[str]
    documents: list[Document]
    observations: list[Observation]
    evidence_edges: list[EvidenceEdge]
    limitations: list[str]
