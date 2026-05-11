from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase15OutcomeTelemetryE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.db_path = self.root / "squad_memory.db"
        self.phase15_dir = self.root / "ingest" / "phase15"
        self.packs_path = self.root / "task_packs.json"

        seo_root = self.skills_root / "seo" / "memory"
        writer_root = self.skills_root / "writer" / "memory"
        marketing_root = self.skills_root / "marketing" / "memory"
        seo_root.mkdir(parents=True, exist_ok=True)
        writer_root.mkdir(parents=True, exist_ok=True)
        marketing_root.mkdir(parents=True, exist_ok=True)

        (self.skills_root / "seo" / "SKILL.md").write_text("# SEO\n")
        (self.skills_root / "writer" / "SKILL.md").write_text("# Writer\n")
        (self.skills_root / "marketing" / "SKILL.md").write_text("# Marketing\n")
        (self.skills_root / "seo" / "MEMORY.md").write_text("# SEO Memory Router\n\n## Routing Guide\n- Existing\n")
        (self.skills_root / "writer" / "MEMORY.md").write_text("# Writer Memory Router\n\n## Routing Guide\n- Existing\n")
        (self.skills_root / "marketing" / "MEMORY.md").write_text("# Marketing Memory Router\n\n## Routing Guide\n- Existing\n")
        (seo_root / "INDEX.md").write_text("# SEO INDEX\n")
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
                            "supporting_skills": ["seo", "marketing"],
                            "memory_focus": ["brief_to_draft", "distribution_system"],
                            "checklist": ["Outline", "Draft", "Revise"],
                            "deliverables": ["Draft"],
                            "output_sections": ["Hook", "Draft"],
                            "handoffs": ["Writer drafts", "Marketing promotes"],
                            "escalation_rules": ["Escalate if the brief is missing."],
                        },
                        {
                            "id": "launch_coordination",
                            "name": "Launch Coordination",
                            "description": "Coordinate rollout handoffs.",
                            "roles": ["pinchy", "current"],
                            "intents": ["coordination"],
                            "keywords": ["launch", "coordination", "rollout", "handoff"],
                            "primary_skill": "orchestrator-pinchy",
                            "supporting_skills": ["marketing", "writer"],
                            "memory_focus": ["distribution_system"],
                            "checklist": ["Owners", "Timeline", "Handoffs"],
                            "deliverables": ["Launch plan"],
                            "output_sections": ["Owners", "Timeline"],
                            "handoffs": ["Pinchy coordinates", "Marketing executes"],
                            "escalation_rules": ["Escalate if owners are unclear."],
                        },
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

    def test_phase15_generates_outcome_telemetry(self) -> None:
        subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "complete-task",
                "Need a blog post draft from a brief with promotion hooks",
                "--db",
                str(self.db_path),
                "--packs-file",
                str(self.packs_path),
                "--status",
                "accepted",
                "--user-rating",
                "5",
                "--completion-minutes",
                "22",
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
        subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "complete-task",
                "Need launch coordination and rollout handoffs for this content push",
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
                "marketing/memory/distribution-system.md",
                "--used-skill",
                "orchestrator-pinchy",
                "--used-skill",
                "marketing",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase15_outcome_telemetry.py"),
                "--phase15-dir",
                str(self.phase15_dir),
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

        self.assertEqual(payload["task_outcomes"], 2)
        self.assertTrue((self.phase15_dir / "outcome_telemetry_ledger.json").exists())
        self.assertTrue((self.phase15_dir / "outcome_telemetry_report.md").exists())
        self.assertTrue((self.phase15_dir / "latest.json").exists())

        ledger = json.loads((self.phase15_dir / "outcome_telemetry_ledger.json").read_text())
        self.assertIn("train_summary", ledger)
        self.assertIn("outcome_report", ledger)
        self.assertIn("pack_report", ledger)
        self.assertGreaterEqual(ledger["train_summary"]["outcome_path_priors"], 1)
        self.assertGreaterEqual(ledger["train_summary"]["outcome_skill_priors"], 1)

        top_paths = [item["path"] for item in payload["top_outcome_paths"]]
        self.assertIn("marketing/memory/distribution-system.md", top_paths)
        top_skill_names = [item["skill"] for item in payload["top_outcome_skills"]]
        self.assertIn("marketing", top_skill_names)

        report_text = (self.phase15_dir / "outcome_telemetry_report.md").read_text()
        self.assertIn("Phase 15 Outcome Telemetry", report_text)
        self.assertIn("Strongest Memory Notes", report_text)
        self.assertIn("Underused Winners", report_text)


if __name__ == "__main__":
    unittest.main()
