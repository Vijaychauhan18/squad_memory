from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase26PromoteDevQaE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase25_dir = self.root / "ingest" / "phase25"
        self.phase26_dir = self.root / "ingest" / "phase26"

        developer_root = self.skills_root / "developer" / "memory"
        qa_root = self.skills_root / "qa" / "memory"
        developer_root.mkdir(parents=True, exist_ok=True)
        qa_root.mkdir(parents=True, exist_ok=True)

        (developer_root / "developer-operating-canon-2026.md").write_text(
            "---\ntitle: Developer Operating Canon 2026\n---\n\n## Core Concept\nBase developer canon.\n",
            encoding="utf-8",
        )
        (developer_root / "small-prs-and-safe-refactors.md").write_text(
            "---\ntitle: Small PRs And Safe Refactors\n---\n\n## Core Concept\nKeep changes reviewable.\n",
            encoding="utf-8",
        )
        (qa_root / "qa-operating-canon-2026.md").write_text(
            "---\ntitle: QA Operating Canon 2026\n---\n\n## Core Concept\nBase QA canon.\n",
            encoding="utf-8",
        )
        (qa_root / "regression-gate-and-release-verdicts.md").write_text(
            "---\ntitle: Regression Gate And Release Verdicts\n---\n\n## Core Concept\nRelease confidence.\n",
            encoding="utf-8",
        )

        (developer_root / "live-source-martin-fowler.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Live Knowledge Snapshot - Martin Fowler",
                    "topic: engineering_patterns",
                    "intent: research, monitoring, engineering_examples",
                    "role: developer, reviewer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Live Knowledge Snapshot - Martin Fowler",
                    "",
                    "## Latest Signals",
                    "- 2026-03-19 | [Refactor Behavior, Not Just Files](https://example.com/refactor-behavior)",
                    "A pragmatic pattern for keeping refactors safe while preserving test confidence.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (qa_root / "live-source-playwright-releases.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Live Knowledge Snapshot - Playwright Releases",
                    "topic: test_tooling",
                    "intent: research, monitoring, tooling_changes",
                    "role: qa, developer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Live Knowledge Snapshot - Playwright Releases",
                    "",
                    "## Latest Signals",
                    "- 2026-03-18 | [Playwright 1.55 release notes](https://example.com/playwright-155)",
                    "A testing-tooling update that changes release-gate and automation assumptions.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        self.phase25_dir.mkdir(parents=True, exist_ok=True)
        (self.phase25_dir / "latest.json").write_text(
            json.dumps(
                {
                    "phase25_dir": str(self.phase25_dir),
                    "domains": [
                        {
                            "domain": "developer",
                            "source_count": 1,
                            "external_canon_path": "developer/memory/developer-external-source-canon-2026.md",
                        },
                        {
                            "domain": "qa",
                            "source_count": 1,
                            "external_canon_path": "qa/memory/qa-external-source-canon-2026.md",
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

    def test_phase26_builds_shared_dev_qa_queue(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase26_promote_dev_qa.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase25-manifest",
                str(self.phase25_dir / "latest.json"),
                "--phase26-dir",
                str(self.phase26_dir),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertEqual(payload["candidate_count"], 2)
        self.assertTrue((self.phase26_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase26_dir / "drafts" / "martin-fowler-refactor-behavior-not-just-files.md").exists())
        self.assertTrue((self.phase26_dir / "drafts" / "playwright-releases-playwright-1-55-release-notes.md").exists())

        queue_text = (self.phase26_dir / "promotion-queue.md").read_text(encoding="utf-8")
        self.assertIn("## Developer", queue_text)
        self.assertIn("## QA", queue_text)
        self.assertIn("small-prs-and-safe-refactors.md", queue_text)
        self.assertIn("regression-gate-and-release-verdicts.md", queue_text)


if __name__ == "__main__":
    unittest.main()
