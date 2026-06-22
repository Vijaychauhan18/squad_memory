from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase7MergeCanonE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.memory_dir = self.root / "skills" / "seo" / "memory"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.phase7_dir = self.root / "ingest" / "phase7"
        self.phase6_decisions = self.root / "ingest" / "phase6" / "decisions.json"
        self.phase6_decisions.parent.mkdir(parents=True, exist_ok=True)

        (self.memory_dir / "ahrefs-ai-visibility-guide.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: The Complete AI Visibility Guide",
                    "topic: ai_visibility",
                    "confidence: high",
                    "canonical: true",
                    "---",
                    "",
                    "## Core Concept",
                    "AI visibility is a measurable operating discipline for mentions and citations.",
                    "",
                ]
            )
        )
        (self.memory_dir / "ahrefs-how-to-rank-on-chatgpt-what-actually-works-based-on-data.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: How to Rank on ChatGPT: What Actually Works (Based on Data)",
                    "topic: ai_visibility",
                    "confidence: high",
                    "canonical_group: Live approved promotions",
                    "promotion_status: approved",
                    "---",
                    "",
                    "## Core Update",
                    "AI visibility depends on citations, mentions, and query behavior in ChatGPT.",
                    "",
                ]
            )
        )
        (self.memory_dir / "ahrefs-keyword-intent-what-it-is-and-how-to-use-it-in-your-seo-strategy.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Keyword Intent: What It Is and How to Use It in Your SEO Strategy",
                    "topic: keyword_research",
                    "confidence: high",
                    "canonical_group: Live approved promotions",
                    "promotion_status: approved",
                    "---",
                    "",
                    "## Core Update",
                    "Keyword intent should shape SEO planning and page design.",
                    "",
                ]
            )
        )
        (self.memory_dir / "live-seo-feed-ahrefs.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Live SEO Feed - Ahrefs",
                    "topic: live_seo_feeds",
                    "---",
                    "",
                    "# Legacy feed",
                    "",
                ]
            )
        )
        self.phase6_decisions.write_text(
            json.dumps(
                {
                    "items": [
                        {"draft_filename": "a.md", "status": "approve"},
                        {"draft_filename": "b.md", "status": "reject"},
                        {"draft_filename": "c.md", "status": "hold"},
                    ]
                },
                indent=2,
            )
            + "\n"
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase7_builds_registry_and_health_report(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase7_merge_canon.py"),
                "--output-dir",
                str(self.memory_dir),
                "--phase6-decisions",
                str(self.phase6_decisions),
                "--phase7-dir",
                str(self.phase7_dir),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertTrue((self.phase7_dir / "canonical_registry.json").exists())
        self.assertTrue((self.phase7_dir / "memory_health_report.md").exists())
        self.assertEqual(payload["health"]["approved_promotions"], 1)
        self.assertEqual(payload["health"]["rejected_promotions"], 1)
        self.assertEqual(payload["health"]["held_promotions"], 1)

        registry = json.loads((self.phase7_dir / "canonical_registry.json").read_text())
        ai_visibility = next(entry for entry in registry["topics"] if entry["topic"] == "ai_visibility")
        keyword_research = next(entry for entry in registry["topics"] if entry["topic"] == "keyword_research")
        live_feed = registry["notes"]["seo/memory/live-seo-feed-ahrefs.md"]
        promoted = registry["notes"]["seo/memory/ahrefs-how-to-rank-on-chatgpt-what-actually-works-based-on-data.md"]

        self.assertEqual(ai_visibility["topic_status"], "healthy")
        self.assertEqual(ai_visibility["primary_path"], "seo/memory/ahrefs-ai-visibility-guide.md")
        self.assertIn("seo/memory/ahrefs-how-to-rank-on-chatgpt-what-actually-works-based-on-data.md", ai_visibility["merge_candidate_paths"])
        self.assertEqual(keyword_research["topic_status"], "needs_canonical")
        self.assertEqual(keyword_research["primary_path"], "seo/memory/ahrefs-keyword-intent-what-it-is-and-how-to-use-it-in-your-seo-strategy.md")
        self.assertEqual(live_feed["status"], "stale_legacy_feed")
        self.assertEqual(promoted["status"], "merge_candidate")


if __name__ == "__main__":
    unittest.main()
