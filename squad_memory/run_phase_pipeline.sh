#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase_pipeline.py" --openclaw-sync >> "$LOG_DIR/phase_pipeline.log" 2>&1
