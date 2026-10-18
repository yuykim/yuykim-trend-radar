"""Bounded HTTP, process-wide arXiv limiter, and durable page checkpoints.

Only public metadata is checkpointed. Credentials and request URLs are never
persisted or included in error codes. RADAR_COLLECTOR_STATE may point to a
persistent .db file (also persist it between CI runs to resume across runners).
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import tempfile
import threading
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from radar.contracts import Document, SourceRun

ROOT = Path(__file__).resolve().parents[3]


def now() -> datetime:
    return datetime.now(timezone.utc)


def utc(value: datetime) -> datetime:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("timestamps must include a timezone")
    return value.astimezone(timezone.utc)


def timestamp(value) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, (float, int)):
        return datetime.fromtimestamp(value / 1000, timezone.utc)
    return utc(datetime.fromisoformat(value.replace("Z", "+00:00")))


class FetchError(Exception):
    """A sanitized, non-secret error code suitable for SourceRun."""

    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


class Limiter:
    def __init__(self, interval=3.0):
        self.interval = interval
        self.lock = threading.Lock()
        self.last = None

    def call(self, operation):
        # Hold the lock through reading the response: one connection at a time.
        with self.lock:
            if self.last is not None:
                time.sleep(max(0, self.interval - (time.monotonic() - self.last)))
            self.last = time.monotonic()
            return operation()


ARXIV_LIMITER = Limiter()
OPENALEX_LIMITER = Limiter(0.11)


def get(url: str, *, headers=None, limiter=None, reserve=None, retries=2) -> bytes:
    """GET with at most three attempts; no response/error bodies are logged."""
    for attempt in range(retries + 1):
        retry_after = 0.0
        try:
            if reserve:
                reserve()  # Reserve cost for EVERY attempt, including failed GETs.
            request = Request(url, headers={"User-Agent": "yuykim-trend-radar/0.1", **(headers or {})})

            def read():
                with urlopen(request, timeout=20) as response:
                    return response.read()

            return limiter.call(read) if limiter else read()
        except HTTPError as exc:
            code = f"http_{exc.code}"
            retryable = exc.code == 429 or 500 <= exc.code < 600
            try:
                retry_after = float(exc.headers.get("Retry-After", "0"))
            except (ValueError, AttributeError):
                pass
            exc.close()
        except (URLError, TimeoutError, OSError):
            code, retryable = "network_error", True
        if not retryable or attempt == retries:
            raise FetchError(code) from None
        if retry_after > 30:
            raise FetchError("retry_after_exceeds_limit") from None
        time.sleep(max(2 ** attempt, retry_after))
    raise AssertionError("unreachable")


class State:
    """Atomic SQLite checkpoint and conservative shared daily OpenAlex budget."""

    def __init__(self, path=None):
        workspace = hashlib.sha256(str(ROOT).encode()).hexdigest()[:12]
        self.path = Path(path or os.environ.get("RADAR_COLLECTOR_STATE") or
                         Path(tempfile.gettempdir()) / f"radar-collectors-{workspace}.db")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS pages (scope TEXT PRIMARY KEY, payload TEXT NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS budget (day TEXT PRIMARY KEY, used INTEGER NOT NULL)")

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=30)
        try:
            with db:
                yield db
        finally:
            db.close()

    def load(self, scope):
        with self.connect() as db:
            row = db.execute("SELECT payload FROM pages WHERE scope=?", (scope,)).fetchone()
        if not row:
            return None, [], False
        data = json.loads(row[0])
        return data["next"], [Document.model_validate(d) for d in data["documents"]], data["done"]

    def save(self, scope, next_page, docs, done=False):
        payload = json.dumps({"next": next_page, "documents": [d.model_dump(mode="json") for d in docs], "done": done})
        with self.connect() as db:
            db.execute("INSERT OR REPLACE INTO pages VALUES (?, ?)", (scope, payload))

    def reserve_openalex(self, daily_limit=950):
        # Units are $0.001: conservatively charge every search/list/retry $0.001.
        # <=950 units leaves headroom below the $1 free daily budget.
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            day = now().date().isoformat()
            db.execute("INSERT OR IGNORE INTO budget VALUES (?, 0)", (day,))
            used = db.execute("SELECT used FROM budget WHERE day=?", (day,)).fetchone()[0]
            if used >= min(950, daily_limit):
                raise FetchError("daily_budget_exhausted")
            db.execute("UPDATE budget SET used=used+1 WHERE day=?", (day,))


def scope_id(source, since, cutoff, settings):
    digest = hashlib.sha256(json.dumps([source, since.isoformat(), cutoff.isoformat(), settings],
                                       sort_keys=True).encode()).hexdigest()[:20]
    return f"{source}:{digest}"


def coverage_id(source, settings):
    """Coverage changes with query settings, never with the collection window."""
    digest = hashlib.sha256(json.dumps(settings, sort_keys=True).encode()).hexdigest()[:20]
    return f"{source}:{digest}"


def run(source, started, coverage, docs, error=None, disabled=False):
    status = "disabled" if disabled else ("partial" if docs else "failed") if error else "ok"
    return SourceRun(source=source, started_at=started, finished_at=now(),
                     status=status,
                     coverage_id=coverage, item_count=len(docs), error_code=error)


def paged(source, since, cutoff, settings, state, coverage, initial, fetch_page):
    """Checkpoint only complete pages; failed pages are retried on next call."""
    from .normalize import canonicalize

    started = now()
    scope = scope_id(source, since, cutoff, settings)
    cursor, docs, done = state.load(scope)
    if done:
        return docs, run(source, started, coverage, docs)
    if cursor is None:
        cursor = initial
    error = None
    try:
        for _ in range(settings.get("max_pages", 100)):
            page, next_cursor = fetch_page(cursor, started)
            # first_public_at is not a version's publication timestamp. Preserve
            # version dates, but never make newly observed metadata historical.
            docs = canonicalize(docs + [d for d in page if d.published_at is None or since <= d.published_at <= cutoff])
            if next_cursor == cursor:
                raise FetchError("pagination_stalled")
            state.save(scope, next_cursor, docs, done=next_cursor is None)
            if next_cursor is None:
                return docs, run(source, started, coverage, docs)
            cursor = next_cursor
        error = "page_limit"
    except FetchError as exc:
        error = exc.code
    except (ValueError, KeyError, TypeError, AttributeError):
        error = "invalid_response"
    return docs, run(source, started, coverage, docs, error)
