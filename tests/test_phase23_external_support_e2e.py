from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


def rss_feed(title: str, item_title: str, item_link: str, published: str, description: str) -> str:
    return "\n".join(
        [
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
            "<rss version=\"2.0\">",
            "<channel>",
            f"<title>{title}</title>",
            f"<item><title>{item_title}</title><link>{item_link}</link><pubDate>{published}</pubDate><description>{description}</description></item>",
            "</channel>",
            "</rss>",
            "",
        ]
    )


class Phase23ExternalSupportE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase23_dir = self.root / "ingest" / "phase23"
        self.db_path = self.root / "squad_memory.db"
        self.config_path = self.root / "knowledge_sources_support.json"
        self.feeds_dir = self.root / "feeds"
        self.feeds_dir.mkdir(parents=True, exist_ok=True)

        support_root = self.skills_root / "support-anemone"
        (support_root / "memory").mkdir(parents=True, exist_ok=True)
        (support_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Support Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Anemone Operating Canon 2026: `memory/anemone-operating-canon-2026.md`",
                    "",
                    "## Anemone Bundle",
                    "- `memory/anemone-operating-canon-2026.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/anemone-operating-canon-2026.md`",
                    "",
                    "## Urchin Bundle",
                    "- `memory/anemone-operating-canon-2026.md`",
                    "",
                    "## Chitin Bundle",
                    "- `memory/anemone-operating-canon-2026.md`",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (support_root / "memory" / "anemone-operating-canon-2026.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Anemone Operating Canon 2026",
                    "topic: support_core",
                    "canonical: true",
                    "confidence: high",
                    "---",
                    "",
                    "# Anemone Operating Canon 2026",
                    "",
                    "## Core Concept",
                    "Base Anemone workflow.",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        helpscout_feed = self.feeds_dir / "helpscout.xml"
        helpscout_feed.write_text(
            rss_feed(
                "Help Scout",
                "How to tighten support handoffs",
                "https://example.com/helpscout-handoff",
                "Thu, 19 Mar 2026 10:00:00 +0000",
                "Support handoff guidance.",
            ),
            encoding="utf-8",
        )
        intercom_feed = self.feeds_dir / "intercom.xml"
        intercom_feed.write_text(
            rss_feed(
                "Intercom",
                "A better escalation workflow",
                "https://example.com/intercom-escalation",
                "Wed, 18 Mar 2026 09:00:00 +0000",
                "Escalation workflow summary.",
            ),
            encoding="utf-8",
        )

        self.config_path.write_text(
            json.dumps(
                {
                    "name": "Phase 23 Fixture",
                    "sources": [
                        {
                            "slug": "helpscout",
                            "name": "Help Scout",
                            "homepage": "https://www.helpscout.com/blog/",
                            "kind": "publication",
                            "strength": "support systems and help-center strategy",
                            "topic": "support_operations",
                            "confidence": "high",
                            "roles": ["support-anemone", "pinchy", "operations"],
                            "intent": ["research", "monitoring", "documentation_patterns"],
                            "tags": ["helpscout", "fixture"],
                            "feed_urls": [helpscout_feed.as_uri()],
                        },
                        {
                            "slug": "intercom",
                            "name": "Intercom Blog",
                            "homepage": "https://www.intercom.com/blog/",
                            "kind": "publication",
                            "strength": "support workflows and escalation patterns",
                            "topic": "support_operations",
                            "confidence": "high",
                            "roles": ["support-anemone", "pinchy", "operations"],
                            "intent": ["research", "monitoring", "escalation_patterns"],
                            "tags": ["intercom", "fixture"],
                            "feed_urls": [intercom_feed.as_uri()],
                        },
                        {
                            "slug": "disabled-source",
                            "name": "Disabled Source",
                            "homepage": "https://example.com/disabled",
                            "kind": "publication",
                            "strength": "should be skipped when disabled",
                            "topic": "support_operations",
                            "confidence": "medium",
                            "roles": ["support-anemone", "pinchy"],
                            "intent": ["research", "monitoring"],
                            "tags": ["disabled", "fixture"],
                            "enabled": False,
                            "feed_urls": ["https://example.com/disabled/feed.xml"],
                        },
                    ],
                },
                indent=2,
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase23_ingests_and_fuses_support_external_sources(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase23_external_support.py"),
                "--config",
                str(self.config_path),
                "--skills-root",
                str(self.skills_root),
                "--phase23-dir",
                str(self.phase23_dir),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertEqual(payload["source_count"], 2)
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "live-source-helpscout.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "live-source-canon-helpscout.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "support-external-source-canon-2026.md").exists())
        self.assertTrue((self.phase23_dir / "support_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase23_dir / "support_external_sources_report.md").exists())

        support_router = (self.skills_root / "support-anemone" / "MEMORY.md").read_text(encoding="utf-8")
        support_operating = (self.skills_root / "support-anemone" / "memory" / "anemone-operating-canon-2026.md").read_text(
            encoding="utf-8"
        )
        report_text = (self.phase23_dir / "support_external_sources_report.md").read_text(encoding="utf-8")

        self.assertIn("support-external-source-canon-2026.md", support_router)
        self.assertIn("Phase 23 External Source Fusion", support_operating)
        self.assertIn("- Healthy sources: 2", report_text)
        self.assertIn("- Failed sources: 0", report_text)
        self.assertNotIn("Disabled Source", report_text)


if __name__ == "__main__":
    unittest.main()
