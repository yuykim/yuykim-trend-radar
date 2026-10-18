"""arXiv Atom collection, with separate broad and seed coverage."""
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlencode

from radar.contracts import Document
from . import base
from .normalize import arxiv_id, doi_id

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
SEARCH = "{http://a9.com/-/spec/opensearch/1.1/}"


def parse_feed(body: bytes, observed_at):
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        raise base.FetchError("invalid_xml") from None
    if root.tag != ATOM + "feed":
        raise base.FetchError("invalid_feed")
    docs = []
    for entry in root.findall(ATOM + "entry"):
        url = entry.findtext(ATOM + "id") or ""
        identity = arxiv_id(url)
        if not identity:
            raise base.FetchError("invalid_arxiv_entry")
        version = re.search(r"v(\d+)$", url)
        version = f"v{version[1]}" if version else None
        first = base.timestamp(entry.findtext(ATOM + "published"))
        updated = base.timestamp(entry.findtext(ATOM + "updated"))
        # Atom published refers to v1; updated refers to the returned version.
        published = updated if version not in (None, "v1") else first
        title = " ".join((entry.findtext(ATOM + "title") or "").split())
        if not title:
            raise base.FetchError("missing_title")
        source_id = identity.removeprefix("arxiv:") + (version or "")
        docs.append(Document(id=f"arxiv:{source_id}", source="arxiv", source_id=source_id,
                             canonical_id=doi_id(entry.findtext(ARXIV + "doi")) or identity,
                             title=title, abstract=entry.findtext(ATOM + "summary"), url=url,
                             version=version, published_at=published, first_public_at=first,
                             observed_at=observed_at, available_at=observed_at, status="preprint"))
    total_text = root.findtext(SEARCH + "totalResults")
    if total_text is None:
        raise base.FetchError("missing_total")
    return docs, int(total_text)


def query(since, cutoff, settings, seed=False):
    if seed:
        terms = settings.get("seed_terms", [])
        if not terms:
            raise ValueError("seed_terms required")
        scope = " OR ".join(f'ti:"{t}" OR abs:"{t}"' for t in terms)
    else:
        scope = " OR ".join(f"cat:{c}" for c in settings.get("categories", ["cs.RO", "cs.AI", "cs.CV", "cs.LG"]))
    # lastUpdatedDate includes new versions of older preprints.
    return f"({scope}) AND lastUpdatedDate:[{since:%Y%m%d%H%M} TO {cutoff:%Y%m%d%H%M}]"


def collect_arxiv(since, cutoff, settings, state, seed=False):
    source = "arxiv_seed" if seed else "arxiv"
    coverage = base.coverage_id(source, settings)
    search = query(since, cutoff, settings, seed)
    size = min(1000, max(1, settings.get("page_size", 100)))

    def page(offset, observed):
        url = "https://export.arxiv.org/api/query?" + urlencode({"search_query": search, "start": offset,
                     "max_results": size, "sortBy": "lastUpdatedDate", "sortOrder": "ascending"})
        docs, total = parse_feed(base.get(url, limiter=base.ARXIV_LIMITER), observed)
        if not docs and offset < total:
            raise base.FetchError("unexpected_empty_page")
        return docs, offset + len(docs) if offset + len(docs) < total else None

    return base.paged(source, since, cutoff, settings, state, coverage, 0, page)
