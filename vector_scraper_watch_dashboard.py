#!/usr/bin/env python3
from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


BASE = Path("/Users/vijaychauhan/squad_memory")
STATUS_JSON = BASE / "status" / "squad_memory_watch" / "latest-status.json"
STATUS_MD = BASE / "status" / "squad_memory_watch" / "latest-status.md"
TIMELINE = BASE / "status" / "squad_memory_watch" / "history" / "timeline.jsonl"


HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Vector DB Scraper Watch Dashboard</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #0d1117;
      --panel: #151b23;
      --panel-2: #101820;
      --border: #2d3745;
      --text: #eef4ff;
      --muted: #9caabb;
      --green: #45d483;
      --amber: #f0bf4d;
      --red: #ff6b6b;
      --blue: #6ab7ff;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font: 14px/1.45 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
    }
    header {
      padding: 22px 28px;
      border-bottom: 1px solid var(--border);
      background: #0f141b;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }
    h1 { margin: 0; font-size: 24px; letter-spacing: 0; }
    .sub { color: var(--muted); margin-top: 4px; }
    button {
      border: 1px solid var(--border);
      background: #1b2633;
      color: var(--text);
      border-radius: 6px;
      padding: 9px 12px;
      cursor: pointer;
    }
    main { padding: 24px 28px 36px; max-width: 1500px; margin: 0 auto; }
    .grid { display: grid; gap: 14px; grid-template-columns: repeat(12, 1fr); }
    .card {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      min-width: 0;
    }
    .span-3 { grid-column: span 3; }
    .span-4 { grid-column: span 4; }
    .span-6 { grid-column: span 6; }
    .span-8 { grid-column: span 8; }
    .span-12 { grid-column: span 12; }
    .label { color: var(--muted); font-size: 12px; text-transform: uppercase; }
    .value { font-size: 32px; font-weight: 700; margin-top: 6px; }
    .small { color: var(--muted); font-size: 13px; }
    .status { display: inline-flex; align-items: center; gap: 8px; }
    .dot { width: 9px; height: 9px; border-radius: 50%; background: var(--green); }
    .dot.idle { background: var(--amber); }
    .dot.bad { background: var(--red); }
    table { width: 100%; border-collapse: collapse; }
    th, td { padding: 9px 7px; border-bottom: 1px solid var(--border); text-align: left; vertical-align: top; }
    th { color: var(--muted); font-size: 12px; text-transform: uppercase; }
    pre {
      white-space: pre-wrap;
      word-break: break-word;
      background: var(--panel-2);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 12px;
      max-height: 360px;
      overflow: auto;
    }
    @media (max-width: 900px) {
      header { align-items: flex-start; flex-direction: column; }
      .span-3, .span-4, .span-6, .span-8 { grid-column: span 12; }
    }
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Vector DB Scraper Watch Dashboard</h1>
      <div class="sub">Live watch view for scraper jobs, vector DB growth, fetch pressure, and recent ingest logs.</div>
    </div>
    <button id="refresh">Refresh</button>
  </header>
  <main>
    <section class="grid" id="app"></section>
  </main>
  <script>
    const app = document.querySelector("#app");
    const fmt = new Intl.NumberFormat();
    const esc = (value) => String(value ?? "").replace(/[&<>"']/g, c => ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;" }[c]));
    const n = (value) => Number.isFinite(Number(value)) ? fmt.format(Number(value)) : "0";
    const age = (seconds) => {
      const s = Number(seconds || 0);
      if (s > 86400) return `${Math.round(s / 86400)}d`;
      if (s > 3600) return `${Math.round(s / 3600)}h`;
      if (s > 60) return `${Math.round(s / 60)}m`;
      return `${Math.round(s)}s`;
    };
    const card = (span, title, body) => `<article class="card span-${span}"><div class="label">${esc(title)}</div>${body}</article>`;
    async function load() {
      const [statusRes, timelineRes] = await Promise.all([fetch("/api/status"), fetch("/api/timeline")]);
      const status = await statusRes.json();
      const timeline = await timelineRes.json();
      const db = status.db || {};
      const articles = status.articles || {};
      const pending = status.pending || {};
      const activity = status.activity || {};
      const jobs = status.active_jobs || [];
      const logs = status.logs || {};
      const sources = activity.top_fetch_sources || [];
      const latest = (status.recent_knowledge || {}).live_articles || [];
      const activeCount = jobs.filter(j => j.status === "active").length;
      const jobRows = jobs.map(j => `<tr><td><span class="status"><span class="dot ${j.status === "active" ? "" : "idle"}"></span>${esc(j.job)}</span></td><td>${esc(j.status)}</td><td>${esc(j.updated_at || "")}</td><td>${age(j.age_seconds)}</td></tr>`).join("");
      const sourceRows = sources.map(s => `<tr><td>${esc(s.source)}</td><td>${n(s.count)}</td></tr>`).join("");
      const latestRows = latest.map(item => `<tr><td>${esc(item.path)}</td><td>${esc(item.updated)}</td></tr>`).join("");
      const logText = Object.entries(logs).map(([name, rows]) => `## ${name}\\n${(rows || []).slice(-8).join("\\n")}`).join("\\n\\n");
      const timelineText = timeline.items.slice(-12).map(item => `${item.updated_at || item.updated_at_iso || ""} | chunks=${(item.db || {}).chunks || ""} | fetched=${((item.pending || {}).fetched_total) || ""}`).join("\\n");
      app.innerHTML = [
        card(3, "Watch State", `<div class="value">${activeCount ? "Active" : "Idle"}</div><div class="small">Updated ${esc(status.updated_at || "")}</div>`),
        card(3, "Vector Chunks", `<div class="value">${n(db.chunks)}</div><div class="small">${esc(db.db_path || "")}</div>`),
        card(3, "Fetched URLs", `<div class="value">${n(pending.fetched_total)}</div><div class="small">${n(pending.failed_total)} failed URLs</div>`),
        card(3, "Live Articles", `<div class="value">${n(articles.live_article_notes)}</div><div class="small">${n(articles.archive_article_notes)} archive notes</div>`),
        card(4, "Current Fetch", `<div class="value">${esc(activity.latest_fetch_code || "n/a")}</div><div class="small">${esc(activity.latest_fetch_source || "")}<br>${esc(activity.latest_fetch_url || "")}<br>${esc(activity.latest_fetch_at || "")}</div>`),
        card(4, "Recent Fetch Window", `<div class="value">${n(activity.recent_fetch_ok)} / ${n(activity.recent_fetch_total)}</div><div class="small">${n(activity.recent_fetch_error)} errors in ${n(activity.recent_fetch_window_seconds)}s</div>`),
        card(4, "Build Phase", `<div class="value">${esc(activity.current_phase || "unknown")}</div><div class="small">Latest harvested notes: ${n(activity.latest_harvested_notes)}</div>`),
        card(8, "Active Jobs", `<table><thead><tr><th>Job</th><th>Status</th><th>Updated</th><th>Age</th></tr></thead><tbody>${jobRows}</tbody></table>`),
        card(4, "Top Fetch Sources", `<table><thead><tr><th>Source</th><th>Count</th></tr></thead><tbody>${sourceRows}</tbody></table>`),
        card(8, "Newest Knowledge", `<table><thead><tr><th>Path</th><th>Updated</th></tr></thead><tbody>${latestRows}</tbody></table>`),
        card(4, "Timeline Tail", `<pre>${esc(timelineText || "No timeline rows.")}</pre>`),
        card(12, "Recent Logs", `<pre>${esc(logText || "No log rows.")}</pre>`)
      ].join("");
    }
    document.querySelector("#refresh").addEventListener("click", load);
    load();
    setInterval(load, 5000);
  </script>
</body>
</html>
"""


def read_json(path: Path) -> object:
    if not path.exists():
        return {"ok": False, "error": f"missing file: {path}"}
    return json.loads(path.read_text(encoding="utf-8"))


def read_timeline(limit: int = 240) -> dict[str, object]:
    if not TIMELINE.exists():
        return {"items": []}
    rows = [line for line in TIMELINE.read_text(encoding="utf-8").splitlines() if line.strip()]
    items = []
    for row in rows[-limit:]:
        try:
            items.append(json.loads(row))
        except json.JSONDecodeError:
            continue
    return {"items": items}


class Handler(BaseHTTPRequestHandler):
    def send_body(self, body: bytes, content_type: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, payload: object) -> None:
        self.send_body(json.dumps(payload, ensure_ascii=True).encode("utf-8"), "application/json; charset=utf-8")

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path in {"/", "/index.html"}:
            self.send_body(HTML.encode("utf-8"), "text/html; charset=utf-8")
            return
        if path == "/api/status":
            self.send_json(read_json(STATUS_JSON))
            return
        if path == "/api/status.md":
            self.send_body(STATUS_MD.read_text(encoding="utf-8").encode("utf-8"), "text/markdown; charset=utf-8")
            return
        if path == "/api/timeline":
            self.send_json(read_timeline())
            return
        self.send_error(404)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Serve the vector DB scraper watch dashboard.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8794)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Vector DB scraper watch dashboard serving on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
