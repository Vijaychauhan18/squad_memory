#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase8_promote_canon.py" \
  --output-dir "$HOME/.codex/skills/seo/memory" \
  --phase6-decisions "$BASE/ingest/phase6/decisions.json" \
  --phase7-registry "$BASE/ingest/phase7/canonical_registry.json" \
  --phase7-dir "$BASE/ingest/phase7" \
  --phase8-dir "$BASE/ingest/phase8" \
  --skills-root "$HOME/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase8_promote_canon.log" 2>&1
