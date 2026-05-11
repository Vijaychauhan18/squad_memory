from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase11BootstrapWriterMarketingE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase11_dir = self.root / "ingest" / "phase11"
        self.db_path = self.root / "squad_memory.db"

        writer_root = self.skills_root / "writer"
        marketing_root = self.skills_root / "marketing"
        (writer_root / "memory").mkdir(parents=True, exist_ok=True)
        (marketing_root / "memory").mkdir(parents=True, exist_ok=True)

        (writer_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Writer Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Brief to draft: `memory/brief-to-draft.md`",
                    "- Hooks and structure: `memory/hooks-and-structure.md`",
                    "",
                    "## Plankton Bundle",
                    "- `memory/brief-to-draft.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/hooks-and-structure.md`",
                    "",
                    "## Current Bundle",
                    "- `memory/brief-to-draft.md`",
                    "",
                ]
            )
            + "\n"
        )
        (marketing_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Marketing Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Distribution system: `memory/distribution-system.md`",
                    "- Launch and follow-up: `memory/launch-and-followup.md`",
                    "",
                    "## Current Bundle",
                    "- `memory/distribution-system.md`",
                    "",
                    "## Charles Bundle",
                    "- `memory/launch-and-followup.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/distribution-system.md`",
                    "",
                ]
            )
            + "\n"
        )

        (writer_root / "memory" / "brief-to-draft.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Brief to Draft Workflow",
                    "topic: brief_to_draft",
                    "use_for: outline_from_brief, first_draft",
                    "---",
                    "",
                    "## Core Concept",
                    "Start from the brief, then outline before drafting.",
                    "",
                ]
            )
        )
        (writer_root / "memory" / "hooks-and-structure.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Hooks and Structure",
                    "topic: hooks_and_structure",
                    "use_for: stronger_hook, structural_editing",
                    "---",
                    "",
                    "## Core Concept",
                    "The first line must earn the second and the structure must carry the idea.",
                    "",
                ]
            )
        )
        (marketing_root / "memory" / "distribution-system.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Distribution System",
                    "topic: distribution_system",
                    "use_for: repurposing_plan, rollout",
                    "---",
                    "",
                    "## Core Concept",
                    "Promotion is part of the work, not an afterthought.",
                    "",
                ]
            )
        )
        (marketing_root / "memory" / "launch-and-followup.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Launch and Follow-up",
                    "topic: launch_followup",
                    "use_for: launch_sequence, traction_reporting",
                    "---",
                    "",
                    "## Core Concept",
                    "A launch needs sequenced follow-up instead of one post.",
                    "",
                ]
            )
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase11_bootstraps_writer_and_marketing_canon(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase11_bootstrap_writer_marketing.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase11-dir",
                str(self.phase11_dir),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(len(payload["domains"]), 2)
        self.assertTrue((self.phase11_dir / "writer_evidence_ledger.json").exists())
        self.assertTrue((self.phase11_dir / "marketing_evidence_ledger.json").exists())
        self.assertTrue((self.phase11_dir / "writer_marketing_bootstrap_report.md").exists())

        writer_canon = (self.skills_root / "writer" / "memory" / "writer-operating-canon-2026.md").read_text()
        self.assertIn("canonical: true", writer_canon)
        self.assertIn("Phase 11 Domain Fusion", writer_canon)
        self.assertIn("brief-to-draft.md", writer_canon)

        marketing_canon = (self.skills_root / "marketing" / "memory" / "marketing-operating-canon-2026.md").read_text()
        self.assertIn("canonical: true", marketing_canon)
        self.assertIn("distribution-system.md", marketing_canon)

        writer_router = (self.skills_root / "writer" / "MEMORY.md").read_text()
        self.assertIn("writer-operating-canon-2026.md", writer_router)
        self.assertIn("## Plankton Bundle", writer_router)

        marketing_router = (self.skills_root / "marketing" / "MEMORY.md").read_text()
        self.assertIn("marketing-operating-canon-2026.md", marketing_router)
        self.assertIn("## Current Bundle", marketing_router)


if __name__ == "__main__":
    unittest.main()
