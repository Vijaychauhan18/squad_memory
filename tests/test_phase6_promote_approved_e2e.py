from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
FIXTURES = BASE / "tests" / "fixtures" / "feeds"


class Phase6PromoteApprovedE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.memory_dir = self.skills_root / "seo" / "memory"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        (self.skills_root / "seo" / "SKILL.md").write_text("# SEO\n")
        (self.skills_root / "seo" / "MEMORY.md").write_text("# Router\n\n## Routing Guide\n- Existing\n")
        (self.memory_dir / "INDEX.md").write_text("# Index\n\n## AI Search & Visibility\n- Existing\n")
        (self.memory_dir / "existing-ai-visibility.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: What AI Visibility Means for SEO Teams",
                    "topic: ai_visibility",
                    "---",
                    "",
                    "# Existing note",
                    "",
                    "Already covers the first Ahrefs fixture title.",
                    "",
                ]
            )
        )

        self.config_path = self.root / "knowledge_sources.json"
        self.summary_path = self.memory_dir / "live-knowledge-monitor.md"
        self.snapshot_dir = self.root / "ingest" / "raw"
        self.runs_dir = self.root / "ingest" / "runs"
        self.state_path = self.root / "ingest" / "state.json"
        self.phase2_dir = self.root / "ingest" / "phase2"
        self.phase3_dir = self.root / "ingest" / "phase3"
        self.phase5_dir = self.root / "ingest" / "phase5"
        self.phase6_dir = self.root / "ingest" / "phase6"
        self.db_path = self.root / "squad_memory.db"
        self.fixtures_path = self.root / "fixtures.json"

        self.config_path.write_text(json.dumps(self._fixture_config(), indent=2))
        self.fixtures_path.write_text(json.dumps(self._fixture_evals(), indent=2))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _fixture_config(self) -> dict:
        return {
            "name": "Fixture Knowledge Source Monitor",
            "sources": [
                {
                    "slug": "ahrefs",
                    "name": "Ahrefs Blog",
                    "homepage": "https://ahrefs.com/blog/",
                    "kind": "publication",
                    "strength": "data studies and AI visibility",
                    "topic": "seo_research",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring", "ai_visibility"],
                    "tags": ["ahrefs", "fixture"],
                    "feed_urls": [(FIXTURES / "ahrefs.xml").as_uri()],
                },
                {
                    "slug": "dejan",
                    "name": "DEJAN / Dan Petrovic",
                    "homepage": "https://dejan.ai/blog/",
                    "kind": "practitioner",
                    "strength": "reverse engineering",
                    "topic": "ai_reverse_engineering",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring", "ai_selection"],
                    "tags": ["dejan", "fixture"],
                    "feed_urls": [(FIXTURES / "dejan.xml").as_uri()],
                },
            ],
        }

    def _fixture_evals(self) -> dict:
        return {
            "cases": [
                {
                    "query": "Need AI visibility monitoring and citation updates from Ahrefs",
                    "expected_primary_skill": "seo",
                    "expected_skills": ["seo"],
                    "expected_paths": ["seo/memory/live-source-canon-ahrefs.md"],
                }
            ]
        }

    def _run(self, script: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(script), *args], check=True, capture_output=True, text=True)

    def _prepare_phase5(self) -> None:
        self._run(
            BASE / "knowledge_ingest.py",
            "run",
            "--config",
            str(self.config_path),
            "--output-dir",
            str(self.memory_dir),
            "--summary-path",
            str(self.summary_path),
            "--snapshot-dir",
            str(self.snapshot_dir),
            "--runs-dir",
            str(self.runs_dir),
            "--state-path",
            str(self.state_path),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--top",
            "2",
        )
        self._run(
            BASE / "phase2_canonicalize.py",
            "--config",
            str(self.config_path),
            "--output-dir",
            str(self.memory_dir),
            "--state-path",
            str(self.state_path),
            "--runs-dir",
            str(self.runs_dir),
            "--phase2-dir",
            str(self.phase2_dir),
        )
        self._run(
            BASE / "phase3_cluster_refresh.py",
            "--output-dir",
            str(self.memory_dir),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--fixtures",
            str(self.fixtures_path),
            "--phase2-manifest",
            str(self.phase2_dir / "latest.json"),
            "--phase3-dir",
            str(self.phase3_dir),
        )
        self._run(
            BASE / "phase5_promote_memory.py",
            "--output-dir",
            str(self.memory_dir),
            "--phase3-manifest",
            str(self.phase3_dir / "latest.json"),
            "--phase5-dir",
            str(self.phase5_dir),
            "--state-path",
            str(self.phase5_dir / "state.json"),
        )

    def test_phase6_requires_approval_before_live_promotion(self) -> None:
        self._prepare_phase5()

        first = self._run(
            BASE / "phase6_promote_approved.py",
            "--output-dir",
            str(self.memory_dir),
            "--phase5-manifest",
            str(self.phase5_dir / "latest.json"),
            "--phase6-dir",
            str(self.phase6_dir),
            "--decisions-path",
            str(self.phase6_dir / "decisions.json"),
            "--state-path",
            str(self.phase6_dir / "state.json"),
            "--memory-router",
            str(self.skills_root / "seo" / "MEMORY.md"),
            "--index-path",
            str(self.memory_dir / "INDEX.md"),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--json",
        )
        payload = json.loads(first.stdout)
        self.assertEqual(payload["promoted_now"], [])
        self.assertTrue((self.phase6_dir / "decisions.json").exists())
        self.assertTrue((self.phase6_dir / "review-status.md").exists())
        self.assertFalse((self.memory_dir / "ahrefs-brand-mentions-and-ai-overviews.md").exists())
        self.assertNotIn("BEGIN AUTO PROMOTED DRAFTS", (self.skills_root / "seo" / "MEMORY.md").read_text())

        decisions = json.loads((self.phase6_dir / "decisions.json").read_text())
        targets = {item["draft_filename"]: item for item in decisions["items"]}
        targets["ahrefs-brand-mentions-and-ai-overviews.md"]["status"] = "approve"
        (self.phase6_dir / "decisions.json").write_text(json.dumps(decisions, indent=2) + "\n")

        second = self._run(
            BASE / "phase6_promote_approved.py",
            "--output-dir",
            str(self.memory_dir),
            "--phase5-manifest",
            str(self.phase5_dir / "latest.json"),
            "--phase6-dir",
            str(self.phase6_dir),
            "--decisions-path",
            str(self.phase6_dir / "decisions.json"),
            "--state-path",
            str(self.phase6_dir / "state.json"),
            "--memory-router",
            str(self.skills_root / "seo" / "MEMORY.md"),
            "--index-path",
            str(self.memory_dir / "INDEX.md"),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--build-db",
            "--json",
        )
        second_payload = json.loads(second.stdout)
        self.assertEqual(len(second_payload["promoted_now"]), 1)
        self.assertTrue((self.memory_dir / "ahrefs-brand-mentions-and-ai-overviews.md").exists())
        self.assertTrue(self.db_path.exists())

        memory_text = (self.skills_root / "seo" / "MEMORY.md").read_text()
        index_text = (self.memory_dir / "INDEX.md").read_text()
        self.assertIn("BEGIN AUTO PROMOTED DRAFTS", memory_text)
        self.assertIn("memory/ahrefs-brand-mentions-and-ai-overviews.md", memory_text)
        self.assertIn("BEGIN AUTO PROMOTED DRAFTS", index_text)
        self.assertIn("ahrefs-brand-mentions-and-ai-overviews.md", index_text)


if __name__ == "__main__":
    unittest.main()
