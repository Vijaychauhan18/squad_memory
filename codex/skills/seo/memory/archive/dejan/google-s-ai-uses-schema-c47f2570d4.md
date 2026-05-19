---
source: https://dejan.ai/blog/googles-ai-schema/
title: Google’s AI Uses Schema?
scraped: 2026-03-25
published_on: 2025-12-19
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

# Google’s AI Uses Schema?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/googles-ai-schema/
Published: 2025-12-19
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Article updated thanks to a sharp observation from Lukasz Rogala who makes my claim less certain and putting us back in the “needs more evidence category”. There’s some evidence Google uses structured data to ground Gemini in its AI search. If true this is good news for AI SEO people and vindication for schema advocates […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Article updated thanks to a sharp observation from Lukasz Rogala who makes my claim less certain and putting us back in the “needs more evidence category”.

There’s some evidence Google uses structured data to ground Gemini in its AI search. If true this is good news for AI SEO people and vindication for schema advocates in the industry.

The above prompt and associated fanout queries returned five final grounding sources:

Each source page was scraped and chunked. Each chunk was then scored against the prompt using a cross-encoder.

The idea was to compare the prediction against actual grounding chunks forming the RAG snippet for each page. See how accurate our model is.

Then I found an outlier initially dismissed as hallucination:

Then I saw it in the SERPs and I knew it wasn’t model-hallucinated:

I clicked on “read more” but it didn’t land on the exact text chunk from the grounding:

Lukasz Rogala makes an excellent point, if anyone wants to run a test against this and let us know:

I’ve always claimed that hidden content doesn’t do well in search and still stand by this, but it’s very likely that Google took the segment from the hidden part of the page instead of schema.

If true the real story here is “ Google’s RAG pipeline includes valid hidden content such as expanders, tabs and accordions. “

The problem: If the same sentence exists in both places, you can’t isolate which source Gemini is using.

Quick test idea: Do you have control over a test page? You could:

The scoring of grounding chunks was done using: https://dejan.ai/tools/snippets/

Perhaps it would be appropriate to block the rendering of this element and leave only JSON-LD for the FAQ schema.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
