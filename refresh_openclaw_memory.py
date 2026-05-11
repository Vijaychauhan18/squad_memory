#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from openclaw_fts_backfill import backfill_openclaw_fts
from refresh_openclaw_seo_bridge import bridge_seo_elite_chunks
from sync_codex_to_openclaw import SyncConfig, sync_openclaw_memory


def parse_args() -> argparse.Namespace:
    home = Path.home()
    parser = argparse.ArgumentParser(description="Sync Codex memory into OpenClaw and rebuild local FTS indices")
    parser.add_argument("--codex-root", default=str(home / ".codex"))
    parser.add_argument("--openclaw-root", default=str(home / ".openclaw"))
    parser.add_argument("--squad-memory-root", default=str(Path(__file__).resolve().parent))
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def refresh_openclaw_memory(codex_root: Path, openclaw_root: Path, squad_memory_root: Path) -> dict[str, Any]:
    openclaw_workspace = openclaw_root / "workspace"
    seo_workspace = openclaw_workspace / "squad" / "seo"
    seo_elite_db = squad_memory_root / "seo_elite_memory.db"
    sync_result = sync_openclaw_memory(
        SyncConfig(
            codex_root=codex_root,
            openclaw_workspace=openclaw_workspace,
            squad_memory_root=squad_memory_root,
        )
    )
    backfill_result = backfill_openclaw_fts(openclaw_root)
    bridge_result: dict[str, Any] = {
        "status": "skipped",
        "reason": f"missing source db: {seo_elite_db}",
    }
    if seo_elite_db.exists():
        seo_bridge = bridge_seo_elite_chunks(
            source_db=seo_elite_db,
            openclaw_root=openclaw_root,
            workspace=seo_workspace,
            target_db=openclaw_root / "memory" / "seo.sqlite",
            write_map=True,
        )
        main_bridge = bridge_seo_elite_chunks(
            source_db=seo_elite_db,
            openclaw_root=openclaw_root,
            workspace=seo_workspace,
            target_db=openclaw_root / "memory" / "main.sqlite",
            write_map=False,
        )
        bridge_result = {
            "status": "ok",
            "source_db": str(seo_elite_db),
            "imported_chunks": seo_bridge["imported_chunks"],
            "imported_paths": seo_bridge["imported_paths"],
            "targets": {
                "seo": seo_bridge,
                "main": main_bridge,
            },
            "written": seo_bridge.get("written", {}),
        }
    return {
        "status": "ok",
        "codex_root": str(codex_root),
        "openclaw_root": str(openclaw_root),
        "squad_memory_root": str(squad_memory_root),
        "sync": sync_result,
        "backfill": backfill_result,
        "bridge": bridge_result,
    }


def main() -> int:
    args = parse_args()
    result = refresh_openclaw_memory(
        codex_root=Path(args.codex_root),
        openclaw_root=Path(args.openclaw_root),
        squad_memory_root=Path(args.squad_memory_root),
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        counts = result["sync"]["counts"]
        agents = result["backfill"]["agents"]
        print(
            "OpenClaw refresh complete | "
            f"seo_memory={counts['seo_memory']} seo_router={counts['seo_router']} "
            f"dejan={counts['dejan']} durable={counts['durable']} "
            f"graph_hq_assets={counts['graph_hq_assets']} graph_hq_docs={counts['graph_hq_docs']} "
            f"skill_packs={counts['skill_packs']} skill_docs={counts['skill_docs']}"
        )
        for agent in agents:
            print(
                f"{agent['agent_id']}: files={agent['files']} chunks={agent['chunks']} db={agent['db_path']}"
            )
        bridge = result["bridge"]
        if bridge.get("status") == "ok":
            print(
                f"bridge: chunks={bridge['imported_chunks']} paths={bridge['imported_paths']} "
                f"seo_db={bridge['targets']['seo']['target_db']} main_db={bridge['targets']['main']['target_db']}"
            )
        else:
            print(f"bridge: {bridge['status']} ({bridge.get('reason', 'no reason')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
