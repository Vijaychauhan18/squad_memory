from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class OpenClawSeoBridgeE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.source_db = self.root / "seo_elite_memory.db"
        self.openclaw_root = self.root / ".openclaw"
        self.workspace = self.openclaw_root / "workspace" / "squad" / "seo"
        self.workspace.mkdir(parents=True, exist_ok=True)
        self._seed_source_db()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _seed_source_db(self) -> None:
        with sqlite3.connect(self.source_db) as con:
            con.executescript(
                """
                CREATE TABLE chunks (
                  chunk_id TEXT PRIMARY KEY,
                  path TEXT NOT NULL,
                  skill TEXT NOT NULL,
                  file_type TEXT NOT NULL,
                  heading TEXT NOT NULL,
                  text TEXT NOT NULL,
                  section_kind TEXT NOT NULL,
                  source TEXT NOT NULL,
                  published_on TEXT NOT NULL,
                  freshness REAL NOT NULL,
                  topics_json TEXT NOT NULL,
                  intents_json TEXT NOT NULL,
                  use_for_json TEXT NOT NULL,
                  avoid_for_json TEXT NOT NULL,
                  confidence TEXT NOT NULL,
                  tags_json TEXT NOT NULL,
                  roles_json TEXT NOT NULL,
                  bundles_json TEXT NOT NULL,
                  is_canonical INTEGER NOT NULL,
                  canonical_group TEXT NOT NULL
                );
                """
            )
            con.executemany(
                """
                INSERT INTO chunks (
                  chunk_id, path, skill, file_type, heading, text, section_kind, source, published_on, freshness,
                  topics_json, intents_json, use_for_json, avoid_for_json, confidence, tags_json,
                  roles_json, bundles_json, is_canonical, canonical_group
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        "chunk-1",
                        "seo-elite/memory/topic-a.md",
                        "seo",
                        "memory",
                        "Intro",
                        "AI visibility starts with entity coverage and citations.",
                        "intro",
                        "ahrefs",
                        "2026-03-20",
                        0.91,
                        '["ai_visibility"]',
                        '["strategy"]',
                        "[]",
                        "[]",
                        "high",
                        '["ahrefs","ai"]',
                        "[]",
                        "[]",
                        1,
                        "ai visibility",
                    ),
                    (
                        "chunk-2",
                        "seo-elite/memory/topic-a.md",
                        "seo",
                        "memory",
                        "Checklist",
                        "Audit answerability, citations, and off-site brand mentions.",
                        "checklist",
                        "ahrefs",
                        "2026-03-20",
                        0.88,
                        '["ai_visibility"]',
                        '["audit"]',
                        "[]",
                        "[]",
                        "high",
                        '["checklist","brand"]',
                        "[]",
                        "[]",
                        1,
                        "ai visibility",
                    ),
                    (
                        "chunk-3",
                        "seo-elite/memory/topic-b.md",
                        "seo",
                        "memory",
                        "Robots",
                        "Check robots, sitemap drift, and crawl discovery gaps.",
                        "section",
                        "",
                        "2026-03-19",
                        0.82,
                        '["technical_seo"]',
                        '["diagnostics"]',
                        "[]",
                        "[]",
                        "medium",
                        '["technical","crawl"]',
                        "[]",
                        "[]",
                        1,
                        "indexation",
                    ),
                ],
            )

    def test_bridge_imports_chunks_and_writes_map(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_seo_bridge.py"),
                "--source-db",
                str(self.source_db),
                "--openclaw-root",
                str(self.openclaw_root),
                "--workspace",
                str(self.workspace),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["imported_chunks"], 3)
        self.assertEqual(payload["imported_paths"], 2)

        target_db = self.openclaw_root / "memory" / "seo.sqlite"
        with sqlite3.connect(target_db) as con:
            chunk_count = con.execute("select count(*) from chunks where source = 'seo_elite_db'").fetchone()[0]
            file_count = con.execute("select count(*) from files where source = 'seo_elite_db'").fetchone()[0]
            sample = con.execute("select path, text from chunks where source = 'seo_elite_db' order by path limit 1").fetchone()

        self.assertEqual(chunk_count, 3)
        self.assertEqual(file_count, 2)
        self.assertEqual(sample[0], "seo-elite/memory/topic-a.md")
        self.assertIn("Canonical Group: ai visibility", sample[1])
        self.assertIn("Topics: ai_visibility", sample[1])

        summary_json = self.workspace / "automation" / "knowledge-bridge" / "seo-elite-map.json"
        summary_md = self.workspace / "automation" / "knowledge-bridge" / "seo-elite-map.md"
        manifest_json = self.workspace / "automation" / "knowledge-bridge" / "seo-elite-path-manifest.json"
        self.assertTrue(summary_json.exists())
        self.assertTrue(summary_md.exists())
        self.assertTrue(manifest_json.exists())

        summary = json.loads(summary_json.read_text(encoding="utf-8"))
        manifest = json.loads(manifest_json.read_text(encoding="utf-8"))
        self.assertEqual(summary["top_canonical_groups"][0]["name"], "ai visibility")
        self.assertEqual(summary["top_topics"][0]["name"], "ai_visibility")
        self.assertEqual(len(manifest["paths"]), 2)
        self.assertIn("imported chunks", summary_md.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
