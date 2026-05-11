#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
SKILLS_ROOT="/Users/vijaychauhan/.codex/elite-skills"
DB_PATH="$BASE/seo_elite_memory.db"
DEFER_BUILD="${SEO_ELITE_DEFER_BUILD:-0}"
DEFER_VISUAL_REFRESH="${SEO_ELITE_DEFER_VISUAL_REFRESH:-0}"

mkdir -p "$LOG_DIR"

python3 "$BASE/harvest_seo_elite_articles.py" \
  --memory-dir "$SKILLS_ROOT/seo-elite/memory" \
  --archive-dir "$SKILLS_ROOT/seo-elite/memory/archive" \
  --skills-root "$SKILLS_ROOT" \
  --db-path "$DB_PATH" \
  --state-path "$BASE/ingest/seo_elite/article_harvest/state.json" \
  --runs-dir "$BASE/ingest/seo_elite/article_harvest/runs" \
  --limit-per-run 2000 \
  --max-workers 24 >> "$LOG_DIR/seo_elite_article_harvest.log" 2>&1

if [[ "$DEFER_BUILD" != "1" ]]; then
  python3 "$BASE/squad_memory.py" build \
    --root "$SKILLS_ROOT" \
    --db "$DB_PATH" >> "$LOG_DIR/seo_elite_article_harvest.log" 2>&1
fi

if [[ "$DEFER_VISUAL_REFRESH" != "1" ]]; then
  zsh "$BASE/run_seo_elite_visual_refresh.sh"
fi
