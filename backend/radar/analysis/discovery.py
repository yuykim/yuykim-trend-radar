"""Deterministic candidate heuristics, not validated technology predictions.

Windows use first_public_at; first_seen_at is earliest usable availability,
not a claim about technology invention. Terms use full-name/acronym pairs;
ambiguous acronyms never identify or merge entities. All counts are unique
canonical documents. Low support is a warning, not a filtering threshold.
"""

from __future__ import annotations

import hashlib
import itertools
import math
import re
from collections import Counter, defaultdict
from datetime import datetime

from ..contracts import Candidate, Document
from .trends import MINIMUM_SUPPORT, WINDOW, _contains, _text, _visible_documents

_PAIR = re.compile(r"\b((?:[A-Za-z][A-Za-z-]*\s+){1,7}[A-Za-z][A-Za-z-]*)\s*\(([A-Z][A-Z0-9-]{1,11})\)")
_STOP = set("a an and are as at be by for from in is it of on or that the this to using via we with".split())


def _pairs(text):
    for match in _PAIR.finditer(text):
        words, acronym = match.group(1).split(), match.group(2)
        # Trim contextual words before the expansion by requiring initials.
        for start in range(len(words)):
            full = " ".join(words[start:])
            initials = "".join(w[0] for w in re.split(r"[\s-]+", full)).upper()
            if initials == acronym.replace("-", ""):
                yield full.casefold(), acronym
                break


def _clusters(documents):
    """Connected components of cosine >= .35, smoothed TF-IDF, pure Python.

    Pairwise comparison is O(n²); intended for a bounded batch, no external
    model or vocabulary fitted using future documents.
    """
    tokens = [Counter(w for w in re.findall(r"[a-z][a-z-]{2,}", _text(d).lower()) if w not in _STOP)
              for d in documents]
    frequency = Counter(token for row in tokens for token in row)
    vectors = []
    for row in tokens:
        vector = {word: (1 + math.log(count)) * (1 + math.log((1 + len(tokens)) / (1 + frequency[word])))
                  for word, count in row.items()}
        norm = math.sqrt(sum(v * v for v in vector.values()))
        vectors.append({w: v / norm for w, v in vector.items()} if norm else {})
    neighbors = defaultdict(set)
    for i, left in enumerate(vectors):
        for j in range(i):
            similarity = sum(v * vectors[j].get(w, 0) for w, v in left.items())
            if similarity >= .35:
                neighbors[i].add(j)
                neighbors[j].add(i)
    seen = set()
    for i in sorted(neighbors):
        if i in seen:
            continue
        component, pending = set(), [i]
        while pending:
            node = pending.pop()
            if node in component:
                continue
            component.add(node)
            pending.extend(neighbors[node] - component)
        seen.update(component)
        words = Counter()
        for node in component:
            words.update(vectors[node])
        label = " ".join(w for w, _ in sorted(words.items(), key=lambda p: (-p[1], p[0]))[:5])
        yield label, [documents[node] for node in sorted(component)]


def _discover(documents, known_aliases, cutoff, minimum_support):
    docs = _visible_documents(documents, cutoff)
    recent = [d for d in docs if cutoff - WINDOW < d.first_public_at <= cutoff]
    previous = [d for d in docs if cutoff - 2 * WINDOW < d.first_public_at <= cutoff - WINDOW]
    terms, combinations = defaultdict(list), defaultdict(list)
    assigned = set()
    all_names = [name.casefold() for names in known_aliases.values() for name in names]
    for doc in docs:
        text = _text(doc)
        pairs = set(_pairs(text))
        for full, acronym in pairs:
            if full not in all_names:
                terms[(full, acronym)].append(doc)
                assigned.add(doc.id)
        entities = sorted(entity for entity, names in known_aliases.items()
                          if any(_contains(text, name) for name in names))
        if entities:
            assigned.add(doc.id)
        for pair in itertools.combinations(entities, 2):
            combinations[pair].append(doc)

    candidates = []

    def add(kind, identity, label, evidence, prior_count, method):
        current_docs = [d for d in evidence if cutoff - WINDOW < d.first_public_at <= cutoff]
        count = len(current_docs)
        if not count:
            return
        entity = kind + ":" + hashlib.sha256(identity.encode()).hexdigest()[:20]
        reasons = [label, method,
                   f"count_28d={count}; previous_count_28d={prior_count}; increase={count - prior_count}",
                   f"support={'low_support' if count < minimum_support else 'ok'}; minimum_support={minimum_support}",
                   f"as_of={cutoff.isoformat()}; proposed candidate; novelty requires human review"]
        reasons += [f"evidence: {d.id} {d.url}" for d in sorted(current_docs, key=lambda d: d.id)]
        candidates.append(Candidate(id=entity, entity_id=entity, kind=kind,
                                    first_seen_at=min(max(d.available_at, d.observed_at) for d in evidence),
                                    reasons=reasons, evidence_ids=sorted(d.id for d in current_docs), review_status="proposed"))

    for (full, acronym), evidence in sorted(terms.items()):
        # Any earlier public evidence prevents a historical term being called new.
        if any(d.first_public_at <= cutoff - WINDOW for d in evidence):
            continue
        add("new_term", full + "|" + acronym, f"{full} ({acronym})", evidence, 0,
            "full-name/acronym pair outside known aliases; acronym is not an alias assignment")
    for pair, evidence in sorted(combinations.items()):
        current_count = sum(cutoff - WINDOW < d.first_public_at <= cutoff for d in evidence)
        old_count = sum(d in previous for d in evidence)
        if current_count > old_count:
            add("new_combination", "|".join(pair), " + ".join(pair), evidence, old_count,
                "increased within-document topic cooccurrence; not a technology relation")
    # Include both windows when fitting TF-IDF, then require a recent increase.
    unassigned = [d for d in previous + recent if d.id not in assigned]
    for label, evidence in _clusters(unassigned):
        old_count = sum(d in previous for d in evidence)
        current_count = len(evidence) - old_count
        if current_count > old_count:
            add("new_cluster", label, label, evidence, old_count,
                "unassigned document TF-IDF cosine cluster >=0.35; cluster is not confirmed technology")
    return sorted(candidates, key=lambda c: (-len(c.evidence_ids), c.kind, c.entity_id))


def discover(documents: list[Document], known_aliases: dict[str, list[str]], cutoff: datetime) -> list[Candidate]:
    """Return at most five ranked proposed candidates, preserving low-support rows."""
    return _discover(documents, known_aliases, cutoff, MINIMUM_SUPPORT)[:5]


def sensitivity_analysis(documents: list[Document], known_aliases: dict[str, list[str]], cutoff: datetime) -> dict:
    """Compare support thresholds 3/5/10 under the same five-alert budget."""
    report = {}
    for threshold in (3, 5, 10):
        candidates = _discover(documents, known_aliases, cutoff, threshold)[:5]
        supported = sum(len(c.evidence_ids) >= threshold for c in candidates)
        report[threshold] = {"candidates": len(candidates), "supported": supported,
                             "low_support": len(candidates) - supported}
    return report
