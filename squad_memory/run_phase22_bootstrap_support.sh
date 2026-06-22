#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase22_bootstrap_support.py" \
  --skills-root "$HOME/.codex/skills" \
  --phase22-dir "$BASE/ingest/phase22" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase22_bootstrap_support.log" 2>&1
