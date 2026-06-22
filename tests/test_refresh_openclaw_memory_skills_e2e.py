from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class RefreshOpenClawMemorySkillsE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.codex_root = self.root / ".codex"
        self.openclaw_root = self.root / ".openclaw"
        self.squad_memory_root = self.root / "squad_memory"
        (self.codex_root / "skills").mkdir(parents=True, exist_ok=True)
        (self.codex_root / "memories").mkdir(parents=True, exist_ok=True)
        self._seed_codex()
        self._seed_squad_memory()
        self._seed_openclaw_workspace()
        self._seed_seo_elite_db()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _seed_codex(self) -> None:
        skills_root = self.codex_root / "skills"
        (skills_root / "SQUAD_MEMORY.md").write_text("# Squad Memory\n", encoding="utf-8")

        seo_root = skills_root / "seo"
        (seo_root / "memory").mkdir(parents=True, exist_ok=True)
        (seo_root / "MEMORY.md").write_text("# SEO Router\n", encoding="utf-8")
        (seo_root / "memory" / "INDEX.md").write_text("# SEO Index\n", encoding="utf-8")
        (seo_root / "memory" / "seo-expert-canon-2026.md").write_text("# SEO Canon\n", encoding="utf-8")

        dejan_root = skills_root / "dejan-ai-reverse-engineering"
        (dejan_root / "references").mkdir(parents=True, exist_ok=True)
        (dejan_root / "SKILL.md").write_text("# DEJAN Skill\n", encoding="utf-8")
        (dejan_root / "references" / "notes.md").write_text("# Reverse Engineering Notes\n", encoding="utf-8")

        orchestrator_root = skills_root / "orchestrator-pinchy"
        (orchestrator_root / "memory").mkdir(parents=True, exist_ok=True)
        (orchestrator_root / "SKILL.md").write_text("# Pinchy\n", encoding="utf-8")
        (orchestrator_root / "MEMORY.md").write_text("# Pinchy Memory\n", encoding="utf-8")
        (orchestrator_root / "memory" / "chief-of-staff.md").write_text("# Chief of Staff\n", encoding="utf-8")

        seo_coral_root = skills_root / "seo-coral"
        (seo_coral_root / "memory").mkdir(parents=True, exist_ok=True)
        (seo_coral_root / "SKILL.md").write_text("# Coral\n", encoding="utf-8")
        (seo_coral_root / "TOOLS.md").write_text("# Coral Tools\n", encoding="utf-8")
        (seo_coral_root / "memory" / "serp-analysis.md").write_text("# SERP Analysis\n", encoding="utf-8")

        (self.codex_root / "memories" / "seo-expert-canon-2026-03-20.md").write_text("# Durable SEO Canon\n", encoding="utf-8")

    def _seed_squad_memory(self) -> None:
        phase21_dir = self.squad_memory_root / "ingest" / "phase21"
        phase31_dir = self.squad_memory_root / "ingest" / "phase31"
        ui_dir = self.squad_memory_root / "memory_graph_ui"
        phase21_dir.mkdir(parents=True, exist_ok=True)
        phase31_dir.mkdir(parents=True, exist_ok=True)
        ui_dir.mkdir(parents=True, exist_ok=True)

        phase21_status = {
            "generated_at": "2026-03-23T02:51:14.095095+00:00",
            "phase21_dir": str(phase21_dir),
            "ingest_root": str(self.squad_memory_root / "ingest"),
            "timeline": [
                {
                    "phase": "phase21",
                    "generated_at": "2026-03-23T02:51:14.095095+00:00",
                    "path": str(phase21_dir / "latest.json"),
                }
            ],
            "alerts": [{"message": "SEO queue has 3 held items."}],
            "queues": {
                "seo": {
                    "label": "SEO",
                    "items_total": 5,
                    "counts": {"approve": 1, "reject": 1, "hold": 3},
                }
            },
            "sources": {
                "seo": {
                    "label": "SEO",
                    "source_count": 15,
                    "ok_source_count": 14,
                    "error_source_count": 0,
                    "stale_source_count": 1,
                    "new_items_total": 2,
                }
            },
            "memory_health": {
                "topics_total": 59,
                "healthy_topics": 52,
                "stale_topics": 3,
                "low_confidence_topics": 2,
                "monitor_only_topics": 1,
            },
            "workspace": {"contexts": [], "items": []},
        }
        (phase21_dir / "control_plane_status.json").write_text(
            json.dumps(phase21_status, indent=2),
            encoding="utf-8",
        )
        (phase21_dir / "control_plane_report.md").write_text(
            "# Phase 21 Squad Control Plane\n\n- Alerts: 1\n- SEO hold: 3\n",
            encoding="utf-8",
        )
        (phase21_dir / "latest.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-23T02:51:14.095095+00:00",
                    "report_path": str(phase21_dir / "control_plane_report.md"),
                    "status_path": str(phase21_dir / "control_plane_status.json"),
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        phase31_graph = {
            "generated_at": "2026-03-23T05:12:12.211301+00:00",
            "meta": {
                "domains_total": 7,
                "packs_total": 11,
                "skills_total": 16,
                "topics_total": 59,
                "memory_paths_total": 8112,
                "chunks_total": 49498,
                "nodes_total": 210,
                "links_total": 284,
                "alerts_total": 8,
                "meetings_total": 2,
                "manual_scorecards": 8,
                "workspace_contexts_total": 1,
                "workspace_items_total": 4,
                "evaluation": {
                    "primary_skill_accuracy": 0.9556,
                    "top3_skill_hit_rate": 1.0,
                    "top5_path_hit_rate": 0.9778,
                },
                "task_evaluation": {
                    "pack_accuracy": 1.0,
                    "pass_rate": 1.0,
                },
            },
            "meetings": [{"id": "meeting-1", "title": "SEO Daily Ops"}],
            "workspace": {"contexts": [{}], "items": [{}, {}, {}, {}]},
        }
        (phase31_dir / "memory_graph.json").write_text(
            json.dumps(phase31_graph, indent=2),
            encoding="utf-8",
        )
        (phase31_dir / "memory_graph_report.md").write_text(
            "# Squad Memory Graph Snapshot\n\n- Nodes: `210`\n- Links: `284`\n",
            encoding="utf-8",
        )
        (phase31_dir / "latest.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-23T05:12:12.211301+00:00",
                    "graph_path": str(phase31_dir / "memory_graph.json"),
                    "report_path": str(phase31_dir / "memory_graph_report.md"),
                    "node_count": 210,
                    "link_count": 284,
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        (ui_dir / "index.html").write_text(
            "<html><body><button data-view='hq'>HQ</button><button data-view='graph-pro'>Graph Pro</button><span>Squad HQ</span></body></html>\n",
            encoding="utf-8",
        )
        (ui_dir / "app.js").write_text('let currentView = "hq";\n', encoding="utf-8")
        (ui_dir / "graph-pro.js").write_text("export const graphPro = true;\n", encoding="utf-8")
        (ui_dir / "styles.css").write_text(".shell[data-view='graph-pro'] {}\n", encoding="utf-8")

        (self.squad_memory_root / "phase21_control_plane.py").write_text(
            "#!/usr/bin/env python3\nprint('phase21')\n",
            encoding="utf-8",
        )
        (self.squad_memory_root / "phase31_memory_graph.py").write_text(
            "#!/usr/bin/env python3\nprint('phase31')\n",
            encoding="utf-8",
        )
        (self.squad_memory_root / "run_phase21_control_plane.sh").write_text(
            "#!/bin/zsh\npython3 phase21_control_plane.py\n",
            encoding="utf-8",
        )
        (self.squad_memory_root / "run_phase31_memory_graph.sh").write_text(
            "#!/bin/zsh\npython3 phase31_memory_graph.py\n",
            encoding="utf-8",
        )

    def _seed_openclaw_workspace(self) -> None:
        automation_dir = self.openclaw_root / "workspace" / "squad" / "seo" / "automation"
        automation_dir.mkdir(parents=True, exist_ok=True)
        (automation_dir / "status.md").write_text("# Automation Status\n\n- Queue: ready\n", encoding="utf-8")

    def _seed_seo_elite_db(self) -> None:
        db_path = self.squad_memory_root / "seo_elite_memory.db"
        with sqlite3.connect(db_path) as con:
            con.execute(
                """
                CREATE TABLE chunks (
                  chunk_id TEXT PRIMARY KEY,
                  path TEXT NOT NULL,
                  heading TEXT,
                  text TEXT NOT NULL,
                  source TEXT,
                  published_on TEXT,
                  freshness INTEGER,
                  topics_json TEXT,
                  tags_json TEXT,
                  confidence REAL,
                  canonical_group TEXT
                )
                """
            )
            con.executemany(
                """
                INSERT INTO chunks
                  (chunk_id, path, heading, text, source, published_on, freshness, topics_json, tags_json, confidence, canonical_group)
                VALUES
                  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        "chunk-1",
                        "memory/articles/example-1.md",
                        "Example One",
                        "Fresh SEO note one.",
                        "seroundtable",
                        "2026-03-23",
                        10,
                        json.dumps(["ai_search"]),
                        json.dumps(["fresh"]),
                        0.9,
                        "example",
                    ),
                    (
                        "chunk-2",
                        "memory/articles/example-2.md",
                        "Example Two",
                        "Fresh SEO note two.",
                        "searchenginejournal",
                        "2026-03-24",
                        9,
                        json.dumps(["indexing"]),
                        json.dumps(["ops"]),
                        0.8,
                        "example",
                    ),
                ],
            )
            con.commit()

    def test_refresh_syncs_skill_packs_and_indexes_them(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_memory.py"),
                "--codex-root",
                str(self.codex_root),
                "--openclaw-root",
                str(self.openclaw_root),
                "--squad-memory-root",
                str(self.squad_memory_root),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)

        counts = payload["sync"]["counts"]
        self.assertEqual(counts["skill_packs"], 3)
        self.assertGreaterEqual(counts["skill_docs"], 8)
        self.assertGreaterEqual(counts["graph_hq_assets"], 14)
        self.assertGreaterEqual(counts["graph_hq_docs"], 5)

        import_root = self.openclaw_root / "workspace" / "memory" / "imports" / "codex"
        self.assertTrue((import_root / "graph-hq" / "INDEX.md").exists())
        self.assertTrue((import_root / "graph-hq" / "phase21" / "HQ_STATUS.md").exists())
        self.assertTrue((import_root / "graph-hq" / "phase31" / "GRAPH_STATUS.md").exists())
        self.assertTrue((import_root / "graph-hq" / "ui" / "HQ_UI.md").exists())
        self.assertTrue((import_root / "graph-hq" / "source" / "BUILD_PIPELINE.md").exists())
        self.assertTrue((import_root / "graph-hq" / "phase31" / "memory_graph.json").exists())
        self.assertTrue((import_root / "graph-hq" / "ui" / "index.html").exists())
        self.assertTrue((import_root / "skill-packs" / "INDEX.md").exists())
        self.assertTrue((import_root / "skill-packs" / "SQUAD_MEMORY.md").exists())
        self.assertTrue((import_root / "skill-packs" / "orchestrator-pinchy" / "SKILL.md").exists())
        self.assertTrue((import_root / "skill-packs" / "seo-coral" / "memory" / "serp-analysis.md").exists())
        self.assertTrue((import_root / "dejan-pack" / "SKILL.md").exists())

        graph_index = (import_root / "graph-hq" / "INDEX.md").read_text(encoding="utf-8")
        hq_ui = (import_root / "graph-hq" / "ui" / "HQ_UI.md").read_text(encoding="utf-8")
        hq_status = (import_root / "graph-hq" / "phase21" / "HQ_STATUS.md").read_text(encoding="utf-8")
        root_router = (self.openclaw_root / "workspace" / "MEMORY.md").read_text(encoding="utf-8")
        seo_router = (self.openclaw_root / "workspace" / "squad" / "seo" / "MEMORY.md").read_text(encoding="utf-8")
        self.assertIn("Graph + HQ Import", graph_index)
        self.assertIn("Graph Pro", hq_ui)
        self.assertIn("Queue Health", hq_status)
        self.assertIn("graph-hq/INDEX.md", root_router)
        self.assertIn("graph-hq/INDEX.md", seo_router)
        self.assertIn("skill-packs/INDEX.md", root_router)
        self.assertIn("skill-packs/INDEX.md", seo_router)

        seo_db = self.openclaw_root / "memory" / "seo.sqlite"
        main_db = self.openclaw_root / "memory" / "main.sqlite"
        with sqlite3.connect(seo_db) as con:
            total_chunks = con.execute("select count(*) from chunks").fetchone()[0]
            skill_hits = con.execute(
                "select count(*) from chunks where path like '%skill-packs/orchestrator-pinchy/%' or path like '%skill-packs/seo-coral/%'"
            ).fetchone()[0]
            graph_hq_hits = con.execute(
                "select count(*) from chunks where path like '%graph-hq/%'"
            ).fetchone()[0]
            automation_hits = con.execute(
                "select count(*) from chunks where path like 'automation/%'"
            ).fetchone()[0]
            bridge_hits = con.execute(
                "select count(*) from chunks where source = 'seo_elite_db'"
            ).fetchone()[0]
        with sqlite3.connect(main_db) as con:
            main_bridge_hits = con.execute(
                "select count(*) from chunks where source = 'seo_elite_db'"
            ).fetchone()[0]

        self.assertGreater(total_chunks, 0)
        self.assertGreater(skill_hits, 0)
        self.assertGreater(graph_hq_hits, 0)
        self.assertGreater(automation_hits, 0)
        self.assertEqual(bridge_hits, 2)
        self.assertEqual(main_bridge_hits, 2)
        self.assertEqual(payload["bridge"]["status"], "ok")
        self.assertEqual(payload["bridge"]["imported_chunks"], 2)
        self.assertEqual(payload["bridge"]["targets"]["seo"]["imported_chunks"], 2)
        self.assertEqual(payload["bridge"]["targets"]["main"]["imported_chunks"], 2)


if __name__ == "__main__":
    unittest.main()
