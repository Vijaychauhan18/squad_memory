#!/bin/zsh
set -eu

SOURCE_DIR="$HOME/.codex/skills/seo/memory"
TARGET_DIR="$HOME/.codex/elite-skills/seo-elite/memory"
MANIFEST="$HOME/squad_memory/seo_elite_seed_manifest.txt"

mkdir -p "$TARGET_DIR"

while IFS= read -r note; do
  [[ -z "$note" ]] && continue
  if [[ -f "$SOURCE_DIR/$note" ]]; then
    cp "$SOURCE_DIR/$note" "$TARGET_DIR/$note"
  fi
done < "$MANIFEST"
