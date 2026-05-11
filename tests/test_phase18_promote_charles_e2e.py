from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase18PromoteCharlesE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase17_dir = self.root / "ingest" / "phase17"
        self.phase18_dir = self.root / "ingest" / "phase18"

        charles_root = self.skills_root / "charles" / "memory"
        charles_root.mkdir(parents=True, exist_ok=True)

        (charles_root / "platform-native-posting-system.md").write_text(
            "---\ntitle: Platform Native Posting System\ntopic: social_platform_native_system\n---\n\n## Core Concept\nUse native packaging.\n"
        )
        (charles_root / "community-engagement-loop.md").write_text(
            "---\ntitle: Community Engagement Loop\ntopic: community_engagement\n---\n\n## Core Concept\nReplies and escalation matter.\n"
        )
        (charles_root / "social-calendar-and-trend-radar.md").write_text(
            "---\ntitle: Social Calendar And Trend Radar\ntopic: social_calendar_trend_radar\n---\n\n## Core Concept\nPlan around patterns.\n"
        )
        (charles_root / "live-source-buffer.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Live Knowledge Snapshot - Buffer",
                    "topic: social_distribution",
                    "intent: research, monitoring, creator_examples",
                    "role: charles, current, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Live Knowledge Snapshot - Buffer",
                    "",
                    "## Latest Items",
                    "- 2026-03-19 | [A Better Creator Posting Workflow for Multi-Channel Founders](https://example.com/creator-posting-workflow)",
                    "  A reusable workflow for adapting one founder insight across channels without flattening the hook and CTA.",
                    "",
                ]
            )
        )
        (charles_root / "live-source-hootsuite.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Live Knowledge Snapshot - Hootsuite",
                    "topic: platform_changes",
                    "intent: research, monitoring, platform_changes",
                    "role: charles, current, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Live Knowledge Snapshot - Hootsuite",
                    "",
                    "## Latest Items",
                    "- 2026-03-18 | [What Changed On LinkedIn For Creators This Week](https://example.com/linkedin-creators-week)",
                    "  A practical summary of creator-facing platform changes and what should change in the next weekly plan.",
                    "",
                ]
            )
        )
        (charles_root / "live-source-canon-buffer.md").write_text("# Live Source Canon - Buffer\n")
        (charles_root / "live-source-canon-hootsuite.md").write_text("# Live Source Canon - Hootsuite\n")

        self.phase17_dir.mkdir(parents=True, exist_ok=True)
        (self.phase17_dir / "latest.json").write_text(
            json.dumps(
                {
                    "external_canon_path": "charles/memory/charles-external-source-canon-2026.md",
                    "report_path": str(self.phase17_dir / "charles_external_sources_report.md"),
                },
                indent=2,
            )
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase18_creates_charles_drafts(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase18_promote_charles.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase17-manifest",
                str(self.phase17_dir / "latest.json"),
                "--phase18-dir",
                str(self.phase18_dir),
                "--state-path",
                str(self.phase18_dir / "state.json"),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        drafted = {item["draft_filename"] for item in payload["new_candidates"]}
        self.assertIn("buffer-a-better-creator-posting-workflow-for-multi-channel-founders.md", drafted)
        self.assertIn("hootsuite-what-changed-on-linkedin-for-creators-this-week.md", drafted)
        self.assertTrue((self.phase18_dir / "promotion-queue.md").exists())
        self.assertTrue(
            (self.phase18_dir / "drafts" / "buffer-a-better-creator-posting-workflow-for-multi-channel-founders.md").exists()
        )
        self.assertTrue(
            (self.phase18_dir / "drafts" / "hootsuite-what-changed-on-linkedin-for-creators-this-week.md").exists()
        )

        second = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase18_promote_charles.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase17-manifest",
                str(self.phase17_dir / "latest.json"),
                "--phase18-dir",
                str(self.phase18_dir),
                "--state-path",
                str(self.phase18_dir / "state.json"),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        second_payload = json.loads(second.stdout)
        self.assertEqual(second_payload["new_candidates"], [])


if __name__ == "__main__":
    unittest.main()
