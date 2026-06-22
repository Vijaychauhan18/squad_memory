from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

BASE = Path("/Users/vijaychauhan/squad_memory")
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))

from openclaw_fts_backfill import ensure_schema


class QueryOpenClawMemoryCliTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.openclaw_root = self.root / ".openclaw"
        (self.openclaw_root / "memory").mkdir(parents=True, exist_ok=True)
        self.db_path = self.openclaw_root / "memory" / "seo.sqlite"
        self._seed_db()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _seed_db(self) -> None:
        now_ms = 1_742_930_000_000
        with sqlite3.connect(self.db_path) as con:
            ensure_schema(con)
            rows = [
                (
                    "bridge-1",
                    "memory/articles/seroundtable/aio.md",
                    "seo_elite_db",
                    0,
                    0,
                    "hash-1",
                    "seo-elite-db-bridge",
                    "Path: memory/articles/seroundtable/aio.md\nHeading: AI Overviews Win\nCanonical Group: ai visibility\nTopics: ai_visibility, seo_article\nTags: fresh\nPublished On: 2026-03-25\nSource: seroundtable\nFreshness: 9\nConfidence: high\n\nGoogle AI Overviews expanded on breaking news queries.",
                    "[]",
                    now_ms,
                ),
                (
                    "bridge-2",
                    "memory/articles/search-engine-journal/indexing.md",
                    "seo_elite_db",
                    0,
                    0,
                    "hash-2",
                    "seo-elite-db-bridge",
                    "Path: memory/articles/search-engine-journal/indexing.md\nHeading: Indexing Cleanup\nCanonical Group: indexation\nTopics: technical_seo\nTags: ops\nPublished On: 2026-03-24\nSource: search-engine-journal\nFreshness: 7\nConfidence: medium\n\nCheck robots, sitemap drift, and crawl discovery gaps.",
                    "[]",
                    now_ms + 1,
                ),
                (
                    "memory-1",
                    "automation/control/command-center.md",
                    "memory",
                    1,
                    12,
                    "hash-3",
                    "fts-only",
                    "# Command Center\n\nFreshness Radar is active today.",
                    "[]",
                    now_ms + 2,
                ),
            ]
            con.executemany(
                """
                INSERT INTO chunks
                  (id, path, source, start_line, end_line, hash, model, text, embedding, updated_at)
                VALUES
                  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                rows,
            )
            con.executemany(
                """
                INSERT INTO chunks_fts
                  (text, id, path, source, model, start_line, end_line)
                VALUES
                  (?, ?, ?, ?, ?, ?, ?)
                """,
                [(row[7], row[0], row[1], row[2], row[6], row[3], row[4]) for row in rows],
            )
            con.commit()

    def test_query_by_topic_and_source_returns_bridge_hits(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(BASE / "query_openclaw_memory.py"),
                "AI Overviews",
                "--openclaw-root",
                str(self.openclaw_root),
                "--db",
                "seo",
                "--bridge-only",
                "--topic",
                "ai_visibility",
                "--source",
                "seroundtable",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["count"], 1)
        self.assertEqual(payload["results"][0]["path"], "memory/articles/seroundtable/aio.md")
        self.assertEqual(payload["results"][0]["index_source"], "seo_elite_db")
        self.assertEqual(payload["results"][0]["article_source"], "seroundtable")

    def test_filter_only_path_query_returns_memory_rows(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(BASE / "query_openclaw_memory.py"),
                "--openclaw-root",
                str(self.openclaw_root),
                "--db",
                "seo",
                "--path-prefix",
                "automation/",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["count"], 1)
        self.assertEqual(payload["results"][0]["path"], "automation/control/command-center.md")
        self.assertEqual(payload["results"][0]["index_source"], "memory")


if __name__ == "__main__":
    unittest.main()
