from __future__ import annotations

import importlib.util
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_NAME = "squad_memory_phase32_test"
MODULE_SPEC = importlib.util.spec_from_file_location(MODULE_NAME, BASE / "squad_memory.py")
SQUAD_MEMORY = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
sys.modules[MODULE_NAME] = SQUAD_MEMORY
MODULE_SPEC.loader.exec_module(SQUAD_MEMORY)


class Phase32EventBusE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.db_path = self.root / "events.db"

        with sqlite3.connect(self.db_path) as con:
            SQUAD_MEMORY.ensure_schema(con)
            SQUAD_MEMORY.ensure_learning_tables(con)
            con.commit()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def fetch_events(self) -> list[tuple[str, str, str]]:
        with sqlite3.connect(self.db_path) as con:
            rows = con.execute(
                "SELECT event_type, event_group, status FROM events ORDER BY id"
            ).fetchall()
        return [(str(row[0]), str(row[1]), str(row[2])) for row in rows]

    def test_query_feedback_and_scorecard_emit_events(self) -> None:
        SQUAD_MEMORY.log_query(
            self.db_path,
            "decide",
            "Need a clean routing decision",
            "pinchy",
            None,
            5,
            {
                "recommended_skills": [{"skill": "orchestrator-pinchy"}],
                "inferred_intents": ["coordination"],
                "expansion_terms": ["handoff", "routing"],
            },
        )
        SQUAD_MEMORY.add_feedback(
            self.db_path,
            "Need a clean routing decision",
            "orchestrator-pinchy/AGENTS.md",
            "useful",
        )

        with sqlite3.connect(self.db_path) as con:
            con.execute(
                """
                INSERT INTO task_outcomes(
                  id, ts, query, role, pack_id, primary_skill, supporting_skills_json, used_skills_json,
                  memory_paths_json, status, revision_count, completion_minutes, user_rating, notes
                )
                VALUES(
                  1, '2026-03-22 10:00:00', 'Need a clean routing decision', 'pinchy', 'launch_coordination',
                  'orchestrator-pinchy', '["operations"]', '["orchestrator-pinchy", "operations"]',
                  '["orchestrator-pinchy/AGENTS.md"]', 'accepted', 0, 12.0, 5.0, 'Strong handoff'
                )
                """
            )
            con.commit()

        result = SQUAD_MEMORY.score_task_result(
            self.db_path,
            1,
            scorer="qa",
            scoring_mode="manual",
            notes="Manual quality review",
            goal_fit_score=4.7,
            correctness_score=4.6,
            clarity_score=4.5,
            completeness_score=4.4,
            actionability_score=4.6,
            format_score=4.5,
        )

        self.assertEqual(result["outcome_id"], 1)
        events = self.fetch_events()
        self.assertEqual(
            events,
            [
                ("query.decide", "query", "ok"),
                ("feedback.recorded", "feedback", "useful"),
                ("task.scored", "scorecard", "excellent"),
            ],
        )

        with sqlite3.connect(self.db_path) as con:
            row = con.execute(
                "SELECT metadata_json FROM events WHERE event_type = 'task.scored'"
            ).fetchone()
        self.assertIsNotNone(row)
        metadata = json.loads(str(row[0]))
        self.assertEqual(metadata["scoring_mode"], "manual")
        self.assertEqual(metadata["scorer"], "qa")


if __name__ == "__main__":
    unittest.main()
