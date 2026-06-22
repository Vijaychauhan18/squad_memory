#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase17_external_charles.py" \
  --config "$BASE/knowledge_sources_charles.json" \
  --skills-root "$HOME/.codex/skills" \
  --phase17-dir "$BASE/ingest/phase17" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase17_external_charles.log" 2>&1
