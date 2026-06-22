#!/bin/zsh
set -euo pipefail

exec python3 $HOME/squad_memory/phase30_scorecard_learning.py "$@"
