#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase11_bootstrap_writer_marketing.py" \
  --skills-root "$HOME/.codex/skills" \
  --phase11-dir "$BASE/ingest/phase11" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase11_bootstrap_writer_marketing.log" 2>&1
