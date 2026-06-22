#!/bin/zsh
set -euo pipefail

python3 $HOME/squad_memory/phase31_memory_graph.py build \
  --db-path $HOME/squad_memory/seo_elite_memory.db \
  "$@"
