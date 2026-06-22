#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase27_promote_dev_qa_approved.py" \
  --phase26-manifest "$BASE/ingest/phase26/latest.json" \
  --phase27-dir "$BASE/ingest/phase27" \
  --decisions-path "$BASE/ingest/phase27/decisions.json" \
  --state-path "$BASE/ingest/phase27/state.json" \
  --skills-root "$HOME/.codex/skills" \
  --db-path "$BASE/squad_memory.db" >> "$LOG_DIR/phase27_promote_dev_qa_approved.log" 2>&1
