from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
FIXTURES = BASE / "tests" / "fixtures" / "feeds"


class KnowledgePipelinePhasesE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.memory_dir = self.skills_root / "seo" / "memory"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        (self.skills_root / "seo" / "SKILL.md").write_text("# SEO\n")
        (self.skills_root / "seo" / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# SEO Memory Router",
                    "",
                    "### Canonical Ahrefs Notes",
                    "- Existing canon: `memory/existing.md`",
                    "",
                    "## Routing Guide",
                    "- Existing routing text",
                    "",
                    "## Default Memory Bundles",
                    "- Existing bundle text",
                    "",
                    "## Output Rule",
                    "- Existing output rule",
                    "",
                ]
            )
        )
        (self.memory_dir / "INDEX.md").write_text(
            "\n".join(
                [
                    "# Coral's SEO Knowledge Base — INDEX",
                    "",
                    "## Source Canon & Monitoring",
                    "- Existing source canon",
                    "",
                    "## AI Search & Visibility",
                    "- Existing AI visibility note",
                    "",
                ]
            )
        )
        (self.memory_dir / "existing.md").write_text("# Existing\n")

        self.config_path = self.root / "knowledge_sources.json"
        self.state_path = self.root / "ingest" / "state.json"
        self.runs_dir = self.root / "ingest" / "runs"
        self.phase2_dir = self.root / "ingest" / "phase2"
        self.phase3_dir = self.root / "ingest" / "phase3"
        self.snapshot_dir = self.root / "ingest" / "raw"
        self.summary_path = self.memory_dir / "live-knowledge-monitor.md"
        self.db_path = self.root / "squad_memory.db"
        self.eval_fixtures = self.root / "fixtures.json"

        self.config_path.write_text(json.dumps(self._fixture_config(), indent=2))
        self.eval_fixtures.write_text(json.dumps(self._eval_cases(), indent=2))

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
                    "slug": "hobo",
                    "name": "Hobo Web",
                    "homepage": "https://www.hobo-web.co.uk/",
                    "kind": "publication",
                    "strength": "quality systems",
                    "topic": "quality_systems",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring", "leak_systems"],
                    "tags": ["hobo", "fixture"],
                    "feed_urls": [(FIXTURES / "hobo.xml").as_uri()],
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

    def _eval_cases(self) -> list:
        return {
            "cases": [
                {
                    "query": "Need AI visibility monitoring and citation updates from Ahrefs",
                    "expected_primary_skill": "seo",
                    "expected_skills": ["seo"],
                    "expected_paths": ["seo/memory/live-source-canon-ahrefs.md"],
                },
                {
                    "query": "Need reverse engineering monitoring for grounding snippets and selection rate",
                    "expected_primary_skill": "seo",
                    "expected_skills": ["seo"],
                    "expected_paths": ["seo/memory/live-source-canon-dejan.md"],
                },
            ]
        }

    def _run(self, script: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(script), *args], check=True, capture_output=True, text=True)

    def test_phase2_to_phase4_pipeline(self) -> None:
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

        phase2 = self._run(
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
            "--json",
        )
        phase2_payload = json.loads(phase2.stdout)
        self.assertEqual(len(phase2_payload["results"]), 3)
        self.assertTrue((self.memory_dir / "live-source-canon-ahrefs.md").exists())
        self.assertTrue((self.memory_dir / "live-source-canon.md").exists())

        phase3 = self._run(
            BASE / "phase3_cluster_refresh.py",
            "--output-dir",
            str(self.memory_dir),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--fixtures",
            str(self.eval_fixtures),
            "--phase2-manifest",
            str(self.phase2_dir / "latest.json"),
            "--phase3-dir",
            str(self.phase3_dir),
            "--json",
        )
        phase3_payload = json.loads(phase3.stdout)
        self.assertTrue(phase3_payload["gate"]["approved"])
        self.assertTrue((self.memory_dir / "live-source-cluster-report.md").exists())

        phase4 = self._run(
            BASE / "phase4_router_refresh.py",
            "--memory-router",
            str(self.skills_root / "seo" / "MEMORY.md"),
            "--index-path",
            str(self.memory_dir / "INDEX.md"),
            "--output-dir",
            str(self.memory_dir),
            "--phase3-manifest",
            str(self.phase3_dir / "latest.json"),
            "--json",
        )
        _phase4_payload = json.loads(phase4.stdout)

        memory_router = (self.skills_root / "seo" / "MEMORY.md").read_text()
        index_text = (self.memory_dir / "INDEX.md").read_text()
        self.assertIn("<!-- BEGIN AUTO LIVE SOURCE CANON -->", memory_router)
        self.assertIn("memory/live-source-canon-ahrefs.md", memory_router)
        self.assertIn("memory/live-source-cluster-report.md", memory_router)
        self.assertIn("<!-- BEGIN AUTO LIVE SOURCE PIPELINE -->", index_text)
        self.assertIn("live-source-canon-ahrefs.md", index_text)
        self.assertIn("live-source-cluster-report.md", index_text)


if __name__ == "__main__":
    unittest.main()
