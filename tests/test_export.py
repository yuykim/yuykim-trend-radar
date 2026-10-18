import json
import re
from datetime import timedelta
from pathlib import Path

import pytest

from radar.contracts import (Candidate, CandidateSummary, DashboardPayload, Document,
    EvidenceEdge, GraphPayload, Observation, SourceRun, TopicDetail)
from radar.export import _wire_id, export_site
from radar.llm import LLMClient
from radar.storage import Repository
from test_llm import CONFIG, NOW, Fake, document

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def disabled_llm(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)


def read(out, name):
    return json.loads((out / name).read_text(encoding="utf-8"))


def populated(tmp_path):
    repo = Repository(str(tmp_path / "radar.db"))
    repo.upsert_document(document().model_copy(update={"title": "Vision-Language-Action with Adaptive Robot Policy (ARP)"}))
    repo.save_run(SourceRun(source="arxiv", started_at=NOW - timedelta(days=1),
        finished_at=NOW - timedelta(days=1), status="ok", coverage_id="test", item_count=1, error_code=None))
    repo.save_run(SourceRun(source="arxiv", started_at=NOW, finished_at=NOW,
        status="failed", coverage_id="test", item_count=0, error_code="timeout"))
    repo.save_edges([EvidenceEdge(id="edge", source_id="vla", target_id="doc", relation="mentions",
        evidence_url=document().url, evidence_location="abstract", available_at=NOW, review_status="proposed")])
    return repo


def test_export_evidence_and_stale_source(tmp_path):
    repo = populated(tmp_path)
    out = tmp_path / "site"
    export_site(repo, str(out), NOW)
    dashboard = DashboardPayload.model_validate(read(out, "dashboard.json"))
    assert dashboard.source_runs[0].status == "failed"
    assert dashboard.source_runs[1].status == "ok" and dashboard.source_runs[1].finished_at == NOW - timedelta(days=1)
    assert dashboard.candidates
    for item in dashboard.candidates:
        topic = TopicDetail.model_validate(read(out, f"topics/{item.entity_id}.json"))
        assert set(item.evidence_ids) <= {d.id for d in topic.documents}
        assert topic.summary is None and item.summary is None
    graph = GraphPayload.model_validate(read(out, "graph.json"))
    assert [e.relation for e in graph.edges] == ["mentions"]
    assert {e.source_id for e in graph.edges} | {e.target_id for e in graph.edges} <= {n.id for n in graph.nodes}
    for node in graph.nodes:
        assert (out / "topics" / f"{node.id}.json").exists()
    assert read(out, "topics/vla.json")["evidence_edges"][0]["evidence_location"] == "abstract"
    assert read(out, "topics/vla.json")["observations"] == []
    assert next(t for t in dashboard.trends if t.entity_id == "vla").share_28d is None


def test_export_contains_no_secret(tmp_path, monkeypatch):
    sentinel = "synthetic-export-secret-only"
    monkeypatch.setenv("GEMINI_API_KEY", sentinel)
    monkeypatch.setattr(LLMClient, "from_env", lambda _: None)
    out = tmp_path / "site"
    export_site(populated(tmp_path), str(out), NOW)
    assert all(sentinel not in p.read_text(encoding="utf-8") for p in out.rglob("*.json"))


def test_export_rejects_secret_in_source_before_writing(tmp_path, monkeypatch):
    sentinel = "synthetic-source-secret-only"
    monkeypatch.setenv("GEMINI_API_KEY", sentinel)
    monkeypatch.setattr(LLMClient, "from_env", lambda _: None)
    repo = Repository(str(tmp_path / "radar.db"))
    repo.upsert_document(document().model_copy(update={"title": "Vision-Language-Action " + sentinel}))
    out = tmp_path / "site"
    with pytest.raises(ValueError, match="configured secret"):
        export_site(repo, str(out), NOW)
    assert not out.exists()


def test_empty_graph_is_valid(tmp_path):
    out = tmp_path / "site"
    export_site(Repository(str(tmp_path / "radar.db")), str(out), NOW)
    graph = GraphPayload.model_validate(read(out, "graph.json"))
    assert graph.nodes == [] and graph.edges == [] and graph.generated_at == NOW


def test_cutoff_excludes_future_documents_runs_observations_and_edges(tmp_path):
    repo = populated(tmp_path)
    future = NOW + timedelta(days=1)
    repo.upsert_document(document("future").model_copy(update={"available_at": future}))
    repo.save_observations([Observation(entity_id="future", metric="count_28d", value=9,
        available_at=NOW, observed_at=future, source="fixture", coverage_id="test", state="ok")])
    repo.save_run(SourceRun(source="future", started_at=future, finished_at=future,
        status="ok", coverage_id="future", item_count=1, error_code=None))
    repo.save_edges([EvidenceEdge(id="future", source_id="future", target_id="vla", relation="mentions",
        evidence_url="https://example.org/future", evidence_location=None, available_at=future, review_status="proposed")])
    out = tmp_path / "site"
    export_site(repo, str(out), NOW)
    assert all("future" not in p.read_text(encoding="utf-8") for p in out.rglob("*.json"))
    with pytest.raises(ValueError, match="timezone-aware"):
        export_site(repo, str(out), NOW.replace(tzinfo=None))


def test_llm_failure_does_not_fail_export(tmp_path, monkeypatch):
    fake = Fake(error=RuntimeError("429"))
    monkeypatch.setattr(LLMClient, "from_env", lambda db: LLMClient(db, generate=fake, config=CONFIG))
    out = tmp_path / "site"
    export_site(populated(tmp_path), str(out), NOW)
    assert fake.calls
    assert all(c["summary"] is None for c in read(out, "dashboard.json")["candidates"])


def test_successful_summary_in_candidate_and_topic(tmp_path, monkeypatch):
    import radar.llm as llm
    from datetime import datetime
    class FixedDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return NOW
    monkeypatch.setattr(llm, "datetime", FixedDatetime)
    monkeypatch.setattr(LLMClient, "from_env", lambda db: LLMClient(db, generate=Fake(), config=CONFIG))
    out = tmp_path / "site"
    export_site(populated(tmp_path), str(out), NOW)
    dashboard = read(out, "dashboard.json")
    assert dashboard["candidates"]
    for candidate in dashboard["candidates"]:
        topic = read(out, f"topics/{candidate['entity_id']}.json")
        assert candidate["summary"] is not None
        assert topic["summary"] == candidate["summary"]


def test_later_summary_is_annotation_and_does_not_change_as_of_ranking(tmp_path, monkeypatch):
    import radar.export as exporter
    summary = CandidateSummary(why_new="Hypothesis", difference="Unknown", limitations=[],
        model="fake", generated_at=NOW + timedelta(days=1), source_document_ids=["doc"])
    monkeypatch.setattr(exporter, "summarize", lambda *_: summary)
    out = tmp_path / "site"
    repo = populated(tmp_path)
    export_site(repo, str(out), NOW)
    annotated = read(out, "dashboard.json")
    assert annotated["candidates"]
    assert all(c["summary"]["generated_at"] == "2026-10-19T00:00:00Z" for c in annotated["candidates"])
    monkeypatch.setattr(exporter, "summarize", lambda *_: None)
    export_site(repo, str(out), NOW)
    raw = read(out, "dashboard.json")
    assert annotated["trends"] == raw["trends"]
    for item in annotated["candidates"]:
        item["summary"] = None
    assert annotated == raw


def test_safe_entity_ids_are_reversible_and_collision_free():
    import base64
    for entity in ["new_term:abc", "../escape", "CON", "한글", "~abc", "a/b"]:
        wire = _wire_id(entity)
        assert ":" not in wire and "/" not in wire and "\\" not in wire
        assert base64.urlsafe_b64decode(wire[1:] + "=" * (-len(wire[1:]) % 4)).decode() == entity
    assert _wire_id("vla") == "vla"


def test_stale_topic_files_removed(tmp_path):
    out = tmp_path / "site"
    export_site(populated(tmp_path), str(out), NOW)
    old = out / "topics" / "old.json"
    old.write_text("{}", encoding="utf-8")
    export_site(Repository(str(tmp_path / "empty.db")), str(out), NOW - timedelta(days=1))
    assert not old.exists()
    assert not list((out / "topics").glob("~*.json"))


def test_frontend_types_match_backend_field_sets_and_fixtures():
    # Read-only: catches frontend contract drift without editing worker-owned files.
    source = (ROOT / "frontend/src/api/types.ts").read_text(encoding="utf-8")
    from radar import contracts
    for name, body in re.findall(r"export interface (\w+)\s*\{([^}]+)\}", source):
        model = getattr(contracts, name)
        fields = set(re.findall(r"^\s*(\w+):", body, re.M))
        assert set(model.model_fields) == fields, name
    fixture_root = ROOT / "frontend/public/data"
    DashboardPayload.model_validate_json((fixture_root / "dashboard.json").read_text(encoding="utf-8"))
    GraphPayload.model_validate_json((fixture_root / "graph.json").read_text(encoding="utf-8"))
    for path in (fixture_root / "topics").glob("*.json"):
        TopicDetail.model_validate_json(path.read_text(encoding="utf-8"))


def test_site_fixtures_match_contracts():
    root = ROOT / "tests/fixtures/site-data"
    DashboardPayload.model_validate_json((root / "dashboard.json").read_text(encoding="utf-8"))
    GraphPayload.model_validate_json((root / "graph.json").read_text(encoding="utf-8"))
    TopicDetail.model_validate_json((root / "topics/sample.json").read_text(encoding="utf-8"))
