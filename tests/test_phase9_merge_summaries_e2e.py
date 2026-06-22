from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase9MergeSummariesE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.memory_dir = self.skills_root / "seo" / "memory"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.phase6_decisions = self.root / "ingest" / "phase6" / "decisions.json"
        self.phase7_dir = self.root / "ingest" / "phase7"
        self.phase8_dir = self.root / "ingest" / "phase8"
        self.phase9_dir = self.root / "ingest" / "phase9"
        self.db_path = self.root / "squad_memory.db"

        self.phase6_decisions.parent.mkdir(parents=True, exist_ok=True)
        self.phase6_decisions.write_text(json.dumps({"items": []}, indent=2) + "\n")

        (self.memory_dir / "ahrefs-ai-visibility-guide.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: AI Visibility Guide",
                    "topic: ai_visibility",
                    "confidence: high",
                    "canonical: true",
                    "source: https://ahrefs.com/blog/ai-visibility/",
                    "tags: ai visibility, citations, ai search",
                    "---",
                    "",
                    "# AI Visibility Guide",
                    "",
                    "## Core Concept",
                    "Canonical baseline for AI visibility work.",
                    "",
                ]
            )
        )
        (self.memory_dir / "ahrefs-what-ai-means-for-seo.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: What AI Means for SEO",
                    "source: https://ahrefs.com/blog/what-ai-means-for-seo/",
                    "tags: ai seo, geo, chatgpt, ai search",
                    "---",
                    "",
                    "## Core Concept",
                    "AI changed search economics but strong SEO still matters.",
                    "",
                ]
            )
        )
        (self.memory_dir / "ahrefs-answer-engine-optimization.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Answer Engine Optimization",
                    "source: https://ahrefs.com/blog/answer-engine-optimization/",
                    "tags: aeo, ai answers, citations",
                    "---",
                    "",
                    "## Core Concept",
                    "Pages should use answer-first formatting so AI systems can retrieve and cite them cleanly.",
                    "",
                ]
            )
        )

        registry = {
            "topics": [
                {
                    "topic": "ai_visibility",
                    "topic_status": "healthy",
                    "primary_path": "seo/memory/ahrefs-ai-visibility-guide.md",
                    "canonical_paths": ["seo/memory/ahrefs-ai-visibility-guide.md"],
                    "supporting_paths": [],
                    "merge_candidate_paths": [],
                    "orphan_paths": [],
                    "monitor_paths": [],
                    "stale_paths": [],
                    "recommended_actions": [],
                },
                {
                    "topic": "__untagged__",
                    "topic_status": "needs_canonical",
                    "primary_path": "seo/memory/ahrefs-what-ai-means-for-seo.md",
                    "canonical_paths": [],
                    "supporting_paths": [],
                    "merge_candidate_paths": ["seo/memory/ahrefs-answer-engine-optimization.md"],
                    "orphan_paths": ["seo/memory/ahrefs-what-ai-means-for-seo.md"],
                    "monitor_paths": [],
                    "stale_paths": [],
                    "recommended_actions": [],
                },
            ],
            "notes": {
                "seo/memory/ahrefs-ai-visibility-guide.md": {
                    "topic": "ai_visibility",
                    "status": "canonical_primary",
                    "merge_target": "",
                },
                "seo/memory/ahrefs-what-ai-means-for-seo.md": {
                    "topic": "__untagged__",
                    "status": "orphan_primary",
                    "merge_target": "",
                },
                "seo/memory/ahrefs-answer-engine-optimization.md": {
                    "topic": "__untagged__",
                    "status": "merge_candidate",
                    "merge_target": "seo/memory/ahrefs-what-ai-means-for-seo.md",
                },
            },
            "health": {
                "healthy_topics": 1,
                "topics_needing_canonical": 1,
            },
        }
        self.phase7_dir.mkdir(parents=True, exist_ok=True)
        (self.phase7_dir / "canonical_registry.json").write_text(json.dumps(registry, indent=2) + "\n")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase9_reassigns_topics_and_refreshes_canonical_digest(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase9_merge_summaries.py"),
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
                "--phase9-dir",
                str(self.phase9_dir),
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

        self.assertTrue((self.phase9_dir / "canonical_summary_merge_report.md").exists())
        self.assertGreaterEqual(len(payload["topic_changes"]), 2)
        self.assertGreaterEqual(len(payload["synthesis_updates"]), 1)

        retagged = (self.memory_dir / "ahrefs-what-ai-means-for-seo.md").read_text()
        self.assertIn("topic: ai_visibility", retagged)
        self.assertIn("topic_assigned_by: phase9_merge_summaries", retagged)

        supporting = (self.memory_dir / "ahrefs-answer-engine-optimization.md").read_text()
        self.assertIn("topic: ai_visibility", supporting)

        canonical = (self.memory_dir / "ahrefs-ai-visibility-guide.md").read_text()
        self.assertIn("<!-- phase9:begin -->", canonical)
        self.assertIn("ahrefs-answer-engine-optimization.md", canonical)
        self.assertIn("ahrefs-what-ai-means-for-seo.md", canonical)

        refreshed_registry = json.loads((self.phase7_dir / "canonical_registry.json").read_text())
        self.assertEqual(refreshed_registry["health"]["topics_needing_canonical"], 0)


if __name__ == "__main__":
    unittest.main()
