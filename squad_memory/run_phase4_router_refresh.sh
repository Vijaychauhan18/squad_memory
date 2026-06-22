#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase4_router_refresh.py" \
  --memory-router "$HOME/.codex/skills/seo/MEMORY.md" \
  --index-path "$HOME/.codex/skills/seo/memory/INDEX.md" \
  --output-dir "$HOME/.codex/skills/seo/memory" \
  --phase3-manifest "$BASE/ingest/phase3/latest.json" \
  --skills-root "$HOME/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase4_router_refresh.log" 2>&1
