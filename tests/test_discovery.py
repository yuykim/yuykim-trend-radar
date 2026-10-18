from datetime import datetime, timedelta, timezone

from radar.analysis.discovery import discover, sensitivity_analysis
from radar.contracts import Document

CUTOFF = datetime(2026, 10, 18, tzinfo=timezone.utc)


def doc(index, title, days=1, **updates):
    stamp = CUTOFF - timedelta(days=days)
    data = dict(id=str(index), source="synthetic", source_id=str(index), canonical_id=str(index),
                title=title, abstract=None, url=f"https://example.org/{index}", version=None,
                published_at=stamp, first_public_at=stamp, observed_at=stamp,
                available_at=stamp, status="unknown")
    data.update(updates)
    return Document(**data)


def test_unknown_term_is_candidate_not_alias():
    docs = [doc(i, "Latent Action Model (LAM)") for i in range(3)]
    docs += [doc(i + 10, "Local Attention Memory (LAM)") for i in range(3)]
    aliases = {"vla": ["vision language action", "VLA"]}
    result = discover(docs, aliases, CUTOFF)
    terms = [c for c in result if c.kind == "new_term"]
    assert len(terms) == 2 and len({c.entity_id for c in terms}) == 2
    assert all(c.review_status == "proposed" and len(c.evidence_ids) == 3 for c in terms)
    assert aliases == {"vla": ["vision language action", "VLA"]}
    assert all(any("low_support" in r for r in c.reasons) for c in terms)


def test_combinations_require_increased_cooccurrence():
    aliases = {"a": ["tactile sensing"], "b": ["world model"]}
    docs = [doc(i, "tactile sensing with world model") for i in range(3)]
    assert discover(docs, aliases, CUTOFF)[0].kind == "new_combination"
    old = [doc(i + 10, "tactile sensing with world model", days=30) for i in range(3)]
    assert not discover(docs + old, aliases, CUTOFF)


def test_unassigned_tfidf_cluster_is_proposed_with_evidence():
    docs = [doc(i, "Soft tactile grasping contact dynamics") for i in range(3)]
    result = discover(docs, {}, CUTOFF)
    assert len(result) == 1 and result[0].kind == "new_cluster"
    assert result[0].evidence_ids == ["0", "1", "2"]
    assert any("TF-IDF" in reason for reason in result[0].reasons)
    assert any("https://example.org/0" in reason for reason in result[0].reasons)


def test_future_feature_ignored_and_input_order_stable():
    docs = [doc(i, "Latent Action Model (LAM)") for i in range(3)]
    expected = discover(docs, {}, CUTOFF)
    assert discover(list(reversed(docs)) + [doc(8, "Other Future Term (OFT)", days=-1)], {}, CUTOFF) == expected
    assert discover(docs + [doc(9, "Latent Action Model (LAM)", canonical_id="0")], {}, CUTOFF) == expected


def test_known_full_name_but_ambiguous_acronym_does_not_merge():
    docs = [doc(i, "Local Attention Memory (LAM)") for i in range(3)]
    result = discover(docs, {"latent": ["latent action model", "LAM"]}, CUTOFF)
    assert any(c.kind == "new_term" for c in result)


def test_sensitivity_retains_small_samples_and_compares_thresholds():
    docs = [doc(i, "Latent Action Model (LAM)") for i in range(4)]
    report = sensitivity_analysis(docs, {}, CUTOFF)
    assert report == {3: {"candidates": 1, "supported": 1, "low_support": 0},
                      5: {"candidates": 1, "supported": 0, "low_support": 1},
                      10: {"candidates": 1, "supported": 0, "low_support": 1}}


def test_unknown_availability_and_old_terms_do_not_become_new():
    assert discover([doc(1, "Latent Action Model (LAM)", available_at=None)], {}, CUTOFF) == []
    docs = [doc(i, "Latent Action Model (LAM)", days=30) for i in range(3)]
    docs += [doc(8, "Latent Action Model (LAM)")]
    assert not any(c.kind == "new_term" for c in discover(docs, {}, CUTOFF))


def test_terms_in_abstract_and_first_observed_time():
    stamp = CUTOFF - timedelta(hours=2)
    result = discover([doc(1, "Learning", abstract="Latent Action Model (LAM)", observed_at=stamp)], {}, CUTOFF)
    assert result[0].kind == "new_term"
    assert result[0].first_seen_at == stamp
    assert "probability" not in result[0].model_dump()


def test_seed_alias_boundaries_and_cluster_growth():
    docs = [doc(1, "Soft tactile grasping contact dynamics"),
            doc(2, "Soft tactile grasping contact dynamics", days=30)]
    assert discover(docs, {}, CUTOFF) == []
    # The alias 'act' must not match the substring in 'tactile'.
    docs[1] = doc(2, "Soft tactile grasping contact dynamics")
    assert discover(docs, {"act": ["act"]}, CUTOFF)[0].kind == "new_cluster"
