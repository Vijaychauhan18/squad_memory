#!/usr/bin/env python3
"""Local hybrid retriever for Codex squad skills and memory.

This tool indexes installed skills, memory notes, and router documents into:
1. SQLite FTS5 for fast lexical recall
2. A pure-Python sparse TF-IDF layer for reranking

It is designed for environments without vector DBs or ML dependencies.
"""

from __future__ import annotations

import argparse
import dataclasses
import fnmatch
import hashlib
import json
import math
import os
import re
import sqlite3
import tempfile
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


HOME = Path("/Users/vijaychauhan")
SKILLS_ROOT = HOME / ".codex" / "skills"
DB_PATH = HOME / "squad_memory" / "squad_memory.db"
TASK_PACKS_PATH = HOME / "squad_memory" / "task_packs.json"
TASK_EVAL_FIXTURES_PATH = HOME / "squad_memory" / "evals" / "task_fixtures.json"
PHASE7_REGISTRY_PATH = HOME / "squad_memory" / "ingest" / "phase7" / "canonical_registry.json"
PHASE10_LEDGER_PATH = HOME / "squad_memory" / "ingest" / "phase10" / "evidence_ledger.json"
PHASE11_LEDGER_DIR = HOME / "squad_memory" / "ingest" / "phase11"
PHASE12_LEDGER_DIR = HOME / "squad_memory" / "ingest" / "phase12"
PHASE16_LEDGER_DIR = HOME / "squad_memory" / "ingest" / "phase16"
PHASE17_LEDGER_DIR = HOME / "squad_memory" / "ingest" / "phase17"
PHASE23_LEDGER_DIR = HOME / "squad_memory" / "ingest" / "phase23"
PHASE24_LEDGER_DIR = HOME / "squad_memory" / "ingest" / "phase24"
PHASE25_LEDGER_DIR = HOME / "squad_memory" / "ingest" / "phase25"
EPISODE_GAP_MINUTES = 120
EPISODE_SUMMARY_KIND = "auto"
WORKSPACE_MAX_FILES = 80
WORKSPACE_MAX_CHARS = 8000
WORKSPACE_BODY_CHARS = 5000
WORKSPACE_TEXT_EXTENSIONS = {
    ".c",
    ".cc",
    ".cfg",
    ".conf",
    ".cpp",
    ".css",
    ".csv",
    ".env",
    ".go",
    ".graphql",
    ".h",
    ".hpp",
    ".html",
    ".ini",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".py",
    ".rb",
    ".rs",
    ".scss",
    ".sh",
    ".sql",
    ".svg",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}


def file_revision_token(path: Path) -> Tuple[str, int, int]:
    try:
        stat = path.stat()
        return (str(path), int(stat.st_mtime_ns), int(stat.st_size))
    except OSError:
        return (str(path), 0, 0)


def db_revision_token(path: Path) -> Tuple[str, int, int]:
    return file_revision_token(path)
WORKSPACE_IGNORED_DIRS = {
    ".git",
    ".idea",
    ".next",
    ".turbo",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "vendor",
}

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_\-]{1,}")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])")
ISO_DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
MONTH_DATE_RE = re.compile(
    r"\b("
    r"January|February|March|April|May|June|July|August|September|October|November|December"
    r")\s+\d{1,2},\s+20\d{2}\b",
    re.IGNORECASE,
)
DEFAULT_VECTOR_DIM_LIMIT = 48
DEFAULT_TOKEN_CONTEXT_LIMIT = 24
MAX_SEMANTIC_DF_RATIO = 0.25
CONFIDENCE_BOOSTS = {
    "high": 0.05,
    "medium": 0.025,
    "low": 0.0,
}

QUERY_INTENT_RULES = [
    {
        "intent": "entity_authority",
        "patterns": [
            r"\bentity seo\b",
            r"\bentity fit\b",
            r"\bbrand fit\b",
            r"\btopical authority\b",
            r"\bbrand salience\b",
            r"\btopic association\b",
            r"\bstronger brands get cited\b",
            r"\bbrands? get cited\b",
            r"\bsynthetic authority\b",
            r"\btrust representation\b",
            r"\bbrand representation\b",
            r"\bauthority signals?\b",
            r"\beeat\b",
            r"\be-e-a-t\b",
        ],
        "terms": [
            "entity_authority",
            "entity_fit",
            "brand_fit",
            "brand_salience",
            "topic_association",
            "topical_authority",
            "site_trust",
            "trust_representation",
            "brand_representation",
            "authority_signals",
            "synthetic_authority",
        ],
    },
    {
        "intent": "site_reputation_abuse",
        "patterns": [
            r"\bsite reputation abuse\b",
            r"\breputation abuse\b",
            r"\bstarkly different\b",
            r"\bindependent or starkly different\b",
            r"\bthird-party content\b",
            r"\bthird[- ]party\b",
            r"\bparasite\b",
            r"\bpublisher coupon\b",
            r"\bcoupon (?:section|directory|directories)\b",
            r"\breviews? (?:section|directory|directories)\b",
            r"\baffiliate section\b",
            r"\brented authority\b",
            r"\bmanual action\b",
        ],
        "terms": [
            "site_reputation_abuse",
            "section_independence",
            "starkly_different",
            "spam_policy",
            "third_party_content",
            "rented_authority",
            "coupon_section",
            "review_section",
            "manual_action",
            "policy_blocking_strategy",
        ],
    },
    {
        "intent": "javascript_ai_systems",
        "patterns": [
            r"\bclient[- ]side render(?:ing)?\b",
            r"\bserver[- ]side render(?:ing)?\b",
            r"\bcsr\b",
            r"\bssr\b",
            r"\bjavascript rendering\b",
            r"\bjavascript seo\b",
            r"\braw html\b",
            r"\brendered html\b",
            r"\bmachine[- ]readable\b",
            r"\breader mode\b",
            r"\bdomdistiller\b",
            r"\bapc\b",
            r"\bannotated page content\b",
            r"\bwebmcp\b",
            r"google sees it but ai (?:systems|search|assistants?) (?:do not|don't|dont)",
            r"(?:chatgpt|claude|perplexity).*(?:can'?t|cannot|cant).*(?:read|see)",
        ],
        "terms": [
            "javascript_ai_systems",
            "javascript_seo",
            "client_side_rendering",
            "server_side_rendering",
            "raw_html_visibility",
            "rendered_html_diff",
            "machine_readability",
            "reader_mode",
            "domdistiller",
            "apc",
            "webmcp",
            "ai_fetch_tools",
        ],
    },
    {
        "intent": "multilingual_ai_systems",
        "patterns": [
            r"\bhreflang\b",
            r"\btranslated content\b",
            r"\btranslated results?\b",
            r"\bmultilingual queries?\b",
            r"\bmultilingual\b",
            r"\binternational seo\b",
            r"\bwrong language url\b",
            r"\bwrong language version\b",
            r"answers? in .*language.*(?:english|french|spanish|german|japanese)",
            r"cites? .*english page",
            r"\blocali[sz]ed page not being selected\b",
        ],
        "terms": [
            "multilingual_ai_systems",
            "international_seo",
            "hreflang_ai_diagnosis",
            "translated_content",
            "language_version_selection",
            "localized_page_selection",
            "translated_results",
            "language_targeting",
        ],
    },
    {
        "intent": "canonicalization",
        "patterns": [
            r"\brel canonical\b",
            r"\bcanonical(?:s|ization)?\b",
            r"\bwrong url indexed\b",
            r"\bduplicate urls?\b",
            r"\burl selection\b",
        ],
        "terms": [
            "canonicalization",
            "canonical_url_selection",
            "duplicate_control",
            "url_selection",
            "canonical_debugging",
            "index_control",
        ],
    },
    {
        "intent": "technical_seo",
        "patterns": [
            r"\bcanonical(?:s|ization)?\b",
            r"\bnoindex\b",
            r"\brobots(?:\.txt)?\b",
            r"\bcrawl(?:ing)?\b",
            r"\bindex(?:ed|ing|ation)?\b",
            r"\brender(?:ed|ing)?\b",
            r"\bjavascript seo\b",
            r"\bhreflang\b",
            r"\bsitemap(?:s)?\b",
            r"\bredirect(?:s|ed|ing)?\b",
        ],
        "terms": [
            "technical_seo",
            "crawl",
            "indexing",
            "rendering",
            "robots_strategy",
            "javascript_seo",
        ],
    },
    {
        "intent": "recovery",
        "patterns": [
            r"\brecover(?:y|ing)?\b",
            r"\btriage\b",
            r"\bvisibility drop\b",
            r"\btraffic drop\b",
            r"\bhcu\b",
            r"\bhelpful content\b",
            r"\bsite[- ]wide quality\b",
            r"\bsite reputation abuse\b",
        ],
        "terms": [
            "recovery",
            "diagnosis",
            "quality_systems",
            "technical_recovery",
            "sitewide_quality_triage",
            "helpful_content_diagnosis",
        ],
    },
    {
        "intent": "ai_overviews",
        "patterns": [
            r"\bai overviews?\b",
            r"\baio\b",
            r"\bai mode\b",
            r"\bgenerative answers?\b",
            r"\bai answers?\b",
        ],
        "terms": [
            "ai_overviews",
            "ai_mode",
            "ai_search_visibility",
            "citations",
            "grounding",
            "selection_rate",
            "brand_radar",
        ],
    },
    {
        "intent": "ai_visibility",
        "patterns": [r"\bai visibility\b", r"\bbrand mentions?\b", r"\bcitations?\b", r"\bimpressions?\b", r"\bbrand radar\b"],
        "terms": ["ai_visibility", "brand_mentions", "citations", "impressions", "brand_radar", "topic_association"],
    },
    {
        "intent": "ai_selection",
        "patterns": [
            r"selected into ai answers",
            r"not being selected",
            r"\bnot selected\b",
            r"not getting cited",
            r"not being cited",
            r"\bnot cited\b",
            r"ranks? but (?:is not|isn't|isnt|not) (?:being )?cited",
            r"ranks? well but .*selected",
            r"page ranks? but",
            r"answer inclusion",
            r"answer selection",
            r"\bground(?:ed|ing)\b",
            r"snippet extraction",
            r"grounding snippets?",
            r"selection rate",
        ],
        "terms": [
            "selection_rate",
            "grounding",
            "grounding_snippets",
            "snippet_extractability",
            "snippet_extraction",
            "selection",
            "answer_selection",
            "cited",
            "citation_diagnostics",
            "answer_inclusion",
        ],
    },
    {
        "intent": "fan_out",
        "patterns": [r"fan[- ]?out", r"hidden queries?", r"implicit queries?", r"sub[- ]queries?"],
        "terms": ["fan_out", "hidden_queries", "implicit_queries", "query_expansion", "subqueries"],
    },
    {
        "intent": "leak_systems",
        "patterns": [r"\bnavboost\b", r"\bcraps\b", r"\bgoogle leak\b", r"\bsite quality\b", r"\btopicality\b"],
        "terms": ["navboost", "craps", "google_leak", "site_quality", "topicality", "quality_signals"],
    },
    {
        "intent": "content_writing",
        "patterns": [r"\bblog post\b", r"\bdraft\b", r"\bhook\b", r"\boutline\b", r"\bstructure\b", r"\bcopy\b"],
        "terms": ["writing", "editorial", "hook", "outline", "structure", "draft"],
    },
    {
        "intent": "distribution_ops",
        "patterns": [
            r"\bdistribution\b",
            r"\bdistribute\b",
            r"\bpromot(?:e|ing|ion)\b",
            r"\bemail\b",
            r"\bnewsletter\b",
            r"\brollout\b",
        ],
        "terms": ["distribution", "promotion", "rollout", "email", "newsletter"],
    },
    {
        "intent": "code_review",
        "patterns": [
            r"\bcode review\b",
            r"\breviewer[- ]level\b",
            r"\breview focused\b",
            r"\bmaintainability risks?\b",
            r"\bsecurity regressions?\b",
            r"\bperformance regressions?\b",
        ],
        "terms": ["review", "code_review", "correctness", "security", "performance", "maintainability", "patch"],
    },
    {
        "intent": "support_triage",
        "patterns": [r"\btriage\b", r"\bcustomer issue\b", r"\bescalate\b", r"\bseverity\b", r"\bsupport\b"],
        "terms": ["support", "ticket", "triage", "severity", "escalation", "troubleshooting"],
    },
    {
        "intent": "implementation_review",
        "patterns": [r"\bfix\b.*\bbug\b", r"\bproduction bug\b", r"\bwrite tests\b", r"\breview\b.*\bpatch\b", r"\bbugfix\b"],
        "terms": ["developer", "implementation", "bugfix", "tests", "review", "patch", "feature"],
    },
    {
        "intent": "coordination",
        "patterns": [
            r"\bcoordinate\b",
            r"\bhandoffs?\b",
            r"\bcross[- ]functional\b",
            r"\bkeep the handoffs clean\b",
            r"\bwriter\b.*\bseo\b.*\bmarketing\b",
            r"\bspecialists?\b.*\bstep",
        ],
        "terms": [
            "coordination",
            "handoff",
            "orchestration",
            "workflow",
            "owners",
            "orchestrator",
            "pinchy",
            "chief_of_staff",
            "routing",
            "route",
        ],
    },
    {
        "intent": "fact_check",
        "patterns": [
            r"\bfact[- ]?check\b",
            r"\bverify claims?\b",
            r"\bsourced\b",
            r"\bsources?\b",
            r"\blandscape\b",
            r"\bcompetitor report\b",
        ],
        "terms": ["fact_check", "verification", "sources", "evidence", "research", "brief"],
    },
    {
        "intent": "social_creator",
        "patterns": [
            r"\bcreator-style\b",
            r"\bsocial channels?\b",
            r"\bengagement routine\b",
            r"\bposting plan\b",
            r"\bcontent calendar\b",
            r"\brepurpose\b.*\bsocial posts?\b",
            r"\blinkedin\b.*\bx\b",
            r"\bsocial posts?\b",
        ],
        "terms": ["social_media", "posting", "engagement", "creator", "content_calendar", "audience", "repurpose", "linkedin", "x"],
    },
]

INTENT_SKILL_PRIORS = {
    "entity_authority": {"seo": 1.0, "seo-coral": 0.65, "researcher": 0.2, "marketing": 0.15},
    "site_reputation_abuse": {"seo": 1.05, "seo-coral": 0.7, "researcher": 0.15},
    "javascript_ai_systems": {"dejan-ai-reverse-engineering": 1.05, "seo": 0.9, "seo-coral": 0.55, "developer": 0.25},
    "multilingual_ai_systems": {"seo": 1.0, "seo-coral": 0.65, "researcher": 0.2, "marketing": 0.1},
    "canonicalization": {"seo": 1.0, "seo-coral": 0.65, "developer": 0.2},
    "technical_seo": {"seo": 0.95, "seo-coral": 0.6, "developer": 0.2},
    "recovery": {"seo": 0.8, "seo-coral": 0.45, "researcher": 0.15},
    "ai_overviews": {"seo": 0.6, "seo-coral": 0.35, "dejan-ai-reverse-engineering": 0.25, "ahrefs": 0.12},
    "ai_visibility": {"seo": 0.7, "seo-coral": 0.45, "ahrefs": 0.35, "marketing": 0.15},
    "ai_selection": {"dejan-ai-reverse-engineering": 1.95, "seo": 0.2},
    "fan_out": {"dejan-ai-reverse-engineering": 0.9, "seo": 0.25},
    "leak_systems": {"seo": 0.55},
    "content_writing": {"writer": 0.8, "writer-plankton": 0.6, "seo": 0.2},
    "distribution_ops": {"marketing": 1.15, "marketing-current": 0.8, "charles": 0.35, "writer": 0.1},
    "code_review": {"reviewer": 1.35, "reviewer-barnacle": 1.05, "developer": 0.15, "qa": 0.1},
    "support_triage": {"support-anemone": 1.6, "support": 0.2, "operations": 0.15},
    "implementation_review": {"developer": 1.0, "developer-chitin": 0.7, "reviewer": 0.45, "qa": 0.35},
    "coordination": {"orchestrator-pinchy": 1.9, "operations": 0.7, "multi-agent-reef": 0.55},
    "fact_check": {"researcher": 1.25, "researcher-kelp": 0.95, "writer": 0.15},
    "social_creator": {"charles": 1.2, "marketing": 0.5, "marketing-current": 0.35},
}

ROLE_INTENT_SKILL_PRIORS = {
    ("pinchy", "coordination"): {
        "orchestrator-pinchy": 5.9,
        "operations": 1.25,
        "multi-agent-reef": 0.9,
    },
}

INTENT_VARIANT_PREFERENCES = {
    "ai_selection": [("seo", "dejan-ai-reverse-engineering")],
    "support_triage": [("support", "support-anemone")],
}

OPENAI_QUERY_HINTS = {"openai", "chatgpt", "api", "gpt", "responses", "assistants", "model", "models"}
FRESHNESS_QUERY_HINTS = {"latest", "current", "recent", "fresh", "monitor", "monitoring", "new", "today"}
EVIDENCE_QUERY_HINTS = {"evidence", "consensus", "conflict", "compare", "comparison", "vs", "versus", "dispute"}
AI_SELECTION_DIAGNOSTIC_HINTS = {
    "diagnose",
    "diagnosis",
    "selected",
    "selection_rate",
    "answer_selection",
    "answer_inclusion",
    "citation_diagnostics",
    "grounding",
    "grounding_snippets",
    "cited",
    "snippet_extractability",
}
COORDINATION_SUPPORT_SKILLS = {"orchestrator-pinchy", "operations", "multi-agent-reef"}
AI_VISIBILITY_CANON_PATHS = (
    "seo/memory/ahrefs-ai-visibility-guide.md",
    "seo/memory/ahrefs-google-ai-overviews-guide.md",
    "seo/memory/seo-source-canon-2026.md",
    "seo/memory/dejan-ai-reverse-engineering-pack.md",
)
BROAD_SYNTHESIS_QUERY_HINTS = {
    "what",
    "how",
    "why",
    "overview",
    "guide",
    "workflow",
    "playbook",
    "framework",
    "recovery",
    "recover",
    "diagnosis",
    "diagnose",
    "triage",
    "debug",
    "debugging",
    "system",
    "systems",
    "canonical",
    "indexing",
    "crawl",
    "rendering",
    "robots",
    "noindex",
    "hcu",
}
SPECIFIC_EVIDENCE_QUERY_HINTS = {
    "source",
    "sources",
    "article",
    "articles",
    "post",
    "posts",
    "case",
    "cases",
    "example",
    "examples",
    "quote",
    "quotes",
    "gsqi",
    "glenn",
    "gabe",
    "ahrefs",
    "dejan",
    "marie",
    "brodie",
    "patrick",
    "yoast",
    "screamingfrog",
    "semrush",
    "moz",
    "sistrix",
    "google",
}
GLOBAL_BUCKET = "__all__"
RESULT_SCORE_FIELDS = (
    "goal_fit_score",
    "correctness_score",
    "clarity_score",
    "completeness_score",
    "actionability_score",
    "format_score",
)
RESULT_SCORE_WEIGHTS = {
    "goal_fit_score": 0.22,
    "correctness_score": 0.24,
    "clarity_score": 0.18,
    "completeness_score": 0.16,
    "actionability_score": 0.12,
    "format_score": 0.08,
}
RESULT_VERDICT_BANDS = [
    (4.5, "excellent"),
    (4.0, "strong"),
    (3.2, "acceptable"),
    (2.4, "weak"),
    (0.0, "poor"),
]
RESULT_MODE_WEIGHTS = {
    "manual": 1.0,
    "suggested": 0.4,
}
RESULT_VERDICT_SIGNAL = {
    "excellent": 0.12,
    "strong": 0.06,
    "acceptable": 0.0,
    "weak": -0.08,
    "poor": -0.14,
}
RESULT_STATUS_SIGNAL = {
    "accepted": 0.05,
    "revised": 0.0,
    "failed": -0.08,
}
RESULT_POSITIVE_NOTE_TERMS = {
    "clear": 0.1,
    "good": 0.08,
    "great": 0.1,
    "right": 0.08,
    "sharp": 0.1,
    "solid": 0.08,
    "strong": 0.12,
    "useful": 0.1,
}
RESULT_NEGATIVE_NOTE_TERMS = {
    "confusing": -0.18,
    "incorrect": -0.28,
    "missed": -0.2,
    "needed": -0.08,
    "noisy": -0.12,
    "thin": -0.16,
    "tighten": -0.12,
    "unclear": -0.2,
    "weak": -0.18,
    "wrong": -0.3,
}
SUGGESTION_STOPWORDS = {
    "need",
    "plan",
    "help",
    "and",
    "with",
    "from",
    "that",
    "this",
    "into",
    "your",
    "our",
    "their",
    "they",
    "them",
    "what",
    "when",
    "where",
    "which",
    "while",
    "for",
    "would",
    "should",
    "could",
    "about",
    "using",
    "used",
    "more",
    "best",
    "better",
    "than",
    "have",
    "make",
    "made",
    "like",
    "just",
    "page",
    "pages",
    "site",
    "sites",
    "domain",
    "mode",
    "query",
    "queries",
    "task",
    "tasks",
    "squad",
    "search",
    "reverse",
    "engineering",
    "style",
}

SKILL_ALIASES = {
    "orchestrator-pinchy": ["pinchy", "orchestrator", "chief_of_staff", "coordination"],
    "seo": ["coral", "seo", "search", "organic", "rankings", "visibility"],
    "seo-coral": ["coral", "seo", "search", "organic", "rankings", "visibility"],
    "ahrefs": ["ahrefs", "backlinks", "refdomains", "traffic_value", "keyword_gap"],
    "dejan-ai-reverse-engineering": [
        "dejan",
        "dan_petrovic",
        "reverse_engineering",
        "ai_mode",
        "grounding",
        "grounding_snippets",
        "snippet_extraction",
        "selection_rate",
        "selection",
        "selected",
        "cited",
        "citations",
        "answer_inclusion",
        "sro",
        "fan_out",
        "machine_readability",
        "primary_bias",
    ],
    "programmatic-seo": ["programmatic", "pseo", "template_pages", "scale_pages"],
    "writer": ["plankton", "writer", "copywriting", "blog", "landing_page", "email"],
    "writer-plankton": ["plankton", "writer", "copywriting", "blog", "landing_page", "email"],
    "charles": ["charles", "social", "social_media", "threads", "linkedin", "tiktok", "youtube"],
    "marketing": ["current", "marketing", "growth", "distribution", "promotion", "campaigns"],
    "marketing-current": ["current", "marketing", "growth", "distribution", "promotion", "campaigns"],
    "developer": ["chitin", "developer", "code", "implementation", "bugfix", "feature"],
    "developer-chitin": ["chitin", "developer", "code", "implementation", "bugfix", "feature"],
    "devops": ["tide", "devops", "deployment", "infra", "infrastructure", "pipeline"],
    "devops-tide": ["tide", "devops", "deployment", "infra", "infrastructure", "pipeline"],
    "qa": ["reef", "qa", "testing", "regression", "verification", "pass_fail"],
    "qa-reef": ["reef", "qa", "testing", "regression", "verification", "pass_fail"],
    "researcher": ["kelp", "research", "context", "fact_check", "sources"],
    "researcher-kelp": ["kelp", "research", "context", "fact_check", "sources"],
    "reviewer": ["barnacle", "review", "code_review", "quality_gate", "request_changes"],
    "reviewer-barnacle": ["barnacle", "review", "code_review", "quality_gate", "request_changes"],
    "support": ["anemone", "support", "tickets", "triage", "customer_issue"],
    "support-anemone": ["anemone", "support", "tickets", "triage", "customer_issue"],
    "operations": ["urchin", "operations", "project_management", "status", "timeline"],
    "operations-urchin": ["urchin", "operations", "project_management", "status", "timeline"],
    "finance": ["krill", "finance", "invoice", "cash_flow", "expenses"],
    "finance-krill": ["krill", "finance", "invoice", "cash_flow", "expenses"],
    "emily": ["emily", "design", "graphic_design", "visuals", "brand_design", "ui"],
    "multi-agent-reef": ["multi_agent", "orchestration", "handoff", "workflow", "specialists"],
}


@dataclasses.dataclass
class DocChunk:
    chunk_id: str
    path: str
    skill: str
    file_type: str
    heading: str
    text: str
    section_kind: str
    source: str
    published_on: str
    freshness: float
    topics: List[str] = dataclasses.field(default_factory=list)
    intents: List[str] = dataclasses.field(default_factory=list)
    use_for: List[str] = dataclasses.field(default_factory=list)
    avoid_for: List[str] = dataclasses.field(default_factory=list)
    confidence: str = ""
    tags: List[str] = dataclasses.field(default_factory=list)
    roles: List[str] = dataclasses.field(default_factory=list)
    is_canonical: bool = False
    canonical_group: str = ""
    bundles: List[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class SquadRouter:
    skill_tags: Dict[str, List[str]]
    role_paths: Dict[str, List[str]]
    path_bundles: Dict[str, List[str]]


@dataclasses.dataclass
class TaskPack:
    pack_id: str
    name: str
    description: str
    roles: List[str]
    intents: List[str]
    keywords: List[str]
    primary_skill: str
    supporting_skills: List[str]
    memory_focus: List[str]
    checklist: List[str]
    deliverables: List[str]
    output_sections: List[str]
    handoffs: List[str]
    escalation_rules: List[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hybrid memory retriever for Codex skills")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build or rebuild the local index")
    build.add_argument("--root", default=str(SKILLS_ROOT))
    build.add_argument("--db", default=str(DB_PATH))

    query = subparsers.add_parser("query", help="Query memory chunks")
    query.add_argument("text", help="Query text")
    query.add_argument("--db", default=str(DB_PATH))
    query.add_argument("--top", type=int, default=8)
    query.add_argument("--role", help="Optional squad role, e.g. pinchy, coral")
    query.add_argument("--skill", help="Optional skill filter")
    query.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    decide = subparsers.add_parser("decide", help="Suggest skills and memory for a task")
    decide.add_argument("text", help="Task or user request")
    decide.add_argument("--db", default=str(DB_PATH))
    decide.add_argument("--top", type=int, default=5)
    decide.add_argument("--role", help="Optional squad role, e.g. pinchy, coral")
    decide.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    pinchy = subparsers.add_parser("pinchy", help="Produce a Pinchy-style action plan")
    pinchy.add_argument("text", help="Task or user request")
    pinchy.add_argument("--db", default=str(DB_PATH))
    pinchy.add_argument("--top", type=int, default=5)
    pinchy.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    task_pack = subparsers.add_parser("task-pack", help="Resolve the best reusable task pack for a request")
    task_pack.add_argument("text", help="Task or user request")
    task_pack.add_argument("--db", default=str(DB_PATH))
    task_pack.add_argument("--top", type=int, default=5)
    task_pack.add_argument("--role", help="Optional squad role, e.g. pinchy, coral")
    task_pack.add_argument("--pack-id", help="Optional explicit task pack id override")
    task_pack.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    task_pack.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    execute_plan = subparsers.add_parser("execute-plan", help="Build an execution plan from the best task pack")
    execute_plan.add_argument("text", help="Task or user request")
    execute_plan.add_argument("--db", default=str(DB_PATH))
    execute_plan.add_argument("--top", type=int, default=5)
    execute_plan.add_argument("--role", help="Optional squad role, e.g. pinchy, coral")
    execute_plan.add_argument("--pack-id", help="Optional explicit task pack id override")
    execute_plan.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    execute_plan.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    complete_task = subparsers.add_parser("complete-task", help="Record the outcome of a completed task pack run")
    complete_task.add_argument("text", help="Original task or request text")
    complete_task.add_argument("--db", default=str(DB_PATH))
    complete_task.add_argument("--top", type=int, default=5)
    complete_task.add_argument("--role", help="Optional squad role, e.g. pinchy, coral")
    complete_task.add_argument("--pack-id", help="Optional explicit task pack id override")
    complete_task.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    complete_task.add_argument("--status", choices=["accepted", "revised", "failed"], required=True)
    complete_task.add_argument("--revision-count", type=int, default=0)
    complete_task.add_argument("--completion-minutes", type=float)
    complete_task.add_argument("--user-rating", type=float)
    complete_task.add_argument("--notes", default="")
    complete_task.add_argument("--used-path", action="append", dest="used_paths")
    complete_task.add_argument("--used-skill", action="append", dest="used_skills")
    complete_task.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    run_pack = subparsers.add_parser("run-pack", help="Start a tracked execution run from the best task pack")
    run_pack.add_argument("text", help="Original task or request text")
    run_pack.add_argument("--db", default=str(DB_PATH))
    run_pack.add_argument("--top", type=int, default=5)
    run_pack.add_argument("--role", help="Optional squad role, e.g. pinchy, coral")
    run_pack.add_argument("--pack-id", help="Optional explicit task pack id override")
    run_pack.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    run_pack.add_argument("--status", choices=["planned", "active", "blocked"], default="active")
    run_pack.add_argument("--notes", default="")
    run_pack.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    run_step = subparsers.add_parser("run-step", help="Update a step inside an active pack run")
    run_step.add_argument("run_id", type=int)
    run_step.add_argument("step_seq", type=int)
    run_step.add_argument("--db", default=str(DB_PATH))
    run_step.add_argument("--status", choices=["pending", "active", "completed", "blocked", "skipped"], required=True)
    run_step.add_argument("--owner-skill")
    run_step.add_argument("--notes", default="")
    run_step.add_argument("--artifact-path", default="")
    run_step.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    run_handoff = subparsers.add_parser("run-handoff", help="Record a specialist handoff during a pack run")
    run_handoff.add_argument("run_id", type=int)
    run_handoff.add_argument("--db", default=str(DB_PATH))
    run_handoff.add_argument("--from-skill", required=True)
    run_handoff.add_argument("--to-skill", required=True)
    run_handoff.add_argument("--reason", default="")
    run_handoff.add_argument("--notes", default="")
    run_handoff.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    run_blocker = subparsers.add_parser("run-blocker", help="Create or resolve a blocker for a pack run")
    run_blocker.add_argument("run_id", type=int)
    run_blocker.add_argument("--db", default=str(DB_PATH))
    run_blocker.add_argument("--blocker-id", type=int)
    run_blocker.add_argument("--step-seq", type=int)
    run_blocker.add_argument("--title", default="")
    run_blocker.add_argument("--severity", choices=["low", "medium", "high", "critical"], default="medium")
    run_blocker.add_argument("--owner-skill")
    run_blocker.add_argument("--status", choices=["open", "resolved"], default="open")
    run_blocker.add_argument("--notes", default="")
    run_blocker.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    run_report = subparsers.add_parser("run-report", help="Show active and recent pack execution runs")
    run_report.add_argument("--db", default=str(DB_PATH))
    run_report.add_argument("--limit", type=int, default=10)
    run_report.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    run_report.add_argument("--status", choices=["planned", "active", "blocked", "completed", "failed"])
    run_report.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    score_task = subparsers.add_parser("score-task", help="Record or update a structured quality scorecard for a completed task outcome")
    score_task.add_argument("outcome_id", type=int, help="Task outcome id from complete-task")
    score_task.add_argument("--db", default=str(DB_PATH))
    score_task.add_argument("--goal-fit", dest="goal_fit_score", type=float)
    score_task.add_argument("--correctness", dest="correctness_score", type=float)
    score_task.add_argument("--clarity", dest="clarity_score", type=float)
    score_task.add_argument("--completeness", dest="completeness_score", type=float)
    score_task.add_argument("--actionability", dest="actionability_score", type=float)
    score_task.add_argument("--format", dest="format_score", type=float)
    score_task.add_argument("--scorer", default="manual")
    score_task.add_argument("--mode", choices=["manual", "suggested"], default="manual")
    score_task.add_argument("--notes", default="")
    score_task.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    feedback = subparsers.add_parser("feedback", help="Record retrieval feedback for a query")
    feedback.add_argument("query", help="Original query text")
    feedback.add_argument("path", help="Path that was useful or not useful")
    feedback.add_argument("--db", default=str(DB_PATH))
    feedback.add_argument("--rating", choices=["useful", "not_useful"], required=True)

    logs = subparsers.add_parser("logs", help="Show recent query logs")
    logs.add_argument("--db", default=str(DB_PATH))
    logs.add_argument("--limit", type=int, default=20)

    train = subparsers.add_parser("train", help="Train learned path and skill priors from query logs and feedback")
    train.add_argument("--db", default=str(DB_PATH))
    train.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    report = subparsers.add_parser("report", help="Show usage-learning report for the squad memory index")
    report.add_argument("--db", default=str(DB_PATH))
    report.add_argument("--limit", type=int, default=10)
    report.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    pack_train = subparsers.add_parser("pack-train", help="Train learned pack priors from completed task outcomes")
    pack_train.add_argument("--db", default=str(DB_PATH))
    pack_train.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    pack_report = subparsers.add_parser("pack-report", help="Show pack outcome report with top packs, weak packs, and pack-level note patterns")
    pack_report.add_argument("--db", default=str(DB_PATH))
    pack_report.add_argument("--limit", type=int, default=10)
    pack_report.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    pack_report.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    outcome_train = subparsers.add_parser("outcome-train", help="Train note and skill priors from completed task outcomes")
    outcome_train.add_argument("--db", default=str(DB_PATH))
    outcome_train.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    outcome_report = subparsers.add_parser(
        "outcome-report",
        help="Show real-task outcome telemetry including strong notes, weak notes, skill stacks, and over-ranked paths",
    )
    outcome_report.add_argument("--db", default=str(DB_PATH))
    outcome_report.add_argument("--limit", type=int, default=10)
    outcome_report.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    outcome_report.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    task_result_report = subparsers.add_parser(
        "task-result-report",
        help="Show structured output-quality scorecards, pending reviews, and scored pack/path/skill summaries",
    )
    task_result_report.add_argument("--db", default=str(DB_PATH))
    task_result_report.add_argument("--limit", type=int, default=10)
    task_result_report.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    task_result_report.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    task_evaluate = subparsers.add_parser(
        "task-eval",
        help="Run full task-pack evaluation against end-to-end task fixtures",
    )
    task_evaluate.add_argument("--db", default=str(DB_PATH))
    task_evaluate.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    task_evaluate.add_argument(
        "--fixtures",
        default=str(TASK_EVAL_FIXTURES_PATH),
        help="Path to task-evaluation fixture JSON",
    )
    task_evaluate.add_argument("--top", type=int, default=5)
    task_evaluate.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    result_train = subparsers.add_parser(
        "result-train",
        help="Train pack, note, and skill priors from structured task-result scorecards",
    )
    result_train.add_argument("--db", default=str(DB_PATH))
    result_train.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    episode_build = subparsers.add_parser(
        "episode-build",
        help="Consolidate event history into episodic task/session memory",
    )
    episode_build.add_argument("--db", default=str(DB_PATH))
    episode_build.add_argument("--gap-minutes", type=int, default=EPISODE_GAP_MINUTES)
    episode_build.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    episode_report = subparsers.add_parser(
        "episode-report",
        help="Show recent episodic memory sessions built from the live event bus",
    )
    episode_report.add_argument("--db", default=str(DB_PATH))
    episode_report.add_argument("--limit", type=int, default=10)
    episode_report.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    workspace_sync = subparsers.add_parser(
        "workspace-sync",
        help="Sync transient workspace files into the active runtime context layer",
    )
    workspace_sync.add_argument("name", help="Human-readable workspace context name")
    workspace_sync.add_argument("--db", default=str(DB_PATH))
    workspace_sync.add_argument("--path", action="append", dest="paths", required=True, help="File or directory to include")
    workspace_sync.add_argument("--role", help="Optional role affinity, e.g. pinchy or coral")
    workspace_sync.add_argument("--pack-id", help="Optional task pack affinity")
    workspace_sync.add_argument("--notes", default="")
    workspace_sync.add_argument("--max-files", type=int, default=WORKSPACE_MAX_FILES)
    workspace_sync.add_argument("--max-chars", type=int, default=WORKSPACE_MAX_CHARS)
    workspace_sync.add_argument("--replace", action="store_true", help="Replace any existing active context with the same scope key")
    workspace_sync.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    workspace_clear = subparsers.add_parser(
        "workspace-clear",
        help="Archive or delete active transient workspace contexts",
    )
    workspace_clear.add_argument("--db", default=str(DB_PATH))
    workspace_clear.add_argument("--context-id", type=int)
    workspace_clear.add_argument("--name", help="Workspace context name")
    workspace_clear.add_argument("--all-active", action="store_true", help="Clear all active workspace contexts")
    workspace_clear.add_argument("--delete", action="store_true", help="Delete rows instead of archiving them")
    workspace_clear.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    workspace_report = subparsers.add_parser(
        "workspace-report",
        help="Show active workspace-aware context and the most relevant synced files",
    )
    workspace_report.add_argument("--db", default=str(DB_PATH))
    workspace_report.add_argument("--limit", type=int, default=10)
    workspace_report.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    suggest = subparsers.add_parser("suggest-metadata", help="Suggest frontmatter updates from usage patterns")
    suggest.add_argument("--db", default=str(DB_PATH))
    suggest.add_argument("--path", help="Optional single path to inspect")
    suggest.add_argument("--limit", type=int, default=8)
    suggest.add_argument("--min-useful", type=int, default=1)
    suggest.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    evaluate = subparsers.add_parser("eval", help="Run retrieval evaluation against fixture queries")
    evaluate.add_argument("--db", default=str(DB_PATH))
    evaluate.add_argument(
        "--fixtures",
        default=str(HOME / "squad_memory" / "evals" / "fixtures.json"),
        help="Path to evaluation fixture JSON",
    )
    evaluate.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    return parser.parse_args()


def tokenize(text: str) -> List[str]:
    return TOKEN_RE.findall(text.lower())


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "root"


def title_from_slug(text: str) -> str:
    value = re.sub(r"[_\-]+", " ", text).strip()
    return value.title() if value else "Untitled"


def compact_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def truncate_text(text: str, limit: int = 96) -> str:
    value = compact_whitespace(text)
    if len(value) <= limit:
        return value
    return value[: max(0, limit - 3)].rstrip() + "..."


def workspace_scope_key(name: str, paths: Sequence[Path], role: Optional[str], pack_id: Optional[str]) -> str:
    normalized_paths = sorted(str(path.expanduser().resolve()) for path in paths)
    seed = json.dumps(
        {
            "name": slugify(name),
            "paths": normalized_paths,
            "role": role or "",
            "pack_id": pack_id or "",
        },
        sort_keys=True,
        ensure_ascii=True,
    )
    return hashlib.sha1(seed.encode("utf-8")).hexdigest()[:20]


def common_root_path(paths: Sequence[Path]) -> str:
    resolved = [str(path.expanduser().resolve()) for path in paths if path.exists()]
    if not resolved:
        return ""
    try:
        return os.path.commonpath(resolved)
    except ValueError:
        return str(Path(resolved[0]).parent)


def workspace_should_skip_dir(name: str) -> bool:
    return name.startswith(".") and name not in {".github"} or name in WORKSPACE_IGNORED_DIRS


def is_workspace_text_file(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.suffix.lower() in WORKSPACE_TEXT_EXTENSIONS:
        return True
    try:
        sample = path.read_bytes()[:2048]
    except OSError:
        return False
    if b"\x00" in sample:
        return False
    return True


def discover_workspace_files(paths: Sequence[Path], max_files: int) -> List[Path]:
    files: List[Path] = []
    seen = set()
    for raw_path in paths:
        path = raw_path.expanduser().resolve()
        if not path.exists():
            continue
        if path.is_file():
            if is_workspace_text_file(path) and str(path) not in seen:
                files.append(path)
                seen.add(str(path))
            if len(files) >= max_files:
                break
            continue
        for root, dirs, filenames in os.walk(path):
            dirs[:] = [name for name in sorted(dirs) if not workspace_should_skip_dir(name)]
            for filename in sorted(filenames):
                file_path = Path(root) / filename
                if not is_workspace_text_file(file_path):
                    continue
                key = str(file_path)
                if key in seen:
                    continue
                files.append(file_path)
                seen.add(key)
                if len(files) >= max_files:
                    return files
    return files


def safe_read_workspace_text(path: Path, max_chars: int) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    text = text.replace("\r\n", "\n")
    if len(text) > max_chars:
        text = text[:max_chars]
    return text.strip()


def workspace_item_title(path: Path, text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()[:120] or path.name
        return stripped[:120]
    return path.name


def safe_json_object(value: str) -> Dict[str, Any]:
    raw = str(value or "").strip()
    if not raw:
        return {}
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def chunk_id_for(rel_path: str, heading: str, index: int, body: str) -> str:
    digest = hashlib.sha1(body.encode("utf-8")).hexdigest()[:10]
    return f"{rel_path}::{slugify(heading)}::{index}::{digest}"


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    header = text[4:end].strip()
    body = text[end + 4 :].lstrip("\n")
    meta = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body


def doc_type_for(path: Path) -> str:
    if path.name == "SQUAD_MEMORY.md":
        return "squad_router"
    if path.name == "INDEX.md":
        return "memory_index"
    if path.name == "SKILL.md":
        return "skill_contract"
    if path.name == "MEMORY.md":
        return "memory_router"
    if path.parent.name == "references":
        return "reference_note"
    if path.parent.name == "memory":
        return "memory_note"
    return "skill_doc"


def parse_tags(meta: Dict[str, str]) -> List[str]:
    tags_value = meta.get("tags", "")
    if not tags_value:
        return []
    return [tag.strip().lower() for tag in tags_value.split(",") if tag.strip()]


def parse_meta_list(meta: Dict[str, str], *keys: str) -> List[str]:
    values: List[str] = []
    for key in keys:
        raw = meta.get(key, "")
        if not raw:
            continue
        values.extend(part.strip().lower() for part in raw.split(",") if part.strip())
    return sorted(set(values))


def parse_meta_bool(meta: Dict[str, str], key: str) -> bool:
    return meta.get(key, "").strip().lower() in {"1", "true", "yes", "y"}


def canonical_info_for_doc(rel_path: str, meta: Dict[str, str], canonical_map: Dict[str, str], topics: List[str], title: str) -> Tuple[bool, str]:
    canonical_group = canonical_map.get(rel_path, "").strip()
    if canonical_group:
        return True, canonical_group
    if parse_meta_bool(meta, "canonical"):
        meta_group = meta.get("canonical_group", "").strip()
        if meta_group:
            return True, meta_group
        if topics:
            return True, topics[0].replace("_", " ")
        if title:
            return True, title
        return True, Path(rel_path).stem.replace("-", " ")
    return False, ""


def load_phase7_registry(path: Path = PHASE7_REGISTRY_PATH) -> Dict[str, Dict[str, object]]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    notes = payload.get("notes", {})
    return notes if isinstance(notes, dict) else {}


def load_phase10_ledger(path: Path = PHASE10_LEDGER_PATH) -> Dict[str, Dict[str, object]]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    primary_paths = payload.get("primary_paths", {})
    return primary_paths if isinstance(primary_paths, dict) else {}


@lru_cache(maxsize=8)
def cached_phase7_registry(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase7_registry(Path(path_str))


@lru_cache(maxsize=8)
def cached_phase10_ledger(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase10_ledger(Path(path_str))


def load_phase11_ledgers(directory: Path = PHASE11_LEDGER_DIR) -> Dict[str, Dict[str, object]]:
    if not directory.exists():
        return {}
    merged: Dict[str, Dict[str, object]] = {}
    for path in sorted(directory.glob("*_evidence_ledger.json")):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        primary_paths = payload.get("primary_paths", {})
        if not isinstance(primary_paths, dict):
            continue
        for rel_path, value in primary_paths.items():
            if isinstance(value, dict):
                merged[rel_path] = value
    return merged


def load_phase12_ledgers(directory: Path = PHASE12_LEDGER_DIR) -> Dict[str, Dict[str, object]]:
    if not directory.exists():
        return {}
    merged: Dict[str, Dict[str, object]] = {}
    for path in sorted(directory.glob("*_external_evidence_ledger.json")):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        primary_paths = payload.get("primary_paths", {})
        if not isinstance(primary_paths, dict):
            continue
        for rel_path, value in primary_paths.items():
            if isinstance(value, dict):
                merged[rel_path] = value
    return merged


def load_phase16_ledgers(directory: Path = PHASE16_LEDGER_DIR) -> Dict[str, Dict[str, object]]:
    if not directory.exists():
        return {}
    merged: Dict[str, Dict[str, object]] = {}
    for path in sorted(directory.glob("*_evidence_ledger.json")):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        primary_paths = payload.get("primary_paths", {})
        if not isinstance(primary_paths, dict):
            continue
        for rel_path, value in primary_paths.items():
            if isinstance(value, dict):
                merged[rel_path] = value
    return merged


def load_phase17_ledgers(directory: Path = PHASE17_LEDGER_DIR) -> Dict[str, Dict[str, object]]:
    if not directory.exists():
        return {}
    merged: Dict[str, Dict[str, object]] = {}
    for path in sorted(directory.glob("*_evidence_ledger.json")):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        primary_paths = payload.get("primary_paths", {})
        if not isinstance(primary_paths, dict):
            continue
        for rel_path, value in primary_paths.items():
            if isinstance(value, dict):
                merged[rel_path] = value
    return merged


def load_phase23_ledgers(directory: Path = PHASE23_LEDGER_DIR) -> Dict[str, Dict[str, object]]:
    if not directory.exists():
        return {}
    merged: Dict[str, Dict[str, object]] = {}
    for path in sorted(directory.glob("*_evidence_ledger.json")):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        primary_paths = payload.get("primary_paths", {})
        if not isinstance(primary_paths, dict):
            continue
        for rel_path, value in primary_paths.items():
            if isinstance(value, dict):
                merged[rel_path] = value
    return merged


def load_phase24_ledgers(directory: Path = PHASE24_LEDGER_DIR) -> Dict[str, Dict[str, object]]:
    if not directory.exists():
        return {}
    merged: Dict[str, Dict[str, object]] = {}
    for path in sorted(directory.glob("*_evidence_ledger.json")):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        primary_paths = payload.get("primary_paths", {})
        if not isinstance(primary_paths, dict):
            continue
        for rel_path, value in primary_paths.items():
            if isinstance(value, dict):
                merged[rel_path] = value
    return merged


def load_phase25_ledgers(directory: Path = PHASE25_LEDGER_DIR) -> Dict[str, Dict[str, object]]:
    if not directory.exists():
        return {}
    merged: Dict[str, Dict[str, object]] = {}
    for path in sorted(directory.glob("*_evidence_ledger.json")):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        primary_paths = payload.get("primary_paths", {})
        if not isinstance(primary_paths, dict):
            continue
        for rel_path, value in primary_paths.items():
            if isinstance(value, dict):
                merged[rel_path] = value
    return merged


@lru_cache(maxsize=8)
def cached_phase11_ledgers(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase11_ledgers(Path(path_str))


@lru_cache(maxsize=8)
def cached_phase12_ledgers(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase12_ledgers(Path(path_str))


@lru_cache(maxsize=8)
def cached_phase16_ledgers(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase16_ledgers(Path(path_str))


@lru_cache(maxsize=8)
def cached_phase17_ledgers(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase17_ledgers(Path(path_str))


@lru_cache(maxsize=8)
def cached_phase23_ledgers(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase23_ledgers(Path(path_str))


@lru_cache(maxsize=8)
def cached_phase24_ledgers(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase24_ledgers(Path(path_str))


@lru_cache(maxsize=8)
def cached_phase25_ledgers(path_str: str, mtime_ns: int, size: int) -> Dict[str, Dict[str, object]]:
    return load_phase25_ledgers(Path(path_str))


def phase7_registry_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    status = str(entry.get("status", "")).strip()
    if not status:
        return 0.0
    freshness_query = bool(query_tokens & FRESHNESS_QUERY_HINTS)
    if status == "canonical_primary":
        return 0.05
    if status == "canonical_secondary":
        return 0.02
    if status == "orphan_primary":
        return 0.03
    if status == "merge_candidate":
        return -0.03
    if status == "orphan_supporting":
        return -0.01
    if status == "monitor_canon":
        return 0.04 if freshness_query else -0.04
    if status == "monitor_raw":
        return 0.02 if freshness_query else -0.08
    if status == "stale_legacy_feed":
        return -0.28
    return 0.0


def phase10_evidence_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    source_count = int(entry.get("source_count", 0) or 0)
    tension = entry.get("tension", [])
    tension_count = len(tension) if isinstance(tension, list) else 0

    score = min(confidence * 0.045, 0.05) + min(freshness * 0.025, 0.03) + min(source_count * 0.01, 0.03)
    if query_tokens & EVIDENCE_QUERY_HINTS:
        score += min(tension_count * 0.018, 0.05)
    if query_tokens & FRESHNESS_QUERY_HINTS:
        score += min(freshness * 0.02, 0.02)
    return round(score, 4)


def phase11_domain_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    evidence_count = int(entry.get("evidence_count", 0) or 0)
    score = min(confidence * 0.03, 0.035) + min(freshness * 0.015, 0.015) + min(evidence_count * 0.004, 0.02)
    if query_tokens & {"draft", "outline", "landing", "copy", "newsletter", "distribution", "launch", "repurpose", "hook"}:
        score += 0.015
    return round(score, 4)


def phase12_domain_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    source_count = int(entry.get("source_count", 0) or 0)
    topic = str(entry.get("topic", "")).strip()
    domain = str(entry.get("domain", "")).strip()

    research_hint_tokens = {
        "recent",
        "fresh",
        "example",
        "examples",
        "research",
        "monitor",
        "monitoring",
        "trend",
        "trends",
        "source",
        "sources",
        "study",
        "studies",
        "editorial",
        "voice",
        "hooks",
        "distribution",
        "campaign",
        "channel",
        "social",
        "newsletter",
    }
    writer_tokens = {"writer", "writing", "draft", "copy", "voice", "hook", "hooks", "editorial", "landing", "email"}
    marketing_tokens = {"marketing", "distribution", "launch", "campaign", "channel", "social", "newsletter", "repurpose"}
    documentation_authoring_tokens = {
        "documentation",
        "docs",
        "guide",
        "guides",
        "instruction",
        "instructions",
        "setup",
        "walkthrough",
        "troubleshooting",
        "checks",
        "steps",
        "product",
    }

    score = min(confidence * 0.04, 0.05) + min(freshness * 0.03, 0.03) + min(source_count * 0.01, 0.04)
    research_query = bool(query_tokens & research_hint_tokens)
    if research_query:
        score += 0.03
    if research_query and domain == "writer" and query_tokens & writer_tokens:
        score += 0.02
    if research_query and domain == "marketing" and query_tokens & marketing_tokens:
        score += 0.02
    if domain == "writer" and query_tokens & documentation_authoring_tokens:
        score += 0.05
    if topic in {"writer_external_sources", "marketing_external_sources"} and query_tokens & FRESHNESS_QUERY_HINTS:
        score += 0.02
    return round(score, 4)


def phase16_domain_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    evidence_count = int(entry.get("evidence_count", 0) or 0)
    topic = str(entry.get("topic", "")).strip()

    social_tokens = {
        "social",
        "creator",
        "engagement",
        "community",
        "posting",
        "platform",
        "platforms",
        "linkedin",
        "instagram",
        "tiktok",
        "reel",
        "reels",
        "carousel",
        "carousels",
        "thread",
        "threads",
        "reply",
        "replies",
        "calendar",
        "trend",
        "trends",
        "audience",
        "x",
    }
    charles_hint_tokens = {
        "hook",
        "hooks",
        "post",
        "posts",
        "dm",
        "dms",
        "comment",
        "comments",
        "native",
        "repurpose",
        "repurposing",
    }
    support_tokens = {
        "support",
        "ticket",
        "tickets",
        "severity",
        "billing",
        "customer",
        "customers",
        "troubleshoot",
        "troubleshooting",
        "issue",
        "issues",
    }

    score = min(confidence * 0.035, 0.04) + min(freshness * 0.02, 0.02) + min(evidence_count * 0.006, 0.025)
    if query_tokens & support_tokens:
        score -= 0.25
    if query_tokens & social_tokens:
        score += 0.03
    if query_tokens & charles_hint_tokens:
        score += 0.02
    if topic == "charles_core" and query_tokens & {"social", "creator", "engagement", "posting", "calendar"}:
        score += 0.025
    return round(score, 4)


def phase17_domain_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    source_count = int(entry.get("source_count", 0) or 0)
    topic = str(entry.get("topic", "")).strip()

    research_tokens = {
        "fresh",
        "recent",
        "example",
        "examples",
        "research",
        "monitor",
        "monitoring",
        "source",
        "sources",
        "platform",
        "platforms",
        "change",
        "changes",
        "trend",
        "trends",
        "creator",
    }
    social_tokens = {
        "social",
        "creator",
        "linkedin",
        "instagram",
        "tiktok",
        "youtube",
        "x",
        "threads",
        "posting",
        "repurpose",
        "repurposing",
        "hook",
        "hooks",
        "engagement",
        "community",
        "comments",
        "comment",
        "calendar",
    }
    support_tokens = {
        "support",
        "ticket",
        "tickets",
        "severity",
        "billing",
        "customer",
        "customers",
        "troubleshoot",
        "troubleshooting",
        "issue",
        "issues",
    }

    score = min(confidence * 0.04, 0.05) + min(freshness * 0.03, 0.03) + min(source_count * 0.012, 0.04)
    if query_tokens & support_tokens:
        score -= 0.25
    research_query = bool(query_tokens & research_tokens)
    if research_query:
        score += 0.03
    if research_query and query_tokens & social_tokens:
        score += 0.03
    if topic == "charles_external_sources" and query_tokens & FRESHNESS_QUERY_HINTS:
        score += 0.02
    return round(score, 4)


def phase23_domain_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    source_count = int(entry.get("source_count", 0) or 0)
    topic = str(entry.get("topic", "")).strip()

    research_tokens = {
        "fresh",
        "recent",
        "example",
        "examples",
        "research",
        "monitor",
        "monitoring",
        "source",
        "sources",
        "documentation",
        "docs",
        "faq",
        "knowledge",
        "help",
        "center",
        "macro",
        "macros",
        "benchmark",
        "benchmarks",
        "pattern",
        "patterns",
        "handoff",
        "handoffs",
        "escalation",
    }
    support_issue_tokens = {
        "severity",
        "triage",
        "ticket",
        "tickets",
        "issue",
        "issues",
        "bug",
        "bugs",
        "billing",
        "outage",
        "urgent",
        "customer",
        "customers",
        "sla",
    }
    documentation_authoring_tokens = {
        "documentation",
        "docs",
        "guide",
        "guides",
        "instruction",
        "instructions",
        "setup",
        "walkthrough",
        "troubleshooting",
        "checks",
        "steps",
        "product",
        "clear",
    }

    score = min(confidence * 0.035, 0.04) + min(freshness * 0.02, 0.02) + min(source_count * 0.01, 0.03)
    research_query = bool(query_tokens & research_tokens)
    if research_query:
        score += 0.03
    if query_tokens & {"documentation", "docs", "faq", "knowledge", "help", "center", "macro", "macros", "benchmark", "benchmarks"}:
        score += 0.03
    if topic == "support_external_sources" and query_tokens & FRESHNESS_QUERY_HINTS:
        score += 0.02
    if query_tokens & support_issue_tokens and not research_query:
        score -= 0.12
    if query_tokens & documentation_authoring_tokens and not (query_tokens & support_issue_tokens):
        score -= 0.18
    return round(score, 4)


def phase24_domain_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    evidence_count = int(entry.get("evidence_count", 0) or 0)
    domain = str(entry.get("domain", "")).strip()
    topic = str(entry.get("topic", "")).strip()

    implementation_tokens = {
        "implement",
        "implementation",
        "feature",
        "features",
        "build",
        "coding",
        "code",
        "patch",
        "bug",
        "bugs",
        "bugfix",
        "fix",
        "fixes",
        "tests",
        "testing",
        "refactor",
        "refactors",
        "pr",
        "prs",
        "handoff",
    }
    qa_tokens = {
        "qa",
        "test",
        "tests",
        "testing",
        "regression",
        "edge",
        "edge_cases",
        "matrix",
        "coverage",
        "verify",
        "verification",
        "repro",
        "reproduce",
        "reproduction",
        "pass",
        "fail",
        "blocked",
        "verdict",
        "bug_report",
    }
    review_only_tokens = {"review", "reviewer", "security", "maintainability", "performance"}

    score = min(confidence * 0.03, 0.035) + min(freshness * 0.015, 0.015) + min(evidence_count * 0.004, 0.02)
    if domain == "developer":
        if query_tokens & implementation_tokens:
            score += 0.04
        if topic in {"developer_core", "developer_tdd_loop", "developer_bugfix_loop"} and query_tokens & {"implement", "feature", "bug", "fix", "tests", "testing"}:
            score += 0.03
        if query_tokens & review_only_tokens and not query_tokens & implementation_tokens:
            score -= 0.05
    elif domain == "qa":
        if query_tokens & qa_tokens:
            score += 0.04
        if topic in {"qa_core", "qa_regression_gate", "qa_edge_matrix", "qa_bug_reporting"} and query_tokens & {"regression", "test", "tests", "edge", "matrix", "verdict", "repro"}:
            score += 0.03
        if query_tokens & {"implement", "implementation", "feature"} and not query_tokens & qa_tokens:
            score -= 0.04
    return round(score, 4)


def phase25_domain_adjustment(entry: Dict[str, object], query_tokens: set[str]) -> float:
    if not entry:
        return 0.0
    confidence = float(entry.get("confidence_score", 0.0) or 0.0)
    freshness = float(entry.get("freshness_score", 0.0) or 0.0)
    source_count = int(entry.get("source_count", 0) or 0)
    domain = str(entry.get("domain", "")).strip()
    topic = str(entry.get("topic", "")).strip()

    research_tokens = {
        "fresh",
        "recent",
        "example",
        "examples",
        "research",
        "monitor",
        "monitoring",
        "source",
        "sources",
        "trend",
        "trends",
        "benchmark",
        "benchmarks",
        "release",
        "releases",
        "release_notes",
        "tool",
        "tools",
        "tooling",
        "framework",
        "frameworks",
        "pattern",
        "patterns",
        "blog",
        "blogs",
        "docs",
        "documentation",
        "change",
        "changes",
    }
    developer_tokens = {
        "developer",
        "engineering",
        "engineer",
        "engineers",
        "implementation",
        "implement",
        "refactor",
        "refactors",
        "architecture",
        "pattern",
        "patterns",
        "codebase",
        "testing",
        "tooling",
    }
    qa_tokens = {
        "qa",
        "test",
        "tests",
        "testing",
        "regression",
        "coverage",
        "matrix",
        "edge",
        "verification",
        "verify",
        "repro",
        "release",
        "tooling",
        "framework",
        "playwright",
        "cypress",
    }
    direct_build_tokens = {
        "fix",
        "fixes",
        "patch",
        "patches",
        "bug",
        "bugs",
        "implement",
        "implementation",
        "feature",
        "features",
        "ship",
        "shipping",
    }
    direct_signoff_tokens = {
        "pass",
        "fail",
        "blocked",
        "verdict",
        "signoff",
        "triage",
    }

    score = min(confidence * 0.035, 0.04) + min(freshness * 0.02, 0.02) + min(source_count * 0.01, 0.03)
    research_query = bool(query_tokens & research_tokens)
    if research_query:
        score += 0.03
    if domain == "developer":
        if query_tokens & developer_tokens and research_query:
            score += 0.05
        elif query_tokens & developer_tokens:
            score += 0.015
        if topic == "developer_external_sources" and query_tokens & FRESHNESS_QUERY_HINTS:
            score += 0.02
        if query_tokens & direct_build_tokens and not research_query:
            score -= 0.08
    elif domain == "qa":
        if query_tokens & qa_tokens and research_query:
            score += 0.05
        elif query_tokens & qa_tokens:
            score += 0.015
        if topic == "qa_external_sources" and query_tokens & FRESHNESS_QUERY_HINTS:
            score += 0.02
        if query_tokens & direct_signoff_tokens and not research_query:
            score -= 0.06
    return round(score, 4)


def top_sparse(weights: Dict[str, float], limit: int) -> Tuple[Dict[str, float], float]:
    if not weights:
        return {}, 1.0
    ranked = sorted(weights.items(), key=lambda item: abs(item[1]), reverse=True)[:limit]
    compact = {token: value for token, value in ranked}
    norm = math.sqrt(sum(value * value for value in compact.values())) or 1.0
    return compact, norm


def is_semantic_token(token: str, total_docs: int, doc_freq: Dict[str, int]) -> bool:
    if len(token) < 3 or token.isdigit():
        return False
    freq = int(doc_freq.get(token, 0))
    if freq < 2:
        return False
    max_df = max(int(total_docs * MAX_SEMANTIC_DF_RATIO), 25)
    if freq > max_df:
        return False
    return True


def expand_query(query: str, role: Optional[str] = None) -> Tuple[str, List[str], List[str]]:
    lowered = query.lower()
    original_tokens = set(tokenize(query))
    intents: List[str] = []
    expansions: List[str] = []

    for rule in QUERY_INTENT_RULES:
        if any(re.search(pattern, lowered) for pattern in rule["patterns"]):
            intents.append(rule["intent"])
            expansions.extend(rule["terms"])

    if role:
        expansions.extend(tokenize(role))

    ordered: List[str] = []
    seen = set(original_tokens)
    for term in expansions:
        if term in seen:
            continue
        seen.add(term)
        ordered.append(term)

    expanded_query = query
    if ordered:
        expanded_query = f"{query} {' '.join(ordered[:18])}"

    return expanded_query, sorted(set(intents)), ordered[:18]


def classify_heading(heading: str) -> str:
    value = heading.strip().lower()
    if value in {"document", "overview"}:
        return "overview"
    patterns = [
        ("quick_read", [r"quick read", r"key takeaways?"]),
        ("core_concept", [r"core concept", r"overview"]),
        ("data_stats", [r"data/stats", r"\bstats\b", r"data points", r"published"]),
        ("framework", [r"framework", r"method", r"workflow", r"playbook", r"checklist", r"output template"]),
        ("models_systems", [r"models?", r"systems?", r"internals?", r"mental models?"]),
        ("latest_posts", [r"latest relevant posts", r"archive", r"timeline"]),
        ("concepts", [r"concepts?", r"operating lens", r"heuristics?", r"how to use"]),
        ("examples", [r"examples?", r"case studies?"]),
        ("sources", [r"references?", r"sources?"]),
    ]
    for section_kind, regexes in patterns:
        if any(re.search(regex, value) for regex in regexes):
            return section_kind
    return "section"


def parse_date_text(value: str) -> Optional[date]:
    value = value.strip()
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        pass
    try:
        return datetime.strptime(value, "%B %d, %Y").date()
    except ValueError:
        return None


def extract_published_on(meta: Dict[str, str], body: str) -> str:
    for key in ("updated_on", "updated", "published_on", "published", "date"):
        parsed = parse_date_text(meta.get(key, ""))
        if parsed:
            return parsed.isoformat()

    for line in body.splitlines()[:80]:
        line = line.strip()
        if not line:
            continue
        match = ISO_DATE_RE.search(line)
        if match:
            parsed = parse_date_text(match.group(1))
            if parsed:
                return parsed.isoformat()
        match = MONTH_DATE_RE.search(line)
        if match:
            parsed = parse_date_text(match.group(0))
            if parsed:
                return parsed.isoformat()
    return ""


def freshness_score(published_on: str) -> float:
    if not published_on:
        return 0.0
    parsed = parse_date_text(published_on)
    if not parsed:
        return 0.0
    days_old = max((date.today() - parsed).days, 0)
    if days_old <= 30:
        return 0.08
    if days_old <= 90:
        return 0.06
    if days_old <= 180:
        return 0.045
    if days_old <= 365:
        return 0.03
    if days_old <= 730:
        return 0.015
    return 0.0


def is_specific_evidence_query(query: str, query_tokens: set[str]) -> bool:
    if query_tokens & SPECIFIC_EVIDENCE_QUERY_HINTS:
        return True
    return bool(re.search(r"\b20\d{2}\b", query))


def is_broad_synthesis_query(query_tokens: set[str], inferred_intents: Sequence[str], specific_evidence_query: bool) -> bool:
    if specific_evidence_query:
        return False
    if query_tokens & BROAD_SYNTHESIS_QUERY_HINTS:
        return True
    return bool(inferred_intents)


def canonical_topic_boost(
    path: str,
    heading: str,
    is_canonical: bool,
    topic_overlap: int,
    intent_overlap: int,
    use_for_overlap: int,
    broad_synthesis_query: bool,
) -> float:
    if not is_canonical:
        return 0.0
    boost = 0.12
    if "/memory/canonical/" in path:
        boost += 0.12
    if broad_synthesis_query:
        boost += min(topic_overlap * 0.04 + intent_overlap * 0.08 + use_for_overlap * 0.06, 0.22)
        if heading.strip().lower() in {
            "what the squad should assume",
            "recovery workflow",
            "common failure patterns",
            "retrieval use",
            "core position",
        }:
            boost += 0.06
    elif topic_overlap or intent_overlap or use_for_overlap:
        boost += min(topic_overlap * 0.02 + intent_overlap * 0.04 + use_for_overlap * 0.03, 0.1)
    return round(min(boost, 0.52), 4)


def low_signal_support_heading(heading: str) -> bool:
    return heading.strip().lower() in {"squad routing", "primary evidence in this pack"}


def infer_source(skill: str, rel: Path) -> str:
    if skill == "dejan-ai-reverse-engineering" or any("dejan" in part for part in rel.parts):
        return "dejan"
    if rel.parts[0] == "seo" and rel.name.startswith("ahrefs-"):
        return "ahrefs"
    if rel.parts[0] == "seo" and rel.name.startswith("hobo-"):
        return "hobo"
    return ""


def parse_markdown_sections(text: str) -> List[Tuple[str, str]]:
    sections: List[Tuple[str, List[str]]] = []
    current_heading = "Document"
    current_lines: List[str] = []

    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            if current_lines:
                sections.append((current_heading, current_lines))
            current_heading = match.group(2).strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_heading, current_lines))

    out: List[Tuple[str, str]] = []
    for heading, lines in sections:
        chunk_text = "\n".join(lines).strip()
        if chunk_text:
            out.append((heading, chunk_text))
    return out


def hard_wrap_block(text: str, limit: int) -> List[str]:
    words = text.split()
    if not words:
        return []
    chunks: List[str] = []
    current: List[str] = []
    size = 0
    for word in words:
        addition = len(word) + (1 if current else 0)
        if size + addition > limit and current:
            chunks.append(" ".join(current).strip())
            current = [word]
            size = len(word)
        else:
            current.append(word)
            size += addition
    if current:
        chunks.append(" ".join(current).strip())
    return chunks


def split_long_block(block: str, limit: int) -> List[str]:
    text = block.strip()
    if not text:
        return []
    if len(text) <= limit:
        return [text]

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) > 1:
        chunks: List[str] = []
        current: List[str] = []
        size = 0
        for line in lines:
            addition = len(line) + (1 if current else 0)
            if size + addition > limit and current:
                chunks.append("\n".join(current).strip())
                current = [line]
                size = len(line)
            else:
                current.append(line)
                size += addition
        if current:
            chunks.append("\n".join(current).strip())
        return chunks

    sentences = [part.strip() for part in SENTENCE_BOUNDARY_RE.split(text) if part.strip()]
    if len(sentences) <= 1:
        return hard_wrap_block(text, limit)

    chunks = []
    current = []
    size = 0
    for sentence in sentences:
        addition = len(sentence) + (1 if current else 0)
        if size + addition > limit and current:
            chunks.append(" ".join(current).strip())
            current = [sentence]
            size = len(sentence)
        else:
            current.append(sentence)
            size += addition
    if current:
        chunks.append(" ".join(current).strip())

    if len(chunks) >= 2 and len(chunks[-1]) < max(140, limit // 4):
        merged = f"{chunks[-2]} {chunks[-1]}".strip()
        if len(merged) <= int(limit * 1.2):
            chunks[-2] = merged
            chunks.pop()
    return chunks


def split_blocks(text: str, block_limit: int = 680) -> List[str]:
    blocks = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    out: List[str] = []
    for block in blocks:
        lines = [line.rstrip() for line in block.splitlines()]
        bullet_lines = [line for line in lines if re.match(r"^\s*[-*]\s+", line)]
        if len(bullet_lines) >= 6:
            group: List[str] = []
            for line in lines:
                if re.match(r"^\s*[-*]\s+", line):
                    group.append(line)
                    if len(group) >= 4:
                        out.append("\n".join(group))
                        group = []
                elif group:
                    group.append(line)
            if group:
                out.append("\n".join(group))
            continue
        out.extend(split_long_block(block, block_limit))
    return out


def skill_root_for_path(path: str) -> str:
    return path.split("/", 1)[0] if "/" in path else path


def normalize_list(value: object) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    if isinstance(value, (list, tuple, set)):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()]


def load_task_packs(path: Path) -> List[TaskPack]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    packs: List[TaskPack] = []
    for item in payload.get("packs", []):
        packs.append(
            TaskPack(
                pack_id=str(item["id"]).strip(),
                name=str(item.get("name", item["id"])).strip(),
                description=str(item.get("description", "")).strip(),
                roles=[value.lower() for value in normalize_list(item.get("roles"))],
                intents=[value.lower() for value in normalize_list(item.get("intents"))],
                keywords=[value.lower() for value in normalize_list(item.get("keywords"))],
                primary_skill=str(item.get("primary_skill", "")).strip(),
                supporting_skills=normalize_list(item.get("supporting_skills")),
                memory_focus=[value.lower() for value in normalize_list(item.get("memory_focus"))],
                checklist=normalize_list(item.get("checklist")),
                deliverables=normalize_list(item.get("deliverables")),
                output_sections=normalize_list(item.get("output_sections")),
                handoffs=normalize_list(item.get("handoffs")),
                escalation_rules=normalize_list(item.get("escalation_rules")),
            )
        )
    return packs


@lru_cache(maxsize=8)
def cached_task_packs(path_str: str, mtime_ns: int, size: int) -> Tuple[TaskPack, ...]:
    return tuple(load_task_packs(Path(path_str)))


def task_pack_to_dict(pack: TaskPack) -> dict:
    return {
        "id": pack.pack_id,
        "name": pack.name,
        "description": pack.description,
        "roles": pack.roles,
        "intents": pack.intents,
        "keywords": pack.keywords,
        "primary_skill": pack.primary_skill,
        "supporting_skills": pack.supporting_skills,
        "memory_focus": pack.memory_focus,
        "checklist": pack.checklist,
        "deliverables": pack.deliverables,
        "output_sections": pack.output_sections,
        "handoffs": pack.handoffs,
        "escalation_rules": pack.escalation_rules,
    }


def default_owner_for_step(title: str, primary_skill: str, supporting_skills: Sequence[str]) -> str:
    lowered = title.lower()
    support_map = {
        "writer": ["draft", "write", "rewrite", "copy", "headline"],
        "marketing": ["launch", "distribute", "promotion", "promote", "campaign"],
        "charles": ["social", "post", "thread", "repurpose", "community"],
        "qa": ["test", "verify", "regression", "pass/fail", "edge case"],
        "developer": ["implement", "fix", "refactor", "code", "patch"],
        "support-anemone": ["ticket", "triage", "customer", "escalate"],
        "support": ["ticket", "triage", "customer", "escalate"],
        "reviewer": ["review", "risk", "approve", "findings"],
        "devops": ["deploy", "release", "rollback", "incident"],
        "operations": ["timeline", "coordination", "handoff", "owner"],
        "researcher": ["research", "fact-check", "source", "evidence"],
    }
    for skill in supporting_skills:
        for hint in support_map.get(skill, []):
            if hint in lowered:
                return skill
    return primary_skill


def run_step_rows_from_plan(plan: dict) -> List[Dict[str, Any]]:
    primary_skill = str(plan.get("primary_skill") or "")
    supporting_skills = [str(item) for item in plan.get("supporting_skills", []) if str(item)]
    execution_steps = [str(item).strip() for item in plan.get("execution_steps", []) if str(item).strip()]
    if not execution_steps:
        execution_steps = [
            f"Execute {plan.get('selected_pack', {}).get('name', 'task pack')}",
        ]
    rows: List[Dict[str, Any]] = []
    for seq, title in enumerate(execution_steps, start=1):
        rows.append(
            {
                "seq": seq,
                "title": title,
                "step_kind": "checklist",
                "owner_skill": default_owner_for_step(title, primary_skill, supporting_skills),
                "status": "pending",
            }
        )
    return rows


def fetch_pack_run_in_connection(con: sqlite3.Connection, run_id: int) -> Optional[Dict[str, Any]]:
    old_row_factory = con.row_factory
    con.row_factory = sqlite3.Row
    try:
        row = con.execute(
            """
            SELECT id, ts_started, ts_updated, ts_completed, query, role, pack_id, pack_name, primary_skill,
                   supporting_skills_json, status, current_step_seq, step_count, blocker_count, handoff_count, notes, metadata_json
            FROM pack_runs
            WHERE id = ?
            """,
            (run_id,),
        ).fetchone()
        if row is None:
            return None
        try:
            supporting_skills = json.loads(str(row["supporting_skills_json"] or "[]"))
        except json.JSONDecodeError:
            supporting_skills = []
        try:
            metadata = json.loads(str(row["metadata_json"] or "{}"))
        except json.JSONDecodeError:
            metadata = {}
        return {
            "id": int(row["id"]),
            "ts_started": str(row["ts_started"] or ""),
            "ts_updated": str(row["ts_updated"] or ""),
            "ts_completed": str(row["ts_completed"] or ""),
            "query": str(row["query"] or ""),
            "role": str(row["role"] or ""),
            "pack_id": str(row["pack_id"] or ""),
            "pack_name": str(row["pack_name"] or ""),
            "primary_skill": str(row["primary_skill"] or ""),
            "supporting_skills": supporting_skills if isinstance(supporting_skills, list) else [],
            "status": str(row["status"] or ""),
            "current_step_seq": int(row["current_step_seq"] or 0),
            "step_count": int(row["step_count"] or 0),
            "blocker_count": int(row["blocker_count"] or 0),
            "handoff_count": int(row["handoff_count"] or 0),
            "notes": str(row["notes"] or ""),
            "metadata": metadata if isinstance(metadata, dict) else {},
        }
    finally:
        con.row_factory = old_row_factory


def fetch_pack_run_steps_in_connection(con: sqlite3.Connection, run_id: int) -> List[Dict[str, Any]]:
    old_row_factory = con.row_factory
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            """
            SELECT id, run_id, seq, title, step_kind, owner_skill, status, notes, artifact_path, evidence_json, ts_updated
            FROM pack_run_steps
            WHERE run_id = ?
            ORDER BY seq ASC, id ASC
            """,
            (run_id,),
        ).fetchall()
        result = []
        for row in rows:
            try:
                evidence = json.loads(str(row["evidence_json"] or "{}"))
            except json.JSONDecodeError:
                evidence = {}
            result.append(
                {
                    "id": int(row["id"]),
                    "run_id": int(row["run_id"]),
                    "seq": int(row["seq"]),
                    "title": str(row["title"] or ""),
                    "step_kind": str(row["step_kind"] or ""),
                    "owner_skill": str(row["owner_skill"] or ""),
                    "status": str(row["status"] or ""),
                    "notes": str(row["notes"] or ""),
                    "artifact_path": str(row["artifact_path"] or ""),
                    "evidence": evidence if isinstance(evidence, dict) else {},
                    "ts_updated": str(row["ts_updated"] or ""),
                }
            )
        return result
    finally:
        con.row_factory = old_row_factory


def fetch_pack_run_handoffs_in_connection(con: sqlite3.Connection, run_id: int) -> List[Dict[str, Any]]:
    old_row_factory = con.row_factory
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            """
            SELECT id, run_id, ts, from_skill, to_skill, reason, notes, status, metadata_json
            FROM pack_run_handoffs
            WHERE run_id = ?
            ORDER BY id DESC
            """,
            (run_id,),
        ).fetchall()
        result = []
        for row in rows:
            try:
                metadata = json.loads(str(row["metadata_json"] or "{}"))
            except json.JSONDecodeError:
                metadata = {}
            result.append(
                {
                    "id": int(row["id"]),
                    "run_id": int(row["run_id"]),
                    "ts": str(row["ts"] or ""),
                    "from_skill": str(row["from_skill"] or ""),
                    "to_skill": str(row["to_skill"] or ""),
                    "reason": str(row["reason"] or ""),
                    "notes": str(row["notes"] or ""),
                    "status": str(row["status"] or ""),
                    "metadata": metadata if isinstance(metadata, dict) else {},
                }
            )
        return result
    finally:
        con.row_factory = old_row_factory


def fetch_pack_run_blockers_in_connection(con: sqlite3.Connection, run_id: int) -> List[Dict[str, Any]]:
    old_row_factory = con.row_factory
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            """
            SELECT id, run_id, ts_opened, ts_resolved, step_seq, title, severity, owner_skill, status, notes, metadata_json
            FROM pack_run_blockers
            WHERE run_id = ?
            ORDER BY id DESC
            """,
            (run_id,),
        ).fetchall()
        result = []
        for row in rows:
            try:
                metadata = json.loads(str(row["metadata_json"] or "{}"))
            except json.JSONDecodeError:
                metadata = {}
            result.append(
                {
                    "id": int(row["id"]),
                    "run_id": int(row["run_id"]),
                    "ts_opened": str(row["ts_opened"] or ""),
                    "ts_resolved": str(row["ts_resolved"] or ""),
                    "step_seq": int(row["step_seq"] or 0),
                    "title": str(row["title"] or ""),
                    "severity": str(row["severity"] or ""),
                    "owner_skill": str(row["owner_skill"] or ""),
                    "status": str(row["status"] or ""),
                    "notes": str(row["notes"] or ""),
                    "metadata": metadata if isinstance(metadata, dict) else {},
                }
            )
        return result
    finally:
        con.row_factory = old_row_factory


def refresh_pack_run_state_in_connection(con: sqlite3.Connection, run_id: int) -> Dict[str, Any]:
    steps = fetch_pack_run_steps_in_connection(con, run_id)
    blockers = fetch_pack_run_blockers_in_connection(con, run_id)
    handoffs = fetch_pack_run_handoffs_in_connection(con, run_id)
    run = fetch_pack_run_in_connection(con, run_id)
    if run is None:
        raise ValueError(f"Unknown pack run: {run_id}")

    open_blockers = [item for item in blockers if item["status"] == "open"]
    active_steps = [item for item in steps if item["status"] == "active"]
    pending_steps = [item for item in steps if item["status"] == "pending"]
    incomplete_steps = [item for item in steps if item["status"] not in {"completed", "skipped"}]

    if open_blockers:
        run_status = "blocked"
    elif run["status"] == "planned" and not active_steps and pending_steps:
        run_status = "planned"
    elif steps and not incomplete_steps:
        run_status = "completed"
    else:
        run_status = "active"

    if run_status == "active" and not active_steps and pending_steps:
        next_step = pending_steps[0]
        con.execute(
            "UPDATE pack_run_steps SET status = 'active', ts_updated = CURRENT_TIMESTAMP WHERE id = ?",
            (next_step["id"],),
        )
        steps = fetch_pack_run_steps_in_connection(con, run_id)
        active_steps = [item for item in steps if item["status"] == "active"]
        pending_steps = [item for item in steps if item["status"] == "pending"]

    current_step_seq = 0
    if active_steps:
        current_step_seq = min(int(item["seq"]) for item in active_steps)
    elif pending_steps:
        current_step_seq = min(int(item["seq"]) for item in pending_steps)

    ts_completed_expr = "CURRENT_TIMESTAMP" if run_status == "completed" and not run["ts_completed"] else "NULL"
    if run_status != "completed":
        con.execute(
            """
            UPDATE pack_runs
            SET ts_updated = CURRENT_TIMESTAMP,
                ts_completed = NULL,
                status = ?,
                current_step_seq = ?,
                step_count = ?,
                blocker_count = ?,
                handoff_count = ?
            WHERE id = ?
            """,
            (run_status, current_step_seq, len(steps), len(open_blockers), len(handoffs), run_id),
        )
    else:
        con.execute(
            f"""
            UPDATE pack_runs
            SET ts_updated = CURRENT_TIMESTAMP,
                ts_completed = COALESCE(ts_completed, {ts_completed_expr}),
                status = ?,
                current_step_seq = ?,
                step_count = ?,
                blocker_count = ?,
                handoff_count = ?
            WHERE id = ?
            """,
            (run_status, current_step_seq, len(steps), len(open_blockers), len(handoffs), run_id),
        )
    return fetch_pack_run_in_connection(con, run_id) or run


def find_task_pack(packs: Sequence[TaskPack], pack_id: str) -> TaskPack:
    for pack in packs:
        if pack.pack_id == pack_id:
            return pack
    raise ValueError(f"Unknown task pack: {pack_id}")


def pack_focus_overlap(item: dict, pack: TaskPack) -> int:
    if not pack.memory_focus:
        return 0
    pack_terms = set(pack.memory_focus)
    meta_tokens = set(item.get("topics", []))
    meta_tokens.update(item.get("intents", []))
    meta_tokens.update(item.get("bundles", []))
    meta_tokens.update(tokenize(item.get("canonical_group", "")))
    meta_tokens.update(tokenize(item.get("heading", "")))
    meta_tokens.update(tokenize(item.get("path", "")))
    return len(meta_tokens & pack_terms)


def summarize_memory_themes(items: Sequence[dict], limit: int = 5) -> List[str]:
    themes: List[str] = []
    seen = set()
    for item in items:
        label = item.get("canonical_group") or item.get("heading") or skill_root_for_path(item.get("path", ""))
        label = label.strip()
        if not label or label in seen:
            continue
        seen.add(label)
        themes.append(label)
        if len(themes) >= limit:
            break
    return themes


def score_task_pack(pack: TaskPack, query: str, role: Optional[str], decision: dict) -> dict:
    lowered = query.lower()
    query_tokens = set(tokenize(query))
    inferred_intents = set(decision.get("inferred_intents", []))
    ranked_skills = [item["skill"] for item in decision.get("recommended_skills", [])]
    top_skills = ranked_skills[:5]
    top3_skills = set(ranked_skills[:3])
    score = 0.0
    reasons: List[str] = []

    if top_skills and pack.primary_skill == top_skills[0]:
        score += 2.2
        reasons.append(f"Primary skill matches top recommendation: {pack.primary_skill}")
    elif pack.primary_skill in top3_skills:
        score += 1.0
        reasons.append(f"Primary skill is already in top-3: {pack.primary_skill}")

    intent_hits = sorted(inferred_intents & set(pack.intents))
    if intent_hits:
        score += len(intent_hits) * 1.1
        reasons.append(f"Intent overlap: {', '.join(intent_hits)}")

    keyword_hits: List[str] = []
    for keyword in pack.keywords:
        if " " in keyword:
            if keyword in lowered:
                keyword_hits.append(keyword)
        elif keyword in query_tokens:
            keyword_hits.append(keyword)
    if keyword_hits:
        score += min(len(keyword_hits) * 0.35, 1.4)
        reasons.append(f"Keyword overlap: {', '.join(keyword_hits[:4])}")

    if role and role.lower() in pack.roles:
        score += 0.45
        reasons.append(f"Role match: {role.lower()}")

    support_hits: List[str] = []
    for skill in pack.supporting_skills:
        if skill in top3_skills:
            score += 0.45
            support_hits.append(skill)
        elif skill in top_skills:
            score += 0.2
            support_hits.append(skill)
    if support_hits:
        reasons.append(f"Supporting skills already surfaced: {', '.join(support_hits)}")

    memory_hits = 0
    for item in decision.get("supporting_memory", [])[:10]:
        memory_hits += pack_focus_overlap(item, pack)
    if memory_hits:
        score += min(memory_hits * 0.14, 0.9)
        reasons.append(f"Memory focus overlap score: {memory_hits}")

    if pack.pack_id == "content_brief":
        bonus = 0.0
        if "content brief" in lowered:
            bonus += 1.1
        if "target keyword" in lowered:
            bonus += 0.45
        if "success criteria" in lowered:
            bonus += 0.35
        if "audience" in query_tokens:
            bonus += 0.2
        if "outline" in query_tokens and "draft" not in query_tokens:
            bonus += 0.18
        if bonus:
            score += bonus
            reasons.append(f"Brief-shape bonus: +{bonus:.2f}")
    elif pack.pack_id == "article_draft":
        penalty = 0.0
        if "content brief" in lowered and "draft" not in query_tokens:
            penalty += 0.65
        if "success criteria" in lowered and "blog" not in query_tokens and "article" not in query_tokens:
            penalty += 0.18
        if penalty:
            score -= penalty
            reasons.append(f"Draft-shape penalty: -{penalty:.2f}")

    return {
        "pack": pack,
        "score": round(score, 4),
        "reasons": reasons[:5],
    }


def usage_stat_row() -> Dict[str, int]:
    return {"useful_count": 0, "not_useful_count": 0, "exposure_count": 0}


def buckets_for_query(query: str, role: Optional[str] = None, inferred_intents: Optional[Sequence[str]] = None) -> List[str]:
    intents = sorted(set(inferred_intents or expand_query(query, role)[1]))
    return [GLOBAL_BUCKET] + intents


def usage_score(useful_count: int, not_useful_count: int, exposure_count: int) -> float:
    observed = max(exposure_count, useful_count + not_useful_count, 1)
    success_rate = useful_count / observed
    failure_rate = not_useful_count / observed
    score = useful_count * 0.22 - not_useful_count * 0.28 + success_rate * 0.45 - failure_rate * 0.35
    if exposure_count >= 3 and useful_count == 0:
        score -= min((exposure_count - 2) * 0.04, 0.2)
    return round(score, 4)


def pack_stat_row() -> Dict[str, float]:
    return {
        "accepted_count": 0,
        "revised_count": 0,
        "failed_count": 0,
        "exposure_count": 0,
        "rating_sum": 0.0,
        "rating_count": 0,
        "revision_sum": 0.0,
    }


def pack_buckets_for_query(query: str, role: Optional[str] = None) -> List[str]:
    buckets = buckets_for_query(query, role=role)
    if role:
        buckets.append(f"role:{role.lower()}")
    return list(dict.fromkeys(buckets))


def update_pack_stats(stats: Dict[str, float], status: str, revision_count: int, user_rating: Optional[float]) -> None:
    stats["exposure_count"] += 1
    field = f"{status}_count"
    if field in stats:
        stats[field] += 1
    stats["revision_sum"] += max(revision_count, 0)
    if user_rating is not None:
        stats["rating_sum"] += user_rating
        stats["rating_count"] += 1


def pack_outcome_score(
    accepted_count: int,
    revised_count: int,
    failed_count: int,
    exposure_count: int,
    avg_rating: Optional[float],
    avg_revisions: float,
) -> float:
    observed = max(exposure_count, accepted_count + revised_count + failed_count, 1)
    accepted_rate = accepted_count / observed
    revised_rate = revised_count / observed
    failed_rate = failed_count / observed
    rating_bonus = 0.0 if avg_rating is None else max(min((avg_rating - 3.0) * 0.08, 0.16), -0.16)
    revision_penalty = min(avg_revisions * 0.08, 0.24)
    score = (
        accepted_count * 0.24
        + revised_count * 0.04
        - failed_count * 0.32
        + accepted_rate * 0.55
        + revised_rate * 0.08
        - failed_rate * 0.5
        + rating_bonus
        - revision_penalty
    )
    if exposure_count >= 3 and accepted_count == 0:
        score -= min((exposure_count - 2) * 0.05, 0.25)
    return round(score, 4)


def result_learning_stat_row() -> Dict[str, float]:
    return {
        "signal_sum": 0.0,
        "overall_sum": 0.0,
        "weight_sum": 0.0,
        "manual_count": 0,
        "suggested_count": 0,
        "exposure_count": 0,
        "high_count": 0,
        "low_count": 0,
    }


def result_mode_weight(scoring_mode: str) -> float:
    return float(RESULT_MODE_WEIGHTS.get(scoring_mode, 0.4))


def result_signal(
    overall_score: float,
    verdict: str,
    status: str,
    revision_count: int,
) -> float:
    normalized = max(min((float(overall_score) - 3.5) / 1.35, 1.0), -1.0)
    verdict_signal = RESULT_VERDICT_SIGNAL.get(verdict, 0.0)
    status_signal = RESULT_STATUS_SIGNAL.get(status, 0.0)
    revision_penalty = min(max(int(revision_count or 0), 0) * 0.04, 0.18)
    return round(max(min(normalized + verdict_signal + status_signal - revision_penalty, 1.15), -1.15), 4)


def update_result_learning_stats(
    stats: Dict[str, float],
    overall_score: float,
    verdict: str,
    scoring_mode: str,
    status: str,
    revision_count: int,
) -> None:
    weight = result_mode_weight(scoring_mode)
    stats["signal_sum"] += result_signal(overall_score, verdict, status, revision_count) * weight
    stats["overall_sum"] += float(overall_score) * weight
    stats["weight_sum"] += weight
    stats["exposure_count"] += 1
    if scoring_mode == "manual":
        stats["manual_count"] += 1
    else:
        stats["suggested_count"] += 1
    if float(overall_score) >= 4.0:
        stats["high_count"] += 1
    if float(overall_score) < 3.2:
        stats["low_count"] += 1


def result_learning_score(stats: Dict[str, float]) -> Tuple[float, float]:
    weight_sum = max(float(stats["weight_sum"]), 1e-9)
    exposure_count = max(int(stats["exposure_count"]), 1)
    avg_signal = float(stats["signal_sum"]) / weight_sum
    avg_overall = float(stats["overall_sum"]) / weight_sum
    high_rate = float(stats["high_count"]) / exposure_count
    low_rate = float(stats["low_count"]) / exposure_count
    confidence_bonus = min(max(weight_sum - 1.0, 0.0) * 0.06, 0.18)
    manual_bonus = min(float(stats["manual_count"]) * 0.05, 0.16)
    score = avg_signal + high_rate * 0.14 - low_rate * 0.18 + confidence_bonus + manual_bonus
    return round(score, 4), round(avg_overall, 4)


def clamp_result_score(value: float) -> float:
    return round(max(1.0, min(float(value), 5.0)), 2)


def result_verdict(overall_score: float) -> str:
    for threshold, verdict in RESULT_VERDICT_BANDS:
        if overall_score >= threshold:
            return verdict
    return "poor"


def compute_result_overall(scores: Dict[str, float]) -> float:
    return round(sum(float(scores[field]) * RESULT_SCORE_WEIGHTS[field] for field in RESULT_SCORE_FIELDS), 2)


def parse_json_list(value: str) -> List[str]:
    try:
        parsed = json.loads(value or "[]")
        if not isinstance(parsed, list):
            return []
        return [str(item).strip() for item in parsed if str(item).strip()]
    except json.JSONDecodeError:
        return []


def fetch_task_outcomes_in_connection(con: sqlite3.Connection) -> List[Dict[str, Any]]:
    rows = con.execute(
        """
        SELECT id, ts, query, role, pack_id, primary_skill, supporting_skills_json, used_skills_json,
               memory_paths_json, status, revision_count, completion_minutes, user_rating, notes
        FROM task_outcomes
        ORDER BY id DESC
        """
    ).fetchall()
    outcomes: List[Dict[str, Any]] = []
    for row in rows:
        outcomes.append(
            {
                "id": int(row[0]),
                "ts": row[1],
                "query": row[2],
                "role": row[3],
                "pack_id": row[4],
                "primary_skill": row[5],
                "supporting_skills": parse_json_list(row[6]),
                "used_skills": parse_json_list(row[7]),
                "memory_paths": parse_json_list(row[8]),
                "status": row[9],
                "revision_count": int(row[10] or 0),
                "completion_minutes": None if row[11] is None else float(row[11]),
                "user_rating": None if row[12] is None else float(row[12]),
                "notes": row[13] or "",
            }
        )
    return outcomes


def fetch_task_result_scorecards_in_connection(con: sqlite3.Connection) -> Dict[int, Dict[str, Any]]:
    rows = con.execute(
        """
        SELECT outcome_id, ts, scorer, scoring_mode, goal_fit_score, correctness_score, clarity_score,
               completeness_score, actionability_score, format_score, overall_score, verdict, notes
        FROM task_result_scorecards
        ORDER BY outcome_id DESC
        """
    ).fetchall()
    scorecards: Dict[int, Dict[str, Any]] = {}
    for row in rows:
        scorecards[int(row[0])] = {
            "outcome_id": int(row[0]),
            "ts": row[1],
            "scorer": row[2],
            "scoring_mode": row[3],
            "goal_fit_score": float(row[4]),
            "correctness_score": float(row[5]),
            "clarity_score": float(row[6]),
            "completeness_score": float(row[7]),
            "actionability_score": float(row[8]),
            "format_score": float(row[9]),
            "overall_score": float(row[10]),
            "verdict": row[11],
            "notes": row[12] or "",
        }
    return scorecards


def suggest_task_result_scorecard(outcome: Dict[str, Any]) -> Dict[str, Any]:
    status = str(outcome.get("status", "revised"))
    revision_count = max(int(outcome.get("revision_count", 0) or 0), 0)
    user_rating = outcome.get("user_rating")
    completion_minutes = outcome.get("completion_minutes")
    notes = str(outcome.get("notes", "") or "").lower()

    base = {"accepted": 4.35, "revised": 3.35, "failed": 1.8}.get(status, 3.2)
    rating_adjustment = 0.0 if user_rating is None else max(min((float(user_rating) - 4.0) * 0.28, 0.42), -0.42)
    revision_penalty = min(revision_count * 0.22, 0.88)
    speed_penalty = 0.0
    if completion_minutes is not None:
        if completion_minutes >= 120:
            speed_penalty = 0.18
        elif completion_minutes >= 75:
            speed_penalty = 0.08

    note_adjustment = 0.0
    reasons = [f"Status `{status}` sets the baseline expectation."]
    if user_rating is not None:
        reasons.append(f"User rating `{float(user_rating):.1f}` adjusts the score upward or downward.")
    if revision_count:
        reasons.append(f"{revision_count} revision(s) reduce confidence in output quality.")
    if speed_penalty:
        reasons.append("Long completion time slightly reduces delivery efficiency.")

    for term, delta in RESULT_POSITIVE_NOTE_TERMS.items():
        if term in notes:
            note_adjustment += delta
    for term, delta in RESULT_NEGATIVE_NOTE_TERMS.items():
        if term in notes:
            note_adjustment += delta
    note_adjustment = max(min(note_adjustment, 0.35), -0.5)
    if note_adjustment:
        reasons.append("Outcome notes contain positive or negative cues that influenced the suggestion.")

    raw_scores = {
        "goal_fit_score": base + rating_adjustment - (revision_penalty * 0.24) - (speed_penalty * 0.08) + note_adjustment * 0.6,
        "correctness_score": base + (rating_adjustment * 0.85) - (revision_penalty * 0.38) - (speed_penalty * 0.06) + note_adjustment * 0.5,
        "clarity_score": base + (rating_adjustment * 0.6) - (revision_penalty * 0.56) - (speed_penalty * 0.04) + note_adjustment * 0.7,
        "completeness_score": base + (rating_adjustment * 0.5) - (revision_penalty * 0.48) - (speed_penalty * 0.08) + note_adjustment * 0.45,
        "actionability_score": base + (rating_adjustment * 0.45) - (revision_penalty * 0.28) - (speed_penalty * 0.02) + note_adjustment * 0.35,
        "format_score": base + (rating_adjustment * 0.35) - (revision_penalty * 0.32) - (speed_penalty * 0.06) + note_adjustment * 0.4,
    }
    scores = {field: clamp_result_score(value) for field, value in raw_scores.items()}
    overall_score = compute_result_overall(scores)
    return {
        **scores,
        "overall_score": overall_score,
        "verdict": result_verdict(overall_score),
        "suggestion_reasons": reasons,
    }


def upsert_task_result_scorecard_in_connection(
    con: sqlite3.Connection,
    outcome_id: int,
    scores: Dict[str, float],
    scorer: str,
    scoring_mode: str,
    notes: str,
) -> None:
    con.execute(
        """
        INSERT INTO task_result_scorecards(
          outcome_id, ts, scorer, scoring_mode, goal_fit_score, correctness_score, clarity_score,
          completeness_score, actionability_score, format_score, overall_score, verdict, notes
        )
        VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(outcome_id) DO UPDATE SET
          ts = CURRENT_TIMESTAMP,
          scorer = excluded.scorer,
          scoring_mode = excluded.scoring_mode,
          goal_fit_score = excluded.goal_fit_score,
          correctness_score = excluded.correctness_score,
          clarity_score = excluded.clarity_score,
          completeness_score = excluded.completeness_score,
          actionability_score = excluded.actionability_score,
          format_score = excluded.format_score,
          overall_score = excluded.overall_score,
          verdict = excluded.verdict,
          notes = excluded.notes
        """,
        (
            outcome_id,
            scorer,
            scoring_mode,
            float(scores["goal_fit_score"]),
            float(scores["correctness_score"]),
            float(scores["clarity_score"]),
            float(scores["completeness_score"]),
            float(scores["actionability_score"]),
            float(scores["format_score"]),
            float(scores["overall_score"]),
            scores["verdict"],
            notes,
        ),
    )


def score_task_result(
    db_path: Path,
    outcome_id: int,
    scorer: str = "manual",
    scoring_mode: str = "manual",
    notes: str = "",
    **score_overrides: Optional[float],
) -> Dict[str, Any]:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        outcomes = fetch_task_outcomes_in_connection(con)
        outcome = next((item for item in outcomes if item["id"] == outcome_id), None)
        if outcome is None:
            raise SystemExit(f"Unknown task outcome id: {outcome_id}")
        suggestion = suggest_task_result_scorecard(outcome)
        scores = {}
        for field in RESULT_SCORE_FIELDS:
            override = score_overrides.get(field)
            scores[field] = clamp_result_score(override if override is not None else suggestion[field])
        overall_score = compute_result_overall(scores)
        final_scores = {
            **scores,
            "overall_score": overall_score,
            "verdict": result_verdict(overall_score),
        }
        upsert_task_result_scorecard_in_connection(con, outcome_id, final_scores, scorer, scoring_mode, notes)
        emit_event_in_connection(
            con,
            event_type="task.scored",
            event_group="scorecard",
            source="squad_memory",
            status=final_scores["verdict"],
            query=str(outcome.get("query") or ""),
            role=outcome.get("role"),
            pack_id=str(outcome.get("pack_id") or ""),
            skill=str(outcome.get("primary_skill") or ""),
            metadata={
                "outcome_id": outcome_id,
                "scorer": scorer,
                "scoring_mode": scoring_mode,
                "overall_score": final_scores["overall_score"],
                "verdict": final_scores["verdict"],
            },
        )
        con.commit()
    finally:
        con.close()

    return {
        "db": str(db_path),
        "outcome_id": outcome_id,
        "scorer": scorer,
        "scoring_mode": scoring_mode,
        "notes": notes,
        "scores": final_scores,
        "suggestion_reasons": suggestion["suggestion_reasons"],
        "status": outcome["status"],
        "pack_id": outcome["pack_id"],
        "primary_skill": outcome["primary_skill"],
        "query": outcome["query"],
    }


def sync_task_result_suggestions(db_path: Path) -> Dict[str, Any]:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        outcomes = fetch_task_outcomes_in_connection(con)
        scorecards = fetch_task_result_scorecards_in_connection(con)
        inserted = 0
        updated = 0
        skipped_manual = 0
        for outcome in outcomes:
            existing = scorecards.get(outcome["id"])
            if existing and existing.get("scoring_mode") == "manual":
                skipped_manual += 1
                continue
            suggestion = suggest_task_result_scorecard(outcome)
            upsert_task_result_scorecard_in_connection(
                con,
                outcome["id"],
                suggestion,
                scorer="system",
                scoring_mode="suggested",
                notes="Suggested from task outcome metadata",
            )
            if existing:
                updated += 1
            else:
                inserted += 1
        con.commit()
    finally:
        con.close()

    return {
        "db": str(db_path),
        "task_outcomes": len(outcomes),
        "inserted_suggestions": inserted,
        "updated_suggestions": updated,
        "skipped_manual": skipped_manual,
    }


def extract_logged_paths_and_skills(mode: str, payload: dict) -> Tuple[List[str], List[str]]:
    paths: List[str] = []
    skills: List[str] = []

    def add_path(value: Optional[str]) -> None:
        if value:
            paths.append(value)
            skills.append(skill_root_for_path(value))

    def add_skill(value: Optional[str]) -> None:
        if value:
            skills.append(value)

    if mode == "query":
        for item in payload.get("results", []):
            add_path(item.get("path"))
            add_skill(item.get("skill"))
    elif mode == "decide":
        for item in payload.get("supporting_memory", []):
            add_path(item.get("path"))
        for item in payload.get("recommended_skills", []):
            add_skill(item.get("skill"))
    elif mode == "pinchy":
        for item in payload.get("memory_shortlist", []):
            add_path(item.get("path"))
        add_skill(payload.get("primary_skill"))
        for skill in payload.get("supporting_skills", []):
            add_skill(skill)
    elif mode in {"task-pack", "execute-plan"}:
        for item in payload.get("memory_shortlist", []):
            add_path(item.get("path"))
        selected_pack = payload.get("selected_pack", {})
        add_skill(selected_pack.get("primary_skill"))
        for skill in selected_pack.get("supporting_skills", []):
            add_skill(skill)
        for item in payload.get("recommended_skills", []):
            add_skill(item.get("skill"))

    return list(dict.fromkeys(paths)), list(dict.fromkeys(skills))


def chunk_section(
    path: Path,
    rel_path: str,
    skill: str,
    file_type: str,
    heading: str,
    text: str,
    tags: List[str],
    roles: List[str],
    topics: List[str],
    intents: List[str],
    use_for: List[str],
    avoid_for: List[str],
    confidence: str,
    is_canonical: bool,
    canonical_group: str,
    source: str,
    published_on: str,
    freshness: float,
) -> List[DocChunk]:
    chunk_limit = 900 if file_type in {"memory_note", "reference_note"} else 1200
    block_limit = max(280, min(680, chunk_limit - 220))
    paragraphs = split_blocks(text, block_limit=block_limit)
    chunks: List[DocChunk] = []
    buf: List[str] = []
    size = 0
    index = 0
    section_kind = classify_heading(heading)
    chunk_tags = sorted(set(tags + [section_kind] + topics + intents + use_for))

    for para in paragraphs:
        if size + len(para) > chunk_limit and buf:
            body = "\n\n".join(buf)
            chunk_id = chunk_id_for(rel_path, heading, index, body)
            chunks.append(
                DocChunk(
                    chunk_id=chunk_id,
                    path=rel_path,
                    skill=skill,
                    file_type=file_type,
                    heading=heading,
                    text=body,
                    section_kind=section_kind,
                    source=source,
                    published_on=published_on,
                    freshness=freshness,
                    topics=topics,
                    intents=intents,
                    use_for=use_for,
                    avoid_for=avoid_for,
                    confidence=confidence,
                    tags=chunk_tags,
                    roles=roles,
                    is_canonical=is_canonical,
                    canonical_group=canonical_group,
                )
            )
            index += 1
            buf = [para]
            size = len(para)
        else:
            buf.append(para)
            size += len(para)

    if buf:
        body = "\n\n".join(buf)
        chunk_id = chunk_id_for(rel_path, heading, index, body)
        chunks.append(
            DocChunk(
                chunk_id=chunk_id,
                path=rel_path,
                skill=skill,
                file_type=file_type,
                heading=heading,
                text=body,
                section_kind=section_kind,
                source=source,
                published_on=published_on,
                freshness=freshness,
                topics=topics,
                intents=intents,
                use_for=use_for,
                avoid_for=avoid_for,
                confidence=confidence,
                tags=chunk_tags,
                roles=roles,
                is_canonical=is_canonical,
                canonical_group=canonical_group,
                )
        )

    if len(chunks) >= 2 and len(chunks[-1].text) < max(180, chunk_limit // 5):
        merged_body = f"{chunks[-2].text}\n\n{chunks[-1].text}".strip()
        if len(merged_body) <= int(chunk_limit * 1.15):
            chunks[-2] = dataclasses.replace(
                chunks[-2],
                chunk_id=chunk_id_for(rel_path, heading, len(chunks) - 2, merged_body),
                text=merged_body,
            )
            chunks.pop()
    return chunks


def chunk_index_text(chunk: DocChunk) -> str:
    return " ".join(
        part
        for part in [
            chunk.heading,
            chunk.text,
            " ".join(chunk.tags),
            " ".join(chunk.roles),
            " ".join(chunk.bundles),
            " ".join(chunk.topics),
            " ".join(chunk.intents),
            " ".join(chunk.use_for),
            chunk.section_kind,
            chunk.source,
            chunk.confidence,
        ]
        if part
    )


def parse_canonical_map(skills_root: Path) -> Dict[str, str]:
    path = skills_root / "seo" / "MEMORY.md"
    if not path.exists():
        return {}

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    result: Dict[str, str] = {}
    in_canonical = False
    for line in lines:
        line = line.strip()
        if line.startswith("### Canonical "):
            in_canonical = True
            continue
        if in_canonical and line.startswith("## "):
            break
        if not in_canonical:
            continue
        if line.startswith("- ") and ": `memory/" in line:
            title, rel = line[2:].split(": `", 1)
            rel_path = rel.rstrip("`")
            result[f"seo/{rel_path}"] = title.strip()
    return result


def parse_role_bundles(skills_root: Path) -> Dict[str, List[str]]:
    path = skills_root / "seo" / "MEMORY.md"
    if not path.exists():
        return {}

    bundles: Dict[str, List[str]] = defaultdict(list)
    lines = path.read_text(encoding="utf-8").splitlines()
    current_role: Optional[str] = None
    for raw in lines:
        line = raw.strip()
        if line.startswith("### ") and line.endswith(" Bundle"):
            current_role = line[4:-7].strip().lower()
            continue
        if current_role and line.startswith("- `memory/") and line.endswith("`"):
            bundles[current_role].append(f"seo/{line[3:-1]}")
    return bundles


def parse_bundle_memberships(skills_root: Path) -> Dict[str, List[str]]:
    path = skills_root / "seo" / "MEMORY.md"
    if not path.exists():
        return {}

    memberships: Dict[str, List[str]] = defaultdict(list)
    current_bundle: Optional[str] = None
    lines = path.read_text(encoding="utf-8").splitlines()
    for raw in lines:
        line = raw.strip()
        if line.startswith("### ") and line.endswith(" Bundle"):
            current_bundle = line[4:-7].strip().lower().replace(" ", "_")
            continue
        if current_bundle and line.startswith("- `memory/") and line.endswith("`"):
            rel_path = f"seo/{line[3:-1]}"
            memberships[rel_path].append(current_bundle)
    return memberships


def parse_squad_router(skills_root: Path) -> SquadRouter:
    path = skills_root / "SQUAD_MEMORY.md"
    if not path.exists():
        return SquadRouter(skill_tags={}, role_paths={}, path_bundles={})

    skill_tags: Dict[str, List[str]] = defaultdict(list)
    role_paths: Dict[str, List[str]] = defaultdict(list)
    path_bundles: Dict[str, List[str]] = defaultdict(list)

    mode: Optional[str] = None
    current_skill: Optional[str] = None
    current_role: Optional[str] = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line == "## Skill Tags":
            mode = "skill_tags"
            current_skill = None
            current_role = None
            continue
        if line == "## Role Bundles":
            mode = "role_bundles"
            current_skill = None
            current_role = None
            continue
        if mode == "skill_tags" and line.startswith("### `") and line.endswith("`"):
            current_skill = line[4:-1]
            continue
        if mode == "role_bundles" and line.startswith("### ") and line.endswith(" Bundle"):
            current_role = line[4:-7].strip().lower()
            continue
        if mode == "skill_tags" and current_skill and line.startswith("- tags: "):
            tags = [tag.strip().lower() for tag in line[8:].split(",") if tag.strip()]
            skill_tags[current_skill].extend(tags)
            continue
        if mode == "role_bundles" and current_role:
            if line.startswith("- `") and line.endswith("`"):
                rel_path = line[3:-1]
                role_paths[current_role].append(rel_path)
                path_bundles[rel_path].append(current_role)
                continue
            if line.startswith("- skill `") and line.endswith("`"):
                skill = line[9:-1]
                rel_path = f"{skill}/SKILL.md"
                role_paths[current_role].append(rel_path)
                path_bundles[rel_path].append(current_role)

    return SquadRouter(
        skill_tags={key: sorted(set(value)) for key, value in skill_tags.items()},
        role_paths={key: sorted(set(value)) for key, value in role_paths.items()},
        path_bundles={key: sorted(set(value)) for key, value in path_bundles.items()},
    )


@lru_cache(maxsize=4)
def cached_squad_router(skills_root_str: str, mtime_ns: int, size: int) -> SquadRouter:
    return parse_squad_router(Path(skills_root_str))


def collect_chunks(skills_root: Path) -> Tuple[List[DocChunk], Dict[str, List[str]]]:
    canonical_map = parse_canonical_map(skills_root)
    seo_role_bundles = parse_role_bundles(skills_root)
    seo_bundle_memberships = parse_bundle_memberships(skills_root)
    squad_router = parse_squad_router(skills_root)
    role_bundles: Dict[str, List[str]] = defaultdict(list)
    for role, paths in seo_role_bundles.items():
        role_bundles[role].extend(paths)
    for role, paths in squad_router.role_paths.items():
        role_bundles[role].extend(paths)

    bundle_memberships: Dict[str, List[str]] = defaultdict(list)
    for rel_path, bundles in seo_bundle_memberships.items():
        bundle_memberships[rel_path].extend(bundles)
    for rel_path, bundles in squad_router.path_bundles.items():
        bundle_memberships[rel_path].extend(bundles)

    chunks: List[DocChunk] = []

    for path in sorted(skills_root.rglob("*.md")):
        rel = path.relative_to(skills_root)
        if any(part.startswith(".") and part != ".system" for part in rel.parts):
            continue
        skill = rel.parts[0] if len(rel.parts) > 1 else "squad_router"
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        file_type = doc_type_for(path)
        rel_path = str(rel)
        source = infer_source(skill, rel)
        published_on = extract_published_on(meta, body)
        freshness = freshness_score(published_on)
        tags = parse_tags(meta)
        topics = parse_meta_list(meta, "topic", "topics")
        intents = parse_meta_list(meta, "intent", "intents")
        use_for = parse_meta_list(meta, "use_for")
        avoid_for = parse_meta_list(meta, "avoid_for")
        explicit_roles = parse_meta_list(meta, "role", "roles")
        confidence = meta.get("confidence", "").strip().lower()
        is_canonical, canonical_group = canonical_info_for_doc(
            rel_path,
            meta,
            canonical_map,
            topics,
            meta.get("title", "").strip(),
        )
        tags.extend(squad_router.skill_tags.get(skill, []))
        tags.extend(tokenize(rel.stem.replace("-", " ")))
        tags.extend(tokenize(skill.replace("-", " ")))
        tags.extend(topics)
        tags.extend(intents)
        tags.extend(use_for)
        if confidence:
            tags.append(f"confidence_{confidence}")
        if file_type == "memory_note" and rel.parts[0] == "seo":
            tags.append("seo_memory")
        if file_type == "reference_note":
            tags.append("reference_note")
        if rel.parts[0] == "seo" and rel.parts[-1].startswith("ahrefs-"):
            tags.extend(["source_ahrefs", "ahrefs"])
        if rel.parts[0] == "seo" and rel.parts[-1].startswith("hobo-"):
            tags.extend(["source_hobo", "hobo"])
        if source == "dejan":
            tags.extend(["source_dejan", "dejan", "reverse_engineering"])
        if published_on:
            tags.extend(tokenize(published_on))
        tags = sorted(set(tags))
        bundles = sorted(set(bundle_memberships.get(rel_path, [])))
        roles = sorted(set(SKILL_ALIASES.get(skill, []) + explicit_roles))

        for heading, section_text in parse_markdown_sections(body):
            section_chunks = chunk_section(
                path,
                rel_path,
                skill,
                file_type,
                heading,
                section_text,
                tags,
                roles,
                topics,
                intents,
                use_for,
                avoid_for,
                confidence,
                is_canonical,
                canonical_group,
                source,
                published_on,
                freshness,
            )
            for chunk in section_chunks:
                chunk.bundles = bundles
            chunks.extend(section_chunks)

    return chunks, {role: sorted(set(paths)) for role, paths in role_bundles.items()}


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE chunks (
          chunk_id TEXT PRIMARY KEY,
          path TEXT NOT NULL,
          skill TEXT NOT NULL,
          file_type TEXT NOT NULL,
          heading TEXT NOT NULL,
          text TEXT NOT NULL,
          section_kind TEXT NOT NULL,
          source TEXT NOT NULL,
          published_on TEXT NOT NULL,
          freshness REAL NOT NULL,
          topics_json TEXT NOT NULL,
          intents_json TEXT NOT NULL,
          use_for_json TEXT NOT NULL,
          avoid_for_json TEXT NOT NULL,
          confidence TEXT NOT NULL,
          tags_json TEXT NOT NULL,
          roles_json TEXT NOT NULL,
          bundles_json TEXT NOT NULL,
          is_canonical INTEGER NOT NULL,
          canonical_group TEXT NOT NULL
        );

        CREATE TABLE chunk_weights (
          chunk_id TEXT PRIMARY KEY,
          weights_json TEXT NOT NULL,
          norm REAL NOT NULL
        );

        CREATE TABLE chunk_vectors (
          chunk_id TEXT PRIMARY KEY,
          weights_json TEXT NOT NULL,
          norm REAL NOT NULL
        );

        CREATE TABLE token_vectors (
          token TEXT PRIMARY KEY,
          weights_json TEXT NOT NULL,
          norm REAL NOT NULL
        );

        CREATE TABLE meta (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );

        CREATE TABLE role_bundles (
          role TEXT NOT NULL,
          path TEXT NOT NULL
        );

        CREATE TABLE query_log (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          mode TEXT NOT NULL,
          query TEXT NOT NULL,
          role TEXT,
          skill_filter TEXT,
          top_n INTEGER NOT NULL,
          result_json TEXT NOT NULL
        );

        CREATE TABLE feedback (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          query TEXT NOT NULL,
          path TEXT NOT NULL,
          rating TEXT NOT NULL
        );

        CREATE TABLE events (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          event_type TEXT NOT NULL,
          event_group TEXT NOT NULL DEFAULT '',
          source TEXT NOT NULL DEFAULT '',
          status TEXT NOT NULL DEFAULT '',
          query TEXT NOT NULL DEFAULT '',
          role TEXT,
          pack_id TEXT,
          skill TEXT,
          path TEXT,
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE episodes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts_start TEXT NOT NULL,
          ts_end TEXT NOT NULL,
          episode_key TEXT NOT NULL,
          episode_type TEXT NOT NULL,
          title TEXT NOT NULL,
          status TEXT NOT NULL DEFAULT '',
          role TEXT,
          pack_id TEXT,
          primary_skill TEXT,
          query TEXT NOT NULL DEFAULT '',
          event_count INTEGER NOT NULL DEFAULT 0,
          summary_text TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE episode_items (
          episode_id INTEGER NOT NULL,
          event_id INTEGER NOT NULL,
          seq INTEGER NOT NULL,
          ts TEXT NOT NULL,
          event_type TEXT NOT NULL,
          PRIMARY KEY(episode_id, event_id)
        );

        CREATE TABLE episode_summaries (
          episode_id INTEGER NOT NULL,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          summary_kind TEXT NOT NULL,
          summary_text TEXT NOT NULL,
          metadata_json TEXT NOT NULL DEFAULT '{}',
          PRIMARY KEY(episode_id, summary_kind)
        );

        CREATE TABLE pack_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts_started TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_completed TEXT,
          query TEXT NOT NULL,
          role TEXT,
          pack_id TEXT NOT NULL,
          pack_name TEXT NOT NULL,
          primary_skill TEXT NOT NULL,
          supporting_skills_json TEXT NOT NULL DEFAULT '[]',
          status TEXT NOT NULL CHECK(status IN ('planned', 'active', 'blocked', 'completed', 'failed')),
          current_step_seq INTEGER NOT NULL DEFAULT 0,
          step_count INTEGER NOT NULL DEFAULT 0,
          blocker_count INTEGER NOT NULL DEFAULT 0,
          handoff_count INTEGER NOT NULL DEFAULT 0,
          notes TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE pack_run_steps (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          run_id INTEGER NOT NULL,
          seq INTEGER NOT NULL,
          title TEXT NOT NULL,
          step_kind TEXT NOT NULL DEFAULT 'checklist',
          owner_skill TEXT,
          status TEXT NOT NULL CHECK(status IN ('pending', 'active', 'completed', 'blocked', 'skipped')),
          notes TEXT NOT NULL DEFAULT '',
          artifact_path TEXT NOT NULL DEFAULT '',
          evidence_json TEXT NOT NULL DEFAULT '{}',
          ts_updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE pack_run_handoffs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          run_id INTEGER NOT NULL,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          from_skill TEXT NOT NULL,
          to_skill TEXT NOT NULL,
          reason TEXT NOT NULL DEFAULT '',
          notes TEXT NOT NULL DEFAULT '',
          status TEXT NOT NULL DEFAULT 'sent',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE pack_run_blockers (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          run_id INTEGER NOT NULL,
          ts_opened TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_resolved TEXT,
          step_seq INTEGER,
          title TEXT NOT NULL,
          severity TEXT NOT NULL CHECK(severity IN ('low', 'medium', 'high', 'critical')),
          owner_skill TEXT,
          status TEXT NOT NULL CHECK(status IN ('open', 'resolved')),
          notes TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE workspace_contexts (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_last_used TEXT,
          name TEXT NOT NULL,
          scope_key TEXT NOT NULL,
          status TEXT NOT NULL CHECK(status IN ('active', 'archived')),
          root_path TEXT NOT NULL DEFAULT '',
          role TEXT,
          pack_id TEXT,
          notes TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE workspace_context_items (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          context_id INTEGER NOT NULL,
          path TEXT NOT NULL,
          rel_path TEXT NOT NULL DEFAULT '',
          item_type TEXT NOT NULL DEFAULT 'file',
          title TEXT NOT NULL,
          text TEXT NOT NULL,
          token_count INTEGER NOT NULL DEFAULT 0,
          metadata_json TEXT NOT NULL DEFAULT '{}',
          UNIQUE(context_id, path)
        );

        CREATE TABLE task_outcomes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          query TEXT NOT NULL,
          role TEXT,
          pack_id TEXT NOT NULL,
          primary_skill TEXT NOT NULL,
          supporting_skills_json TEXT NOT NULL,
          used_skills_json TEXT NOT NULL,
          memory_paths_json TEXT NOT NULL,
          status TEXT NOT NULL CHECK(status IN ('accepted', 'revised', 'failed')),
          revision_count INTEGER NOT NULL DEFAULT 0,
          completion_minutes REAL,
          user_rating REAL,
          notes TEXT NOT NULL DEFAULT ''
        );

        CREATE TABLE task_result_scorecards (
          outcome_id INTEGER PRIMARY KEY,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          scorer TEXT NOT NULL DEFAULT 'system',
          scoring_mode TEXT NOT NULL CHECK(scoring_mode IN ('suggested', 'manual')),
          goal_fit_score REAL NOT NULL,
          correctness_score REAL NOT NULL,
          clarity_score REAL NOT NULL,
          completeness_score REAL NOT NULL,
          actionability_score REAL NOT NULL,
          format_score REAL NOT NULL,
          overall_score REAL NOT NULL,
          verdict TEXT NOT NULL CHECK(verdict IN ('excellent', 'strong', 'acceptable', 'weak', 'poor')),
          notes TEXT NOT NULL DEFAULT ''
        );

        CREATE TABLE learned_result_pack_priors (
          bucket TEXT NOT NULL,
          pack_id TEXT NOT NULL,
          score REAL NOT NULL,
          avg_overall_score REAL NOT NULL,
          manual_count INTEGER NOT NULL,
          suggested_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, pack_id)
        );

        CREATE TABLE learned_result_path_priors (
          bucket TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          avg_overall_score REAL NOT NULL,
          manual_count INTEGER NOT NULL,
          suggested_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, path)
        );

        CREATE TABLE learned_result_skill_priors (
          bucket TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          avg_overall_score REAL NOT NULL,
          manual_count INTEGER NOT NULL,
          suggested_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, skill)
        );

        CREATE TABLE learned_path_priors (
          bucket TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          useful_count INTEGER NOT NULL,
          not_useful_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, path)
        );

        CREATE TABLE learned_skill_priors (
          bucket TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          useful_count INTEGER NOT NULL,
          not_useful_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, skill)
        );

        CREATE TABLE learned_pack_priors (
          bucket TEXT NOT NULL,
          pack_id TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, pack_id)
        );

        CREATE TABLE learned_pack_path_priors (
          pack_id TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(pack_id, path)
        );

        CREATE TABLE learned_pack_skill_priors (
          pack_id TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(pack_id, skill)
        );

        CREATE TABLE learned_outcome_path_priors (
          bucket TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, path)
        );

        CREATE TABLE learned_outcome_skill_priors (
          bucket TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, skill)
        );

        CREATE TABLE training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          query_logs INTEGER NOT NULL,
          feedback_rows INTEGER NOT NULL,
          path_priors INTEGER NOT NULL,
          skill_priors INTEGER NOT NULL
        );

        CREATE TABLE pack_training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          task_outcomes INTEGER NOT NULL,
          pack_priors INTEGER NOT NULL,
          pack_path_priors INTEGER NOT NULL,
          pack_skill_priors INTEGER NOT NULL
        );

        CREATE TABLE outcome_training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          task_outcomes INTEGER NOT NULL,
          outcome_path_priors INTEGER NOT NULL,
          outcome_skill_priors INTEGER NOT NULL
        );

        CREATE TABLE result_training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          scored_outcomes INTEGER NOT NULL,
          manual_scorecards INTEGER NOT NULL,
          suggested_scorecards INTEGER NOT NULL,
          result_pack_priors INTEGER NOT NULL,
          result_path_priors INTEGER NOT NULL,
          result_skill_priors INTEGER NOT NULL
        );

        CREATE INDEX idx_events_ts ON events(ts DESC);
        CREATE INDEX idx_events_group ON events(event_group, id DESC);
        CREATE INDEX idx_episodes_end ON episodes(ts_end DESC);
        CREATE INDEX idx_episodes_type ON episodes(episode_type, id DESC);
        CREATE INDEX idx_pack_runs_status ON pack_runs(status, ts_updated DESC);
        CREATE INDEX idx_pack_runs_pack ON pack_runs(pack_id, id DESC);
        CREATE INDEX idx_pack_run_steps_run ON pack_run_steps(run_id, seq);
        CREATE INDEX idx_pack_run_handoffs_run ON pack_run_handoffs(run_id, id DESC);
        CREATE INDEX idx_pack_run_blockers_run ON pack_run_blockers(run_id, status, id DESC);
        CREATE INDEX idx_workspace_contexts_status ON workspace_contexts(status, ts_updated DESC);
        CREATE INDEX idx_workspace_contexts_scope ON workspace_contexts(scope_key, status);
        CREATE INDEX idx_workspace_context_items_context ON workspace_context_items(context_id, id DESC);

        CREATE VIRTUAL TABLE chunks_fts USING fts5(
          chunk_id UNINDEXED,
          path,
          heading,
          text,
          section_kind,
          source,
          topics,
          intents,
          use_for,
          confidence,
          tags,
          roles,
          bundles
        );
        """
    )


def ensure_learning_tables(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS task_outcomes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          query TEXT NOT NULL,
          role TEXT,
          pack_id TEXT NOT NULL,
          primary_skill TEXT NOT NULL,
          supporting_skills_json TEXT NOT NULL,
          used_skills_json TEXT NOT NULL,
          memory_paths_json TEXT NOT NULL,
          status TEXT NOT NULL CHECK(status IN ('accepted', 'revised', 'failed')),
          revision_count INTEGER NOT NULL DEFAULT 0,
          completion_minutes REAL,
          user_rating REAL,
          notes TEXT NOT NULL DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS task_result_scorecards (
          outcome_id INTEGER PRIMARY KEY,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          scorer TEXT NOT NULL DEFAULT 'system',
          scoring_mode TEXT NOT NULL CHECK(scoring_mode IN ('suggested', 'manual')),
          goal_fit_score REAL NOT NULL,
          correctness_score REAL NOT NULL,
          clarity_score REAL NOT NULL,
          completeness_score REAL NOT NULL,
          actionability_score REAL NOT NULL,
          format_score REAL NOT NULL,
          overall_score REAL NOT NULL,
          verdict TEXT NOT NULL CHECK(verdict IN ('excellent', 'strong', 'acceptable', 'weak', 'poor')),
          notes TEXT NOT NULL DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS events (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          event_type TEXT NOT NULL,
          event_group TEXT NOT NULL DEFAULT '',
          source TEXT NOT NULL DEFAULT '',
          status TEXT NOT NULL DEFAULT '',
          query TEXT NOT NULL DEFAULT '',
          role TEXT,
          pack_id TEXT,
          skill TEXT,
          path TEXT,
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS episodes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts_start TEXT NOT NULL,
          ts_end TEXT NOT NULL,
          episode_key TEXT NOT NULL,
          episode_type TEXT NOT NULL,
          title TEXT NOT NULL,
          status TEXT NOT NULL DEFAULT '',
          role TEXT,
          pack_id TEXT,
          primary_skill TEXT,
          query TEXT NOT NULL DEFAULT '',
          event_count INTEGER NOT NULL DEFAULT 0,
          summary_text TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS episode_items (
          episode_id INTEGER NOT NULL,
          event_id INTEGER NOT NULL,
          seq INTEGER NOT NULL,
          ts TEXT NOT NULL,
          event_type TEXT NOT NULL,
          PRIMARY KEY(episode_id, event_id)
        );

        CREATE TABLE IF NOT EXISTS episode_summaries (
          episode_id INTEGER NOT NULL,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          summary_kind TEXT NOT NULL,
          summary_text TEXT NOT NULL,
          metadata_json TEXT NOT NULL DEFAULT '{}',
          PRIMARY KEY(episode_id, summary_kind)
        );

        CREATE TABLE IF NOT EXISTS pack_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts_started TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_completed TEXT,
          query TEXT NOT NULL,
          role TEXT,
          pack_id TEXT NOT NULL,
          pack_name TEXT NOT NULL,
          primary_skill TEXT NOT NULL,
          supporting_skills_json TEXT NOT NULL DEFAULT '[]',
          status TEXT NOT NULL CHECK(status IN ('planned', 'active', 'blocked', 'completed', 'failed')),
          current_step_seq INTEGER NOT NULL DEFAULT 0,
          step_count INTEGER NOT NULL DEFAULT 0,
          blocker_count INTEGER NOT NULL DEFAULT 0,
          handoff_count INTEGER NOT NULL DEFAULT 0,
          notes TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS pack_run_steps (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          run_id INTEGER NOT NULL,
          seq INTEGER NOT NULL,
          title TEXT NOT NULL,
          step_kind TEXT NOT NULL DEFAULT 'checklist',
          owner_skill TEXT,
          status TEXT NOT NULL CHECK(status IN ('pending', 'active', 'completed', 'blocked', 'skipped')),
          notes TEXT NOT NULL DEFAULT '',
          artifact_path TEXT NOT NULL DEFAULT '',
          evidence_json TEXT NOT NULL DEFAULT '{}',
          ts_updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS pack_run_handoffs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          run_id INTEGER NOT NULL,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          from_skill TEXT NOT NULL,
          to_skill TEXT NOT NULL,
          reason TEXT NOT NULL DEFAULT '',
          notes TEXT NOT NULL DEFAULT '',
          status TEXT NOT NULL DEFAULT 'sent',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS pack_run_blockers (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          run_id INTEGER NOT NULL,
          ts_opened TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_resolved TEXT,
          step_seq INTEGER,
          title TEXT NOT NULL,
          severity TEXT NOT NULL CHECK(severity IN ('low', 'medium', 'high', 'critical')),
          owner_skill TEXT,
          status TEXT NOT NULL CHECK(status IN ('open', 'resolved')),
          notes TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS workspace_contexts (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          ts_last_used TEXT,
          name TEXT NOT NULL,
          scope_key TEXT NOT NULL,
          status TEXT NOT NULL CHECK(status IN ('active', 'archived')),
          root_path TEXT NOT NULL DEFAULT '',
          role TEXT,
          pack_id TEXT,
          notes TEXT NOT NULL DEFAULT '',
          metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS workspace_context_items (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          context_id INTEGER NOT NULL,
          path TEXT NOT NULL,
          rel_path TEXT NOT NULL DEFAULT '',
          item_type TEXT NOT NULL DEFAULT 'file',
          title TEXT NOT NULL,
          text TEXT NOT NULL,
          token_count INTEGER NOT NULL DEFAULT 0,
          metadata_json TEXT NOT NULL DEFAULT '{}',
          UNIQUE(context_id, path)
        );

        CREATE INDEX IF NOT EXISTS idx_events_ts ON events(ts DESC);
        CREATE INDEX IF NOT EXISTS idx_events_group ON events(event_group, id DESC);
        CREATE INDEX IF NOT EXISTS idx_episodes_end ON episodes(ts_end DESC);
        CREATE INDEX IF NOT EXISTS idx_episodes_type ON episodes(episode_type, id DESC);
        CREATE INDEX IF NOT EXISTS idx_pack_runs_status ON pack_runs(status, ts_updated DESC);
        CREATE INDEX IF NOT EXISTS idx_pack_runs_pack ON pack_runs(pack_id, id DESC);
        CREATE INDEX IF NOT EXISTS idx_pack_run_steps_run ON pack_run_steps(run_id, seq);
        CREATE INDEX IF NOT EXISTS idx_pack_run_handoffs_run ON pack_run_handoffs(run_id, id DESC);
        CREATE INDEX IF NOT EXISTS idx_pack_run_blockers_run ON pack_run_blockers(run_id, status, id DESC);
        CREATE INDEX IF NOT EXISTS idx_workspace_contexts_status ON workspace_contexts(status, ts_updated DESC);
        CREATE INDEX IF NOT EXISTS idx_workspace_contexts_scope ON workspace_contexts(scope_key, status);
        CREATE INDEX IF NOT EXISTS idx_workspace_context_items_context ON workspace_context_items(context_id, id DESC);

        CREATE TABLE IF NOT EXISTS learned_result_pack_priors (
          bucket TEXT NOT NULL,
          pack_id TEXT NOT NULL,
          score REAL NOT NULL,
          avg_overall_score REAL NOT NULL,
          manual_count INTEGER NOT NULL,
          suggested_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, pack_id)
        );

        CREATE TABLE IF NOT EXISTS learned_result_path_priors (
          bucket TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          avg_overall_score REAL NOT NULL,
          manual_count INTEGER NOT NULL,
          suggested_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, path)
        );

        CREATE TABLE IF NOT EXISTS learned_result_skill_priors (
          bucket TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          avg_overall_score REAL NOT NULL,
          manual_count INTEGER NOT NULL,
          suggested_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, skill)
        );

        CREATE TABLE IF NOT EXISTS learned_path_priors (
          bucket TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          useful_count INTEGER NOT NULL,
          not_useful_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, path)
        );

        CREATE TABLE IF NOT EXISTS learned_skill_priors (
          bucket TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          useful_count INTEGER NOT NULL,
          not_useful_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, skill)
        );

        CREATE TABLE IF NOT EXISTS learned_pack_priors (
          bucket TEXT NOT NULL,
          pack_id TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, pack_id)
        );

        CREATE TABLE IF NOT EXISTS learned_pack_path_priors (
          pack_id TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(pack_id, path)
        );

        CREATE TABLE IF NOT EXISTS learned_pack_skill_priors (
          pack_id TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(pack_id, skill)
        );

        CREATE TABLE IF NOT EXISTS learned_outcome_path_priors (
          bucket TEXT NOT NULL,
          path TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, path)
        );

        CREATE TABLE IF NOT EXISTS learned_outcome_skill_priors (
          bucket TEXT NOT NULL,
          skill TEXT NOT NULL,
          score REAL NOT NULL,
          accepted_count INTEGER NOT NULL,
          revised_count INTEGER NOT NULL,
          failed_count INTEGER NOT NULL,
          exposure_count INTEGER NOT NULL,
          PRIMARY KEY(bucket, skill)
        );

        CREATE TABLE IF NOT EXISTS training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          query_logs INTEGER NOT NULL,
          feedback_rows INTEGER NOT NULL,
          path_priors INTEGER NOT NULL,
          skill_priors INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS pack_training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          task_outcomes INTEGER NOT NULL,
          pack_priors INTEGER NOT NULL,
          pack_path_priors INTEGER NOT NULL,
          pack_skill_priors INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS outcome_training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          task_outcomes INTEGER NOT NULL,
          outcome_path_priors INTEGER NOT NULL,
          outcome_skill_priors INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS result_training_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          scored_outcomes INTEGER NOT NULL,
          manual_scorecards INTEGER NOT NULL,
          suggested_scorecards INTEGER NOT NULL,
          result_pack_priors INTEGER NOT NULL,
          result_path_priors INTEGER NOT NULL,
          result_skill_priors INTEGER NOT NULL
        );
        """
    )


def copy_usage_tables(old_db_path: Path, con: sqlite3.Connection) -> None:
    if not old_db_path.exists():
        return

    old = sqlite3.connect(str(old_db_path))
    try:
        tables = {row[0] for row in old.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        if "query_log" in tables:
            for row in old.execute("SELECT id, ts, mode, query, role, skill_filter, top_n, result_json FROM query_log ORDER BY id"):
                con.execute(
                    "INSERT INTO query_log(id, ts, mode, query, role, skill_filter, top_n, result_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    row,
                )
        if "feedback" in tables:
            for row in old.execute("SELECT id, ts, query, path, rating FROM feedback ORDER BY id"):
                con.execute(
                    "INSERT INTO feedback(id, ts, query, path, rating) VALUES (?, ?, ?, ?, ?)",
                    row,
                )
        if "events" in tables:
            for row in old.execute(
                """
                SELECT id, ts, event_type, event_group, source, status, query, role, pack_id, skill, path, metadata_json
                FROM events
                ORDER BY id
                """
            ):
                con.execute(
                    """
                    INSERT INTO events(
                      id, ts, event_type, event_group, source, status, query, role, pack_id, skill, path, metadata_json
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "episodes" in tables:
            for row in old.execute(
                """
                SELECT id, ts_start, ts_end, episode_key, episode_type, title, status, role, pack_id,
                       primary_skill, query, event_count, summary_text, metadata_json
                FROM episodes
                ORDER BY id
                """
            ):
                con.execute(
                    """
                    INSERT INTO episodes(
                      id, ts_start, ts_end, episode_key, episode_type, title, status, role, pack_id,
                      primary_skill, query, event_count, summary_text, metadata_json
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "episode_items" in tables:
            for row in old.execute(
                """
                SELECT episode_id, event_id, seq, ts, event_type
                FROM episode_items
                ORDER BY episode_id, seq
                """
            ):
                con.execute(
                    """
                    INSERT INTO episode_items(episode_id, event_id, seq, ts, event_type)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "episode_summaries" in tables:
            for row in old.execute(
                """
                SELECT episode_id, ts, summary_kind, summary_text, metadata_json
                FROM episode_summaries
                ORDER BY episode_id, summary_kind
                """
            ):
                con.execute(
                    """
                    INSERT INTO episode_summaries(episode_id, ts, summary_kind, summary_text, metadata_json)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "pack_runs" in tables:
            for row in old.execute(
                """
                SELECT id, ts_started, ts_updated, ts_completed, query, role, pack_id, pack_name, primary_skill,
                       supporting_skills_json, status, current_step_seq, step_count, blocker_count, handoff_count,
                       notes, metadata_json
                FROM pack_runs
                ORDER BY id
                """
            ):
                con.execute(
                    """
                    INSERT INTO pack_runs(
                      id, ts_started, ts_updated, ts_completed, query, role, pack_id, pack_name, primary_skill,
                      supporting_skills_json, status, current_step_seq, step_count, blocker_count, handoff_count,
                      notes, metadata_json
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "pack_run_steps" in tables:
            for row in old.execute(
                """
                SELECT id, run_id, seq, title, step_kind, owner_skill, status, notes, artifact_path, evidence_json, ts_updated
                FROM pack_run_steps
                ORDER BY run_id, seq, id
                """
            ):
                con.execute(
                    """
                    INSERT INTO pack_run_steps(
                      id, run_id, seq, title, step_kind, owner_skill, status, notes, artifact_path, evidence_json, ts_updated
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "pack_run_handoffs" in tables:
            for row in old.execute(
                """
                SELECT id, run_id, ts, from_skill, to_skill, reason, notes, status, metadata_json
                FROM pack_run_handoffs
                ORDER BY run_id, id
                """
            ):
                con.execute(
                    """
                    INSERT INTO pack_run_handoffs(id, run_id, ts, from_skill, to_skill, reason, notes, status, metadata_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "pack_run_blockers" in tables:
            for row in old.execute(
                """
                SELECT id, run_id, ts_opened, ts_resolved, step_seq, title, severity, owner_skill, status, notes, metadata_json
                FROM pack_run_blockers
                ORDER BY run_id, id
                """
            ):
                con.execute(
                    """
                    INSERT INTO pack_run_blockers(
                      id, run_id, ts_opened, ts_resolved, step_seq, title, severity, owner_skill, status, notes, metadata_json
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "workspace_contexts" in tables:
            for row in old.execute(
                """
                SELECT id, ts_created, ts_updated, ts_last_used, name, scope_key, status, root_path, role, pack_id, notes, metadata_json
                FROM workspace_contexts
                ORDER BY id
                """
            ):
                con.execute(
                    """
                    INSERT INTO workspace_contexts(
                      id, ts_created, ts_updated, ts_last_used, name, scope_key, status, root_path, role, pack_id, notes, metadata_json
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "workspace_context_items" in tables:
            for row in old.execute(
                """
                SELECT id, context_id, path, rel_path, item_type, title, text, token_count, metadata_json
                FROM workspace_context_items
                ORDER BY context_id, id
                """
            ):
                con.execute(
                    """
                    INSERT INTO workspace_context_items(
                      id, context_id, path, rel_path, item_type, title, text, token_count, metadata_json
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "task_outcomes" in tables:
            for row in old.execute(
                """
                SELECT id, ts, query, role, pack_id, primary_skill, supporting_skills_json, used_skills_json,
                       memory_paths_json, status, revision_count, completion_minutes, user_rating, notes
                FROM task_outcomes
                ORDER BY id
                """
            ):
                con.execute(
                    """
                    INSERT INTO task_outcomes(
                      id, ts, query, role, pack_id, primary_skill, supporting_skills_json, used_skills_json,
                      memory_paths_json, status, revision_count, completion_minutes, user_rating, notes
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "task_result_scorecards" in tables:
            for row in old.execute(
                """
                SELECT outcome_id, ts, scorer, scoring_mode, goal_fit_score, correctness_score, clarity_score,
                       completeness_score, actionability_score, format_score, overall_score, verdict, notes
                FROM task_result_scorecards
                ORDER BY outcome_id
                """
            ):
                con.execute(
                    """
                    INSERT INTO task_result_scorecards(
                      outcome_id, ts, scorer, scoring_mode, goal_fit_score, correctness_score, clarity_score,
                      completeness_score, actionability_score, format_score, overall_score, verdict, notes
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "training_runs" in tables:
            for row in old.execute("SELECT id, ts, query_logs, feedback_rows, path_priors, skill_priors FROM training_runs ORDER BY id"):
                con.execute(
                    "INSERT INTO training_runs(id, ts, query_logs, feedback_rows, path_priors, skill_priors) VALUES (?, ?, ?, ?, ?, ?)",
                    row,
                )
        if "pack_training_runs" in tables:
            for row in old.execute(
                "SELECT id, ts, task_outcomes, pack_priors, pack_path_priors, pack_skill_priors FROM pack_training_runs ORDER BY id"
            ):
                con.execute(
                    """
                    INSERT INTO pack_training_runs(id, ts, task_outcomes, pack_priors, pack_path_priors, pack_skill_priors)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_pack_priors" in tables:
            for row in old.execute(
                """
                SELECT bucket, pack_id, score, accepted_count, revised_count, failed_count, exposure_count
                FROM learned_pack_priors
                ORDER BY bucket, pack_id
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_pack_priors(bucket, pack_id, score, accepted_count, revised_count, failed_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_pack_path_priors" in tables:
            for row in old.execute(
                """
                SELECT pack_id, path, score, accepted_count, revised_count, failed_count, exposure_count
                FROM learned_pack_path_priors
                ORDER BY pack_id, path
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_pack_path_priors(pack_id, path, score, accepted_count, revised_count, failed_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_pack_skill_priors" in tables:
            for row in old.execute(
                """
                SELECT pack_id, skill, score, accepted_count, revised_count, failed_count, exposure_count
                FROM learned_pack_skill_priors
                ORDER BY pack_id, skill
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_pack_skill_priors(pack_id, skill, score, accepted_count, revised_count, failed_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_outcome_path_priors" in tables:
            for row in old.execute(
                """
                SELECT bucket, path, score, accepted_count, revised_count, failed_count, exposure_count
                FROM learned_outcome_path_priors
                ORDER BY bucket, path
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_outcome_path_priors(bucket, path, score, accepted_count, revised_count, failed_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_outcome_skill_priors" in tables:
            for row in old.execute(
                """
                SELECT bucket, skill, score, accepted_count, revised_count, failed_count, exposure_count
                FROM learned_outcome_skill_priors
                ORDER BY bucket, skill
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_outcome_skill_priors(bucket, skill, score, accepted_count, revised_count, failed_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "outcome_training_runs" in tables:
            for row in old.execute(
                """
                SELECT id, ts, task_outcomes, outcome_path_priors, outcome_skill_priors
                FROM outcome_training_runs
                ORDER BY id
                """
            ):
                con.execute(
                    """
                    INSERT INTO outcome_training_runs(id, ts, task_outcomes, outcome_path_priors, outcome_skill_priors)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_result_pack_priors" in tables:
            for row in old.execute(
                """
                SELECT bucket, pack_id, score, avg_overall_score, manual_count, suggested_count, exposure_count
                FROM learned_result_pack_priors
                ORDER BY bucket, pack_id
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_result_pack_priors(bucket, pack_id, score, avg_overall_score, manual_count, suggested_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_result_path_priors" in tables:
            for row in old.execute(
                """
                SELECT bucket, path, score, avg_overall_score, manual_count, suggested_count, exposure_count
                FROM learned_result_path_priors
                ORDER BY bucket, path
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_result_path_priors(bucket, path, score, avg_overall_score, manual_count, suggested_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "learned_result_skill_priors" in tables:
            for row in old.execute(
                """
                SELECT bucket, skill, score, avg_overall_score, manual_count, suggested_count, exposure_count
                FROM learned_result_skill_priors
                ORDER BY bucket, skill
                """
            ):
                con.execute(
                    """
                    INSERT INTO learned_result_skill_priors(bucket, skill, score, avg_overall_score, manual_count, suggested_count, exposure_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
        if "result_training_runs" in tables:
            for row in old.execute(
                """
                SELECT id, ts, scored_outcomes, manual_scorecards, suggested_scorecards,
                       result_pack_priors, result_path_priors, result_skill_priors
                FROM result_training_runs
                ORDER BY id
                """
            ):
                con.execute(
                    """
                    INSERT INTO result_training_runs(
                      id, ts, scored_outcomes, manual_scorecards, suggested_scorecards,
                      result_pack_priors, result_path_priors, result_skill_priors
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    row,
                )
    finally:
        old.close()


def build_index(skills_root: Path, db_path: Path) -> None:
    chunks, role_bundles = collect_chunks(skills_root)
    doc_freq: Dict[str, int] = Counter()
    tokenized: Dict[str, Counter] = {}

    for chunk in chunks:
        counts = Counter(tokenize(chunk_index_text(chunk)))
        tokenized[chunk.chunk_id] = counts
        for token in counts:
            doc_freq[token] += 1

    total_docs = max(len(chunks), 1)
    token_semantic_vectors = build_token_semantic_vectors(tokenized, doc_freq, total_docs)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    temp_db_path = db_path.with_suffix(db_path.suffix + ".tmp")
    if temp_db_path.exists():
        temp_db_path.unlink()

    con = sqlite3.connect(str(temp_db_path))
    ensure_schema(con)
    copy_usage_tables(db_path, con)

    for chunk in chunks:
        counts = tokenized[chunk.chunk_id]
        weights = {}
        norm_sq = 0.0
        total_terms = sum(counts.values()) or 1
        for token, tf_count in counts.items():
            tf = tf_count / total_terms
            idf = math.log(1 + (total_docs / (1 + doc_freq[token])))
            weight = tf * idf
            weights[token] = weight
            norm_sq += weight * weight

        con.execute(
            """
            INSERT INTO chunks(
              chunk_id, path, skill, file_type, heading, text, section_kind, source, published_on, freshness,
              topics_json, intents_json, use_for_json, avoid_for_json, confidence,
              tags_json, roles_json, bundles_json, is_canonical, canonical_group
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                chunk.chunk_id,
                chunk.path,
                chunk.skill,
                chunk.file_type,
                chunk.heading,
                chunk.text,
                chunk.section_kind,
                chunk.source,
                chunk.published_on,
                chunk.freshness,
                json.dumps(chunk.topics),
                json.dumps(chunk.intents),
                json.dumps(chunk.use_for),
                json.dumps(chunk.avoid_for),
                chunk.confidence,
                json.dumps(chunk.tags),
                json.dumps(chunk.roles),
                json.dumps(chunk.bundles),
                1 if chunk.is_canonical else 0,
                chunk.canonical_group,
            ),
        )
        con.execute(
            "INSERT INTO chunk_weights(chunk_id, weights_json, norm) VALUES (?, ?, ?)",
            (chunk.chunk_id, json.dumps(weights), math.sqrt(norm_sq) or 1.0),
        )
        vector_weights, vector_norm = semantic_vector_from_counts(counts, token_semantic_vectors, total_terms=total_terms)
        con.execute(
            "INSERT INTO chunk_vectors(chunk_id, weights_json, norm) VALUES (?, ?, ?)",
            (chunk.chunk_id, json.dumps(vector_weights), vector_norm),
        )
        con.execute(
            """
            INSERT INTO chunks_fts(chunk_id, path, heading, text, section_kind, source, topics, intents, use_for, confidence, tags, roles, bundles)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                chunk.chunk_id,
                chunk.path,
                chunk.heading,
                chunk.text,
                chunk.section_kind,
                chunk.source,
                " ".join(chunk.topics),
                " ".join(chunk.intents),
                " ".join(chunk.use_for),
                chunk.confidence,
                " ".join(chunk.tags),
                " ".join(chunk.roles),
                " ".join(chunk.bundles),
            ),
        )

    for token, (weights, norm) in token_semantic_vectors.items():
        con.execute(
            "INSERT INTO token_vectors(token, weights_json, norm) VALUES (?, ?, ?)",
            (token, json.dumps(weights), norm),
        )

    for role, paths in role_bundles.items():
        for path in paths:
            con.execute("INSERT INTO role_bundles(role, path) VALUES (?, ?)", (role, path))

    con.execute("INSERT INTO meta(key, value) VALUES (?, ?)", ("total_docs", str(total_docs)))
    con.execute("INSERT INTO meta(key, value) VALUES (?, ?)", ("doc_freq", json.dumps(doc_freq)))
    train_summary = train_usage_priors_in_connection(con)
    pack_summary = train_pack_priors_in_connection(con)
    outcome_summary = train_outcome_priors_in_connection(con)
    result_summary = train_result_priors_in_connection(con)
    episode_summary = rebuild_episodes_in_connection(con)
    train_summary = {**train_summary, **pack_summary, **outcome_summary, **result_summary, **episode_summary}
    con.commit()
    con.close()
    os.replace(temp_db_path, db_path)

    print(
        f"Built index with {len(chunks)} chunks into {db_path} "
        f"(trained {train_summary['path_priors']} path priors, {train_summary['skill_priors']} skill priors, "
        f"{train_summary['pack_priors']} pack priors, "
        f"{train_summary['outcome_path_priors']} outcome path priors, "
        f"{train_summary['outcome_skill_priors']} outcome skill priors, "
        f"{train_summary['result_pack_priors']} result pack priors, "
        f"{train_summary['result_path_priors']} result path priors, "
        f"{train_summary['result_skill_priors']} result skill priors, "
        f"{train_summary['episodes']} episodes)"
    )


def load_meta(con: sqlite3.Connection) -> Tuple[int, Dict[str, int]]:
    rows = dict(con.execute("SELECT key, value FROM meta").fetchall())
    total_docs = int(rows["total_docs"])
    doc_freq = json.loads(rows["doc_freq"])
    return total_docs, doc_freq


@lru_cache(maxsize=4)
def cached_load_meta(db_path_str: str, mtime_ns: int, size: int) -> Tuple[int, Dict[str, int]]:
    con = sqlite3.connect(db_path_str)
    try:
        return load_meta(con)
    finally:
        con.close()


def query_weights(query: str, total_docs: int, doc_freq: Dict[str, int]) -> Tuple[Dict[str, float], float]:
    counts = Counter(tokenize(query))
    total_terms = sum(counts.values()) or 1
    weights = {}
    norm_sq = 0.0
    for token, tf_count in counts.items():
        tf = tf_count / total_terms
        idf = math.log(1 + (total_docs / (1 + int(doc_freq.get(token, 0)))))
        weight = tf * idf
        weights[token] = weight
        norm_sq += weight * weight
    return weights, math.sqrt(norm_sq) or 1.0


def sparse_cosine(query_w: Dict[str, float], query_norm: float, doc_w: Dict[str, float], doc_norm: float) -> float:
    dot = 0.0
    for token, weight in query_w.items():
        dot += weight * doc_w.get(token, 0.0)
    return dot / (query_norm * doc_norm) if dot else 0.0


def build_token_semantic_vectors(tokenized: Dict[str, Counter], doc_freq: Dict[str, int], total_docs: int) -> Dict[str, Tuple[Dict[str, float], float]]:
    token_contexts: Dict[str, Counter] = defaultdict(Counter)

    for counts in tokenized.values():
        semantic_tokens = [
            token
            for token, _count in counts.most_common(48)
            if is_semantic_token(token, total_docs, doc_freq)
        ]
        if len(semantic_tokens) < 2:
            continue
        for token in semantic_tokens:
            token_count = counts[token]
            for other in semantic_tokens:
                if other == token:
                    continue
                token_contexts[token][other] += min(token_count, counts[other])

    vectors: Dict[str, Tuple[Dict[str, float], float]] = {}
    for token, contexts in token_contexts.items():
        weighted: Dict[str, float] = {}
        for context, count in contexts.most_common(DEFAULT_TOKEN_CONTEXT_LIMIT):
            idf = math.log(1 + (total_docs / (1 + int(doc_freq.get(context, 0)))))
            weighted[context] = math.log1p(count) * idf
        compact, norm = top_sparse(weighted, DEFAULT_TOKEN_CONTEXT_LIMIT)
        if compact:
            vectors[token] = (compact, norm)
    return vectors


def semantic_vector_from_counts(
    counts: Counter,
    token_vectors: Dict[str, Tuple[Dict[str, float], float]],
    total_terms: Optional[int] = None,
    limit: int = DEFAULT_VECTOR_DIM_LIMIT,
) -> Tuple[Dict[str, float], float]:
    if total_terms is None:
        total_terms = sum(counts.values()) or 1

    aggregate: Dict[str, float] = defaultdict(float)
    for token, token_count in counts.items():
        vector_row = token_vectors.get(token)
        if not vector_row:
            continue
        token_weights, _norm = vector_row
        multiplier = token_count / total_terms
        for dim, weight in token_weights.items():
            aggregate[dim] += multiplier * weight
    return top_sparse(dict(aggregate), limit)


def fetch_role_paths(con: sqlite3.Connection, role: Optional[str]) -> set:
    if not role:
        return set()
    rows = con.execute("SELECT path FROM role_bundles WHERE role = ?", (role.lower(),)).fetchall()
    return {row[0] for row in rows}


@lru_cache(maxsize=32)
def cached_role_paths(db_path_str: str, mtime_ns: int, size: int, role: str) -> Tuple[str, ...]:
    con = sqlite3.connect(db_path_str)
    try:
        return tuple(sorted(fetch_role_paths(con, role)))
    finally:
        con.close()


def fetch_path_feedback(con: sqlite3.Connection) -> Dict[str, float]:
    rows = con.execute(
        """
        SELECT path,
               SUM(CASE WHEN rating='useful' THEN 1 ELSE -1 END) AS score
        FROM feedback
        GROUP BY path
        """
    ).fetchall()
    return {path: float(score) for path, score in rows}


@lru_cache(maxsize=4)
def cached_path_feedback(db_path_str: str, mtime_ns: int, size: int) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_path_feedback(con)
    finally:
        con.close()


def skill_feedback_scores(con: sqlite3.Connection) -> Dict[str, float]:
    rows = con.execute(
        """
        SELECT substr(path, 1, instr(path, '/') - 1) AS skill_root,
               SUM(CASE WHEN rating='useful' THEN 1 ELSE -1 END) AS score
        FROM feedback
        WHERE instr(path, '/') > 0
        GROUP BY skill_root
        """
    ).fetchall()
    return {skill_root: float(score) for skill_root, score in rows}


@lru_cache(maxsize=4)
def cached_skill_feedback(db_path_str: str, mtime_ns: int, size: int) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return skill_feedback_scores(con)
    finally:
        con.close()


def learned_bucket_key(inferred_intents: Sequence[str]) -> Tuple[str, ...]:
    return tuple([GLOBAL_BUCKET] + sorted(set(inferred_intents)))


def role_bucket_key(inferred_intents: Sequence[str], role: Optional[str]) -> Tuple[str, ...]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    if role:
        buckets.append(f"role:{role.lower()}")
    return tuple(buckets)


def fetch_learned_path_priors(con: sqlite3.Connection, inferred_intents: Sequence[str]) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, path, score FROM learned_path_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, path, score in rows:
        scores[path] += float(score) * (0.6 if bucket == GLOBAL_BUCKET else 1.0)
    return dict(scores)


@lru_cache(maxsize=64)
def cached_learned_path_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...]
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_learned_path_priors(con, buckets)
    finally:
        con.close()


def fetch_learned_skill_priors(con: sqlite3.Connection, inferred_intents: Sequence[str]) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, skill, score FROM learned_skill_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, skill, score in rows:
        scores[skill] += float(score) * (0.6 if bucket == GLOBAL_BUCKET else 1.0)
    return dict(scores)


@lru_cache(maxsize=64)
def cached_learned_skill_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...]
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_learned_skill_priors(con, buckets)
    finally:
        con.close()


def fetch_outcome_path_priors(
    con: sqlite3.Connection, inferred_intents: Sequence[str], role: Optional[str]
) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    if role:
        buckets.append(f"role:{role.lower()}")
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, path, score FROM learned_outcome_path_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, path, score in rows:
        weight = 0.6 if bucket == GLOBAL_BUCKET else 1.0
        if role and bucket == f"role:{role.lower()}":
            weight = 1.1
        scores[path] += float(score) * weight
    return dict(scores)


@lru_cache(maxsize=64)
def cached_outcome_path_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...], role_key: str
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_outcome_path_priors(con, buckets, role_key or None)
    finally:
        con.close()


def fetch_outcome_skill_priors(
    con: sqlite3.Connection, inferred_intents: Sequence[str], role: Optional[str]
) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    if role:
        buckets.append(f"role:{role.lower()}")
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, skill, score FROM learned_outcome_skill_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, skill, score in rows:
        weight = 0.6 if bucket == GLOBAL_BUCKET else 1.0
        if role and bucket == f"role:{role.lower()}":
            weight = 1.1
        scores[skill] += float(score) * weight
    return dict(scores)


@lru_cache(maxsize=64)
def cached_outcome_skill_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...], role_key: str
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_outcome_skill_priors(con, buckets, role_key or None)
    finally:
        con.close()


def fetch_learned_pack_priors(con: sqlite3.Connection, inferred_intents: Sequence[str], role: Optional[str]) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    if role:
        buckets.append(f"role:{role.lower()}")
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, pack_id, score FROM learned_pack_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, pack_id, score in rows:
        weight = 0.6 if bucket == GLOBAL_BUCKET else 1.0
        if role and bucket == f"role:{role.lower()}":
            weight = 1.1
        scores[pack_id] += float(score) * weight
    return dict(scores)


@lru_cache(maxsize=64)
def cached_learned_pack_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...], role_key: str
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_learned_pack_priors(con, buckets, role_key or None)
    finally:
        con.close()


def fetch_result_path_priors(
    con: sqlite3.Connection, inferred_intents: Sequence[str], role: Optional[str]
) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    if role:
        buckets.append(f"role:{role.lower()}")
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, path, score FROM learned_result_path_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, path, score in rows:
        weight = 0.6 if bucket == GLOBAL_BUCKET else 1.0
        if role and bucket == f"role:{role.lower()}":
            weight = 1.1
        scores[path] += float(score) * weight
    return dict(scores)


@lru_cache(maxsize=64)
def cached_result_path_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...], role_key: str
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_result_path_priors(con, buckets, role_key or None)
    finally:
        con.close()


def fetch_result_skill_priors(
    con: sqlite3.Connection, inferred_intents: Sequence[str], role: Optional[str]
) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    if role:
        buckets.append(f"role:{role.lower()}")
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, skill, score FROM learned_result_skill_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, skill, score in rows:
        weight = 0.6 if bucket == GLOBAL_BUCKET else 1.0
        if role and bucket == f"role:{role.lower()}":
            weight = 1.1
        scores[skill] += float(score) * weight
    return dict(scores)


@lru_cache(maxsize=64)
def cached_result_skill_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...], role_key: str
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_result_skill_priors(con, buckets, role_key or None)
    finally:
        con.close()


def fetch_result_pack_priors(
    con: sqlite3.Connection, inferred_intents: Sequence[str], role: Optional[str]
) -> Dict[str, float]:
    buckets = [GLOBAL_BUCKET] + sorted(set(inferred_intents))
    if role:
        buckets.append(f"role:{role.lower()}")
    placeholders = ", ".join("?" for _ in buckets)
    rows = con.execute(
        f"SELECT bucket, pack_id, score FROM learned_result_pack_priors WHERE bucket IN ({placeholders})",
        buckets,
    ).fetchall()
    scores: Dict[str, float] = defaultdict(float)
    for bucket, pack_id, score in rows:
        weight = 0.6 if bucket == GLOBAL_BUCKET else 1.0
        if role and bucket == f"role:{role.lower()}":
            weight = 1.1
        scores[pack_id] += float(score) * weight
    return dict(scores)


@lru_cache(maxsize=64)
def cached_result_pack_priors(
    db_path_str: str, mtime_ns: int, size: int, buckets: Tuple[str, ...], role_key: str
) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_result_pack_priors(con, buckets, role_key or None)
    finally:
        con.close()


def fetch_pack_path_priors(con: sqlite3.Connection, pack_id: str) -> Dict[str, float]:
    rows = con.execute(
        """
        SELECT path, score
        FROM learned_pack_path_priors
        WHERE pack_id = ?
        """,
        (pack_id,),
    ).fetchall()
    return {path: float(score) for path, score in rows}


@lru_cache(maxsize=128)
def cached_pack_path_priors(db_path_str: str, mtime_ns: int, size: int, pack_id: str) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_pack_path_priors(con, pack_id)
    finally:
        con.close()


def fetch_pack_skill_priors(con: sqlite3.Connection, pack_id: str) -> Dict[str, float]:
    rows = con.execute(
        """
        SELECT skill, score
        FROM learned_pack_skill_priors
        WHERE pack_id = ?
        """,
        (pack_id,),
    ).fetchall()
    return {skill: float(score) for skill, score in rows}


@lru_cache(maxsize=128)
def cached_pack_skill_priors(db_path_str: str, mtime_ns: int, size: int, pack_id: str) -> Dict[str, float]:
    con = sqlite3.connect(db_path_str)
    try:
        return fetch_pack_skill_priors(con, pack_id)
    finally:
        con.close()


@lru_cache(maxsize=4096)
def cached_path_chunk_ids(
    db_path_str: str, mtime_ns: int, size: int, path: str, limit: int = 4
) -> Tuple[str, ...]:
    con = sqlite3.connect(db_path_str)
    try:
        rows = con.execute(
            """
            SELECT chunk_id
            FROM chunks
            WHERE path = ?
            ORDER BY is_canonical DESC, freshness DESC
            LIMIT ?
            """,
            (path, limit),
        ).fetchall()
        return tuple(row[0] for row in rows)
    finally:
        con.close()


def train_pack_priors_in_connection(con: sqlite3.Connection) -> dict:
    pack_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(pack_stat_row)
    pack_path_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(pack_stat_row)
    pack_skill_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(pack_stat_row)

    rows = con.execute(
        """
        SELECT query, role, pack_id, used_skills_json, memory_paths_json, status, revision_count, user_rating
        FROM task_outcomes
        ORDER BY id
        """
    ).fetchall()

    con.execute("DELETE FROM learned_pack_priors")
    con.execute("DELETE FROM learned_pack_path_priors")
    con.execute("DELETE FROM learned_pack_skill_priors")

    for query, role, pack_id, used_skills_json, memory_paths_json, status, revision_count, user_rating in rows:
        try:
            used_skills = json.loads(used_skills_json or "[]")
            if not isinstance(used_skills, list):
                used_skills = []
        except json.JSONDecodeError:
            used_skills = []
        try:
            memory_paths = json.loads(memory_paths_json or "[]")
            if not isinstance(memory_paths, list):
                memory_paths = []
        except json.JSONDecodeError:
            memory_paths = []

        rating = float(user_rating) if user_rating is not None else None
        revision_count = int(revision_count or 0)

        for bucket in pack_buckets_for_query(query, role=role):
            update_pack_stats(pack_stats[(bucket, pack_id)], status, revision_count, rating)

        for path in list(dict.fromkeys(str(item) for item in memory_paths if str(item).strip())):
            update_pack_stats(pack_path_stats[(pack_id, path)], status, revision_count, rating)

        for skill in list(dict.fromkeys(str(item) for item in used_skills if str(item).strip())):
            update_pack_stats(pack_skill_stats[(pack_id, skill)], status, revision_count, rating)

    pack_rows = 0
    for (bucket, pack_id), stats in sorted(pack_stats.items()):
        avg_rating = stats["rating_sum"] / stats["rating_count"] if stats["rating_count"] else None
        avg_revisions = stats["revision_sum"] / max(stats["exposure_count"], 1)
        score = pack_outcome_score(
            int(stats["accepted_count"]),
            int(stats["revised_count"]),
            int(stats["failed_count"]),
            int(stats["exposure_count"]),
            avg_rating,
            avg_revisions,
        )
        con.execute(
            """
            INSERT INTO learned_pack_priors(bucket, pack_id, score, accepted_count, revised_count, failed_count, exposure_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                pack_id,
                score,
                int(stats["accepted_count"]),
                int(stats["revised_count"]),
                int(stats["failed_count"]),
                int(stats["exposure_count"]),
            ),
        )
        pack_rows += 1

    pack_path_rows = 0
    for (pack_id, path), stats in sorted(pack_path_stats.items()):
        avg_rating = stats["rating_sum"] / stats["rating_count"] if stats["rating_count"] else None
        avg_revisions = stats["revision_sum"] / max(stats["exposure_count"], 1)
        score = pack_outcome_score(
            int(stats["accepted_count"]),
            int(stats["revised_count"]),
            int(stats["failed_count"]),
            int(stats["exposure_count"]),
            avg_rating,
            avg_revisions,
        )
        con.execute(
            """
            INSERT INTO learned_pack_path_priors(pack_id, path, score, accepted_count, revised_count, failed_count, exposure_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                pack_id,
                path,
                score,
                int(stats["accepted_count"]),
                int(stats["revised_count"]),
                int(stats["failed_count"]),
                int(stats["exposure_count"]),
            ),
        )
        pack_path_rows += 1

    pack_skill_rows = 0
    for (pack_id, skill), stats in sorted(pack_skill_stats.items()):
        avg_rating = stats["rating_sum"] / stats["rating_count"] if stats["rating_count"] else None
        avg_revisions = stats["revision_sum"] / max(stats["exposure_count"], 1)
        score = pack_outcome_score(
            int(stats["accepted_count"]),
            int(stats["revised_count"]),
            int(stats["failed_count"]),
            int(stats["exposure_count"]),
            avg_rating,
            avg_revisions,
        )
        con.execute(
            """
            INSERT INTO learned_pack_skill_priors(pack_id, skill, score, accepted_count, revised_count, failed_count, exposure_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                pack_id,
                skill,
                score,
                int(stats["accepted_count"]),
                int(stats["revised_count"]),
                int(stats["failed_count"]),
                int(stats["exposure_count"]),
            ),
        )
        pack_skill_rows += 1

    con.execute(
        """
        INSERT INTO pack_training_runs(task_outcomes, pack_priors, pack_path_priors, pack_skill_priors)
        VALUES (?, ?, ?, ?)
        """,
        (len(rows), pack_rows, pack_path_rows, pack_skill_rows),
    )

    return {
        "task_outcomes": len(rows),
        "pack_priors": pack_rows,
        "pack_path_priors": pack_path_rows,
        "pack_skill_priors": pack_skill_rows,
    }


def train_outcome_priors_in_connection(con: sqlite3.Connection) -> dict:
    outcome_path_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(pack_stat_row)
    outcome_skill_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(pack_stat_row)

    rows = con.execute(
        """
        SELECT query, role, used_skills_json, memory_paths_json, status, revision_count, user_rating
        FROM task_outcomes
        ORDER BY id
        """
    ).fetchall()

    con.execute("DELETE FROM learned_outcome_path_priors")
    con.execute("DELETE FROM learned_outcome_skill_priors")

    for query, role, used_skills_json, memory_paths_json, status, revision_count, user_rating in rows:
        try:
            used_skills = json.loads(used_skills_json or "[]")
            if not isinstance(used_skills, list):
                used_skills = []
        except json.JSONDecodeError:
            used_skills = []
        try:
            memory_paths = json.loads(memory_paths_json or "[]")
            if not isinstance(memory_paths, list):
                memory_paths = []
        except json.JSONDecodeError:
            memory_paths = []

        rating = float(user_rating) if user_rating is not None else None
        revision_count = int(revision_count or 0)
        buckets = pack_buckets_for_query(query, role=role)

        for bucket in buckets:
            for path in list(dict.fromkeys(str(item) for item in memory_paths if str(item).strip())):
                update_pack_stats(outcome_path_stats[(bucket, path)], status, revision_count, rating)
            for skill in list(dict.fromkeys(str(item) for item in used_skills if str(item).strip())):
                update_pack_stats(outcome_skill_stats[(bucket, skill)], status, revision_count, rating)

    outcome_path_rows = 0
    for (bucket, path), stats in sorted(outcome_path_stats.items()):
        avg_rating = stats["rating_sum"] / stats["rating_count"] if stats["rating_count"] else None
        avg_revisions = stats["revision_sum"] / max(stats["exposure_count"], 1)
        score = pack_outcome_score(
            int(stats["accepted_count"]),
            int(stats["revised_count"]),
            int(stats["failed_count"]),
            int(stats["exposure_count"]),
            avg_rating,
            avg_revisions,
        )
        con.execute(
            """
            INSERT INTO learned_outcome_path_priors(bucket, path, score, accepted_count, revised_count, failed_count, exposure_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                path,
                score,
                int(stats["accepted_count"]),
                int(stats["revised_count"]),
                int(stats["failed_count"]),
                int(stats["exposure_count"]),
            ),
        )
        outcome_path_rows += 1

    outcome_skill_rows = 0
    for (bucket, skill), stats in sorted(outcome_skill_stats.items()):
        avg_rating = stats["rating_sum"] / stats["rating_count"] if stats["rating_count"] else None
        avg_revisions = stats["revision_sum"] / max(stats["exposure_count"], 1)
        score = pack_outcome_score(
            int(stats["accepted_count"]),
            int(stats["revised_count"]),
            int(stats["failed_count"]),
            int(stats["exposure_count"]),
            avg_rating,
            avg_revisions,
        )
        con.execute(
            """
            INSERT INTO learned_outcome_skill_priors(bucket, skill, score, accepted_count, revised_count, failed_count, exposure_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                skill,
                score,
                int(stats["accepted_count"]),
                int(stats["revised_count"]),
                int(stats["failed_count"]),
                int(stats["exposure_count"]),
            ),
        )
        outcome_skill_rows += 1

    con.execute(
        """
        INSERT INTO outcome_training_runs(task_outcomes, outcome_path_priors, outcome_skill_priors)
        VALUES (?, ?, ?)
        """,
        (len(rows), outcome_path_rows, outcome_skill_rows),
    )

    return {
        "task_outcomes": len(rows),
        "outcome_path_priors": outcome_path_rows,
        "outcome_skill_priors": outcome_skill_rows,
    }


def train_result_priors_in_connection(con: sqlite3.Connection) -> dict:
    result_pack_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(result_learning_stat_row)
    result_path_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(result_learning_stat_row)
    result_skill_stats: Dict[Tuple[str, str], Dict[str, float]] = defaultdict(result_learning_stat_row)

    outcomes = {row["id"]: row for row in fetch_task_outcomes_in_connection(con)}
    scorecards = fetch_task_result_scorecards_in_connection(con)

    con.execute("DELETE FROM learned_result_pack_priors")
    con.execute("DELETE FROM learned_result_path_priors")
    con.execute("DELETE FROM learned_result_skill_priors")

    manual_scorecards = 0
    suggested_scorecards = 0
    for outcome_id, scorecard in scorecards.items():
        outcome = outcomes.get(outcome_id)
        if outcome is None:
            continue
        scoring_mode = str(scorecard.get("scoring_mode", "suggested"))
        if scoring_mode == "manual":
            manual_scorecards += 1
        else:
            suggested_scorecards += 1

        overall_score = float(scorecard["overall_score"])
        verdict = str(scorecard["verdict"])
        status = str(outcome["status"])
        revision_count = int(outcome["revision_count"] or 0)
        buckets = pack_buckets_for_query(outcome["query"], role=outcome["role"])

        for bucket in buckets:
            update_result_learning_stats(
                result_pack_stats[(bucket, outcome["pack_id"])],
                overall_score,
                verdict,
                scoring_mode,
                status,
                revision_count,
            )

        for path in list(dict.fromkeys(path for path in outcome["memory_paths"] if path)):
            for bucket in buckets:
                update_result_learning_stats(
                    result_path_stats[(bucket, path)],
                    overall_score,
                    verdict,
                    scoring_mode,
                    status,
                    revision_count,
                )

        for skill in list(dict.fromkeys(skill for skill in outcome["used_skills"] if skill)):
            for bucket in buckets:
                update_result_learning_stats(
                    result_skill_stats[(bucket, skill)],
                    overall_score,
                    verdict,
                    scoring_mode,
                    status,
                    revision_count,
                )

    result_pack_rows = 0
    for (bucket, pack_id), stats in sorted(result_pack_stats.items()):
        score, avg_overall = result_learning_score(stats)
        con.execute(
            """
            INSERT INTO learned_result_pack_priors(
              bucket, pack_id, score, avg_overall_score, manual_count, suggested_count, exposure_count
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                pack_id,
                score,
                avg_overall,
                int(stats["manual_count"]),
                int(stats["suggested_count"]),
                int(stats["exposure_count"]),
            ),
        )
        result_pack_rows += 1

    result_path_rows = 0
    for (bucket, path), stats in sorted(result_path_stats.items()):
        score, avg_overall = result_learning_score(stats)
        con.execute(
            """
            INSERT INTO learned_result_path_priors(
              bucket, path, score, avg_overall_score, manual_count, suggested_count, exposure_count
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                path,
                score,
                avg_overall,
                int(stats["manual_count"]),
                int(stats["suggested_count"]),
                int(stats["exposure_count"]),
            ),
        )
        result_path_rows += 1

    result_skill_rows = 0
    for (bucket, skill), stats in sorted(result_skill_stats.items()):
        score, avg_overall = result_learning_score(stats)
        con.execute(
            """
            INSERT INTO learned_result_skill_priors(
              bucket, skill, score, avg_overall_score, manual_count, suggested_count, exposure_count
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                skill,
                score,
                avg_overall,
                int(stats["manual_count"]),
                int(stats["suggested_count"]),
                int(stats["exposure_count"]),
            ),
        )
        result_skill_rows += 1

    con.execute(
        """
        INSERT INTO result_training_runs(
          scored_outcomes, manual_scorecards, suggested_scorecards, result_pack_priors, result_path_priors, result_skill_priors
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            len(scorecards),
            manual_scorecards,
            suggested_scorecards,
            result_pack_rows,
            result_path_rows,
            result_skill_rows,
        ),
    )

    return {
        "scored_outcomes": len(scorecards),
        "manual_scorecards": manual_scorecards,
        "suggested_scorecards": suggested_scorecards,
        "result_pack_priors": result_pack_rows,
        "result_path_priors": result_path_rows,
        "result_skill_priors": result_skill_rows,
    }


def train_usage_priors_in_connection(con: sqlite3.Connection) -> dict:
    path_stats: Dict[Tuple[str, str], Dict[str, int]] = defaultdict(usage_stat_row)
    skill_stats: Dict[Tuple[str, str], Dict[str, int]] = defaultdict(usage_stat_row)

    log_rows = con.execute("SELECT mode, query, role, result_json FROM query_log ORDER BY id").fetchall()
    feedback_rows = con.execute("SELECT query, path, rating FROM feedback ORDER BY id").fetchall()

    con.execute("DELETE FROM learned_path_priors")
    con.execute("DELETE FROM learned_skill_priors")

    for mode, query, role, result_json in log_rows:
        try:
            payload = json.loads(result_json)
        except json.JSONDecodeError:
            continue
        inferred_intents = payload.get("inferred_intents") if isinstance(payload, dict) else None
        buckets = buckets_for_query(query, role=role, inferred_intents=inferred_intents)
        paths, skills = extract_logged_paths_and_skills(mode, payload if isinstance(payload, dict) else {})
        for bucket in buckets:
            for path in paths:
                path_stats[(bucket, path)]["exposure_count"] += 1
            for skill in skills:
                skill_stats[(bucket, skill)]["exposure_count"] += 1

    for query, path, rating in feedback_rows:
        buckets = buckets_for_query(query)
        skill = skill_root_for_path(path)
        target_field = "useful_count" if rating == "useful" else "not_useful_count"
        for bucket in buckets:
            path_stats[(bucket, path)][target_field] += 1
            skill_stats[(bucket, skill)][target_field] += 1

    path_rows = 0
    for (bucket, path), stats in sorted(path_stats.items()):
        score = usage_score(stats["useful_count"], stats["not_useful_count"], stats["exposure_count"])
        con.execute(
            """
            INSERT INTO learned_path_priors(bucket, path, score, useful_count, not_useful_count, exposure_count)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                path,
                score,
                stats["useful_count"],
                stats["not_useful_count"],
                stats["exposure_count"],
            ),
        )
        path_rows += 1

    skill_rows = 0
    for (bucket, skill), stats in sorted(skill_stats.items()):
        score = usage_score(stats["useful_count"], stats["not_useful_count"], stats["exposure_count"])
        con.execute(
            """
            INSERT INTO learned_skill_priors(bucket, skill, score, useful_count, not_useful_count, exposure_count)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                bucket,
                skill,
                score,
                stats["useful_count"],
                stats["not_useful_count"],
                stats["exposure_count"],
            ),
        )
        skill_rows += 1

    con.execute(
        """
        INSERT INTO training_runs(query_logs, feedback_rows, path_priors, skill_priors)
        VALUES (?, ?, ?, ?)
        """,
        (len(log_rows), len(feedback_rows), path_rows, skill_rows),
    )

    return {
        "query_logs": len(log_rows),
        "feedback_rows": len(feedback_rows),
        "path_priors": path_rows,
        "skill_priors": skill_rows,
    }


def train_usage_priors(db_path: Path) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        summary = train_usage_priors_in_connection(con)
        pack_summary = train_pack_priors_in_connection(con)
        outcome_summary = train_outcome_priors_in_connection(con)
        result_summary = train_result_priors_in_connection(con)
        con.commit()
        return {**summary, **pack_summary, **outcome_summary, **result_summary}
    finally:
        con.close()


def train_outcome_priors(db_path: Path) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        summary = train_outcome_priors_in_connection(con)
        con.commit()
        return {"db": str(db_path), **summary}
    finally:
        con.close()


def train_result_priors(db_path: Path) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        summary = train_result_priors_in_connection(con)
        con.commit()
        return {"db": str(db_path), **summary}
    finally:
        con.close()


def feedback_aware_top(results: List[dict], top: int) -> List[dict]:
    pool = sorted(results, key=lambda item: item["score"], reverse=True)
    selected: List[dict] = []
    path_counts: Counter = Counter()
    canonical_counts: Counter = Counter()
    source_counts: Counter = Counter()

    while pool and len(selected) < top:
        best_index = 0
        best_score = None
        for index, item in enumerate(pool):
            adjusted = item["score"]
            adjusted -= path_counts[item["path"]] * 0.85
            if item["canonical_group"]:
                adjusted -= canonical_counts[item["canonical_group"]] * 0.25
            if item["source"]:
                adjusted -= source_counts[item["source"]] * 0.08
            if item["file_type"] == "memory_index":
                adjusted -= 0.45
            elif item["file_type"] in {"memory_router", "squad_router", "skill_contract"}:
                adjusted -= 0.25
            if best_score is None or adjusted > best_score:
                best_score = adjusted
                best_index = index
        chosen = pool.pop(best_index)
        selected.append(chosen)
        path_counts[chosen["path"]] += 1
        if chosen["canonical_group"]:
            canonical_counts[chosen["canonical_group"]] += 1
        if chosen["source"]:
            source_counts[chosen["source"]] += 1
    return selected


def fts_candidates(con: sqlite3.Connection, query: str, top_k: int = 40) -> List[Tuple[str, float]]:
    tokens = tokenize(query)
    if not tokens:
        return []
    fts_query = " OR ".join(f'"{token.replace(chr(34), "")}"' for token in tokens[:16])
    rows = con.execute(
        """
        SELECT chunk_id, bm25(chunks_fts) AS rank
        FROM chunks_fts
        WHERE chunks_fts MATCH ?
        ORDER BY rank
        LIMIT ?
        """,
        (fts_query, top_k),
    ).fetchall()
    return [(chunk_id, -rank) for chunk_id, rank in rows]


def query_semantic_vector(con: sqlite3.Connection, query: str) -> Tuple[Dict[str, float], float]:
    counts = Counter(tokenize(query))
    return semantic_vector_from_counts(counts, load_token_vectors(con), total_terms=sum(counts.values()) or 1)


def load_token_vectors(con: sqlite3.Connection) -> Dict[str, Tuple[Dict[str, float], float]]:
    rows = con.execute("SELECT token, weights_json, norm FROM token_vectors").fetchall()
    return {
        token: (json.loads(weights_json), norm)
        for token, weights_json, norm in rows
    }


@lru_cache(maxsize=4)
def cached_load_token_vectors(db_path_str: str, mtime_ns: int, size: int) -> Dict[str, Tuple[Dict[str, float], float]]:
    con = sqlite3.connect(db_path_str)
    try:
        return load_token_vectors(con)
    finally:
        con.close()


def semantic_candidates(con: sqlite3.Connection, query_weights: Dict[str, float], query_norm: float, top_k: int = 40) -> List[Tuple[str, float]]:
    if not query_weights:
        return []
    scored: List[Tuple[str, float]] = []
    rows = con.execute("SELECT chunk_id, weights_json, norm FROM chunk_vectors").fetchall()
    for chunk_id, weights_json, norm in rows:
        weights = json.loads(weights_json)
        score = sparse_cosine(query_weights, query_norm, weights, norm)
        if score > 0:
            scored.append((chunk_id, score))
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:top_k]


def active_workspace_context(
    con: sqlite3.Connection,
    query: str,
    role: Optional[str],
    top: int = 6,
    pack_id: Optional[str] = None,
) -> Dict[str, Any]:
    ensure_learning_tables(con)
    params: List[Any] = []
    where = ["wc.status = 'active'"]
    if role:
        where.append("(wc.role IS NULL OR wc.role = '' OR LOWER(wc.role) = ?)")
        params.append(role.lower())
    if pack_id:
        where.append("(wc.pack_id IS NULL OR wc.pack_id = '' OR wc.pack_id = ?)")
        params.append(pack_id)
    rows = con.execute(
        f"""
        SELECT
          wc.id,
          wc.name,
          wc.root_path,
          wc.role,
          wc.pack_id,
          wc.ts_updated,
          wc.ts_last_used,
          wc.metadata_json,
          wci.id,
          wci.path,
          wci.rel_path,
          wci.item_type,
          wci.title,
          wci.text,
          wci.token_count,
          wci.metadata_json
        FROM workspace_contexts wc
        JOIN workspace_context_items wci ON wci.context_id = wc.id
        WHERE {' AND '.join(where)}
        ORDER BY wc.ts_updated DESC, wc.id DESC, wci.id ASC
        """,
        tuple(params),
    ).fetchall()
    if not rows:
        return {
            "active_contexts": 0,
            "active_items": 0,
            "hits": [],
            "tokens": set(),
            "roles": set(),
            "context_ids": [],
            "contexts": [],
        }

    query_tokens = set(tokenize(query))
    hit_rows: List[Dict[str, Any]] = []
    context_rows: Dict[int, Dict[str, Any]] = {}
    token_counter: Counter[str] = Counter()

    for row in rows:
        (
            context_id,
            name,
            root_path,
            context_role,
            context_pack_id,
            ts_updated,
            ts_last_used,
            context_meta_json,
            item_id,
            path,
            rel_path,
            item_type,
            title,
            text,
            token_count,
            item_meta_json,
        ) = row
        context_rows.setdefault(
            int(context_id),
            {
                "id": int(context_id),
                "name": str(name or ""),
                "root_path": str(root_path or ""),
                "role": str(context_role or ""),
                "pack_id": str(context_pack_id or ""),
                "ts_updated": str(ts_updated or ""),
                "ts_last_used": str(ts_last_used or ""),
                "metadata": safe_json_object(str(context_meta_json or "{}")),
            },
        )
        title_tokens = set(tokenize(str(title or "")))
        path_tokens = set(tokenize(str(rel_path or path or "")))
        body_tokens = set(tokenize(str(text or "")[:WORKSPACE_BODY_CHARS]))
        title_overlap = len(title_tokens & query_tokens)
        path_overlap = len(path_tokens & query_tokens)
        body_overlap = len(body_tokens & query_tokens)
        exact_hit = 1.0 if compact_whitespace(query).lower() in compact_whitespace(str(text or "")).lower() else 0.0
        score = title_overlap * 0.34 + path_overlap * 0.24 + min(body_overlap * 0.08, 0.88) + exact_hit * 0.4
        if context_role and role and context_role.lower() == role.lower():
            score += 0.16
        if context_pack_id and pack_id and context_pack_id == pack_id:
            score += 0.18
        hit_rows.append(
            {
                "id": int(item_id),
                "context_id": int(context_id),
                "context_name": str(name or ""),
                "role": str(context_role or ""),
                "pack_id": str(context_pack_id or ""),
                "path": str(path or ""),
                "rel_path": str(rel_path or ""),
                "item_type": str(item_type or "file"),
                "title": str(title or ""),
                "text": str(text or ""),
                "token_count": int(token_count or 0),
                "metadata": safe_json_object(str(item_meta_json or "{}")),
                "score": round(score, 4),
                "title_overlap": title_overlap,
                "path_overlap": path_overlap,
                "body_overlap": body_overlap,
            }
        )

    hit_rows.sort(key=lambda item: item["score"], reverse=True)
    selected_hits = [item for item in hit_rows if item["score"] > 0][: max(top, 4)]
    if selected_hits:
        for item in selected_hits[: max(top, 6)]:
            token_counter.update(tokenize(item["title"]))
            token_counter.update(tokenize(item["rel_path"] or item["path"]))
            token_counter.update(tokenize(item["text"][:WORKSPACE_BODY_CHARS]))
        for context in context_rows.values():
            token_counter.update(tokenize(context["name"]))
            if context["role"]:
                token_counter.update(tokenize(context["role"]))
            if context["pack_id"]:
                token_counter.update(tokenize(context["pack_id"]))

    return {
        "active_contexts": len(context_rows),
        "active_items": len(rows),
        "hits": [
            {
                "id": item["id"],
                "context_id": item["context_id"],
                "context_name": item["context_name"],
                "role": item["role"],
                "pack_id": item["pack_id"],
                "path": item["path"],
                "rel_path": item["rel_path"],
                "item_type": item["item_type"],
                "title": item["title"],
                "score": item["score"],
                "snippet": truncate_text(item["text"], 200),
            }
            for item in selected_hits[:top]
        ],
        "tokens": {token for token, _count in token_counter.most_common(180)},
        "roles": (
            {context["role"].lower() for context in context_rows.values() if context["role"]}
            if selected_hits
            else set()
        ),
        "context_ids": sorted(context_rows),
        "contexts": list(context_rows.values()),
    }


def touch_workspace_contexts_in_connection(con: sqlite3.Connection, context_ids: Sequence[int]) -> None:
    ids = [int(context_id) for context_id in context_ids if context_id]
    if not ids:
        return
    placeholders = ", ".join("?" for _ in ids)
    con.execute(
        f"""
        UPDATE workspace_contexts
        SET ts_last_used = CURRENT_TIMESTAMP,
            ts_updated = CASE WHEN status = 'active' THEN ts_updated ELSE CURRENT_TIMESTAMP END
        WHERE id IN ({placeholders})
        """,
        tuple(ids),
    )


def fetch_candidate_chunk_rows(con: sqlite3.Connection, chunk_ids: Sequence[str]) -> Dict[str, tuple]:
    ids = [chunk_id for chunk_id in chunk_ids if chunk_id]
    if not ids:
        return {}
    placeholders = ", ".join("?" for _ in ids)
    rows = con.execute(
        f"""
        SELECT c.chunk_id, c.path, c.skill, c.file_type, c.heading, c.text, c.section_kind, c.source, c.published_on, c.freshness,
               c.topics_json, c.intents_json, c.use_for_json, c.avoid_for_json, c.confidence,
               c.tags_json, c.roles_json, c.bundles_json, c.is_canonical, c.canonical_group,
               w.weights_json, w.norm, v.weights_json, v.norm
        FROM chunks c
        JOIN chunk_weights w ON w.chunk_id = c.chunk_id
        JOIN chunk_vectors v ON v.chunk_id = c.chunk_id
        WHERE c.chunk_id IN ({placeholders})
        """,
        tuple(ids),
    ).fetchall()
    return {row[0]: row[1:] for row in rows}


@lru_cache(maxsize=256)
def cached_support_item_by_path(db_path_str: str, mtime_ns: int, size: int, path: str) -> Optional[dict]:
    con = sqlite3.connect(db_path_str)
    try:
        row = con.execute(
            """
            SELECT chunk_id, path, skill, file_type, heading, text, section_kind, source, published_on, freshness,
                   topics_json, intents_json, use_for_json, roles_json, confidence, is_canonical, canonical_group
            FROM chunks
            WHERE path = ?
            ORDER BY is_canonical DESC, freshness DESC
            LIMIT 1
            """,
            (path,),
        ).fetchone()
    finally:
        con.close()
    if not row:
        return None
    (
        chunk_id,
        item_path,
        skill,
        file_type,
        heading,
        text,
        section_kind,
        source,
        published_on,
        freshness,
        topics_json,
        intents_json,
        use_for_json,
        roles_json,
        confidence,
        is_canonical,
        canonical_group,
    ) = row
    return {
        "chunk_id": chunk_id,
        "path": item_path,
        "skill": skill,
        "file_type": file_type,
        "heading": heading,
        "section_kind": section_kind,
        "source": source,
        "published_on": published_on,
        "score": 0.0,
        "lexical": 0.0,
        "semantic": 0.0,
        "vector_semantic": 0.0,
        "vector_seed": 0.0,
        "result_seed": 0.0,
        "role_boost": 0.0,
        "canonical_boost": 0.12 if is_canonical else 0.0,
        "bundle_boost": 0.0,
        "alias_boost": 0.0,
        "feedback_boost": 0.0,
        "skill_feedback_boost": 0.0,
        "freshness_boost": float(freshness or 0.0),
        "intent_boost": 0.0,
        "registry_boost": 0.0,
        "registry_status": "",
        "evidence_boost": 0.0,
        "evidence_confidence": 0.0,
        "evidence_freshness": 0.0,
        "phase11_boost": 0.0,
        "phase12_boost": 0.0,
        "phase16_boost": 0.0,
        "phase17_boost": 0.0,
        "phase23_boost": 0.0,
        "phase24_boost": 0.0,
        "phase25_boost": 0.0,
        "workspace_boost": 0.0,
        "workspace_overlap": 0,
        "metadata_boost": 0.0,
        "confidence_boost": CONFIDENCE_BOOSTS.get(confidence or "", 0.0),
        "path_prior_boost": 0.0,
        "outcome_path_boost": 0.0,
        "result_path_boost": 0.0,
        "avoid_penalty": 0.0,
        "heading_penalty": 0.0,
        "synthesis_penalty": 0.0,
        "confidence": confidence,
        "topics": parse_json_list(topics_json),
        "intents": parse_json_list(intents_json),
        "use_for": parse_json_list(use_for_json),
        "roles": parse_json_list(roles_json),
        "bundles": [],
        "canonical_group": canonical_group,
        "snippet": (text or "")[:280].replace("\n", " "),
    }


def rank_chunks(
    db_path: Path,
    query: str,
    role: Optional[str],
    skill_filter: Optional[str],
    top: int,
    pack_id: Optional[str] = None,
    workspace_enabled: bool = True,
) -> List[dict]:
    con = sqlite3.connect(str(db_path))
    ensure_learning_tables(con)
    expanded_query, inferred_intents, expansion_terms = expand_query(query, role)
    db_key = db_revision_token(db_path)
    learned_buckets = learned_bucket_key(inferred_intents)
    role_buckets = role_bucket_key(inferred_intents, role)
    role_key = role.lower() if role else ""
    total_docs, doc_freq = cached_load_meta(*db_key)
    q_weights, q_norm = query_weights(expanded_query, total_docs, doc_freq)
    q_vector_weights, q_vector_norm = semantic_vector_from_counts(
        Counter(tokenize(expanded_query)),
        cached_load_token_vectors(*db_key),
    )
    role_paths = set(cached_role_paths(*db_key, role_key)) if role_key else set()
    feedback_scores = cached_path_feedback(*db_key)
    skill_feedback = cached_skill_feedback(*db_key)
    learned_path_priors = cached_learned_path_priors(*db_key, learned_buckets)
    outcome_path_priors = cached_outcome_path_priors(*db_key, role_buckets, role_key)
    result_path_priors = cached_result_path_priors(*db_key, role_buckets, role_key)
    query_token_set = set(tokenize(expanded_query))
    query_context_tokens = set(query_token_set)
    query_context_tokens.update(tokenize(" ".join(inferred_intents)))
    query_context_tokens.update(tokenize(" ".join(expansion_terms)))
    specific_evidence_query = is_specific_evidence_query(query, query_token_set)
    broad_synthesis_query = is_broad_synthesis_query(query_token_set, inferred_intents, specific_evidence_query)
    workspace_context = (
        active_workspace_context(con, expanded_query, role, top=max(4, top), pack_id=pack_id)
        if workspace_enabled
        else {"active_contexts": 0, "active_items": 0, "hits": [], "tokens": set(), "roles": set(), "context_ids": [], "contexts": []}
    )
    workspace_tokens = set(workspace_context["tokens"])
    workspace_roles = set(workspace_context["roles"])
    phase7_registry = cached_phase7_registry(*file_revision_token(PHASE7_REGISTRY_PATH))
    phase10_ledger = cached_phase10_ledger(*file_revision_token(PHASE10_LEDGER_PATH))
    phase11_ledgers = cached_phase11_ledgers(*file_revision_token(PHASE11_LEDGER_DIR))
    phase12_ledgers = cached_phase12_ledgers(*file_revision_token(PHASE12_LEDGER_DIR))
    phase16_ledgers = cached_phase16_ledgers(*file_revision_token(PHASE16_LEDGER_DIR))
    phase17_ledgers = cached_phase17_ledgers(*file_revision_token(PHASE17_LEDGER_DIR))
    phase23_ledgers = cached_phase23_ledgers(*file_revision_token(PHASE23_LEDGER_DIR))
    phase24_ledgers = cached_phase24_ledgers(*file_revision_token(PHASE24_LEDGER_DIR))
    phase25_ledgers = cached_phase25_ledgers(*file_revision_token(PHASE25_LEDGER_DIR))
    lexical_candidates = fts_candidates(con, expanded_query, top_k=max(top * 12, 60))
    candidate_scores: Dict[str, Dict[str, float]] = defaultdict(
        lambda: {"lexical": 0.0, "vector_seed": 0.0, "learned_seed": 0.0, "outcome_seed": 0.0, "result_seed": 0.0}
    )
    for chunk_id, lexical_score in lexical_candidates:
        candidate_scores[chunk_id]["lexical"] = max(candidate_scores[chunk_id]["lexical"], lexical_score)
    need_vector_expansion = len(candidate_scores) < max(top * 2, 48)
    if need_vector_expansion:
        vector_candidates = semantic_candidates(con, q_vector_weights, q_vector_norm, top_k=max(top * 10, 50))
        for chunk_id, vector_score in vector_candidates:
            candidate_scores[chunk_id]["vector_seed"] = max(candidate_scores[chunk_id]["vector_seed"], vector_score)
    for path, score in sorted(learned_path_priors.items(), key=lambda item: item[1], reverse=True)[: max(top * 6, 24)]:
        if score <= 0:
            continue
        for chunk_id in cached_path_chunk_ids(*db_key, path, 4):
            candidate_scores[chunk_id]["learned_seed"] = max(candidate_scores[chunk_id]["learned_seed"], score)
    for path, score in sorted(outcome_path_priors.items(), key=lambda item: item[1], reverse=True)[: max(top * 6, 24)]:
        if score <= 0:
            continue
        for chunk_id in cached_path_chunk_ids(*db_key, path, 4):
            candidate_scores[chunk_id]["outcome_seed"] = max(candidate_scores[chunk_id]["outcome_seed"], score)
    for path, score in sorted(result_path_priors.items(), key=lambda item: item[1], reverse=True)[: max(top * 6, 24)]:
        if score <= 0:
            continue
        for chunk_id in cached_path_chunk_ids(*db_key, path, 4):
            candidate_scores[chunk_id]["result_seed"] = max(candidate_scores[chunk_id]["result_seed"], score)
    candidates = list(candidate_scores.items())

    # Fallback if FTS returns too little.
    if not candidates:
        rows = con.execute("SELECT chunk_id FROM chunks LIMIT 100").fetchall()
        candidates = [
            (row[0], {"lexical": 0.0, "vector_seed": 0.0, "learned_seed": 0.0, "outcome_seed": 0.0, "result_seed": 0.0})
            for row in rows
        ]

    candidate_rows = fetch_candidate_chunk_rows(con, [chunk_id for chunk_id, _seed_scores in candidates])
    ranked = []
    for chunk_id, seed_scores in candidates:
        row = candidate_rows.get(chunk_id)
        if not row:
            continue
        (
            path,
            skill,
            file_type,
            heading,
            text,
            section_kind,
            source,
            published_on,
            freshness,
            topics_json,
            intents_json,
            use_for_json,
            avoid_for_json,
            confidence,
            tags_json,
            roles_json,
            bundles_json,
            is_canonical,
            canonical_group,
            weights_json,
            norm,
            vector_weights_json,
            vector_norm,
        ) = row
        if skill_filter and skill != skill_filter:
            continue
        lexical_score = seed_scores["lexical"]
        vector_seed = seed_scores["vector_seed"]
        learned_seed = seed_scores["learned_seed"]
        outcome_seed = seed_scores["outcome_seed"]
        result_seed = seed_scores["result_seed"]
        weights = json.loads(weights_json)
        direct_semantic = sparse_cosine(q_weights, q_norm, weights, norm)
        vector_semantic = sparse_cosine(q_vector_weights, q_vector_norm, json.loads(vector_weights_json), vector_norm) if q_vector_weights else 0.0
        topic_list = json.loads(topics_json)
        intent_list = json.loads(intents_json)
        use_for_list = json.loads(use_for_json)
        avoid_for_list = json.loads(avoid_for_json)
        tag_list = json.loads(tags_json)
        role_list = json.loads(roles_json)
        bundle_list = json.loads(bundles_json)
        chunk_context_terms = set(tokenize(heading))
        chunk_context_terms.update(tokenize(path))
        for value in topic_list + intent_list + use_for_list + tag_list + role_list + bundle_list:
            chunk_context_terms.update(tokenize(str(value)))
        tag_overlap = len(set(tag_list) & query_context_tokens)
        topic_overlap = len(set(topic_list) & query_context_tokens)
        intent_overlap = len(set(intent_list) & query_context_tokens)
        use_for_overlap = len(set(use_for_list) & query_context_tokens)
        avoid_overlap = len(set(avoid_for_list) & query_context_tokens)
        role_boost = 0.18 if path in role_paths else 0.0
        canonical_boost = canonical_topic_boost(
            path,
            heading,
            bool(is_canonical),
            topic_overlap,
            intent_overlap,
            use_for_overlap,
            broad_synthesis_query,
        )
        tag_boost = min(tag_overlap * 0.05, 0.15)
        metadata_boost = min(topic_overlap * 0.08 + intent_overlap * 0.09 + use_for_overlap * 0.07, 0.32)
        avoid_penalty = min(avoid_overlap * 0.12, 0.24)
        confidence_boost = CONFIDENCE_BOOSTS.get(confidence, 0.0)
        path_prior_boost = max(min(learned_path_priors.get(path, 0.0) * 0.5, 0.22), -0.18)
        outcome_path_boost = max(min(outcome_path_priors.get(path, 0.0) * 0.55, 0.24), -0.2)
        result_path_boost = max(min(result_path_priors.get(path, 0.0) * 0.62, 0.28), -0.22)
        bundle_boost = 0.05 if role and any(role.lower() in bundle for bundle in bundle_list) else 0.0
        alias_boost = 0.08 if set(role_list) & query_token_set else 0.0
        feedback_boost = max(min(feedback_scores.get(path, 0.0) * 0.03, 0.12), -0.12)
        skill_feedback_boost = max(min(skill_feedback.get(skill, 0.0) * 0.02, 0.08), -0.08)
        section_boost = 0.0
        if section_kind in {"quick_read", "core_concept", "key_takeaways", "framework", "models_systems"}:
            section_boost = 0.04
        heading_penalty = 0.0
        heading_key = heading.strip().lower()
        if heading_key == "squad routing":
            heading_penalty = 0.24
        elif heading_key == "primary evidence in this pack":
            heading_penalty = 0.12
        source_boost = 0.05 if source and source in query_token_set else 0.0
        intent_boost = 0.0
        if "ai_selection" in inferred_intents and source == "dejan":
            intent_boost += 0.08
        if "javascript_ai_systems" in inferred_intents and source == "dejan":
            intent_boost += 0.08
        if "javascript_ai_systems" in inferred_intents and source == "gsqi":
            intent_boost += 0.06
        if "javascript_ai_systems" in inferred_intents and source == "google":
            intent_boost += 0.04
        if "multilingual_ai_systems" in inferred_intents and source == "gsqi":
            intent_boost += 0.07
        if "multilingual_ai_systems" in inferred_intents and source == "google":
            intent_boost += 0.04
        if "multilingual_ai_systems" in inferred_intents and source == "aleyda":
            intent_boost += 0.05
        if "fan_out" in inferred_intents and source == "dejan":
            intent_boost += 0.06
        if "ai_visibility" in inferred_intents and source == "ahrefs":
            intent_boost += 0.05
        if "leak_systems" in inferred_intents and source == "hobo":
            intent_boost += 0.06
        if "coordination" in inferred_intents:
            if skill == "orchestrator-pinchy":
                intent_boost += 0.28
            elif skill == "operations":
                intent_boost += 0.12
            elif skill == "multi-agent-reef":
                intent_boost += 0.1
        registry_entry = phase7_registry.get(path, {})
        registry_boost = phase7_registry_adjustment(registry_entry, query_context_tokens)
        evidence_entry = phase10_ledger.get(path, {})
        evidence_boost = phase10_evidence_adjustment(evidence_entry, query_context_tokens)
        phase11_entry = phase11_ledgers.get(path, {})
        phase11_boost = phase11_domain_adjustment(phase11_entry, query_context_tokens)
        phase12_entry = phase12_ledgers.get(path, {})
        phase12_boost = phase12_domain_adjustment(phase12_entry, query_context_tokens)
        phase16_entry = phase16_ledgers.get(path, {})
        phase16_boost = phase16_domain_adjustment(phase16_entry, query_context_tokens)
        phase17_entry = phase17_ledgers.get(path, {})
        phase17_boost = phase17_domain_adjustment(phase17_entry, query_context_tokens)
        phase23_entry = phase23_ledgers.get(path, {})
        phase23_boost = phase23_domain_adjustment(phase23_entry, query_context_tokens)
        phase24_entry = phase24_ledgers.get(path, {})
        phase24_boost = phase24_domain_adjustment(phase24_entry, query_context_tokens)
        phase25_entry = phase25_ledgers.get(path, {})
        phase25_boost = phase25_domain_adjustment(phase25_entry, query_context_tokens)
        workspace_overlap = len(chunk_context_terms & workspace_tokens)
        workspace_boost = min(workspace_overlap * 0.045, 0.28) if workspace_tokens else 0.0
        if workspace_roles and set(role_list) & workspace_roles:
            workspace_boost += 0.04
        type_adjust = 0.0
        if file_type == "memory_note":
            type_adjust = 0.08
        elif file_type == "reference_note":
            type_adjust = 0.06
        elif file_type in {"memory_router", "memory_index", "skill_contract", "squad_router"}:
            type_adjust = -0.08
        synthesis_penalty = 0.0
        if broad_synthesis_query and not is_canonical:
            if heading.strip().lower() == "extracted article passages":
                synthesis_penalty = 0.14
            elif "/memory/articles/" in path and section_kind in {"examples", "section"}:
                synthesis_penalty = 0.05
        total = (
            lexical_score * 0.25
            + direct_semantic * 0.26
            + vector_semantic * 0.18
            + vector_seed * 0.12
            + max(min(learned_seed * 0.08, 0.12), 0.0)
            + max(min(outcome_seed * 0.1, 0.15), 0.0)
            + max(min(result_seed * 0.12, 0.18), 0.0)
            + role_boost
            + canonical_boost
            + tag_boost
            + metadata_boost
            + confidence_boost
            + path_prior_boost
            + outcome_path_boost
            + result_path_boost
            + bundle_boost
            + alias_boost
            + feedback_boost
            + skill_feedback_boost
            + section_boost
            + source_boost
            + intent_boost
            + registry_boost
            + evidence_boost
            + phase11_boost
            + phase12_boost
            + phase16_boost
            + phase17_boost
            + phase23_boost
            + phase24_boost
            + phase25_boost
            + workspace_boost
            + freshness
            + type_adjust
            - avoid_penalty
            - heading_penalty
            - synthesis_penalty
        )
        ranked.append(
            {
                "chunk_id": chunk_id,
                "path": path,
                "skill": skill,
                "file_type": file_type,
                "heading": heading,
                "section_kind": section_kind,
                "source": source,
                "published_on": published_on,
                "inferred_intents": inferred_intents,
                "expansion_terms": expansion_terms,
                "score": round(total, 4),
                "lexical": round(lexical_score, 4),
                "semantic": round(direct_semantic, 4),
                "vector_semantic": round(vector_semantic, 4),
                "vector_seed": round(vector_seed, 4),
                "result_seed": round(result_seed, 4),
                "role_boost": role_boost,
                "canonical_boost": canonical_boost,
                "bundle_boost": bundle_boost,
                "alias_boost": alias_boost,
                "feedback_boost": feedback_boost,
                "skill_feedback_boost": skill_feedback_boost,
                "freshness_boost": freshness,
                "intent_boost": intent_boost,
                "registry_boost": registry_boost,
                "registry_status": registry_entry.get("status", ""),
                "evidence_boost": evidence_boost,
                "evidence_confidence": round(float(evidence_entry.get("confidence_score", 0.0) or 0.0), 4),
                "evidence_freshness": round(float(evidence_entry.get("freshness_score", 0.0) or 0.0), 4),
                "phase11_boost": phase11_boost,
                "phase12_boost": phase12_boost,
                "phase16_boost": phase16_boost,
                "phase17_boost": phase17_boost,
                "phase23_boost": phase23_boost,
                "phase24_boost": phase24_boost,
                "phase25_boost": phase25_boost,
                "workspace_boost": workspace_boost,
                "workspace_overlap": workspace_overlap,
                "metadata_boost": metadata_boost,
                "confidence_boost": confidence_boost,
                "path_prior_boost": path_prior_boost,
                "outcome_path_boost": outcome_path_boost,
                "result_path_boost": result_path_boost,
                "avoid_penalty": avoid_penalty,
                "heading_penalty": heading_penalty,
                "synthesis_penalty": synthesis_penalty,
                "confidence": confidence,
                "topics": topic_list,
                "intents": intent_list,
                "use_for": use_for_list,
                "roles": role_list,
                "bundles": bundle_list,
                "canonical_group": canonical_group,
                "snippet": text[:280].replace("\n", " "),
            }
        )

    con.close()
    return feedback_aware_top(ranked, top)


def skill_intent_decision_bonus(skill: str, inferred_intents: Sequence[str], query_tokens: set[str]) -> float:
    bonus = 0.0
    documentation_authoring_tokens = {
        "documentation",
        "docs",
        "guide",
        "guides",
        "instruction",
        "instructions",
        "setup",
        "walkthrough",
        "troubleshooting",
        "checks",
        "steps",
        "product",
        "clear",
    }
    support_issue_tokens = {"ticket", "customer", "customers", "triage", "severity", "billing", "issue", "issues", "outage"}
    design_direction_tokens = {
        "visual",
        "direction",
        "asset",
        "assets",
        "design",
        "designer",
        "creative",
        "brand",
        "branding",
        "layout",
        "landing",
        "page",
        "hero",
        "ui",
    }
    social_execution_tokens = {
        "linkedin",
        "x",
        "repurpose",
        "repackage",
        "social",
        "post",
        "posts",
        "hook",
        "hooks",
        "creator",
        "thread",
        "threads",
    }
    doc_authoring_query = bool(query_tokens & documentation_authoring_tokens) and not bool(query_tokens & support_issue_tokens)
    design_direction_query = bool(query_tokens & design_direction_tokens) and not doc_authoring_query
    if doc_authoring_query:
        if skill == "writer":
            bonus += 1.8
        elif skill == "writer-plankton":
            bonus += 1.0
        elif skill in {"support-anemone", "support"}:
            bonus -= 1.2
    if design_direction_query:
        if skill == "emily":
            bonus += 2.15
        elif skill == "marketing":
            bonus += 0.35
        elif skill == "writer":
            bonus -= 0.55
    if "ai_selection" in inferred_intents:
        if skill == "dejan-ai-reverse-engineering":
            bonus += 4.55
            if query_tokens & AI_SELECTION_DIAGNOSTIC_HINTS:
                bonus += 1.85
        elif skill == "seo":
            bonus -= 0.35
    if "social_creator" in inferred_intents:
        if skill == "charles":
            bonus += 1.1
            if query_tokens & social_execution_tokens:
                bonus += 0.55
        elif skill in {"marketing", "marketing-current"} and query_tokens & social_execution_tokens:
            bonus -= 0.2
    if "coordination" in inferred_intents:
        if skill == "orchestrator-pinchy":
            if query_tokens & {"coordinate", "coordination", "handoff", "handoffs", "routing", "route", "orchestrator", "pinchy"}:
                bonus += 1.75
            else:
                bonus += 0.9
            if query_tokens & {"launch", "writer", "seo", "marketing"}:
                bonus += 0.45
        elif skill == "operations":
            if query_tokens & {"owner", "owners", "timeline", "timelines", "deadline", "deadlines", "blocker", "blockers"}:
                bonus += 1.0
            else:
                bonus += 0.3
        elif skill == "multi-agent-reef":
            if query_tokens & {"handoff", "handoffs", "agents", "specialists", "workflow"}:
                bonus += 0.7
            else:
                bonus += 0.2
    return bonus


def coordination_support_priority(item: dict, primary_skill: Optional[str], inferred_intents: Sequence[str], role_key: Optional[str]) -> float:
    if "coordination" not in inferred_intents:
        return 0.0
    priority = 0.0
    skill = item["skill"]
    path = item["path"]
    if role_key == "pinchy" and skill == "orchestrator-pinchy":
        priority += 4.0
    elif skill == primary_skill:
        priority += 2.6
    elif skill in {"operations", "multi-agent-reef"}:
        priority += 1.9
    if path.endswith("AGENTS.md"):
        priority += 2.2
    elif path.endswith("SKILL.md"):
        priority += 1.8
    elif path.endswith("MEMORY.md"):
        priority += 1.4
    elif path.endswith("SOUL.md"):
        priority += 1.0
    elif path.endswith("TOOLS.md"):
        priority += 0.7
    return priority


def is_coordination_anchor(item: dict) -> bool:
    if item["skill"] not in COORDINATION_SUPPORT_SKILLS:
        return False
    if item["file_type"] not in {"skill_doc", "skill_contract", "memory_router"}:
        return False
    return item["path"].endswith(("AGENTS.md", "SKILL.md", "MEMORY.md", "SOUL.md"))


def decide(db_path: Path, query: str, role: Optional[str], top: int, workspace_enabled: bool = True) -> dict:
    results = rank_chunks(
        db_path,
        query,
        role=role,
        skill_filter=None,
        top=max(top * 5, 20),
        workspace_enabled=workspace_enabled,
    )
    expanded_query, inferred_intents, expansion_terms = expand_query(query, role)
    workspace_context = (
        workspace_context_snapshot(db_path, expanded_query, role, top=max(4, top))
        if workspace_enabled
        else {"active_contexts": 0, "active_items": 0, "hits": [], "tokens": set(), "roles": set(), "context_ids": [], "contexts": []}
    )
    db_key = db_revision_token(db_path)
    query_tokens = set(tokenize(expanded_query))
    squad_router = cached_squad_router(*file_revision_token(SKILLS_ROOT / "SQUAD_MEMORY.md"))
    role_key = role.lower() if role else None
    learned_skill_priors = cached_learned_skill_priors(*db_key, learned_bucket_key(inferred_intents))
    outcome_skill_priors = cached_outcome_skill_priors(*db_key, role_bucket_key(inferred_intents, role), role.lower() if role else "")
    result_skill_priors = cached_result_skill_priors(*db_key, role_bucket_key(inferred_intents, role), role.lower() if role else "")
    skills = defaultdict(lambda: {"scores": [], "paths": set(), "headings": []})
    for item in results:
        if item["skill"] == "squad_router":
            continue
        if item["skill"] == "blank-agent-kit":
            continue
        if item["skill"].startswith(".system") and not (query_tokens & OPENAI_QUERY_HINTS):
            continue
        weight = item["score"]
        skills[item["skill"]]["scores"].append(weight)
        skills[item["skill"]]["paths"].add(item["path"])
        if len(skills[item["skill"]]["headings"]) < 3:
            skills[item["skill"]]["headings"].append(item["heading"])

    ranked_skills = sorted(
        (
            {
                "skill": skill,
                "score": round(
                    (
                        max(data["scores"])
                        + sum(sorted(data["scores"], reverse=True)[1:4]) * 0.35
                        + min(len(query_tokens & set(SKILL_ALIASES.get(skill, []))) * 0.45, 1.35)
                        + min(len(query_tokens & set(squad_router.skill_tags.get(skill, []))) * 0.35, 1.05)
                        + sum(INTENT_SKILL_PRIORS.get(intent, {}).get(skill, 0.0) for intent in inferred_intents)
                        + sum(
                            ROLE_INTENT_SKILL_PRIORS.get((role_key, intent), {}).get(skill, 0.0)
                            for intent in inferred_intents
                        )
                        + skill_intent_decision_bonus(skill, inferred_intents, query_tokens)
                        + (0.0 if skill not in learned_skill_priors else max(min(learned_skill_priors[skill] * 0.85, 0.65), -0.35))
                        + (0.0 if skill not in outcome_skill_priors else max(min(outcome_skill_priors[skill] * 0.95, 0.72), -0.38))
                        + (0.0 if skill not in result_skill_priors else max(min(result_skill_priors[skill] * 1.05, 0.82), -0.42))
                    ),
                    4,
                ),
                "supporting_paths": sorted(data["paths"])[:5],
                "headings": data["headings"],
            }
            for skill, data in skills.items()
        ),
        key=lambda item: item["score"],
        reverse=True,
    )[:top]
    ranked_skills = apply_variant_preferences(ranked_skills, inferred_intents)

    preferred_skills = [item["skill"] for item in ranked_skills[:3]]
    primary_skill = preferred_skills[0] if preferred_skills else None
    allow_system_refs = bool(query_tokens & OPENAI_QUERY_HINTS)
    supporting_memory: List[dict] = []
    seen_chunk_ids = set()
    seen_paths = set()

    def collect(matches) -> None:
        for item in results:
            if item["chunk_id"] in seen_chunk_ids:
                continue
            if item["path"] in seen_paths:
                continue
            if item["file_type"] == "squad_router":
                continue
            if item["skill"].startswith(".system") and not allow_system_refs:
                continue
            if low_signal_support_heading(item["heading"]):
                continue
            if not matches(item):
                continue
            supporting_memory.append(item)
            seen_chunk_ids.add(item["chunk_id"])
            seen_paths.add(item["path"])
            if len(supporting_memory) >= top * 2:
                break

    if "coordination" in inferred_intents:
        collect(
            lambda item: item["skill"] == primary_skill
            and item["file_type"] in {"skill_doc", "skill_contract", "memory_router"}
        )
        collect(
            lambda item: item["skill"] in COORDINATION_SUPPORT_SKILLS - {primary_skill}
            and item["file_type"] in {"skill_doc", "skill_contract", "memory_router"}
        )
    collect(lambda item: item["skill"] == primary_skill and item["file_type"] in {"memory_note", "reference_note"})
    collect(lambda item: item["skill"] == primary_skill and item["file_type"] in {"skill_doc", "skill_contract", "memory_router"})
    collect(lambda item: item["skill"] in preferred_skills[1:] and item["file_type"] in {"memory_note", "reference_note"})
    collect(lambda item: item["skill"] in preferred_skills[1:] and item["file_type"] in {"skill_doc", "skill_contract", "memory_router"})
    collect(lambda item: item["file_type"] in {"memory_note", "reference_note"})
    collect(lambda item: item["file_type"] not in {"memory_index", "squad_router"})

    primary_target = min(2, top)
    if "coordination" in inferred_intents and primary_skill == "orchestrator-pinchy":
        primary_target = max(primary_target, 4)
    primary_count = sum(1 for item in supporting_memory if item["skill"] == primary_skill)
    if primary_skill and primary_count < primary_target:
        primary_only = rank_chunks(
            db_path,
            query,
            role=role,
            skill_filter=primary_skill,
            top=max(top, 4),
            workspace_enabled=workspace_enabled,
        )
        if "coordination" in inferred_intents:
            primary_only = sorted(
                primary_only,
                key=lambda item: (coordination_support_priority(item, primary_skill, inferred_intents, role_key), item["score"]),
                reverse=True,
            )
        primary_prefix: List[dict] = []
        for item in primary_only:
            if item["chunk_id"] in seen_chunk_ids:
                continue
            if item["path"] in seen_paths:
                continue
            if item["file_type"] in {"memory_index", "squad_router"}:
                continue
            if low_signal_support_heading(item["heading"]):
                continue
            primary_prefix.append(item)
            seen_chunk_ids.add(item["chunk_id"])
            seen_paths.add(item["path"])
            primary_count += 1
            if primary_count >= primary_target:
                break
        if primary_prefix:
            supporting_memory = primary_prefix + supporting_memory

    if "coordination" in inferred_intents and role_key == "pinchy":
        coordination_prefix: List[dict] = []
        coordination_candidates: List[dict] = []
        for anchor_skill in ("orchestrator-pinchy", "operations", "multi-agent-reef"):
            coordination_candidates.extend(
                rank_chunks(
                    db_path,
                    query,
                    role=role,
                    skill_filter=anchor_skill,
                    top=max(top, 6),
                    workspace_enabled=workspace_enabled,
                )
            )
        coordination_candidates = sorted(
            coordination_candidates,
            key=lambda item: (coordination_support_priority(item, primary_skill, inferred_intents, role_key), item["score"]),
            reverse=True,
        )
        for item in coordination_candidates:
            if not is_coordination_anchor(item):
                continue
            if item["chunk_id"] in seen_chunk_ids:
                continue
            if item["path"] in seen_paths:
                continue
            if low_signal_support_heading(item["heading"]):
                continue
            coordination_prefix.append(item)
            seen_chunk_ids.add(item["chunk_id"])
            seen_paths.add(item["path"])
            if len(coordination_prefix) >= 3:
                break
        if coordination_prefix:
            supporting_memory = coordination_prefix + supporting_memory

    if primary_skill == "seo" and {"ai_visibility", "ai_overviews"} & set(inferred_intents):
        visibility_prefix: List[dict] = []
        visibility_candidates = list(results)
        visibility_candidates.extend(
            rank_chunks(
                db_path,
                query,
                role=role,
                skill_filter="seo",
                top=max(top * 6, 24),
                workspace_enabled=workspace_enabled,
            )
        )
        for preferred_path in AI_VISIBILITY_CANON_PATHS:
            for item in visibility_candidates:
                if item["path"] != preferred_path:
                    continue
                if item["chunk_id"] in seen_chunk_ids:
                    continue
                if item["path"] in seen_paths:
                    continue
                visibility_prefix.append(item)
                seen_chunk_ids.add(item["chunk_id"])
                seen_paths.add(item["path"])
                break
            else:
                item = cached_support_item_by_path(*db_revision_token(db_path), preferred_path)
                if not item:
                    continue
                if item["chunk_id"] in seen_chunk_ids:
                    continue
                if item["path"] in seen_paths:
                    continue
                visibility_prefix.append(item)
                seen_chunk_ids.add(item["chunk_id"])
                seen_paths.add(item["path"])
        if visibility_prefix:
            supporting_memory = visibility_prefix + supporting_memory

    if "coordination" in inferred_intents:
        supporting_memory = sorted(
            supporting_memory,
            key=lambda item: (coordination_support_priority(item, primary_skill, inferred_intents, role_key), item["score"]),
            reverse=True,
        )

    if len(supporting_memory) < top * 2:
        supporting_memory = results[: top * 2]

    return {
        "query": query,
        "role": role,
        "inferred_intents": inferred_intents,
        "expansion_terms": expansion_terms,
        "workspace_context": workspace_context,
        "recommended_skills": ranked_skills,
        "supporting_memory": supporting_memory[: top * 2],
    }


def plan_for_pinchy(db_path: Path, query: str, top: int) -> dict:
    decision = decide(db_path, query, role="pinchy", top=top)
    skills = decision["recommended_skills"]
    primary = skills[0]["skill"] if skills else None
    support = [item["skill"] for item in skills[1:3]]
    memory = []
    seen_paths = set()
    for item in decision["supporting_memory"]:
        if item["path"] in seen_paths:
            continue
        seen_paths.add(item["path"])
        memory.append(item)
        if len(memory) >= 8:
            break
    themes = []
    for item in memory:
        theme = item["canonical_group"]
        if not theme and item.get("topics"):
            theme = item["topics"][0].replace("_", " ")
        if theme and theme not in themes:
            themes.append(theme)
    plan_steps = [
        "Identify the primary skill and supporting memory before answering.",
        "Use canonical notes first, then one supporting note per topic if needed.",
        "Keep the active context minimal and focused on the retrieved themes.",
    ]
    if memory:
        plan_steps.append("Prioritize the top-ranked memory notes before opening router or contract files.")

    return {
        "query": query,
        "role": "pinchy",
        "inferred_intents": decision.get("inferred_intents", []),
        "expansion_terms": decision.get("expansion_terms", []),
        "workspace_context": decision.get("workspace_context", {}),
        "primary_skill": primary,
        "supporting_skills": support,
        "memory_themes": themes,
        "memory_shortlist": memory,
        "plan_steps": plan_steps,
    }


def build_task_pack_memory_shortlist(
    db_path: Path,
    query: str,
    role: Optional[str],
    pack: TaskPack,
    decision: dict,
    top: int,
    pack_path_priors: Optional[Dict[str, float]] = None,
    workspace_enabled: bool = True,
) -> List[dict]:
    pack_path_priors = pack_path_priors or {}
    pool: List[dict] = []
    scoped_query = query
    if pack.memory_focus:
        scoped_query = f"{query} {' '.join(pack.memory_focus[:8])}"

    for skill in [pack.primary_skill] + pack.supporting_skills[:3]:
        if not skill:
            continue
        pool.extend(
            rank_chunks(
                db_path,
                scoped_query,
                role=role,
                skill_filter=skill,
                top=max(top * 2, 6),
                pack_id=pack.pack_id,
                workspace_enabled=workspace_enabled,
            )
        )
    pool.extend(decision.get("supporting_memory", []))

    ranked: List[dict] = []
    seen_chunk_ids = set()
    allow_system_refs = bool(set(tokenize(query)) & OPENAI_QUERY_HINTS)
    for item in pool:
        chunk_id = item.get("chunk_id")
        if chunk_id in seen_chunk_ids:
            continue
        seen_chunk_ids.add(chunk_id)
        if item["skill"].startswith(".system") and not allow_system_refs:
            continue
        focus_hits = pack_focus_overlap(item, pack)
        bonus = 0.0
        if item["skill"] == pack.primary_skill:
            bonus += 0.45
        elif item["skill"] in pack.supporting_skills:
            bonus += 0.25
        if item["file_type"] in {"memory_note", "reference_note"}:
            bonus += 0.12
        elif item["file_type"] in {"skill_doc", "skill_contract", "memory_router"}:
            bonus += 0.08
        bonus += min(focus_hits * 0.16, 0.48)
        bonus += max(min(pack_path_priors.get(item["path"], 0.0) * 0.5, 0.32), -0.2)
        if item.get("canonical_group"):
            bonus += 0.05
        ranked_item = dict(item)
        ranked_item["pack_score"] = round(item.get("score", 0.0) + bonus, 4)
        ranked_item["pack_focus_hits"] = focus_hits
        ranked.append(ranked_item)

    ranked.sort(key=lambda item: item["pack_score"], reverse=True)
    selected: List[dict] = []
    seen_paths = set()
    for item in ranked:
        if item["path"] in seen_paths:
            continue
        seen_paths.add(item["path"])
        selected.append(item)
        if len(selected) >= top:
            break
    return selected


def resolve_task_pack(
    db_path: Path,
    packs_path: Path,
    query: str,
    role: Optional[str],
    top: int,
    pack_id: Optional[str] = None,
    workspace_enabled: bool = True,
) -> dict:
    decision = decide(db_path, query, role=role, top=max(top, 5), workspace_enabled=workspace_enabled)
    packs = list(cached_task_packs(*file_revision_token(packs_path)))
    db_key = db_revision_token(db_path)
    learned_pack_priors = cached_learned_pack_priors(
        *db_key,
        role_bucket_key(decision.get("inferred_intents", []), role),
        role.lower() if role else "",
    )
    result_pack_priors = cached_result_pack_priors(
        *db_key,
        role_bucket_key(decision.get("inferred_intents", []), role),
        role.lower() if role else "",
    )

    scored_packs = [score_task_pack(pack, query, role, decision) for pack in packs]
    for item in scored_packs:
        learned_bonus = max(min(learned_pack_priors.get(item["pack"].pack_id, 0.0) * 0.85, 0.9), -0.5)
        if learned_bonus:
            item["score"] = round(item["score"] + learned_bonus, 4)
            item["reasons"].append(f"Learned outcome prior: {learned_bonus:+.2f}")
        result_bonus = max(min(result_pack_priors.get(item["pack"].pack_id, 0.0) * 1.05, 1.0), -0.55)
        if result_bonus:
            item["score"] = round(item["score"] + result_bonus, 4)
            item["reasons"].append(f"Scorecard quality prior: {result_bonus:+.2f}")
    scored_packs.sort(key=lambda item: item["score"], reverse=True)

    if pack_id:
        pack = find_task_pack(packs, pack_id)
        selected = next((item for item in scored_packs if item["pack"].pack_id == pack_id), None)
        if selected is None:
            selected = {"pack": pack, "score": 0.0, "reasons": []}
        selected = {
            **selected,
            "score": round(selected["score"] + 5.0, 4),
            "reasons": ["Explicit pack override", *selected["reasons"]],
        }
    else:
        if not scored_packs:
            raise ValueError(f"No task packs found in {packs_path}")
        selected = scored_packs[0]
        pack = selected["pack"]

    pack_path_priors = cached_pack_path_priors(*db_key, pack.pack_id)
    pack_skill_priors = cached_pack_skill_priors(*db_key, pack.pack_id)
    shortlist = build_task_pack_memory_shortlist(
        db_path,
        query,
        role,
        pack,
        decision,
        top=max(top * 2, 8),
        pack_path_priors=pack_path_priors,
        workspace_enabled=workspace_enabled,
    )
    workspace_context = (
        workspace_context_snapshot(db_path, query, role, top=max(4, top), pack_id=pack.pack_id)
        if workspace_enabled
        else {"active_contexts": 0, "active_items": 0, "hits": [], "tokens": set(), "roles": set(), "context_ids": [], "contexts": []}
    )
    themes = summarize_memory_themes(shortlist, limit=6)

    runner_ups = []
    for item in scored_packs:
        if item["pack"].pack_id == pack.pack_id:
            continue
        runner_ups.append(
            {
                "id": item["pack"].pack_id,
                "name": item["pack"].name,
                "score": item["score"],
            }
        )
        if len(runner_ups) >= 3:
            break

    return {
        "query": query,
        "role": role,
        "inferred_intents": decision.get("inferred_intents", []),
        "expansion_terms": decision.get("expansion_terms", []),
        "selected_pack": {
            **task_pack_to_dict(pack),
            "score": selected["score"],
            "reasons": selected["reasons"][:5],
        },
        "runner_up_packs": runner_ups,
        "recommended_skills": decision.get("recommended_skills", []),
        "learned_pack_skill_priors": pack_skill_priors,
        "workspace_context": workspace_context,
        "memory_themes": themes,
        "memory_shortlist": shortlist,
    }


def build_execute_plan(
    db_path: Path,
    packs_path: Path,
    query: str,
    role: Optional[str],
    top: int,
    pack_id: Optional[str] = None,
    workspace_enabled: bool = True,
) -> dict:
    task_pack = resolve_task_pack(
        db_path,
        packs_path,
        query,
        role,
        top,
        pack_id=pack_id,
        workspace_enabled=workspace_enabled,
    )
    pack_info = task_pack["selected_pack"]
    recommended_skills = task_pack.get("recommended_skills", [])
    plan_steps = list(pack_info.get("checklist", []))
    if not plan_steps:
        plan_steps = [
            "Confirm the primary skill and scope.",
            "Load the top supporting memory before answering.",
            "Produce the deliverable in the required output format.",
        ]

    return {
        "query": query,
        "role": role,
        "inferred_intents": task_pack.get("inferred_intents", []),
        "expansion_terms": task_pack.get("expansion_terms", []),
        "workspace_context": task_pack.get("workspace_context", {}),
        "selected_pack": pack_info,
        "recommended_skills": recommended_skills,
        "primary_skill": pack_info.get("primary_skill"),
        "supporting_skills": pack_info.get("supporting_skills", []),
        "memory_themes": task_pack.get("memory_themes", []),
        "memory_shortlist": task_pack.get("memory_shortlist", []),
        "execution_steps": plan_steps,
        "deliverables": pack_info.get("deliverables", []),
        "output_sections": pack_info.get("output_sections", []),
        "handoff_plan": pack_info.get("handoffs", []),
        "escalation_rules": pack_info.get("escalation_rules", []),
    }


def start_pack_run(
    db_path: Path,
    packs_path: Path,
    query: str,
    role: Optional[str],
    top: int,
    status: str = "active",
    notes: str = "",
    pack_id: Optional[str] = None,
) -> dict:
    plan = build_execute_plan(db_path, packs_path, query, role, top, pack_id=pack_id)
    pack = plan["selected_pack"]
    steps = run_step_rows_from_plan(plan)
    if steps and status in {"active", "blocked"}:
        steps[0]["status"] = "active" if status == "active" else "blocked"

    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        metadata = {
            "memory_themes": plan.get("memory_themes", [])[:8],
            "deliverables": plan.get("deliverables", [])[:8],
            "output_sections": plan.get("output_sections", [])[:8],
            "handoff_plan": plan.get("handoff_plan", [])[:8],
            "escalation_rules": plan.get("escalation_rules", [])[:8],
        }
        con.execute(
            """
            INSERT INTO pack_runs(
              query, role, pack_id, pack_name, primary_skill, supporting_skills_json,
              status, current_step_seq, step_count, blocker_count, handoff_count, notes, metadata_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0, ?, ?)
            """,
            (
                query,
                role,
                pack["id"],
                pack["name"],
                plan["primary_skill"],
                json.dumps(plan.get("supporting_skills", [])),
                status,
                1 if steps and status in {"active", "blocked"} else 0,
                len(steps),
                notes,
                json.dumps(metadata, ensure_ascii=True),
            ),
        )
        run_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        for step in steps:
            con.execute(
                """
                INSERT INTO pack_run_steps(run_id, seq, title, step_kind, owner_skill, status, evidence_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    run_id,
                    step["seq"],
                    step["title"],
                    step["step_kind"],
                    step["owner_skill"],
                    step["status"],
                    json.dumps({}, ensure_ascii=True),
                ),
            )
        run = refresh_pack_run_state_in_connection(con, run_id)
        emit_event_in_connection(
            con,
            event_type="pack_run.started",
            event_group="execution",
            source="squad_memory",
            status=run["status"],
            query=query,
            role=role,
            pack_id=pack["id"],
            skill=plan["primary_skill"],
            metadata={
                "run_id": run_id,
                "step_count": len(steps),
                "supporting_skills": plan.get("supporting_skills", []),
            },
        )
        con.commit()
        run = fetch_pack_run_in_connection(con, run_id) or run
        step_rows = fetch_pack_run_steps_in_connection(con, run_id)
    finally:
        con.close()

    return {
        "db": str(db_path),
        "run_id": run_id,
        "query": query,
        "role": role,
        "selected_pack": pack,
        "status": run["status"],
        "current_step_seq": run["current_step_seq"],
        "primary_skill": plan["primary_skill"],
        "supporting_skills": plan.get("supporting_skills", []),
        "steps": step_rows,
    }


def update_pack_run_step(
    db_path: Path,
    run_id: int,
    step_seq: int,
    *,
    status: str,
    owner_skill: Optional[str] = None,
    notes: str = "",
    artifact_path: str = "",
) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        existing = con.execute(
            "SELECT id FROM pack_run_steps WHERE run_id = ? AND seq = ?",
            (run_id, step_seq),
        ).fetchone()
        if existing is None:
            raise ValueError(f"Unknown run step: run={run_id} seq={step_seq}")
        updates = ["status = ?", "ts_updated = CURRENT_TIMESTAMP"]
        values: List[Any] = [status]
        if owner_skill is not None:
            updates.append("owner_skill = ?")
            values.append(owner_skill)
        if notes:
            updates.append("notes = CASE WHEN notes = '' THEN ? ELSE notes || '\n' || ? END")
            values.extend([notes, notes])
        if artifact_path:
            updates.append("artifact_path = ?")
            values.append(artifact_path)
        values.extend([run_id, step_seq])
        con.execute(
            f"UPDATE pack_run_steps SET {', '.join(updates)} WHERE run_id = ? AND seq = ?",
            tuple(values),
        )
        run = refresh_pack_run_state_in_connection(con, run_id)
        emit_event_in_connection(
            con,
            event_type="pack_run.step_updated",
            event_group="execution",
            source="squad_memory",
            status=run["status"],
            query=run["query"],
            role=run["role"] or None,
            pack_id=run["pack_id"],
            skill=owner_skill or run["primary_skill"],
            metadata={
                "run_id": run_id,
                "step_seq": step_seq,
                "step_status": status,
                "artifact_path": artifact_path,
            },
        )
        con.commit()
        step_rows = fetch_pack_run_steps_in_connection(con, run_id)
    finally:
        con.close()

    return {
        "db": str(db_path),
        "run_id": run_id,
        "status": run["status"],
        "current_step_seq": run["current_step_seq"],
        "steps": step_rows,
    }


def record_pack_run_handoff(
    db_path: Path,
    run_id: int,
    *,
    from_skill: str,
    to_skill: str,
    reason: str = "",
    notes: str = "",
) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        run = fetch_pack_run_in_connection(con, run_id)
        if run is None:
            raise ValueError(f"Unknown pack run: {run_id}")
        con.execute(
            """
            INSERT INTO pack_run_handoffs(run_id, from_skill, to_skill, reason, notes, status, metadata_json)
            VALUES (?, ?, ?, ?, ?, 'sent', ?)
            """,
            (
                run_id,
                from_skill,
                to_skill,
                reason,
                notes,
                json.dumps({}, ensure_ascii=True),
            ),
        )
        active_step = con.execute(
            "SELECT id FROM pack_run_steps WHERE run_id = ? AND status = 'active' ORDER BY seq ASC LIMIT 1",
            (run_id,),
        ).fetchone()
        if active_step is not None:
            con.execute(
                "UPDATE pack_run_steps SET owner_skill = ?, ts_updated = CURRENT_TIMESTAMP WHERE id = ?",
                (to_skill, int(active_step[0])),
            )
        run = refresh_pack_run_state_in_connection(con, run_id)
        emit_event_in_connection(
            con,
            event_type="pack_run.handoff",
            event_group="execution",
            source="squad_memory",
            status=run["status"],
            query=run["query"],
            role=run["role"] or None,
            pack_id=run["pack_id"],
            skill=to_skill,
            metadata={
                "run_id": run_id,
                "from_skill": from_skill,
                "to_skill": to_skill,
                "reason": reason,
            },
        )
        con.commit()
        handoffs = fetch_pack_run_handoffs_in_connection(con, run_id)
        step_rows = fetch_pack_run_steps_in_connection(con, run_id)
    finally:
        con.close()

    return {
        "db": str(db_path),
        "run_id": run_id,
        "status": run["status"],
        "handoffs": handoffs,
        "steps": step_rows,
    }


def record_pack_run_blocker(
    db_path: Path,
    run_id: int,
    *,
    blocker_id: Optional[int] = None,
    step_seq: Optional[int] = None,
    title: str = "",
    severity: str = "medium",
    owner_skill: Optional[str] = None,
    status: str = "open",
    notes: str = "",
) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        run = fetch_pack_run_in_connection(con, run_id)
        if run is None:
            raise ValueError(f"Unknown pack run: {run_id}")
        if blocker_id is not None:
            if status == "resolved":
                con.execute(
                    """
                    UPDATE pack_run_blockers
                    SET status = 'resolved',
                        ts_resolved = CURRENT_TIMESTAMP,
                        notes = CASE WHEN notes = '' THEN ? ELSE notes || '\n' || ? END
                    WHERE id = ? AND run_id = ?
                    """,
                    (notes, notes, blocker_id, run_id),
                )
            else:
                con.execute(
                    """
                    UPDATE pack_run_blockers
                    SET notes = CASE WHEN notes = '' THEN ? ELSE notes || '\n' || ? END
                    WHERE id = ? AND run_id = ?
                    """,
                    (notes, notes, blocker_id, run_id),
                )
        else:
            if not title:
                raise ValueError("title is required when creating a blocker")
            con.execute(
                """
                INSERT INTO pack_run_blockers(run_id, step_seq, title, severity, owner_skill, status, notes, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    run_id,
                    step_seq,
                    title,
                    severity,
                    owner_skill,
                    status,
                    notes,
                    json.dumps({}, ensure_ascii=True),
                ),
            )
        run = refresh_pack_run_state_in_connection(con, run_id)
        emit_event_in_connection(
            con,
            event_type="pack_run.blocker",
            event_group="execution",
            source="squad_memory",
            status=status,
            query=run["query"],
            role=run["role"] or None,
            pack_id=run["pack_id"],
            skill=owner_skill or run["primary_skill"],
            metadata={
                "run_id": run_id,
                "blocker_id": blocker_id,
                "step_seq": step_seq,
                "title": title,
                "severity": severity,
                "blocker_status": status,
            },
        )
        con.commit()
        blockers = fetch_pack_run_blockers_in_connection(con, run_id)
    finally:
        con.close()

    return {
        "db": str(db_path),
        "run_id": run_id,
        "status": run["status"],
        "blockers": blockers,
    }


def pack_run_report(db_path: Path, packs_path: Path, limit: int, status_filter: Optional[str] = None) -> dict:
    pack_map = {pack.pack_id: pack for pack in load_task_packs(packs_path)}
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        ensure_learning_tables(con)
        params: List[Any] = []
        where_sql = ""
        if status_filter:
            where_sql = "WHERE status = ?"
            params.append(status_filter)
        total_runs = int(con.execute("SELECT COUNT(*) FROM pack_runs").fetchone()[0])
        active_runs = int(con.execute("SELECT COUNT(*) FROM pack_runs WHERE status = 'active'").fetchone()[0])
        blocked_runs = int(con.execute("SELECT COUNT(*) FROM pack_runs WHERE status = 'blocked'").fetchone()[0])
        completed_runs = int(con.execute("SELECT COUNT(*) FROM pack_runs WHERE status = 'completed'").fetchone()[0])
        open_blockers = int(con.execute("SELECT COUNT(*) FROM pack_run_blockers WHERE status = 'open'").fetchone()[0])
        rows = con.execute(
            f"""
            SELECT id, ts_started, ts_updated, ts_completed, query, role, pack_id, pack_name, primary_skill,
                   supporting_skills_json, status, current_step_seq, step_count, blocker_count, handoff_count, notes, metadata_json
            FROM pack_runs
            {where_sql}
            ORDER BY ts_updated DESC, id DESC
            LIMIT ?
            """,
            tuple(params + [limit]),
        ).fetchall()
        recent_runs = []
        for row in rows:
            run_id = int(row["id"])
            steps = fetch_pack_run_steps_in_connection(con, run_id)
            blockers = fetch_pack_run_blockers_in_connection(con, run_id)
            handoffs = fetch_pack_run_handoffs_in_connection(con, run_id)
            recent_runs.append(
                {
                    "id": run_id,
                    "ts_started": str(row["ts_started"] or ""),
                    "ts_updated": str(row["ts_updated"] or ""),
                    "ts_completed": str(row["ts_completed"] or ""),
                    "query": str(row["query"] or ""),
                    "role": str(row["role"] or ""),
                    "pack_id": str(row["pack_id"] or ""),
                    "pack_name": str(row["pack_name"] or pack_map.get(str(row["pack_id"] or ""), TaskPack("", "", "", [], [], [], "", [], [], [], [], [], [], [])).name),
                    "primary_skill": str(row["primary_skill"] or ""),
                    "status": str(row["status"] or ""),
                    "current_step_seq": int(row["current_step_seq"] or 0),
                    "step_count": int(row["step_count"] or 0),
                    "blocker_count": int(row["blocker_count"] or 0),
                    "handoff_count": int(row["handoff_count"] or 0),
                    "notes": str(row["notes"] or ""),
                    "steps": steps,
                    "blockers": blockers[:5],
                    "handoffs": handoffs[:5],
                }
            )
    finally:
        con.close()

    return {
        "db": str(db_path),
        "total_runs": total_runs,
        "active_runs": active_runs,
        "blocked_runs": blocked_runs,
        "completed_runs": completed_runs,
        "open_blockers": open_blockers,
        "recent_runs": recent_runs,
        "status_filter": status_filter,
    }


def complete_task(
    db_path: Path,
    packs_path: Path,
    query: str,
    role: Optional[str],
    top: int,
    status: str,
    revision_count: int = 0,
    completion_minutes: Optional[float] = None,
    user_rating: Optional[float] = None,
    notes: str = "",
    pack_id: Optional[str] = None,
    used_paths: Optional[Sequence[str]] = None,
    used_skills: Optional[Sequence[str]] = None,
) -> dict:
    result = build_execute_plan(db_path, packs_path, query, role, top, pack_id=pack_id)
    primary_skill = result.get("primary_skill") or result["selected_pack"]["primary_skill"]
    supporting_skills = list(result.get("supporting_skills", []))
    memory_paths = [item["path"] for item in result.get("memory_shortlist", [])]

    resolved_used_paths = list(dict.fromkeys([path for path in (used_paths or memory_paths) if path]))
    resolved_used_skills = list(
        dict.fromkeys([skill for skill in (used_skills or ([primary_skill] + supporting_skills)) if skill])
    )

    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        con.execute(
            """
            INSERT INTO task_outcomes(
              query, role, pack_id, primary_skill, supporting_skills_json, used_skills_json,
              memory_paths_json, status, revision_count, completion_minutes, user_rating, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                query,
                role,
                result["selected_pack"]["id"],
                primary_skill,
                json.dumps(supporting_skills),
                json.dumps(resolved_used_skills),
                json.dumps(resolved_used_paths),
                status,
                max(revision_count, 0),
                completion_minutes,
                user_rating,
                notes,
            ),
        )
        outcome_id = con.execute("SELECT last_insert_rowid()").fetchone()[0]
        emit_event_in_connection(
            con,
            event_type="task.completed",
            event_group="task",
            source="squad_memory",
            status=status,
            query=query,
            role=role,
            pack_id=result["selected_pack"]["id"],
            skill=primary_skill,
            metadata={
                "outcome_id": outcome_id,
                "supporting_skills": supporting_skills,
                "used_skills": resolved_used_skills,
                "used_paths": resolved_used_paths[:8],
                "revision_count": max(revision_count, 0),
                "completion_minutes": completion_minutes,
                "user_rating": user_rating,
            },
        )
        con.commit()
    finally:
        con.close()

    return {
        "db": str(db_path),
        "outcome_id": outcome_id,
        "query": query,
        "role": role,
        "status": status,
        "revision_count": max(revision_count, 0),
        "completion_minutes": completion_minutes,
        "user_rating": user_rating,
        "notes": notes,
        "selected_pack": result["selected_pack"],
        "primary_skill": primary_skill,
        "supporting_skills": supporting_skills,
        "used_skills": resolved_used_skills,
        "used_paths": resolved_used_paths,
    }


def train_pack_priors(db_path: Path) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        summary = train_pack_priors_in_connection(con)
        con.commit()
        return {"db": str(db_path), **summary}
    finally:
        con.close()


def pack_report(db_path: Path, packs_path: Path, limit: int) -> dict:
    packs = {pack.pack_id: pack for pack in load_task_packs(packs_path)}
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        task_outcome_count = con.execute("SELECT COUNT(*) FROM task_outcomes").fetchone()[0]
        last_training_row = con.execute(
            """
            SELECT ts, task_outcomes, pack_priors, pack_path_priors, pack_skill_priors
            FROM pack_training_runs
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()

        top_packs_rows = con.execute(
            """
            SELECT pack_id, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_pack_priors
            WHERE bucket = ?
            ORDER BY score DESC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        weak_packs_rows = con.execute(
            """
            SELECT pack_id, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_pack_priors
            WHERE bucket = ?
            ORDER BY score ASC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        top_paths_rows = con.execute(
            """
            SELECT pack_id, path, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_pack_path_priors
            ORDER BY score DESC, exposure_count DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        weak_paths_rows = con.execute(
            """
            SELECT pack_id, path, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_pack_path_priors
            ORDER BY score ASC, exposure_count DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        top_skills_rows = con.execute(
            """
            SELECT pack_id, skill, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_pack_skill_priors
            ORDER BY score DESC, exposure_count DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        weak_skills_rows = con.execute(
            """
            SELECT pack_id, skill, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_pack_skill_priors
            ORDER BY score ASC, exposure_count DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        high_revision_rows = con.execute(
            """
            SELECT pack_id,
                   COUNT(*) AS outcomes,
                   AVG(revision_count) AS avg_revision_count,
                   AVG(CASE WHEN user_rating IS NOT NULL THEN user_rating END) AS avg_user_rating
            FROM task_outcomes
            GROUP BY pack_id
            HAVING outcomes > 0
            ORDER BY avg_revision_count DESC, outcomes DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    finally:
        con.close()

    def pack_name(pack_id: str) -> str:
        return packs.get(pack_id).name if pack_id in packs else pack_id

    def pack_dict(row) -> dict:
        pack_id, score, accepted_count, revised_count, failed_count, exposure_count = row
        return {
            "pack_id": pack_id,
            "pack_name": pack_name(pack_id),
            "score": score,
            "accepted_count": accepted_count,
            "revised_count": revised_count,
            "failed_count": failed_count,
            "exposure_count": exposure_count,
        }

    def path_dict(row) -> dict:
        pack_id, path, score, accepted_count, revised_count, failed_count, exposure_count = row
        return {
            "pack_id": pack_id,
            "pack_name": pack_name(pack_id),
            "path": path,
            "score": score,
            "accepted_count": accepted_count,
            "revised_count": revised_count,
            "failed_count": failed_count,
            "exposure_count": exposure_count,
        }

    def skill_dict(row) -> dict:
        pack_id, skill, score, accepted_count, revised_count, failed_count, exposure_count = row
        return {
            "pack_id": pack_id,
            "pack_name": pack_name(pack_id),
            "skill": skill,
            "score": score,
            "accepted_count": accepted_count,
            "revised_count": revised_count,
            "failed_count": failed_count,
            "exposure_count": exposure_count,
        }

    return {
        "db": str(db_path),
        "packs_file": str(packs_path),
        "task_outcomes": task_outcome_count,
        "last_pack_training": None
        if not last_training_row
        else {
            "ts": last_training_row[0],
            "task_outcomes": last_training_row[1],
            "pack_priors": last_training_row[2],
            "pack_path_priors": last_training_row[3],
            "pack_skill_priors": last_training_row[4],
        },
        "top_packs": [pack_dict(row) for row in top_packs_rows],
        "weak_packs": [pack_dict(row) for row in weak_packs_rows],
        "high_revision_packs": [
            {
                "pack_id": pack_id,
                "pack_name": pack_name(pack_id),
                "outcomes": outcomes,
                "avg_revision_count": round(avg_revision_count or 0.0, 3),
                "avg_user_rating": None if avg_user_rating is None else round(avg_user_rating, 3),
            }
            for pack_id, outcomes, avg_revision_count, avg_user_rating in high_revision_rows
        ],
        "top_pack_paths": [path_dict(row) for row in top_paths_rows],
        "weak_pack_paths": [path_dict(row) for row in weak_paths_rows],
        "top_pack_skills": [skill_dict(row) for row in top_skills_rows],
        "weak_pack_skills": [skill_dict(row) for row in weak_skills_rows],
    }


def outcome_report(db_path: Path, packs_path: Path, limit: int) -> dict:
    packs = {pack.pack_id: pack for pack in load_task_packs(packs_path)}
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        task_outcome_count = con.execute("SELECT COUNT(*) FROM task_outcomes").fetchone()[0]
        status_rows = con.execute(
            """
            SELECT status, COUNT(*) AS outcomes
            FROM task_outcomes
            GROUP BY status
            ORDER BY outcomes DESC, status ASC
            """
        ).fetchall()
        averages_row = con.execute(
            """
            SELECT AVG(revision_count),
                   AVG(CASE WHEN completion_minutes IS NOT NULL THEN completion_minutes END),
                   AVG(CASE WHEN user_rating IS NOT NULL THEN user_rating END)
            FROM task_outcomes
            """
        ).fetchone()
        last_outcome_row = con.execute(
            """
            SELECT ts, query, role, pack_id, status, revision_count, completion_minutes, user_rating, notes
            FROM task_outcomes
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()
        last_training_row = con.execute(
            """
            SELECT ts, task_outcomes, outcome_path_priors, outcome_skill_priors
            FROM outcome_training_runs
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()
        top_paths_rows = con.execute(
            """
            SELECT path, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_outcome_path_priors
            WHERE bucket = ? AND score > 0
            ORDER BY score DESC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        weak_paths_rows = con.execute(
            """
            SELECT path, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_outcome_path_priors
            WHERE bucket = ? AND exposure_count >= 2 AND score < 0.15
            ORDER BY score ASC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        top_skills_rows = con.execute(
            """
            SELECT skill, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_outcome_skill_priors
            WHERE bucket = ? AND score > 0
            ORDER BY score DESC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        weak_skills_rows = con.execute(
            """
            SELECT skill, score, accepted_count, revised_count, failed_count, exposure_count
            FROM learned_outcome_skill_priors
            WHERE bucket = ? AND exposure_count >= 2 AND score < 0.15
            ORDER BY score ASC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        overranked_rows = con.execute(
            """
            SELECT lp.path,
                   lp.score,
                   lp.exposure_count,
                   COALESCE(op.score, 0.0) AS outcome_score,
                   COALESCE(op.accepted_count, 0),
                   COALESCE(op.revised_count, 0),
                   COALESCE(op.failed_count, 0)
            FROM learned_path_priors lp
            LEFT JOIN learned_outcome_path_priors op
              ON op.bucket = lp.bucket
             AND op.path = lp.path
            WHERE lp.bucket = ?
              AND lp.score > 0.2
              AND lp.exposure_count >= 2
              AND COALESCE(op.score, 0.0) <= 0.1
            ORDER BY lp.score DESC, lp.exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        underused_rows = con.execute(
            """
            SELECT op.path,
                   op.score,
                   op.exposure_count,
                   COALESCE(lp.score, 0.0) AS retrieval_score,
                   op.accepted_count,
                   op.revised_count,
                   op.failed_count
            FROM learned_outcome_path_priors op
            LEFT JOIN learned_path_priors lp
              ON lp.bucket = op.bucket
             AND lp.path = op.path
            WHERE op.bucket = ?
              AND op.score > 0.3
              AND op.exposure_count >= 1
              AND COALESCE(lp.score, 0.0) <= 0.12
            ORDER BY op.score DESC, op.exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        recent_rows = con.execute(
            """
            SELECT ts, query, role, pack_id, primary_skill, status, revision_count, user_rating
            FROM task_outcomes
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        combo_rows = con.execute(
            """
            SELECT used_skills_json, COUNT(*) AS outcomes
            FROM task_outcomes
            GROUP BY used_skills_json
            ORDER BY outcomes DESC
            LIMIT ?
            """,
            (limit * 3,),
        ).fetchall()
        high_revision_rows = con.execute(
            """
            SELECT pack_id,
                   COUNT(*) AS outcomes,
                   AVG(revision_count) AS avg_revision_count,
                   AVG(CASE WHEN user_rating IS NOT NULL THEN user_rating END) AS avg_user_rating
            FROM task_outcomes
            GROUP BY pack_id
            HAVING outcomes > 0
            ORDER BY avg_revision_count DESC, outcomes DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    finally:
        con.close()

    def pack_name(pack_id: str) -> str:
        return packs.get(pack_id).name if pack_id in packs else pack_id

    def prior_dict(row, key_name: str) -> dict:
        key, score, accepted_count, revised_count, failed_count, exposure_count = row
        return {
            key_name: key,
            "score": round(float(score), 4),
            "accepted_count": accepted_count,
            "revised_count": revised_count,
            "failed_count": failed_count,
            "exposure_count": exposure_count,
        }

    skill_stacks = []
    for used_skills_json, outcomes in combo_rows:
        try:
            parsed = json.loads(used_skills_json or "[]")
            if not isinstance(parsed, list):
                parsed = []
        except json.JSONDecodeError:
            parsed = []
        normalized = [str(item).strip() for item in parsed if str(item).strip()]
        if not normalized:
            continue
        skill_stacks.append({"skills": normalized, "outcomes": outcomes})
        if len(skill_stacks) >= limit:
            break

    total_statuses = sum(count for _status, count in status_rows) or 1
    status_breakdown = []
    for status, count in status_rows:
        status_breakdown.append(
            {
                "status": status,
                "count": count,
                "rate": round(count / total_statuses, 4),
            }
        )

    averages = {
        "avg_revision_count": round(float(averages_row[0] or 0.0), 3) if averages_row else 0.0,
        "avg_completion_minutes": None
        if not averages_row or averages_row[1] is None
        else round(float(averages_row[1]), 3),
        "avg_user_rating": None if not averages_row or averages_row[2] is None else round(float(averages_row[2]), 3),
    }

    return {
        "db": str(db_path),
        "packs_file": str(packs_path),
        "task_outcomes": task_outcome_count,
        "status_breakdown": status_breakdown,
        "averages": averages,
        "last_outcome": None
        if not last_outcome_row
        else {
            "ts": last_outcome_row[0],
            "query": last_outcome_row[1],
            "role": last_outcome_row[2],
            "pack_id": last_outcome_row[3],
            "pack_name": pack_name(last_outcome_row[3]),
            "status": last_outcome_row[4],
            "revision_count": last_outcome_row[5],
            "completion_minutes": last_outcome_row[6],
            "user_rating": last_outcome_row[7],
            "notes": last_outcome_row[8],
        },
        "last_outcome_training": None
        if not last_training_row
        else {
            "ts": last_training_row[0],
            "task_outcomes": last_training_row[1],
            "outcome_path_priors": last_training_row[2],
            "outcome_skill_priors": last_training_row[3],
        },
        "top_outcome_paths": [prior_dict(row, "path") for row in top_paths_rows],
        "weak_outcome_paths": [prior_dict(row, "path") for row in weak_paths_rows],
        "top_outcome_skills": [prior_dict(row, "skill") for row in top_skills_rows],
        "weak_outcome_skills": [prior_dict(row, "skill") for row in weak_skills_rows],
        "overranked_paths": [
            {
                "path": path,
                "retrieval_score": round(float(retrieval_score), 4),
                "retrieval_exposure_count": retrieval_exposure_count,
                "outcome_score": round(float(outcome_score), 4),
                "accepted_count": accepted_count,
                "revised_count": revised_count,
                "failed_count": failed_count,
            }
            for path, retrieval_score, retrieval_exposure_count, outcome_score, accepted_count, revised_count, failed_count in overranked_rows
        ],
        "underused_winners": [
            {
                "path": path,
                "outcome_score": round(float(outcome_score), 4),
                "outcome_exposure_count": outcome_exposure_count,
                "retrieval_score": round(float(retrieval_score), 4),
                "accepted_count": accepted_count,
                "revised_count": revised_count,
                "failed_count": failed_count,
            }
            for path, outcome_score, outcome_exposure_count, retrieval_score, accepted_count, revised_count, failed_count in underused_rows
        ],
        "top_skill_stacks": skill_stacks,
        "high_revision_packs": [
            {
                "pack_id": pack_id,
                "pack_name": pack_name(pack_id),
                "outcomes": outcomes,
                "avg_revision_count": round(avg_revision_count or 0.0, 3),
                "avg_user_rating": None if avg_user_rating is None else round(avg_user_rating, 3),
            }
            for pack_id, outcomes, avg_revision_count, avg_user_rating in high_revision_rows
        ],
        "recent_outcomes": [
            {
                "ts": ts,
                "query": query,
                "role": role,
                "pack_id": pack_id,
                "pack_name": pack_name(pack_id),
                "primary_skill": primary_skill,
                "status": status,
                "revision_count": revision_count,
                "user_rating": user_rating,
            }
            for ts, query, role, pack_id, primary_skill, status, revision_count, user_rating in recent_rows
        ],
    }


def task_result_report(db_path: Path, packs_path: Path, limit: int) -> dict:
    packs = {pack.pack_id: pack for pack in load_task_packs(packs_path)}
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        outcomes = fetch_task_outcomes_in_connection(con)
        scorecards = fetch_task_result_scorecards_in_connection(con)
        last_training_row = con.execute(
            """
            SELECT ts, scored_outcomes, manual_scorecards, suggested_scorecards,
                   result_pack_priors, result_path_priors, result_skill_priors
            FROM result_training_runs
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()
        top_learned_pack_rows = con.execute(
            """
            SELECT pack_id, score, avg_overall_score, manual_count, suggested_count, exposure_count
            FROM learned_result_pack_priors
            WHERE bucket = ?
            ORDER BY score DESC, avg_overall_score DESC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        weak_learned_pack_rows = con.execute(
            """
            SELECT pack_id, score, avg_overall_score, manual_count, suggested_count, exposure_count
            FROM learned_result_pack_priors
            WHERE bucket = ? AND exposure_count >= 1 AND score < 0.2
            ORDER BY score ASC, avg_overall_score ASC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        top_learned_path_rows = con.execute(
            """
            SELECT path, score, avg_overall_score, manual_count, suggested_count, exposure_count
            FROM learned_result_path_priors
            WHERE bucket = ?
            ORDER BY score DESC, avg_overall_score DESC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        weak_learned_path_rows = con.execute(
            """
            SELECT path, score, avg_overall_score, manual_count, suggested_count, exposure_count
            FROM learned_result_path_priors
            WHERE bucket = ? AND exposure_count >= 1 AND score < 0.18
            ORDER BY score ASC, avg_overall_score ASC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        top_learned_skill_rows = con.execute(
            """
            SELECT skill, score, avg_overall_score, manual_count, suggested_count, exposure_count
            FROM learned_result_skill_priors
            WHERE bucket = ?
            ORDER BY score DESC, avg_overall_score DESC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
        weak_learned_skill_rows = con.execute(
            """
            SELECT skill, score, avg_overall_score, manual_count, suggested_count, exposure_count
            FROM learned_result_skill_priors
            WHERE bucket = ? AND exposure_count >= 1 AND score < 0.18
            ORDER BY score ASC, avg_overall_score ASC, exposure_count DESC
            LIMIT ?
            """,
            (GLOBAL_BUCKET, limit),
        ).fetchall()
    finally:
        con.close()

    def pack_name(pack_id: str) -> str:
        return packs.get(pack_id).name if pack_id in packs else pack_id

    scored_rows: List[Dict[str, Any]] = []
    pending_rows: List[Dict[str, Any]] = []
    for outcome in outcomes:
        scorecard = scorecards.get(outcome["id"])
        if scorecard is None:
            pending_rows.append(
                {
                    "outcome_id": outcome["id"],
                    "ts": outcome["ts"],
                    "query": outcome["query"],
                    "pack_id": outcome["pack_id"],
                    "pack_name": pack_name(outcome["pack_id"]),
                    "primary_skill": outcome["primary_skill"],
                    "status": outcome["status"],
                    "suggested": suggest_task_result_scorecard(outcome),
                }
            )
            continue
        merged = {**outcome, **scorecard, "pack_name": pack_name(outcome["pack_id"])}
        scored_rows.append(merged)
        if scorecard["scoring_mode"] == "suggested":
            pending_rows.append(
                {
                    "outcome_id": outcome["id"],
                    "ts": outcome["ts"],
                    "query": outcome["query"],
                    "pack_id": outcome["pack_id"],
                    "pack_name": pack_name(outcome["pack_id"]),
                    "primary_skill": outcome["primary_skill"],
                    "status": outcome["status"],
                    "suggested": scorecard,
                }
            )

    manual_rows = [row for row in scored_rows if row["scoring_mode"] == "manual"]
    suggested_rows = [row for row in scored_rows if row["scoring_mode"] == "suggested"]

    def average(values: Sequence[float]) -> Optional[float]:
        if not values:
            return None
        return round(sum(values) / len(values), 3)

    verdict_counts: Dict[str, int] = defaultdict(int)
    pack_scores: Dict[str, List[float]] = defaultdict(list)
    path_scores: Dict[str, List[float]] = defaultdict(list)
    skill_scores: Dict[str, List[float]] = defaultdict(list)
    for row in scored_rows:
        verdict_counts[row["verdict"]] += 1
        pack_scores[row["pack_id"]].append(float(row["overall_score"]))
        for path in row["memory_paths"]:
            path_scores[path].append(float(row["overall_score"]))
        for skill in row["used_skills"]:
            skill_scores[skill].append(float(row["overall_score"]))

    def summarize_scores(mapping: Dict[str, List[float]], key_name: str) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for key, values in mapping.items():
            rows.append(
                {
                    key_name: key,
                    "avg_overall_score": round(sum(values) / len(values), 3),
                    "count": len(values),
                }
            )
        rows.sort(key=lambda item: (-item["avg_overall_score"], -item["count"], item[key_name]))
        return rows

    def learned_prior_dict(row, key_name: str) -> Dict[str, Any]:
        key, score, avg_overall_score, manual_count, suggested_count, exposure_count = row
        return {
            key_name: key,
            "score": round(float(score), 4),
            "avg_overall_score": round(float(avg_overall_score), 3),
            "manual_count": int(manual_count),
            "suggested_count": int(suggested_count),
            "exposure_count": int(exposure_count),
        }

    top_packs = [
        {**item, "pack_name": pack_name(item["pack_id"])}
        for item in summarize_scores(pack_scores, "pack_id")[:limit]
    ]
    weak_packs = [
        {**item, "pack_name": pack_name(item["pack_id"])}
        for item in sorted(
            summarize_scores(pack_scores, "pack_id"),
            key=lambda item: (item["avg_overall_score"], -item["count"], item["pack_id"]),
        )
        if item["avg_overall_score"] < 3.7
    ][:limit]

    scored_rows_sorted = sorted(scored_rows, key=lambda item: (item["ts"], item["outcome_id"]), reverse=True)
    pending_rows_sorted = sorted(pending_rows, key=lambda item: (item["ts"], item["outcome_id"]), reverse=True)

    return {
        "db": str(db_path),
        "packs_file": str(packs_path),
        "task_outcomes": len(outcomes),
        "scored_outcomes": len(scored_rows),
        "manual_scorecards": len(manual_rows),
        "suggested_scorecards": len(suggested_rows),
        "pending_manual_reviews": len(pending_rows),
        "last_result_training": None
        if not last_training_row
        else {
            "ts": last_training_row[0],
            "scored_outcomes": last_training_row[1],
            "manual_scorecards": last_training_row[2],
            "suggested_scorecards": last_training_row[3],
            "result_pack_priors": last_training_row[4],
            "result_path_priors": last_training_row[5],
            "result_skill_priors": last_training_row[6],
        },
        "avg_overall_manual": average([float(row["overall_score"]) for row in manual_rows]),
        "avg_overall_all": average([float(row["overall_score"]) for row in scored_rows]),
        "verdict_breakdown": [
            {"verdict": verdict, "count": count}
            for verdict, count in sorted(verdict_counts.items(), key=lambda item: (-item[1], item[0]))
        ],
        "latest_scored_outcome": None
        if not scored_rows_sorted
        else {
            "outcome_id": scored_rows_sorted[0]["outcome_id"],
            "ts": scored_rows_sorted[0]["ts"],
            "query": scored_rows_sorted[0]["query"],
            "pack_id": scored_rows_sorted[0]["pack_id"],
            "pack_name": scored_rows_sorted[0]["pack_name"],
            "primary_skill": scored_rows_sorted[0]["primary_skill"],
            "scoring_mode": scored_rows_sorted[0]["scoring_mode"],
            "overall_score": round(float(scored_rows_sorted[0]["overall_score"]), 3),
            "verdict": scored_rows_sorted[0]["verdict"],
        },
        "top_packs": top_packs,
        "weak_packs": weak_packs,
        "top_learned_packs": [
            {**learned_prior_dict(row, "pack_id"), "pack_name": pack_name(row[0])}
            for row in top_learned_pack_rows
        ],
        "weak_learned_packs": [
            {**learned_prior_dict(row, "pack_id"), "pack_name": pack_name(row[0])}
            for row in weak_learned_pack_rows
        ],
        "top_paths": summarize_scores(path_scores, "path")[:limit],
        "weak_paths": [
            item
            for item in sorted(
                summarize_scores(path_scores, "path"),
                key=lambda row: (row["avg_overall_score"], -row["count"], row["path"]),
            )
            if item["avg_overall_score"] < 3.7
        ][:limit],
        "top_learned_paths": [learned_prior_dict(row, "path") for row in top_learned_path_rows],
        "weak_learned_paths": [learned_prior_dict(row, "path") for row in weak_learned_path_rows],
        "top_skills": summarize_scores(skill_scores, "skill")[:limit],
        "weak_skills": [
            item
            for item in sorted(
                summarize_scores(skill_scores, "skill"),
                key=lambda row: (row["avg_overall_score"], -row["count"], row["skill"]),
            )
            if item["avg_overall_score"] < 3.7
        ][:limit],
        "top_learned_skills": [learned_prior_dict(row, "skill") for row in top_learned_skill_rows],
        "weak_learned_skills": [learned_prior_dict(row, "skill") for row in weak_learned_skill_rows],
        "pending_reviews": [
            {
                "outcome_id": row["outcome_id"],
                "ts": row["ts"],
                "query": row["query"],
                "pack_id": row["pack_id"],
                "pack_name": row["pack_name"],
                "primary_skill": row["primary_skill"],
                "status": row["status"],
                "suggested_overall_score": round(float(row["suggested"]["overall_score"]), 3),
                "suggested_verdict": row["suggested"]["verdict"],
            }
            for row in pending_rows_sorted[:limit]
        ],
        "recent_scorecards": [
            {
                "outcome_id": row["outcome_id"],
                "ts": row["ts"],
                "query": row["query"],
                "pack_id": row["pack_id"],
                "pack_name": row["pack_name"],
                "primary_skill": row["primary_skill"],
                "scoring_mode": row["scoring_mode"],
                "overall_score": round(float(row["overall_score"]), 3),
                "verdict": row["verdict"],
            }
            for row in scored_rows_sorted[:limit]
        ],
    }


def emit_event_in_connection(
    con: sqlite3.Connection,
    *,
    event_type: str,
    event_group: str = "",
    source: str = "squad_memory",
    status: str = "",
    query: str = "",
    role: Optional[str] = None,
    pack_id: Optional[str] = None,
    skill: Optional[str] = None,
    path: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> int:
    ensure_learning_tables(con)
    payload = json.dumps(metadata or {}, ensure_ascii=True)
    con.execute(
        """
        INSERT INTO events(
          event_type, event_group, source, status, query, role, pack_id, skill, path, metadata_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (event_type, event_group, source, status, query, role, pack_id, skill, path, payload),
    )
    event_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
    rebuild_episodes_in_connection(con)
    return event_id


def emit_event(
    db_path: Path,
    *,
    event_type: str,
    event_group: str = "",
    source: str = "squad_memory",
    status: str = "",
    query: str = "",
    role: Optional[str] = None,
    pack_id: Optional[str] = None,
    skill: Optional[str] = None,
    path: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> int:
    con = sqlite3.connect(str(db_path))
    try:
        event_id = emit_event_in_connection(
            con,
            event_type=event_type,
            event_group=event_group,
            source=source,
            status=status,
            query=query,
            role=role,
            pack_id=pack_id,
            skill=skill,
            path=path,
            metadata=metadata,
        )
        con.commit()
        return event_id
    finally:
        con.close()


def parse_event_timestamp(value: str) -> datetime:
    raw = (value or "").strip()
    if not raw:
        return datetime.utcnow()
    normalized = raw.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            parsed = datetime.strptime(raw, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return datetime.utcnow()
    if parsed.tzinfo is not None:
        return parsed.astimezone(tz=None).replace(tzinfo=None)
    return parsed


def episode_key_for_event(event: Dict[str, Any]) -> Tuple[str, str]:
    query = compact_whitespace(str(event.get("query") or ""))
    pack_id = compact_whitespace(str(event.get("pack_id") or ""))
    skill = compact_whitespace(str(event.get("skill") or ""))
    role = compact_whitespace(str(event.get("role") or ""))
    path = compact_whitespace(str(event.get("path") or ""))
    event_group = compact_whitespace(str(event.get("event_group") or ""))
    event_type = compact_whitespace(str(event.get("event_type") or ""))

    if query:
        return (f"query:{slugify(query)[:96]}", "task_session")
    if pack_id:
        return (f"pack:{pack_id}", "task_session")
    if skill and role:
        return (f"skill:{skill}:role:{role}", "skill_session")
    if skill:
        return (f"skill:{skill}", "skill_session")
    if path:
        return (f"path:{path}", "memory_path")
    bucket = slugify(event_group or event_type or "activity")
    return (f"group:{bucket}", event_group or "activity")


def episode_title_for_events(events: Sequence[Dict[str, Any]], episode_type: str) -> str:
    latest = events[-1]
    query = compact_whitespace(str(latest.get("query") or ""))
    if query:
        return truncate_text(query, 104)
    pack_id = compact_whitespace(str(latest.get("pack_id") or ""))
    if pack_id:
        return f"{title_from_slug(pack_id)} Session"
    skill = compact_whitespace(str(latest.get("skill") or ""))
    if skill:
        return f"{title_from_slug(skill)} Session"
    path = compact_whitespace(str(latest.get("path") or ""))
    if path:
        return title_from_slug(Path(path).stem)
    return f"{title_from_slug(episode_type)} Session"


def summarize_episode(events: Sequence[Dict[str, Any]], episode_type: str) -> Dict[str, Any]:
    latest = events[-1]
    skill_counts: Counter[str] = Counter(
        compact_whitespace(str(event.get("skill") or "")) for event in events if compact_whitespace(str(event.get("skill") or ""))
    )
    pack_counts: Counter[str] = Counter(
        compact_whitespace(str(event.get("pack_id") or "")) for event in events if compact_whitespace(str(event.get("pack_id") or ""))
    )
    role_counts: Counter[str] = Counter(
        compact_whitespace(str(event.get("role") or "")) for event in events if compact_whitespace(str(event.get("role") or ""))
    )
    status_counts: Counter[str] = Counter(
        compact_whitespace(str(event.get("status") or "")) for event in events if compact_whitespace(str(event.get("status") or ""))
    )
    group_counts: Counter[str] = Counter(
        compact_whitespace(str(event.get("event_group") or "")) or compact_whitespace(str(event.get("event_type") or ""))
        for event in events
    )
    path_counts: Counter[str] = Counter(
        compact_whitespace(str(event.get("path") or "")) for event in events if compact_whitespace(str(event.get("path") or ""))
    )
    query = next(
        (compact_whitespace(str(event.get("query") or "")) for event in reversed(events) if compact_whitespace(str(event.get("query") or ""))),
        "",
    )
    primary_skill = skill_counts.most_common(1)[0][0] if skill_counts else compact_whitespace(str(latest.get("skill") or ""))
    pack_id = pack_counts.most_common(1)[0][0] if pack_counts else compact_whitespace(str(latest.get("pack_id") or ""))
    role = role_counts.most_common(1)[0][0] if role_counts else compact_whitespace(str(latest.get("role") or ""))
    status = next(
        (compact_whitespace(str(event.get("status") or "")) for event in reversed(events) if compact_whitespace(str(event.get("status") or ""))),
        "",
    )
    title = episode_title_for_events(events, episode_type)
    event_labels = [label for label, _count in group_counts.most_common(3) if label]
    summary_parts = [f"{len(events)} events"]
    if event_labels:
        summary_parts.append(" -> ".join(event_labels))
    if primary_skill:
        summary_parts.append(f"lead {primary_skill}")
    if pack_id:
        summary_parts.append(f"pack {pack_id}")
    if status:
        summary_parts.append(f"latest {status}")
    summary_text = f"{title}: " + "; ".join(summary_parts)
    metadata = {
        "event_types": [label for label, _count in group_counts.most_common(6) if label],
        "skills": [label for label, _count in skill_counts.most_common(5) if label],
        "packs": [label for label, _count in pack_counts.most_common(3) if label],
        "roles": [label for label, _count in role_counts.most_common(3) if label],
        "statuses": [label for label, _count in status_counts.most_common(4) if label],
        "paths": [label for label, _count in path_counts.most_common(4) if label],
        "event_ids": [int(event["id"]) for event in events],
    }
    return {
        "title": title,
        "query": query,
        "primary_skill": primary_skill,
        "pack_id": pack_id,
        "role": role,
        "status": status,
        "summary_text": summary_text,
        "metadata": metadata,
    }


def rebuild_episodes_in_connection(con: sqlite3.Connection, gap_minutes: int = EPISODE_GAP_MINUTES) -> Dict[str, Any]:
    ensure_learning_tables(con)
    old_row_factory = con.row_factory
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            """
            SELECT id, ts, event_type, event_group, source, status, query, role, pack_id, skill, path, metadata_json
            FROM events
            ORDER BY id ASC
            """
        ).fetchall()
        episodes: List[Dict[str, Any]] = []
        latest_by_key: Dict[str, Dict[str, Any]] = {}
        gap = timedelta(minutes=max(5, gap_minutes))

        for row in rows:
            event = {
                "id": int(row["id"]),
                "ts": str(row["ts"] or ""),
                "event_type": str(row["event_type"] or ""),
                "event_group": str(row["event_group"] or ""),
                "source": str(row["source"] or ""),
                "status": str(row["status"] or ""),
                "query": str(row["query"] or ""),
                "role": str(row["role"] or ""),
                "pack_id": str(row["pack_id"] or ""),
                "skill": str(row["skill"] or ""),
                "path": str(row["path"] or ""),
            }
            event_dt = parse_event_timestamp(event["ts"])
            episode_key, episode_type = episode_key_for_event(event)
            current = latest_by_key.get(episode_key)
            if current and event_dt - current["last_dt"] <= gap:
                current["events"].append(event)
                current["last_dt"] = event_dt
                continue
            current = {
                "episode_key": episode_key,
                "episode_type": episode_type,
                "events": [event],
                "last_dt": event_dt,
            }
            episodes.append(current)
            latest_by_key[episode_key] = current

        con.execute("DELETE FROM episode_items")
        con.execute("DELETE FROM episode_summaries")
        con.execute("DELETE FROM episodes")

        inserted = 0
        for episode in episodes:
            summary = summarize_episode(episode["events"], episode["episode_type"])
            first_event = episode["events"][0]
            last_event = episode["events"][-1]
            metadata_json = json.dumps(summary["metadata"], ensure_ascii=True)
            con.execute(
                """
                INSERT INTO episodes(
                  ts_start, ts_end, episode_key, episode_type, title, status, role, pack_id,
                  primary_skill, query, event_count, summary_text, metadata_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    first_event["ts"],
                    last_event["ts"],
                    episode["episode_key"],
                    episode["episode_type"],
                    summary["title"],
                    summary["status"],
                    summary["role"] or None,
                    summary["pack_id"] or None,
                    summary["primary_skill"] or None,
                    summary["query"],
                    len(episode["events"]),
                    summary["summary_text"],
                    metadata_json,
                ),
            )
            episode_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
            for seq, event in enumerate(episode["events"], start=1):
                con.execute(
                    """
                    INSERT INTO episode_items(episode_id, event_id, seq, ts, event_type)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (episode_id, int(event["id"]), seq, event["ts"], event["event_type"]),
                )
            con.execute(
                """
                INSERT INTO episode_summaries(episode_id, ts, summary_kind, summary_text, metadata_json)
                VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?)
                """,
                (episode_id, EPISODE_SUMMARY_KIND, summary["summary_text"], metadata_json),
            )
            inserted += 1

        return {
            "episodes": inserted,
            "event_rows": len(rows),
            "gap_minutes": gap_minutes,
        }
    finally:
        con.row_factory = old_row_factory


def rebuild_episodes(db_path: Path, gap_minutes: int = EPISODE_GAP_MINUTES) -> Dict[str, Any]:
    con = sqlite3.connect(str(db_path))
    try:
        result = rebuild_episodes_in_connection(con, gap_minutes=gap_minutes)
        con.commit()
        return {"db": str(db_path), **result}
    finally:
        con.close()


def episode_report(db_path: Path, limit: int) -> Dict[str, Any]:
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        ensure_learning_tables(con)
        episode_count = int(con.execute("SELECT COUNT(*) FROM episodes").fetchone()[0])
        item_count = int(con.execute("SELECT COUNT(*) FROM episode_items").fetchone()[0])
        summary_count = int(con.execute("SELECT COUNT(*) FROM episode_summaries").fetchone()[0])
        type_rows = con.execute(
            """
            SELECT episode_type, COUNT(*) AS count
            FROM episodes
            GROUP BY episode_type
            ORDER BY count DESC, episode_type ASC
            """
        ).fetchall()
        recent_rows = con.execute(
            """
            SELECT id, ts_start, ts_end, episode_key, episode_type, title, status, role, pack_id,
                   primary_skill, query, event_count, summary_text, metadata_json
            FROM episodes
            ORDER BY ts_end DESC, id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        recent = []
        for row in recent_rows:
            try:
                metadata = json.loads(str(row["metadata_json"] or "{}"))
            except json.JSONDecodeError:
                metadata = {}
            recent.append(
                {
                    "id": int(row["id"]),
                    "ts_start": str(row["ts_start"] or ""),
                    "ts_end": str(row["ts_end"] or ""),
                    "episode_key": str(row["episode_key"] or ""),
                    "episode_type": str(row["episode_type"] or ""),
                    "title": str(row["title"] or ""),
                    "status": str(row["status"] or ""),
                    "role": str(row["role"] or ""),
                    "pack_id": str(row["pack_id"] or ""),
                    "primary_skill": str(row["primary_skill"] or ""),
                    "query": str(row["query"] or ""),
                    "event_count": int(row["event_count"] or 0),
                    "summary_text": str(row["summary_text"] or ""),
                    "metadata": metadata if isinstance(metadata, dict) else {},
                }
            )
    finally:
        con.close()

    return {
        "db": str(db_path),
        "episodes": episode_count,
        "episode_items": item_count,
        "episode_summaries": summary_count,
        "episode_types": [
            {"episode_type": str(row["episode_type"] or ""), "count": int(row["count"] or 0)}
            for row in type_rows
        ],
        "recent_episodes": recent,
    }


def workspace_context_snapshot(
    db_path: Path,
    query: str,
    role: Optional[str],
    top: int = 6,
    pack_id: Optional[str] = None,
) -> Dict[str, Any]:
    con = sqlite3.connect(str(db_path))
    try:
        snapshot = active_workspace_context(con, query, role, top=top, pack_id=pack_id)
        return {
            "active_contexts": snapshot["active_contexts"],
            "active_items": snapshot["active_items"],
            "context_ids": list(snapshot["context_ids"]),
            "contexts": [
                {
                    "id": int(item["id"]),
                    "name": item["name"],
                    "root_path": item["root_path"],
                    "role": item["role"],
                    "pack_id": item["pack_id"],
                    "ts_updated": item["ts_updated"],
                    "ts_last_used": item["ts_last_used"],
                }
                for item in snapshot["contexts"][:top]
            ],
            "hits": snapshot["hits"][:top],
        }
    finally:
        con.close()


def sync_workspace_context(
    db_path: Path,
    name: str,
    paths: Sequence[Path],
    *,
    role: Optional[str] = None,
    pack_id: Optional[str] = None,
    notes: str = "",
    max_files: int = WORKSPACE_MAX_FILES,
    max_chars: int = WORKSPACE_MAX_CHARS,
    replace: bool = False,
) -> Dict[str, Any]:
    normalized_paths = [Path(path).expanduser().resolve() for path in paths]
    scope_key = workspace_scope_key(name, normalized_paths, role, pack_id)
    root_path = common_root_path(normalized_paths)
    files = discover_workspace_files(normalized_paths, max_files=max_files)
    items = []
    for file_path in files:
        text = safe_read_workspace_text(file_path, max_chars=max_chars)
        if not text:
            continue
        rel_path = ""
        if root_path:
            try:
                rel_path = str(file_path.relative_to(root_path))
            except ValueError:
                rel_path = file_path.name
        item_title = workspace_item_title(file_path, text)
        item_metadata = {
            "suffix": file_path.suffix.lower(),
            "size_bytes": file_path.stat().st_size if file_path.exists() else 0,
            "mtime": datetime.utcfromtimestamp(file_path.stat().st_mtime).isoformat() if file_path.exists() else "",
        }
        items.append(
            {
                "path": str(file_path),
                "rel_path": rel_path or file_path.name,
                "item_type": "file",
                "title": item_title,
                "text": text,
                "token_count": len(tokenize(text)),
                "metadata": item_metadata,
            }
        )

    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        existing = con.execute(
            """
            SELECT id
            FROM workspace_contexts
            WHERE scope_key = ? AND status = 'active'
            ORDER BY id DESC
            LIMIT 1
            """,
            (scope_key,),
        ).fetchone()
        if existing and replace:
            context_id = int(existing[0])
            con.execute("DELETE FROM workspace_context_items WHERE context_id = ?", (context_id,))
            con.execute(
                """
                UPDATE workspace_contexts
                SET name = ?, role = ?, pack_id = ?, root_path = ?, notes = ?, ts_updated = CURRENT_TIMESTAMP, metadata_json = ?
                WHERE id = ?
                """,
                (
                    name,
                    role,
                    pack_id,
                    root_path,
                    notes,
                    json.dumps({"input_paths": [str(path) for path in normalized_paths]}, ensure_ascii=True),
                    context_id,
                ),
            )
        elif existing:
            context_id = int(existing[0])
            con.execute("DELETE FROM workspace_context_items WHERE context_id = ?", (context_id,))
            con.execute(
                """
                UPDATE workspace_contexts
                SET name = ?, role = ?, pack_id = ?, root_path = ?, notes = ?, ts_updated = CURRENT_TIMESTAMP, metadata_json = ?
                WHERE id = ?
                """,
                (
                    name,
                    role,
                    pack_id,
                    root_path,
                    notes,
                    json.dumps({"input_paths": [str(path) for path in normalized_paths]}, ensure_ascii=True),
                    context_id,
                ),
            )
        else:
            con.execute(
                """
                INSERT INTO workspace_contexts(name, scope_key, status, root_path, role, pack_id, notes, metadata_json)
                VALUES (?, ?, 'active', ?, ?, ?, ?, ?)
                """,
                (
                    name,
                    scope_key,
                    root_path,
                    role,
                    pack_id,
                    notes,
                    json.dumps({"input_paths": [str(path) for path in normalized_paths]}, ensure_ascii=True),
                ),
            )
            context_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        for item in items:
            con.execute(
                """
                INSERT INTO workspace_context_items(context_id, path, rel_path, item_type, title, text, token_count, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    context_id,
                    item["path"],
                    item["rel_path"],
                    item["item_type"],
                    item["title"],
                    item["text"],
                    item["token_count"],
                    json.dumps(item["metadata"], ensure_ascii=True),
                ),
            )
        emit_event_in_connection(
            con,
            event_type="workspace.synced",
            event_group="workspace",
            source="squad_memory",
            status="active",
            role=role,
            pack_id=pack_id,
            metadata={
                "context_id": context_id,
                "scope_key": scope_key,
                "root_path": root_path,
                "item_count": len(items),
                "paths": [str(path) for path in normalized_paths],
            },
        )
        con.commit()
    finally:
        con.close()

    return {
        "db": str(db_path),
        "context_id": context_id,
        "name": name,
        "scope_key": scope_key,
        "status": "active",
        "role": role,
        "pack_id": pack_id,
        "root_path": root_path,
        "item_count": len(items),
        "items": [
            {
                "path": item["path"],
                "rel_path": item["rel_path"],
                "title": item["title"],
                "token_count": item["token_count"],
            }
            for item in items[:10]
        ],
    }


def clear_workspace_context(
    db_path: Path,
    *,
    context_id: Optional[int] = None,
    name: Optional[str] = None,
    all_active: bool = False,
    delete: bool = False,
) -> Dict[str, Any]:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        where_parts = []
        params: List[Any] = []
        if all_active:
            where_parts.append("status = 'active'")
        if context_id is not None:
            where_parts.append("id = ?")
            params.append(context_id)
        if name:
            where_parts.append("LOWER(name) = ?")
            params.append(name.lower())
        if not where_parts:
            raise ValueError("Provide --context-id, --name, or --all-active")
        where_sql = " AND ".join(where_parts)
        rows = con.execute(
            f"""
            SELECT id, name, status
            FROM workspace_contexts
            WHERE {where_sql}
            ORDER BY id ASC
            """,
            tuple(params),
        ).fetchall()
        cleared = [{"id": int(row[0]), "name": str(row[1] or ""), "status": str(row[2] or "")} for row in rows]
        context_ids = [item["id"] for item in cleared]
        if context_ids:
            placeholders = ", ".join("?" for _ in context_ids)
            con.execute(f"DELETE FROM workspace_context_items WHERE context_id IN ({placeholders})", tuple(context_ids))
            if delete:
                con.execute(f"DELETE FROM workspace_contexts WHERE id IN ({placeholders})", tuple(context_ids))
                status = "deleted"
            else:
                con.execute(
                    f"""
                    UPDATE workspace_contexts
                    SET status = 'archived', ts_updated = CURRENT_TIMESTAMP
                    WHERE id IN ({placeholders})
                    """,
                    tuple(context_ids),
                )
                status = "archived"
            emit_event_in_connection(
                con,
                event_type="workspace.cleared",
                event_group="workspace",
                source="squad_memory",
                status=status,
                metadata={
                    "context_ids": context_ids,
                    "delete": bool(delete),
                    "count": len(context_ids),
                },
            )
        con.commit()
    finally:
        con.close()

    return {
        "db": str(db_path),
        "cleared": cleared,
        "delete": bool(delete),
        "count": len(cleared),
    }


def workspace_report(db_path: Path, limit: int) -> Dict[str, Any]:
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        ensure_learning_tables(con)
        active_contexts = int(con.execute("SELECT COUNT(*) FROM workspace_contexts WHERE status = 'active'").fetchone()[0])
        archived_contexts = int(con.execute("SELECT COUNT(*) FROM workspace_contexts WHERE status = 'archived'").fetchone()[0])
        active_items = int(
            con.execute(
                """
                SELECT COUNT(*)
                FROM workspace_context_items wci
                JOIN workspace_contexts wc ON wc.id = wci.context_id
                WHERE wc.status = 'active'
                """
            ).fetchone()[0]
        )
        rows = con.execute(
            """
            SELECT
              wc.id,
              wc.ts_created,
              wc.ts_updated,
              wc.ts_last_used,
              wc.name,
              wc.scope_key,
              wc.status,
              wc.root_path,
              wc.role,
              wc.pack_id,
              wc.notes,
              COUNT(wci.id) AS item_count
            FROM workspace_contexts wc
            LEFT JOIN workspace_context_items wci ON wci.context_id = wc.id
            GROUP BY wc.id
            ORDER BY CASE WHEN wc.status = 'active' THEN 0 ELSE 1 END, wc.ts_updated DESC, wc.id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        contexts = []
        for row in rows:
            top_items = con.execute(
                """
                SELECT path, rel_path, title, token_count
                FROM workspace_context_items
                WHERE context_id = ?
                ORDER BY token_count DESC, id ASC
                LIMIT 5
                """,
                (int(row["id"]),),
            ).fetchall()
            contexts.append(
                {
                    "id": int(row["id"]),
                    "ts_created": str(row["ts_created"] or ""),
                    "ts_updated": str(row["ts_updated"] or ""),
                    "ts_last_used": str(row["ts_last_used"] or ""),
                    "name": str(row["name"] or ""),
                    "scope_key": str(row["scope_key"] or ""),
                    "status": str(row["status"] or ""),
                    "root_path": str(row["root_path"] or ""),
                    "role": str(row["role"] or ""),
                    "pack_id": str(row["pack_id"] or ""),
                    "notes": str(row["notes"] or ""),
                    "item_count": int(row["item_count"] or 0),
                    "top_items": [
                        {
                            "path": str(item["path"] or ""),
                            "rel_path": str(item["rel_path"] or ""),
                            "title": str(item["title"] or ""),
                            "token_count": int(item["token_count"] or 0),
                        }
                        for item in top_items
                    ],
                }
            )
    finally:
        con.close()

    return {
        "db": str(db_path),
        "active_contexts": active_contexts,
        "archived_contexts": archived_contexts,
        "active_items": active_items,
        "contexts": contexts,
    }


def log_query(db_path: Path, mode: str, query: str, role: Optional[str], skill_filter: Optional[str], top_n: int, result: dict) -> None:
    con = sqlite3.connect(str(db_path))
    try:
        con.execute(
            "INSERT INTO query_log(mode, query, role, skill_filter, top_n, result_json) VALUES (?, ?, ?, ?, ?, ?)",
            (mode, query, role, skill_filter, top_n, json.dumps(result)),
        )
        recommended = result.get("recommended_skills", []) if isinstance(result, dict) else []
        primary_skill = ""
        pack_id = ""
        if recommended and isinstance(recommended, list):
            primary_skill = str((recommended[0] or {}).get("skill", ""))
        elif isinstance(result, dict) and result.get("primary_skill"):
            primary_skill = str(result.get("primary_skill") or "")
        if isinstance(result, dict) and isinstance(result.get("selected_pack"), dict):
            pack_id = str(result["selected_pack"].get("id") or "")
        workspace_context = result.get("workspace_context", {}) if isinstance(result, dict) else {}
        workspace_context_ids = list(workspace_context.get("context_ids", [])) if isinstance(workspace_context, dict) else []
        touch_workspace_contexts_in_connection(con, workspace_context_ids)
        emit_event_in_connection(
            con,
            event_type=f"query.{mode}",
            event_group="query",
            source="squad_memory",
            status="ok",
            query=query,
            role=role,
            pack_id=pack_id or None,
            skill=primary_skill or None,
            path=skill_filter,
            metadata={
                "mode": mode,
                "top_n": top_n,
                "skill_filter": skill_filter or "",
                "inferred_intents": list(result.get("inferred_intents", [])) if isinstance(result, dict) else [],
                "expansion_terms": list(result.get("expansion_terms", []))[:8] if isinstance(result, dict) else [],
                "workspace_context_ids": workspace_context_ids[:8],
                "workspace_hits": len(workspace_context.get("hits", [])) if isinstance(workspace_context, dict) else 0,
            },
        )
        con.commit()
    finally:
        con.close()


def add_feedback(db_path: Path, query: str, path: str, rating: str) -> None:
    con = sqlite3.connect(str(db_path))
    try:
        con.execute(
            "INSERT INTO feedback(query, path, rating) VALUES (?, ?, ?)",
            (query, path, rating),
        )
        emit_event_in_connection(
            con,
            event_type="feedback.recorded",
            event_group="feedback",
            source="squad_memory",
            status=rating,
            query=query,
            path=path,
            metadata={"rating": rating},
        )
        con.commit()
    finally:
        con.close()


def recent_logs(db_path: Path, limit: int) -> List[dict]:
    con = sqlite3.connect(str(db_path))
    rows = con.execute(
        "SELECT ts, mode, query, role, skill_filter, top_n FROM query_log ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    con.close()
    return [
        {
            "ts": ts,
            "mode": mode,
            "query": query,
            "role": role,
            "skill_filter": skill_filter,
            "top_n": top_n,
        }
        for ts, mode, query, role, skill_filter, top_n in rows
    ]


def query_role_lookup(con: sqlite3.Connection) -> Dict[str, Counter]:
    rows = con.execute("SELECT query, role FROM query_log WHERE role IS NOT NULL AND role != ''").fetchall()
    lookup: Dict[str, Counter] = defaultdict(Counter)
    for query, role in rows:
        lookup[query][role] += 1
    return lookup


def read_current_meta(rel_path: str) -> Dict[str, str]:
    path = SKILLS_ROOT / rel_path
    if not path.exists():
        return {}
    meta, _body = parse_frontmatter(path.read_text(encoding="utf-8"))
    return meta


def suggested_confidence(score: float, useful_count: int, not_useful_count: int) -> str:
    if useful_count >= 3 and score >= 0.45 and useful_count >= not_useful_count:
        return "high"
    if useful_count >= 1 and score >= 0.12:
        return "medium"
    return "low"


def confidence_rank(value: str) -> int:
    return {"": 0, "low": 1, "medium": 2, "high": 3}.get(value, 0)


def candidate_terms_for_queries(queries: Sequence[str]) -> List[str]:
    counts: Counter = Counter()
    for query in queries:
        _expanded, _intents, expansions = expand_query(query)
        if expansions:
            counts.update(
                term
                for term in expansions
                if term not in SUGGESTION_STOPWORDS and ("_" in term or len(term) >= 6)
            )
        else:
            counts.update(
                token
                for token in tokenize(query)
                if token not in SUGGESTION_STOPWORDS and len(token) > 2
            )
    return [term for term, _count in counts.most_common(8)]


def usage_report(db_path: Path, limit: int) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        query_log_count = con.execute("SELECT COUNT(*) FROM query_log").fetchone()[0]
        feedback_count = con.execute("SELECT COUNT(*) FROM feedback").fetchone()[0]
        last_training_row = con.execute(
            """
            SELECT ts, query_logs, feedback_rows, path_priors, skill_priors
            FROM training_runs
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()
        top_paths = [
            {
                "path": path,
                "score": round(score, 4),
                "useful_count": useful_count,
                "not_useful_count": not_useful_count,
                "exposure_count": exposure_count,
            }
            for path, score, useful_count, not_useful_count, exposure_count in con.execute(
                """
                SELECT path, score, useful_count, not_useful_count, exposure_count
                FROM learned_path_priors
                WHERE bucket = ? AND score > 0
                ORDER BY score DESC, useful_count DESC
                LIMIT ?
                """,
                (GLOBAL_BUCKET, limit),
            ).fetchall()
        ]
        weak_paths = [
            {
                "path": path,
                "score": round(score, 4),
                "useful_count": useful_count,
                "not_useful_count": not_useful_count,
                "exposure_count": exposure_count,
            }
            for path, score, useful_count, not_useful_count, exposure_count in con.execute(
                """
                SELECT path, score, useful_count, not_useful_count, exposure_count
                FROM learned_path_priors
                WHERE bucket = ? AND exposure_count >= 2 AND (score < 0 OR not_useful_count > 0)
                ORDER BY score ASC, exposure_count DESC
                LIMIT ?
                """,
                (GLOBAL_BUCKET, limit),
            ).fetchall()
        ]
        top_skills = [
            {
                "skill": skill,
                "score": round(score, 4),
                "useful_count": useful_count,
                "not_useful_count": not_useful_count,
                "exposure_count": exposure_count,
            }
            for skill, score, useful_count, not_useful_count, exposure_count in con.execute(
                """
                SELECT skill, score, useful_count, not_useful_count, exposure_count
                FROM learned_skill_priors
                WHERE bucket = ? AND score > 0
                ORDER BY score DESC, useful_count DESC
                LIMIT ?
                """,
                (GLOBAL_BUCKET, limit),
            ).fetchall()
        ]
        bucket_rows = con.execute(
            """
            SELECT bucket, path, score
            FROM learned_path_priors
            WHERE bucket != ? AND score > 0
            ORDER BY bucket ASC, score DESC
            """,
            (GLOBAL_BUCKET,),
        ).fetchall()
        seen_buckets = set()
        top_buckets = []
        for bucket, path, score in bucket_rows:
            if bucket in seen_buckets:
                continue
            seen_buckets.add(bucket)
            top_buckets.append({"bucket": bucket, "top_path": path, "score": round(score, 4)})
            if len(top_buckets) >= limit:
                break
    finally:
        con.close()

    return {
        "db": str(db_path),
        "query_logs": query_log_count,
        "feedback_rows": feedback_count,
        "last_training": (
            None
            if not last_training_row
            else {
                "ts": last_training_row[0],
                "query_logs": last_training_row[1],
                "feedback_rows": last_training_row[2],
                "path_priors": last_training_row[3],
                "skill_priors": last_training_row[4],
            }
        ),
        "top_paths": top_paths,
        "weak_paths": weak_paths,
        "top_skills": top_skills,
        "top_buckets": top_buckets,
    }


def suggest_metadata(db_path: Path, limit: int, path_filter: Optional[str], min_useful: int) -> dict:
    con = sqlite3.connect(str(db_path))
    try:
        ensure_learning_tables(con)
        query_roles = query_role_lookup(con)
        if path_filter:
            candidate_rows = con.execute(
                """
                SELECT path, score, useful_count, not_useful_count, exposure_count
                FROM learned_path_priors
                WHERE bucket = ? AND path = ?
                """,
                (GLOBAL_BUCKET, path_filter),
            ).fetchall()
        else:
            candidate_rows = con.execute(
                """
                SELECT path, score, useful_count, not_useful_count, exposure_count
                FROM learned_path_priors
                WHERE bucket = ? AND useful_count >= ?
                ORDER BY score DESC, useful_count DESC
                LIMIT ?
                """,
                (GLOBAL_BUCKET, min_useful, limit),
            ).fetchall()

        suggestions = []
        for path, score, useful_count, not_useful_count, exposure_count in candidate_rows:
            meta = read_current_meta(path)
            current_intents = parse_meta_list(meta, "intent", "intents")
            current_roles = parse_meta_list(meta, "role", "roles")
            current_use_for = parse_meta_list(meta, "use_for")
            current_topics = parse_meta_list(meta, "topic", "topics")
            current_avoid = parse_meta_list(meta, "avoid_for")
            current_confidence = meta.get("confidence", "").strip().lower()
            current_canonical = parse_meta_bool(meta, "canonical")
            current_canonical_group = meta.get("canonical_group", "").strip()
            feedback_rows = con.execute(
                "SELECT query, rating FROM feedback WHERE path = ? ORDER BY id DESC",
                (path,),
            ).fetchall()
            useful_queries = [query for query, rating in feedback_rows if rating == "useful"]
            intent_counts: Counter = Counter()
            role_counts: Counter = Counter()
            for query in useful_queries:
                _expanded, inferred_intents, _expansions = expand_query(query)
                intent_counts.update(inferred_intents)
                role_counts.update(query_roles.get(query, Counter()))
            suggested_intents = [
                intent
                for intent, _count in intent_counts.most_common(4)
                if intent not in current_intents
            ]
            suggested_roles = [
                role
                for role, _count in role_counts.most_common(4)
                if role not in current_roles
            ]
            suggested_use_for = [
                term
                for term in candidate_terms_for_queries(useful_queries)
                if term not in (current_use_for + current_intents + current_topics)
            ][:5]
            if current_use_for:
                suggested_use_for = [term for term in suggested_use_for if "_" in term]
            topic_suggestion = current_topics[0] if current_topics else (suggested_intents[0] if suggested_intents else "")
            confidence_value = max(
                [current_confidence, suggested_confidence(float(score), useful_count, not_useful_count)],
                key=confidence_rank,
            )
            should_be_canonical = useful_count >= max(min_useful + 1, 3) and float(score) >= 0.35
            if not (
                (topic_suggestion and not current_topics)
                or suggested_intents
                or suggested_roles
                or suggested_use_for
                or confidence_rank(confidence_value) > confidence_rank(current_confidence)
                or (should_be_canonical and not current_canonical)
            ):
                continue
            suggestions.append(
                {
                    "path": path,
                    "training_signal": {
                        "score": round(float(score), 4),
                        "useful_count": useful_count,
                        "not_useful_count": not_useful_count,
                        "exposure_count": exposure_count,
                    },
                    "current_meta": {
                        "topic": meta.get("topic", ""),
                        "intent": current_intents,
                        "role": current_roles,
                        "use_for": current_use_for,
                        "avoid_for": current_avoid,
                        "confidence": current_confidence,
                        "canonical": current_canonical,
                        "canonical_group": current_canonical_group,
                    },
                    "suggested_meta": {
                        "topic": topic_suggestion,
                        "intent": suggested_intents,
                        "role": suggested_roles,
                        "use_for": suggested_use_for,
                        "confidence": confidence_value,
                        "canonical": current_canonical or should_be_canonical,
                        "canonical_group": current_canonical_group or topic_suggestion.replace("_", " "),
                    },
                }
            )
    finally:
        con.close()

    return {
        "db": str(db_path),
        "path_filter": path_filter,
        "min_useful": min_useful,
        "suggestions": suggestions,
    }


def evaluate_fixtures(db_path: Path, fixtures_path: Path) -> dict:
    fixtures = json.loads(fixtures_path.read_text(encoding="utf-8"))
    cases = fixtures["cases"]
    results = []
    primary_hits = 0
    skill_hits = 0
    path_hits = 0

    for case in cases:
        query = case["query"]
        role = case.get("role")
        expected_primary = case.get("expected_primary_skill")
        expected_skills = set(case.get("expected_skills", []))
        expected_paths = set(case.get("expected_paths", []))

        decision = decide(db_path, query, role=role, top=5, workspace_enabled=False)
        ranked_skills = [item["skill"] for item in decision["recommended_skills"]]
        memory_paths = [item["path"] for item in decision["supporting_memory"]]

        primary_ok = expected_primary == ranked_skills[0] if expected_primary and ranked_skills else False
        skill_ok = bool(expected_skills & set(ranked_skills[:3])) if expected_skills else True
        path_ok = bool(expected_paths & set(memory_paths[:5])) if expected_paths else True

        primary_hits += 1 if primary_ok else 0
        skill_hits += 1 if skill_ok else 0
        path_hits += 1 if path_ok else 0

        results.append(
            {
                "query": query,
                "role": role,
                "expected_primary_skill": expected_primary,
                "recommended_skills": ranked_skills[:5],
                "top_memory_paths": memory_paths[:5],
                "primary_hit": primary_ok,
                "skill_hit": skill_ok,
                "path_hit": path_ok,
                "inferred_intents": decision.get("inferred_intents", []),
            }
        )

    total = len(cases) or 1
    return {
        "fixture_path": str(fixtures_path),
        "total_cases": len(cases),
        "primary_skill_accuracy": round(primary_hits / total, 4),
        "top3_skill_hit_rate": round(skill_hits / total, 4),
        "top5_path_hit_rate": round(path_hits / total, 4),
        "results": results,
    }


def normalize_task_eval_value(value: Any) -> str:
    text = re.sub(r"[^a-z0-9]+", " ", str(value or "").lower())
    return compact_whitespace(text)


def normalize_task_eval_values(values: Sequence[Any]) -> List[str]:
    normalized: List[str] = []
    for value in values:
        item = normalize_task_eval_value(value)
        if item:
            normalized.append(item)
    return normalized


def evaluate_task_fixtures(db_path: Path, packs_path: Path, fixtures_path: Path, top: int = 5) -> dict:
    fixtures = json.loads(fixtures_path.read_text(encoding="utf-8"))
    cases = fixtures["cases"]
    results = []
    pack_hits = 0
    primary_hits = 0
    supporting_hits = 0
    path_hits = 0
    theme_hits = 0
    section_hits = 0
    deliverable_hits = 0
    pass_hits = 0

    for case in cases:
        query = case["query"]
        role = case.get("role")
        plan = build_execute_plan(
            db_path,
            packs_path,
            query,
            role,
            top,
            pack_id=case.get("pack_id"),
            workspace_enabled=False,
        )
        selected_pack = plan["selected_pack"]
        actual_supporting = set(plan.get("supporting_skills", []))
        actual_paths = [item["path"] for item in plan.get("memory_shortlist", [])]
        actual_themes = set(normalize_task_eval_values(plan.get("memory_themes", [])))
        actual_sections = set(normalize_task_eval_values(plan.get("output_sections", [])))
        actual_deliverables = set(normalize_task_eval_values(plan.get("deliverables", [])))

        expected_pack = str(case.get("expected_pack_id", "") or "")
        expected_primary = str(case.get("expected_primary_skill", "") or "")
        expected_supporting = set(case.get("expected_supporting_skills", []))
        expected_paths = set(case.get("expected_memory_paths", []))
        expected_themes = set(normalize_task_eval_values(case.get("expected_memory_themes", [])))
        expected_sections = set(normalize_task_eval_values(case.get("expected_output_sections", [])))
        expected_deliverables = set(normalize_task_eval_values(case.get("expected_deliverables", [])))

        pack_ok = selected_pack["id"] == expected_pack if expected_pack else True
        primary_ok = plan.get("primary_skill") == expected_primary if expected_primary else True
        supporting_ok = expected_supporting.issubset(actual_supporting) if expected_supporting else True
        path_ok = bool(expected_paths & set(actual_paths[: max(top * 2, 8)])) if expected_paths else True
        theme_ok = bool(expected_themes & actual_themes) if expected_themes else True
        section_ok = expected_sections.issubset(actual_sections) if expected_sections else True
        deliverable_ok = expected_deliverables.issubset(actual_deliverables) if expected_deliverables else True

        failed_checks = []
        if not pack_ok:
            failed_checks.append("pack")
        if not primary_ok:
            failed_checks.append("primary_skill")
        if not supporting_ok:
            failed_checks.append("supporting_skills")
        if not path_ok:
            failed_checks.append("memory_paths")
        if not theme_ok:
            failed_checks.append("memory_themes")
        if not section_ok:
            failed_checks.append("output_sections")
        if not deliverable_ok:
            failed_checks.append("deliverables")
        case_pass = not failed_checks

        pack_hits += 1 if pack_ok else 0
        primary_hits += 1 if primary_ok else 0
        supporting_hits += 1 if supporting_ok else 0
        path_hits += 1 if path_ok else 0
        theme_hits += 1 if theme_ok else 0
        section_hits += 1 if section_ok else 0
        deliverable_hits += 1 if deliverable_ok else 0
        pass_hits += 1 if case_pass else 0

        results.append(
            {
                "query": query,
                "role": role,
                "expected_pack_id": expected_pack,
                "selected_pack_id": selected_pack["id"],
                "selected_pack_name": selected_pack["name"],
                "expected_primary_skill": expected_primary,
                "primary_skill": plan.get("primary_skill"),
                "expected_supporting_skills": sorted(expected_supporting),
                "supporting_skills": plan.get("supporting_skills", []),
                "expected_memory_paths": sorted(expected_paths),
                "top_memory_paths": actual_paths[: max(top * 2, 8)],
                "expected_memory_themes": sorted(expected_themes),
                "memory_themes": plan.get("memory_themes", []),
                "expected_output_sections": sorted(expected_sections),
                "output_sections": plan.get("output_sections", []),
                "expected_deliverables": sorted(expected_deliverables),
                "deliverables": plan.get("deliverables", []),
                "pack_hit": pack_ok,
                "primary_hit": primary_ok,
                "supporting_skill_hit": supporting_ok,
                "memory_path_hit": path_ok,
                "memory_theme_hit": theme_ok,
                "output_section_hit": section_ok,
                "deliverable_hit": deliverable_ok,
                "pass": case_pass,
                "failed_checks": failed_checks,
                "workspace_contexts": int((plan.get("workspace_context") or {}).get("active_contexts", 0) or 0),
            }
        )

    total = len(cases) or 1
    weak_cases = [item for item in results if not item["pass"]]
    return {
        "db": str(db_path),
        "packs_file": str(packs_path),
        "fixture_path": str(fixtures_path),
        "workspace_ignored": True,
        "total_cases": len(cases),
        "pack_accuracy": round(pack_hits / total, 4),
        "primary_skill_accuracy": round(primary_hits / total, 4),
        "supporting_skill_match_rate": round(supporting_hits / total, 4),
        "memory_path_hit_rate": round(path_hits / total, 4),
        "memory_theme_hit_rate": round(theme_hits / total, 4),
        "output_section_hit_rate": round(section_hits / total, 4),
        "deliverable_hit_rate": round(deliverable_hits / total, 4),
        "pass_rate": round(pass_hits / total, 4),
        "results": results,
        "weak_cases": weak_cases,
    }


def apply_variant_preferences(ranked_skills: List[dict], inferred_intents: List[str]) -> List[dict]:
    adjusted = list(ranked_skills)
    for intent in inferred_intents:
        for generic, specialist in INTENT_VARIANT_PREFERENCES.get(intent, []):
            generic_index = next((i for i, item in enumerate(adjusted) if item["skill"] == generic), None)
            specialist_index = next((i for i, item in enumerate(adjusted) if item["skill"] == specialist), None)
            if generic_index is None or specialist_index is None:
                continue
            if generic_index > specialist_index:
                continue
            generic_score = adjusted[generic_index]["score"]
            specialist_score = adjusted[specialist_index]["score"]
            if specialist_score + 1.0 >= generic_score:
                adjusted[generic_index], adjusted[specialist_index] = adjusted[specialist_index], adjusted[generic_index]
    return adjusted


def print_query_results(results: Sequence[dict]) -> None:
    for index, item in enumerate(results, start=1):
        print(f"{index}. [{item['score']:.4f}] {item['path']} :: {item['heading']}")
        print(
            f"   skill={item['skill']} type={item['file_type']} section={item['section_kind']} "
            f"source={item['source'] or '-'} lexical={item['lexical']} semantic={item['semantic']} vector={item['vector_semantic']}"
        )
        if item["canonical_group"]:
            print(f"   canonical={item['canonical_group']}")
        if item["topics"] or item["intents"] or item["confidence"]:
            print(
                f"   topics={', '.join(item['topics']) or '-'} "
                f"intents={', '.join(item['intents']) or '-'} "
                f"confidence={item['confidence'] or '-'}"
            )
        if item["published_on"]:
            print(f"   published_on={item['published_on']}")
        if item["bundles"]:
            print(f"   bundles={', '.join(item['bundles'])}")
        if item.get("workspace_boost"):
            print(f"   workspace_boost={item['workspace_boost']:.4f} overlap={item.get('workspace_overlap', 0)}")
        print(f"   {item['snippet']}")


def print_workspace_context(workspace_context: dict) -> None:
    if not workspace_context or not workspace_context.get("active_contexts"):
        print("\nWorkspace context: (none)")
        return
    print(
        "\nWorkspace context: "
        f"contexts={workspace_context.get('active_contexts', 0)} "
        f"items={workspace_context.get('active_items', 0)}"
    )
    contexts = workspace_context.get("contexts", [])
    if contexts:
        print("Active contexts:")
        for item in contexts[:5]:
            scope = []
            if item.get("role"):
                scope.append(f"role={item['role']}")
            if item.get("pack_id"):
                scope.append(f"pack={item['pack_id']}")
            print(f"- #{item['id']} {item['name']} ({', '.join(scope) if scope else 'global'})")
            if item.get("root_path"):
                print(f"  root={item['root_path']}")
    hits = workspace_context.get("hits", [])
    if hits:
        print("Relevant workspace files:")
        for item in hits[:6]:
            print(
                f"- [{item['score']:.4f}] {item['rel_path'] or item['path']} :: {item['title']}"
            )
            if item.get("snippet"):
                print(f"  {item['snippet']}")


def print_decision(result: dict) -> None:
    print(f"Query: {result['query']}")
    if result["role"]:
        print(f"Role: {result['role']}")
    print_workspace_context(result.get("workspace_context", {}))
    print("\nRecommended skills:")
    for index, item in enumerate(result["recommended_skills"], start=1):
        print(f"{index}. {item['skill']} [{item['score']:.4f}]")
        print(f"   paths: {', '.join(item['supporting_paths'])}")
        print(f"   headings: {', '.join(item['headings'])}")
    print("\nSupporting memory:")
    print_query_results(result["supporting_memory"])


def print_pinchy_plan(result: dict) -> None:
    print(f"Query: {result['query']}")
    print(f"Role: {result['role']}")
    print_workspace_context(result.get("workspace_context", {}))
    print(f"Primary skill: {result['primary_skill']}")
    print(f"Supporting skills: {', '.join(result['supporting_skills']) if result['supporting_skills'] else '(none)'}")
    if result["memory_themes"]:
        print(f"Memory themes: {', '.join(result['memory_themes'])}")
    print("\nPlan:")
    for idx, step in enumerate(result["plan_steps"], start=1):
        print(f"{idx}. {step}")
    print("\nMemory shortlist:")
    print_query_results(result["memory_shortlist"])


def print_task_pack(result: dict) -> None:
    pack = result["selected_pack"]
    print(f"Query: {result['query']}")
    if result["role"]:
        print(f"Role: {result['role']}")
    print(f"Selected pack: {pack['id']} ({pack['name']}) [{pack['score']:.4f}]")
    print(f"Primary skill: {pack['primary_skill']}")
    print(f"Supporting skills: {', '.join(pack['supporting_skills']) if pack['supporting_skills'] else '(none)'}")
    print_workspace_context(result.get("workspace_context", {}))
    if pack["description"]:
        print(f"\nDescription: {pack['description']}")
    if pack["reasons"]:
        print("\nWhy this pack:")
        for reason in pack["reasons"]:
            print(f"- {reason}")
    if result["runner_up_packs"]:
        print("\nRunner-ups:")
        for item in result["runner_up_packs"]:
            print(f"- {item['id']} ({item['score']:.4f})")
    if result["memory_themes"]:
        print(f"\nMemory themes: {', '.join(result['memory_themes'])}")
    print("\nMemory shortlist:")
    print_query_results(result["memory_shortlist"])


def print_execute_plan(result: dict) -> None:
    pack = result["selected_pack"]
    print(f"Query: {result['query']}")
    if result["role"]:
        print(f"Role: {result['role']}")
    print(f"Execution pack: {pack['id']} ({pack['name']})")
    print(f"Primary skill: {result['primary_skill']}")
    print(f"Supporting skills: {', '.join(result['supporting_skills']) if result['supporting_skills'] else '(none)'}")
    print_workspace_context(result.get("workspace_context", {}))
    if result["memory_themes"]:
        print(f"Memory themes: {', '.join(result['memory_themes'])}")
    print("\nExecution steps:")
    for idx, step in enumerate(result["execution_steps"], start=1):
        print(f"{idx}. {step}")
    if result["deliverables"]:
        print("\nDeliverables:")
        for item in result["deliverables"]:
            print(f"- {item}")
    if result["output_sections"]:
        print("\nOutput sections:")
        for item in result["output_sections"]:
            print(f"- {item}")
    if result["handoff_plan"]:
        print("\nHandoff plan:")
        for item in result["handoff_plan"]:
            print(f"- {item}")
    if result["escalation_rules"]:
        print("\nEscalation rules:")
        for item in result["escalation_rules"]:
            print(f"- {item}")
    print("\nMemory shortlist:")
    print_query_results(result["memory_shortlist"])


def print_completed_task(result: dict) -> None:
    print(f"Outcome ID: {result['outcome_id']}")
    print(f"Query: {result['query']}")
    if result["role"]:
        print(f"Role: {result['role']}")
    print(f"Status: {result['status']}")
    print(f"Pack: {result['selected_pack']['id']} ({result['selected_pack']['name']})")
    print(f"Primary skill: {result['primary_skill']}")
    print(f"Supporting skills: {', '.join(result['supporting_skills']) if result['supporting_skills'] else '(none)'}")
    print(f"Used skills: {', '.join(result['used_skills']) if result['used_skills'] else '(none)'}")
    if result["used_paths"]:
        print("Used paths:")
        for path in result["used_paths"]:
            print(f"- {path}")
    if result["completion_minutes"] is not None:
        print(f"Completion minutes: {result['completion_minutes']}")
    if result["user_rating"] is not None:
        print(f"User rating: {result['user_rating']}")
    if result["notes"]:
        print(f"Notes: {result['notes']}")


def print_train_summary(result: dict) -> None:
    print(f"DB: {result['db']}")
    if "query_logs" in result:
        print(f"Query logs: {result['query_logs']}")
    if "feedback_rows" in result:
        print(f"Feedback rows: {result['feedback_rows']}")
    if "path_priors" in result:
        print(f"Path priors: {result['path_priors']}")
    if "skill_priors" in result:
        print(f"Skill priors: {result['skill_priors']}")
    if "task_outcomes" in result:
        print(f"Task outcomes: {result['task_outcomes']}")
    if "pack_priors" in result:
        print(f"Pack priors: {result['pack_priors']}")
    if "pack_path_priors" in result:
        print(f"Pack path priors: {result['pack_path_priors']}")
    if "pack_skill_priors" in result:
        print(f"Pack skill priors: {result['pack_skill_priors']}")
    if "outcome_path_priors" in result:
        print(f"Outcome path priors: {result['outcome_path_priors']}")
    if "outcome_skill_priors" in result:
        print(f"Outcome skill priors: {result['outcome_skill_priors']}")
    if "scored_outcomes" in result:
        print(f"Scored outcomes: {result['scored_outcomes']}")
    if "manual_scorecards" in result:
        print(f"Manual scorecards: {result['manual_scorecards']}")
    if "suggested_scorecards" in result:
        print(f"Suggested scorecards: {result['suggested_scorecards']}")
    if "result_pack_priors" in result:
        print(f"Result pack priors: {result['result_pack_priors']}")
    if "result_path_priors" in result:
        print(f"Result path priors: {result['result_path_priors']}")
    if "result_skill_priors" in result:
        print(f"Result skill priors: {result['result_skill_priors']}")
    if "episodes" in result:
        print(f"Episodes: {result['episodes']}")
    if "event_rows" in result:
        print(f"Event rows: {result['event_rows']}")


def print_usage_report(result: dict) -> None:
    print(f"DB: {result['db']}")
    print(f"Query logs: {result['query_logs']}")
    print(f"Feedback rows: {result['feedback_rows']}")
    if result["last_training"]:
        print(
            "Last training: "
            f"{result['last_training']['ts']} "
            f"(logs={result['last_training']['query_logs']}, feedback={result['last_training']['feedback_rows']}, "
            f"path_priors={result['last_training']['path_priors']}, skill_priors={result['last_training']['skill_priors']})"
        )
    print("\nTop paths:")
    for item in result["top_paths"]:
        print(
            f"- {item['path']} score={item['score']:.4f} "
            f"useful={item['useful_count']} not_useful={item['not_useful_count']} exposure={item['exposure_count']}"
        )
    print("\nWeak paths:")
    for item in result["weak_paths"]:
        print(
            f"- {item['path']} score={item['score']:.4f} "
            f"useful={item['useful_count']} not_useful={item['not_useful_count']} exposure={item['exposure_count']}"
        )
    print("\nTop skills:")
    for item in result["top_skills"]:
        print(
            f"- {item['skill']} score={item['score']:.4f} "
            f"useful={item['useful_count']} not_useful={item['not_useful_count']} exposure={item['exposure_count']}"
        )


def print_pack_report(result: dict) -> None:
    print(f"DB: {result['db']}")
    print(f"Task outcomes: {result['task_outcomes']}")
    if result["last_pack_training"]:
        print(
            "Last pack training: "
            f"{result['last_pack_training']['ts']} "
            f"(outcomes={result['last_pack_training']['task_outcomes']}, "
            f"pack_priors={result['last_pack_training']['pack_priors']}, "
            f"pack_path_priors={result['last_pack_training']['pack_path_priors']}, "
            f"pack_skill_priors={result['last_pack_training']['pack_skill_priors']})"
        )
    print("\nTop packs:")
    for item in result["top_packs"]:
        print(
            f"- {item['pack_id']} ({item['pack_name']}) score={item['score']:.4f} "
            f"accepted={item['accepted_count']} revised={item['revised_count']} failed={item['failed_count']} exposure={item['exposure_count']}"
        )
    print("\nWeak packs:")
    for item in result["weak_packs"]:
        print(
            f"- {item['pack_id']} ({item['pack_name']}) score={item['score']:.4f} "
            f"accepted={item['accepted_count']} revised={item['revised_count']} failed={item['failed_count']} exposure={item['exposure_count']}"
        )
    print("\nHigh revision packs:")
    for item in result["high_revision_packs"]:
        rating = "-" if item["avg_user_rating"] is None else f"{item['avg_user_rating']:.2f}"
        print(
            f"- {item['pack_id']} ({item['pack_name']}) outcomes={item['outcomes']} "
            f"avg_revisions={item['avg_revision_count']:.2f} avg_rating={rating}"
        )
    print("\nTop pack paths:")
    for item in result["top_pack_paths"]:
        print(f"- {item['pack_id']} :: {item['path']} score={item['score']:.4f} exposure={item['exposure_count']}")
    print("\nWeak pack paths:")
    for item in result["weak_pack_paths"]:
        print(f"- {item['pack_id']} :: {item['path']} score={item['score']:.4f} exposure={item['exposure_count']}")
    print("\nTop pack skills:")
    for item in result["top_pack_skills"]:
        print(f"- {item['pack_id']} :: {item['skill']} score={item['score']:.4f} exposure={item['exposure_count']}")
    print("\nWeak pack skills:")
    for item in result["weak_pack_skills"]:
        print(f"- {item['pack_id']} :: {item['skill']} score={item['score']:.4f} exposure={item['exposure_count']}")


def print_outcome_report(result: dict) -> None:
    averages = result["averages"]
    completion_text = "-" if averages["avg_completion_minutes"] is None else f"{averages['avg_completion_minutes']:.2f}"
    rating_text = "-" if averages["avg_user_rating"] is None else f"{averages['avg_user_rating']:.2f}"
    print(f"DB: {result['db']}")
    print(f"Task outcomes: {result['task_outcomes']}")
    if result["last_outcome_training"]:
        print(
            "Last outcome training: "
            f"{result['last_outcome_training']['ts']} "
            f"(outcomes={result['last_outcome_training']['task_outcomes']}, "
            f"outcome_path_priors={result['last_outcome_training']['outcome_path_priors']}, "
            f"outcome_skill_priors={result['last_outcome_training']['outcome_skill_priors']})"
        )
    if result["status_breakdown"]:
        print("\nStatus breakdown:")
        for item in result["status_breakdown"]:
            print(f"- {item['status']}: count={item['count']} rate={item['rate']:.2%}")
    print(
        "\nAverages: "
        f"revisions={averages['avg_revision_count']:.2f} "
        f"completion_minutes={completion_text} "
        f"user_rating={rating_text}"
    )
    if result["last_outcome"]:
        last = result["last_outcome"]
        print(
            "\nLast outcome: "
            f"{last['pack_id']} ({last['pack_name']}) status={last['status']} "
            f"revisions={last['revision_count']} rating={'-' if last['user_rating'] is None else last['user_rating']}"
        )
    print("\nTop outcome paths:")
    for item in result["top_outcome_paths"]:
        print(
            f"- {item['path']} score={item['score']:.4f} "
            f"accepted={item['accepted_count']} revised={item['revised_count']} failed={item['failed_count']} exposure={item['exposure_count']}"
        )
    print("\nWeak outcome paths:")
    for item in result["weak_outcome_paths"]:
        print(
            f"- {item['path']} score={item['score']:.4f} "
            f"accepted={item['accepted_count']} revised={item['revised_count']} failed={item['failed_count']} exposure={item['exposure_count']}"
        )
    print("\nTop outcome skills:")
    for item in result["top_outcome_skills"]:
        print(
            f"- {item['skill']} score={item['score']:.4f} "
            f"accepted={item['accepted_count']} revised={item['revised_count']} failed={item['failed_count']} exposure={item['exposure_count']}"
        )
    print("\nOver-ranked paths:")
    for item in result["overranked_paths"]:
        print(
            f"- {item['path']} retrieval_score={item['retrieval_score']:.4f} "
            f"outcome_score={item['outcome_score']:.4f} retrieval_exposure={item['retrieval_exposure_count']}"
        )
    print("\nUnderused winners:")
    for item in result["underused_winners"]:
        print(
            f"- {item['path']} outcome_score={item['outcome_score']:.4f} "
            f"retrieval_score={item['retrieval_score']:.4f} outcome_exposure={item['outcome_exposure_count']}"
        )
    print("\nTop skill stacks:")
    for item in result["top_skill_stacks"]:
        print(f"- {', '.join(item['skills'])} outcomes={item['outcomes']}")


def print_task_result_report(result: dict) -> None:
    manual_avg = "-" if result["avg_overall_manual"] is None else f"{result['avg_overall_manual']:.2f}"
    all_avg = "-" if result["avg_overall_all"] is None else f"{result['avg_overall_all']:.2f}"
    print(f"DB: {result['db']}")
    print(f"Task outcomes: {result['task_outcomes']}")
    print(
        "Scorecards: "
        f"manual={result['manual_scorecards']} suggested={result['suggested_scorecards']} "
        f"pending_manual_reviews={result['pending_manual_reviews']}"
    )
    print(f"Averages: manual={manual_avg} all={all_avg}")
    if result["last_result_training"]:
        print(
            "Last result training: "
            f"{result['last_result_training']['ts']} "
            f"(scored={result['last_result_training']['scored_outcomes']}, "
            f"manual={result['last_result_training']['manual_scorecards']}, "
            f"suggested={result['last_result_training']['suggested_scorecards']}, "
            f"pack_priors={result['last_result_training']['result_pack_priors']}, "
            f"path_priors={result['last_result_training']['result_path_priors']}, "
            f"skill_priors={result['last_result_training']['result_skill_priors']})"
        )
    if result["verdict_breakdown"]:
        print("\nVerdict breakdown:")
        for item in result["verdict_breakdown"]:
            print(f"- {item['verdict']}: {item['count']}")
    if result["latest_scored_outcome"]:
        item = result["latest_scored_outcome"]
        print(
            "\nLatest scored outcome: "
            f"{item['outcome_id']} {item['pack_id']} ({item['pack_name']}) "
            f"score={item['overall_score']:.2f} verdict={item['verdict']} mode={item['scoring_mode']}"
        )
    print("\nTop scored packs:")
    for item in result["top_packs"]:
        print(f"- {item['pack_id']} ({item['pack_name']}) avg_score={item['avg_overall_score']:.2f} count={item['count']}")
    print("\nWeak scored packs:")
    for item in result["weak_packs"]:
        print(f"- {item['pack_id']} ({item['pack_name']}) avg_score={item['avg_overall_score']:.2f} count={item['count']}")
    print("\nTop learned pack priors:")
    for item in result["top_learned_packs"]:
        print(
            f"- {item['pack_id']} ({item['pack_name']}) score={item['score']:.4f} "
            f"avg_score={item['avg_overall_score']:.2f} exposure={item['exposure_count']}"
        )
    print("\nWeak learned pack priors:")
    for item in result["weak_learned_packs"]:
        print(
            f"- {item['pack_id']} ({item['pack_name']}) score={item['score']:.4f} "
            f"avg_score={item['avg_overall_score']:.2f} exposure={item['exposure_count']}"
        )
    print("\nTop scored paths:")
    for item in result["top_paths"]:
        print(f"- {item['path']} avg_score={item['avg_overall_score']:.2f} count={item['count']}")
    print("\nWeak scored paths:")
    for item in result["weak_paths"]:
        print(f"- {item['path']} avg_score={item['avg_overall_score']:.2f} count={item['count']}")
    print("\nTop learned path priors:")
    for item in result["top_learned_paths"]:
        print(f"- {item['path']} score={item['score']:.4f} avg_score={item['avg_overall_score']:.2f} exposure={item['exposure_count']}")
    print("\nWeak learned path priors:")
    for item in result["weak_learned_paths"]:
        print(f"- {item['path']} score={item['score']:.4f} avg_score={item['avg_overall_score']:.2f} exposure={item['exposure_count']}")
    print("\nTop scored skills:")
    for item in result["top_skills"]:
        print(f"- {item['skill']} avg_score={item['avg_overall_score']:.2f} count={item['count']}")
    print("\nTop learned skill priors:")
    for item in result["top_learned_skills"]:
        print(f"- {item['skill']} score={item['score']:.4f} avg_score={item['avg_overall_score']:.2f} exposure={item['exposure_count']}")
    print("\nPending manual reviews:")
    for item in result["pending_reviews"]:
        print(
            f"- outcome={item['outcome_id']} pack={item['pack_id']} "
            f"suggested_score={item['suggested_overall_score']:.2f} verdict={item['suggested_verdict']}"
        )


def print_episode_report(result: dict) -> None:
    print(f"DB: {result['db']}")
    print(f"Episodes: {result['episodes']}")
    print(f"Episode items: {result['episode_items']}")
    print(f"Episode summaries: {result['episode_summaries']}")
    if result["episode_types"]:
        print("\nEpisode types:")
        for item in result["episode_types"]:
            print(f"- {item['episode_type']}: {item['count']}")
    if result["recent_episodes"]:
        print("\nRecent episodes:")
        for item in result["recent_episodes"]:
            print(
                f"- [{item['episode_type']}] {item['title']} "
                f"events={item['event_count']} status={item['status'] or '-'} "
                f"skill={item['primary_skill'] or '-'} pack={item['pack_id'] or '-'}"
            )
            print(f"  {item['summary_text']}")


def print_workspace_report(result: dict) -> None:
    print(f"DB: {result['db']}")
    print(f"Active contexts: {result['active_contexts']}")
    print(f"Archived contexts: {result['archived_contexts']}")
    print(f"Active items: {result['active_items']}")
    if result["contexts"]:
        print("\nContexts:")
        for item in result["contexts"]:
            scope = []
            if item["role"]:
                scope.append(f"role={item['role']}")
            if item["pack_id"]:
                scope.append(f"pack={item['pack_id']}")
            if not scope:
                scope.append("global")
            print(
                f"- #{item['id']} [{item['status']}] {item['name']} "
                f"items={item['item_count']} {' '.join(scope)}"
            )
            if item["root_path"]:
                print(f"  root={item['root_path']}")
            for top_item in item["top_items"]:
                print(f"  - {top_item['rel_path'] or top_item['path']} :: {top_item['title']}")


def print_pack_run_payload(result: dict) -> None:
    if "run_id" in result:
        print(f"Run ID: {result['run_id']}")
    if "query" in result:
        print(f"Query: {result['query']}")
    if "selected_pack" in result:
        print(f"Pack: {result['selected_pack']['id']} ({result['selected_pack']['name']})")
        print(f"Primary skill: {result['primary_skill']}")
    print(f"Status: {result['status']}")
    if "current_step_seq" in result:
        print(f"Current step: {result['current_step_seq']}")
    if result.get("steps"):
        print("\nSteps:")
        for item in result["steps"]:
            print(
                f"- {item['seq']}. [{item['status']}] {item['title']} "
                f"(owner={item['owner_skill'] or '-'})"
            )
    if result.get("blockers"):
        print("\nBlockers:")
        for item in result["blockers"]:
            print(
                f"- #{item['id']} [{item['status']}] {item['title']} "
                f"severity={item['severity']} owner={item['owner_skill'] or '-'}"
            )
    if result.get("handoffs"):
        print("\nHandoffs:")
        for item in result["handoffs"]:
            print(f"- {item['from_skill']} -> {item['to_skill']} | {item['reason'] or item['status']}")


def print_pack_run_report(result: dict) -> None:
    print(f"DB: {result['db']}")
    print(f"Total runs: {result['total_runs']}")
    print(f"Active runs: {result['active_runs']}")
    print(f"Blocked runs: {result['blocked_runs']}")
    print(f"Completed runs: {result['completed_runs']}")
    print(f"Open blockers: {result['open_blockers']}")
    if result["recent_runs"]:
        print("\nRecent runs:")
        for item in result["recent_runs"]:
            print(
                f"- Run #{item['id']} [{item['status']}] {item['pack_id']} "
                f"step={item['current_step_seq']}/{item['step_count']} "
                f"blockers={item['blocker_count']} handoffs={item['handoff_count']}"
            )
            print(f"  {truncate_text(item['query'], 120)}")


def print_metadata_suggestions(result: dict) -> None:
    for item in result["suggestions"]:
        print(item["path"])
        signal = item["training_signal"]
        print(
            f"  score={signal['score']:.4f} useful={signal['useful_count']} "
            f"not_useful={signal['not_useful_count']} exposure={signal['exposure_count']}"
        )
        print(f"  current={json.dumps(item['current_meta'], ensure_ascii=True)}")
        print(f"  suggested={json.dumps(item['suggested_meta'], ensure_ascii=True)}")


def print_eval(result: dict) -> None:
    print(f"Fixtures: {result['fixture_path']}")
    print(f"Total cases: {result['total_cases']}")
    print(f"Primary skill accuracy: {result['primary_skill_accuracy']:.2%}")
    print(f"Top-3 skill hit rate: {result['top3_skill_hit_rate']:.2%}")
    print(f"Top-5 path hit rate: {result['top5_path_hit_rate']:.2%}")
    print("\nCases:")
    for idx, item in enumerate(result["results"], start=1):
        print(f"{idx}. {item['query']}")
        print(f"   primary_hit={item['primary_hit']} skill_hit={item['skill_hit']} path_hit={item['path_hit']}")
        print(f"   skills={', '.join(item['recommended_skills'])}")


def print_task_eval(result: dict) -> None:
    print(f"DB: {result['db']}")
    print(f"Packs: {result['packs_file']}")
    print(f"Fixtures: {result['fixture_path']}")
    print(f"Total cases: {result['total_cases']}")
    print(f"Pack accuracy: {result['pack_accuracy']:.2%}")
    print(f"Primary skill accuracy: {result['primary_skill_accuracy']:.2%}")
    print(f"Supporting skill match rate: {result['supporting_skill_match_rate']:.2%}")
    print(f"Memory path hit rate: {result['memory_path_hit_rate']:.2%}")
    print(f"Memory theme hit rate: {result['memory_theme_hit_rate']:.2%}")
    print(f"Output section hit rate: {result['output_section_hit_rate']:.2%}")
    print(f"Deliverable hit rate: {result['deliverable_hit_rate']:.2%}")
    print(f"Pass rate: {result['pass_rate']:.2%}")
    if result["weak_cases"]:
        print("\nWeak cases:")
        for item in result["weak_cases"]:
            checks = ", ".join(item["failed_checks"]) if item["failed_checks"] else "-"
            print(
                f"- {item['query']}\n"
                f"  pack={item['selected_pack_id']} primary={item['primary_skill']} failed={checks}"
            )
    print("\nCases:")
    for idx, item in enumerate(result["results"], start=1):
        print(f"{idx}. {item['query']}")
        print(
            f"   pack_hit={item['pack_hit']} primary_hit={item['primary_hit']} "
            f"supporting_hit={item['supporting_skill_hit']} path_hit={item['memory_path_hit']} "
            f"sections_hit={item['output_section_hit']} deliverables_hit={item['deliverable_hit']} "
            f"pass={item['pass']}"
        )
        print(
            f"   selected_pack={item['selected_pack_id']} primary={item['primary_skill']} "
            f"supporting={', '.join(item['supporting_skills'])}"
        )


def main() -> None:
    args = parse_args()
    if args.command == "build":
        build_index(Path(args.root), Path(args.db))
        return
    if args.command == "query":
        results = rank_chunks(Path(args.db), args.text, args.role, args.skill, args.top)
        payload = {
            "query": args.text,
            "role": args.role,
            "skill_filter": args.skill,
            "workspace_context": workspace_context_snapshot(Path(args.db), args.text, args.role, top=max(4, args.top)),
            "results": results,
        }
        log_query(Path(args.db), "query", args.text, args.role, args.skill, args.top, payload)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_workspace_context(payload["workspace_context"])
            print()
            print_query_results(results)
        return
    if args.command == "decide":
        result = decide(Path(args.db), args.text, args.role, args.top)
        log_query(Path(args.db), "decide", args.text, args.role, None, args.top, result)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_decision(result)
        return
    if args.command == "pinchy":
        result = plan_for_pinchy(Path(args.db), args.text, args.top)
        log_query(Path(args.db), "pinchy", args.text, "pinchy", None, args.top, result)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_pinchy_plan(result)
        return
    if args.command == "task-pack":
        result = resolve_task_pack(
            Path(args.db),
            Path(args.packs_file),
            args.text,
            args.role,
            args.top,
            pack_id=args.pack_id,
        )
        log_query(Path(args.db), "task-pack", args.text, args.role, None, args.top, result)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_task_pack(result)
        return
    if args.command == "execute-plan":
        result = build_execute_plan(
            Path(args.db),
            Path(args.packs_file),
            args.text,
            args.role,
            args.top,
            pack_id=args.pack_id,
        )
        log_query(Path(args.db), "execute-plan", args.text, args.role, None, args.top, result)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_execute_plan(result)
        return
    if args.command == "complete-task":
        result = complete_task(
            Path(args.db),
            Path(args.packs_file),
            args.text,
            args.role,
            args.top,
            args.status,
            revision_count=args.revision_count,
            completion_minutes=args.completion_minutes,
            user_rating=args.user_rating,
            notes=args.notes,
            pack_id=args.pack_id,
            used_paths=args.used_paths,
            used_skills=args.used_skills,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_completed_task(result)
        return
    if args.command == "run-pack":
        result = start_pack_run(
            Path(args.db),
            Path(args.packs_file),
            args.text,
            args.role,
            args.top,
            status=args.status,
            notes=args.notes,
            pack_id=args.pack_id,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_pack_run_payload(result)
        return
    if args.command == "run-step":
        result = update_pack_run_step(
            Path(args.db),
            args.run_id,
            args.step_seq,
            status=args.status,
            owner_skill=args.owner_skill,
            notes=args.notes,
            artifact_path=args.artifact_path,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_pack_run_payload(result)
        return
    if args.command == "run-handoff":
        result = record_pack_run_handoff(
            Path(args.db),
            args.run_id,
            from_skill=args.from_skill,
            to_skill=args.to_skill,
            reason=args.reason,
            notes=args.notes,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_pack_run_payload(result)
        return
    if args.command == "run-blocker":
        result = record_pack_run_blocker(
            Path(args.db),
            args.run_id,
            blocker_id=args.blocker_id,
            step_seq=args.step_seq,
            title=args.title,
            severity=args.severity,
            owner_skill=args.owner_skill,
            status=args.status,
            notes=args.notes,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_pack_run_payload(result)
        return
    if args.command == "run-report":
        result = pack_run_report(Path(args.db), Path(args.packs_file), args.limit, status_filter=args.status)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_pack_run_report(result)
        return
    if args.command == "score-task":
        overrides = {field: getattr(args, field) for field in RESULT_SCORE_FIELDS}
        result = score_task_result(
            Path(args.db),
            args.outcome_id,
            scorer=args.scorer,
            scoring_mode=args.mode,
            notes=args.notes,
            **overrides,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(result, indent=2))
        return
    if args.command == "feedback":
        add_feedback(Path(args.db), args.query, args.path, args.rating)
        print(f"Recorded {args.rating} feedback for {args.path}")
        return
    if args.command == "logs":
        rows = recent_logs(Path(args.db), args.limit)
        print(json.dumps(rows, indent=2))
        return
    if args.command == "train":
        result = train_usage_priors(Path(args.db))
        payload = {"db": str(Path(args.db)), **result}
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_train_summary(payload)
        return
    if args.command == "report":
        result = usage_report(Path(args.db), args.limit)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_usage_report(result)
        return
    if args.command == "pack-train":
        result = train_pack_priors(Path(args.db))
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_train_summary(result)
        return
    if args.command == "outcome-train":
        result = train_outcome_priors(Path(args.db))
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_train_summary(result)
        return
    if args.command == "result-train":
        result = train_result_priors(Path(args.db))
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_train_summary(result)
        return
    if args.command == "episode-build":
        result = rebuild_episodes(Path(args.db), gap_minutes=args.gap_minutes)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_train_summary(result)
        return
    if args.command == "pack-report":
        result = pack_report(Path(args.db), Path(args.packs_file), args.limit)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_pack_report(result)
        return
    if args.command == "outcome-report":
        result = outcome_report(Path(args.db), Path(args.packs_file), args.limit)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_outcome_report(result)
        return
    if args.command == "task-result-report":
        result = task_result_report(Path(args.db), Path(args.packs_file), args.limit)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_task_result_report(result)
        return
    if args.command == "episode-report":
        result = episode_report(Path(args.db), args.limit)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_episode_report(result)
        return
    if args.command == "workspace-sync":
        result = sync_workspace_context(
            Path(args.db),
            args.name,
            [Path(path) for path in args.paths],
            role=args.role,
            pack_id=args.pack_id,
            notes=args.notes,
            max_files=args.max_files,
            max_chars=args.max_chars,
            replace=args.replace,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(result, indent=2))
        return
    if args.command == "workspace-clear":
        result = clear_workspace_context(
            Path(args.db),
            context_id=args.context_id,
            name=args.name,
            all_active=args.all_active,
            delete=args.delete,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(result, indent=2))
        return
    if args.command == "workspace-report":
        result = workspace_report(Path(args.db), args.limit)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_workspace_report(result)
        return
    if args.command == "suggest-metadata":
        result = suggest_metadata(Path(args.db), args.limit, args.path, args.min_useful)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_metadata_suggestions(result)
        return
    if args.command == "eval":
        result = evaluate_fixtures(Path(args.db), Path(args.fixtures))
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_eval(result)
        return
    if args.command == "task-eval":
        result = evaluate_task_fixtures(Path(args.db), Path(args.packs_file), Path(args.fixtures), top=args.top)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_task_eval(result)
        return


if __name__ == "__main__":
    main()
