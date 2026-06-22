#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/prune_reputable_live_sources.py" >> "$LOG_DIR/reputable_daily_cleanup.log" 2>&1
