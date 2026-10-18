"""OpenAlex works metadata under a conservative free daily budget."""
import json
import os
from urllib.parse import urlencode

from radar.contracts import Document
from . import base
from .normalize import arxiv_id, doi_id


def parse_work(work, observed_at):
    identifier = work["id"].rsplit("/", 1)[-1]
    ids = work.get("ids") or {}
    identity = doi_id(work.get("doi") or ids.get("doi"))
    locations = work.get("locations") or []
    if work.get("primary_location"):
        locations = [work["primary_location"], *locations]
    url = work["id"]
    for location in locations:
        for key in ("landing_page_url", "pdf_url"):
            candidate = location.get(key)
            if candidate:
                identity = identity or arxiv_id(candidate)
                if url == work["id"]:
                    url = candidate
    inverted = work.get("abstract_inverted_index")
    abstract = None
    if inverted:
        words = sorted((position, word) for word, positions in inverted.items() for position in positions)
        abstract = " ".join(word for _, word in words)
    # OpenAlex provides day precision, not an exact public timestamp. Noon or
    # midnight would fabricate precision; keep both public timestamps unknown.
    return Document(id=f"openalex:{identifier}", source="openalex", source_id=identifier,
                    canonical_id=identity or f"openalex:{identifier}", title=work["title"], abstract=abstract,
                    url=url, version=None, published_at=None, first_public_at=None,
                    observed_at=observed_at, available_at=observed_at,
                    status="retracted" if work.get("is_retracted") else "unknown")


def collect_openalex(since, cutoff, settings, state):
    key = os.environ.get("OPENALEX_API_KEY")
    if not key:
        return [], base.run("openalex", base.now(), None, [], "missing_api_key", disabled=True)
    coverage = base.coverage_id("openalex", settings)
    attempts = 0

    def reserve():
        nonlocal attempts
        if attempts >= min(100, settings.get("max_requests_per_run", 100)):
            raise base.FetchError("request_budget_exhausted")
        state.reserve_openalex(settings.get("daily_budget_milliusd", 950))
        attempts += 1

    def page(cursor, observed):
        params = {"filter": f"from_publication_date:{since:%Y-%m-%d},to_publication_date:{cutoff:%Y-%m-%d}",
                  "search": settings.get("search", "robot learning"), "cursor": cursor,
                  "per_page": min(100, max(1, settings.get("page_size", 100)))}
        data = json.loads(base.get("https://api.openalex.org/works?" + urlencode(params),
                                  headers={"Authorization": f"Bearer {key}"}, reserve=reserve,
                                  limiter=base.OPENALEX_LIMITER))
        works = data["results"]
        next_cursor = data["meta"].get("next_cursor")
        if not works and next_cursor:
            raise base.FetchError("unexpected_empty_page")
        return [parse_work(work, observed) for work in works], next_cursor

    return base.paged("openalex", since, cutoff, settings, state, coverage, "*", page)
