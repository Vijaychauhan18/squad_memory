# Squad AI — Vijay Chauhan's SEO Agent Stack

A 24-agent AI system for SEO professionals, built on Claude Code. One setup, full coverage from keyword research to technical audits to GSC monitoring.

---

## What's included

| Layer | What it does |
|-------|-------------|
| **24 AI agents** | Each specialist handles one domain — SEO, writing, research, code, finance, support |
| **Pinchy (orchestrator)** | Routes every task to the right agent automatically |
| **SEO knowledge base** | 70,000+ chunks of SEO research, patents, practitioner notes pre-loaded |
| **3 live dashboards** | Memory Graph (8765), SEO Elite (8791), Scraper Watch (8794) |
| **MCP data connections** | GSC, GA4, Ahrefs, Lumar wired up and ready |
| **Patent-backed audit tool** | 17 Google patents mapped to 6 audit types |

---

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Claude Code | Latest | https://claude.ai/code |
| Python | 3.10+ | https://python.org |
| Node.js | 18+ | https://nodejs.org |

---

## Setup

### Windows

```powershell
# 1. Clone
git clone https://github.com/Vijaychauhan18/squad_memory.git
cd squad_memory

# 2. Reassemble the vector databases (required — they ship as chunks)
cd squad_memory\db_chunks
python reassemble_dbs.py
cd ..\..

# 3. Run setup (PowerShell as Admin)
powershell -ExecutionPolicy Bypass -File setup.ps1

# 4. Fill in API keys — Vijay will share these separately
# Edit: %USERPROFILE%\.claude\settings.json
```

### Mac / Linux

```bash
# 1. Clone
git clone https://github.com/Vijaychauhan18/squad_memory.git
cd squad_memory

# 2. Reassemble the vector databases
cd squad_memory/db_chunks && python3 reassemble_dbs.py && cd ../..

# 3. Run setup
zsh setup.sh

# 4. Fill in API keys
# Edit: ~/.claude/settings.json
```

### API keys you need (get from Vijay)

| Key | Where it goes in settings.json |
|-----|-------------------------------|
| Ahrefs API key | `mcpServers.ahrefs.env.API_KEY` |
| SEO MCP API key | `mcpServers.seo-mcp-busbud.env.SEOMCP_API_KEY` |
| Google Service Account JSON | `mcpServers.seo-mcp-busbud.env.GOOGLE_SERVICE_ACCOUNT` |
| GA4 Property IDs | `mcpServers.seo-mcp-busbud.env.GA4_PROPERTIES` |
| GSC Site URLs | `mcpServers.seo-mcp-busbud.env.GSC_PROPERTIES` |
| GA4 Property ID | `mcpServers.ga4-busbud.env.GA_PROPERTY_ID` |
| Google credentials path | `mcpServers.ga4-busbud.env.GOOGLE_APPLICATION_CREDENTIALS` |

---

## Daily use

Open Claude Code and just describe what you need. Pinchy handles routing.

```
"Morning briefing"
"What are our top quick wins this week?"
"Write a content brief for 'bus from Montreal to New York'"
"Check if busbud.com homepage is indexed"
"Find what Air Transat ranks for that we don't"
"Audit the technical SEO on busbud.com/en-us"
```

### Slash commands

| Command | What it does |
|---------|-------------|
| `/crawl-page [url]` | Full SEO audit of a URL |
| `/serp-scrape [keyword]` | Scrape top 10 + PAA + rich features |
| `/full-audit [url]` | NavBoost + E-E-A-T + AI Overview audit |
| `/eeat-check [url]` | E-E-A-T score 0-100 with fixes |
| `/content-gap [keyword] \| [your-url]` | Find topics competitors cover that you don't |
| `/pipeline-status` | Full system health check |
| `/dashboards` | Check/start all 3 dashboards |

---

## Dashboards

Start with:
```bash
cd ~/squad_memory
python3 phase31_memory_graph.py serve --host 127.0.0.1 --port 8765 --db-path squad_memory.db &
zsh run_seo_elite_dashboard.sh 8791 &
python3 vector_scraper_watch_dashboard.py --host 127.0.0.1 --port 8794 &
```

| Dashboard | URL | What it shows |
|-----------|-----|---------------|
| Memory Graph | http://127.0.0.1:8765 | 3D agent network, task history, knowledge nodes |
| SEO Elite | http://127.0.0.1:8791 | SEO knowledge DB status, chunk counts, recent ingests |
| Scraper Watch | http://127.0.0.1:8794 | Live scraper jobs, fetch pressure, ingest timeline |

---

## Repo structure

```
├── setup.sh                    ← Mac/Linux setup
├── setup.ps1                   ← Windows setup (PowerShell)
├── settings.template.json      ← Claude Code MCP config (fill in API keys)
├── claude/
│   ├── CLAUDE.md               ← Pinchy orchestrator (goes to ~/.claude/)
│   └── agents/                 ← 26 specialist agents (go to ~/.claude/agents/)
├── squad_memory/
│   ├── *.py / *.sh             ← Pipeline scripts
│   ├── knowledge_sources*.json ← Scraper source configs
│   ├── mcp/                    ← Universal memory MCP server
│   └── db_chunks/              ← Split databases (reassemble_dbs.py joins them)
├── codex/skills/seo/           ← SEO knowledge base (3,980 .md notes)
└── docs/
    ├── AGENTS.md               ← Full agent reference
    └── COMMANDS.md             ← All slash commands
```

---

## Contact

Built by Vijay Chauhan — vijay.chauhan@busbud.com
