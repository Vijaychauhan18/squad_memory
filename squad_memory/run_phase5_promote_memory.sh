#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase5_promote_memory.py" \
  --output-dir "$HOME/.codex/skills/seo/memory" \
  --phase3-manifest "$BASE/ingest/phase3/latest.json" \
  --phase5-dir "$BASE/ingest/phase5" \
  --state-path "$BASE/ingest/phase5/state.json" >> "$LOG_DIR/phase5_promote_memory.log" 2>&1
