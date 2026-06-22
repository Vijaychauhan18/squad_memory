#!/usr/bin/env python3
from __future__ import annotations

import json
import traceback
from datetime import datetime
from pathlib import Path

from refresh_openclaw_seo_automation import (
    DEFAULT_OPENCLAW_WORKSPACE,
    DEFAULT_STATUS_JSON,
    DEFAULT_STATUS_MD,
    refresh_openclaw_seo_automation,
)
from report_seo_elite_status import build_status_payload, send_notification, write_outputs


BASE = Path.home() / "squad_memory"
LOG_PATH = BASE / "logs" / "seo_elite_status_ping.log"


def append_log(step: str, rc: int, text: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(f"{timestamp} step={step} rc={rc}\n")
        if text:
            handle.write(text.rstrip() + "\n")


def run_report_status() -> int:
    try:
        payload = build_status_payload()
        write_outputs(payload)
        send_notification(
            payload["db"]["chunks"],
            payload["articles"]["live_article_notes"],
            payload["articles"]["archive_article_notes"],
        )
        summary = json.dumps(
            {
                "status_path": str(DEFAULT_STATUS_MD),
                "status_json_path": str(DEFAULT_STATUS_JSON),
                "chunks": payload["db"]["chunks"],
                "live_articles": payload["articles"]["live_article_notes"],
                "archive_articles": payload["articles"]["archive_article_notes"],
                "pending_total": payload["pending"]["pending_total"],
            },
            ensure_ascii=True,
        )
        append_log("report_status", 0, summary)
        return 0
    except Exception:
        append_log("report_status", 1, traceback.format_exc())
        return 1


def run_refresh() -> int:
    try:
        result = refresh_openclaw_seo_automation(
            status_json_path=DEFAULT_STATUS_JSON,
            status_md_path=DEFAULT_STATUS_MD,
            workspace=DEFAULT_OPENCLAW_WORKSPACE,
        )
        append_log("refresh_openclaw_automation", 0, json.dumps(result, ensure_ascii=True))
        return 0
    except Exception:
        append_log("refresh_openclaw_automation", 1, traceback.format_exc())
        return 1


def main() -> int:
    report_rc = run_report_status()
    if report_rc != 0:
        return report_rc
    return run_refresh()


if __name__ == "__main__":
    raise SystemExit(main())
