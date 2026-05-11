from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase21ControlPlaneE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.ingest_root = self.root / "ingest"
        self.phase21_dir = self.ingest_root / "phase21"
        self.skills_root = self.root / "skills"
        (self.skills_root / "charles" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "charles" / "MEMORY.md").write_text(
            "# Charles Memory Router\n\n## Charles Bundle\n- Existing bundle note\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_report_aggregates_sparse_artifacts(self) -> None:
        (self.ingest_root / "runs").mkdir(parents=True, exist_ok=True)
        (self.ingest_root / "runs" / "latest.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-20T06:00:00+00:00",
                    "results": [
                        {
                            "slug": "ahrefs",
                            "name": "Ahrefs",
                            "status": "ok",
                            "new_item_count": 1,
                            "latest_published": "2026-03-19",
                        },
                        {
                            "slug": "old-source",
                            "name": "Old Source",
                            "status": "ok",
                            "new_item_count": 0,
                            "latest_published": "2025-12-01",
                        },
                    ],
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        for phase_name, items in (
            ("phase6", [{"draft_filename": "seo-item.md", "status": "hold", "title": "SEO item", "score": 0.9}]),
            ("phase14", [{"draft_filename": "writer-item.md", "status": "approve", "title": "Writer item", "score": 0.8}]),
            ("phase19", [{"draft_filename": "charles-item.md", "status": "reject", "title": "Charles item", "score": 0.7}]),
        ):
            phase_dir = self.ingest_root / phase_name
            phase_dir.mkdir(parents=True, exist_ok=True)
            (phase_dir / "decisions.json").write_text(
                json.dumps({"generated_at": "2026-03-20T06:00:00+00:00", "items": items}, indent=2),
                encoding="utf-8",
            )
        (self.ingest_root / "phase12").mkdir(parents=True, exist_ok=True)
        (self.ingest_root / "phase12" / "latest.json").write_text(
            json.dumps(
                {
                    "domains": [
                        {"domain": "writer", "source_count": 2, "ok_source_count": 2, "error_source_count": 0, "failed_sources": [], "live_note_count": 2, "source_canon_count": 2},
                        {"domain": "marketing", "source_count": 3, "ok_source_count": 2, "error_source_count": 1, "failed_sources": [{"slug": "blocked", "status": "403"}], "live_note_count": 2, "source_canon_count": 2},
                    ]
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        (self.ingest_root / "phase17").mkdir(parents=True, exist_ok=True)
        (self.ingest_root / "phase17" / "latest.json").write_text(
            json.dumps(
                {
                    "source_count": 2,
                    "ok_source_count": 2,
                    "error_source_count": 0,
                    "failed_sources": [],
                    "live_note_count": 2,
                    "source_canon_count": 2,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        (self.ingest_root / "phase7").mkdir(parents=True, exist_ok=True)
        (self.ingest_root / "phase7" / "latest.json").write_text(
            json.dumps(
                {
                    "generated_at": "2026-03-20T06:00:00+00:00",
                    "health": {
                        "topics_total": 10,
                        "healthy_topics": 8,
                        "topics_needing_canonical": 1,
                        "monitor_only_topics": 1,
                        "legacy_only_topics": 0,
                        "note_status_counts": {"stale_legacy_feed": 2, "merge_candidate": 3},
                    },
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        (self.ingest_root / "phase10").mkdir(parents=True, exist_ok=True)
        (self.ingest_root / "phase10" / "evidence_ledger.json").write_text(
            json.dumps(
                {
                    "topics": {
                        "ai_visibility": {
                            "topic": "ai_visibility",
                            "source_count": 2,
                            "tension": ["Source disagreement."],
                            "confidence_label": "medium",
                            "freshness_label": "current",
                        },
                        "stale_topic": {
                            "topic": "stale_topic",
                            "source_count": 1,
                            "tension": [],
                            "confidence_label": "low",
                            "freshness_label": "aging",
                        },
                    }
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        (self.ingest_root / "phase15").mkdir(parents=True, exist_ok=True)
        (self.ingest_root / "phase15" / "latest.json").write_text(
            json.dumps(
                {
                    "task_outcomes": 4,
                    "status_breakdown": [{"status": "accepted", "count": 3, "rate": 0.75}],
                    "top_outcome_skills": ["seo", "charles"],
                    "top_packs": ["ai_visibility_audit"],
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase21_control_plane.py"),
                "report",
                "--phase21-dir",
                str(self.phase21_dir),
                "--ingest-root",
                str(self.ingest_root),
                "--skills-root",
                str(self.skills_root),
                "--db-path",
                str(self.root / "missing.db"),
                "--fixtures",
                str(self.root / "missing-fixtures.json"),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertTrue((self.phase21_dir / "control_plane_status.json").exists())
        self.assertTrue((self.phase21_dir / "control_plane_report.md").exists())
        self.assertTrue((self.phase21_dir / "latest.json").exists())
        self.assertGreaterEqual(len(payload["alerts"]), 1)
        report_text = (self.phase21_dir / "control_plane_report.md").read_text(encoding="utf-8")
        self.assertIn("SEO queue has 1 held item(s).", report_text)
        self.assertIn("Cross-source tension topics", report_text)

    def test_queue_action_routes_through_charles_gate(self) -> None:
        phase18_dir = self.ingest_root / "phase18"
        phase19_dir = self.ingest_root / "phase19"
        drafts_dir = phase18_dir / "drafts"
        drafts_dir.mkdir(parents=True, exist_ok=True)
        (drafts_dir / "buffer-workflow.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - Buffer Workflow",
                    "topic: social_distribution",
                    "intent: research, monitoring",
                    "role: charles, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - Buffer Workflow",
                    "",
                    "## Source Signal",
                    "A platform-native workflow for repurposing one idea across channels.",
                    "",
                    "## Draft Summary",
                    "- Platform-native social workflow.",
                    "",
                    "## Why This Candidate Is In Queue",
                    "- Durable Charles operating note.",
                    "",
                    "## Suggested Placement",
                    "- memory/platform-native-posting-system.md",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (drafts_dir / "stats-roundup.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Promotion Candidate - 30+ social statistics marketers need to know",
                    "topic: social_distribution",
                    "intent: research, monitoring",
                    "role: charles, pinchy",
                    "confidence: medium",
                    "---",
                    "",
                    "# Promotion Candidate - Stats Roundup",
                    "",
                    "## Source Signal",
                    "A broad statistics list.",
                    "",
                    "## Draft Summary",
                    "- Statistics round-up without operating workflow.",
                    "",
                    "## Why This Candidate Is In Queue",
                    "- Candidate queued from external monitor.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (phase18_dir / "latest.json").write_text(
            json.dumps({"phase18_dir": str(phase18_dir), "tracked_candidates": []}, indent=2),
            encoding="utf-8",
        )
        phase19_dir.mkdir(parents=True, exist_ok=True)
        (phase19_dir / "latest.json").write_text(
            json.dumps({"phase18_manifest": str(phase18_dir / "latest.json")}, indent=2),
            encoding="utf-8",
        )
        (phase19_dir / "decisions.json").write_text(
            json.dumps(
                {
                    "items": [
                        {
                            "draft_filename": "buffer-workflow.md",
                            "domain": "charles",
                            "status": "hold",
                            "title": "Buffer Workflow",
                            "source_slug": "buffer",
                            "draft_topic": "social_distribution",
                            "score": 0.95,
                            "final_filename": "buffer-workflow.md",
                            "promoted_path": "",
                            "routing": {"suggested_bundle": "Charles Bundle"},
                        },
                        {
                            "draft_filename": "stats-roundup.md",
                            "domain": "charles",
                            "status": "hold",
                            "title": "Stats Roundup",
                            "source_slug": "hootsuite",
                            "draft_topic": "social_distribution",
                            "score": 0.72,
                            "final_filename": "stats-roundup.md",
                            "promoted_path": "",
                            "routing": {"suggested_bundle": "Charles Bundle"},
                        },
                    ]
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase21_control_plane.py"),
                "queue-action",
                "--domain",
                "charles",
                "--phase21-dir",
                str(self.phase21_dir),
                "--ingest-root",
                str(self.ingest_root),
                "--skills-root",
                str(self.skills_root),
                "--approve",
                "buffer-workflow.md",
                "--reject",
                "stats-roundup.md",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        decisions = json.loads((phase19_dir / "decisions.json").read_text(encoding="utf-8"))
        by_name = {item["draft_filename"]: item for item in decisions["items"]}
        self.assertEqual(by_name["buffer-workflow.md"]["status"], "approve")
        self.assertEqual(by_name["stats-roundup.md"]["status"], "reject")
        self.assertTrue((self.skills_root / "charles" / "memory" / "buffer-workflow.md").exists())
        self.assertTrue((self.ingest_root / "phase20" / "triage.json").exists())
        self.assertTrue((self.phase21_dir / "latest.json").exists())
        self.assertEqual(payload["queue_counts"]["approve"], 1)
        self.assertEqual(payload["queue_counts"]["reject"], 1)


if __name__ == "__main__":
    unittest.main()
