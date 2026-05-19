#!/usr/bin/env zsh
# Squad AI — One-command setup script
# Usage: zsh setup.sh
set -euo pipefail

EXPORT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOME_DIR="$HOME"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
info()  { echo "${GREEN}[✓]${NC} $1"; }
warn()  { echo "${YELLOW}[!]${NC} $1"; }
error() { echo "${RED}[✗]${NC} $1"; exit 1; }
ask()   { echo "${YELLOW}[?]${NC} $1"; }

echo ""
echo "  Squad AI Setup — Vijay Chauhan's SEO Agent Stack"
echo "  ================================================="
echo ""

# ── 1. Prerequisites ──────────────────────────────────────────────────────────
echo "Checking prerequisites..."

command -v python3 >/dev/null 2>&1 || error "Python 3 required. Install from https://python.org"
PY_VER=$(python3 -c "import sys; print(sys.version_info.minor)")
[[ "$PY_VER" -ge 10 ]] || error "Python 3.10+ required (found 3.${PY_VER})"
info "Python 3.${PY_VER} found"

command -v node >/dev/null 2>&1 || error "Node.js required. Install from https://nodejs.org"
info "Node.js found"

if ! command -v claude >/dev/null 2>&1; then
  warn "Claude Code CLI not found."
  echo "  Install it from: https://claude.ai/code"
  echo "  Or via: npm install -g @anthropic-ai/claude-code"
  ask "Press Enter once Claude Code is installed, or Ctrl+C to exit..."
  read -r
fi
info "Claude Code found"

# ── 2. Python dependencies ────────────────────────────────────────────────────
echo ""
echo "Installing Python dependencies..."
pip3 install -q requests beautifulsoup4 lxml 2>/dev/null || warn "Some pip packages failed — non-critical"
info "Python deps installed"

# ── 3. Copy Claude config files ───────────────────────────────────────────────
echo ""
echo "Installing agent config files..."

mkdir -p "$HOME_DIR/.claude/agents"

if [[ -f "$HOME_DIR/.claude/CLAUDE.md" ]]; then
  warn "CLAUDE.md already exists — backing up to CLAUDE.md.bak"
  cp "$HOME_DIR/.claude/CLAUDE.md" "$HOME_DIR/.claude/CLAUDE.md.bak"
fi
cp "$EXPORT_DIR/claude/CLAUDE.md" "$HOME_DIR/.claude/CLAUDE.md"
info "CLAUDE.md installed"

cp "$EXPORT_DIR/claude/agents/"*.md "$HOME_DIR/.claude/agents/"
info "$(ls "$EXPORT_DIR/claude/agents/" | wc -l | tr -d ' ') agent files installed"

# ── 4. Install squad_memory pipeline ─────────────────────────────────────────
echo ""
echo "Installing squad_memory pipeline..."
mkdir -p "$HOME_DIR/squad_memory/logs" "$HOME_DIR/squad_memory/mcp" "$HOME_DIR/squad_memory/status"

cp "$EXPORT_DIR/squad_memory/"*.py "$HOME_DIR/squad_memory/"
cp "$EXPORT_DIR/squad_memory/"*.sh "$HOME_DIR/squad_memory/"
cp "$EXPORT_DIR/squad_memory/"*.json "$HOME_DIR/squad_memory/"
cp "$EXPORT_DIR/squad_memory/mcp/universal_memory_mcp_server.py" "$HOME_DIR/squad_memory/mcp/"
chmod +x "$HOME_DIR/squad_memory/"*.sh
info "Pipeline scripts installed"

# ── 5. Copy Codex knowledge base ─────────────────────────────────────────────
echo ""
echo "Installing SEO knowledge base (this may take a moment)..."
mkdir -p "$HOME_DIR/.codex/skills"
cp -r "$EXPORT_DIR/codex/skills/seo" "$HOME_DIR/.codex/skills/"
info "$(find "$EXPORT_DIR/codex/skills" -name '*.md' | wc -l | tr -d ' ') knowledge notes installed"

# ── 6. Build the vector DB ────────────────────────────────────────────────────
echo ""
echo "Building memory index (squad_memory.db)..."
echo "  This takes 2-5 minutes..."
cd "$HOME_DIR/squad_memory" && python3 squad_memory.py build \
  --root "$HOME_DIR/.codex/skills" \
  --db "$HOME_DIR/squad_memory/squad_memory.db" \
  2>&1 | tail -3
info "Memory index built"

# ── 7. Configure settings.json ───────────────────────────────────────────────
echo ""
echo "Configuring API keys..."
echo ""
warn "You will need the following credentials from Vijay:"
echo "  1. Ahrefs API key"
echo "  2. SEO MCP API key"
echo "  3. Google Service Account JSON (for GSC + GA4)"
echo "  4. GA4 Property ID"
echo ""

SETTINGS_SRC="$EXPORT_DIR/settings.template.json"
SETTINGS_DST="$HOME_DIR/.claude/settings.json"

if [[ -f "$SETTINGS_DST" ]]; then
  warn "settings.json already exists — backing up to settings.json.bak"
  cp "$SETTINGS_DST" "$SETTINGS_DST.bak"
fi

cp "$SETTINGS_SRC" "$SETTINGS_DST"
# Replace $HOME placeholder with actual home directory
sed -i '' "s|\$HOME|$HOME_DIR|g" "$SETTINGS_DST" 2>/dev/null || sed -i "s|\$HOME|$HOME_DIR|g" "$SETTINGS_DST"
info "settings.json installed (API keys need to be filled in)"

echo ""
echo "  Edit $SETTINGS_DST and replace these placeholders:"
echo "  • YOUR_AHREFS_API_KEY"
echo "  • YOUR_SEOMCP_API_KEY"
echo "  • YOUR_GOOGLE_SERVICE_ACCOUNT_JSON_BASE64"
echo "  • YOUR_GA4_PROPERTY_IDS_COMMA_SEPARATED"
echo "  • YOUR_GSC_SITE_URLS_COMMA_SEPARATED"
echo "  • YOUR_GA4_PROPERTY_ID"
echo "  • YOUR_GOOGLE_SERVICE_ACCOUNT_KEY_PATH"

# ── 8. Start dashboards ───────────────────────────────────────────────────────
echo ""
ask "Start dashboards now? (y/n)"
read -r START_DASH
if [[ "$START_DASH" == "y" ]]; then
  cd "$HOME_DIR/squad_memory"
  nohup zsh run_seo_elite_dashboard.sh 8791 > logs/dashboard_8791.log 2>&1 &
  nohup python3 phase31_memory_graph.py serve --host 127.0.0.1 --port 8765 --db-path squad_memory.db > logs/dashboard_8765.log 2>&1 &
  nohup python3 vector_scraper_watch_dashboard.py --host 127.0.0.1 --port 8794 > logs/dashboard_8794.log 2>&1 &
  sleep 3
  info "Dashboards started:"
  echo "  • SEO Dashboard:  http://127.0.0.1:8791"
  echo "  • Memory Graph:   http://127.0.0.1:8765"
  echo "  • Scraper Watch:  http://127.0.0.1:8794"
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo "  Setup complete!"
echo "  ─────────────────────────────────────────────────"
echo "  1. Fill in API keys in: ~/.claude/settings.json"
echo "  2. Open Claude Code and start with: 'Morning briefing'"
echo "  3. All 24 agents are ready — just describe your task"
echo ""
