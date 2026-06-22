#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase25_external_dev_qa.py" \
  --config "$BASE/knowledge_sources_dev_qa.json" \
  --skills-root "$HOME/.codex/skills" \
  --phase25-dir "$BASE/ingest/phase25" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase25_external_dev_qa.log" 2>&1
