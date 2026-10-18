"""Conservative identity normalization; titles alone never establish identity."""
import re
from urllib.parse import unquote

from radar.contracts import Document

_ARXIV = re.compile(r"(?:arxiv:|(?:https?://)?(?:export\.)?arxiv\.org/(?:abs|pdf)/)([a-z-]+(?:\.[A-Z]{2})?/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?(?:$|[?#\s])", re.I)


def arxiv_id(value: str | None) -> str | None:
    match = _ARXIV.search(value or "")
    return f"arxiv:{match[1].lower()}" if match else None


def doi_id(value: str | None) -> str | None:
    value = unquote(value or "").strip()
    value = re.sub(r"^(?:https?://(?:dx\.)?doi.org/|doi:)", "", value, flags=re.I)
    return f"doi:{value.lower()}" if re.fullmatch(r"10\.\d{4,9}/\S+", value) else None


def canonicalize(documents: list[Document]) -> list[Document]:
    """Assign shared canonical IDs while keeping every source/version record.

    Explicit DOI/arXiv links bridge sources. Unknown titles and abbreviations do
    not. Repeated identical document IDs are idempotent, conflicting payloads
    use the newest observation. Inputs are not mutated.
    """
    unique = {}
    for doc in documents:
        if doc.id not in unique or doc.observed_at > unique[doc.id].observed_at:
            unique[doc.id] = doc
    docs = list(unique.values())
    parent = {}

    def find(key):
        parent.setdefault(key, key)
        if parent[key] != key:
            parent[key] = find(parent[key])
        return parent[key]

    def rank(key):
        return (0 if key.startswith("doi:") else 1 if key.startswith("arxiv:") else 2, key)

    keys = []
    for doc in docs:
        aliases = {doc.canonical_id}
        for value in (doc.source_id, doc.url, doc.canonical_id):
            identity = arxiv_id(value) or doi_id(value)
            if identity:
                aliases.add(identity)
        roots = {find(a) for a in aliases}
        root = min(roots, key=rank)
        for other in roots:
            parent[other] = root
        keys.append(doc.canonical_id)
    return [doc.model_copy(update={"canonical_id": find(key)}) for doc, key in zip(docs, keys)]
