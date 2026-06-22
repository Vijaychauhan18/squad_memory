from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase30ScorecardLearningE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.db_path = self.root / "squad_memory.db"
        self.phase29_dir = self.root / "ingest" / "phase29"
        self.phase30_dir = self.root / "ingest" / "phase30"
        self.packs_path = self.root / "task_packs.json"

        writer_root = self.skills_root / "writer" / "memory"
        marketing_root = self.skills_root / "marketing" / "memory"
        writer_root.mkdir(parents=True, exist_ok=True)
        marketing_root.mkdir(parents=True, exist_ok=True)

        (self.skills_root / "writer" / "SKILL.md").write_text("# Writer\n")
        (self.skills_root / "marketing" / "SKILL.md").write_text("# Marketing\n")
        (self.skills_root / "writer" / "MEMORY.md").write_text("# Writer Memory Router\n")
        (self.skills_root / "marketing" / "MEMORY.md").write_text("# Marketing Memory Router\n")
        (writer_root / "brief-to-draft.md").write_text(
            "---\n"
            "title: Brief to Draft Workflow\n"
            "topic: brief_to_draft\n"
            "intent: content_writing\n"
            "role: writer, pinchy\n"
            "use_for: draft_from_brief\n"
            "confidence: high\n"
            "canonical: true\n"
            "---\n\n"
            "## Core Concept\nTurn briefs into drafts.\n"
        )
        (marketing_root / "distribution-system.md").write_text(
            "---\n"
            "title: Distribution System\n"
            "topic: distribution_system\n"
            "intent: distribution\n"
            "role: marketing, current, pinchy\n"
            "use_for: rollout\n"
            "confidence: high\n"
            "canonical: true\n"
            "---\n\n"
            "## Core Concept\nPromotion is part of the work.\n"
        )

        self.packs_path.write_text(
            json.dumps(
                {
                    "packs": [
                        {
                            "id": "article_draft",
                            "name": "Article Draft",
                            "description": "Draft an article from a brief.",
                            "roles": ["plankton", "pinchy"],
                            "intents": ["content_writing"],
                            "keywords": ["blog post", "article draft", "draft", "brief"],
                            "primary_skill": "writer",
                            "supporting_skills": ["marketing"],
                            "memory_focus": ["brief_to_draft", "distribution_system"],
                            "checklist": ["Outline", "Draft", "Revise"],
                            "deliverables": ["Draft"],
                            "output_sections": ["Hook", "Draft"],
                            "handoffs": ["Writer drafts", "Marketing promotes"],
                            "escalation_rules": ["Escalate if the brief is missing."],
                        }
                    ]
                },
                indent=2,
            )
            + "\n"
        )

        subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "build",
                "--root",
                str(self.skills_root),
                "--db",
                str(self.db_path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase30_trains_scorecard_priors_and_writes_report(self) -> None:
        first = subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "complete-task",
                "Need a blog post draft from a brief with stronger structure",
                "--db",
                str(self.db_path),
                "--packs-file",
                str(self.packs_path),
                "--status",
                "accepted",
                "--user-rating",
                "5",
                "--completion-minutes",
                "20",
                "--used-path",
                "writer/memory/brief-to-draft.md",
                "--used-skill",
                "writer",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "complete-task",
                "Need another article draft with cleaner promotion handoff",
                "--db",
                str(self.db_path),
                "--packs-file",
                str(self.packs_path),
                "--status",
                "revised",
                "--revision-count",
                "2",
                "--user-rating",
                "4",
                "--completion-minutes",
                "35",
                "--used-path",
                "writer/memory/brief-to-draft.md",
                "--used-path",
                "marketing/memory/distribution-system.md",
                "--used-skill",
                "writer",
                "--used-skill",
                "marketing",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        first_payload = json.loads(first.stdout)
        json.loads(second.stdout)

        subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "score-task",
                str(first_payload["outcome_id"]),
                "--db",
                str(self.db_path),
                "--mode",
                "manual",
                "--goal-fit",
                "4.8",
                "--correctness",
                "4.7",
                "--clarity",
                "4.6",
                "--completeness",
                "4.5",
                "--actionability",
                "4.4",
                "--format",
                "4.3",
                "--notes",
                "Manual review: strong result.",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        subprocess.run(
            [
                sys.executable,
                str(BASE / "phase29_task_result_eval.py"),
                "--phase29-dir",
                str(self.phase29_dir),
                "--db-path",
                str(self.db_path),
                "--packs-file",
                str(self.packs_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase30_scorecard_learning.py"),
                "--phase30-dir",
                str(self.phase30_dir),
                "--db-path",
                str(self.db_path),
                "--packs-file",
                str(self.packs_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertEqual(payload["task_result_summary"]["scored_outcomes"], 2)
        self.assertEqual(payload["task_result_summary"]["manual_scorecards"], 1)
        self.assertEqual(payload["task_result_summary"]["suggested_scorecards"], 1)
        self.assertGreaterEqual(payload["train_summary"]["result_pack_priors"], 1)
        self.assertGreaterEqual(payload["train_summary"]["result_path_priors"], 1)
        self.assertGreaterEqual(payload["train_summary"]["result_skill_priors"], 1)
        self.assertTrue((self.phase30_dir / "scorecard_learning_ledger.json").exists())
        self.assertTrue((self.phase30_dir / "scorecard_learning_report.md").exists())
        self.assertTrue((self.phase30_dir / "latest.json").exists())

        ledger = json.loads((self.phase30_dir / "scorecard_learning_ledger.json").read_text())
        self.assertIn("train_summary", ledger)
        self.assertIn("task_result_report", ledger)
        self.assertEqual(ledger["task_result_report"]["manual_scorecards"], 1)

        report_text = (self.phase30_dir / "scorecard_learning_report.md").read_text()
        self.assertIn("Phase 30 Scorecard Learning", report_text)
        self.assertIn("Top Learned Pack Priors", report_text)
        self.assertIn("Article Draft", report_text)


if __name__ == "__main__":
    unittest.main()
