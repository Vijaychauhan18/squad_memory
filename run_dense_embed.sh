#!/usr/bin/env zsh
# Daily dense embedding pass — embed 2K new chunks per run
# Cron: 45 4 * * * (4:45 AM local — after main pipeline)

set -euo pipefail

LOG="$HOME/squad_memory/logs/dense_embed_$(date +%Y%m%d).log"

echo "[$(date)] Dense embedding pass started" | tee -a "$LOG"

# Check Ollama is running
if ! curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
    echo "[$(date)] Ollama not running — starting..." | tee -a "$LOG"
    ollama serve &>/tmp/ollama.log &
    sleep 5
fi

# Run embedding pass (2K chunks per day = ~58K fully embedded in ~30 days)
python3 "$HOME/squad_memory/dense_embeddings.py" embed --limit 2000 2>&1 | tee -a "$LOG"

echo "[$(date)] Dense embedding pass complete" | tee -a "$LOG"
