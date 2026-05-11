from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase28TriageDevQaQueueE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.phase26_dir = self.root / "ingest" / "phase26"
        self.phase27_dir = self.root / "ingest" / "phase27"
        self.phase28_dir = self.root / "ingest" / "phase28"

        drafts_dir = self.phase26_dir / "drafts"
        drafts_dir.mkdir(parents=True, exist_ok=True)
        (drafts_dir / "developer-workflow.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - Safer refactor loop with TDD",
                    "topic: engineering_patterns",
                    "intent: research, monitoring, implementation_patterns",
                    "role: developer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - Safer refactor loop with TDD",
                    "",
                    "## Source Signal",
                    "A reusable workflow for refactoring code safely with tests, code review, and incremental changes.",
                    "",
                    "## Draft Summary",
                    "- Safe refactor workflow with TDD, review, and maintainability signals.",
                    "",
                ]
            )
            + "\n"
        )
        (drafts_dir / "qa-release.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - v1.99.1 release note",
                    "topic: test_tooling",
                    "intent: research, monitoring, tooling_changes",
                    "role: qa, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - v1.99.1 release note",
                    "",
                    "## Source Signal",
                    "A patch release fixing browser viewer details without a broader QA workflow change.",
                    "",
                    "## Draft Summary",
                    "- Release note with patch fixes and browser version changes.",
                    "",
                ]
            )
            + "\n"
        )
        (drafts_dir / "developer-fragments.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - Fragments: March notes on code review",
                    "topic: engineering_patterns",
                    "intent: research, monitoring, engineering_examples",
                    "role: developer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - Fragments: March notes on code review",
                    "",
                    "## Source Signal",
                    "A short reflection on code review and engineering workflow tradeoffs.",
                    "",
                    "## Draft Summary",
                    "- Code review thoughts with some workflow value but digest-style framing.",
                    "",
                ]
            )
            + "\n"
        )

        self.phase27_dir.mkdir(parents=True, exist_ok=True)
        (self.phase27_dir / "latest.json").write_text(
            json.dumps(
                {
                    "phase26_manifest": str(self.phase26_dir / "latest.json"),
                },
                indent=2,
            )
        )
        (self.phase27_dir / "decisions.json").write_text(
            json.dumps(
                {
                    "items": [
                        {
                            "draft_filename": "developer-workflow.md",
                            "status": "hold",
                            "domain": "developer",
                            "title": "Safer refactor loop with TDD",
                            "source_slug": "thoughtbot",
                            "draft_topic": "engineering_patterns",
                            "score": 0.86,
                        },
                        {
                            "draft_filename": "qa-release.md",
                            "status": "hold",
                            "domain": "qa",
                            "title": "v1.99.1 release note",
                            "source_slug": "playwright-releases",
                            "draft_topic": "test_tooling",
                            "score": 0.74,
                        },
                        {
                            "draft_filename": "developer-fragments.md",
                            "status": "hold",
                            "domain": "developer",
                            "title": "Fragments: March notes on code review",
                            "source_slug": "martin-fowler",
                            "draft_topic": "engineering_patterns",
                            "score": 0.78,
                        },
                    ]
                },
                indent=2,
            )
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase28_triages_dev_qa_queue(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase28_triage_dev_qa_queue.py"),
                "--phase27-manifest",
                str(self.phase27_dir / "latest.json"),
                "--decisions-path",
                str(self.phase27_dir / "decisions.json"),
                "--phase28-dir",
                str(self.phase28_dir),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["approve_suggested"], 1)
        self.assertEqual(payload["hold"], 1)
        self.assertEqual(payload["reject_suggested"], 1)
        self.assertTrue((self.phase28_dir / "triage.json").exists())
        self.assertTrue((self.phase28_dir / "triage-report.md").exists())

        decisions = json.loads((self.phase27_dir / "decisions.json").read_text())
        by_name = {item["draft_filename"]: item for item in decisions["items"]}
        self.assertEqual(by_name["developer-workflow.md"]["triage_recommendation"], "approve_suggested")
        self.assertEqual(by_name["qa-release.md"]["triage_recommendation"], "reject_suggested")
        self.assertEqual(by_name["developer-fragments.md"]["triage_recommendation"], "hold")


if __name__ == "__main__":
    unittest.main()
