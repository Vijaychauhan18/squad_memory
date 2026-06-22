#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase4_router_refresh.py" \
  --memory-router "/Users/vijaychauhan/.codex/skills/seo/MEMORY.md" \
  --index-path "/Users/vijaychauhan/.codex/skills/seo/memory/INDEX.md" \
  --output-dir "/Users/vijaychauhan/.codex/skills/seo/memory" \
  --phase3-manifest "$BASE/ingest/phase3/latest.json" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase4_router_refresh.log" 2>&1
