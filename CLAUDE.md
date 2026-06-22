# Squad AI — Setup Instructions for Claude Code

This folder contains Vijay Chauhan's full SEO agent stack. Your job is to install it on this machine.

## When this folder is opened, do this automatically:

1. Detect the OS — Windows or Mac/Linux
2. **Mac/Linux:** Run `zsh setup.sh` from this directory
   **Windows:** Tell the user to run `powershell -ExecutionPolicy Bypass -File setup.ps1` as Admin
3. If Python or Node are missing, help install them first, then re-run setup
4. Remind the user to reassemble the databases first:
   - Mac: `cd squad_memory/db_chunks && python3 reassemble_dbs.py && cd ../..`
   - Windows: `cd squad_memory\db_chunks && python reassemble_dbs.py && cd ..\..`
5. After setup completes, remind the user to fill in API keys in `~/.claude/settings.json`
6. Start the three dashboards (Mac/Linux only):
   - `cd ~/squad_memory && python3 seo_elite_dashboard.py serve --host 127.0.0.1 --port 8791 &`
   - `cd ~/squad_memory && python3 phase31_memory_graph.py serve --host 127.0.0.1 --port 8765 --db-path squad_memory.db &`
   - `cd ~/squad_memory && python3 vector_scraper_watch_dashboard.py --host 127.0.0.1 --port 8794 &`
7. Verify by running: `/pipeline-status`
8. Tell the user: "Setup complete. Type 'Morning briefing' to start."

## If anything fails:
- Missing Python (Mac): `brew install python@3.11` or https://python.org
- Missing Python (Windows): https://python.org — check "Add to PATH" during install
- Missing Node (Mac): `brew install node` or https://nodejs.org
- Missing Node (Windows): https://nodejs.org
- Missing brew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Permission errors on .sh files (Mac): `chmod +x ~/squad_memory/*.sh`
- npm errors on Windows: run PowerShell as Administrator

## What this installs (Claude Code + Codex):
- 24 AI agents into `~/.claude/agents/`
- Pinchy orchestrator into `~/.claude/CLAUDE.md`
- Pipeline scripts into `~/squad_memory/`
- SEO knowledge base (70,000+ chunks) in `~/squad_memory/squad_memory.db`
- SEO Elite DB in `~/squad_memory/seo_elite_memory.db`
- 3,988 knowledge notes into `~/.codex/skills/seo/`
- 8,962 elite SEO notes into `~/.codex/elite-skills/seo-elite/memory/`
- 3 Codex MCP node packages into `~/.codex/mcps/`
- Global npm MCPs: `mcp-server-gsc`, `mcp-server-ga4`, `mcp-remote`
- Codex config into `~/.codex/config.toml` with all MCPs wired up

## After setup, the user can:
- Type anything in Claude Code — Pinchy routes it to the right agent
- Say "Morning briefing" to start the day
- Use `/crawl-page`, `/serp-scrape`, `/full-audit` and other slash commands
- Open dashboards at http://127.0.0.1:8791 and http://127.0.0.1:8765 (Mac/Linux)

## Note for Windows users:
- The `.sh` shell scripts (cron jobs, pipeline runners) require WSL or Git Bash to run
- Dashboards work on Windows — start them with `python` instead of `zsh run_*.sh`
- See SETUP_GUIDE.md for full Windows-specific instructions
