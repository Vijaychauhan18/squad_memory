from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
FIXTURES = BASE / "tests" / "fixtures" / "feeds"


class Phase5PromoteMemoryE2ETest(unittest.TestCase):
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

    def test_phase5_creates_draft_candidates_and_state(self) -> None:
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

        first = self._run(
            BASE / "phase5_promote_memory.py",
            "--output-dir",
            str(self.memory_dir),
            "--phase3-manifest",
            str(self.phase3_dir / "latest.json"),
            "--phase5-dir",
            str(self.phase5_dir),
            "--state-path",
            str(self.phase5_dir / "state.json"),
            "--json",
        )
        payload = json.loads(first.stdout)
        drafted = {item["draft_filename"] for item in payload["new_candidates"]}

        self.assertNotIn("ahrefs-what-ai-visibility-means-for-seo-teams.md", drafted)
        self.assertIn("ahrefs-brand-mentions-and-ai-overviews.md", drafted)
        self.assertIn("dejan-grounding-snippets-and-selection-rate.md", drafted)
        self.assertTrue((self.phase5_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase5_dir / "drafts" / "ahrefs-brand-mentions-and-ai-overviews.md").exists())

        second = self._run(
            BASE / "phase5_promote_memory.py",
            "--output-dir",
            str(self.memory_dir),
            "--phase3-manifest",
            str(self.phase3_dir / "latest.json"),
            "--phase5-dir",
            str(self.phase5_dir),
            "--state-path",
            str(self.phase5_dir / "state.json"),
            "--json",
        )
        second_payload = json.loads(second.stdout)
        self.assertEqual(second_payload["new_candidates"], [])


if __name__ == "__main__":
    unittest.main()
