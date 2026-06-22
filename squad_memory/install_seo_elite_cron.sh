#!/bin/zsh
set -eu

CRON_FILE="$HOME/squad_memory/cron/seo_elite_memory.crontab"
TMP_FILE="$(mktemp)"

cleanup() {
  rm -f "$TMP_FILE"
}
trap cleanup EXIT

if crontab -l > "$TMP_FILE" 2>/dev/null; then
  :
else
  : > "$TMP_FILE"
fi

# Remove previous elite cron lines before appending the current canonical schedule.
FILTERED="$(mktemp)"
grep -v "$HOME/squad_memory/run_seo_elite_live_sync.sh" "$TMP_FILE" \
  | grep -v "$HOME/squad_memory/run_seo_elite_primary_sources.sh" \
  | grep -v "$HOME/squad_memory/run_seo_elite_archive_backfill.sh" \
  | grep -v "$HOME/squad_memory/run_seo_elite_bulk_backfill.sh" \
  | grep -v "$HOME/squad_memory/run_seo_elite_article_harvest.sh" \
  | grep -v "$HOME/squad_memory/run_seo_elite_cleanup.sh" \
  | grep -v "$HOME/squad_memory/run_seo_elite_status_ping.sh" > "$FILTERED"
mv "$FILTERED" "$TMP_FILE"

while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  [[ "$line" == \#* ]] && continue
  if ! grep -Fqx "$line" "$TMP_FILE"; then
    printf '%s\n' "$line" >> "$TMP_FILE"
  fi
done < "$CRON_FILE"

crontab "$TMP_FILE"
