from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase27PromoteDevQaApprovedE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase26_dir = self.root / "ingest" / "phase26"
        self.phase27_dir = self.root / "ingest" / "phase27"
        self.db_path = self.root / "squad_memory.db"

        developer_root = self.skills_root / "developer"
        qa_root = self.skills_root / "qa"
        (developer_root / "memory").mkdir(parents=True, exist_ok=True)
        (qa_root / "memory").mkdir(parents=True, exist_ok=True)
        (developer_root / "MEMORY.md").write_text("# Developer Memory Router\n", encoding="utf-8")
        (qa_root / "MEMORY.md").write_text("# QA Memory Router\n", encoding="utf-8")

        drafts_dir = self.phase26_dir / "drafts"
        drafts_dir.mkdir(parents=True, exist_ok=True)
        (drafts_dir / "developer-draft.md").write_text(
            "\n".join(
                [
                    "---",
                    "topic: engineering_patterns",
                    "intent: research, monitoring, engineering_examples",
                    "role: developer, reviewer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - Safer Refactor Sequence",
                    "",
                    "Source article: [Safer Refactor Sequence](https://example.com/safer-refactor)",
                    "Source canon: `developer/memory/live-source-canon-martin-fowler.md`",
                    "Published: 2026-03-19",
                    "Domain: developer",
                    "Source topic: engineering_patterns",
                    "",
                    "## Source Signal",
                    "A practical way to break large refactors into smaller reviewable changes.",
                    "",
                    "## Why This Candidate Is In Queue",
                    "- Strong fit for the developer durable library.",
                    "",
                    "## Draft Summary",
                    "- Safer sequencing for refactors and reviewable change sets.",
                    "",
                    "## Suggested Placement",
                    "- Review against `memory/small-prs-and-safe-refactors.md`.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (drafts_dir / "qa-draft.md").write_text(
            "\n".join(
                [
                    "---",
                    "topic: test_tooling",
                    "intent: research, monitoring, tooling_changes",
                    "role: qa, developer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - Better Release Gate Checks",
                    "",
                    "Source article: [Better Release Gate Checks](https://example.com/release-gate-checks)",
                    "Source canon: `qa/memory/live-source-canon-playwright-releases.md`",
                    "Published: 2026-03-18",
                    "Domain: qa",
                    "Source topic: test_tooling",
                    "",
                    "## Source Signal",
                    "A testing-framework change that affects what should be in the release gate.",
                    "",
                    "## Why This Candidate Is In Queue",
                    "- Strong fit for the QA durable library.",
                    "",
                    "## Draft Summary",
                    "- Release-gate checks updated for recent tooling behavior.",
                    "",
                    "## Suggested Placement",
                    "- Review against `memory/regression-gate-and-release-verdicts.md`.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        self.phase26_dir.mkdir(parents=True, exist_ok=True)
        (self.phase26_dir / "latest.json").write_text(
            json.dumps(
                {
                    "phase26_dir": str(self.phase26_dir),
                    "tracked_candidates": [
                        {
                            "draft_filename": "developer-draft.md",
                            "domain": "developer",
                            "title": "Safer Refactor Sequence",
                            "link": "https://example.com/safer-refactor",
                            "published": "2026-03-19",
                            "source_slug": "martin-fowler",
                            "source_topic": "engineering_patterns",
                            "score": 0.84,
                            "routing": {
                                "suggested_note": "memory/small-prs-and-safe-refactors.md",
                                "suggested_bundle": "Chitin Bundle",
                                "reason": "This fits safe-change discipline.",
                            },
                        },
                        {
                            "draft_filename": "qa-draft.md",
                            "domain": "qa",
                            "title": "Better Release Gate Checks",
                            "link": "https://example.com/release-gate-checks",
                            "published": "2026-03-18",
                            "source_slug": "playwright-releases",
                            "source_topic": "test_tooling",
                            "score": 0.82,
                            "routing": {
                                "suggested_note": "memory/regression-gate-and-release-verdicts.md",
                                "suggested_bundle": "Reef Bundle",
                                "reason": "This belongs with release gating.",
                            },
                        },
                    ],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase27_defaults_to_hold_then_promotes_approved_drafts(self) -> None:
        initial = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase27_promote_dev_qa_approved.py"),
                "--phase26-manifest",
                str(self.phase26_dir / "latest.json"),
                "--phase27-dir",
                str(self.phase27_dir),
                "--decisions-path",
                str(self.phase27_dir / "decisions.json"),
                "--state-path",
                str(self.phase27_dir / "state.json"),
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
        self.assertEqual(initial_payload["queue"]["held"], 2)
        self.assertTrue((self.phase27_dir / "decisions.json").exists())
        self.assertTrue((self.phase27_dir / "review-status.md").exists())

        approved = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase27_promote_dev_qa_approved.py"),
                "--phase26-manifest",
                str(self.phase26_dir / "latest.json"),
                "--phase27-dir",
                str(self.phase27_dir),
                "--decisions-path",
                str(self.phase27_dir / "decisions.json"),
                "--state-path",
                str(self.phase27_dir / "state.json"),
                "--skills-root",
                str(self.skills_root),
                "--db-path",
                str(self.db_path),
                "--approve",
                "developer-draft.md",
                "--approve",
                "qa-draft.md",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        approved_payload = json.loads(approved.stdout)
        self.assertEqual(approved_payload["approved_total"], 2)
        self.assertTrue((self.skills_root / "developer" / "memory" / "developer-draft.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "qa-draft.md").exists())

        developer_router = (self.skills_root / "developer" / "MEMORY.md").read_text(encoding="utf-8")
        qa_router = (self.skills_root / "qa" / "MEMORY.md").read_text(encoding="utf-8")
        self.assertIn("BEGIN AUTO APPROVED DEV QA PROMOTIONS", developer_router)
        self.assertIn("memory/developer-draft.md", developer_router)
        self.assertIn("BEGIN AUTO APPROVED DEV QA PROMOTIONS", qa_router)
        self.assertIn("memory/qa-draft.md", qa_router)


if __name__ == "__main__":
    unittest.main()
