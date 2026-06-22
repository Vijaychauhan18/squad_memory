from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase14PromoteWriterMarketingApprovedE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.db_path = self.root / "squad_memory.db"
        self.phase13_dir = self.root / "ingest" / "phase13"
        self.phase14_dir = self.root / "ingest" / "phase14"

        writer_root = self.skills_root / "writer" / "memory"
        marketing_root = self.skills_root / "marketing" / "memory"
        writer_root.mkdir(parents=True, exist_ok=True)
        marketing_root.mkdir(parents=True, exist_ok=True)

        (self.skills_root / "writer" / "MEMORY.md").write_text("# Writer Memory Router\n\n## Routing Guide\n- Existing\n")
        (self.skills_root / "marketing" / "MEMORY.md").write_text("# Marketing Memory Router\n\n## Routing Guide\n- Existing\n")
        (writer_root / "landing-page-copy.md").write_text("---\ntitle: Landing Page Copy\n---\n\n## Core Concept\nConversion copy.\n")
        (marketing_root / "platform-native-posts.md").write_text("---\ntitle: Platform Native Posts\n---\n\n## Core Concept\nAdapt to platform.\n")

        drafts_dir = self.phase13_dir / "drafts"
        drafts_dir.mkdir(parents=True, exist_ok=True)
        (drafts_dir / "writer-draft.md").write_text(
            "\n".join(
                [
                    "---",
                    "topic: conversion_copywriting",
                    "intent: research, monitoring, writing_examples",
                    "role: writer, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - Better CTA Copy",
                    "",
                    "Source article: [Better CTA Copy](https://example.com/better-cta)",
                    "Source canon: `writer/memory/live-source-canon-copyhackers.md`",
                    "Published: 2026-03-19",
                    "Domain: writer",
                    "Source topic: conversion_copywriting",
                    "",
                    "## Source Signal",
                    "A tighter CTA framework that improves clarity and conversion intent.",
                    "",
                    "## Why This Candidate Is In Queue",
                    "- Strong fit for conversion-oriented writer memory.",
                    "",
                    "## Draft Summary",
                    "- Better CTA language for landing pages.",
                    "",
                    "## Suggested Placement",
                    "- Review against `memory/landing-page-copy.md`.",
                    "",
                ]
            )
        )
        (drafts_dir / "marketing-draft.md").write_text(
            "\n".join(
                [
                    "---",
                    "topic: social_distribution",
                    "intent: research, monitoring, distribution_examples",
                    "role: marketing, charles, pinchy",
                    "confidence: high",
                    "---",
                    "",
                    "# Promotion Candidate - Better Social Packaging",
                    "",
                    "Source article: [Better Social Packaging](https://example.com/better-social-packaging)",
                    "Source canon: `marketing/memory/live-source-canon-buffer.md`",
                    "Published: 2026-03-18",
                    "Domain: marketing",
                    "Source topic: social_distribution",
                    "",
                    "## Source Signal",
                    "A reusable way to adapt the same content into channel-native social variants.",
                    "",
                    "## Why This Candidate Is In Queue",
                    "- Strong fit for marketing distribution memory.",
                    "",
                    "## Draft Summary",
                    "- Better packaging for platform-native social posts.",
                    "",
                    "## Suggested Placement",
                    "- Review against `memory/platform-native-posts.md`.",
                    "",
                ]
            )
        )

        self.phase13_dir.mkdir(parents=True, exist_ok=True)
        (self.phase13_dir / "latest.json").write_text(
            json.dumps(
                {
                    "phase13_dir": str(self.phase13_dir),
                    "tracked_candidates": [
                        {
                            "draft_filename": "writer-draft.md",
                            "domain": "writer",
                            "title": "Better CTA Copy",
                            "link": "https://example.com/better-cta",
                            "published": "2026-03-19",
                            "source_slug": "copyhackers",
                            "draft_topic": "conversion_copywriting",
                            "score": 0.81,
                            "routing": {
                                "suggested_note": "memory/landing-page-copy.md",
                                "suggested_bundle": "Plankton Bundle",
                                "reason": "This belongs with conversion-focused copy and CTA structure.",
                            },
                        },
                        {
                            "draft_filename": "marketing-draft.md",
                            "domain": "marketing",
                            "title": "Better Social Packaging",
                            "link": "https://example.com/better-social-packaging",
                            "published": "2026-03-18",
                            "source_slug": "buffer",
                            "draft_topic": "social_distribution",
                            "score": 0.79,
                            "routing": {
                                "suggested_note": "memory/platform-native-posts.md",
                                "suggested_bundle": "Current Bundle",
                                "reason": "This is a channel and platform adaptation signal.",
                            },
                        },
                    ],
                },
                indent=2,
            )
            + "\n"
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase14_requires_approval_before_promotion(self) -> None:
        first = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase14_promote_writer_marketing_approved.py"),
                "--phase13-manifest",
                str(self.phase13_dir / "latest.json"),
                "--phase14-dir",
                str(self.phase14_dir),
                "--decisions-path",
                str(self.phase14_dir / "decisions.json"),
                "--state-path",
                str(self.phase14_dir / "state.json"),
                "--skills-root",
                str(self.skills_root),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(first.stdout)
        self.assertEqual(payload["promoted_now"], [])
        self.assertTrue((self.phase14_dir / "decisions.json").exists())
        self.assertTrue((self.phase14_dir / "review-status.md").exists())
        self.assertFalse((self.skills_root / "writer" / "memory" / "writer-draft.md").exists())
        self.assertNotIn("BEGIN AUTO APPROVED EXTERNAL PROMOTIONS", (self.skills_root / "writer" / "MEMORY.md").read_text())

        decisions = json.loads((self.phase14_dir / "decisions.json").read_text())
        items = {item["draft_filename"]: item for item in decisions["items"]}
        items["writer-draft.md"]["status"] = "approve"
        items["marketing-draft.md"]["status"] = "approve"
        (self.phase14_dir / "decisions.json").write_text(json.dumps(decisions, indent=2) + "\n")

        second = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase14_promote_writer_marketing_approved.py"),
                "--phase13-manifest",
                str(self.phase13_dir / "latest.json"),
                "--phase14-dir",
                str(self.phase14_dir),
                "--decisions-path",
                str(self.phase14_dir / "decisions.json"),
                "--state-path",
                str(self.phase14_dir / "state.json"),
                "--skills-root",
                str(self.skills_root),
                "--db-path",
                str(self.db_path),
                "--build-db",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        second_payload = json.loads(second.stdout)
        self.assertEqual(len(second_payload["promoted_now"]), 2)
        self.assertTrue((self.skills_root / "writer" / "memory" / "writer-draft.md").exists())
        self.assertTrue((self.skills_root / "marketing" / "memory" / "marketing-draft.md").exists())
        self.assertTrue(self.db_path.exists())

        writer_router = (self.skills_root / "writer" / "MEMORY.md").read_text()
        marketing_router = (self.skills_root / "marketing" / "MEMORY.md").read_text()
        self.assertIn("BEGIN AUTO APPROVED EXTERNAL PROMOTIONS", writer_router)
        self.assertIn("memory/writer-draft.md", writer_router)
        self.assertIn("BEGIN AUTO APPROVED EXTERNAL PROMOTIONS", marketing_router)
        self.assertIn("memory/marketing-draft.md", marketing_router)


if __name__ == "__main__":
    unittest.main()
