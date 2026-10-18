"""Offline collector contracts; all network responses are synthetic fixtures."""
import json
import io
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError

import pytest

from radar.collectors import canonicalize
from radar.collectors.arxiv import parse_feed
from radar.collectors.openreview import parse_note


FIXTURES = Path(__file__).parent / "fixtures"
NOW = datetime(2026, 10, 18, tzinfo=timezone.utc)


def fixture(name):
    return json.loads((FIXTURES / f"{name}.json").read_text(encoding="utf-8"))


def test_preprint_and_venue_version_count_once():
    preprints, _ = parse_feed(fixture("arxiv")["body"].encode(), NOW)
    venue = parse_note(fixture("openreview")["notes"][0], NOW, 2)
    docs = canonicalize([*preprints, venue])
    assert len(docs) == 3
    assert len({d.canonical_id for d in docs}) == 1
    assert [d.published_at.day for d in docs] == [1, 5, 10]
    assert docs[1].first_public_at.day == 1
    assert docs[2].status == "unknown"


def test_partial_fetch_not_empty_success(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.arxiv import collect_arxiv

    settings = {"categories": ["cs.RO"], "page_size": 2, "max_pages": 5}
    calls = []

    def fetch(url, **kwargs):
        calls.append(url)
        if len(calls) > 1:
            raise base.FetchError("http_503")
        return fixture("arxiv")["body"].encode()

    monkeypatch.setattr(base, "get", fetch)
    docs, run = collect_arxiv(NOW.replace(day=1), NOW, settings,
                              base.State(tmp_path / "state.db"))
    assert len(docs) == run.item_count == 2
    assert run.status == "partial"
    assert run.error_code == "http_503"


def test_resume_replays_completed_pages_without_refetch(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.arxiv import collect_arxiv

    settings = {"categories": ["cs.RO"], "page_size": 2, "max_pages": 5}
    state = base.State(tmp_path / "state.db")
    body = fixture("arxiv")["body"]
    calls = []

    def fail_second(url, **kwargs):
        calls.append(url)
        if "start=2" in url:
            raise base.FetchError("http_429")
        return body.encode()

    monkeypatch.setattr(base, "get", fail_second)
    first, run = collect_arxiv(NOW.replace(day=1), NOW, settings, state)
    assert run.status == "partial"

    def finish(url, **kwargs):
        assert "start=2" in url
        calls.append(url)
        # Fixture last page repeats a source record: checkpoint stays idempotent.
        return body.replace("<opensearch:totalResults>3", "<opensearch:totalResults>2").encode()

    monkeypatch.setattr(base, "get", finish)
    docs, run = collect_arxiv(NOW.replace(day=1), NOW, settings, base.State(tmp_path / "state.db"))
    assert run.status == "ok"
    assert len(docs) == len(first) == 2
    assert len(calls) == 3
    monkeypatch.setattr(base, "get", lambda *a, **k: pytest.fail("completed checkpoint fetched"))
    assert collect_arxiv(NOW.replace(day=1), NOW, settings, state)[1].status == "ok"


def test_first_page_failure_is_failed_not_empty_success(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.arxiv import collect_arxiv

    def fail(*a, **k):
        raise base.FetchError("http_503")

    monkeypatch.setattr(base, "get", fail)
    docs, run = collect_arxiv(NOW.replace(day=1), NOW, {}, base.State(tmp_path / "state.db"))
    assert docs == [] and run.status == "failed" and run.item_count == 0


def test_bounded_retry_and_secret_safe_error(monkeypatch):
    from radar.collectors import base

    calls = []
    sleeps = []

    def fail(request, **kwargs):
        calls.append(request)
        raise HTTPError("https://invalid/?secret=DO_NOT_LEAK", 429, "DO_NOT_LEAK", {"Retry-After": "1"}, io.BytesIO())

    monkeypatch.setattr(base, "urlopen", fail)
    monkeypatch.setattr(base.time, "sleep", sleeps.append)
    with pytest.raises(base.FetchError, match="^http_429$") as error:
        base.get("https://invalid/?secret=DO_NOT_LEAK")
    assert len(calls) == 3 and sleeps == [1, 2]
    assert "DO_NOT_LEAK" not in str(error.value)


def test_nonretryable_error_is_not_retried(monkeypatch):
    from radar.collectors import base

    calls = []

    def fail(*args, **kwargs):
        calls.append(1)
        raise HTTPError("https://invalid", 403, "forbidden", {}, io.BytesIO())

    monkeypatch.setattr(base, "urlopen", fail)
    with pytest.raises(base.FetchError, match="http_403"):
        base.get("https://invalid")
    assert len(calls) == 1


def test_shared_arxiv_limiter_waits_and_holds_connection_lock(monkeypatch):
    from radar.collectors import base

    limiter = base.Limiter(3)
    ticks = iter([0.0, 1.0, 3.0])
    sleeps = []
    monkeypatch.setattr(base.time, "monotonic", lambda: next(ticks))
    monkeypatch.setattr(base.time, "sleep", sleeps.append)

    def operation():
        assert not limiter.lock.acquire(blocking=False)
        return b"ok"

    assert limiter.call(operation) == limiter.call(operation) == b"ok"
    assert sleeps == [2.0]


def test_coverage_is_stable_but_seed_scope_is_separate():
    from radar.collectors import base
    from radar.collectors.arxiv import query

    settings = {"categories": ["cs.RO", "cs.AI"], "seed_terms": ["World Model", "JEPA"]}
    broad = query(NOW.replace(day=1), NOW, settings)
    seed = query(NOW.replace(day=1), NOW, settings, True)
    assert "cat:cs.RO" in broad and 'ti:"World Model"' not in broad
    assert 'ti:"World Model"' in seed and "cat:cs.RO" not in seed
    assert base.coverage_id("arxiv", settings) != base.coverage_id("arxiv_seed", settings)
    assert base.coverage_id("arxiv", settings) != base.coverage_id("arxiv", {**settings, "categories": ["cs.RO"]})


def test_titles_alone_never_merge_and_inputs_unchanged():
    docs, _ = parse_feed(fixture("arxiv")["body"].encode(), NOW)
    original = docs[0].model_dump()
    unrelated = docs[0].model_copy(update={"id": "other", "source_id": "other", "source": "other",
                      "url": "https://example.org/other", "canonical_id": "other"})
    result = canonicalize([docs[0], docs[0], unrelated])
    assert len(result) == 2 and len({d.canonical_id for d in result}) == 2
    assert docs[0].model_dump() == original
    assert canonicalize(result) == result


def test_openalex_doi_bridge_and_unknown_dates():
    from radar.collectors.openalex import parse_work

    docs, _ = parse_feed(fixture("arxiv")["body"].encode(), NOW)
    work = parse_work(fixture("openalex")["results"][0], NOW)
    note = parse_note(fixture("openreview")["notes"][0], NOW, 2)
    result = canonicalize([*docs, note, work])
    assert len(result) == 4 and len({d.canonical_id for d in result}) == 1
    assert work.abstract == "Synthetic robot policy"
    assert work.published_at is work.first_public_at is None
    assert all(d.available_at == NOW for d in result)


def test_openreview_api1_and_private_creation_time():
    note = {"id": "legacy", "forum": "forum", "cdate": 1790812800000,
            "content": {"title": "Public submission", "abstract": None}}
    doc = parse_note(note, NOW, 1)
    assert doc.published_at is doc.first_public_at is None
    assert doc.available_at == NOW and doc.status == "unknown"
    assert doc.canonical_id == "openreview:forum"


def test_openreview_requires_verified_manifest(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.openreview import collect_openreview

    monkeypatch.setattr(base, "get", lambda *a, **k: pytest.fail("unverified venue fetched"))
    docs, run = collect_openreview(NOW.replace(day=1), NOW, {"venues": []}, base.State(tmp_path / "state.db"))
    assert docs == [] and run.status == "disabled" and run.error_code == "unverified_venue"


@pytest.mark.parametrize("api_version", [1, 2])
def test_openreview_venue_pagination(monkeypatch, tmp_path, api_version):
    from radar.collectors import base
    from radar.collectors.openreview import collect_openreview

    notes = fixture("openreview")["notes"]
    if api_version == 1:
        notes[0]["content"] = {k: v["value"] for k, v in notes[0]["content"].items()}
    calls = []

    def fetch(url, **kwargs):
        calls.append(url)
        return json.dumps({"notes": notes, "count": 1}).encode()

    monkeypatch.setattr(base, "get", fetch)
    settings = {"venues": [{"venue_id": "synthetic", "invitation": "synthetic/-/Submission",
                             "api_version": api_version, "verification": "verified"}]}
    docs, run = collect_openreview(NOW.replace(day=1), NOW, settings, base.State(tmp_path / "state.db"))
    assert len(docs) == 1 and run.status == "ok"
    assert ("api2.openreview.net" if api_version == 2 else "api.openreview.net") in calls[0]


def test_openalex_missing_key_is_disabled(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.openalex import collect_openalex

    monkeypatch.delenv("OPENALEX_API_KEY", raising=False)
    monkeypatch.setattr(base, "get", lambda *a, **k: pytest.fail("missing key fetched"))
    docs, run = collect_openalex(NOW.replace(day=1), NOW, {}, base.State(tmp_path / "state.db"))
    assert docs == [] and run.status == "disabled" and run.error_code == "missing_api_key"


def test_openalex_budget_counts_attempts_and_stops_before_next_get(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.openalex import collect_openalex

    monkeypatch.setenv("OPENALEX_API_KEY", "synthetic-test-key")
    calls = []

    def fetch(url, **kwargs):
        kwargs["reserve"]()
        calls.append(url)
        assert "synthetic-test-key" not in url
        data = fixture("openalex")
        data["meta"]["next_cursor"] = "next"
        return json.dumps(data).encode()

    monkeypatch.setattr(base, "get", fetch)
    docs, run = collect_openalex(NOW.replace(day=1), NOW, {"max_requests_per_run": 1}, base.State(tmp_path / "state.db"))
    assert len(docs) == 1 and run.status == "partial"
    assert run.error_code == "request_budget_exhausted" and len(calls) == 1


def test_openalex_daily_budget_survives_new_state_instance(tmp_path):
    from radar.collectors import base

    path = tmp_path / "state.db"
    base.State(path).reserve_openalex(1)
    with pytest.raises(base.FetchError, match="daily_budget_exhausted"):
        base.State(path).reserve_openalex(1)


def test_invalid_response_does_not_erase_checkpoint(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.arxiv import collect_arxiv

    responses = iter([fixture("arxiv")["body"].encode(), b"<feed>broken"])
    monkeypatch.setattr(base, "get", lambda *a, **k: next(responses))
    docs, run = collect_arxiv(NOW.replace(day=1), NOW, {"page_size": 2}, base.State(tmp_path / "state.db"))
    assert len(docs) == 2 and run.status == "partial" and run.error_code == "invalid_xml"


def test_public_dispatch_validates_timestamps_and_config():
    from radar.collectors import collect

    with pytest.raises(ValueError, match="timezone"):
        collect("arxiv", datetime(2026, 10, 1), NOW)
    with pytest.raises(ValueError, match="since"):
        collect("arxiv", NOW, NOW.replace(day=1))
    with pytest.raises(ValueError, match="unknown source"):
        collect("invalid", NOW, NOW)
    for source in ("openreview", "openalex"):
        docs, run = collect(source, NOW.replace(day=1), NOW)
        assert docs == [] and run.status == "disabled"


def test_closed_window_and_real_observation_timestamp(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.arxiv import collect_arxiv

    body = fixture("arxiv")["body"].replace("<opensearch:totalResults>3", "<opensearch:totalResults>2")
    monkeypatch.setattr(base, "get", lambda *a, **k: body.encode())
    docs, run = collect_arxiv(NOW.replace(day=5), NOW.replace(day=5), {}, base.State(tmp_path / "state.db"))
    assert run.status == "ok" and len(docs) == 1
    assert docs[0].version == "v2" and docs[0].first_public_at.day == 1
    assert docs[0].published_at == NOW.replace(day=5)
    assert docs[0].available_at == docs[0].observed_at > NOW.replace(day=5)


def test_openreview_revisions_are_preserved():
    note = fixture("openreview")["notes"][0]
    first = parse_note(note, NOW, 2)
    note["mdate"] += 1000
    second = parse_note(note, NOW, 2)
    docs = canonicalize([first, second])
    assert len(docs) == 2 and docs[0].id != docs[1].id
    assert docs[0].canonical_id == docs[1].canonical_id


def test_legitimate_empty_result_and_page_limit(monkeypatch, tmp_path):
    from radar.collectors import base
    from radar.collectors.arxiv import collect_arxiv

    empty = b'<feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://a9.com/-/spec/opensearch/1.1/"><s:totalResults>0</s:totalResults></feed>'
    monkeypatch.setattr(base, "get", lambda *a, **k: empty)
    state = base.State(tmp_path / "state.db")
    docs, run = collect_arxiv(NOW.replace(day=1), NOW, {}, state)
    assert docs == [] and run.status == "ok"
    monkeypatch.setattr(base, "get", lambda *a, **k: fixture("arxiv")["body"].encode())
    docs, run = collect_arxiv(NOW.replace(day=1), NOW, {"max_pages": 1}, state)
    assert len(docs) == 2 and run.status == "partial" and run.error_code == "page_limit"


def test_429_retry_recovers_and_reserves_every_attempt(monkeypatch):
    from radar.collectors import base

    attempts, reservations = [], []

    class Response(io.BytesIO):
        pass

    def fetch(*args, **kwargs):
        attempts.append(1)
        if len(attempts) == 1:
            raise HTTPError("https://invalid", 429, "rate limited", {}, io.BytesIO())
        return Response(b"public metadata")

    monkeypatch.setattr(base, "urlopen", fetch)
    monkeypatch.setattr(base.time, "sleep", lambda seconds: None)
    assert base.get("https://invalid", reserve=lambda: reservations.append(1)) == b"public metadata"
    assert len(reservations) == len(attempts) == 2
