#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import time
from typing import Any, Dict, List
from urllib.parse import parse_qs, urlparse

import dataset_registry
import manual_url_ingest
import report_seo_elite_status as status_report


HOME = Path.home()
BASE = HOME / "squad_memory"
UI_DIR = BASE / "seo_elite_dashboard_ui"
PRIMARY_DATASET_ID = "seo_elite"
STATUS_JSON = Path(
    os.getenv(
        "SEO_ELITE_STATUS_JSON",
        str(HOME / ".codex" / "elite-skills" / "seo-elite" / "status" / "latest-status.json"),
    )
)
HISTORY_PATH = Path(
    os.getenv(
        "SEO_ELITE_HISTORY_PATH",
        str(HOME / ".codex" / "elite-skills" / "seo-elite" / "status" / "history" / "timeline.jsonl"),
    )
)
MANUAL_INGEST = manual_url_ingest.ManualUrlIngestManager()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the SEO Elite realtime dashboard.")
    parser.add_argument("command", choices=["serve", "snapshot"])
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8788)
    parser.add_argument("--ui-dir", default=str(UI_DIR))
    return parser.parse_args()


def attach_dataset_context(payload: Dict[str, Any], dataset_id: str = PRIMARY_DATASET_ID) -> Dict[str, Any]:
    registry_payload = dataset_registry.build_registry_payload()
    overview = dict(payload)
    overview["dataset"] = next((item for item in registry_payload["items"] if item["id"] == dataset_id), None)
    overview["datasets"] = registry_payload
    return overview


def attach_runtime_context(payload: Dict[str, Any], dataset_id: str = PRIMARY_DATASET_ID) -> Dict[str, Any]:
    overview = attach_dataset_context(payload, dataset_id=dataset_id)
    overview["manual_ingest"] = MANUAL_INGEST.snapshot()
    return overview


def load_overview(refresh: bool = False) -> Dict[str, Any]:
    if refresh or not STATUS_JSON.exists():
        payload = status_report.build_status_payload()
        try:
            status_report.write_outputs(payload)
        except PermissionError:
            if STATUS_JSON.exists():
                return attach_runtime_context(json.loads(STATUS_JSON.read_text()))
        return attach_runtime_context(payload)
    return attach_runtime_context(json.loads(STATUS_JSON.read_text()))


def load_history(limit: int = 288) -> List[Dict[str, Any]]:
    if not HISTORY_PATH.exists():
        return []
    rows = [line for line in HISTORY_PATH.read_text().splitlines() if line.strip()]
    if limit > 0:
        rows = rows[-limit:]
    history: List[Dict[str, Any]] = []
    for row in rows:
        try:
            history.append(json.loads(row))
        except json.JSONDecodeError:
            continue
    return history


def make_handler(ui_dir: Path):
    class DashboardHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(ui_dir), **kwargs)

        def end_headers(self) -> None:
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            super().end_headers()

        def json_response(self, payload: Any, status: int = 200) -> None:
            body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def read_json_body(self) -> Dict[str, Any]:
            try:
                content_length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                content_length = 0
            raw = self.rfile.read(max(content_length, 0)) if content_length > 0 else b"{}"
            if not raw:
                return {}
            try:
                payload = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError as exc:
                raise ValueError("Request body must be valid JSON.") from exc
            if not isinstance(payload, dict):
                raise ValueError("Request body must be a JSON object.")
            return payload

        def event_response(self) -> None:
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Connection", "keep-alive")
            self.end_headers()
            try:
                while True:
                    payload = attach_runtime_context(status_report.build_status_payload())
                    body = json.dumps(payload, ensure_ascii=True)
                    self.wfile.write(f"event: overview\ndata: {body}\n\n".encode("utf-8"))
                    self.wfile.flush()
                    time.sleep(3)
            except (BrokenPipeError, ConnectionResetError):
                return

        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            if parsed.path == "/api/overview":
                refresh = query.get("refresh", ["0"])[0] == "1"
                self.json_response(load_overview(refresh=refresh))
                return
            if parsed.path == "/api/history":
                try:
                    limit = int(query.get("limit", ["288"])[0])
                except ValueError:
                    limit = 288
                self.json_response({"items": load_history(limit)})
                return
            if parsed.path == "/api/datasets":
                self.json_response(dataset_registry.build_registry_payload())
                return
            if parsed.path == "/api/manual-ingest":
                self.json_response(MANUAL_INGEST.snapshot())
                return
            if parsed.path.startswith("/api/datasets/"):
                dataset_id = parsed.path[len("/api/datasets/"):].strip("/")
                payload = dataset_registry.get_dataset_summary(dataset_id)
                if payload is None:
                    self.json_response({"ok": False, "error": f"unknown dataset: {dataset_id}"}, status=404)
                    return
                self.json_response(payload)
                return
            if parsed.path == "/api/stream":
                self.event_response()
                return
            if parsed.path == "/api/health":
                payload = load_overview(refresh=False)
                self.json_response(
                    {
                        "ok": True,
                        "dataset_id": payload.get("dataset", {}).get("id", PRIMARY_DATASET_ID),
                        "dataset_label": payload.get("dataset", {}).get("label", ""),
                        "dataset_path": payload.get("dataset", {}).get("path", ""),
                        "chunks": payload.get("db", {}).get("chunks", 0),
                        "updated_at": payload.get("updated_at", ""),
                    }
                )
                return
            super().do_GET()

        def do_POST(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            if parsed.path != "/api/manual-ingest":
                self.json_response({"ok": False, "error": f"unsupported endpoint: {parsed.path}"}, status=404)
                return
            try:
                payload = self.read_json_body()
                url = str(payload.get("url", "")).strip()
                if not url:
                    raise ValueError("Paste a URL to start instant knowledge chunking.")
                snapshot = MANUAL_INGEST.start(url)
            except ValueError as exc:
                self.json_response({"ok": False, "error": str(exc), "manual_ingest": MANUAL_INGEST.snapshot()}, status=400)
                return
            except RuntimeError as exc:
                self.json_response({"ok": False, "error": str(exc), "manual_ingest": MANUAL_INGEST.snapshot()}, status=409)
                return
            self.json_response({"ok": True, "manual_ingest": snapshot}, status=202)

    return DashboardHandler


def handle_snapshot() -> int:
    payload = load_overview(refresh=True)
    print(json.dumps(payload, indent=2, ensure_ascii=True))
    return 0


def handle_serve(args: argparse.Namespace) -> int:
    ui_dir = Path(args.ui_dir)
    server = ThreadingHTTPServer((args.host, args.port), make_handler(ui_dir))
    print(f"SEO Elite dashboard serving on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "snapshot":
        return handle_snapshot()
    return handle_serve(args)


if __name__ == "__main__":
    raise SystemExit(main())
