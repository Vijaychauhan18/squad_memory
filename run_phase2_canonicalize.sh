#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
MEMORY_DIR="/Users/vijaychauhan/.codex/skills/seo/memory"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase2_canonicalize.py" \
  --config "$BASE/knowledge_sources.json" \
  --output-dir "$MEMORY_DIR" \
  --state-path "$BASE/ingest/state.json" \
  --runs-dir "$BASE/ingest/runs" \
  --phase2-dir "$BASE/ingest/phase2" \
  --top 5 >> "$LOG_DIR/phase2_canonicalize.log" 2>&1
