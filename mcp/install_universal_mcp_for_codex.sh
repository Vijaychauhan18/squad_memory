#!/usr/bin/env bash
set -euo pipefail

SERVER_NAME="${1:-squad-memory-os}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

codex mcp add "$SERVER_NAME" -- \
  python3 "$ROOT/mcp/universal_memory_mcp_server.py" \
    --skills-root "/Users/vijaychauhan/.codex/skills" \
    --task-packs "$ROOT/task_packs.json"

echo "Installed $SERVER_NAME for Codex."
