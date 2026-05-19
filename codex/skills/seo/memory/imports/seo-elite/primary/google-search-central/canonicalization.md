---
source: https://developers.google.com/search/docs/crawling-indexing/canonicalization
title: What is canonicalization
scraped: 2026-05-18
tags: google, official, canonicalization, duplicates, url_selection
topic: canonicalization
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: Google’s current baseline on duplicate clustering and canonical selection
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# What is canonicalization

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/canonicalization
Page updated label: 2025-12-10 UTC

## Why This Matters
Google’s current baseline on duplicate clustering and canonical selection

## Extracted Passages
- Canonicalization is the process of selecting the representative – canonical – URL of a piece of content. Consequently, a canonical URL is the URL of a page that Google chose as the most representative from a set of duplicate pages. Often called deduplication, this process helps Google show only one version of the otherwise duplicate content in its search results.
- Some duplicate content on a site is normal and it's not a violation of Google's spam policies . However, having the same content accessible through many different URLs can be a bad user experience (for example, people might wonder which is the right page, and whether there's a difference between the two) and it may make it harder for you to track how your content performs in search results.
- When Google indexes a page , it determines the primary content (or centerpiece ) of each page. If Google finds multiple pages that seem to be the same or the primary content very similar, it chooses the page that, based on the factors (or signals ) the indexing process collected, is objectively the most complete and useful for search users, and marks it as canonical. The canonical page will be crawled most regularly; duplicates are crawled less frequently in order to reduce the crawling load on sites.
- There are a handful of factors that play a role in canonicalization: whether the page is served over HTTP or HTTPS, redirects, presence of the URL in a sitemap, and rel="canonical" link annotations. You can indicate your preference to Google using these techniques, but Google may choose a different page as canonical than you do, for various reasons. That is, indicating a canonical preference is a hint, not a rule.
- Different language versions of a single page are considered duplicates only if the primary content is in the same language (that is, if only the header, footer, and other non-critical text is translated, but the body remains the same, then the pages are considered to be duplicates). To learn more about setting up localized sites, see our documentation about managing multi-lingual and multi-regional sites .
- Google uses the canonical page as the main source to evaluate content and quality. A Google Search result usually points to the canonical page, unless one of the duplicates is explicitly better suited for a search user. For example, the search result will probably point to the mobile page if the user is on a mobile device, even if the desktop page is the canonical.
- Read more about how to indicate your preference for the canonical URL, and whether you need to .
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

