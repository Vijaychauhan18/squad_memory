#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
MEMORY_DIR="/Users/vijaychauhan/.codex/skills/seo/memory"

mkdir -p "$LOG_DIR"

python3 "$BASE/knowledge_ingest.py" run \
  --config "$BASE/knowledge_sources.json" \
  --output-dir "$MEMORY_DIR" \
  --summary-path "$MEMORY_DIR/live-knowledge-monitor.md" \
  --snapshot-dir "$BASE/ingest/raw" \
  --runs-dir "$BASE/ingest/runs" \
  --state-path "$BASE/ingest/state.json" \
  --top 10 \
  --build-db \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --db-path "$BASE/squad_memory.db" >> "$LOG_DIR/phase1_ingest.log" 2>&1
