from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import TypeVar

from .contracts import Document, EvidenceEdge, Observation, Review, SourceRun

T = TypeVar("T")


def _stamp(value: datetime | None) -> str | None:
    if value is None:
        return None
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("cutoff and stored timestamps must be timezone-aware")
    return value.astimezone(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _json(model) -> str:
    return model.model_dump_json()


class Repository:
    """SQLite repository. Every mutating operation is an atomic transaction."""

    def __init__(self, db_path: str):
        self.db_path = str(db_path)
        self._uri = self.db_path == ":memory:"
        self._sqlite_path = f"file:radar-{id(self)}?mode=memory&cache=shared" if self._uri else self.db_path
        self._keeper = self._connect() if self._uri else None
        if not self._uri:
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self._migrate()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._sqlite_path, timeout=30, uri=self._uri)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA busy_timeout = 30000")
        return connection

    @contextmanager
    def _connection(self):
        db = self._connect()
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            raise
        finally:
            if not self._uri or db is not self._keeper:
                db.close()

    def _migrate(self) -> None:
        with self._connection() as db:
            if not self._uri:
                db.execute("PRAGMA journal_mode = WAL")
            db.executescript("""
                BEGIN IMMEDIATE;
                CREATE TABLE IF NOT EXISTS schema_migrations (
                    version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS documents (
                    id TEXT PRIMARY KEY, canonical_id TEXT NOT NULL, available_at TEXT,
                    payload TEXT NOT NULL
                );
                CREATE INDEX IF NOT EXISTS documents_canonical_id_idx ON documents(canonical_id);
                CREATE INDEX IF NOT EXISTS documents_available_at_idx ON documents(available_at);
                CREATE TABLE IF NOT EXISTS document_versions (
                    document_id TEXT PRIMARY KEY, canonical_id TEXT NOT NULL,
                    source TEXT NOT NULL, source_id TEXT NOT NULL,
                    published_at TEXT, first_public_at TEXT, available_at TEXT,
                    payload TEXT NOT NULL
                );
                CREATE INDEX IF NOT EXISTS document_versions_canonical_id_idx ON document_versions(canonical_id);
                CREATE INDEX IF NOT EXISTS document_versions_available_at_idx ON document_versions(available_at);
                CREATE TABLE IF NOT EXISTS observations (
                    observation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    entity_id TEXT NOT NULL, metric TEXT NOT NULL, available_at TEXT,
                    payload TEXT NOT NULL
                );
                CREATE INDEX IF NOT EXISTS observations_available_at_idx ON observations(available_at);
                CREATE TABLE IF NOT EXISTS evidence_edges (
                    edge_row_id INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT NOT NULL,
                    available_at TEXT, payload TEXT NOT NULL
                );
                CREATE INDEX IF NOT EXISTS evidence_edges_id_available_idx ON evidence_edges(id, available_at);
                CREATE TABLE IF NOT EXISTS source_runs (
                    run_id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT NOT NULL,
                    started_at TEXT NOT NULL, payload TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS reviews (
                    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    candidate_id TEXT NOT NULL, reviewed_at TEXT NOT NULL, payload TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS entities (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS aliases (entity_id TEXT NOT NULL, alias TEXT NOT NULL, payload TEXT NOT NULL,
                    PRIMARY KEY(entity_id, alias));
                CREATE TABLE IF NOT EXISTS document_entities (document_id TEXT NOT NULL, entity_id TEXT NOT NULL,
                    PRIMARY KEY(document_id, entity_id));
                INSERT OR IGNORE INTO schema_migrations(version, applied_at)
                    VALUES (1, strftime('%Y-%m-%dT%H:%M:%fZ','now'));
                COMMIT;
            """)

    @staticmethod
    def _decode(model_type: type[T], rows) -> list[T]:
        return [model_type.model_validate_json(row["payload"]) for row in rows]

    def upsert_document(self, doc: Document) -> None:
        with self._connection() as db:
            db.execute("""INSERT INTO documents(id, canonical_id, available_at, payload) VALUES (?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET canonical_id=excluded.canonical_id,
                available_at=excluded.available_at, payload=excluded.payload""",
                (doc.id, doc.canonical_id, _stamp(doc.available_at), _json(doc)))
            db.execute("""INSERT INTO document_versions(
                    document_id, canonical_id, source, source_id, published_at,
                    first_public_at, available_at, payload
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(document_id) DO UPDATE SET canonical_id=excluded.canonical_id,
                    source=excluded.source, source_id=excluded.source_id,
                    published_at=excluded.published_at, first_public_at=excluded.first_public_at,
                    available_at=excluded.available_at, payload=excluded.payload""",
                (doc.id, doc.canonical_id, doc.source, doc.source_id,
                 _stamp(doc.published_at), _stamp(doc.first_public_at),
                 _stamp(doc.available_at), _json(doc)))

    def list_documents(self, cutoff: datetime) -> list[Document]:
        with self._connection() as db:
            rows = db.execute("SELECT payload FROM document_versions WHERE available_at IS NOT NULL AND available_at <= ? ORDER BY available_at, document_id", (_stamp(cutoff),)).fetchall()
        return self._decode(Document, rows)

    def save_observations(self, items: list[Observation]) -> None:
        with self._connection() as db:
            db.executemany("INSERT INTO observations(entity_id, metric, available_at, payload) VALUES (?, ?, ?, ?)",
                [(item.entity_id, item.metric, _stamp(item.available_at), _json(item)) for item in items])

    def save_run(self, run: SourceRun) -> None:
        with self._connection() as db:
            db.execute("INSERT INTO source_runs(source, started_at, payload) VALUES (?, ?, ?)",
                (run.source, _stamp(run.started_at), _json(run)))

    def save_review(self, review: Review) -> None:
        with self._connection() as db:
            db.execute("INSERT INTO reviews(candidate_id, reviewed_at, payload) VALUES (?, ?, ?)",
                (review.candidate_id, _stamp(review.reviewed_at), _json(review)))

    def list_reviews(self) -> list[Review]:
        with self._connection() as db:
            rows = db.execute("SELECT payload FROM reviews ORDER BY reviewed_at, review_id").fetchall()
        return self._decode(Review, rows)

    def save_edges(self, edges: list[EvidenceEdge]) -> None:
        with self._connection() as db:
            db.executemany("INSERT INTO evidence_edges(id, available_at, payload) VALUES (?, ?, ?)",
                [(edge.id, _stamp(edge.available_at), _json(edge)) for edge in edges])

    def list_edges(self, cutoff: datetime) -> list[EvidenceEdge]:
        with self._connection() as db:
            rows = db.execute("""SELECT e.payload FROM evidence_edges AS e
                WHERE e.available_at IS NOT NULL AND e.available_at <= ?
                AND e.edge_row_id = (SELECT MAX(prior.edge_row_id) FROM evidence_edges AS prior
                    WHERE prior.id = e.id AND prior.available_at IS NOT NULL AND prior.available_at <= ?)
                ORDER BY e.available_at, e.id""", (_stamp(cutoff), _stamp(cutoff))).fetchall()
        return self._decode(EvidenceEdge, rows)

    def list_observations(self, cutoff: datetime) -> list[Observation]:
        with self._connection() as db:
            rows = db.execute("SELECT payload FROM observations WHERE available_at IS NOT NULL AND available_at <= ? ORDER BY available_at, observation_id", (_stamp(cutoff),)).fetchall()
        return self._decode(Observation, rows)

    def list_runs(self) -> list[SourceRun]:
        with self._connection() as db:
            rows = db.execute("SELECT payload FROM source_runs ORDER BY started_at, run_id").fetchall()
        return self._decode(SourceRun, rows)