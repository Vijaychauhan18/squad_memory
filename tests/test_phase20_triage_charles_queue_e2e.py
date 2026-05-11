from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase20TriageCharlesQueueE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.phase18_dir = self.root / "ingest" / "phase18"
        self.phase19_dir = self.root / "ingest" / "phase19"
        self.phase20_dir = self.root / "ingest" / "phase20"

        drafts_dir = self.phase18_dir / "drafts"
        drafts_dir.mkdir(parents=True, exist_ok=True)
        (drafts_dir / "buffer-workflow.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - A Better Creator Workflow",
                    "topic: social_distribution",
                    "intent: research, monitoring, creator_examples",
                    "role: charles, current, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - A Better Creator Workflow",
                    "",
                    "## Source Signal",
                    "A platform-native workflow for repurposing one creator idea across channels.",
                    "",
                    "## Draft Summary",
                    "- Workflow for platform-native creator repurposing and hooks.",
                    "",
                ]
            )
            + "\n"
        )
        (drafts_dir / "hootsuite-stats.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - 30+ Instagram statistics marketers need to know in 2026",
                    "topic: social_distribution",
                    "intent: research, monitoring, creator_examples",
                    "role: charles, current, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - 30+ Instagram statistics marketers need to know in 2026",
                    "",
                    "## Source Signal",
                    "A broad list of stats about Instagram usage.",
                    "",
                    "## Draft Summary",
                    "- Statistics round-up without a clear operating workflow.",
                    "",
                ]
            )
            + "\n"
        )

        self.phase19_dir.mkdir(parents=True, exist_ok=True)
        (self.phase19_dir / "latest.json").write_text(
            json.dumps(
                {
                    "phase18_manifest": str(self.phase18_dir / "latest.json"),
                },
                indent=2,
            )
        )
        (self.phase19_dir / "decisions.json").write_text(
            json.dumps(
                {
                    "items": [
                        {
                            "draft_filename": "buffer-workflow.md",
                            "status": "hold",
                            "title": "A Better Creator Workflow",
                            "source_slug": "buffer",
                            "draft_topic": "social_distribution",
                            "score": 0.95,
                        },
                        {
                            "draft_filename": "hootsuite-stats.md",
                            "status": "hold",
                            "title": "30+ Instagram statistics marketers need to know in 2026",
                            "source_slug": "hootsuite",
                            "draft_topic": "social_distribution",
                            "score": 0.74,
                        },
                    ]
                },
                indent=2,
            )
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase20_triages_charles_queue(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase20_triage_charles_queue.py"),
                "--phase19-manifest",
                str(self.phase19_dir / "latest.json"),
                "--decisions-path",
                str(self.phase19_dir / "decisions.json"),
                "--phase20-dir",
                str(self.phase20_dir),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["approve_suggested"], 1)
        self.assertEqual(payload["reject_suggested"], 1)
        self.assertTrue((self.phase20_dir / "triage.json").exists())
        self.assertTrue((self.phase20_dir / "triage-report.md").exists())

        decisions = json.loads((self.phase19_dir / "decisions.json").read_text())
        by_name = {item["draft_filename"]: item for item in decisions["items"]}
        self.assertEqual(by_name["buffer-workflow.md"]["triage_recommendation"], "approve_suggested")
        self.assertEqual(by_name["hootsuite-stats.md"]["triage_recommendation"], "reject_suggested")


if __name__ == "__main__":
    unittest.main()
