import json
from datetime import datetime, timezone

import pytest

from radar.contracts import Candidate, Document
from radar.llm import LLMClient, summarize

NOW = datetime(2026, 10, 18, tzinfo=timezone.utc)
CONFIG = {"model": "fake-flash", "max_calls_per_run": 30, "min_request_interval_seconds": 2}


def document(identifier="doc"):
    return Document(id=identifier, source="synthetic", source_id=identifier,
        canonical_id=identifier, title="Synthetic Adaptive Robot Policy (ARP)",
        abstract="Synthetic fixture, not research evidence.", url=f"https://example.org/{identifier}",
        version="v1", published_at=NOW, first_public_at=NOW, observed_at=NOW,
        available_at=NOW, status="preprint")


def candidate(ids=None):
    return Candidate(id="candidate", entity_id="adaptive-policy", kind="new_term",
        first_seen_at=NOW, reasons=["Synthetic fixture"], evidence_ids=ids or ["doc"],
        review_status="proposed")


class Fake:
    def __init__(self, error=None, urls=None):
        self.calls = []
        self.error, self.urls = error, urls

    def __call__(self, model, documents):
        self.calls.append((model, documents))
        if self.error:
            raise self.error
        return {"why_new": "신규성은 미확인입니다.", "difference": "조건 비교가 필요합니다.",
                "limitations": ["합성 테스트입니다."],
                "source_urls": self.urls if self.urls is not None else [documents[0]["url"]]}


@pytest.fixture
def clients(tmp_path):
    opened = []

    def create(fake, **kwargs):
        client = LLMClient(str(tmp_path / "cache.db"), generate=fake,
                           config=kwargs.pop("config", CONFIG), **kwargs)
        opened.append(client)
        return client

    yield create
    for client in opened:
        client.close()


def test_llm_disabled_returns_none(monkeypatch, tmp_path):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    assert LLMClient.from_env(str(tmp_path / "cache.db")) is None
    assert summarize(candidate(), [document()], None) is None
    assert not (tmp_path / "cache.db").exists()


def test_llm_429_does_not_fail_run(clients, caplog):
    fake = Fake(error=RuntimeError("429 private provider response"))
    assert summarize(candidate(), [document()], clients(fake)) is None
    assert len(fake.calls) == 1
    assert "LLM summary unavailable" in caplog.text
    assert "private provider response" not in caplog.text


def test_summary_cached_by_document_set(clients):
    fake = Fake()
    client = clients(fake)
    docs = [document(), document("other")]
    item = candidate([d.id for d in docs])
    first = summarize(item, docs, client)
    assert first is not None
    assert summarize(item, docs[::-1], client) == first
    # A new client uses the same SQLite cache, even with a zero run budget.
    reopened = clients(fake, config={**CONFIG, "max_calls_per_run": 0})
    assert summarize(item, docs, reopened) == first
    assert len(fake.calls) == 1


def test_cache_invalidated_by_content_model_and_document_set(clients):
    fake = Fake()
    client = clients(fake, config={**CONFIG, "min_request_interval_seconds": 0})
    assert summarize(candidate(), [document()], client)
    assert summarize(candidate(), [document().model_copy(update={"abstract": "Changed"})], client)
    assert summarize(candidate(["other"]), [document("other")], client)
    assert summarize(candidate(), [document()], clients(fake, config={**CONFIG, "model": "other"}))
    assert len(fake.calls) == 4


def test_summary_only_cites_given_documents(clients):
    fake = Fake()
    docs = [document(), document("unrelated")]
    summary = summarize(candidate(), docs, clients(fake))
    assert summary.source_document_ids == ["doc"]
    assert summary.model == "fake-flash" and summary.generated_at.utcoffset().total_seconds() == 0
    assert "LLM 생성, 원문 확인 필요" in summary.limitations
    assert fake.calls[0][1] == [{"title": docs[0].title, "abstract": docs[0].abstract, "url": docs[0].url}]


@pytest.mark.parametrize("urls", [["https://example.org/invented"], []])
def test_unsupported_citations_reject_entire_summary(clients, urls):
    assert summarize(candidate(), [document()], clients(Fake(urls=urls))) is None


def test_budget_counts_failures_and_interval(clients):
    sleeps = []
    fake = Fake(error=RuntimeError("offline"))
    client = clients(fake, config={**CONFIG, "max_calls_per_run": 2}, clock=lambda: 10,
                     sleep=sleeps.append)
    for _ in range(3):
        assert summarize(candidate(), [document()], client) is None
    assert len(fake.calls) == 2 and client.calls == 2 and sleeps == [2]


def test_malformed_response_and_secrets_are_not_logged_or_cached(clients, monkeypatch, caplog):
    sentinel = "synthetic-secret-for-test-only"
    monkeypatch.setenv("GEMINI_API_KEY", sentinel)
    fake = Fake(error=ValueError(sentinel))
    assert summarize(candidate(), [document()], clients(fake)) is None
    leaking = lambda *_: {"why_new": sentinel, "difference": "x", "limitations": [],
                           "source_urls": [document().url]}
    client = clients(leaking)
    assert summarize(candidate(), [document()], client) is None
    assert client._db.execute("SELECT COUNT(*) FROM llm_summaries").fetchone()[0] == 0
    assert sentinel not in caplog.text
    assert summarize(candidate(), [document()], clients(lambda *_: {"bad": "schema"})) is None


def test_no_evidence_does_not_call_client(clients):
    fake = Fake()
    assert summarize(candidate(), [document("unrelated")], clients(fake)) is None
    assert not fake.calls
