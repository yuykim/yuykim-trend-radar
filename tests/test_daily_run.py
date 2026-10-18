import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from radar import cli
from radar.contracts import Document, SourceRun
from radar.storage import Repository

NOW = datetime(2026, 10, 18, 22, tzinfo=timezone.utc)


@pytest.fixture(autouse=True)
def isolated(monkeypatch, tmp_path):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setenv("RADAR_COLLECTOR_STATE", str(tmp_path / "checkpoint.db"))
    monkeypatch.setattr(cli, "now", lambda: NOW)


def fake_collect(source, since, cutoff):
    docs = []
    if source == "arxiv":
        docs = [Document(id="arxiv:1", source="arxiv", source_id="1", canonical_id="arxiv:1",
            title="Vision-Language-Action robot policy", abstract="Adaptive Robot Policy (ARP)",
            url="https://arxiv.org/abs/1", version="v1", published_at=NOW - timedelta(days=1),
            first_public_at=NOW - timedelta(days=1), observed_at=NOW, available_at=NOW, status="preprint")]
    return docs, SourceRun(source=source, started_at=NOW, finished_at=NOW,
        status="ok" if docs else "disabled", coverage_id="test" if docs else None,
        item_count=len(docs), error_code=None)


def test_as_of_is_0700_seoul(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "collect", fake_collect)
    result = cli.run(db_path=tmp_path / "radar.db", out=tmp_path / "site")
    kst = datetime.fromisoformat(result["as_of"]).astimezone(timezone(timedelta(hours=9)))
    assert (kst.day, kst.hour) == (19, 7)
    assert result["collection_cutoff"] == NOW.isoformat()


def test_run_succeeds_without_llm(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "collect", fake_collect)
    result = cli.run(db_path=tmp_path / "radar.db", out=tmp_path / "site")
    assert result["llm"] == "disabled" and result["collected"] == 1
    assert [r["status"] for r in result["source_runs"]] == ["ok", "disabled", "disabled"]
    data = json.loads((tmp_path / "site/dashboard.json").read_text())
    assert next(t for t in data["trends"] if t["entity_id"] == "vla")["share_28d"] == 1
    assert all(c["summary"] is None for c in data["candidates"])
    graph = json.loads((tmp_path / "site/graph.json").read_text())
    assert all((tmp_path / "site/topics" / (n["id"] + ".json")).exists() for n in graph["nodes"])


def test_resume_partial_run(monkeypatch, tmp_path):
    windows = []
    partial = True

    def collector(source, since, cutoff):
        docs, run = fake_collect(source, since, cutoff)
        windows.append((source, since, cutoff))
        if source == "arxiv" and partial:
            run.status, run.error_code = "partial", "network_error"
        return docs, run

    monkeypatch.setattr(cli, "collect", collector)
    args = dict(db_path=tmp_path / "radar.db", out=tmp_path / "site")
    cli.run(**args)
    data = json.loads((tmp_path / "site/dashboard.json").read_text())
    assert all(t["support"] == "missing" and t["share_28d"] is None for t in data["trends"])
    partial = False
    cli.run(**args)
    assert windows[:3] == windows[3:]
    repo = Repository(str(tmp_path / "radar.db"))
    assert len(repo.list_documents(NOW)) == 1
    assert [r.status for r in repo.list_runs() if r.source == "arxiv"] == ["partial", "ok"]


def test_preserve_demo_until_first_document(monkeypatch, tmp_path):
    out = tmp_path / "site"
    out.mkdir()
    fixture = '{"candidates": [], "synthetic": true}'
    (out / "dashboard.json").write_text(fixture)
    monkeypatch.setattr(cli, "collect", lambda s, a, b: ([], SourceRun(source=s,
        started_at=NOW, finished_at=NOW, status="failed" if s == "arxiv" else "disabled",
        coverage_id=None, item_count=0, error_code="network_error")))
    assert cli.run(db_path=tmp_path / "radar.db", out=out)["demo"]
    assert (out / "dashboard.json").read_text() == fixture
    monkeypatch.setattr(cli, "collect", fake_collect)
    assert not cli.run(db_path=tmp_path / "radar.db", out=out)["demo"]
    assert "synthetic" not in (out / "dashboard.json").read_text()


def test_historical_cutoff_does_not_backdate_live_documents(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "collect", fake_collect)
    result = cli.run(db_path=tmp_path / "radar.db", out=tmp_path / "site", as_of=NOW - timedelta(days=1))
    assert result["visible_documents"] == 0
    payload = json.loads((tmp_path / "site/dashboard.json").read_text())
    assert all(t["support"] == "missing" for t in payload["trends"])
    assert Repository(str(tmp_path / "radar.db")).list_observations(NOW - timedelta(days=1)) == []


def test_evaluation_does_not_invent_prospective_start(tmp_path):
    result = cli.evaluate_protocol(tmp_path / "radar.db", "config/evaluation.yml")
    assert result["status"] == "inconclusive" and result["days_observed"] == 0
    assert result["core_success_rate"] is None


def test_recollection_preserves_first_observation(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "collect", fake_collect)
    args = dict(db_path=tmp_path / "radar.db", out=tmp_path / "site")
    cli.run(**args)

    def later(source, since, cutoff):
        docs, run = fake_collect(source, since, cutoff)
        return [d.model_copy(update={"observed_at": NOW + timedelta(days=1),
                                    "available_at": NOW + timedelta(days=1)}) for d in docs], run

    monkeypatch.setattr(cli, "collect", later)
    monkeypatch.setattr(cli, "now", lambda: NOW + timedelta(days=1))
    cli.run(**args)
    assert Repository(str(tmp_path / "radar.db")).list_documents(NOW)[0].observed_at == NOW


def test_real_checkpoint_resumes_failed_page(monkeypatch, tmp_path):
    from radar.collectors import base
    state = base.State()
    pages = []
    fail = True

    def collector(source, since, cutoff):
        if source != "arxiv":
            return fake_collect(source, since, cutoff)

        def page(cursor, observed):
            pages.append(cursor)
            if cursor == 1 and fail:
                raise base.FetchError("network_error")
            if cursor == 0:
                return fake_collect("arxiv", since, cutoff)[0], 1
            return [], None

        return base.paged(source, since, cutoff, {}, state, "test", 0, page)

    monkeypatch.setattr(base, "now", lambda: NOW)
    monkeypatch.setattr(cli, "collect", collector)
    args = dict(db_path=tmp_path / "radar.db", out=tmp_path / "site")
    assert cli.run(**args)["source_runs"][0]["status"] == "partial"
    fail = False
    monkeypatch.setattr(cli, "now", lambda: NOW + timedelta(days=1))
    assert cli.run(**args)["source_runs"][0]["status"] == "ok"
    assert pages == [0, 1, 1]
    data = json.loads((tmp_path / "site/dashboard.json").read_text())
    assert all(t["support"] == "missing" for t in data["trends"])
    with state.connect() as db:
        assert db.execute("SELECT count(*) FROM pages").fetchone()[0] == 1
    monkeypatch.setattr(cli, "now", lambda: NOW + timedelta(days=2))
    cli.run(**args)
    assert pages == [0, 1, 1, 0, 1]


def test_prospective_evaluation_and_blind_reviews(tmp_path, monkeypatch):
    import sqlite3
    import yaml
    from radar.contracts import Candidate

    db_path = tmp_path / "radar.db"
    repo = Repository(str(db_path))
    start = NOW
    protocol = yaml.safe_load(Path("config/evaluation.yml").read_text())
    protocol["prospective_start"] = start.isoformat()
    config = tmp_path / "evaluation.yml"
    config.write_text(yaml.safe_dump(protocol))
    reviews = []
    with sqlite3.connect(db_path) as db:
        cli._snapshots(db)
        for day in range(28):
            at = start + timedelta(days=day)
            arms = {}
            for arm in ("candidates", "baseline", "broad"):
                items = []
                for n in range(5):
                    item = Candidate(id=f"{arm}:{day}:{n}", entity_id=f"entity:{day}:{n}",
                        kind="new_term", first_seen_at=at + (timedelta(days=1) if arm != "candidates" else timedelta()),
                        reasons=["hidden_score=99"], evidence_ids=["doc"], review_status="proposed")
                    items.append(item.model_dump(mode="json"))
                    if arm != "broad":
                        reviews.append(dict(candidate_id=item.id, reviewed_at=at.isoformat(), already_known=False,
                            relevant=True, distinct=True, useful=arm == "candidates", minutes_spent=0.5))
                arms[arm] = items
            snapshot = dict(as_of=at.isoformat(), core_ok=True, **arms)
            db.execute("INSERT INTO daily_snapshots VALUES (?, ?)", (at.date().isoformat(), json.dumps(snapshot)))
            db.commit()
            repo.save_run(SourceRun(source="arxiv", started_at=at, finished_at=at, status="ok",
                coverage_id="test", item_count=5, error_code=None))
    review_file = tmp_path / "reviews.json"
    review_file.write_text(json.dumps(reviews))
    packet = tmp_path / "blind.json"
    monkeypatch.setattr(cli, "now", lambda: start + timedelta(days=28))
    result = cli.evaluate_protocol(db_path, config, review_file, packet)
    assert result["status"] == "go"
    assert result["matched_median_lead_days"] == 1
    assert all(result["criteria_met"].values())
    assert all(set(p) == {"review_id", "evidence_ids"} for p in json.loads(packet.read_text()))
    assert "hidden_score" not in packet.read_text()
    reviews[0]["already_known"] = None
    review_file.write_text(json.dumps(reviews))
    assert cli.evaluate_protocol(db_path, config, review_file)["status"] == "inconclusive"
