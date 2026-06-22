from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase10FuseEvidenceE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.memory_dir = self.skills_root / "seo" / "memory"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.phase7_dir = self.root / "ingest" / "phase7"
        self.phase10_dir = self.root / "ingest" / "phase10"
        self.db_path = self.root / "squad_memory.db"

        (self.memory_dir / "ahrefs-ai-visibility-guide.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: AI Visibility Guide",
                    "topic: ai_visibility",
                    "confidence: high",
                    "canonical: true",
                    "source: https://ahrefs.com/blog/ai-visibility/",
                    "tags: ai visibility, citations, brand mentions",
                    "---",
                    "",
                    "## Core Concept",
                    "Track mentions and citations across AI systems as a separate visibility layer.",
                    "",
                ]
            )
        )
        (self.memory_dir / "ahrefs-answer-engine-optimization.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Answer Engine Optimization",
                    "topic: ai_visibility",
                    "confidence: high",
                    "source: https://ahrefs.com/blog/answer-engine-optimization/",
                    "tags: aeo, ai answers, citations",
                    "---",
                    "",
                    "## Core Concept",
                    "Rewriting pages into answer-first formats improves retrieval and citation likelihood.",
                    "",
                ]
            )
        )
        (self.memory_dir / "gsqi-chatgpt-citations.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: ChatGPT Citations",
                    "topic: ai_visibility",
                    "confidence: high",
                    "source: https://www.gsqi.com/example/",
                    "tags: citations, prompts, ai visibility",
                    "---",
                    "",
                    "## Core Concept",
                    "Real prompt-derived citations are stronger than synthetic monitoring prompts for visibility diagnostics.",
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
                    "supporting_paths": ["seo/memory/gsqi-chatgpt-citations.md"],
                    "merge_candidate_paths": ["seo/memory/ahrefs-answer-engine-optimization.md"],
                    "orphan_paths": [],
                    "monitor_paths": [],
                    "stale_paths": [],
                    "recommended_actions": [],
                }
            ]
        }
        self.phase7_dir.mkdir(parents=True, exist_ok=True)
        (self.phase7_dir / "canonical_registry.json").write_text(json.dumps(registry, indent=2) + "\n")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase10_builds_evidence_ledger_and_fusion_block(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase10_fuse_evidence.py"),
                "--output-dir",
                str(self.memory_dir),
                "--phase7-registry",
                str(self.phase7_dir / "canonical_registry.json"),
                "--phase10-dir",
                str(self.phase10_dir),
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
        self.assertEqual(payload["topics_fused"], 1)
        self.assertEqual(len(payload["fusion_updates"]), 1)
        self.assertTrue((self.phase10_dir / "evidence_ledger.json").exists())
        self.assertTrue((self.phase10_dir / "evidence_fusion_report.md").exists())

        ledger = json.loads((self.phase10_dir / "evidence_ledger.json").read_text())
        ai_visibility = ledger["topics"]["ai_visibility"]
        self.assertEqual(ai_visibility["source_count"], 2)
        self.assertGreater(ai_visibility["confidence_score"], 0.7)
        self.assertIn("citations", " ".join(ai_visibility["consensus"]).lower())

        primary = (self.memory_dir / "ahrefs-ai-visibility-guide.md").read_text()
        self.assertIn("<!-- phase10:begin -->", primary)
        self.assertIn("Evidence confidence:", primary)
        self.assertIn("Ahrefs", primary)
        self.assertIn("GSQi", primary)
        self.assertIn("Squad Action", primary)


if __name__ == "__main__":
    unittest.main()
