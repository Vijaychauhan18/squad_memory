#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase18_promote_charles.py" \
  --skills-root "$HOME/.codex/skills" \
  --phase17-manifest "$BASE/ingest/phase17/latest.json" \
  --phase18-dir "$BASE/ingest/phase18" \
  --state-path "$BASE/ingest/phase18/state.json" >> "$LOG_DIR/phase18_promote_charles.log" 2>&1
