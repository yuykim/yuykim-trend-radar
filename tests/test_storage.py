from datetime import datetime, timezone

from radar.contracts import Document, EvidenceEdge, Observation, Review, SourceRun
from radar.storage import Repository


def dt(day: int) -> datetime:
    return datetime(2026, 10, day, tzinfo=timezone.utc)


def doc(identifier: str, available_at):
    return Document(
        id=identifier,
        source="fixture",
        source_id=identifier,
        canonical_id=identifier,
        title=identifier,
        abstract=None,
        url=f"https://example.org/{identifier}",
        version=None,
        published_at=None,
        first_public_at=None,
        observed_at=dt(1),
        available_at=available_at,
        status="unknown",
    )


def test_cutoff_excludes_late_features(tmp_path):
    repo = Repository(str(tmp_path / "radar.db"))
    cutoff = dt(10)
    repo.upsert_document(doc("late", dt(11)))
    repo.upsert_document(doc("on-time", cutoff))
    repo.upsert_document(doc("unknown-time", None))
    repo.save_observations([
        Observation(entity_id="e", metric="citations", value=3, available_at=dt(11), observed_at=dt(11), source="fixture", coverage_id="c", state="ok"),
        Observation(entity_id="e", metric="papers", value=1, available_at=cutoff, observed_at=cutoff, source="fixture", coverage_id="c", state="ok"),
        Observation(entity_id="e", metric="unknown", value=None, available_at=None, observed_at=cutoff, source="fixture", coverage_id="c", state="unknown"),
    ])
    repo.save_edges([
        EvidenceEdge(id="late-edge", source_id="a", target_id="b", relation="uses", evidence_url="https://example.org/e", evidence_location=None, available_at=dt(11), review_status="proposed"),
        EvidenceEdge(id="on-time-edge", source_id="a", target_id="c", relation="uses", evidence_url="https://example.org/e2", evidence_location=None, available_at=cutoff, review_status="verified"),
        EvidenceEdge(id="unknown-edge", source_id="a", target_id="d", relation="uses", evidence_url="https://example.org/e3", evidence_location=None, available_at=None, review_status="proposed"),
    ])
    assert [item.id for item in repo.list_documents(cutoff)] == ["on-time"]
    assert [item.metric for item in repo.list_observations(cutoff)] == ["papers"]
    assert [item.id for item in repo.list_edges(cutoff)] == ["on-time-edge"]


def test_versions_and_review_history_are_preserved(tmp_path):
    repo = Repository(str(tmp_path / "radar.db"))
    first = doc("paper-v1", dt(1)).model_copy(update={"canonical_id": "paper"})
    second = doc("paper-v2", dt(2)).model_copy(update={"canonical_id": "paper", "version": "v2"})
    repo.upsert_document(first)
    repo.upsert_document(second)
    assert {item.id for item in repo.list_documents(dt(3))} == {"paper-v1", "paper-v2"}
    review = Review(candidate_id="candidate", reviewed_at=dt(3), already_known=False, relevant=True, distinct=True, useful=True, minutes_spent=2)
    repo.save_review(review)
    repo.save_review(review.model_copy(update={"useful": False}))
    assert len(repo.list_reviews()) == 2


def test_run_round_trip(tmp_path):
    repo = Repository(str(tmp_path / "radar.db"))
    run = SourceRun(source="fixture", started_at=dt(1), finished_at=dt(1), status="ok", coverage_id="c", item_count=1, error_code=None)
    repo.save_run(run)
    assert repo.list_runs() == [run]
