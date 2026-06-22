#!/usr/bin/env python3
"""
Dense Embedding Layer — Phase 3B
Adds nomic-embed-text (via Ollama) dense vectors to squad_memory.db
Runs alongside FTS5 sparse TF-IDF for true hybrid retrieval.

Usage:
  python3 dense_embeddings.py embed --limit 10000   # embed top 10K chunks
  python3 dense_embeddings.py embed --all            # embed all 58K+ chunks
  python3 dense_embeddings.py status                 # coverage stats
  python3 dense_embeddings.py query "your query"     # test dense retrieval
  python3 dense_embeddings.py hybrid "your query"    # test hybrid retrieval
"""

from __future__ import annotations
import sys
import json
import sqlite3
import struct
import urllib.request
import urllib.error
import hashlib
import os
import time
from typing import Optional, List

DB_PATH = os.path.expanduser("~/squad_memory/squad_memory.db")
OLLAMA_URL = "http://localhost:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"
EMBED_DIM = 768  # nomic-embed-text dimension
BATCH_SIZE = 32


# ── Schema Setup ─────────────────────────────────────────────────────────────

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS dense_embeddings (
    chunk_id   TEXT PRIMARY KEY,
    embedding  BLOB NOT NULL,   -- float32 array, EMBED_DIM values
    model      TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_dense_model ON dense_embeddings(model);
"""


def setup_schema(conn):
    conn.executescript(SCHEMA_SQL)
    conn.commit()


# ── Ollama Embedding ──────────────────────────────────────────────────────────

def embed_text(text: str) -> Optional[List[float]]:
    """Call Ollama nomic-embed-text and return float vector."""
    payload = json.dumps({"model": EMBED_MODEL, "prompt": text[:2000]}).encode()
    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            return data.get("embedding")
    except Exception as e:
        print(f"  [embed error] {e}")
        return None


def vec_to_blob(vec: list[float]) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def blob_to_vec(blob: bytes) -> list[float]:
    n = len(blob) // 4
    return list(struct.unpack(f"{n}f", blob))


# ── Cosine Similarity ─────────────────────────────────────────────────────────

def cosine_sim(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(x * x for x in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


# ── Embedding Pipeline ────────────────────────────────────────────────────────

def get_unemdedded_chunks(conn, limit: Optional[int] = None) -> List[tuple]:
    """Get chunks that don't have dense embeddings yet.
    Priority: high confidence + high freshness + canonical first.
    """
    limit_clause = f"LIMIT {limit}" if limit else ""
    rows = conn.execute(f"""
        SELECT c.chunk_id, c.text, c.heading
        FROM chunks c
        LEFT JOIN dense_embeddings d ON c.chunk_id = d.chunk_id
        WHERE d.chunk_id IS NULL
          AND length(c.text) > 50
        ORDER BY c.is_canonical DESC, c.freshness DESC, c.confidence DESC
        {limit_clause}
    """).fetchall()
    return rows


def embed_chunks(limit: Optional[int] = None, verbose: bool = True):
    """Embed chunks and store in dense_embeddings table."""
    conn = sqlite3.connect(DB_PATH, timeout=30)
    setup_schema(conn)

    chunks = get_unemdedded_chunks(conn, limit)
    total = len(chunks)

    if total == 0:
        print("All chunks already embedded.")
        conn.close()
        return

    print(f"Embedding {total} chunks using {EMBED_MODEL}...")
    start = time.time()
    done = 0
    errors = 0

    for i, (chunk_id, text, heading) in enumerate(chunks):
        # Combine heading + text for richer embedding
        input_text = f"{heading}\n\n{text}" if heading else text

        vec = embed_text(input_text)
        if vec is None:
            errors += 1
            continue

        blob = vec_to_blob(vec)
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ")

        conn.execute("""
            INSERT OR REPLACE INTO dense_embeddings (chunk_id, embedding, model, created_at)
            VALUES (?, ?, ?, ?)
        """, (chunk_id, blob, EMBED_MODEL, now))

        done += 1

        # Commit in batches
        if done % BATCH_SIZE == 0:
            conn.commit()
            elapsed = time.time() - start
            rate = done / elapsed
            eta = (total - done) / rate if rate > 0 else 0
            if verbose:
                print(f"  [{done}/{total}] {rate:.1f} chunks/s — ETA {eta/60:.1f}m")

    conn.commit()
    elapsed = time.time() - start
    print(f"\nDone. Embedded {done} chunks in {elapsed:.1f}s. Errors: {errors}")
    conn.close()


# ── Retrieval ─────────────────────────────────────────────────────────────────

def dense_query(query: str, top_k: int = 10) -> list[dict]:
    """Pure dense retrieval — cosine similarity against all embeddings."""
    query_vec = embed_text(query)
    if query_vec is None:
        print("Failed to embed query.")
        return []

    conn = sqlite3.connect(DB_PATH, timeout=30)
    rows = conn.execute("""
        SELECT d.chunk_id, d.embedding, c.text, c.heading, c.skill, c.source, c.freshness
        FROM dense_embeddings d
        JOIN chunks c ON d.chunk_id = c.chunk_id
        WHERE d.model = ?
    """, (EMBED_MODEL,)).fetchall()
    conn.close()

    scored = []
    for chunk_id, blob, text, heading, skill, source, freshness in rows:
        vec = blob_to_vec(blob)
        sim = cosine_sim(query_vec, vec)
        scored.append({
            "chunk_id": chunk_id,
            "score": sim,
            "heading": heading,
            "text": text[:200],
            "skill": skill,
            "source": source,
            "freshness": freshness
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]


def hybrid_query(query: str, top_k: int = 10, dense_weight: float = 0.4) -> list[dict]:
    """
    Hybrid retrieval: FTS5 sparse (TF-IDF) + dense cosine similarity.
    dense_weight: 0.0 = pure sparse, 1.0 = pure dense, 0.4 = recommended default
    sparse_weight = 1 - dense_weight
    """
    sparse_weight = 1.0 - dense_weight

    conn = sqlite3.connect(DB_PATH, timeout=30)

    # Stage 1: FTS5 sparse retrieval (top 50 candidates)
    try:
        fts_rows = conn.execute("""
            SELECT c.chunk_id, bm25(chunks_fts) as fts_score, c.text, c.heading, c.skill, c.source, c.freshness
            FROM chunks_fts
            JOIN chunks c ON chunks_fts.rowid = c.rowid
            WHERE chunks_fts MATCH ?
            ORDER BY fts_score
            LIMIT 50
        """, (query,)).fetchall()
    except Exception:
        # Fallback to LIKE if FTS fails
        fts_rows = conn.execute("""
            SELECT chunk_id, -1.0, text, heading, skill, source, freshness
            FROM chunks
            WHERE text LIKE ?
            LIMIT 50
        """, (f"%{query[:50]}%",)).fetchall()

    # Normalize FTS scores (lower bm25 = better, convert to 0-1)
    fts_scores = {}
    if fts_rows:
        raw_scores = [abs(r[1]) for r in fts_rows]
        max_score = max(raw_scores) if raw_scores else 1
        for row in fts_rows:
            normalized = abs(row[1]) / max_score if max_score > 0 else 0
            fts_scores[row[0]] = {
                "sparse_score": normalized,
                "text": row[2],
                "heading": row[3],
                "skill": row[4],
                "source": row[5],
                "freshness": row[6]
            }

    # Stage 2: Dense retrieval on candidate set
    query_vec = embed_text(query)
    dense_scores = {}

    if query_vec and fts_scores:
        candidate_ids = list(fts_scores.keys())
        placeholders = ",".join("?" * len(candidate_ids))
        dense_rows = conn.execute(f"""
            SELECT chunk_id, embedding
            FROM dense_embeddings
            WHERE chunk_id IN ({placeholders}) AND model = ?
        """, candidate_ids + [EMBED_MODEL]).fetchall()

        for chunk_id, blob in dense_rows:
            vec = blob_to_vec(blob)
            dense_scores[chunk_id] = cosine_sim(query_vec, vec)

    conn.close()

    # Hybrid scoring
    results = []
    for chunk_id, sparse_data in fts_scores.items():
        sparse = sparse_data["sparse_score"]
        dense = dense_scores.get(chunk_id, 0.0)
        hybrid = (sparse_weight * sparse) + (dense_weight * dense)

        results.append({
            "chunk_id": chunk_id,
            "hybrid_score": hybrid,
            "sparse_score": sparse,
            "dense_score": dense,
            "heading": sparse_data["heading"],
            "text": sparse_data["text"][:200],
            "skill": sparse_data["skill"],
            "source": sparse_data["source"],
            "freshness": sparse_data["freshness"]
        })

    results.sort(key=lambda x: x["hybrid_score"], reverse=True)
    return results[:top_k]


# ── Status ────────────────────────────────────────────────────────────────────

def status():
    conn = sqlite3.connect(DB_PATH, timeout=30)
    setup_schema(conn)

    total_chunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    embedded = conn.execute(
        "SELECT COUNT(*) FROM dense_embeddings WHERE model = ?", (EMBED_MODEL,)
    ).fetchone()[0]
    coverage = (embedded / total_chunks * 100) if total_chunks > 0 else 0

    print(f"Dense Embedding Status")
    print(f"  Model:     {EMBED_MODEL}")
    print(f"  Total chunks:  {total_chunks:,}")
    print(f"  Embedded:      {embedded:,}")
    print(f"  Coverage:      {coverage:.1f}%")
    print(f"  Remaining:     {total_chunks - embedded:,}")

    conn.close()


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "status":
        status()

    elif cmd == "embed":
        limit = None
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            limit = int(sys.argv[idx + 1])
        elif "--all" not in sys.argv:
            limit = 10000  # default: top 10K
        embed_chunks(limit=limit)

    elif cmd == "query":
        query = " ".join(sys.argv[2:])
        print(f"\nDense query: '{query}'\n")
        results = dense_query(query, top_k=5)
        for i, r in enumerate(results, 1):
            print(f"{i}. [{r['score']:.3f}] {r['heading']} ({r['skill']})")
            print(f"   {r['text'][:120]}...")
            print()

    elif cmd == "hybrid":
        query = " ".join(sys.argv[2:])
        print(f"\nHybrid query: '{query}'\n")
        results = hybrid_query(query, top_k=5)
        for i, r in enumerate(results, 1):
            print(f"{i}. [hybrid:{r['hybrid_score']:.3f} | sparse:{r['sparse_score']:.3f} | dense:{r['dense_score']:.3f}]")
            print(f"   {r['heading']} ({r['skill']})")
            print(f"   {r['text'][:120]}...")
            print()

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
