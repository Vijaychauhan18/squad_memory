from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase19PromoteCharlesApprovedE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase18_dir = self.root / "ingest" / "phase18"
        self.phase19_dir = self.root / "ingest" / "phase19"
        self.db_path = self.root / "squad_memory.db"

        charles_root = self.skills_root / "charles"
        (charles_root / "memory").mkdir(parents=True, exist_ok=True)
        (charles_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Charles Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Charles Operating Canon 2026: `memory/charles-operating-canon-2026.md`",
                    "",
                    "## Charles Bundle",
                    "- `memory/charles-operating-canon-2026.md`",
                    "",
                ]
            )
            + "\n"
        )
        (charles_root / "memory" / "charles-operating-canon-2026.md").write_text("# Charles Operating Canon 2026\n")

        drafts_dir = self.phase18_dir / "drafts"
        drafts_dir.mkdir(parents=True, exist_ok=True)
        (drafts_dir / "buffer-creator-workflow.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - A Better Creator Posting Workflow",
                    "topic: social_distribution",
                    "intent: research, monitoring, creator_examples",
                    "role: charles, current, pinchy",
                    "confidence: high",
                    "use_for: durable_note_review, external_signal_triage",
                    "---",
                    "",
                    "# Promotion Candidate - A Better Creator Posting Workflow",
                    "",
                    "Source article: [A Better Creator Posting Workflow](https://example.com/creator-workflow)",
                    "Source canon: `charles/memory/live-source-canon-buffer.md`",
                    "Published: 2026-03-19",
                    "Domain: charles",
                    "Source topic: social_distribution",
                    "",
                    "## Source Signal",
                    "A reusable workflow for adapting one creator insight across multiple channels without flattening the hook.",
                    "",
                    "## Why This Candidate Is In Queue",
                    "- Strong fresh signal for Charles.",
                    "",
                    "## Draft Summary",
                    "- Cross-channel creator workflow with platform-native adaptation.",
                    "",
                    "## Suggested Placement",
                    "- Review against `memory/platform-native-posting-system.md`.",
                    "- If approved, route it through `Charles Bundle` first.",
                    "- Proposed durable filename: `buffer-creator-workflow.md`",
                ]
            )
            + "\n"
        )

        self.phase18_dir.mkdir(parents=True, exist_ok=True)
        (self.phase18_dir / "latest.json").write_text(
            json.dumps(
                {
                    "phase18_dir": str(self.phase18_dir),
                    "tracked_candidates": [
                        {
                            "domain": "charles",
                            "source_slug": "buffer",
                            "draft_filename": "buffer-creator-workflow.md",
                            "title": "A Better Creator Posting Workflow",
                            "link": "https://example.com/creator-workflow",
                            "published": "2026-03-19",
                            "score": 0.91,
                            "draft_topic": "social_distribution",
                            "routing": {
                                "suggested_note": "memory/platform-native-posting-system.md",
                                "suggested_bundle": "Charles Bundle",
                                "reason": "This is platform-native packaging.",
                            },
                        }
                    ],
                },
                indent=2,
            )
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase19_defaults_to_hold_then_promotes_approved_draft(self) -> None:
        initial = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase19_promote_charles_approved.py"),
                "--phase18-manifest",
                str(self.phase18_dir / "latest.json"),
                "--phase19-dir",
                str(self.phase19_dir),
                "--decisions-path",
                str(self.phase19_dir / "decisions.json"),
                "--state-path",
                str(self.phase19_dir / "state.json"),
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
        initial_payload = json.loads(initial.stdout)
        self.assertEqual(initial_payload["approved_total"], 0)
        self.assertEqual(initial_payload["queue"]["held"], 1)
        self.assertTrue((self.phase19_dir / "decisions.json").exists())
        self.assertTrue((self.phase19_dir / "review-status.md").exists())

        approved = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase19_promote_charles_approved.py"),
                "--phase18-manifest",
                str(self.phase18_dir / "latest.json"),
                "--phase19-dir",
                str(self.phase19_dir),
                "--decisions-path",
                str(self.phase19_dir / "decisions.json"),
                "--state-path",
                str(self.phase19_dir / "state.json"),
                "--skills-root",
                str(self.skills_root),
                "--db-path",
                str(self.db_path),
                "--approve",
                "buffer-creator-workflow.md",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        approved_payload = json.loads(approved.stdout)
        self.assertEqual(approved_payload["approved_total"], 1)
        self.assertTrue((self.skills_root / "charles" / "memory" / "buffer-creator-workflow.md").exists())

        router_text = (self.skills_root / "charles" / "MEMORY.md").read_text()
        self.assertIn("BEGIN AUTO APPROVED CHARLES PROMOTIONS", router_text)
        self.assertIn("buffer-creator-workflow.md", router_text)


if __name__ == "__main__":
    unittest.main()
