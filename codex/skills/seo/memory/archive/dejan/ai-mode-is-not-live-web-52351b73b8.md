---
source: https://dejan.ai/blog/ai-mode-is-not-live-web/
title: AI Mode is Not Live Web
scraped: 2026-03-25
published_on: 2025-05-29
tags: live_feed, phase1_ingest, dejan, practitioner, reverse-engineering, grounding, archive_backfill, historical_source
topic: ai_reverse_engineering
intent: research, monitoring, source_selection, ai_selection
role: researcher, seo, pinchy
confidence: high
canonical: false
canonical_group: Archive backfill - DEJAN / Dan Petrovic
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# AI Mode is Not Live Web

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/ai-mode-is-not-live-web/
Published: 2025-05-29
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
I recently stumbled upon a fascinating aspect of how Google’s AI Mode (powered by a custom Gemini model) interacts with the internet. I ran a simple test, and the results suggest that instead of performing truly live fetches for all URLs, the AI Mode relies on Google’s existing index or a cached version of the […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

I recently stumbled upon a fascinating aspect of how Google’s AI Mode (powered by a custom Gemini model) interacts with the internet. I ran a simple test, and the results suggest that instead of performing truly live fetches for all URLs, the AI Mode relies on Google’s existing index or a cached version of the web. This can lead to some surprising discrepancies when dealing with brand-new or unindexed content.

First, I disabled the use of search_tool and made AI Mode run python code in its local environment.

I repeated the test with another file (test.php) and replicated the test successfully.

The key takeaway for me was the stark difference in how AI Mode handled the newly created page:

However, for a page that is likely already known to Google (indexed or cached), the AI Mode correctly fetched and reported its status and content.

This strongly suggests to me that when Google’s AI Mode (or its Python execution environment) attempts to access a URL, it doesn’t necessarily perform a fresh, live HTTP request to the target server every single time. It seems more likely that it first consults Google’s vast index or a cached representation of the web.

[…] tests show that Google’s AI Mode doesn’t retrieve page content from the live web but somewhere else, and that “somewhere else” appears to be a proprietary content store […]

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
