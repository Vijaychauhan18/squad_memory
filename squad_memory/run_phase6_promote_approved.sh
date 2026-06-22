#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase6_promote_approved.py" \
  --output-dir "$HOME/.codex/skills/seo/memory" \
  --phase5-manifest "$BASE/ingest/phase5/latest.json" \
  --phase6-dir "$BASE/ingest/phase6" \
  --decisions-path "$BASE/ingest/phase6/decisions.json" \
  --state-path "$BASE/ingest/phase6/state.json" \
  --memory-router "$HOME/.codex/skills/seo/MEMORY.md" \
  --index-path "$HOME/.codex/skills/seo/memory/INDEX.md" \
  --skills-root "$HOME/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase6_promote_approved.log" 2>&1
