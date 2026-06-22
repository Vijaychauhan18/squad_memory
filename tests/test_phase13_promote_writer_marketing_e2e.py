from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase13PromoteWriterMarketingE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase12_dir = self.root / "ingest" / "phase12"
        self.phase13_dir = self.root / "ingest" / "phase13"

        writer_root = self.skills_root / "writer" / "memory"
        marketing_root = self.skills_root / "marketing" / "memory"
        writer_root.mkdir(parents=True, exist_ok=True)
        marketing_root.mkdir(parents=True, exist_ok=True)

        (writer_root / "hooks-and-structure.md").write_text(
            "---\ntitle: Hooks and Structure\ntopic: hooks_structure\n---\n\n## Core Concept\nUse strong openings and visible structure.\n"
        )
        (marketing_root / "distribution-system.md").write_text(
            "---\ntitle: Distribution System\ntopic: distribution_system\n---\n\n## Core Concept\nPromotion should be systematic.\n"
        )

        (writer_root / "live-source-copyblogger.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Live Knowledge Snapshot - Copyblogger",
                    "topic: copywriting_systems",
                    "intent: research, monitoring, writing_examples",
                    "role: writer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Live Knowledge Snapshot - Copyblogger",
                    "",
                    "## Latest Items",
                    "- 2026-03-19 | [How to Write a Sharper Lead Without Losing Clarity](https://example.com/sharper-lead)",
                    "  A practical breakdown of openings, readability, and how to keep the reader moving through the piece.",
                    "",
                ]
            )
        )
        (marketing_root / "live-source-buffer.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Live Knowledge Snapshot - Buffer",
                    "topic: social_distribution",
                    "intent: research, monitoring, distribution_examples",
                    "role: marketing, charles, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Live Knowledge Snapshot - Buffer",
                    "",
                    "## Latest Items",
                    "- 2026-03-18 | [A Better Social Distribution System for Multi-Channel Launches](https://example.com/better-distribution-system)",
                    "  A reusable workflow for adapting the same launch asset across channels without posting the same message everywhere.",
                    "",
                ]
            )
        )
        (writer_root / "live-source-canon-copyblogger.md").write_text("# Live Source Canon - Copyblogger\n")
        (marketing_root / "live-source-canon-buffer.md").write_text("# Live Source Canon - Buffer\n")

        self.phase12_dir.mkdir(parents=True, exist_ok=True)
        (self.phase12_dir / "latest.json").write_text(
            json.dumps(
                {
                    "domains": [
                        {"domain": "writer"},
                        {"domain": "marketing"},
                    ]
                },
                indent=2,
            )
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase13_creates_writer_and_marketing_drafts(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase13_promote_writer_marketing.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase12-manifest",
                str(self.phase12_dir / "latest.json"),
                "--phase13-dir",
                str(self.phase13_dir),
                "--state-path",
                str(self.phase13_dir / "state.json"),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        drafted = {item["draft_filename"] for item in payload["new_candidates"]}
        self.assertIn("copyblogger-how-to-write-a-sharper-lead-without-losing-clarity.md", drafted)
        self.assertIn("buffer-a-better-social-distribution-system-for-multi-channel-launches.md", drafted)
        self.assertTrue((self.phase13_dir / "promotion-queue.md").exists())
        self.assertTrue(
            (self.phase13_dir / "drafts" / "copyblogger-how-to-write-a-sharper-lead-without-losing-clarity.md").exists()
        )
        self.assertTrue(
            (self.phase13_dir / "drafts" / "buffer-a-better-social-distribution-system-for-multi-channel-launches.md").exists()
        )

        second = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase13_promote_writer_marketing.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase12-manifest",
                str(self.phase12_dir / "latest.json"),
                "--phase13-dir",
                str(self.phase13_dir),
                "--state-path",
                str(self.phase13_dir / "state.json"),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        second_payload = json.loads(second.stdout)
        self.assertEqual(second_payload["new_candidates"], [])


if __name__ == "__main__":
    unittest.main()
