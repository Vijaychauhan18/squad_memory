from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
FIXTURES = BASE / "tests" / "fixtures" / "feeds"


class PhasePipelineRunnerE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.memories_dir = self.root / "memories"
        self.memory_dir = self.skills_root / "seo" / "memory"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.memories_dir.mkdir(parents=True, exist_ok=True)
        (self.skills_root / "seo" / "SKILL.md").write_text("# SEO\n")
        (self.skills_root / "writer" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "marketing" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "charles").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "support-anemone").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "developer").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "qa").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "SQUAD_MEMORY.md").write_text(
            "\n".join(
                [
                    "# Squad Memory Router",
                    "",
                    "## Role Bundles",
                    "",
                    "### Pinchy Bundle",
                    "- `writer/MEMORY.md`",
                    "- `marketing/MEMORY.md`",
                    "",
                    "### Plankton Bundle",
                    "- `writer/MEMORY.md`",
                    "",
                    "### Charles Bundle",
                    "- `marketing/MEMORY.md`",
                    "",
                    "### Current Bundle",
                    "- `marketing/MEMORY.md`",
                    "",
                ]
            )
            + "\n"
        )
        (self.skills_root / "seo" / "MEMORY.md").write_text(
            "# SEO Memory Router\n\n## Routing Guide\n- Existing routing text\n\n## Default Memory Bundles\n- Existing bundle text\n\n## Output Rule\n- Existing output rule\n"
        )
        (self.skills_root / "writer" / "MEMORY.md").write_text(
            "# Writer Memory Router\n\n## Canonical Notes\n- Brief to draft: `memory/brief-to-draft.md`\n\n## Plankton Bundle\n- `memory/brief-to-draft.md`\n\n## Pinchy Bundle\n- `memory/brief-to-draft.md`\n\n## Current Bundle\n- `memory/brief-to-draft.md`\n"
        )
        (self.skills_root / "marketing" / "MEMORY.md").write_text(
            "# Marketing Memory Router\n\n## Canonical Notes\n- Distribution system: `memory/distribution-system.md`\n\n## Current Bundle\n- `memory/distribution-system.md`\n\n## Charles Bundle\n- `memory/distribution-system.md`\n\n## Pinchy Bundle\n- `memory/distribution-system.md`\n"
        )
        (self.skills_root / "support-anemone" / "MEMORY.md").write_text(
            "# MEMORY.md — Customer Support\n\n## FAQ\n| Question | Answer | Last Updated |\n|----------|--------|-------------|\n| — | — | — |\n"
        )
        (self.memory_dir / "INDEX.md").write_text(
            "# Coral's SEO Knowledge Base — INDEX\n\n## Source Canon & Monitoring\n- Existing source canon\n\n## AI Search & Visibility\n- Existing AI visibility note\n"
        )
        (self.skills_root / "writer" / "memory" / "brief-to-draft.md").write_text(
            "---\ntitle: Brief to Draft Workflow\ntopic: brief_to_draft\nuse_for: outline_from_brief\n---\n\n## Core Concept\nStart from the brief.\n"
        )
        (self.skills_root / "marketing" / "memory" / "distribution-system.md").write_text(
            "---\ntitle: Distribution System\ntopic: distribution_system\nuse_for: rollout\n---\n\n## Core Concept\nPromotion is part of the work.\n"
        )

        self.config_path = self.root / "knowledge_sources.json"
        self.summary_path = self.memory_dir / "live-knowledge-monitor.md"
        self.snapshot_dir = self.root / "ingest" / "raw"
        self.runs_dir = self.root / "ingest" / "runs"
        self.state_path = self.root / "ingest" / "state.json"
        self.phase2_dir = self.root / "ingest" / "phase2"
        self.phase3_dir = self.root / "ingest" / "phase3"
        self.phase5_dir = self.root / "ingest" / "phase5"
        self.phase6_dir = self.root / "ingest" / "phase6"
        self.phase7_dir = self.root / "ingest" / "phase7"
        self.phase8_dir = self.root / "ingest" / "phase8"
        self.phase9_dir = self.root / "ingest" / "phase9"
        self.phase10_dir = self.root / "ingest" / "phase10"
        self.phase11_dir = self.root / "ingest" / "phase11"
        self.phase12_dir = self.root / "ingest" / "phase12"
        self.phase13_dir = self.root / "ingest" / "phase13"
        self.phase14_dir = self.root / "ingest" / "phase14"
        self.phase15_dir = self.root / "ingest" / "phase15"
        self.phase16_dir = self.root / "ingest" / "phase16"
        self.phase17_dir = self.root / "ingest" / "phase17"
        self.phase18_dir = self.root / "ingest" / "phase18"
        self.phase19_dir = self.root / "ingest" / "phase19"
        self.phase20_dir = self.root / "ingest" / "phase20"
        self.phase21_dir = self.root / "ingest" / "phase21"
        self.phase22_dir = self.root / "ingest" / "phase22"
        self.phase23_dir = self.root / "ingest" / "phase23"
        self.phase24_dir = self.root / "ingest" / "phase24"
        self.phase25_dir = self.root / "ingest" / "phase25"
        self.phase26_dir = self.root / "ingest" / "phase26"
        self.phase27_dir = self.root / "ingest" / "phase27"
        self.phase28_dir = self.root / "ingest" / "phase28"
        self.phase29_dir = self.root / "ingest" / "phase29"
        self.phase30_dir = self.root / "ingest" / "phase30"
        self.phase31_dir = self.root / "ingest" / "phase31"
        self.phase12_config = self.root / "knowledge_sources_writer_marketing.json"
        self.phase17_config = self.root / "knowledge_sources_charles.json"
        self.phase23_config = self.root / "knowledge_sources_support.json"
        self.phase25_config = self.root / "knowledge_sources_dev_qa.json"
        self.phase12_feed_dir = self.root / "phase12_feeds"
        self.phase17_feed_dir = self.root / "phase17_feeds"
        self.phase23_feed_dir = self.root / "phase23_feeds"
        self.phase25_feed_dir = self.root / "phase25_feeds"
        self.db_path = self.root / "squad_memory.db"
        self.fixtures_path = self.root / "fixtures.json"
        self.lock_path = self.root / "locks" / "phase_pipeline.lock"

        self.config_path.write_text(json.dumps(self._fixture_config(), indent=2))
        self.fixtures_path.write_text(json.dumps(self._fixture_evals(), indent=2))
        self.phase12_feed_dir.mkdir(parents=True, exist_ok=True)
        self.phase17_feed_dir.mkdir(parents=True, exist_ok=True)
        self.phase23_feed_dir.mkdir(parents=True, exist_ok=True)
        self.phase25_feed_dir.mkdir(parents=True, exist_ok=True)
        self._write_phase12_config()
        self._write_phase17_config()
        self._write_phase23_config()
        self._write_phase25_config()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _fixture_config(self) -> dict:
        return {
            "name": "Fixture Knowledge Source Monitor",
            "sources": [
                {
                    "slug": "ahrefs",
                    "name": "Ahrefs Blog",
                    "homepage": "https://ahrefs.com/blog/",
                    "kind": "publication",
                    "strength": "data studies and AI visibility",
                    "topic": "seo_research",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring", "ai_visibility"],
                    "tags": ["ahrefs", "fixture"],
                    "feed_urls": [(FIXTURES / "ahrefs.xml").as_uri()],
                },
                {
                    "slug": "dejan",
                    "name": "DEJAN / Dan Petrovic",
                    "homepage": "https://dejan.ai/blog/",
                    "kind": "practitioner",
                    "strength": "reverse engineering",
                    "topic": "ai_reverse_engineering",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring", "ai_selection"],
                    "tags": ["dejan", "fixture"],
                    "feed_urls": [(FIXTURES / "dejan.xml").as_uri()],
                },
            ],
        }

    def _fixture_evals(self) -> dict:
        return {
            "cases": [
                {
                    "query": "Need AI visibility monitoring and citation updates from Ahrefs",
                    "expected_primary_skill": "seo",
                    "expected_skills": ["seo"],
                    "expected_paths": ["seo/memory/live-source-canon-ahrefs.md"],
                },
                {
                    "query": "Need reverse engineering monitoring for grounding snippets and selection rate",
                    "expected_primary_skill": "seo",
                    "expected_skills": ["seo"],
                    "expected_paths": ["seo/memory/live-source-canon-dejan.md"],
                },
            ]
        }

    def _rss_feed(self, title: str, item_title: str, item_link: str, published: str, description: str) -> str:
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

    def _write_phase12_config(self) -> None:
        writer_feed = self.phase12_feed_dir / "copyblogger.xml"
        writer_feed.write_text(
            self._rss_feed(
                "Copyblogger",
                "How to write a sharper lead",
                "https://example.com/copyblogger-lead",
                "Thu, 19 Mar 2026 10:00:00 +0000",
                "Lead and hook guidance.",
            )
        )
        marketing_feed = self.phase12_feed_dir / "buffer.xml"
        marketing_feed.write_text(
            self._rss_feed(
                "Buffer",
                "A better social distribution system",
                "https://example.com/buffer-system",
                "Wed, 18 Mar 2026 09:00:00 +0000",
                "Distribution workflow update.",
            )
        )
        self.phase12_config.write_text(
            json.dumps(
                {
                    "name": "Phase 12 Fixture",
                    "sources": [
                        {
                            "domain": "writer",
                            "slug": "copyblogger",
                            "name": "Copyblogger",
                            "homepage": "https://copyblogger.com/",
                            "kind": "publication",
                            "strength": "copywriting systems",
                            "topic": "copywriting_systems",
                            "confidence": "high",
                            "roles": ["writer", "pinchy"],
                            "intent": ["research", "monitoring", "writing_examples"],
                            "tags": ["copyblogger", "fixture"],
                            "feed_urls": [writer_feed.as_uri()],
                        },
                        {
                            "domain": "marketing",
                            "slug": "buffer",
                            "name": "Buffer",
                            "homepage": "https://buffer.com/resources/",
                            "kind": "publication",
                            "strength": "distribution systems",
                            "topic": "social_distribution",
                            "confidence": "high",
                            "roles": ["marketing", "charles", "pinchy"],
                            "intent": ["research", "monitoring", "distribution_examples"],
                            "tags": ["buffer", "fixture"],
                            "feed_urls": [marketing_feed.as_uri()],
                        },
                    ],
                },
                indent=2,
            )
        )

    def _write_phase17_config(self) -> None:
        buffer_feed = self.phase17_feed_dir / "buffer.xml"
        buffer_feed.write_text(
            self._rss_feed(
                "Buffer",
                "A better creator posting workflow",
                "https://example.com/buffer-creator",
                "Thu, 19 Mar 2026 08:00:00 +0000",
                "Creator workflow update.",
            )
        )
        hootsuite_feed = self.phase17_feed_dir / "hootsuite.xml"
        hootsuite_feed.write_text(
            self._rss_feed(
                "Hootsuite",
                "LinkedIn changes creators should track",
                "https://example.com/hootsuite-linkedin",
                "Wed, 18 Mar 2026 07:00:00 +0000",
                "Platform update summary.",
            )
        )
        self.phase17_config.write_text(
            json.dumps(
                {
                    "name": "Phase 17 Fixture",
                    "sources": [
                        {
                            "slug": "buffer",
                            "name": "Buffer",
                            "homepage": "https://buffer.com/resources/",
                            "kind": "publication",
                            "strength": "creator workflows and social distribution",
                            "topic": "social_distribution",
                            "confidence": "high",
                            "roles": ["charles", "current", "pinchy"],
                            "intent": ["research", "monitoring", "creator_examples"],
                            "tags": ["buffer", "fixture"],
                            "feed_urls": [buffer_feed.as_uri()],
                        },
                        {
                            "slug": "hootsuite",
                            "name": "Hootsuite",
                            "homepage": "https://blog.hootsuite.com/",
                            "kind": "publication",
                            "strength": "platform changes and channel tactics",
                            "topic": "platform_changes",
                            "confidence": "high",
                            "roles": ["charles", "current", "pinchy"],
                            "intent": ["research", "monitoring", "platform_changes"],
                            "tags": ["hootsuite", "fixture"],
                            "feed_urls": [hootsuite_feed.as_uri()],
                        },
                    ],
                },
                indent=2,
            )
        )

    def _write_phase23_config(self) -> None:
        helpscout_feed = self.phase23_feed_dir / "helpscout.xml"
        helpscout_feed.write_text(
            self._rss_feed(
                "Help Scout",
                "How to tighten support handoffs",
                "https://example.com/helpscout-handoff",
                "Thu, 19 Mar 2026 06:00:00 +0000",
                "Support handoff and documentation guidance.",
            )
        )
        intercom_feed = self.phase23_feed_dir / "intercom.xml"
        intercom_feed.write_text(
            self._rss_feed(
                "Intercom",
                "A better AI-assisted support workflow",
                "https://example.com/intercom-workflow",
                "Wed, 18 Mar 2026 05:00:00 +0000",
                "Support operations workflow update.",
            )
        )
        self.phase23_config.write_text(
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
                    ],
                },
                indent=2,
            )
        )

    def _write_phase25_config(self) -> None:
        developer_feed = self.phase25_feed_dir / "martin-fowler.xml"
        developer_feed.write_text(
            self._rss_feed(
                "Martin Fowler",
                "How to keep refactors small",
                "https://example.com/mf-refactor",
                "Thu, 19 Mar 2026 04:00:00 +0000",
                "Engineering decision and refactoring guidance.",
            )
        )
        qa_feed = self.phase25_feed_dir / "playwright.xml"
        qa_feed.write_text(
            self._rss_feed(
                "Playwright Releases",
                "Playwright 1.55 release notes",
                "https://example.com/playwright-release",
                "Wed, 18 Mar 2026 03:00:00 +0000",
                "Testing framework release summary.",
            )
        )
        self.phase25_config.write_text(
            json.dumps(
                {
                    "name": "Phase 25 Fixture",
                    "sources": [
                        {
                            "domain": "developer",
                            "slug": "martin-fowler",
                            "name": "Martin Fowler",
                            "homepage": "https://martinfowler.com/",
                            "kind": "practitioner",
                            "strength": "software design and refactoring guidance",
                            "topic": "engineering_patterns",
                            "confidence": "high",
                            "roles": ["developer", "reviewer", "pinchy"],
                            "intent": ["research", "monitoring", "engineering_examples"],
                            "tags": ["martin-fowler", "fixture"],
                            "feed_urls": [developer_feed.as_uri()],
                        },
                        {
                            "domain": "qa",
                            "slug": "playwright-releases",
                            "name": "Playwright Releases",
                            "homepage": "https://github.com/microsoft/playwright/releases",
                            "kind": "release_notes",
                            "strength": "testing framework release updates",
                            "topic": "test_tooling",
                            "confidence": "high",
                            "roles": ["qa", "developer", "pinchy"],
                            "intent": ["research", "monitoring", "tooling_changes"],
                            "tags": ["playwright", "fixture"],
                            "feed_urls": [qa_feed.as_uri()],
                        },
                    ],
                },
                indent=2,
            )
        )

    def test_pipeline_runner_end_to_end(self) -> None:
        cmd = [
            sys.executable,
            str(BASE / "phase_pipeline.py"),
            "--config",
            str(self.config_path),
            "--output-dir",
            str(self.memory_dir),
            "--summary-path",
            str(self.summary_path),
            "--snapshot-dir",
            str(self.snapshot_dir),
            "--runs-dir",
            str(self.runs_dir),
            "--state-path",
            str(self.state_path),
            "--phase2-dir",
            str(self.phase2_dir),
            "--phase3-dir",
            str(self.phase3_dir),
            "--phase5-dir",
            str(self.phase5_dir),
            "--phase6-dir",
            str(self.phase6_dir),
            "--phase7-dir",
            str(self.phase7_dir),
            "--phase8-dir",
            str(self.phase8_dir),
            "--phase9-dir",
            str(self.phase9_dir),
            "--phase10-dir",
            str(self.phase10_dir),
            "--phase11-dir",
            str(self.phase11_dir),
            "--phase12-dir",
            str(self.phase12_dir),
            "--phase13-dir",
            str(self.phase13_dir),
            "--phase14-dir",
            str(self.phase14_dir),
            "--phase15-dir",
            str(self.phase15_dir),
            "--phase16-dir",
            str(self.phase16_dir),
            "--phase17-dir",
            str(self.phase17_dir),
            "--phase18-dir",
            str(self.phase18_dir),
            "--phase19-dir",
            str(self.phase19_dir),
            "--phase20-dir",
            str(self.phase20_dir),
            "--phase21-dir",
            str(self.phase21_dir),
            "--phase22-dir",
            str(self.phase22_dir),
            "--phase23-dir",
            str(self.phase23_dir),
            "--phase24-dir",
            str(self.phase24_dir),
            "--phase25-dir",
            str(self.phase25_dir),
            "--phase26-dir",
            str(self.phase26_dir),
            "--phase27-dir",
            str(self.phase27_dir),
            "--phase28-dir",
            str(self.phase28_dir),
            "--phase29-dir",
            str(self.phase29_dir),
            "--phase30-dir",
            str(self.phase30_dir),
            "--phase31-dir",
            str(self.phase31_dir),
            "--phase12-config",
            str(self.phase12_config),
            "--phase17-config",
            str(self.phase17_config),
            "--phase23-config",
            str(self.phase23_config),
            "--phase25-config",
            str(self.phase25_config),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--fixtures",
            str(self.fixtures_path),
            "--memory-router",
            str(self.skills_root / "seo" / "MEMORY.md"),
            "--index-path",
            str(self.memory_dir / "INDEX.md"),
            "--lock-path",
            str(self.lock_path),
            "--json",
        ]
        completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
        payload = json.loads(completed.stdout)

        self.assertEqual(payload["status"], "ok")
        self.assertEqual([phase["returncode"] for phase in payload["phases"]], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertTrue((self.memory_dir / "live-source-canon-ahrefs.md").exists())
        self.assertTrue((self.memory_dir / "live-source-cluster-report.md").exists())
        self.assertTrue((self.phase5_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase6_dir / "decisions.json").exists())
        self.assertTrue((self.phase6_dir / "review-status.md").exists())
        self.assertTrue((self.phase7_dir / "canonical_registry.json").exists())
        self.assertTrue((self.phase7_dir / "memory_health_report.md").exists())
        self.assertTrue((self.phase8_dir / "canonical_promotion_report.md").exists())
        self.assertTrue((self.phase9_dir / "canonical_summary_merge_report.md").exists())
        self.assertTrue((self.phase10_dir / "evidence_ledger.json").exists())
        self.assertTrue((self.phase10_dir / "evidence_fusion_report.md").exists())
        self.assertTrue((self.phase11_dir / "writer_evidence_ledger.json").exists())
        self.assertTrue((self.phase11_dir / "marketing_evidence_ledger.json").exists())
        self.assertTrue((self.phase11_dir / "writer_marketing_bootstrap_report.md").exists())
        self.assertTrue((self.phase12_dir / "writer_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase12_dir / "marketing_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase12_dir / "writer_marketing_external_sources_report.md").exists())
        self.assertTrue((self.phase13_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase13_dir / "latest.json").exists())
        self.assertTrue((self.phase14_dir / "decisions.json").exists())
        self.assertTrue((self.phase14_dir / "review-status.md").exists())
        self.assertTrue((self.phase15_dir / "outcome_telemetry_ledger.json").exists())
        self.assertTrue((self.phase15_dir / "outcome_telemetry_report.md").exists())
        self.assertTrue((self.phase16_dir / "charles_evidence_ledger.json").exists())
        self.assertTrue((self.phase16_dir / "charles_bootstrap_report.md").exists())
        self.assertTrue((self.phase17_dir / "charles_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase17_dir / "charles_external_sources_report.md").exists())
        self.assertTrue((self.phase18_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase18_dir / "latest.json").exists())
        self.assertTrue((self.phase19_dir / "decisions.json").exists())
        self.assertTrue((self.phase19_dir / "review-status.md").exists())
        self.assertTrue((self.phase20_dir / "triage.json").exists())
        self.assertTrue((self.phase20_dir / "triage-report.md").exists())
        self.assertTrue((self.phase21_dir / "control_plane_status.json").exists())
        self.assertTrue((self.phase21_dir / "control_plane_report.md").exists())
        self.assertTrue((self.phase21_dir / "latest.json").exists())
        self.assertTrue((self.phase22_dir / "support_evidence_ledger.json").exists())
        self.assertTrue((self.phase22_dir / "support_bootstrap_report.md").exists())
        self.assertTrue((self.phase22_dir / "latest.json").exists())
        self.assertTrue((self.phase23_dir / "support_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase23_dir / "support_external_sources_report.md").exists())
        self.assertTrue((self.phase23_dir / "latest.json").exists())
        self.assertTrue((self.phase24_dir / "developer_evidence_ledger.json").exists())
        self.assertTrue((self.phase24_dir / "qa_evidence_ledger.json").exists())
        self.assertTrue((self.phase24_dir / "developer_qa_bootstrap_report.md").exists())
        self.assertTrue((self.phase24_dir / "latest.json").exists())
        self.assertTrue((self.phase25_dir / "developer_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase25_dir / "qa_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase25_dir / "developer_qa_external_sources_report.md").exists())
        self.assertTrue((self.phase25_dir / "latest.json").exists())
        self.assertTrue((self.phase26_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase26_dir / "latest.json").exists())
        self.assertTrue((self.phase27_dir / "decisions.json").exists())
        self.assertTrue((self.phase27_dir / "review-status.md").exists())
        self.assertTrue((self.phase27_dir / "latest.json").exists())
        self.assertTrue((self.phase28_dir / "triage.json").exists())
        self.assertTrue((self.phase28_dir / "triage-report.md").exists())
        self.assertTrue((self.phase28_dir / "latest.json").exists())
        self.assertTrue((self.phase29_dir / "task_result_eval_ledger.json").exists())
        self.assertTrue((self.phase29_dir / "task_result_eval_report.md").exists())
        self.assertTrue((self.phase29_dir / "scorecard_review_queue.md").exists())
        self.assertTrue((self.phase29_dir / "latest.json").exists())
        self.assertTrue((self.phase30_dir / "scorecard_learning_ledger.json").exists())
        self.assertTrue((self.phase30_dir / "scorecard_learning_report.md").exists())
        self.assertTrue((self.phase30_dir / "latest.json").exists())
        self.assertTrue((self.phase31_dir / "memory_graph.json").exists())
        self.assertTrue((self.phase31_dir / "memory_graph_report.md").exists())
        self.assertTrue((self.phase31_dir / "latest.json").exists())
        self.assertTrue((self.skills_root / "writer" / "memory" / "writer-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "marketing" / "memory" / "marketing-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "charles" / "memory" / "charles-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "charles" / "MEMORY.md").exists())
        self.assertTrue((self.skills_root / "charles" / "memory" / "charles-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "anemone-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "MEMORY.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "support-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "developer" / "memory" / "developer-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "developer" / "MEMORY.md").exists())
        self.assertTrue((self.skills_root / "developer" / "memory" / "developer-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "qa-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "qa" / "MEMORY.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "qa-external-source-canon-2026.md").exists())

        memory_text = (self.skills_root / "seo" / "MEMORY.md").read_text()
        index_text = (self.memory_dir / "INDEX.md").read_text()
        squad_router_text = (self.skills_root / "SQUAD_MEMORY.md").read_text()
        charles_operating_text = (self.skills_root / "charles" / "memory" / "charles-operating-canon-2026.md").read_text()
        support_operating_text = (self.skills_root / "support-anemone" / "memory" / "anemone-operating-canon-2026.md").read_text()
        developer_router_text = (self.skills_root / "developer" / "MEMORY.md").read_text()
        qa_router_text = (self.skills_root / "qa" / "MEMORY.md").read_text()
        self.assertIn("BEGIN AUTO LIVE SOURCE CANON", memory_text)
        self.assertIn("BEGIN AUTO LIVE SOURCE PIPELINE", index_text)
        self.assertNotIn("BEGIN AUTO PROMOTED DRAFTS", memory_text)
        self.assertEqual(list(self.memory_dir.glob("live-source-canon-canon*.md")), [])
        self.assertIn("charles/MEMORY.md", squad_router_text)
        self.assertIn("support-anemone/MEMORY.md", squad_router_text)
        self.assertIn("developer/MEMORY.md", squad_router_text)
        self.assertIn("qa/MEMORY.md", squad_router_text)
        self.assertIn("Phase 17 External Source Fusion", charles_operating_text)
        self.assertIn("Phase 23 External Source Fusion", support_operating_text)
        self.assertIn("Developer Operating Canon 2026", developer_router_text)
        self.assertIn("QA Operating Canon 2026", qa_router_text)

    def test_pipeline_runner_with_openclaw_sync(self) -> None:
        dejan_root = self.skills_root / "dejan-ai-reverse-engineering"
        (dejan_root / "references").mkdir(parents=True, exist_ok=True)
        (dejan_root / "SKILL.md").write_text("# DEJAN\n")
        (dejan_root / "references" / "notes.md").write_text("# Notes\n")
        (self.memories_dir / "dejan-ai-reverse-engineering-2026-03-20.md").write_text("# Durable\n")
        self.fixtures_path.write_text(
            json.dumps(
                {
                    "cases": [
                        {
                            "query": "Need AI visibility monitoring and citation updates from Ahrefs",
                            "expected_primary_skill": "seo",
                            "expected_skills": ["seo"],
                            "expected_paths": ["seo/memory/live-source-canon-ahrefs.md"],
                        },
                        {
                            "query": "Need reverse engineering monitoring for grounding snippets and selection rate",
                            "expected_primary_skill": "dejan-ai-reverse-engineering",
                            "expected_skills": ["dejan-ai-reverse-engineering"],
                            "expected_paths": ["seo/memory/live-source-canon-dejan.md"],
                        },
                    ]
                },
                indent=2,
            )
        )

        openclaw_root = self.root / "openclaw"
        cmd = [
            sys.executable,
            str(BASE / "phase_pipeline.py"),
            "--config",
            str(self.config_path),
            "--output-dir",
            str(self.memory_dir),
            "--summary-path",
            str(self.summary_path),
            "--snapshot-dir",
            str(self.snapshot_dir),
            "--runs-dir",
            str(self.runs_dir),
            "--state-path",
            str(self.state_path),
            "--phase2-dir",
            str(self.phase2_dir),
            "--phase3-dir",
            str(self.phase3_dir),
            "--phase5-dir",
            str(self.phase5_dir),
            "--phase6-dir",
            str(self.phase6_dir),
            "--phase7-dir",
            str(self.phase7_dir),
            "--phase8-dir",
            str(self.phase8_dir),
            "--phase9-dir",
            str(self.phase9_dir),
            "--phase10-dir",
            str(self.phase10_dir),
            "--phase11-dir",
            str(self.phase11_dir),
            "--phase12-dir",
            str(self.phase12_dir),
            "--phase13-dir",
            str(self.phase13_dir),
            "--phase14-dir",
            str(self.phase14_dir),
            "--phase15-dir",
            str(self.phase15_dir),
            "--phase16-dir",
            str(self.phase16_dir),
            "--phase17-dir",
            str(self.phase17_dir),
            "--phase18-dir",
            str(self.phase18_dir),
            "--phase19-dir",
            str(self.phase19_dir),
            "--phase20-dir",
            str(self.phase20_dir),
            "--phase21-dir",
            str(self.phase21_dir),
            "--phase22-dir",
            str(self.phase22_dir),
            "--phase23-dir",
            str(self.phase23_dir),
            "--phase24-dir",
            str(self.phase24_dir),
            "--phase25-dir",
            str(self.phase25_dir),
            "--phase26-dir",
            str(self.phase26_dir),
            "--phase27-dir",
            str(self.phase27_dir),
            "--phase28-dir",
            str(self.phase28_dir),
            "--phase29-dir",
            str(self.phase29_dir),
            "--phase30-dir",
            str(self.phase30_dir),
            "--phase31-dir",
            str(self.phase31_dir),
            "--phase12-config",
            str(self.phase12_config),
            "--phase17-config",
            str(self.phase17_config),
            "--phase23-config",
            str(self.phase23_config),
            "--phase25-config",
            str(self.phase25_config),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--fixtures",
            str(self.fixtures_path),
            "--memory-router",
            str(self.skills_root / "seo" / "MEMORY.md"),
            "--index-path",
            str(self.memory_dir / "INDEX.md"),
            "--lock-path",
            str(self.lock_path),
            "--openclaw-sync",
            "--openclaw-root",
            str(openclaw_root),
            "--json",
        ]
        completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
        payload = json.loads(completed.stdout)

        self.assertEqual(payload["status"], "ok")
        self.assertEqual([phase["returncode"] for phase in payload["phases"]], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(payload["phases"][-1]["name"], "openclaw_sync")

        import_root = openclaw_root / "workspace" / "memory" / "imports" / "codex"
        self.assertTrue((openclaw_root / "workspace" / "MEMORY.md").exists())
        self.assertTrue((import_root / "IMPORT_INDEX.md").exists())
        self.assertTrue((import_root / "seo-memory" / "live-source-canon-ahrefs.md").exists())
        self.assertTrue((import_root / "dejan-pack" / "SKILL.md").exists())
        self.assertTrue((self.phase7_dir / "canonical_registry.json").exists())
        self.assertTrue((self.phase8_dir / "canonical_promotion_report.md").exists())
        self.assertTrue((self.phase9_dir / "canonical_summary_merge_report.md").exists())
        self.assertTrue((self.phase10_dir / "evidence_ledger.json").exists())
        self.assertTrue((self.phase10_dir / "evidence_fusion_report.md").exists())
        self.assertTrue((self.phase11_dir / "writer_evidence_ledger.json").exists())
        self.assertTrue((self.phase11_dir / "marketing_evidence_ledger.json").exists())
        self.assertTrue((self.phase11_dir / "writer_marketing_bootstrap_report.md").exists())
        self.assertTrue((self.phase12_dir / "writer_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase12_dir / "marketing_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase12_dir / "writer_marketing_external_sources_report.md").exists())
        self.assertTrue((self.phase13_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase14_dir / "decisions.json").exists())
        self.assertTrue((self.phase14_dir / "review-status.md").exists())
        self.assertTrue((self.phase15_dir / "outcome_telemetry_ledger.json").exists())
        self.assertTrue((self.phase15_dir / "outcome_telemetry_report.md").exists())
        self.assertTrue((self.phase16_dir / "charles_evidence_ledger.json").exists())
        self.assertTrue((self.phase16_dir / "charles_bootstrap_report.md").exists())
        self.assertTrue((self.phase17_dir / "charles_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase17_dir / "charles_external_sources_report.md").exists())
        self.assertTrue((self.phase18_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase18_dir / "latest.json").exists())
        self.assertTrue((self.phase19_dir / "decisions.json").exists())
        self.assertTrue((self.phase19_dir / "review-status.md").exists())
        self.assertTrue((self.phase20_dir / "triage.json").exists())
        self.assertTrue((self.phase20_dir / "triage-report.md").exists())
        self.assertTrue((self.phase21_dir / "control_plane_status.json").exists())
        self.assertTrue((self.phase21_dir / "control_plane_report.md").exists())
        self.assertTrue((self.phase21_dir / "latest.json").exists())
        self.assertTrue((self.phase22_dir / "support_evidence_ledger.json").exists())
        self.assertTrue((self.phase22_dir / "support_bootstrap_report.md").exists())
        self.assertTrue((self.phase22_dir / "latest.json").exists())
        self.assertTrue((self.phase23_dir / "support_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase23_dir / "support_external_sources_report.md").exists())
        self.assertTrue((self.phase23_dir / "latest.json").exists())
        self.assertTrue((self.phase24_dir / "developer_evidence_ledger.json").exists())
        self.assertTrue((self.phase24_dir / "qa_evidence_ledger.json").exists())
        self.assertTrue((self.phase24_dir / "developer_qa_bootstrap_report.md").exists())
        self.assertTrue((self.phase24_dir / "latest.json").exists())
        self.assertTrue((self.phase25_dir / "developer_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase25_dir / "qa_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase25_dir / "developer_qa_external_sources_report.md").exists())
        self.assertTrue((self.phase25_dir / "latest.json").exists())
        self.assertTrue((self.phase26_dir / "promotion-queue.md").exists())
        self.assertTrue((self.phase26_dir / "latest.json").exists())
        self.assertTrue((self.phase27_dir / "decisions.json").exists())
        self.assertTrue((self.phase27_dir / "review-status.md").exists())
        self.assertTrue((self.phase27_dir / "latest.json").exists())
        self.assertTrue((self.phase28_dir / "triage.json").exists())
        self.assertTrue((self.phase28_dir / "triage-report.md").exists())
        self.assertTrue((self.phase28_dir / "latest.json").exists())
        self.assertTrue((self.phase29_dir / "task_result_eval_ledger.json").exists())
        self.assertTrue((self.phase29_dir / "task_result_eval_report.md").exists())
        self.assertTrue((self.phase29_dir / "scorecard_review_queue.md").exists())
        self.assertTrue((self.phase29_dir / "latest.json").exists())
        self.assertTrue((self.phase30_dir / "scorecard_learning_ledger.json").exists())
        self.assertTrue((self.phase30_dir / "scorecard_learning_report.md").exists())
        self.assertTrue((self.phase30_dir / "latest.json").exists())
        self.assertTrue((self.phase31_dir / "memory_graph.json").exists())
        self.assertTrue((self.phase31_dir / "memory_graph_report.md").exists())
        self.assertTrue((self.phase31_dir / "latest.json").exists())
        self.assertTrue((self.skills_root / "charles" / "memory" / "charles-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "charles" / "memory" / "charles-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "anemone-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "support-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "developer" / "memory" / "developer-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "developer" / "memory" / "developer-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "qa-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "qa-external-source-canon-2026.md").exists())

        with sqlite3.connect(openclaw_root / "memory" / "main.sqlite") as conn:
            main_files = conn.execute("select count(*) from files").fetchone()[0]
            main_chunks = conn.execute("select count(*) from chunks").fetchone()[0]
        with sqlite3.connect(openclaw_root / "memory" / "seo.sqlite") as conn:
            seo_files = conn.execute("select count(*) from files").fetchone()[0]
            seo_chunks = conn.execute("select count(*) from chunks").fetchone()[0]

        self.assertGreater(main_files, 0)
        self.assertGreater(main_chunks, 0)
        self.assertGreater(seo_files, 0)
        self.assertGreater(seo_chunks, 0)


if __name__ == "__main__":
    unittest.main()
