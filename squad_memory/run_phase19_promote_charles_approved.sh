#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase19_promote_charles_approved.py" \
  --phase18-manifest "$BASE/ingest/phase18/latest.json" \
  --phase19-dir "$BASE/ingest/phase19" \
  --decisions-path "$BASE/ingest/phase19/decisions.json" \
  --state-path "$BASE/ingest/phase19/state.json" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase19_promote_charles_approved.log" 2>&1
