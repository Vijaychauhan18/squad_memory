from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase8PromoteCanonE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.memory_dir = self.skills_root / "seo" / "memory"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.phase6_decisions = self.root / "ingest" / "phase6" / "decisions.json"
        self.phase7_dir = self.root / "ingest" / "phase7"
        self.phase8_dir = self.root / "ingest" / "phase8"
        self.db_path = self.root / "squad_memory.db"

        self.phase6_decisions.parent.mkdir(parents=True, exist_ok=True)
        self.phase6_decisions.write_text(json.dumps({"items": []}, indent=2) + "\n")

        (self.memory_dir / "ahrefs-keyword-intent.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Keyword Intent",
                    "topic: keyword_research",
                    "confidence: high",
                    "canonical: false",
                    "canonical_group: Live approved promotions",
                    "promotion_status: approved",
                    "---",
                    "",
                    "# Keyword Intent",
                    "",
                    "Useful durable note.",
                    "",
                ]
            )
        )
        (self.memory_dir / "ahrefs-what-ai-means-for-seo.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: What AI Means for SEO",
                    "confidence: high",
                    "---",
                    "",
                    "# What AI Means for SEO",
                    "",
                    "Older durable note missing topic metadata.",
                    "",
                ]
            )
        )
        registry = {
            "notes": {
                "seo/memory/ahrefs-keyword-intent.md": {
                    "topic": "keyword_research",
                    "status": "orphan_primary",
                },
                "seo/memory/ahrefs-what-ai-means-for-seo.md": {
                    "topic": "__untagged__",
                    "status": "orphan_primary",
                },
            },
            "topics": [],
            "health": {},
        }
        self.phase7_dir.mkdir(parents=True, exist_ok=True)
        (self.phase7_dir / "canonical_registry.json").write_text(json.dumps(registry, indent=2) + "\n")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase8_promotes_safe_orphans_and_skips_untagged(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase8_promote_canon.py"),
                "--output-dir",
                str(self.memory_dir),
                "--phase6-decisions",
                str(self.phase6_decisions),
                "--phase7-registry",
                str(self.phase7_dir / "canonical_registry.json"),
                "--phase7-dir",
                str(self.phase7_dir),
                "--phase8-dir",
                str(self.phase8_dir),
                "--skills-root",
                str(self.skills_root),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(len(payload["changed"]), 1)
        self.assertEqual(len(payload["skipped"]), 1)
        self.assertTrue((self.phase8_dir / "canonical_promotion_report.md").exists())

        promoted_text = (self.memory_dir / "ahrefs-keyword-intent.md").read_text()
        self.assertIn("canonical: true", promoted_text)
        self.assertIn("canonical_group: Keyword research", promoted_text)
        self.assertIn("canonicalized_by: phase8_promote_canon", promoted_text)

        untouched_text = (self.memory_dir / "ahrefs-what-ai-means-for-seo.md").read_text()
        self.assertNotIn("canonicalized_by: phase8_promote_canon", untouched_text)

        refreshed_registry = json.loads((self.phase7_dir / "canonical_registry.json").read_text())
        promoted_state = refreshed_registry["notes"]["seo/memory/ahrefs-keyword-intent.md"]
        skipped_state = refreshed_registry["notes"]["seo/memory/ahrefs-what-ai-means-for-seo.md"]
        self.assertEqual(promoted_state["status"], "canonical_primary")
        self.assertEqual(skipped_state["status"], "orphan_primary")


if __name__ == "__main__":
    unittest.main()
