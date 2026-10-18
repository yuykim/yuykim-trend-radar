"""Public collection API. Configuration is read without modifying Task 1 files."""
from datetime import datetime

import yaml

from radar.contracts import Document, SourceRun
from . import base
from .normalize import canonicalize

__all__ = ["collect", "canonicalize"]


def collect(source: str, since: datetime, cutoff: datetime) -> tuple[list[Document], SourceRun]:
    """Collect a closed UTC publication window, retaining actual observation time.

    Sources: arxiv (broad), arxiv_seed (seed search), openreview, openalex.
    Unknown publication timestamps remain null and are retained for review.
    Replays of the same window/config resume the saved checkpoint. A past cutoff
    never backdates metadata availability to the historical publication date.
    """
    from .arxiv import collect_arxiv
    from .openalex import collect_openalex
    from .openreview import collect_openreview

    since, cutoff = base.utc(since), base.utc(cutoff)
    if since > cutoff:
        raise ValueError("since must not be later than cutoff")
    if source not in ("arxiv", "arxiv_seed", "openreview", "openalex"):
        raise ValueError("unknown source")
    with (base.ROOT / "config/sources.yml").open(encoding="utf-8") as handle:
        sources = yaml.safe_load(handle)["sources"]
    with (base.ROOT / "config/venue-coverage.yml").open(encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle)
    config_source = "arxiv" if source == "arxiv_seed" else source
    settings = {**manifest.get(config_source, {}), **sources[config_source]}
    # Verified manifest entries describe venues; sources.yml is the enable switch.
    if config_source == "openreview":
        settings["venues"] = manifest.get("openreview", {}).get("venues", [])
    if not settings.get("enabled", False):
        return [], base.run(source, base.now(), None, [], "config_disabled", disabled=True)
    if source == "arxiv_seed":
        with (base.ROOT / "config/topics.yml").open(encoding="utf-8") as handle:
            topics = yaml.safe_load(handle)
        settings["seed_terms"] = [topic["label"] for topic in topics["seed_topics"]]
    state = base.State()
    if config_source == "arxiv":
        return collect_arxiv(since, cutoff, settings, state, seed=source == "arxiv_seed")
    if source == "openreview":
        return collect_openreview(since, cutoff, settings, state)
    return collect_openalex(since, cutoff, settings, state)
