from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class OpenClawSeoAutomationE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.status_dir = self.root / "status"
        self.workspace = self.root / "workspace" / "squad" / "seo"
        self.cron_store = self.root / ".openclaw" / "cron" / "jobs.json"
        self.graph_hq_root = self.root / "workspace" / "memory" / "imports" / "codex" / "graph-hq"
        self.status_dir.mkdir(parents=True, exist_ok=True)
        self.workspace.mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root / "phase21").mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root / "phase31").mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root / "ui").mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root.parent / "skill-packs" / "orchestrator-pinchy").mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root.parent / "skill-packs").mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root.parent / "skill-packs" / "INDEX.md").write_text("# Skill Packs\n", encoding="utf-8")
        (self.graph_hq_root.parent / "skill-packs" / "orchestrator-pinchy" / "SKILL.md").write_text("# Pinchy\n", encoding="utf-8")
        (self.graph_hq_root.parent / "skill-packs" / "researcher-kelp").mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root.parent / "skill-packs" / "researcher-kelp" / "SKILL.md").write_text("# Kelp\n", encoding="utf-8")
        (self.graph_hq_root.parent / "skill-packs" / "seo-coral").mkdir(parents=True, exist_ok=True)
        (self.graph_hq_root.parent / "skill-packs" / "seo-coral" / "SKILL.md").write_text("# Coral\n", encoding="utf-8")
        (self.graph_hq_root / "phase21" / "control_plane_status.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-23T02:30:00+00:00",
                    "alerts": [{"message": "SEO queue has 40 held items."}],
                    "queues": {
                        "seo": {
                            "label": "SEO",
                            "items_total": 88,
                            "counts": {"approve": 17, "reject": 31, "hold": 40},
                        }
                    },
                    "sources": {
                        "seo": {
                            "label": "SEO",
                            "source_count": 15,
                            "ok_source_count": 15,
                            "stale_source_count": 3,
                            "new_items_total": 3,
                        }
                    },
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        (self.graph_hq_root / "phase21" / "HQ_STATUS.md").write_text("# HQ Status\n\n- Queue Health\n", encoding="utf-8")
        (self.graph_hq_root / "phase31" / "memory_graph.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-23T02:35:00+00:00",
                    "meta": {
                        "topics_total": 59,
                        "memory_paths_total": 8112,
                        "links_total": 284,
                        "alerts_total": 8,
                        "meetings_total": 2,
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
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        (self.graph_hq_root / "phase31" / "GRAPH_STATUS.md").write_text("# Graph Status\n\n- Topics: 59\n", encoding="utf-8")
        (self.graph_hq_root / "ui" / "HQ_UI.md").write_text("# HQ UI\n\n- Graph Pro\n", encoding="utf-8")

        self.status_json = self.status_dir / "latest-status.json"
        self.status_md = self.status_dir / "latest-status.md"
        self.status_json.write_text(
            json.dumps(
                {
                    "updated_at": "2026-03-23 02:00:00 UTC",
                    "updated_at_iso": "2026-03-23T02:00:00+00:00",
                    "goal": {"target_chunks": 30000, "progress_percent": 82.4, "over_target": False},
                    "db": {
                        "chunks": 24720,
                        "paths": 920,
                        "primary_chunks": 320,
                        "live_article_chunks": 8000,
                        "archive_article_chunks": 11000,
                        "google_patent_chunks": 120,
                        "google_search_central_chunks": 90,
                        "google_crawling_chunks": 40,
                    },
                    "coverage": {
                        "live_source_notes": 34,
                        "archive_source_notes": 112,
                        "primary_source_notes": 8,
                    },
                    "articles": {
                        "live_article_notes": 240,
                        "archive_article_notes": 640,
                    },
                    "monitors": {
                        "live_monitor_updated": "2026-03-23 02:00:00 UTC",
                        "archive_monitor_updated": "2026-03-23 01:30:00 UTC",
                    },
                    "recent_knowledge": {
                        "live_articles": [
                            {"path": "memory/articles/dejan/new-note.md", "updated": "2026-03-23 01:58:00 UTC"},
                            {"path": "memory/articles/ahrefs/fresh.md", "updated": "2026-03-23 01:54:00 UTC"},
                        ],
                        "archive_articles": [],
                        "primary_notes": [
                            {"path": "memory/primary/google-search-central.md", "updated": "2026-03-23 01:30:00 UTC"},
                        ],
                    },
                    "logs": {
                        "live_sync": [],
                        "primary_refresh": [],
                        "archive_backfill": [],
                        "article_harvest": [],
                        "bulk_backfill": [],
                    },
                    "active_jobs": [
                        {"job": "live_sync", "status": "active", "updated_at": "2026-03-23 01:58:00 UTC", "age_seconds": 120},
                        {"job": "bulk_backfill", "status": "idle", "updated_at": "2026-03-22 20:00:00 UTC", "age_seconds": 21600},
                    ],
                    "pending": {
                        "pending_total": 320,
                        "failed_total": 3,
                        "fetched_total": 150,
                        "top_sources": [
                            {"source": "dejan.ai", "count": 40},
                            {"source": "ahrefs.com", "count": 22},
                        ],
                        "sample_urls": [],
                    },
                    "activity": {
                        "current_phase": "discovering",
                        "recent_fetch_total": 12,
                        "recent_fetch_ok": 10,
                        "recent_fetch_error": 2,
                        "recent_fetch_window_seconds": 120,
                        "recent_fetch_sources": [
                            {"source": "dejan.ai", "count": 5},
                            {"source": "ahrefs.com", "count": 3},
                        ],
                        "recent_error_sources": [
                            {"source": "semrush.com", "count": 2},
                        ],
                        "latest_fetch_source": "dejan.ai",
                        "latest_fetch_url": "https://dejan.ai/example",
                        "latest_fetch_code": 200,
                        "latest_fetch_at": "2026-03-23 01:59:00 UTC",
                        "top_fetch_sources": [],
                        "top_error_sources": [],
                        "ticker": [],
                    },
                    "sources": {
                        "snapshots": [],
                        "live_article_sources": [
                            {"source": "dejan", "layer": "live", "article_count": 22, "updated_at": "2026-03-23 01:58:00 UTC"},
                            {"source": "ahrefs", "layer": "live", "article_count": 18, "updated_at": "2026-03-23 01:54:00 UTC"},
                        ],
                        "archive_article_sources": [],
                    },
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        self.status_md.write_text("# SEO Elite Status\n\nFixture status.\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_refresh_and_install_generate_openclaw_artifacts(self) -> None:
        refresh = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_seo_automation.py"),
                "--status-json",
                str(self.status_json),
                "--status-md",
                str(self.status_md),
                "--openclaw-workspace",
                str(self.workspace),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        refresh_payload = json.loads(refresh.stdout)
        self.assertEqual(refresh_payload["status"], "ok")
        self.assertTrue((self.workspace / "automation" / "README.md").exists())
        self.assertTrue((self.workspace / "automation" / "digest" / "latest.json").exists())
        self.assertTrue((self.workspace / "automation" / "prompts" / "watchtower.md").exists())
        self.assertTrue((self.workspace / "automation" / "prompts" / "mission-runner.md").exists())
        self.assertTrue((self.workspace / "automation" / "prompts" / "hq-mission-runner.md").exists())
        self.assertTrue((self.workspace / "automation" / "control" / "command-center.md").exists())
        self.assertTrue((self.workspace / "automation" / "hq" / "current-plan.md").exists())
        self.assertTrue((self.workspace / "automation" / "hq" / "current-plan-deterministic.md").exists())
        self.assertTrue((self.workspace / "automation" / "hq" / "role-handoffs.md").exists())
        self.assertTrue((self.workspace / "automation" / "capabilities" / "local-stack.md").exists())
        self.assertTrue((self.workspace / "automation" / "capabilities" / "workflows.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "catalog.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "prose" / "freshness-radar.prose").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "execution" / "freshness-radar.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "execution" / "current-queue.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "execution" / "progress-state.json").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "execution" / "action-runner-state.json").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "router" / "next-best-mission.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "router" / "next-best-mission-deterministic.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "router" / "next-best-mission-trusted.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "router" / "mission-scoreboard.md").exists())
        self.assertTrue((self.workspace / "automation" / "missions" / "router" / "history.json").exists())
        self.assertTrue((self.workspace / "automation" / "outbox" / "watchtower-deterministic.md").exists())
        self.assertTrue((self.workspace / "automation" / "outbox" / "watchtower-trusted.md").exists())
        self.assertTrue((self.workspace / "automation" / "outbox" / "opportunity-radar-trusted.md").exists())
        self.assertTrue((self.workspace / "automation" / "outbox" / "daily-ops-plan-trusted.md").exists())
        self.assertIn(
            "Generated by deterministic fallback",
            (self.workspace / "automation" / "outbox" / "watchtower-latest.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "trusted-source",
            (self.workspace / "automation" / "outbox" / "watchtower-trusted.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Generated by deterministic fallback",
            (self.workspace / "automation" / "missions" / "outbox" / "freshness-radar.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "watchtower-trusted.md",
            (self.workspace / "automation" / "prompts" / "daily-ops-plan.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "opportunity-radar-trusted.md",
            (self.workspace / "automation" / "prompts" / "daily-ops-plan.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "watchtower-trusted.md",
            (self.workspace / "automation" / "control" / "command-center.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "current-plan-trusted.md",
            (self.workspace / "automation" / "control" / "command-center.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Role Handoffs",
            (self.workspace / "automation" / "hq" / "current-plan-deterministic.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Collect Fresh Signals",
            (self.workspace / "automation" / "hq" / "role-handoffs.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "current-queue.md",
            (self.workspace / "automation" / "control" / "command-center.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Action Runner",
            (self.workspace / "automation" / "control" / "command-center.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Collect Fresh Signals",
            (self.workspace / "automation" / "missions" / "execution" / "current-queue.md").read_text(encoding="utf-8"),
        )
        self.assertIn("hq_fit", refresh_payload["missions"]["automatic_route"]["score_breakdown"])
        self.assertEqual(refresh_payload["hq"]["status"], "ok")
        self.assertIsNotNone(refresh_payload["hq"]["current_focus_role"])
        self.assertEqual(refresh_payload["action_runner"]["status"], "ok")
        self.assertEqual(refresh_payload["action_runner"]["executed_count"], 1)
        self.assertEqual(refresh_payload["missions"]["current_queue"]["summary"]["done"], 1)
        self.assertEqual(
            refresh_payload["missions"]["current_queue"]["current_focus"]["title"],
            "Retrieve Supporting Canon",
        )
        self.assertTrue(
            (
                self.workspace
                / "automation"
                / "missions"
                / "execution"
                / "artifacts"
                / "freshness-radar"
                / "collect-fresh-signals.md"
            ).exists()
        )

        digest = json.loads((self.workspace / "automation" / "digest" / "latest.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(digest["alerts"]), 2)
        self.assertGreaterEqual(len(digest["opportunities"]), 3)

        second_refresh = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_seo_automation.py"),
                "--status-json",
                str(self.status_json),
                "--status-md",
                str(self.status_md),
                "--openclaw-workspace",
                str(self.workspace),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        second_refresh_payload = json.loads(second_refresh.stdout)
        self.assertEqual(second_refresh_payload["action_runner"]["executed_count"], 1)
        self.assertEqual(second_refresh_payload["missions"]["current_queue"]["summary"]["done"], 2)
        self.assertEqual(
            second_refresh_payload["missions"]["current_queue"]["current_focus"]["title"],
            "Draft Same-Day Brief",
        )
        self.assertTrue(
            (
                self.workspace
                / "automation"
                / "missions"
                / "execution"
                / "artifacts"
                / "freshness-radar"
                / "retrieve-supporting-canon.md"
            ).exists()
        )

        third_refresh = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_seo_automation.py"),
                "--status-json",
                str(self.status_json),
                "--status-md",
                str(self.status_md),
                "--openclaw-workspace",
                str(self.workspace),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        third_refresh_payload = json.loads(third_refresh.stdout)
        self.assertEqual(third_refresh_payload["action_runner"]["executed_count"], 1)
        self.assertEqual(third_refresh_payload["missions"]["current_queue"]["summary"]["done"], 3)
        self.assertEqual(
            third_refresh_payload["missions"]["current_queue"]["current_focus"]["title"],
            "Publish Priority Output",
        )
        self.assertTrue(
            (
                self.workspace
                / "automation"
                / "missions"
                / "execution"
                / "artifacts"
                / "freshness-radar"
                / "draft-same-day-brief.md"
            ).exists()
        )

        fourth_refresh = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_seo_automation.py"),
                "--status-json",
                str(self.status_json),
                "--status-md",
                str(self.status_md),
                "--openclaw-workspace",
                str(self.workspace),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        fourth_refresh_payload = json.loads(fourth_refresh.stdout)
        self.assertEqual(fourth_refresh_payload["action_runner"]["executed_count"], 1)
        self.assertEqual(fourth_refresh_payload["missions"]["current_queue"]["summary"]["done"], 4)
        self.assertIsNone(fourth_refresh_payload["missions"]["current_queue"]["current_focus"])
        self.assertIn(
            "Generated by action runner",
            (self.workspace / "automation" / "missions" / "outbox" / "freshness-radar.md").read_text(encoding="utf-8"),
        )
        self.assertGreaterEqual(
            len(fourth_refresh_payload["missions"]["current_queue"]["auto_progress"]["advanced"]),
            1,
        )

        mission_route = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_seo_missions.py"),
                "--workspace",
                str(self.workspace),
                "--status-json",
                str(self.workspace / "automation" / "data" / "latest-status.json"),
                "--digest-json",
                str(self.workspace / "automation" / "digest" / "latest.json"),
                "--goal",
                "debug indexing coverage issue",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        mission_payload = json.loads(mission_route.stdout)
        self.assertEqual(mission_payload["status"], "ok")
        self.assertEqual(mission_payload["goal_route"]["selected"]["id"], "indexation-war-room")
        self.assertIn("confidence", mission_payload["automatic_route"])
        self.assertIn("score_breakdown", mission_payload["automatic_route"])
        self.assertTrue((self.workspace / "automation" / "missions" / "router" / "goal-route.md").exists())
        self.assertIn(
            "indexation-war-room",
            (self.workspace / "automation" / "missions" / "router" / "current-mission.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Indexation War Room",
            (self.workspace / "automation" / "missions" / "execution" / "current-queue.md").read_text(encoding="utf-8"),
        )

        cannibalization_route = subprocess.run(
            [
                sys.executable,
                str(BASE / "refresh_openclaw_seo_missions.py"),
                "--workspace",
                str(self.workspace),
                "--status-json",
                str(self.workspace / "automation" / "data" / "latest-status.json"),
                "--digest-json",
                str(self.workspace / "automation" / "digest" / "latest.json"),
                "--goal",
                "find cannibalization problems",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        cannibalization_payload = json.loads(cannibalization_route.stdout)
        self.assertEqual(cannibalization_payload["goal_route"]["selected"]["id"], "cannibalization-cleanup")
        self.assertIn(
            "Cannibalization Cleanup",
            (self.workspace / "automation" / "missions" / "execution" / "current-queue.md").read_text(encoding="utf-8"),
        )

        install = subprocess.run(
            [
                sys.executable,
                str(BASE / "install_openclaw_seo_cron.py"),
                "--workspace",
                str(self.workspace),
                "--cron-store",
                str(self.cron_store),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        install_payload = json.loads(install.stdout)
        self.assertEqual(install_payload["managed_job_count"], 5)
        store = json.loads(self.cron_store.read_text(encoding="utf-8"))
        self.assertEqual(store["version"], 1)
        self.assertEqual(len(store["jobs"]), 5)
        by_id = {job["id"]: job for job in store["jobs"]}
        self.assertIn("seo_ops_watchtower", by_id)
        self.assertIn("seo_workflow_router", by_id)
        self.assertIn("seo_hq_mission_runner", by_id)
        self.assertIn("automation/outbox/watchtower-latest.md", by_id["seo_ops_watchtower"]["payload"]["message"])
        self.assertIn("automation/control/command-center.md", by_id["seo_ops_watchtower"]["payload"]["message"])
        self.assertIn("automation/missions/execution/current-queue.md", by_id["seo_ops_watchtower"]["payload"]["message"])
        self.assertIn("automation/missions/router/next-best-mission.md", by_id["seo_workflow_router"]["payload"]["message"])
        self.assertIn("automation/missions/router/mission-scoreboard.md", by_id["seo_workflow_router"]["payload"]["message"])
        self.assertIn("automation/hq/current-plan.md", by_id["seo_hq_mission_runner"]["payload"]["message"])
        self.assertIn("../../memory/imports/codex/graph-hq/phase21/HQ_STATUS.md", by_id["seo_hq_mission_runner"]["payload"]["message"])
        self.assertIn("automation/missions/execution/current-queue.md", by_id["seo_daily_ops_plan"]["payload"]["message"])
        self.assertIn("automation/outbox/watchtower-trusted.md", by_id["seo_daily_ops_plan"]["payload"]["message"])
        self.assertIn("automation/outbox/opportunity-radar-trusted.md", by_id["seo_daily_ops_plan"]["payload"]["message"])
        self.assertEqual(by_id["seo_ops_watchtower"]["delivery"]["mode"], "none")


if __name__ == "__main__":
    unittest.main()
