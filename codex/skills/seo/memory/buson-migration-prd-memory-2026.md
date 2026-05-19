---
source: /Users/vijaychauhan/.gemini/antigravity/brain/06286b5a-e5e2-4498-99c8-e1cf2091d46e/Master_Buson_SEO_PRD.md, /Users/vijaychauhan/.gemini/antigravity/brain/06286b5a-e5e2-4498-99c8-e1cf2091d46e/Buson_Technical_SEO_Elements_PRD.md, /Users/vijaychauhan/.gemini/antigravity/brain/06286b5a-e5e2-4498-99c8-e1cf2091d46e/Buson_URL_Architecture_PRD.md, /Users/vijaychauhan/.gemini/antigravity/brain/06286b5a-e5e2-4498-99c8-e1cf2091d46e/Buson_Comprehensive_SEO_PRD.md
title: Buson Migration PRD Memory
scraped: 2026-04-21
tags: buson, busbud, migration, prd, url architecture, robots, sitemaps, redirects, ssr, schema, breadcrumbs
topic: buson_migration, technical_seo
intent: implementation_review, technical_seo, migration_planning
role: chitin, coral, pinchy, reef
confidence: high
canonical: true
canonical_group: Buson migration
use_for: migration_requirements, redirect_logic, crawl_management, sitemap_logic, ssr_requirements
avoid_for: post_migration_content_briefs, generic_metadata_only_tasks
---

# Buson Migration PRD Memory

## Core Concept
This is the reusable architecture note for the migration of `buson.com.br` onto the Busbud stack. Use it when the task touches URL architecture, crawl management, redirects, SSR, sitemap rules, breadcrumbs, or domain-level technical SEO requirements.

## Most Important Reusable Rules
- Buson indexation thresholds are per-domain, not per-locale.
- Route pages use a demand-gated indexation model plus a 90-day grace period.
- Only canonical `200 OK` pages belong in sitemaps.
- Legacy URLs must use strict one-hop `301` redirects, never vague homepage redirects or `302`s.
- Core SEO content must be server-rendered; Googlebot should not need client-side rendering just to understand the page.

## URL Architecture To Remember
- Supported core patterns include homepage, city pages, route pages, operator pages, station pages, support/info pages, and new country/state hub pages.
- New migration-specific hubs:
  - `/p/[country-slug]`
  - `/e/[state-slug]`
- Unknown or infra-only paths such as `/t/...`, `/pagamento/`, and `/cdn-cgi/...` should not accidentally enter the SEO layer without explicit handling.

## Crawl and Robots Rules
- `robots.txt` must live at the root and allow rendering assets such as `/_next/static/`.
- API, login, checkout, and parameter crawl traps must be blocked.
- Search/filter parameter explosions must not consume crawl budget.

## Sitemap Rules
- Use a sitemap index plus chunked sub-sitemaps.
- Enforce the `50,000 URL / 50MB` rule.
- Break out core pages, hubs, operators, stations, and routes.
- Remove noindexed, redirected, broken, or non-canonical URLs from sitemap output.

## Redirect Rule
- Build a strict old-to-new mapping table.
- Use one-hop `301`s`.
- Preserve route, operator, and station equivalence whenever possible.
- Never collapse unknown legacy SEO URLs to the homepage by default.

## Rendering and Structured Data Rules
- Important body content, headings, meta tags, and internal links must be in the initial HTML.
- Use JSON-LD, not scattered markup styles.
- Organization and WebSite/SearchAction schema belong on the homepage.
- Breadcrumbs must be visible and backed by valid `BreadcrumbList` schema.

## Performance and Quality Rules
- Treat Core Web Vitals as launch requirements, not cleanup items.
- Keep LCP, CLS, and INP within target ranges.
- Prevent hydration mismatches and layout shifts on critical templates.

## When To Load This Note
- Buson migration rollout planning
- redirect mapping reviews
- robots and sitemap audits
- SSR and JavaScript SEO checks
- breadcrumb and schema implementation reviews























































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Master-Buson-Seo-Prd-Md-Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Buson-Technical-Seo-Elements-Prd-Md-Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Buson-Url-Architecture-Prd-Md-Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Buson-Comprehensive-Seo-Prd-Md

### Cross-Source Signals
- **Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Master-Buson-Seo-Prd-Md-Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Buson-Technical-Seo-Elements-Prd-Md-Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Buson-Url-Architecture-Prd-Md-Users-Vijaychauhan-Gemini-Antigravity-Brain-06286B5A-E5E2-4498-99C8-E1Cf2091D46E-Buson-Comprehensive-Seo-Prd-Md**: This is the reusable architecture note for the migration of `buson.com.br` onto the Busbud stack. Use it when the task touches URL architecture, crawl management, redirects, SSR, sitemap rules, breadcrumbs, or domain-level technical SEO requirements.

### Consensus
- Sources converge that `buson migration, technical seo` should be treated as a repeatable operating concern, not a one-off tactic.

### Tension / Caveat
- No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon.

### Squad Action
- Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.
<!-- phase10:end -->
