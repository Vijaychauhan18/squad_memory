---
source: https://dejan.ai/blog/does-schema-help-with-ai/
title: Does Schema Help With “AI”?
scraped: 2026-03-25
published_on: 2025-08-23
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

# Does Schema Help With “AI”?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/does-schema-help-with-ai/
Published: 2025-08-23
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
This test is designed to show whether Open AI’s browsing tool does a better job at supplying their model GPT-5 with grounding context from a page with schema. We took the exact HTML from the original experiment here, stripped off the “experiment” from the title and header and uploaded here and here and then ran […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

This test is designed to show whether Open AI’s browsing tool does a better job at supplying their model GPT-5 with grounding context from a page with schema. We took the exact HTML from the original experiment here , stripped off the “experiment” from the title and header and uploaded here and here and then ran some tests.

did browsing tool supply anything from page schema or just plain text?

The browsing tool provided me with only the plain text content from the specified page—there was no structured schema data (like JSON-LD or <meta> schema markup) extracted. I did not retrieve any schema info such as structured data fields or metadata annotations—just the HTML-rendered markdown-style content you saw.

If you’d like, I can look specifically for schema elements (like JSON-LD scripts or other structured markup) by searching or inspecting the raw page. Just let me know if you’d like me to dig deeper.

I used the browsing tool to fetch the raw HTML content exactly as-is. It returned plain text lines—no JSON-LD or page-schema metadata was extracted—just the visible Markdown-style content from that file.

Here’s what I retrieved: standard headings, lists, and textual structure like “Company Details” and “Key Achievements”—but nothing pointing to structured schema data embedded in the page. As far as I can tell, only plain text was available, not structured schema.

Would you like me to check for hidden schema embedded elsewhere (like in the page head or embedded scripts)?

Thanks for doing this Dan. I wonder if the same is true for product pages?

For this to be true they would have to have a tool variant on their browsing tool which contains that capability (e.g. shopping_assistant). As it is now I don’t think it’s designed to supply anything other than clean text.

Makes sense that AI doesn’t trust hidden structured data directly. Unlike Google/Bing, which have years of heuristics for it, AI sticks to visible text.

The real value of structured data is indirect: it enriches Google/Bing/etc snippets (the data GenAI gets from search providers). Supported schema = more data in snippets → potentially better AI visibility?

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
