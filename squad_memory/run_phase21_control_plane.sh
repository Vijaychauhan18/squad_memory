#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase21_control_plane.py" report \
  --phase21-dir "$BASE/ingest/phase21" \
  --ingest-root "$BASE/ingest" >> "$LOG_DIR/phase21_control_plane.log" 2>&1
