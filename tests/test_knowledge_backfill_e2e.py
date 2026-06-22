from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from urllib.error import HTTPError


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_SPEC = importlib.util.spec_from_file_location("knowledge_ingest", BASE / "knowledge_ingest.py")
KNOWLEDGE_INGEST = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
MODULE_SPEC.loader.exec_module(KNOWLEDGE_INGEST)


class KnowledgeBackfillE2ETest(unittest.TestCase):
    def test_fetch_bytes_uses_curl_fallback_for_server_errors(self) -> None:
        original_urlopen = KNOWLEDGE_INGEST.urlopen
        original_curl = KNOWLEDGE_INGEST.fetch_bytes_with_curl
        calls: list[tuple[str, int, str]] = []

        def fake_urlopen(_req, timeout: int = 25):
            raise HTTPError(
                "https://example.com/feed.xml",
                503,
                "service unavailable",
                hdrs={},
                fp=None,
            )

        def fake_curl(url: str, timeout: int = 25, accept: str = ""):
            calls.append((url, timeout, accept))
            return b"<rss />"

        KNOWLEDGE_INGEST.urlopen = fake_urlopen
        KNOWLEDGE_INGEST.fetch_bytes_with_curl = fake_curl
        try:
            payload = KNOWLEDGE_INGEST.fetch_bytes(
                "https://example.com/feed.xml",
                timeout=19,
                accept="application/rss+xml",
            )
        finally:
            KNOWLEDGE_INGEST.urlopen = original_urlopen
            KNOWLEDGE_INGEST.fetch_bytes_with_curl = original_curl

        self.assertEqual(payload, b"<rss />")
        self.assertEqual(
            calls,
            [("https://example.com/feed.xml", 19, "application/rss+xml")],
        )

    def test_domain_inference_for_non_explicit_configs(self) -> None:
        self.assertEqual(
            KNOWLEDGE_INGEST.domain_for_source({"roles": ["charles", "pinchy"], "name": "Social Source"}),
            "charles",
        )
        self.assertEqual(
            KNOWLEDGE_INGEST.domain_for_source({"roles": ["support-anemone", "pinchy"], "name": "Support Source"}),
            "support",
        )
        self.assertEqual(
            KNOWLEDGE_INGEST.domain_for_source({"roles": ["researcher", "seo", "pinchy", "current"], "name": "SEO Source"}),
            "seo",
        )
        self.assertEqual(KNOWLEDGE_INGEST.skill_dir_for_domain("support"), "support-anemone")

    def test_collect_archive_urls_uses_sitemaps_and_filters_non_articles(self) -> None:
        original_discover = KNOWLEDGE_INGEST.discover_sitemap_urls
        original_fetch = KNOWLEDGE_INGEST.fetch_bytes

        def fake_discover(_page_url: str, timeout: int = 25):
            return ["https://example.com/sitemap.xml"]

        def fake_fetch(url: str, timeout: int = 25, accept: str = ""):
            if url.endswith("/sitemap.xml"):
                return b"""
                <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
                  <sitemap><loc>https://example.com/post-sitemap.xml</loc></sitemap>
                </sitemapindex>
                """
            if url.endswith("/post-sitemap.xml"):
                return b"""
                <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
                  <url><loc>https://example.com/blog/post-one/</loc></url>
                  <url><loc>https://example.com/blog/post-two/</loc></url>
                  <url><loc>https://example.com/category/news/</loc></url>
                  <url><loc>https://example.com/feed/</loc></url>
                </urlset>
                """
            raise AssertionError(f"Unexpected URL fetched: {url}")

        KNOWLEDGE_INGEST.discover_sitemap_urls = fake_discover
        KNOWLEDGE_INGEST.fetch_bytes = fake_fetch
        try:
            result = KNOWLEDGE_INGEST.collect_archive_urls(
                {
                    "slug": "example",
                    "name": "Example",
                    "homepage": "https://example.com/blog/",
                },
                limit=10,
                sitemap_limit=5,
            )
        finally:
            KNOWLEDGE_INGEST.discover_sitemap_urls = original_discover
            KNOWLEDGE_INGEST.fetch_bytes = original_fetch

        self.assertEqual(len(result["article_urls"]), 2)
        self.assertIn("https://example.com/blog/post-one/", result["article_urls"])
        self.assertIn("https://example.com/blog/post-two/", result["article_urls"])
        self.assertFalse(
            KNOWLEDGE_INGEST.is_probable_listing_article(
                'https://example.com/blog/author/jane-doe">Jane Doe</a>',
                "Jane Doe",
                "https://example.com/blog/",
            )
        )

    def test_extract_article_document_and_note_generation(self) -> None:
        html = """
        <html>
          <head>
            <title>How Search Teams Build Durable Memory</title>
            <meta property="article:published_time" content="2026-03-22T10:00:00Z" />
            <meta name="description" content="A practical guide to building durable memory from search research." />
            <script type="application/ld+json">
              {
                "@context": "https://schema.org",
                "@type": "BlogPosting",
                "headline": "How Search Teams Build Durable Memory",
                "datePublished": "2026-03-22T10:00:00Z",
                "author": {
                  "@type": "Person",
                  "name": "Casey Rivers"
                }
              }
            </script>
          </head>
          <body>
            <article>
              <h1>How Search Teams Build Durable Memory</h1>
              <h2>Entity Signals</h2>
              <p>This guide explains how archive backfills turn scattered source material into structured memory that agents can actually retrieve and use in production systems.</p>
              <ul>
                <li>Tie author expertise to the brand</li>
                <li>Keep source provenance visible</li>
              </ul>
              <h2>Quality Controls</h2>
              <p>It also covers how chunking, canonical review, and promotion gates prevent archive growth from turning into low-quality noise that weakens retrieval quality.</p>
            </article>
          </body>
        </html>
        """
        source_cfg = {
            "slug": "example",
            "name": "Example Research",
            "homepage": "https://example.com/blog/",
            "topic": "archive_backfill",
            "intent": ["research", "archive_backfill"],
            "roles": ["researcher", "pinchy"],
            "confidence": "high",
            "strength": "archive research",
            "tags": ["example", "research"],
        }
        article = KNOWLEDGE_INGEST.extract_article_document(html, "https://example.com/blog/durable-memory/", source_cfg)
        self.assertIsNotNone(article)
        assert article is not None
        self.assertEqual(article["title"], "How Search Teams Build Durable Memory")
        self.assertEqual(article["published"], "2026-03-22")
        self.assertGreaterEqual(len(article["paragraphs"]), 2)
        self.assertEqual(article["author"], "Casey Rivers")
        self.assertIn("BlogPosting", article["schema_types"])
        self.assertIn("Entity Signals", article["headings"])
        self.assertTrue(any(block.startswith("### Entity Signals") for block in article["body_blocks"]))
        self.assertTrue(any("Tie author expertise to the brand" in block for block in article["body_blocks"]))

        note = KNOWLEDGE_INGEST.build_article_note(source_cfg, article)
        self.assertIn("Archive backfill - Example Research", note)
        self.assertIn("## Summary", note)
        self.assertIn("## Metadata", note)
        self.assertIn("Author: Casey Rivers", note)
        self.assertIn("## Section Outline", note)
        self.assertIn("## Extracted Body", note)
        self.assertIn("### Entity Signals", note)
        self.assertIn("How Search Teams Build Durable Memory", note)


if __name__ == "__main__":
    unittest.main()
