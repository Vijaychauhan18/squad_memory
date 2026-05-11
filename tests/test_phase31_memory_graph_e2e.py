from __future__ import annotations

import json
import importlib.util
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_SPEC = importlib.util.spec_from_file_location("phase31_memory_graph", BASE / "phase31_memory_graph.py")
PHASE31_MODULE = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
MODULE_SPEC.loader.exec_module(PHASE31_MODULE)


class Phase31MemoryGraphE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.ingest_root = self.root / "ingest"
        self.phase21_dir = self.ingest_root / "phase21"
        self.phase31_dir = self.ingest_root / "phase31"
        self.phase10_dir = self.ingest_root / "phase10"
        self.db_path = self.root / "graph.db"
        self.packs_path = self.root / "task_packs.json"

        self.phase21_dir.mkdir(parents=True, exist_ok=True)
        self.phase10_dir.mkdir(parents=True, exist_ok=True)

        (self.phase21_dir / "control_plane_status.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-20T18:00:00+00:00",
                    "queues": {
                        "seo": {
                            "label": "SEO",
                            "counts": {"approve": 2, "reject": 1, "hold": 1},
                            "items_total": 4,
                            "held_items": [{"draft_filename": "dejan-grounding.md", "title": "Grounding note", "score": 0.9}],
                            "approved_items": [],
                        }
                    },
                    "sources": {
                        "seo": {
                            "label": "SEO",
                            "source_count": 3,
                            "ok_source_count": 3,
                            "error_source_count": 0,
                            "stale_source_count": 1,
                            "stale_sources": [{"slug": "mobilemoxie", "name": "MobileMoxie", "age_days": 300}],
                        }
                    },
                    "memory_health": {"topics_total": 2, "healthy_topics": 2},
                    "learning": {
                        "evaluation": {
                            "primary_skill_accuracy": 1.0,
                            "top3_skill_hit_rate": 1.0,
                            "top5_path_hit_rate": 1.0,
                        },
                        "task_evaluation": {
                            "pack_accuracy": 1.0,
                            "pass_rate": 1.0,
                            "total_cases": 6
                        },
                        "task_results": {"manual_scorecards": 2},
                    },
                    "alerts": ["SEO queue has 1 held item(s)."],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        (self.phase10_dir / "evidence_ledger.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-20T18:00:00+00:00",
                    "topics": {
                        "ai_visibility": {
                            "topic": "ai_visibility",
                            "primary_path": "seo/memory/ahrefs-ai-visibility-guide.md",
                            "distinct_sources": ["Ahrefs", "DEJAN"],
                            "source_count": 2,
                            "evidence_count": 4,
                            "confidence_score": 0.92,
                            "confidence_label": "high",
                            "freshness_label": "current",
                            "consensus": ["AI visibility needs citations and mentions."],
                            "squad_action": "Audit citations and answerability.",
                        }
                    },
                    "primary_paths": {"ai_visibility": "seo/memory/ahrefs-ai-visibility-guide.md"},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        self.packs_path.write_text(
            json.dumps(
                {
                    "packs": [
                        {
                            "id": "ai_visibility_audit",
                            "name": "AI Visibility Audit",
                            "primary_skill": "seo",
                            "supporting_skills": ["dejan-ai-reverse-engineering", "marketing"],
                            "roles": ["pinchy", "coral"],
                            "deliverables": ["Diagnosis"],
                            "intents": ["ai_visibility"],
                            "description": "Diagnose AI answer visibility.",
                            "checklist": ["Baseline", "Diagnosis"],
                        }
                    ]
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        with sqlite3.connect(self.db_path) as con:
            con.execute(
                """
                CREATE TABLE task_outcomes (
                  id INTEGER PRIMARY KEY,
                  ts TEXT,
                  query TEXT,
                  pack_id TEXT,
                  primary_skill TEXT,
                  status TEXT,
                  revision_count INTEGER,
                  user_rating REAL
                )
                """
            )
            con.execute(
                """
                CREATE TABLE task_result_scorecards (
                  outcome_id INTEGER PRIMARY KEY,
                  ts TEXT,
                  scorer TEXT,
                  scoring_mode TEXT,
                  goal_fit_score REAL,
                  correctness_score REAL,
                  clarity_score REAL,
                  completeness_score REAL,
                  actionability_score REAL,
                  format_score REAL,
                  overall_score REAL,
                  verdict TEXT,
                  notes TEXT
                )
                """
            )
            con.execute(
                """
                CREATE TABLE learned_result_skill_priors (
                  bucket TEXT,
                  skill TEXT,
                  score REAL,
                  avg_overall_score REAL,
                  manual_count INTEGER,
                  suggested_count INTEGER,
                  exposure_count INTEGER
                )
                """
            )
            con.execute(
                """
                CREATE TABLE learned_result_pack_priors (
                  bucket TEXT,
                  pack_id TEXT,
                  score REAL,
                  avg_overall_score REAL,
                  manual_count INTEGER,
                  suggested_count INTEGER,
                  exposure_count INTEGER
                )
                """
            )
            con.execute(
                """
                CREATE TABLE events (
                  id INTEGER PRIMARY KEY,
                  ts TEXT,
                  event_type TEXT,
                  event_group TEXT,
                  source TEXT,
                  status TEXT,
                  query TEXT,
                  role TEXT,
                  pack_id TEXT,
                  skill TEXT,
                  path TEXT,
                  metadata_json TEXT
                )
                """
            )
            con.execute(
                """
                CREATE TABLE episodes (
                  id INTEGER PRIMARY KEY,
                  ts_start TEXT,
                  ts_end TEXT,
                  episode_key TEXT,
                  episode_type TEXT,
                  title TEXT,
                  status TEXT,
                  role TEXT,
                  pack_id TEXT,
                  primary_skill TEXT,
                  query TEXT,
                  event_count INTEGER,
                  summary_text TEXT,
                  metadata_json TEXT
                )
                """
            )
            con.execute(
                """
                CREATE TABLE pack_runs (
                  id INTEGER PRIMARY KEY,
                  ts_started TEXT,
                  ts_updated TEXT,
                  ts_completed TEXT,
                  query TEXT,
                  role TEXT,
                  pack_id TEXT,
                  pack_name TEXT,
                  primary_skill TEXT,
                  supporting_skills_json TEXT,
                  status TEXT,
                  current_step_seq INTEGER,
                  step_count INTEGER,
                  blocker_count INTEGER,
                  handoff_count INTEGER,
                  notes TEXT,
                  metadata_json TEXT
                )
                """
            )
            con.execute(
                """
                CREATE TABLE pack_run_blockers (
                  id INTEGER PRIMARY KEY,
                  run_id INTEGER,
                  ts_opened TEXT,
                  ts_resolved TEXT,
                  step_seq INTEGER,
                  title TEXT,
                  severity TEXT,
                  owner_skill TEXT,
                  status TEXT,
                  notes TEXT,
                  metadata_json TEXT
                )
                """
            )
            con.execute(
                """
                CREATE TABLE workspace_contexts (
                  id INTEGER PRIMARY KEY,
                  ts_created TEXT,
                  ts_updated TEXT,
                  ts_last_used TEXT,
                  name TEXT,
                  scope_key TEXT,
                  status TEXT,
                  root_path TEXT,
                  role TEXT,
                  pack_id TEXT,
                  notes TEXT,
                  metadata_json TEXT
                )
                """
            )
            con.execute(
                """
                CREATE TABLE workspace_context_items (
                  id INTEGER PRIMARY KEY,
                  context_id INTEGER,
                  path TEXT,
                  rel_path TEXT,
                  item_type TEXT,
                  title TEXT,
                  text TEXT,
                  token_count INTEGER,
                  metadata_json TEXT
                )
                """
            )
            con.execute(
                """
                CREATE TABLE chunks (
                  chunk_id TEXT PRIMARY KEY,
                  path TEXT,
                  skill TEXT,
                  file_type TEXT,
                  heading TEXT,
                  text TEXT,
                  section_kind TEXT,
                  source TEXT,
                  published_on TEXT,
                  freshness REAL,
                  topics_json TEXT,
                  intents_json TEXT,
                  use_for_json TEXT,
                  avoid_for_json TEXT,
                  confidence TEXT,
                  tags_json TEXT,
                  roles_json TEXT,
                  bundles_json TEXT,
                  is_canonical INTEGER,
                  canonical_group TEXT
                )
                """
            )
            con.execute(
                """
                INSERT INTO task_outcomes(id, ts, query, pack_id, primary_skill, status, revision_count, user_rating)
                VALUES(1, '2026-03-20 18:00:00', 'Need an AI visibility plan', 'ai_visibility_audit', 'seo', 'accepted', 0, 5.0)
                """
            )
            con.execute(
                """
                INSERT INTO task_result_scorecards(
                  outcome_id, ts, scorer, scoring_mode, goal_fit_score, correctness_score, clarity_score,
                  completeness_score, actionability_score, format_score, overall_score, verdict, notes
                )
                VALUES(1, '2026-03-20 18:05:00', 'pinchy', 'manual', 4.7, 4.8, 4.6, 4.5, 4.8, 4.4, 4.63, 'excellent', 'Strong result')
                """
            )
            con.execute(
                """
                INSERT INTO learned_result_skill_priors(bucket, skill, score, avg_overall_score, manual_count, suggested_count, exposure_count)
                VALUES('global', 'seo', 1.22, 4.63, 1, 0, 1)
                """
            )
            con.execute(
                """
                INSERT INTO learned_result_pack_priors(bucket, pack_id, score, avg_overall_score, manual_count, suggested_count, exposure_count)
                VALUES('global', 'ai_visibility_audit', 1.19, 4.63, 1, 0, 1)
                """
            )
            con.execute(
                """
                INSERT INTO events(
                  id, ts, event_type, event_group, source, status, query, role, pack_id, skill, path, metadata_json
                )
                VALUES(
                  1, '2026-03-20 18:06:00', 'task.completed', 'task', 'squad_memory', 'accepted',
                  'Need an AI visibility plan', 'pinchy', 'ai_visibility_audit', 'seo', '', '{"outcome_id": 1}'
                )
                """
            )
            con.execute(
                """
                INSERT INTO episodes(
                  id, ts_start, ts_end, episode_key, episode_type, title, status, role, pack_id,
                  primary_skill, query, event_count, summary_text, metadata_json
                )
                VALUES(
                  1, '2026-03-20 18:00:00', '2026-03-20 18:06:00', 'query:need-an-ai-visibility-plan',
                  'task_session', 'Need an AI visibility plan', 'accepted', 'pinchy', 'ai_visibility_audit',
                  'seo', 'Need an AI visibility plan', 3,
                  'Need an AI visibility plan: 3 events; lead seo; pack ai_visibility_audit; latest accepted',
                  '{"skills": ["seo"], "packs": ["ai_visibility_audit"]}'
                )
                """
            )
            con.execute(
                """
                INSERT INTO pack_runs(
                  id, ts_started, ts_updated, ts_completed, query, role, pack_id, pack_name, primary_skill,
                  supporting_skills_json, status, current_step_seq, step_count, blocker_count, handoff_count, notes, metadata_json
                )
                VALUES(
                  1, '2026-03-20 18:07:00', '2026-03-20 18:09:00', '', 'Need an AI visibility plan', 'pinchy',
                  'ai_visibility_audit', 'AI Visibility Audit', 'seo', '["marketing"]', 'active', 1, 2, 1, 1,
                  'Working through diagnosis', '{"memory_themes": ["AI visibility"]}'
                )
                """
            )
            con.execute(
                """
                INSERT INTO pack_run_blockers(
                  id, run_id, ts_opened, ts_resolved, step_seq, title, severity, owner_skill, status, notes, metadata_json
                )
                VALUES(
                  1, 1, '2026-03-20 18:08:00', '', 1, 'Need branded demand baseline', 'medium', 'seo', 'open',
                  'Waiting on baseline export', '{}'
                )
                """
            )
            con.execute(
                """
                INSERT INTO workspace_contexts(
                  id, ts_created, ts_updated, ts_last_used, name, scope_key, status, root_path, role, pack_id, notes, metadata_json
                )
                VALUES(
                  1, '2026-03-20 18:04:00', '2026-03-20 18:09:00', '2026-03-20 18:09:00',
                  'Release Context', 'scope-1', 'active', '/tmp/project', 'pinchy', 'ai_visibility_audit', '', '{}'
                )
                """
            )
            con.execute(
                """
                INSERT INTO workspace_context_items(
                  id, context_id, path, rel_path, item_type, title, text, token_count, metadata_json
                )
                VALUES(
                  1, 1, '/tmp/project/docs/release.md', 'docs/release.md', 'file', 'Release Notes',
                  'Need AI visibility and citation baseline after launch.', 12, '{}'
                )
                """
            )
            con.execute(
                """
                INSERT INTO chunks(
                  chunk_id, path, skill, file_type, heading, text, section_kind, source, published_on, freshness,
                  topics_json, intents_json, use_for_json, avoid_for_json, confidence, tags_json, roles_json,
                  bundles_json, is_canonical, canonical_group
                )
                VALUES
                  ('chunk-1', 'seo/memory/ahrefs-ai-visibility-guide.md', 'seo', 'memory', 'Intro', 'AI visibility needs citations and mentions.', 'intro', 'Ahrefs', '2026-03-20', 0.94, '["ai_visibility"]', '["strategy"]', '[]', '[]', 'high', '["ahrefs"]', '[]', '[]', 1, 'ai_visibility'),
                  ('chunk-2', 'seo/memory/ahrefs-ai-visibility-guide.md', 'seo', 'memory', 'Checklist', 'Audit citations and answerability.', 'checklist', 'DEJAN', '2026-03-20', 0.88, '["ai_visibility"]', '["audit"]', '[]', '[]', 'high', '["dejan"]', '[]', '[]', 1, 'ai_visibility'),
                  ('chunk-3', 'writer/memory/writer-operating-canon-2026.md', 'writer', 'memory', 'Canon', 'Writing system note.', 'canon', 'Copyhackers', '2026-03-18', 0.76, '["writing_system"]', '["writing"]', '[]', '[]', 'medium', '["copy"]', '[]', '[]', 0, 'writing_system')
                """
            )
            con.commit()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_build_writes_graph_snapshot(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase31_memory_graph.py"),
                "build",
                "--phase31-dir",
                str(self.phase31_dir),
                "--phase21-status",
                str(self.phase21_dir / "control_plane_status.json"),
                "--ingest-root",
                str(self.ingest_root),
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
        self.assertTrue((self.phase31_dir / "memory_graph.json").exists())
        self.assertTrue((self.phase31_dir / "memory_graph_report.md").exists())
        self.assertTrue((self.phase31_dir / "latest.json").exists())
        graph_payload = json.loads((self.phase31_dir / "memory_graph.json").read_text(encoding="utf-8"))
        node_ids = {node["id"] for node in graph_payload["nodes"]}
        self.assertIn("brain", node_ids)
        self.assertIn("memory-bank:global", node_ids)
        self.assertIn("memory-bank:seo", node_ids)
        self.assertIn("domain:seo", node_ids)
        self.assertIn("pack:ai_visibility_audit", node_ids)
        self.assertTrue(graph_payload["meetings"])
        self.assertEqual(graph_payload["meetings"][0]["pack_id"], "ai_visibility_audit")
        self.assertGreaterEqual(len(graph_payload["meetings"][0]["participants"]), 2)
        self.assertIn("topic:seo:ai-visibility", node_ids)
        self.assertIn("outcome:1", node_ids)
        self.assertEqual(graph_payload["meta"]["chunks_total"], 3)
        self.assertEqual(graph_payload["meta"]["memory_paths_total"], 2)
        self.assertEqual(graph_payload["meta"]["recent_events_total"], 1)
        self.assertEqual(graph_payload["meta"]["episodes_total"], 1)
        self.assertEqual(graph_payload["meta"]["runs_total"], 1)
        self.assertEqual(graph_payload["meta"]["open_blockers_total"], 1)
        self.assertEqual(graph_payload["meta"]["workspace_contexts_total"], 1)
        self.assertEqual(graph_payload["meta"]["workspace_items_total"], 1)
        self.assertEqual(graph_payload["meta"]["task_evaluation"]["pack_accuracy"], 1.0)
        self.assertEqual(graph_payload["meta"]["task_evaluation"]["pass_rate"], 1.0)
        self.assertEqual(graph_payload["recent_events"][0]["event_type"], "task.completed")
        self.assertEqual(graph_payload["recent_episodes"][0]["episode_type"], "task_session")
        self.assertIn("episode:1", node_ids)
        self.assertIn("run:1", node_ids)
        self.assertIn("workspace:active", node_ids)
        self.assertIn("workspace-context:1", node_ids)
        self.assertGreater(payload["node_count"], 5)

    def test_graph_pro_payload_includes_chunks_publications_and_filters(self) -> None:
        payload = PHASE31_MODULE.build_graph_pro_payload(
            control_status_path=self.phase21_dir / "control_plane_status.json",
            ingest_root=self.ingest_root,
            db_path=self.db_path,
            packs_file=self.packs_path,
            outcomes_limit=12,
            alerts_limit=8,
            chunk_limit=12,
        )
        node_ids = {node["id"] for node in payload["nodes"]}
        node_kinds = {node["kind"] for node in payload["nodes"]}

        self.assertEqual(payload["graph_mode"], "graph_pro")
        self.assertIn("chunk", node_kinds)
        self.assertIn("publication", node_kinds)
        self.assertIn("timeline", node_kinds)
        self.assertIn("publication:ahrefs", node_ids)
        self.assertGreaterEqual(payload["meta"]["chunk_nodes_total"], 2)
        self.assertGreaterEqual(payload["meta"]["publication_nodes_total"], 1)
        self.assertGreaterEqual(payload["meta"]["timeline_nodes_total"], 1)
        self.assertIn("sources", payload["filters"])
        self.assertIn("detail_modes", payload["filters"])
        self.assertIn("view_modes", payload["filters"])
        self.assertIn("drill_levels", payload["filters"])
        self.assertIn("timeline_buckets", payload["filters"])
        self.assertIn("causal_link_kinds", payload["filters"])
        self.assertIn("all", payload["filters"]["detail_modes"])
        self.assertIn("topology", payload["filters"]["view_modes"])
        self.assertIn("timeline", payload["filters"]["view_modes"])
        self.assertIn("causal", payload["filters"]["view_modes"])
        self.assertIn("topic", payload["filters"]["drill_levels"])
        self.assertIn("7d", payload["filters"]["timeline_buckets"])
        self.assertIn("chunk", payload["filters"]["kinds"])
        self.assertIn("topic_pack", payload["filters"]["causal_link_kinds"])
        self.assertTrue(any(link["kind"] == "topic_pack" for link in payload["links"]))
        self.assertTrue(any(link["kind"] == "timeline_chunk" for link in payload["links"]))


if __name__ == "__main__":
    unittest.main()
