"""Daily static-site batch and prospective personal-utility evaluation."""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import median

import yaml

from .analysis import discover, evaluate
from .collectors import canonicalize, collect
from .contracts import Candidate, Observation, Review
from .export import export_site
from .storage import Repository

ROOT = Path(__file__).resolve().parents[2]
UTC = timezone.utc


def now():
    return datetime.now(UTC)


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("as-of must include a timezone")
    return result.astimezone(UTC)


def _matches(doc, names):
    return any(re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)",
                        doc.title + " " + (doc.abstract or ""), re.I) for name in names)


def _seeds():
    return yaml.safe_load((ROOT / "config/topics.yml").read_text(encoding="utf-8"))["seed_topics"]


def _snapshots(db):
    db.execute("CREATE TABLE IF NOT EXISTS daily_snapshots (day TEXT PRIMARY KEY, payload TEXT NOT NULL)")


def run(*, db_path="data/radar.db", out="frontend/public/data", as_of=None):
    """Resume a fixed UTC-day collection window; never backdate observations.

    The publication query ends at the day's 22:00 UTC boundary (07:00 Seoul).
    Bootstrap spans 56 days; completed windows then advance with one overlap day.
    Before that boundary use the previous day. Export uses actual completion time
    unless an explicit historical as_of is supplied. Checkpoint scope therefore
    stays stable for manual retries of the same daily batch.
    """
    started = now()
    cutoff = timestamp(as_of) if isinstance(as_of, str) else as_of or started
    boundary = cutoff.replace(hour=22, minute=0, second=0, microsecond=0)
    if boundary > cutoff:
        boundary -= timedelta(days=1)
    repo = Repository(str(db_path))
    with sqlite3.connect(str(db_path)) as db:
        db.execute("CREATE TABLE IF NOT EXISTS daily_batch_state (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
        pending = db.execute("SELECT value FROM daily_batch_state WHERE key='pending_cutoff'").fetchone()
        completed = db.execute("SELECT value FROM daily_batch_state WHERE key='completed_cutoff'").fetchone()
        if pending and as_of is None:
            boundary = timestamp(pending[0])
    since = (min(boundary, timestamp(completed[0])) - timedelta(days=1)
             if completed and as_of is None else boundary - timedelta(days=56))
    os.environ.setdefault("RADAR_COLLECTOR_STATE", str(Path(db_path).with_name("collector-state.db")))
    runs, collected = [], []
    for source in ("arxiv", "openreview", "openalex"):
        docs, source_run = collect(source, since, boundary)
        collected.extend(docs)
        runs.append(source_run)
        repo.save_run(source_run)
    if as_of is None:
        with sqlite3.connect(str(db_path)) as db:
            if runs[0].status in ("partial", "failed"):
                db.execute("INSERT OR REPLACE INTO daily_batch_state VALUES ('pending_cutoff', ?)", (boundary.isoformat(),))
            else:
                db.execute("DELETE FROM daily_batch_state WHERE key='pending_cutoff'")
                if runs[0].status == "ok":
                    db.execute("INSERT OR REPLACE INTO daily_batch_state VALUES ('completed_cutoff', ?)", (boundary.isoformat(),))
    existing_ids = {d.id for d in repo.list_documents(datetime.max.replace(tzinfo=UTC))}
    for doc in canonicalize(collected):
        # Repository upserts replace timestamps. Preserve the first observation
        # of an immutable source version; new arXiv versions have separate IDs.
        if doc.id not in existing_ids:
            repo.upsert_document(doc)
    effective = cutoff if as_of is not None else now()
    visible = [d for d in repo.list_documents(effective) if d.observed_at <= effective
               and d.first_public_at is not None and d.first_public_at <= effective
               and (d.published_at is None or d.published_at <= effective)]
    # Match Task 3's earliest usable version, one vote per canonical document.
    unique = {}
    for doc in sorted(visible, key=lambda d: (d.available_at, d.id)):
        unique.setdefault(doc.canonical_id, doc)
    documents = list(unique.values())
    arxiv = runs[0]
    current = [d for d in documents if d.source == "arxiv"
               and effective - timedelta(days=28) < d.first_public_at <= effective]
    seeds = _seeds()
    # Only observations made by this cutoff can describe the current snapshot.
    complete = (arxiv.status == "ok" and arxiv.finished_at is not None
                and arxiv.finished_at <= effective
                and effective - boundary < timedelta(days=1))
    observations = []
    for entity, names in [("__all__", None), *[(s["id"], [s["label"], *s["aliases"]]) for s in seeds]]:
        count = len(current) if names is None else sum(_matches(d, names) for d in current)
        observed = now() if as_of is not None else effective
        observations.append(Observation(entity_id=entity, metric="count_28d",
            value=count if complete else None, available_at=observed, observed_at=observed,
            source="arxiv", coverage_id=arxiv.coverage_id or "unknown", state="ok" if complete else "missing"))
    repo.save_observations(observations)
    aliases = {s["id"]: [s["label"], *s["aliases"]] for s in seeds}
    candidates = discover(documents, aliases, effective)
    chronological = sorted(current, key=lambda d: (d.first_public_at, d.id), reverse=True)
    baseline, broad = [], []
    for doc in chronological:
        for seed in seeds:
            if _matches(doc, aliases[seed["id"]]):
                baseline.append(Candidate(id=f"baseline:{doc.id}:{seed['id']}", entity_id=seed["id"],
                    kind="new_term", first_seen_at=max(doc.available_at, doc.observed_at),
                    reasons=[], evidence_ids=[doc.id], review_status="proposed"))
        broad.append(Candidate(id=f"broad:{doc.id}", entity_id=doc.canonical_id,
            kind="new_term", first_seen_at=max(doc.available_at, doc.observed_at),
            reasons=[], evidence_ids=[doc.id], review_status="proposed"))
    snapshot = {"as_of": effective.isoformat(), "candidates": [c.model_dump(mode="json") for c in candidates[:5]],
                "baseline": [c.model_dump(mode="json") for c in baseline[:5]],
                "broad": [c.model_dump(mode="json") for c in broad[:5]],
                "core_ok": arxiv.status == "ok"}
    with sqlite3.connect(str(db_path)) as db:
        _snapshots(db)
        # First daily exposure is immutable: retries must not rewrite evaluation history.
        db.execute("INSERT OR IGNORE INTO daily_snapshots VALUES (?, ?)",
                   (boundary.date().isoformat(), json.dumps(snapshot)))
    output = Path(out)
    existing = output / "dashboard.json"
    # Existing synthetic examples stay available until the first real document.
    preserve_demo = not visible and existing.exists() and not (output / "run-status.json").exists()
    if (output / "run-status.json").exists():
        previous = json.loads((output / "run-status.json").read_text(encoding="utf-8"))
        preserve_demo = not visible and previous.get("demo", False)
    if not preserve_demo:
        export_site(repo, str(output), effective)
    output.mkdir(parents=True, exist_ok=True)
    dashboard = json.loads(existing.read_text(encoding="utf-8"))
    result = {"as_of": effective.isoformat(), "collection_cutoff": boundary.isoformat(),
              "collected": len({d.canonical_id for d in collected}), "visible_documents": len(documents),
              "demo": preserve_demo, "source_runs": [r.model_dump(mode="json") for r in runs],
              "llm": "disabled" if not os.environ.get("GEMINI_API_KEY") else
              "not_needed" if preserve_demo or not dashboard["candidates"] else
              "generated_or_cached" if any(c.get("summary") for c in dashboard["candidates"]) else "unavailable"}
    (output / "run-status.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Checkpoint WAL before CI commits the main database file.
    with sqlite3.connect(str(db_path)) as db:
        db.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    return result


def evaluate_protocol(db_path, protocol_path, reviews_path=None, review_out=None):
    protocol = yaml.safe_load(Path(protocol_path).read_text(encoding="utf-8"))
    repo = Repository(str(db_path))
    reviews = repo.list_reviews()
    if reviews_path:
        raw = json.loads(Path(reviews_path).read_text(encoding="utf-8"))
        reviews.extend(Review.model_validate(r) for r in (raw["reviews"] if isinstance(raw, dict) else raw))
    with sqlite3.connect(str(db_path)) as db:
        _snapshots(db)
        snapshots = [json.loads(row[0]) for row in db.execute("SELECT payload FROM daily_snapshots ORDER BY day")]
    start = timestamp(protocol["prospective_start"]) if protocol["prospective_start"] else None
    end = start + timedelta(weeks=protocol["duration_weeks"]) if start else None
    rows = [s for s in snapshots if start and start <= timestamp(s["as_of"]) < end]
    if review_out:
        # Opaque review IDs hide system/baseline assignment, scores and reasons.
        import hashlib
        packets = {}
        for row in rows:
            for arm in ("candidates", "baseline", "broad"):
                for item in row[arm]:
                    blind = hashlib.sha256(item["id"].encode()).hexdigest()[:20]
                    packets[blind] = {"review_id": blind, "evidence_ids": item["evidence_ids"]}
        Path(review_out).write_text(json.dumps(sorted(packets.values(), key=lambda p: p["review_id"]), indent=2), encoding="utf-8")
    import hashlib
    mapping = {hashlib.sha256(c["id"].encode()).hexdigest()[:20]: c["id"]
               for row in rows for arm in ("candidates", "baseline", "broad") for c in row[arm]}
    reviews = [r.model_copy(update={"candidate_id": mapping.get(r.candidate_id, r.candidate_id)}) for r in reviews]
    results = []
    all_candidates, all_baseline = [], []
    for row in rows:
        arms = {k: [Candidate.model_validate(c) for c in row[k]] for k in ("candidates", "baseline", "broad")}
        all_candidates.extend(arms["candidates"])
        all_baseline.extend(arms["baseline"])
        day = timestamp(row["as_of"]).date()
        day_reviews = [r for r in reviews if r.reviewed_at.date() == day]
        results.append({"as_of": row["as_of"], **evaluate(arms["candidates"], arms["baseline"], day_reviews),
                        "broad_comparison": evaluate(arms["candidates"], arms["broad"], day_reviews)})
    def earliest(items):
        result = {}
        for c in sorted(items, key=lambda c: c.first_seen_at):
            result.setdefault(c.entity_id, c)
        return result
    system, baseline = earliest(all_candidates), earliest(all_baseline)
    latest = {r.candidate_id: r for r in sorted(reviews, key=lambda r: r.reviewed_at)
              if start and start <= r.reviewed_at < end}
    unknown_weekly = [0] * protocol["duration_weeks"]
    for c in system.values():
        r = latest.get(c.id)
        if r and r.useful is True and r.already_known is False:
            week = (c.first_seen_at - start).days // 7
            if 0 <= week < len(unknown_weekly):
                unknown_weekly[week] += 1
    leads = [(baseline[e].first_seen_at - c.first_seen_at).total_seconds() / 86400
             for e, c in system.items() if e in baseline]
    precisions = [r["precision_at_5"] for r in results]
    baseline_precisions = [r["baseline_precision_at_5"] for r in results]
    delta = (sum(precisions) - sum(baseline_precisions)) / len(results) if results and all(
        p is not None for p in precisions + baseline_precisions) else None
    durations = [r["median_daily_review_minutes"] for r in results]
    minutes = median(durations) if durations and all(d is not None for d in durations) else None
    core_runs = [r for r in repo.list_runs() if start and r.source == "arxiv"
                 and start <= r.started_at < end and r.status != "disabled"]
    success = sum(r.status == "ok" for r in core_runs) / len(core_runs) if core_runs else None
    criteria = protocol["go_criteria"]
    known_reviews = bool(system) and all(latest.get(c.id) and latest[c.id].already_known is not None
                                        and latest[c.id].useful is not None for c in system.values())
    checks = {
        "core_collection": success >= criteria["core_collection_success_rate_min"] if success is not None else None,
        "precision_improvement": delta >= criteria["precision_at_5_improvement_min"] if delta is not None else None,
        "unknown_useful_weekly": all(n >= criteria["unknown_useful_candidates_per_week_min"] for n in unknown_weekly) if known_reviews else None,
        "matched_lead": median(leads) >= criteria["matched_median_lead_days_min"] if leads else None,
        "review_minutes": minutes <= criteria["median_daily_review_minutes_max"] if minutes is not None else None,
    }
    required_days = protocol["duration_weeks"] * 7
    full_samples = (len(rows) == required_days and start is not None and now() >= end
                    and all(len(s["candidates"]) == 5 and len(s["baseline"]) == 5 for s in rows)
                    and all(r["status"] == "reviewed" for r in results)
                    and all(latest.get(c.id) and latest[c.id].already_known is not None for c in system.values()))
    status = "go" if full_samples and all(v is True for v in checks.values()) else (
        "no_go" if full_samples and all(v is not None for v in checks.values()) else "inconclusive")
    return {"status": status, "prospective_start": protocol["prospective_start"],
            "days_observed": len(rows), "duration_weeks": protocol["duration_weeks"],
            "core_success_rate": success, "precision_at_5_improvement": delta,
            "unknown_useful_candidates_per_week": unknown_weekly if known_reviews else None,
            "matched_median_lead_days": median(leads) if leads else None,
            "median_daily_review_minutes": minutes, "criteria_met": checks,
            "daily_results": results, "go_criteria": protocol["go_criteria"],
            "limitations": ["Go judgement requires all five criteria and 28 complete daily samples.",
                            "No prospective start is assumed; set it before collecting evaluation samples."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    daily = sub.add_parser("run")
    daily.add_argument("--as-of", type=timestamp)
    daily.add_argument("--out", default="frontend/public/data")
    daily.add_argument("--db", default="data/radar.db")
    evaluation = sub.add_parser("evaluate")
    evaluation.add_argument("--protocol", default="config/evaluation.yml")
    evaluation.add_argument("--db", default="data/radar.db")
    evaluation.add_argument("--reviews")
    evaluation.add_argument("--review-out")
    args = parser.parse_args(argv)
    if args.command == "run":
        result = run(db_path=args.db, out=args.out, as_of=args.as_of)
    else:
        result = evaluate_protocol(args.db, args.protocol, args.reviews, args.review_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
