#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
RUNNER="$BASE/run_seo_elite_2h_sprint_cycle.sh"
STOP_FILE="$BASE/seo_elite_2h_sprint_stop_at.txt"
MARKER="codex-seo-elite-2h-sprint"
TMP_FILE="$(mktemp)"

python3 -c 'import time; print(int(time.time()) + 7200)' > "$STOP_FILE"

if crontab -l > "$TMP_FILE" 2>/dev/null; then
  grep -v "$MARKER" "$TMP_FILE" > "${TMP_FILE}.filtered" || true
else
  : > "${TMP_FILE}.filtered"
fi

{
  cat "${TMP_FILE}.filtered"
  echo "*/20 * * * * zsh $RUNNER # $MARKER"
} > "${TMP_FILE}.next"

crontab "${TMP_FILE}.next"
rm -f "$TMP_FILE" "${TMP_FILE}.filtered" "${TMP_FILE}.next"

nohup zsh "$RUNNER" >/dev/null 2>&1 &
