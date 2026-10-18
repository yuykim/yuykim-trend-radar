"""Public submission notes only; venue/API version must be verified in manifest."""
import json
from urllib.parse import urlencode

from radar.contracts import Document
from . import base
from .normalize import arxiv_id, doi_id


def content_value(content, name, api_version):
    value = content.get(name)
    return value.get("value") if api_version == 2 and isinstance(value, dict) else value


def parse_note(note, observed_at, api_version):
    content = note.get("content", {})
    value = lambda key: content_value(content, key, api_version)
    identifier = note["id"]
    title = value("title")
    if not title:
        raise base.FetchError("missing_title")
    # pdate is public release; cdate/tcdate can be private creation dates.
    public = base.timestamp(note.get("pdate"))
    identity = doi_id(value("doi"))
    for key in ("arxiv", "arxiv_id", "arxiv_url", "paper_url", "url"):
        raw = value(key)
        if isinstance(raw, str):
            identity = identity or arxiv_id(raw if not key.startswith("arxiv") or ":" in raw else f"arxiv:{raw}")
    version = str(note["mdate"]) if note.get("mdate") is not None else None
    return Document(id=f"openreview:{identifier}" + (f":{version}" if version else ""), source="openreview", source_id=identifier,
                    canonical_id=identity or f"openreview:{note.get('forum') or identifier}",
                    title=title, abstract=value("abstract"), url=f"https://openreview.net/forum?id={identifier}",
                    version=version,
                    published_at=public, first_public_at=public, observed_at=observed_at,
                    available_at=observed_at, status="unknown")


def collect_openreview(since, cutoff, settings, state):
    venues = settings.get("venues", [])
    if not venues or any(v.get("verification") != "verified" or v.get("api_version") not in (1, 2)
                         or not v.get("invitation") for v in venues):
        return [], base.run("openreview", base.now(), None, [], "unverified_venue", disabled=True)
    coverage = base.coverage_id("openreview", settings)
    size = min(1000, max(1, settings.get("page_size", 100)))

    def page(cursor, observed):
        venue_index, offset = cursor
        venue = venues[venue_index]
        host = "api2.openreview.net" if venue["api_version"] == 2 else "api.openreview.net"
        url = f"https://{host}/notes?" + urlencode({"invitation": venue["invitation"], "limit": size,
                                                 "offset": offset, "sort": "id:asc"})
        data = json.loads(base.get(url))
        notes = data["notes"]
        docs = [parse_note(note, observed, venue["api_version"]) for note in notes]
        total = data.get("count")
        if not notes and total is not None and offset < total:
            raise base.FetchError("unexpected_empty_page")
        more = offset + len(notes) < total if total is not None else len(notes) == size
        next_cursor = [venue_index, offset + len(notes)] if more else ([venue_index + 1, 0] if venue_index + 1 < len(venues) else None)
        return docs, next_cursor

    return base.paged("openreview", since, cutoff, settings, state, coverage, [0, 0], page)
