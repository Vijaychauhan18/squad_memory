from __future__ import annotations

import importlib.util
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_NAME = "squad_memory_phase34_test"
MODULE_SPEC = importlib.util.spec_from_file_location(MODULE_NAME, BASE / "squad_memory.py")
SQUAD_MEMORY = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
sys.modules[MODULE_NAME] = SQUAD_MEMORY
MODULE_SPEC.loader.exec_module(SQUAD_MEMORY)


class Phase34WorkspaceContextE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.db_path = self.root / "workspace.db"
        self.workspace_root = self.root / "project"

        (self.skills_root / "seo" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "writer" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "seo" / "SKILL.md").write_text(
            "# SEO Skill\n\nTechnical SEO diagnostics and release investigations.\n",
            encoding="utf-8",
        )
        (self.skills_root / "writer" / "SKILL.md").write_text(
            "# Writer Skill\n\nDraft hooks and structure.\n",
            encoding="utf-8",
        )
        (self.skills_root / "seo" / "memory" / "technical-seo-canon.md").write_text(
            "---\n"
            "topic: technical_seo\n"
            "intent: technical_seo, diagnosis\n"
            "role: pinchy, coral\n"
            "confidence: high\n"
            "canonical: true\n"
            "canonical_group: Technical SEO\n"
            "---\n\n"
            "# Technical SEO Canon\n\n"
            "## Core Concept\n"
            "Audit crawlability, indexation, rendering, canonicals, robots rules, and sitemap health.\n",
            encoding="utf-8",
        )
        (self.skills_root / "writer" / "memory" / "writer-canon.md").write_text(
            "---\n"
            "topic: writing_system\n"
            "intent: content_writing\n"
            "role: plankton\n"
            "confidence: medium\n"
            "---\n\n"
            "# Writer Canon\n\n"
            "## Hook\n"
            "Use strong hooks and clean article structure.\n",
            encoding="utf-8",
        )

        (self.workspace_root / "docs").mkdir(parents=True, exist_ok=True)
        (self.workspace_root / "docs" / "release-checklist.md").write_text(
            "# Release SEO Checklist\n\n"
            "Check crawlability, indexation, rendering regressions, canonicals, and robots.txt after deploy.\n",
            encoding="utf-8",
        )
        (self.workspace_root / "notes.txt").write_text(
            "Need a technical SEO war room for indexation and rendering after the latest release.\n",
            encoding="utf-8",
        )

        SQUAD_MEMORY.build_index(self.skills_root, self.db_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_workspace_sync_rank_and_clear(self) -> None:
        synced = SQUAD_MEMORY.sync_workspace_context(
            self.db_path,
            "Release Context",
            [self.workspace_root],
            role="pinchy",
            pack_id="technical_seo_war_room",
            max_files=10,
        )
        self.assertEqual(synced["status"], "active")
        self.assertGreaterEqual(synced["item_count"], 2)

        report = SQUAD_MEMORY.workspace_report(self.db_path, limit=5)
        self.assertEqual(report["active_contexts"], 1)
        self.assertGreaterEqual(report["active_items"], 2)
        self.assertEqual(report["contexts"][0]["name"], "Release Context")

        snapshot = SQUAD_MEMORY.workspace_context_snapshot(
            self.db_path,
            "Need technical SEO help for crawlability and rendering after release",
            "pinchy",
            top=5,
            pack_id="technical_seo_war_room",
        )
        self.assertEqual(snapshot["active_contexts"], 1)
        self.assertTrue(snapshot["hits"])
        self.assertTrue(any("release-checklist.md" in item["path"] for item in snapshot["hits"]))

        results = SQUAD_MEMORY.rank_chunks(
            self.db_path,
            "Need technical SEO help for crawlability and rendering after release",
            role="pinchy",
            skill_filter=None,
            top=5,
            pack_id="technical_seo_war_room",
        )
        self.assertTrue(results)
        self.assertEqual(results[0]["path"], "seo/memory/technical-seo-canon.md")
        self.assertGreater(results[0]["workspace_boost"], 0.0)

        decision = SQUAD_MEMORY.decide(
            self.db_path,
            "Need technical SEO help for crawlability and rendering after release",
            role="pinchy",
            top=5,
        )
        self.assertIn("workspace_context", decision)
        self.assertEqual(decision["workspace_context"]["active_contexts"], 1)
        self.assertTrue(decision["workspace_context"]["hits"])

        cleared = SQUAD_MEMORY.clear_workspace_context(self.db_path, context_id=synced["context_id"])
        self.assertEqual(cleared["count"], 1)
        post_clear = SQUAD_MEMORY.workspace_report(self.db_path, limit=5)
        self.assertEqual(post_clear["active_contexts"], 0)

        with sqlite3.connect(self.db_path) as con:
            events = [row[0] for row in con.execute("SELECT event_type FROM events ORDER BY id").fetchall()]
        self.assertIn("workspace.synced", events)
        self.assertIn("workspace.cleared", events)


if __name__ == "__main__":
    unittest.main()
