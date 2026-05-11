from __future__ import annotations

import functools
import http.server
import json
import socketserver
import sys
import tempfile
import threading
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MCP_BASE = BASE / "mcp"
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))
if str(MCP_BASE) not in sys.path:
    sys.path.insert(0, str(MCP_BASE))

import live_patent_seo_audit
from universal_memory_mcp_server import SquadMemoryOsMcpServer


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return


class LivePatentSeoAuditTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self._write_site_fixture()
        handler = functools.partial(QuietHandler, directory=str(self.root))
        self.httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        self.base_url = f"http://127.0.0.1:{self.httpd.server_address[1]}"

    def tearDown(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()
        self.thread.join(timeout=2)
        self.temp_dir.cleanup()

    def _write(self, rel_path: str, text: str) -> None:
        path = self.root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _write_site_fixture(self) -> None:
        self._write(
            "robots.txt",
            "User-agent: *\nAllow: /\nSitemap: http://127.0.0.1:1/sitemap.xml\n",
        )
        self._write(
            "sitemap.xml",
            "\n".join(
                [
                    '<?xml version="1.0" encoding="UTF-8"?>',
                    "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">",
                    "  <url><loc>http://127.0.0.1:1/</loc></url>",
                    "  <url><loc>http://127.0.0.1:1/about.html</loc></url>",
                    "  <url><loc>http://127.0.0.1:1/team/dr-jane.html</loc></url>",
                    "  <url><loc>http://127.0.0.1:1/services/seo-audit.html</loc></url>",
                    "  <url><loc>http://127.0.0.1:1/pricing.html</loc></url>",
                    "  <url><loc>http://127.0.0.1:1/blog/ai-visibility-guide.html</loc></url>",
                    "  <url><loc>http://127.0.0.1:1/blog/entity-clusters.html</loc></url>",
                    "</urlset>",
                    "",
                ]
            ),
        )
        self._write(
            "index.html",
            """
<!doctype html>
<html>
  <head>
    <title>Acme Health SEO | Patent-Aware Health Visibility Platform</title>
    <meta name="description" content="Acme Health helps clinics build trusted, machine-readable health content.">
    <link rel="canonical" href="/" />
    <script type="application/ld+json">
      {"@context":"https://schema.org","@type":"Organization","name":"Acme Health","url":"http://127.0.0.1:1/"}
    </script>
  </head>
  <body>
    <header>
      <a href="/about.html">About</a>
      <a href="/team/dr-jane.html">Experts</a>
      <a href="/services/seo-audit.html">SEO Audit Service</a>
      <a href="/pricing.html">Pricing</a>
      <a href="/blog/ai-visibility-guide.html">AI Visibility Guide</a>
      <a href="/blog/entity-clusters.html">Entity Cluster Guide</a>
      <a href="/privacy.html">Privacy</a>
      <a href="/terms.html">Terms</a>
    </header>
    <main>
      <h1>Trusted health SEO for clinics and expert-led publishers</h1>
      <p>Acme Health helps clinics turn expertise, trust, and entity clarity into stronger search visibility and better patient confidence.</p>
      <p>We publish health SEO guidance, clinic trust playbooks, and expert-backed content operations frameworks built for machine-readable answers.</p>
    </main>
  </body>
</html>
""".strip()
            + "\n",
        )
        self._write(
            "about.html",
            """
<!doctype html>
<html>
  <head>
    <title>About Acme Health</title>
    <meta name="description" content="Learn how Acme Health works with clinics and expert medical teams.">
    <link rel="canonical" href="/about.html" />
  </head>
  <body>
    <h1>About Acme Health</h1>
    <p>Acme Health is a specialist content and SEO platform for regulated health organizations that need stronger trust, authorship, and patient-facing clarity.</p>
    <p>Our editorial standards document medical review, update discipline, and clear responsibility for every clinical content program we support.</p>
    <a href="/privacy.html">Privacy Policy</a>
    <a href="/terms.html">Terms</a>
    <a href="/contact.html">Contact</a>
  </body>
</html>
""".strip()
            + "\n",
        )
        self._write(
            "team/dr-jane.html",
            """
<!doctype html>
<html>
  <head>
    <title>Dr Jane Smith | Medical Reviewer</title>
    <meta name="description" content="Meet Dr Jane Smith, Acme Health's medical reviewer.">
    <link rel="canonical" href="/team/dr-jane.html" />
    <script type="application/ld+json">
      {"@context":"https://schema.org","@type":"Person","name":"Dr Jane Smith","jobTitle":"Medical Reviewer"}
    </script>
  </head>
  <body>
    <h1>Dr Jane Smith</h1>
    <p>Dr Jane Smith is a practicing physician and medical reviewer who validates health content accuracy, safety, and evidence quality.</p>
  </body>
</html>
""".strip()
            + "\n",
        )
        self._write(
            "services/seo-audit.html",
            """
<!doctype html>
<html>
  <head>
    <title>Clinic SEO Audit Service | Acme Health</title>
    <meta name="description" content="A patent-aware clinic SEO audit for trust, entity clarity, and AI visibility.">
    <link rel="canonical" href="/services/seo-audit.html" />
  </head>
  <body>
    <h1>Clinic SEO Audit Service</h1>
    <p>Our clinic SEO audit translates trust, expert identity, and patient-intent signals into a practical action plan.</p>
    <p>Request a demo to review your clinic site, surface weak destination pages, and fix extractability issues before they limit visibility.</p>
    <a href="/contact.html">Request demo</a>
  </body>
</html>
""".strip()
            + "\n",
        )
        self._write(
            "pricing.html",
            """
<!doctype html>
<html>
  <head>
    <title>Pricing | Acme Health</title>
  </head>
  <body>
    <h1>Acme Health Pricing</h1>
    <p>Choose a monthly plan for entity audits, trust reviews, and content quality monitoring.</p>
    <p>Talk to sales for custom health network deployments and multi-clinic governance support.</p>
  </body>
</html>
""".strip()
            + "\n",
        )
        self._write(
            "blog/ai-visibility-guide.html",
            """
<!doctype html>
<html>
  <head>
    <title>AI Visibility Guide For Health Sites | Acme Health</title>
    <meta name="description" content="A practical guide to building health content for AI visibility.">
    <meta name="author" content="Dr Jane Smith">
    <link rel="canonical" href="/blog/ai-visibility-guide.html" />
    <script type="application/ld+json">
      {"@context":"https://schema.org","@type":"BlogPosting","headline":"AI Visibility Guide For Health Sites","author":{"@type":"Person","name":"Dr Jane Smith"}}
    </script>
  </head>
  <body>
    <article>
      <h1>AI Visibility Guide For Health Sites</h1>
      <time datetime="2026-04-01">April 1, 2026</time>
      <p>Health content needs more than generic summaries. Systems prefer passages that are easy to attribute, easy to verify, and clearly connected to a trusted medical entity that can stand behind the advice.</p>
      <p>For example, clinics should connect diagnosis explanations, treatment comparisons, and medical reviewer notes into a consistent topic system so follow-up questions can be grounded without forcing the user back to generic content.</p>
      <ol>
        <li>Define the medical entity and reviewer.</li>
        <li>Expose structured facts and updated dates.</li>
        <li>Connect guidance pages to treatment and clinic trust pages.</li>
      </ol>
    </article>
  </body>
</html>
""".strip()
            + "\n",
        )
        self._write(
            "blog/entity-clusters.html",
            """
<!doctype html>
<html>
  <head>
    <title>Entity Clusters For Clinic Content | Acme Health</title>
    <meta name="description" content="How clinic entity clusters reinforce topic ownership.">
    <link rel="canonical" href="/blog/entity-clusters.html" />
  </head>
  <body>
    <article>
      <h1>Entity Clusters For Clinic Content</h1>
      <time datetime="2026-04-03">April 3, 2026</time>
      <p>Many clinic sites publish pages in isolation and miss the opportunity to reinforce the same expert, service, and condition relationships from page to page. That weakens topic continuity and makes retrieval less confident.</p>
      <p>A stronger cluster connects service pages, condition explainers, expert profiles, and trust pages with explicit internal links, clearer entity repetition, and examples of how real clinical workflows support the advice.</p>
      <ul>
        <li>Link supporting pages from strong hubs.</li>
        <li>Use consistent entity naming.</li>
        <li>Reduce generic boilerplate.</li>
      </ul>
    </article>
  </body>
</html>
""".strip()
            + "\n",
        )
        self._write("privacy.html", "<html><head><title>Privacy</title></head><body><h1>Privacy</h1></body></html>\n")
        self._write("terms.html", "<html><head><title>Terms</title></head><body><h1>Terms</h1></body></html>\n")
        self._write("contact.html", "<html><head><title>Contact</title></head><body><h1>Contact</h1><p>Email support@example.com or call us.</p></body></html>\n")

    def _live_url(self, path: str = "/") -> str:
        return f"{self.base_url}{path}"

    def _rewrite_host_placeholders(self) -> None:
        for path in self.root.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            if "127.0.0.1:1" in text:
                path.write_text(text.replace("127.0.0.1:1", f"127.0.0.1:{self.httpd.server_address[1]}"), encoding="utf-8")

    def test_direct_live_patent_audit(self) -> None:
        self._rewrite_host_placeholders()
        payload = live_patent_seo_audit.audit_site(self._live_url("/"), max_pages=7, timeout=10)
        self.assertEqual(payload["summary"]["site_name"], "Acme Health")
        self.assertGreaterEqual(payload["page_selection"]["fetched_ok"], 6)
        self.assertIn("US20250103662A1", {item["patent_id"] for item in payload["patent_lenses"]})
        self.assertTrue(any(item["selection_reason"] == "about_or_trust" for item in payload["page_selection"]["selected_pages"]))
        self.assertTrue(any(item["selection_reason"] == "commercial" for item in payload["page_selection"]["selected_pages"]))
        self.assertTrue(any(item["audit_type"] == "landing_page_quality" for item in payload["top_findings"]))

    def test_mcp_tool_exposes_live_audit(self) -> None:
        self._rewrite_host_placeholders()
        server = SquadMemoryOsMcpServer(Path("/Users/vijaychauhan/.codex/skills"), Path("/Users/vijaychauhan/squad_memory/task_packs.json"))
        result = server.call_tool(
            "seo_patent_live_audit",
            {
                "url": self._live_url("/"),
                "max_pages": 7,
                "timeout": 10,
            },
        )
        self.assertFalse(result["isError"])
        self.assertIn("Live patent audit: Acme Health", result["content"][0]["text"])
        self.assertEqual(result["structuredContent"]["summary"]["site_name"], "Acme Health")


if __name__ == "__main__":
    unittest.main()
