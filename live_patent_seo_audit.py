#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urldefrag, urljoin, urlparse, urlunparse

import knowledge_ingest


HOME = Path("/Users/vijaychauhan")
SEO_MEMORY_ROOT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_MAX_PAGES = 7
DEFAULT_TIMEOUT = 20
MAX_SITEMAPS = 6
MAX_SITEMAP_URLS = 80
MAX_HOMEPAGE_LINKS = 60
MAX_LINK_TEXT = 120
JSON_LD_RE = re.compile(
    r"<script\b[^>]*type=(['\"])[^>]*?(?:application/ld\+json|ld\+json)[^>]*?\1[^>]*>(.*?)</script>",
    re.IGNORECASE | re.DOTALL,
)
ANCHOR_RE = re.compile(
    r"<a\b(?P<attrs>[^>]*)href=(?P<quote>['\"])(?P<href>.*?)(?P=quote)[^>]*>(?P<body>.*?)</a>",
    re.IGNORECASE | re.DOTALL,
)
TIME_DATETIME_RE = re.compile(r"<time\b[^>]*datetime=(['\"])(.*?)\1[^>]*>", re.IGNORECASE | re.DOTALL)
LIST_ITEM_RE = re.compile(r"<li\b[^>]*>", re.IGNORECASE)
ORDERED_LIST_RE = re.compile(r"<ol\b[^>]*>", re.IGNORECASE)
TABLE_RE = re.compile(r"<table\b[^>]*>", re.IGNORECASE)
CTA_RE = re.compile(
    r"\b(sign up|get started|start free|request demo|book demo|pricing|contact sales|talk to sales|buy now|request quote|schedule)\b",
    re.IGNORECASE,
)
ABOUT_HINT_RE = re.compile(
    r"\b(about|company|mission|story|trust|editorial|contact|legal|privacy|terms|team|experts?)\b",
    re.IGNORECASE,
)
AUTHOR_BYLINE_RE = re.compile(r"\b(by|author|reviewed by)\b", re.IGNORECASE)
DATE_TEXT_RE = re.compile(
    r"\b("
    r"January|February|March|April|May|June|July|August|September|October|November|December"
    r")\s+\d{1,2},\s+20\d{2}\b",
    re.IGNORECASE,
)
WORD_RE = re.compile(r"[a-z0-9]{2,}", re.IGNORECASE)
PATH_TOKEN_RE = re.compile(r"[a-z0-9]+")
GENERIC_TITLE_TOKENS = {
    "home",
    "homepage",
    "official",
    "welcome",
    "page",
    "blog",
    "article",
    "service",
    "services",
}

AUDIT_TYPES = (
    "eeat_trust",
    "entity_clarity",
    "topical_authority",
    "information_gain",
    "ai_search_readiness",
    "landing_page_quality",
)

PATENT_LENSES: Dict[str, List[Dict[str, str]]] = {
    "eeat_trust": [
        {
            "patent_id": "US20250103662A1",
            "label": "Transformers With Link-Based Ranking",
            "mechanism": "source trust, author credibility, freshness, and model-side source preference",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us20250103662a1-transformers-link-ranking.md"),
        },
        {
            "patent_id": "US7346839B2",
            "label": "Historical Data",
            "mechanism": "historical trust, stable maintenance, freshness, and spam-risk interpretation",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us7346839b2-historical-data.md"),
        },
        {
            "patent_id": "US9009192B1",
            "label": "Central Entities",
            "mechanism": "clear ownership, entity hierarchy, and aboutness reinforcement",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us9009192b1-central-entities.md"),
        },
    ],
    "entity_clarity": [
        {
            "patent_id": "US9009192B1",
            "label": "Central Entities",
            "mechanism": "dominant entity clarity, semantic hierarchy, and supporting-entity reinforcement",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us9009192b1-central-entities.md"),
        },
        {
            "patent_id": "US2008005090A1",
            "label": "Named Entity / Implicit Query",
            "mechanism": "named entity extraction, contextual relevance, and snippet-worthiness",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us2008005090a1-named-entity-implicit-query.md"),
        },
    ],
    "topical_authority": [
        {
            "patent_id": "US10268680B2",
            "label": "Context-Aware Dialog",
            "mechanism": "topic reinforcement, follow-up coverage, and cluster continuity",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us10268680b2-context-aware-dialog.md"),
        },
        {
            "patent_id": "US9009192B1",
            "label": "Central Entities",
            "mechanism": "topic ownership and semantic hierarchy",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us9009192b1-central-entities.md"),
        },
    ],
    "information_gain": [
        {
            "patent_id": "US20200349181A1",
            "label": "Information Gain",
            "mechanism": "anti-commodity content, net-new passages, and extractable differentiation",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us20200349181a1-information-gain.md"),
        }
    ],
    "ai_search_readiness": [
        {
            "patent_id": "US20240289407A1",
            "label": "Stateful Chat",
            "mechanism": "multi-turn retrieval readiness, grounding, and follow-up answer support",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us20240289407a1-stateful-chat.md"),
        },
        {
            "patent_id": "JP2026012740A",
            "label": "Selective Rendering",
            "mechanism": "zero-click answer exposure, fact precision, and machine-readable extraction",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-jp2026012740a-selective-rendering.md"),
        },
        {
            "patent_id": "US20250103662A1",
            "label": "Transformers With Link-Based Ranking",
            "mechanism": "trusted source preference in model-mediated answers",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us20250103662a1-transformers-link-ranking.md"),
        },
    ],
    "landing_page_quality": [
        {
            "patent_id": "US12536233B1",
            "label": "AI-Generated Landing Pages",
            "mechanism": "destination-page quality, intent match, and mediated-click confidence",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us12536233b1-ai-generated-landing-pages.md"),
        },
        {
            "patent_id": "US7346839B2",
            "label": "Historical Data",
            "mechanism": "long-horizon trust and confidence in destination quality",
            "note_path": str(SEO_MEMORY_ROOT / "google-patent-us7346839b2-historical-data.md"),
        },
    ],
}

URL_CATEGORY_HINTS: Dict[str, Tuple[Tuple[str, int], ...]] = {
    "about_or_trust": (
        ("about", 7),
        ("company", 6),
        ("trust", 6),
        ("mission", 5),
        ("story", 5),
        ("editorial", 4),
        ("contact", 4),
        ("legal", 3),
        ("privacy", 2),
        ("terms", 2),
    ),
    "author_or_expert": (
        ("author", 7),
        ("authors", 7),
        ("team", 5),
        ("expert", 5),
        ("experts", 5),
        ("doctor", 4),
        ("reviewer", 4),
        ("contributor", 4),
        ("staff", 3),
    ),
    "commercial": (
        ("pricing", 7),
        ("product", 6),
        ("products", 6),
        ("service", 6),
        ("services", 6),
        ("feature", 6),
        ("features", 6),
        ("solution", 5),
        ("solutions", 5),
        ("demo", 5),
        ("quote", 4),
        ("consulting", 4),
        ("software", 4),
    ),
    "informational": (
        ("blog", 7),
        ("article", 7),
        ("articles", 7),
        ("guide", 6),
        ("guides", 6),
        ("learn", 5),
        ("resource", 5),
        ("resources", 5),
        ("academy", 5),
        ("library", 4),
        ("insights", 4),
        ("help", 3),
        ("docs", 3),
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a local-first live patent-backed SEO audit for a website")
    parser.add_argument("url", help="Website or page URL to audit")
    parser.add_argument("--audit-type", action="append", dest="audit_types", help="Optional audit type filter")
    parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def normalize_url(value: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ValueError("URL is required")
    if "://" not in text:
        text = f"https://{text}"
    parsed = urlparse(text)
    cleaned = parsed._replace(fragment="")
    if not cleaned.path:
        cleaned = cleaned._replace(path="/")
    return urlunparse(cleaned)


def site_root(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse((parsed.scheme or "https", parsed.netloc, "/", "", "", ""))


def normalize_candidate_url(url: str) -> str:
    clean, _fragment = urldefrag(url)
    parsed = urlparse(clean)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return ""
    normalized_path = parsed.path or "/"
    return urlunparse((parsed.scheme, parsed.netloc, normalized_path, "", "", ""))


def same_host(url: str, root_url: str) -> bool:
    url_host = urlparse(url).netloc.lower().strip()
    root_host = urlparse(root_url).netloc.lower().strip()
    return bool(url_host) and url_host == root_host


def tokenize_text(text: str) -> List[str]:
    return [token.lower() for token in WORD_RE.findall(text or "")]


def text_overlap_ratio(a: str, b: str) -> float:
    left = {token for token in tokenize_text(a) if token not in GENERIC_TITLE_TOKENS}
    right = {token for token in tokenize_text(b) if token not in GENERIC_TITLE_TOKENS}
    if not left or not right:
        return 0.0
    return len(left & right) / float(max(len(left), len(right)))


def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def score_to_status(score: int) -> str:
    if score >= 72:
        return "strong"
    if score >= 52:
        return "mixed"
    return "weak"


def excerpt(items: Sequence[str], limit: int = 2) -> List[str]:
    return [item for item in items[:limit] if item]


def load_patent_lenses(audit_types: Sequence[str]) -> List[Dict[str, str]]:
    seen = set()
    rows: List[Dict[str, str]] = []
    for audit_type in audit_types:
        for item in PATENT_LENSES.get(audit_type, []):
            key = (item["patent_id"], item["note_path"])
            if key in seen:
                continue
            seen.add(key)
            rows.append({**item, "audit_type": audit_type})
    return rows


def extract_internal_links(html: str, page_url: str, root_url: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for match in ANCHOR_RE.finditer(html):
        href = match.group("href").strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        absolute = normalize_candidate_url(urljoin(page_url, href))
        if not absolute or not same_host(absolute, root_url):
            continue
        text = knowledge_ingest.strip_html(match.group("body"))[:MAX_LINK_TEXT]
        rows.append({"url": absolute, "text": text})
    return rows


def extract_json_ld_objects(html: str) -> List[Dict[str, Any]]:
    objects: List[Dict[str, Any]] = []
    for match in JSON_LD_RE.finditer(html):
        raw = match.group(2).strip()
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, list):
            for item in parsed:
                if isinstance(item, dict):
                    objects.append(item)
        elif isinstance(parsed, dict):
            objects.append(parsed)
    return objects


def flatten_schema_types(value: Any) -> List[str]:
    if isinstance(value, list):
        items = value
    else:
        items = [value]
    flattened: List[str] = []
    for item in items:
        text = str(item or "").strip()
        if not text:
            continue
        flattened.append(text.split("/")[-1])
    return flattened


def extract_canonical_url(html: str, page_url: str) -> str:
    for tag_html in knowledge_ingest.LINK_TAG_RE.findall(html):
        attrs = knowledge_ingest.parse_link_attrs(tag_html)
        rel_tokens = {token.strip().lower() for token in attrs.get("rel", "").split()}
        if "canonical" not in rel_tokens:
            continue
        href = normalize_candidate_url(urljoin(page_url, attrs.get("href", "")))
        if href:
            return href
    return ""


def extract_page_signals(url: str, html: str, root_url: str) -> Dict[str, Any]:
    title = knowledge_ingest.title_from_html(html)
    h1 = knowledge_ingest.first_heading_text(html)
    meta_description = knowledge_ingest.extract_meta_content(html, "description", "og:description", "twitter:description")
    meta_author = knowledge_ingest.extract_meta_content(html, "author", "article:author")
    meta_site_name = knowledge_ingest.extract_meta_content(html, "og:site_name", "application-name")
    meta_robots = knowledge_ingest.extract_meta_content(html, "robots")
    published_date = (
        knowledge_ingest.extract_meta_content(html, "article:published_time", "datePublished")
        or next((item[1] for item in TIME_DATETIME_RE.findall(html)), "")
        or next((match.group(0) for match in DATE_TEXT_RE.finditer(knowledge_ingest.strip_html(html))), "")
    )
    updated_date = knowledge_ingest.extract_meta_content(html, "article:modified_time", "dateModified")
    canonical_url = extract_canonical_url(html, url)
    link_rows = extract_internal_links(html, url, root_url)
    json_ld_objects = extract_json_ld_objects(html)
    schema_types = sorted({schema_type for item in json_ld_objects for schema_type in flatten_schema_types(item.get("@type"))})
    organization_names = sorted(
        {
            str(item.get("name", "")).strip()
            for item in json_ld_objects
            if "Organization" in flatten_schema_types(item.get("@type")) and str(item.get("name", "")).strip()
        }
    )
    person_names = sorted(
        {
            str(item.get("name", "")).strip()
            for item in json_ld_objects
            if "Person" in flatten_schema_types(item.get("@type")) and str(item.get("name", "")).strip()
        }
    )
    paragraphs = knowledge_ingest.extract_article_paragraphs(html, limit=12)
    body_text = knowledge_ingest.strip_html(html)
    path = urlparse(url).path or "/"
    lower_text = body_text.lower()
    has_author_signal = bool(meta_author or person_names or AUTHOR_BYLINE_RE.search(lower_text))
    has_contact_signal = bool(re.search(r"\b(contact|call|email|phone|support)\b", lower_text))
    has_legal_signal = bool(re.search(r"\b(privacy|terms|policy|legal)\b", lower_text))
    has_cta = bool(CTA_RE.search(lower_text))
    has_faq_schema = "FAQPage" in schema_types
    has_breadcrumb_schema = "BreadcrumbList" in schema_types
    has_article_schema = any(item in schema_types for item in ("Article", "BlogPosting", "NewsArticle"))
    has_person_schema = "Person" in schema_types
    has_org_schema = any(item in schema_types for item in ("Organization", "WebSite", "LocalBusiness", "MedicalOrganization"))
    word_count = len(tokenize_text(body_text))
    average_paragraph_words = 0
    if paragraphs:
        average_paragraph_words = sum(len(tokenize_text(item)) for item in paragraphs) // len(paragraphs)
    evidence_markers = 0
    if LIST_ITEM_RE.search(html):
        evidence_markers += 1
    if ORDERED_LIST_RE.search(html):
        evidence_markers += 1
    if TABLE_RE.search(html):
        evidence_markers += 1
    if len(re.findall(r"\b\d{2,}\b", body_text)) >= 3:
        evidence_markers += 1
    if re.search(r"\b(compare|comparison|case study|workflow|checklist|example|examples|step 1|steps)\b", lower_text):
        evidence_markers += 1
    internal_link_targets = [item["url"] for item in link_rows]
    about_link_count = sum(1 for item in link_rows if ABOUT_HINT_RE.search(item["text"]) or ABOUT_HINT_RE.search(item["url"]))
    title_h1_overlap = text_overlap_ratio(title, h1)
    return {
        "url": url,
        "path": path,
        "title": title,
        "h1": h1,
        "meta_description": meta_description,
        "meta_author": meta_author,
        "site_name": meta_site_name,
        "meta_robots": meta_robots,
        "canonical_url": canonical_url,
        "canonical_matches_url": bool(canonical_url and normalize_candidate_url(canonical_url) == normalize_candidate_url(url)),
        "published_date": knowledge_ingest.normalize_date(published_date) if published_date else "",
        "updated_date": knowledge_ingest.normalize_date(updated_date) if updated_date else "",
        "word_count": word_count,
        "paragraph_count": len(paragraphs),
        "average_paragraph_words": average_paragraph_words,
        "content_excerpt": excerpt(paragraphs, limit=2),
        "internal_links": len(internal_link_targets),
        "about_link_count": about_link_count,
        "internal_link_targets": internal_link_targets[:40],
        "schema_types": schema_types,
        "organization_names": organization_names,
        "person_names": person_names,
        "has_author_signal": has_author_signal,
        "has_contact_signal": has_contact_signal,
        "has_legal_signal": has_legal_signal,
        "has_cta": has_cta,
        "has_faq_schema": has_faq_schema,
        "has_breadcrumb_schema": has_breadcrumb_schema,
        "has_article_schema": has_article_schema,
        "has_person_schema": has_person_schema,
        "has_org_schema": has_org_schema,
        "evidence_markers": evidence_markers,
        "title_h1_overlap": round(title_h1_overlap, 3),
    }


def url_pattern_score(url: str, category: str) -> int:
    parsed = urlparse(url)
    blob = f"{parsed.path} {parsed.netloc}".lower()
    score = 0
    for token, weight in URL_CATEGORY_HINTS.get(category, ()):
        if token in blob:
            score += weight
    if category == "commercial" and any(token in blob for token in ("blog", "article", "guide", "resource", "learn")):
        score -= 4
    if category == "informational" and any(token in blob for token in ("pricing", "service", "product", "demo")):
        score -= 3
    return score


def gather_candidate_urls(seed_url: str, timeout: int) -> Dict[str, Any]:
    root_url = site_root(seed_url)
    homepage_html = knowledge_ingest.fetch_html(root_url, timeout=timeout)
    homepage_links = extract_internal_links(homepage_html, root_url, root_url)
    seed_links: List[Dict[str, str]] = []
    if normalize_candidate_url(seed_url) != normalize_candidate_url(root_url):
        try:
            seed_html = knowledge_ingest.fetch_html(seed_url, timeout=timeout)
            seed_links = extract_internal_links(seed_html, seed_url, root_url)
        except Exception:
            seed_links = []

    sitemap_candidates: List[str] = []
    sitemap_urls: List[str] = []
    try:
        queue = list(knowledge_ingest.discover_sitemap_urls(root_url, timeout=timeout))
        seen_sitemaps = set()
        while queue and len(sitemap_urls) < MAX_SITEMAPS and len(sitemap_candidates) < MAX_SITEMAP_URLS:
            sitemap_url = queue.pop(0)
            if sitemap_url in seen_sitemaps:
                continue
            seen_sitemaps.add(sitemap_url)
            sitemap_urls.append(sitemap_url)
            raw = knowledge_ingest.fetch_bytes(sitemap_url, timeout=timeout, accept="application/xml,text/xml;q=0.9,*/*;q=0.5")
            child_sitemaps, page_urls = knowledge_ingest.parse_sitemap(raw, sitemap_url)
            for child in child_sitemaps:
                if child not in seen_sitemaps and child not in queue:
                    queue.append(child)
            for page_url in page_urls:
                normalized = normalize_candidate_url(page_url)
                if not normalized or not same_host(normalized, root_url):
                    continue
                sitemap_candidates.append(normalized)
                if len(sitemap_candidates) >= MAX_SITEMAP_URLS:
                    break
    except Exception:
        sitemap_urls = []
        sitemap_candidates = []

    candidates = {normalize_candidate_url(root_url): "homepage", normalize_candidate_url(seed_url): "seed"}
    for item in homepage_links[:MAX_HOMEPAGE_LINKS]:
        candidates.setdefault(item["url"], "homepage_link")
    for item in seed_links[:MAX_HOMEPAGE_LINKS]:
        candidates.setdefault(item["url"], "seed_link")
    for item in sitemap_candidates:
        candidates.setdefault(item, "sitemap")

    urls = [url for url in candidates if url]
    return {
        "root_url": root_url,
        "homepage_html": homepage_html,
        "candidate_urls": urls,
        "candidate_sources": candidates,
        "source_counts": {
            "homepage_links": len(homepage_links),
            "seed_links": len(seed_links),
            "sitemap_urls": len(sitemap_candidates),
            "inspected_sitemaps": len(sitemap_urls),
        },
    }


def select_urls_for_audit(seed_url: str, candidate_urls: Sequence[str]) -> List[Dict[str, str]]:
    root_url = site_root(seed_url)
    selected: List[Dict[str, str]] = []
    seen = set()

    def add(url: str, reason: str) -> None:
        normalized = normalize_candidate_url(url)
        if not normalized or normalized in seen:
            return
        seen.add(normalized)
        selected.append({"url": normalized, "selection_reason": reason})

    add(root_url, "homepage")
    if normalize_candidate_url(seed_url) != normalize_candidate_url(root_url):
        add(seed_url, "seed_page")

    scored = {
        category: sorted(
            (
                {"url": url, "score": url_pattern_score(url, category)}
                for url in candidate_urls
                if normalize_candidate_url(url) not in seen
            ),
            key=lambda item: (item["score"], -len(urlparse(item["url"]).path)),
            reverse=True,
        )
        for category in ("about_or_trust", "author_or_expert", "commercial", "informational")
    }

    for item in scored["about_or_trust"][:1]:
        if item["score"] > 0:
            add(item["url"], "about_or_trust")
    for item in scored["author_or_expert"][:1]:
        if item["score"] > 0:
            add(item["url"], "author_or_expert")
    for item in scored["commercial"][:2]:
        if item["score"] > 0:
            add(item["url"], "commercial")
    for item in scored["informational"][:2]:
        if item["score"] > 0:
            add(item["url"], "informational")

    for url in candidate_urls:
        if len(selected) >= DEFAULT_MAX_PAGES + 2:
            break
        add(url, "fallback")
    return selected


def fetch_page(url: str, timeout: int) -> Dict[str, Any]:
    try:
        html = knowledge_ingest.fetch_html(url, timeout=timeout)
        return {"url": url, "status": "ok", "html": html}
    except Exception as exc:
        return {"url": url, "status": "error", "error": f"{type(exc).__name__}: {exc}"}


def select_signal_groups(page_signals: Sequence[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    groups = {
        "homepage": [],
        "about_or_trust": [],
        "author_or_expert": [],
        "commercial": [],
        "informational": [],
    }
    for item in page_signals:
        reason = item.get("selection_reason", "")
        if reason in groups:
            groups[reason].append(item)
    return groups


def add_finding(
    findings: List[Dict[str, Any]],
    audit_type: str,
    severity: str,
    title: str,
    evidence: Iterable[str],
    fix: str,
) -> None:
    findings.append(
        {
            "audit_type": audit_type,
            "severity": severity,
            "title": title,
            "evidence": [item for item in evidence if item],
            "fix": fix,
            "patent_lenses": [item["patent_id"] for item in PATENT_LENSES.get(audit_type, [])],
        }
    )


def assess_eeat(groups: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    homepage = groups["homepage"][0] if groups["homepage"] else {}
    about_pages = groups["about_or_trust"]
    author_pages = groups["author_or_expert"]
    info_pages = groups["informational"]
    findings: List[Dict[str, Any]] = []
    strengths: List[str] = []
    score = 50

    if about_pages:
        strengths.append("A trust/about page was discoverable in the audited page set.")
        score += 12
    else:
        add_finding(
            findings,
            "eeat_trust",
            "high",
            "Trust and ownership pages are hard to verify",
            [f"The audit did not find a clear About/Trust page from {homepage.get('url', 'the homepage')}."],
            "Expose a strong About or Trust page with clear business identity, editorial standards, and contact pathways.",
        )
        score -= 20

    if homepage.get("has_org_schema"):
        strengths.append("Homepage exposes organization-level structured data.")
        score += 10
    else:
        add_finding(
            findings,
            "eeat_trust",
            "medium",
            "Homepage lacks clear organization schema",
            [f"{homepage.get('url', 'Homepage')} did not surface Organization-style schema."],
            "Add Organization or LocalBusiness schema and reinforce the same entity consistently across homepage and trust pages.",
        )
        score -= 10

    if author_pages:
        strengths.append("An author or expert profile page was discoverable.")
        score += 8

    if info_pages:
        pages_with_author = [item for item in info_pages if item.get("has_author_signal")]
        pages_with_dates = [item for item in info_pages if item.get("published_date") or item.get("updated_date")]
        if len(pages_with_author) == len(info_pages):
            strengths.append("Informational pages surfaced author signals consistently.")
            score += 10
        elif not pages_with_author:
            add_finding(
                findings,
                "eeat_trust",
                "high",
                "Informational content lacks clear authorship",
                [f"{item['url']} has no clear author signal." for item in info_pages],
                "Add visible authorship, reviewer information, and connect authors to expert profile pages.",
            )
            score -= 18
        else:
            add_finding(
                findings,
                "eeat_trust",
                "medium",
                "Authorship is inconsistent across informational pages",
                [f"{item['url']} has no clear author signal." for item in info_pages if not item.get("has_author_signal")],
                "Standardize authorship and reviewer signals across informational templates.",
            )
            score -= 8

        if len(pages_with_dates) >= max(1, len(info_pages) - 1):
            strengths.append("Most informational pages surfaced published or updated dates.")
            score += 6
        else:
            add_finding(
                findings,
                "eeat_trust",
                "medium",
                "Freshness and maintenance cues are patchy",
                [f"{item['url']} has no visible published or updated date." for item in info_pages if not (item.get('published_date') or item.get('updated_date'))],
                "Surface publication and update dates consistently on informational templates.",
            )
            score -= 6

    if homepage.get("has_contact_signal") or homepage.get("has_legal_signal") or homepage.get("about_link_count", 0) > 0:
        strengths.append("Homepage exposes supporting trust or contact cues.")
        score += 5
    else:
        score -= 4

    return {
        "audit_type": "eeat_trust",
        "score": max(0, min(score, 100)),
        "status": score_to_status(max(0, min(score, 100))),
        "strengths": strengths,
        "findings": findings,
    }


def assess_entity(groups: Dict[str, List[Dict[str, Any]]], page_signals: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    homepage = groups["homepage"][0] if groups["homepage"] else {}
    findings: List[Dict[str, Any]] = []
    strengths: List[str] = []
    score = 50
    canonical_coverage = [item for item in page_signals if item.get("canonical_url")]
    strong_alignment = [item for item in page_signals if item.get("title_h1_overlap", 0.0) >= 0.45]

    if homepage.get("organization_names") or homepage.get("site_name") or homepage.get("title"):
        strengths.append("Homepage exposes a dominant brand/entity candidate.")
        score += 10
    else:
        add_finding(
            findings,
            "entity_clarity",
            "high",
            "Homepage does not clearly anchor the core entity",
            [f"{homepage.get('url', 'Homepage')} has weak title/H1/entity signals."],
            "Clarify the primary entity with stronger title, H1, organization schema, and above-the-fold copy.",
        )
        score -= 18

    if len(canonical_coverage) >= max(1, len(page_signals) - 1):
        strengths.append("Canonical coverage is strong across the audited page set.")
        score += 10
    else:
        add_finding(
            findings,
            "entity_clarity",
            "medium",
            "Canonical signals are inconsistent",
            [f"{item['url']} is missing a canonical URL." for item in page_signals if not item.get("canonical_url")],
            "Add stable canonicals across templates so entity and page ownership signals are less ambiguous.",
        )
        score -= 10

    if len(strong_alignment) >= max(1, len(page_signals) - 1):
        strengths.append("Most pages show healthy title-to-H1 alignment.")
        score += 8
    else:
        add_finding(
            findings,
            "entity_clarity",
            "medium",
            "Title and H1 signals drift on some pages",
            [
                f"{item['url']} has weak title/H1 overlap ({item.get('title_h1_overlap', 0.0)})."
                for item in page_signals
                if item.get("title_h1_overlap", 0.0) < 0.45
            ],
            "Tighten title and H1 alignment so the page’s dominant entity and intent are easier to identify.",
        )
        score -= 8

    if groups["about_or_trust"]:
        strengths.append("The site has a dedicated page for entity and business context.")
        score += 6

    return {
        "audit_type": "entity_clarity",
        "score": max(0, min(score, 100)),
        "status": score_to_status(max(0, min(score, 100))),
        "strengths": strengths,
        "findings": findings,
    }


def assess_topical_authority(groups: Dict[str, List[Dict[str, Any]]], discovery: Dict[str, Any]) -> Dict[str, Any]:
    info_pages = groups["informational"]
    findings: List[Dict[str, Any]] = []
    strengths: List[str] = []
    score = 50
    discovered_info = sum(1 for url in discovery.get("candidate_urls", []) if url_pattern_score(url, "informational") > 0)
    avg_word_count = sum(item.get("word_count", 0) for item in info_pages) // len(info_pages) if info_pages else 0

    if discovered_info >= 4:
        strengths.append("The site exposes multiple informational URLs that look like a cluster, not a single orphan article.")
        score += 10
    elif discovered_info >= 2:
        score += 3
    else:
        add_finding(
            findings,
            "topical_authority",
            "medium",
            "Topical coverage looks thin from the audit surface",
            [f"Only {discovered_info} informational candidate URLs were discoverable from homepage and sitemaps."],
            "Expand or better expose cluster-supporting content through internal linking, resource hubs, and sitemap coverage.",
        )
        score -= 12

    if info_pages and avg_word_count >= 650:
        strengths.append("Supporting informational pages have enough depth to suggest real topic coverage.")
        score += 8
    elif info_pages and avg_word_count < 450:
        add_finding(
            findings,
            "topical_authority",
            "medium",
            "Supporting content looks shallow",
            [f"Average informational word count is {avg_word_count} across the inspected supporting pages."],
            "Strengthen cluster pages with deeper explanations, internal transitions, and more complete supporting coverage.",
        )
        score -= 8

    homepage_links_to_info = 0
    if groups["homepage"]:
        homepage_links_to_info = sum(
            1
            for target in groups["homepage"][0].get("internal_link_targets", [])
            if any(target == item["url"] for item in info_pages)
        )
    if homepage_links_to_info >= 2:
        strengths.append("Homepage or primary navigation connects into informational support pages.")
        score += 5
    elif info_pages:
        add_finding(
            findings,
            "topical_authority",
            "low",
            "Important informational pages are not strongly reinforced from primary navigation",
            [f"Only {homepage_links_to_info} inspected informational pages were linked directly from the homepage."],
            "Give core cluster content more visible internal links from hubs, navigation, or supporting pages.",
        )
        score -= 4

    return {
        "audit_type": "topical_authority",
        "score": max(0, min(score, 100)),
        "status": score_to_status(max(0, min(score, 100))),
        "strengths": strengths,
        "findings": findings,
    }


def assess_information_gain(groups: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    info_pages = groups["informational"]
    findings: List[Dict[str, Any]] = []
    strengths: List[str] = []
    if not info_pages:
        return {
            "audit_type": "information_gain",
            "score": 0,
            "status": "insufficient_evidence",
            "strengths": strengths,
            "findings": findings,
        }

    score = 50
    avg_markers = sum(item.get("evidence_markers", 0) for item in info_pages) / float(len(info_pages))
    avg_words = sum(item.get("word_count", 0) for item in info_pages) / float(len(info_pages))

    if avg_markers >= 2.0:
        strengths.append("Supporting content includes structure that can carry differentiated evidence or workflows.")
        score += 10
    else:
        add_finding(
            findings,
            "information_gain",
            "medium",
            "Supporting content looks too summary-shaped",
            [f"Average evidence marker count is {avg_markers:.1f} across inspected informational pages."],
            "Add examples, comparisons, workflows, data points, or original evidence so the content adds more than a generic summary.",
        )
        score -= 10

    if avg_words >= 700:
        strengths.append("Inspected informational pages have enough length to support net-new detail.")
        score += 6
    elif avg_words < 450:
        add_finding(
            findings,
            "information_gain",
            "medium",
            "Informational pages may not go deep enough to create obvious net-new value",
            [f"Average informational word count is {avg_words:.0f}."],
            "Increase specificity with original passages, examples, measurements, or distinctive workflows.",
        )
        score -= 6

    if any(item.get("has_article_schema") for item in info_pages):
        strengths.append("At least one informational page uses article-level structured data.")
        score += 4

    return {
        "audit_type": "information_gain",
        "score": max(0, min(score, 100)),
        "status": score_to_status(max(0, min(score, 100))),
        "strengths": strengths,
        "findings": findings,
    }


def assess_ai_readiness(groups: Dict[str, List[Dict[str, Any]]], page_signals: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    findings: List[Dict[str, Any]] = []
    strengths: List[str] = []
    score = 50
    structured_pages = [
        item
        for item in page_signals
        if item.get("has_org_schema") or item.get("has_article_schema") or item.get("has_breadcrumb_schema") or item.get("has_faq_schema")
    ]
    chunkable_pages = [
        item
        for item in page_signals
        if item.get("paragraph_count", 0) >= 3 and item.get("average_paragraph_words", 999) <= 120
    ]

    if len(structured_pages) >= max(1, len(page_signals) - 2):
        strengths.append("Structured data appears on most inspected pages.")
        score += 10
    else:
        add_finding(
            findings,
            "ai_search_readiness",
            "medium",
            "Structured extraction signals are limited",
            [f"{item['url']} exposes little or no useful structured data." for item in page_signals if item not in structured_pages],
            "Improve Organization, Article, Breadcrumb, or FAQ schema coverage so systems can extract trustworthy facts more easily.",
        )
        score -= 10

    if len(chunkable_pages) >= max(1, len(page_signals) - 2):
        strengths.append("Pages are reasonably chunkable for answer extraction and follow-up retrieval.")
        score += 8
    else:
        add_finding(
            findings,
            "ai_search_readiness",
            "medium",
            "Pages are not consistently structured for extraction",
            [f"{item['url']} has weak paragraph/section chunkability." for item in page_signals if item not in chunkable_pages],
            "Use clearer sections, shorter answer-bearing blocks, and stronger heading structure for machine retrieval.",
        )
        score -= 8

    if any(item.get("has_faq_schema") for item in page_signals):
        strengths.append("FAQ-style structured answers exist on the audited pages.")
        score += 6
    else:
        add_finding(
            findings,
            "ai_search_readiness",
            "low",
            "The site exposes few explicit answer surfaces",
            ["No inspected page surfaced FAQ-style structured answers."],
            "Add cleaner answer blocks, FAQ sections, or extractable fact surfaces where appropriate.",
        )
        score -= 4

    return {
        "audit_type": "ai_search_readiness",
        "score": max(0, min(score, 100)),
        "status": score_to_status(max(0, min(score, 100))),
        "strengths": strengths,
        "findings": findings,
    }


def assess_landing_quality(groups: Dict[str, List[Dict[str, Any]]], homepage: Dict[str, Any]) -> Dict[str, Any]:
    commercial_pages = groups["commercial"]
    findings: List[Dict[str, Any]] = []
    strengths: List[str] = []
    if not commercial_pages:
        return {
            "audit_type": "landing_page_quality",
            "score": 0,
            "status": "insufficient_evidence",
            "strengths": strengths,
            "findings": findings,
        }

    score = 50
    meta_ok = [item for item in commercial_pages if item.get("meta_description")]
    canonical_ok = [item for item in commercial_pages if item.get("canonical_url")]
    cta_ok = [item for item in commercial_pages if item.get("has_cta")]
    trust_ok = [item for item in commercial_pages if item.get("has_contact_signal") or item.get("has_legal_signal") or homepage.get("about_link_count", 0) > 0]

    if len(meta_ok) == len(commercial_pages):
        strengths.append("Commercial pages have meta descriptions for result and snippet framing.")
        score += 8
    else:
        add_finding(
            findings,
            "landing_page_quality",
            "medium",
            "Some commercial pages are missing meta descriptions",
            [f"{item['url']} has no meta description." for item in commercial_pages if not item.get("meta_description")],
            "Write clearer meta descriptions on commercial pages so intent match is easier before the click.",
        )
        score -= 8

    if len(canonical_ok) == len(commercial_pages):
        strengths.append("Commercial canonicals are stable across the audited set.")
        score += 8
    else:
        add_finding(
            findings,
            "landing_page_quality",
            "medium",
            "Commercial canonicals are inconsistent",
            [f"{item['url']} is missing a canonical URL." for item in commercial_pages if not item.get("canonical_url")],
            "Set explicit canonicals on commercial templates so destination ownership is clearer.",
        )
        score -= 8

    if len(cta_ok) >= max(1, len(commercial_pages) - 1):
        strengths.append("Commercial pages surface clear next-step calls to action.")
        score += 6
    else:
        add_finding(
            findings,
            "landing_page_quality",
            "low",
            "Commercial pages could be clearer about the next action",
            [f"{item['url']} has weak CTA language." for item in commercial_pages if not item.get("has_cta")],
            "Make the primary next step clearer with stronger CTA framing and above-the-fold clarity.",
        )
        score -= 5

    if trust_ok:
        strengths.append("Commercial pages inherit at least some trust cues from the wider site.")
        score += 4

    return {
        "audit_type": "landing_page_quality",
        "score": max(0, min(score, 100)),
        "status": score_to_status(max(0, min(score, 100))),
        "strengths": strengths,
        "findings": findings,
    }


def assess_lenses(audit_types: Sequence[str], page_signals: Sequence[Dict[str, Any]], discovery: Dict[str, Any]) -> List[Dict[str, Any]]:
    groups = select_signal_groups(page_signals)
    homepage = groups["homepage"][0] if groups["homepage"] else {}
    results: List[Dict[str, Any]] = []
    for audit_type in audit_types:
        if audit_type == "eeat_trust":
            results.append(assess_eeat(groups))
        elif audit_type == "entity_clarity":
            results.append(assess_entity(groups, page_signals))
        elif audit_type == "topical_authority":
            results.append(assess_topical_authority(groups, discovery))
        elif audit_type == "information_gain":
            results.append(assess_information_gain(groups))
        elif audit_type == "ai_search_readiness":
            results.append(assess_ai_readiness(groups, page_signals))
        elif audit_type == "landing_page_quality":
            results.append(assess_landing_quality(groups, homepage))
    return results


def priority_findings(lens_results: Sequence[Dict[str, Any]], limit: int = 6) -> List[Dict[str, Any]]:
    severity_rank = {"high": 0, "medium": 1, "low": 2}
    rows: List[Dict[str, Any]] = []
    for lens in lens_results:
        rows.extend(lens.get("findings", []))
    rows.sort(key=lambda item: (severity_rank.get(item.get("severity", "low"), 9), item.get("audit_type", "")))
    return rows[:limit]


def build_summary(
    root_url: str,
    page_signals: Sequence[Dict[str, Any]],
    lens_results: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    applicable_scores = [item["score"] for item in lens_results if item.get("status") != "insufficient_evidence"]
    overall_score = safe_int(sum(applicable_scores) / len(applicable_scores), 0) if applicable_scores else 0
    overall_status = score_to_status(overall_score) if applicable_scores else "insufficient_evidence"
    homepage = next((item for item in page_signals if item.get("selection_reason") == "homepage"), {})
    site_name = (
        (homepage.get("organization_names") or [None])[0]
        or homepage.get("site_name")
        or homepage.get("title")
        or urlparse(root_url).netloc
    )
    findings = priority_findings(lens_results, limit=4)
    priority_actions = [item["fix"] for item in findings[:4]]
    if findings:
        headline = f"{site_name} looks {overall_status} overall; the biggest gaps are in {', '.join(sorted({item['audit_type'] for item in findings[:2]}))}."
    else:
        headline = f"{site_name} shows mostly solid signals in the audited page set."
    return {
        "site_name": site_name,
        "overall_score": overall_score,
        "overall_status": overall_status,
        "headline": headline,
        "priority_actions": priority_actions,
    }


def audit_site(
    url: str,
    audit_types: Optional[Sequence[str]] = None,
    max_pages: int = DEFAULT_MAX_PAGES,
    timeout: int = DEFAULT_TIMEOUT,
) -> Dict[str, Any]:
    normalized_url = normalize_url(url)
    selected_audit_types = [item for item in (audit_types or AUDIT_TYPES) if item in AUDIT_TYPES]
    if not selected_audit_types:
        raise ValueError("No valid audit types provided")

    discovery = gather_candidate_urls(normalized_url, timeout=timeout)
    selected_urls = select_urls_for_audit(normalized_url, discovery["candidate_urls"])[: max(3, min(max_pages, 12))]

    fetch_results: List[Dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(selected_urls), 6) or 1) as pool:
        futures = [pool.submit(fetch_page, item["url"], timeout) for item in selected_urls]
        for future, selected in zip(futures, selected_urls):
            result = future.result()
            result["selection_reason"] = selected["selection_reason"]
            fetch_results.append(result)

    page_signals: List[Dict[str, Any]] = []
    fetch_errors: List[Dict[str, Any]] = []
    for item in fetch_results:
        if item["status"] != "ok":
            fetch_errors.append({"url": item["url"], "error": item.get("error", "unknown error"), "selection_reason": item["selection_reason"]})
            continue
        signals = extract_page_signals(item["url"], item["html"], discovery["root_url"])
        signals["selection_reason"] = item["selection_reason"]
        page_signals.append(signals)

    lens_results = assess_lenses(selected_audit_types, page_signals, discovery)
    summary = build_summary(discovery["root_url"], page_signals, lens_results)

    return {
        "scope": {
            "input_url": url,
            "normalized_url": normalized_url,
            "site_root": discovery["root_url"],
            "audit_types": selected_audit_types,
            "max_pages": max_pages,
            "timeout": timeout,
        },
        "page_selection": {
            "discovered_candidate_count": len(discovery["candidate_urls"]),
            "source_counts": discovery["source_counts"],
            "selected_pages": [{"url": item["url"], "selection_reason": item["selection_reason"]} for item in selected_urls],
            "fetched_ok": len(page_signals),
            "fetched_error": len(fetch_errors),
        },
        "pages": page_signals,
        "fetch_errors": fetch_errors,
        "patent_lenses": load_patent_lenses(selected_audit_types),
        "lens_results": lens_results,
        "top_findings": priority_findings(lens_results),
        "summary": summary,
        "limitations": [
            "This V1 reads raw HTML and sitemap/homepage surfaces only.",
            "Heavy JavaScript rendering or gated content may hide signals from the audit.",
            "Patent lenses are audit frameworks, not proof of direct ranking-factor usage.",
        ],
    }


def render_text_report(payload: Dict[str, Any]) -> str:
    lines = [
        f"Live patent audit: {payload['summary']['site_name']}",
        f"Root: {payload['scope']['site_root']}",
        f"Overall: {payload['summary']['overall_status']} [{payload['summary']['overall_score']}]",
        f"Pages fetched: {payload['page_selection']['fetched_ok']} ok / {payload['page_selection']['fetched_error']} error",
        payload["summary"]["headline"],
        "",
        "Top findings:",
    ]
    findings = payload.get("top_findings", [])
    if not findings:
        lines.append("- No major findings in the audited sample.")
    else:
        for item in findings[:6]:
            lines.append(
                f"- [{item['severity']}] {item['audit_type']}: {item['title']} "
                f":: patents={', '.join(item.get('patent_lenses', []))}"
            )
    lines.extend(["", "Priority actions:"])
    for item in payload["summary"].get("priority_actions", [])[:5]:
        lines.append(f"- {item}")
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    payload = audit_site(
        args.url,
        audit_types=args.audit_types,
        max_pages=args.max_pages,
        timeout=args.timeout,
    )
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(render_text_report(payload))


if __name__ == "__main__":
    main()
