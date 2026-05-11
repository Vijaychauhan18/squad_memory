from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_NAME = "squad_memory_phase36_test"
MODULE_SPEC = importlib.util.spec_from_file_location(MODULE_NAME, BASE / "squad_memory.py")
SQUAD_MEMORY = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
sys.modules[MODULE_NAME] = SQUAD_MEMORY
MODULE_SPEC.loader.exec_module(SQUAD_MEMORY)


class Phase36TaskEvalE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.db_path = self.root / "task_eval.db"
        self.packs_path = self.root / "task_packs.json"
        self.fixtures_path = self.root / "task_fixtures.json"

        (self.skills_root / "writer" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "support-anemone" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "seo" / "memory").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "writer" / "SKILL.md").write_text(
            "# Writer\n\nDraft articles and sharpen hooks.\n",
            encoding="utf-8",
        )
        (self.skills_root / "support-anemone" / "SKILL.md").write_text(
            "# Support Anemone\n\nHandle support triage and first-response flows.\n",
            encoding="utf-8",
        )
        (self.skills_root / "seo" / "SKILL.md").write_text(
            "# SEO\n\nSupport search-intent and structure checks.\n",
            encoding="utf-8",
        )
        (self.skills_root / "writer" / "memory" / "brief-to-draft.md").write_text(
            "---\n"
            "topic: brief_to_draft\n"
            "intent: content_writing\n"
            "role: plankton\n"
            "confidence: high\n"
            "canonical: true\n"
            "canonical_group: Brief To Draft\n"
            "---\n\n"
            "# Brief To Draft\n\n"
            "## Core Concept\n"
            "Turn a brief into an outline, hook, and structured first draft.\n",
            encoding="utf-8",
        )
        (self.skills_root / "writer" / "memory" / "hooks-and-structure.md").write_text(
            "---\n"
            "topic: hooks_and_structure\n"
            "intent: content_writing\n"
            "role: plankton\n"
            "confidence: high\n"
            "---\n\n"
            "# Hooks And Structure\n\n"
            "## Core Concept\n"
            "Open with a strong hook and keep the draft tightly structured.\n",
            encoding="utf-8",
        )
        (self.skills_root / "support-anemone" / "memory" / "fast-first-response.md").write_text(
            "---\n"
            "topic: support_triage\n"
            "intent: support_triage\n"
            "role: anemone\n"
            "confidence: high\n"
            "canonical: true\n"
            "canonical_group: Support Triage\n"
            "---\n\n"
            "# Fast First Response\n\n"
            "## Core Concept\n"
            "Send a fast first reply, classify severity, and escalate cleanly.\n",
            encoding="utf-8",
        )

        self.packs_path.write_text(
            json.dumps(
                {
                    "packs": [
                        {
                            "id": "article_draft",
                            "name": "Article Draft",
                            "description": "Draft from a brief.",
                            "roles": ["plankton"],
                            "intents": ["content_writing"],
                            "keywords": ["blog post", "article draft", "hook", "brief"],
                            "primary_skill": "writer",
                            "supporting_skills": ["seo"],
                            "memory_focus": ["brief_to_draft", "hooks_and_structure"],
                            "checklist": ["Outline first", "Draft with a strong hook"],
                            "deliverables": ["Working outline", "First full draft"],
                            "output_sections": ["Hook", "Draft", "Revision Notes", "Promotion Hooks"],
                            "handoffs": ["Writer owns the draft.", "SEO validates intent fit."],
                            "escalation_rules": ["Escalate if the brief is missing angle or audience."]
                        },
                        {
                            "id": "support_triage",
                            "name": "Support Triage",
                            "description": "First response and escalation flow.",
                            "roles": ["anemone"],
                            "intents": ["support_triage"],
                            "keywords": ["support", "triage", "severity", "first reply", "escalate"],
                            "primary_skill": "support-anemone",
                            "supporting_skills": [],
                            "memory_focus": ["support_triage", "severity", "response_templates"],
                            "checklist": ["Capture the issue", "Reply fast", "Escalate if severity is high"],
                            "deliverables": ["Severity classification", "First-response draft"],
                            "output_sections": ["Issue Summary", "Severity", "First Reply", "Escalation", "Follow-up"],
                            "handoffs": ["Anemone owns the response."],
                            "escalation_rules": ["Escalate immediately when severity is unclear."]
                        }
                    ]
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        self.fixtures_path.write_text(
            json.dumps(
                {
                    "cases": [
                        {
                            "query": "Need a blog post draft from a brief with a strong hook and clear structure",
                            "expected_pack_id": "article_draft",
                            "expected_primary_skill": "writer",
                            "expected_supporting_skills": ["seo"],
                            "expected_memory_paths": ["writer/memory/brief-to-draft.md"],
                            "expected_output_sections": ["Hook", "Draft", "Revision Notes", "Promotion Hooks"],
                            "expected_deliverables": ["Working outline", "First full draft"]
                        },
                        {
                            "query": "Need to triage a customer issue, reply fast, and escalate if severity is high",
                            "expected_pack_id": "support_triage",
                            "expected_primary_skill": "support-anemone",
                            "expected_memory_paths": ["support-anemone/memory/fast-first-response.md"],
                            "expected_output_sections": ["Issue Summary", "Severity", "First Reply", "Escalation", "Follow-up"],
                            "expected_deliverables": ["Severity classification", "First-response draft"]
                        }
                    ]
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        SQUAD_MEMORY.build_index(self.skills_root, self.db_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_task_eval_scores_pack_shape_and_memory_hits(self) -> None:
        result = SQUAD_MEMORY.evaluate_task_fixtures(
            self.db_path,
            self.packs_path,
            self.fixtures_path,
            top=5,
        )
        self.assertEqual(result["total_cases"], 2)
        self.assertEqual(result["pack_accuracy"], 1.0)
        self.assertEqual(result["primary_skill_accuracy"], 1.0)
        self.assertEqual(result["memory_path_hit_rate"], 1.0)
        self.assertEqual(result["output_section_hit_rate"], 1.0)
        self.assertEqual(result["deliverable_hit_rate"], 1.0)
        self.assertEqual(result["pass_rate"], 1.0)
        self.assertFalse(result["weak_cases"])


if __name__ == "__main__":
    unittest.main()
