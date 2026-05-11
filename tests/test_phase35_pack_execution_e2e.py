from __future__ import annotations

import importlib.util
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_NAME = "squad_memory_phase35_test"
MODULE_SPEC = importlib.util.spec_from_file_location(MODULE_NAME, BASE / "squad_memory.py")
SQUAD_MEMORY = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
sys.modules[MODULE_NAME] = SQUAD_MEMORY
MODULE_SPEC.loader.exec_module(SQUAD_MEMORY)


class Phase35PackExecutionE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.db_path = self.root / "execution.db"
        self.packs_path = self.root / "task_packs.json"

        (self.skills_root / "seo" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "seo" / "SKILL.md").write_text(
            "# SEO Skill\n\n## Scope\nTechnical SEO diagnostics and war-room coordination.\n",
            encoding="utf-8",
        )
        (self.skills_root / "seo" / "memory" / "technical-seo-canon.md").write_text(
            "---\n"
            "topic: technical_seo\n"
            "intent: technical_seo, diagnosis\n"
            "role: coral, pinchy\n"
            "confidence: high\n"
            "canonical: true\n"
            "canonical_group: Technical SEO\n"
            "---\n\n"
            "# Technical SEO Canon\n\n"
            "## Core Concept\n"
            "Use this note for crawlability, indexation, canonicals, and rendering.\n\n"
            "## Squad Action\n"
            "Run a technical SEO war room after releases.\n",
            encoding="utf-8",
        )
        self.packs_path.write_text(
            json.dumps(
                {
                    "packs": [
                        {
                            "id": "technical_seo_war_room",
                            "name": "Technical SEO War Room",
                            "description": "Diagnose crawl, indexation, rendering, and release regressions.",
                            "roles": ["pinchy", "coral"],
                            "intents": ["technical_seo"],
                            "keywords": ["crawlability", "indexation", "rendering"],
                            "primary_skill": "seo",
                            "supporting_skills": ["qa"],
                            "memory_focus": ["technical_seo"],
                            "checklist": ["Audit crawlability", "Verify release regressions"],
                            "deliverables": ["Technical diagnosis"],
                            "output_sections": ["Findings", "Fixes"],
                            "handoffs": ["SEO to QA"],
                            "escalation_rules": ["Escalate if production indexing is broken"],
                        }
                    ]
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        SQUAD_MEMORY.build_index(self.skills_root, self.db_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_pack_run_lifecycle(self) -> None:
        started = SQUAD_MEMORY.start_pack_run(
            self.db_path,
            self.packs_path,
            "Need a technical SEO war room for crawlability and indexation after release",
            "pinchy",
            5,
            pack_id="technical_seo_war_room",
        )
        self.assertEqual(started["status"], "active")
        self.assertEqual(started["current_step_seq"], 1)
        run_id = started["run_id"]

        handed = SQUAD_MEMORY.record_pack_run_handoff(
            self.db_path,
            run_id,
            from_skill="seo",
            to_skill="qa",
            reason="Need regression validation",
        )
        self.assertEqual(handed["status"], "active")

        first_step = SQUAD_MEMORY.update_pack_run_step(
            self.db_path,
            run_id,
            1,
            status="completed",
            notes="Crawl checks done",
        )
        self.assertEqual(first_step["status"], "active")
        active_steps = [item for item in first_step["steps"] if item["status"] == "active"]
        self.assertEqual(active_steps[0]["seq"], 2)

        blocked = SQUAD_MEMORY.record_pack_run_blocker(
            self.db_path,
            run_id,
            step_seq=2,
            title="Need production log sample",
            severity="high",
            owner_skill="qa",
            status="open",
            notes="Waiting on logs",
        )
        self.assertEqual(blocked["status"], "blocked")
        blocker_id = blocked["blockers"][0]["id"]

        unblocked = SQUAD_MEMORY.record_pack_run_blocker(
            self.db_path,
            run_id,
            blocker_id=blocker_id,
            status="resolved",
            notes="Logs received",
        )
        self.assertEqual(unblocked["status"], "active")

        finished = SQUAD_MEMORY.update_pack_run_step(
            self.db_path,
            run_id,
            2,
            status="completed",
            notes="Regression verified",
        )
        self.assertEqual(finished["status"], "completed")

        report = SQUAD_MEMORY.pack_run_report(self.db_path, self.packs_path, limit=5)
        self.assertEqual(report["total_runs"], 1)
        self.assertEqual(report["completed_runs"], 1)
        self.assertEqual(report["open_blockers"], 0)
        self.assertEqual(report["recent_runs"][0]["handoff_count"], 1)

        with sqlite3.connect(self.db_path) as con:
            events = con.execute("SELECT event_type FROM events ORDER BY id").fetchall()
        self.assertGreaterEqual(len(events), 5)
        self.assertEqual(events[-1][0], "pack_run.step_updated")


if __name__ == "__main__":
    unittest.main()
