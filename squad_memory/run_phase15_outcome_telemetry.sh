#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase15_outcome_telemetry.py" \
  --phase15-dir "$BASE/ingest/phase15" \
  --db-path "$BASE/squad_memory.db" >> "$LOG_DIR/phase15_outcome_telemetry.log" 2>&1
