#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase14_promote_writer_marketing_approved.py" \
  --phase13-manifest "$BASE/ingest/phase13/latest.json" \
  --phase14-dir "$BASE/ingest/phase14" \
  --decisions-path "$BASE/ingest/phase14/decisions.json" \
  --state-path "$BASE/ingest/phase14/state.json" \
  --skills-root "$HOME/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase14_promote_writer_marketing_approved.log" 2>&1
