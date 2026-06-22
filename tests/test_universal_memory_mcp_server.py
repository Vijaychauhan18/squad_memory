from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MCP_BASE = BASE / "mcp"
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))
if str(MCP_BASE) not in sys.path:
    sys.path.insert(0, str(MCP_BASE))

import dataset_registry
from universal_memory_mcp_server import SquadMemoryOsMcpServer


class UniversalMemoryMcpServerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.registry_path = self.root / "dataset_registry.json"
        self.db_path = self.root / "demo.db"
        self.history_path = self.root / "history.jsonl"
        self.task_packs_path = self.root / "task_packs.json"
        self.skills_root = self.root / "skills"
        self.skills_root.mkdir(parents=True, exist_ok=True)
        self.task_packs_path.write_text(json.dumps({"packs": []}, indent=2), encoding="utf-8")
        self._seed_db()
        self._seed_history()
        self.registry_path.write_text(
            json.dumps(
                {
                    "datasets": [
                        {
                            "id": "demo",
                            "label": "Demo DB",
                            "db_path": str(self.db_path),
                            "query_adapter": "counts_only",
                            "purpose": "Temporary dataset for MCP tests.",
                            "owner": "Tests",
                            "update_source": "Fixtures",
                            "history_path": str(self.history_path),
                            "dashboard_urls": [],
                            "relations": [],
                        }
                    ]
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        self.original_registry_path = dataset_registry.REGISTRY_PATH
        dataset_registry.REGISTRY_PATH = self.registry_path

    def tearDown(self) -> None:
        dataset_registry.REGISTRY_PATH = self.original_registry_path
        self.temp_dir.cleanup()

    def _seed_db(self) -> None:
        with sqlite3.connect(self.db_path) as con:
            con.execute("CREATE TABLE chunks (path TEXT)")
            rows = [
                ("notes/a.md",),
                ("notes/a.md",),
                ("notes/b.md",),
                ("notes/b.md",),
                ("notes/c.md",),
                ("notes/c.md",),
                ("notes/c.md",),
                ("notes/c.md",),
                ("notes/d.md",),
                ("notes/d.md",),
                ("notes/d.md",),
                ("notes/d.md",),
            ]
            con.executemany("INSERT INTO chunks(path) VALUES (?)", rows)
            con.commit()

    def _seed_history(self) -> None:
        entries = [
            {
                "updated_at": "2026-04-24 10:00:00 IST",
                "updated_at_iso": "2026-04-24T10:00:00+05:30",
                "chunks": 9,
                "paths": 3,
                "current_phase": "building",
            },
            {
                "updated_at": "2026-04-24 11:00:00 IST",
                "updated_at_iso": "2026-04-24T11:00:00+05:30",
                "chunks": 12,
                "paths": 4,
                "current_phase": "idle",
            },
        ]
        self.history_path.write_text(
            "\n".join(json.dumps(item, ensure_ascii=True) for item in entries) + "\n",
            encoding="utf-8",
        )

    def test_dataset_history_and_delta_are_exposed(self) -> None:
        history = dataset_registry.build_dataset_history("demo", limit=5)
        self.assertIsNotNone(history)
        self.assertEqual(history["history_entry_count"], 2)
        self.assertEqual(history["history"][0]["chunks"], 12)
        self.assertEqual(history["history"][0]["delta_chunks_from_previous"], 3)

        delta = dataset_registry.build_dataset_delta("demo")
        self.assertIsNotNone(delta)
        self.assertEqual(delta["status"], "ready")
        self.assertTrue(delta["current_matches_latest_history"])
        self.assertEqual(delta["delta"]["chunks"], 3)
        self.assertEqual(delta["delta"]["paths"], 1)
        self.assertEqual(delta["baseline_source"], "previous_history_entry")

    def test_mcp_server_lists_and_reads_new_history_resources(self) -> None:
        server = SquadMemoryOsMcpServer(self.skills_root, self.task_packs_path)
        tool_names = {item["name"] for item in server.list_tools()["tools"]}
        self.assertIn("memory_dataset_history", tool_names)
        self.assertIn("memory_dataset_delta", tool_names)
        self.assertIn("memory_run_ledger", tool_names)

        resources = {item["uri"] for item in server.list_resources()["resources"]}
        self.assertIn("memory://runs/ledger", resources)
        self.assertIn("memory://dataset/demo/history", resources)
        self.assertIn("memory://dataset/demo/delta", resources)

        history_tool = server.call_tool("memory_dataset_history", {"dataset_id": "demo", "limit": 5})
        self.assertFalse(history_tool["isError"])
        self.assertEqual(history_tool["structuredContent"]["history_entry_count"], 2)

        delta_tool = server.call_tool("memory_dataset_delta", {"dataset_id": "demo"})
        self.assertFalse(delta_tool["isError"])
        self.assertEqual(delta_tool["structuredContent"]["delta"]["chunks"], 3)

        history_resource = server.read_resource("memory://dataset/demo/history")
        self.assertIn("Dataset History: Demo DB", history_resource["contents"][0]["text"])

        delta_resource = server.read_resource("memory://dataset/demo/delta")
        self.assertIn("Dataset Delta: Demo DB", delta_resource["contents"][0]["text"])


if __name__ == "__main__":
    unittest.main()
