#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
DEFER_BUILD="${SEO_ELITE_DEFER_BUILD:-0}"
DEFER_VISUAL_REFRESH="${SEO_ELITE_DEFER_VISUAL_REFRESH:-0}"

mkdir -p "$LOG_DIR"

primary_cmd=(python3 "$BASE/refresh_seo_elite_primary_sources.py")
if [[ "$DEFER_BUILD" == "1" ]]; then
  primary_cmd+=(--skip-build)
fi
"${primary_cmd[@]}" >> "$LOG_DIR/seo_elite_primary_sources.log" 2>&1

if [[ "$DEFER_VISUAL_REFRESH" != "1" ]]; then
  zsh "$BASE/run_seo_elite_visual_refresh.sh"
fi
