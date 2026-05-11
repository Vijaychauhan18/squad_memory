from __future__ import annotations

import importlib.util
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_NAME = "squad_memory_phase33_test"
MODULE_SPEC = importlib.util.spec_from_file_location(MODULE_NAME, BASE / "squad_memory.py")
SQUAD_MEMORY = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
sys.modules[MODULE_NAME] = SQUAD_MEMORY
MODULE_SPEC.loader.exec_module(SQUAD_MEMORY)


class Phase33EpisodicMemoryE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.db_path = self.root / "episodes.db"

        with sqlite3.connect(self.db_path) as con:
            SQUAD_MEMORY.ensure_schema(con)
            SQUAD_MEMORY.ensure_learning_tables(con)
            con.commit()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_events_consolidate_into_episode_sessions(self) -> None:
        query = "Need a technical SEO war room for crawl and indexation issues"
        SQUAD_MEMORY.log_query(
            self.db_path,
            "decide",
            query,
            "pinchy",
            None,
            5,
            {
                "recommended_skills": [{"skill": "seo"}],
                "selected_pack": {"id": "technical_seo_war_room"},
                "inferred_intents": ["technical_seo"],
                "expansion_terms": ["crawlability", "indexation"],
            },
        )
        SQUAD_MEMORY.emit_event(
            self.db_path,
            event_type="task.completed",
            event_group="task",
            status="accepted",
            query=query,
            role="pinchy",
            pack_id="technical_seo_war_room",
            skill="seo",
            metadata={"outcome_id": 7},
        )

        rebuilt = SQUAD_MEMORY.rebuild_episodes(self.db_path)
        self.assertGreaterEqual(rebuilt["episodes"], 1)
        self.assertGreaterEqual(rebuilt["event_rows"], 2)

        report = SQUAD_MEMORY.episode_report(self.db_path, limit=5)
        self.assertEqual(report["episodes"], 1)
        self.assertEqual(report["episode_items"], 2)
        self.assertEqual(report["episode_summaries"], 1)
        self.assertEqual(report["episode_types"][0]["episode_type"], "task_session")
        recent = report["recent_episodes"][0]
        self.assertEqual(recent["primary_skill"], "seo")
        self.assertEqual(recent["pack_id"], "technical_seo_war_room")
        self.assertEqual(recent["event_count"], 2)
        self.assertIn("Need a technical SEO war room", recent["title"])
        self.assertIn("lead seo", recent["summary_text"])


if __name__ == "__main__":
    unittest.main()
