#!/usr/bin/env bash
set -euo pipefail

SERVER_NAME="${1:-squad-memory-os}"
SCOPE="${2:-user}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

claude mcp add --transport stdio --scope "$SCOPE" "$SERVER_NAME" -- \
  python3 "$ROOT/mcp/universal_memory_mcp_server.py" \
    --skills-root "/Users/vijaychauhan/.codex/skills" \
    --task-packs "$ROOT/task_packs.json"

echo "Installed $SERVER_NAME for Claude ($SCOPE scope)."
