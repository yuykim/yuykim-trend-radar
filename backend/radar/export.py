"""Export repository evidence to the frontend's static JSON contract.

Entity IDs unsafe on Windows are mapped reversibly to '~' + URL-safe base64.
The same wire ID is used in every payload; evidence/document IDs are unchanged.
Collection belongs to the batch caller; exporting never fetches source documents.
"""
from __future__ import annotations

import base64
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

from .analysis import compute_trends, discover
from .contracts import DashboardPayload, GraphNode, GraphPayload, TopicDetail
from .llm import LLMClient, NOTICE, ROOT, summarize
from .storage import Repository


def _wire_id(entity_id: str) -> str:
    if (re.fullmatch(r"[A-Za-z0-9_-]+", entity_id)
            and not re.fullmatch(r"(?i:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])", entity_id)):
        return entity_id
    return "~" + base64.urlsafe_b64encode(entity_id.encode()).decode().rstrip("=")


def export_site(repo: Repository, out_dir: str, as_of: datetime) -> None:
    """Write dashboard.json, graph.json, topics/{wire entity_id}.json.

    as_of must be timezone-aware. Unknown metrics remain null/missing. A single
    optional LLMClient shares the configured budget across all candidate summaries.
    Source history retains last successful runs without adding frontend fields.
    """
    if as_of.tzinfo is None or as_of.utcoffset() is None:
        raise ValueError("as_of must be timezone-aware")
    as_of = as_of.astimezone(timezone.utc)
    documents = [d for d in repo.list_documents(as_of) if d.observed_at <= as_of
                 and (d.published_at is None or d.published_at <= as_of)
                 and (d.first_public_at is None or d.first_public_at <= as_of)]
    observations = [o for o in repo.list_observations(as_of) if o.observed_at <= as_of]
    edges = repo.list_edges(as_of)
    runs = [r for r in repo.list_runs() if r.started_at <= as_of
            and (r.finished_at is None or r.finished_at <= as_of)]
    runs.sort(key=lambda r: (r.started_at, r.source), reverse=True)
    seeds = yaml.safe_load((ROOT / "config/topics.yml").read_text(encoding="utf-8"))["seed_topics"]
    aliases = {s["id"]: [s["label"], *s["aliases"]] for s in seeds}
    trends = compute_trends(documents, observations, as_of)
    candidates = discover(documents, aliases, as_of)
    client = None
    try:
        try:
            client = LLMClient.from_env(repo.db_path)
        except Exception:
            # Cache/config initialization is also optional.
            import logging
            logging.getLogger(__name__).warning("LLM summary unavailable: initialization failure")
        for candidate in candidates:
            # Presentation annotation only, after ranking. generated_at records
            # its actual creation time; it is never fed back into as_of features.
            candidate.summary = summarize(candidate, documents, client)
    finally:
        if client is not None:
            client.close()

    entities = {s["id"] for s in seeds} | {t.entity_id for t in trends}
    entities.update(c.entity_id for c in candidates)
    entities.update(o.entity_id for o in observations if o.entity_id != "__all__")
    doc_by_id = {d.id: d for d in documents}
    # Existing evidence creates nodes, never inferred technology edges.
    endpoints = {i for e in edges for i in (e.source_id, e.target_id)}
    entities.update(endpoints)
    mapping = {entity: _wire_id(entity) for entity in entities}
    labels = {s["id"]: s["label"] for s in seeds}
    labels.update({d.id: d.title for d in documents if d.id in endpoints})
    labels.update({c.entity_id: c.reasons[0] if c.reasons else c.entity_id for c in candidates})
    topic_payloads = {}
    for entity in sorted(entities):
        related = [c for c in candidates if c.entity_id == entity]
        evidence = {i for c in related for i in c.evidence_ids}
        if entity in doc_by_id:
            evidence.add(entity)
        evidence.update(i for t in trends if t.entity_id == entity for i in t.evidence_ids)
        topic_edges = [e for e in edges if entity in (e.source_id, e.target_id)]
        evidence.update(i for e in topic_edges for i in (e.source_id, e.target_id) if i in doc_by_id)
        topic_obs = [o.model_copy(update={"entity_id": mapping[entity]})
                     for o in observations if o.entity_id == entity]
        limitations = ["원문·코드·재현성 검증 상태는 별도로 확인해야 합니다."]
        if any(t.entity_id == entity and t.support == "missing" for t in trends):
            limitations.append("수집 coverage 미확인: missing은 관심도 하락이나 0을 의미하지 않습니다.")
        if any(t.entity_id == entity and t.support == "low_support" for t in trends):
            limitations.append("low_support: 표본이 작아 해석에 주의가 필요합니다.")
        if related:
            limitations.append("규칙 기반 제안 후보이며 신규 기술로 확정되지 않았습니다.")
            limitations.extend(r for c in related for r in c.reasons if "low_support" in r)
        summary = next((c.summary for c in related if c.summary is not None), None)
        if summary:
            limitations.append(NOTICE)
        topic_payloads[mapping[entity]] = TopicDetail(entity_id=mapping[entity],
            label=labels.get(entity, entity), aliases=aliases.get(entity, [])[1:],
            documents=[d for d in documents if d.id in evidence], observations=topic_obs,
            evidence_edges=[e.model_copy(update={"source_id": mapping.get(e.source_id, e.source_id),
                "target_id": mapping.get(e.target_id, e.target_id)}) for e in topic_edges],
            limitations=list(dict.fromkeys(limitations)), summary=summary)
    wire_edges = [e.model_copy(update={"source_id": mapping.get(e.source_id, e.source_id),
                  "target_id": mapping.get(e.target_id, e.target_id)}) for e in edges]
    nodes = [GraphNode(id=mapping[e], label=labels.get(e, e),
             type="document" if e in doc_by_id else "topic" if e in labels else "unknown")
             for e in sorted(entities)]
    # A truly empty repository produces the empty graph rather than seed placeholders.
    if not documents and not observations and not edges:
        nodes = []
    dashboard = DashboardPayload(as_of=as_of,
        trends=[t.model_copy(update={"entity_id": mapping[t.entity_id]}) for t in trends],
        candidates=[c.model_copy(update={"entity_id": mapping[c.entity_id]}) for c in candidates],
        community_candidates=[], growth_watchlist=[], source_runs=runs)
    payloads = {"dashboard.json": dashboard,
                "graph.json": GraphPayload(nodes=nodes, edges=wire_edges, generated_at=as_of)}
    payloads.update({f"topics/{entity}.json": topic for entity, topic in topic_payloads.items()})
    rendered = {name: model.model_dump_json(indent=2) + "\n" for name, model in payloads.items()}
    secret = os.environ.get("GEMINI_API_KEY")
    if secret and any(secret in value for value in rendered.values()):
        raise ValueError("Export contains a configured secret")
    output = Path(out_dir)
    (output / "topics").mkdir(parents=True, exist_ok=True)
    for name, value in rendered.items():
        target = output / name
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=target.parent,
                                         suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(value)
        try:
            os.replace(temporary, target)
        finally:
            temporary.unlink(missing_ok=True)
    for old in (output / "topics").glob("*.json"):
        if old.name[:-5] not in topic_payloads:
            old.unlink()
