---
source: https://dejan.ai/blog/what-extraction-method-is-google-using-to-build-grounding-snippets/
title: What extraction method is Google using to build grounding snippets?
scraped: 2026-03-22
published_on: 2026-02-24
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

# What extraction method is Google using to build grounding snippets?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/what-extraction-method-is-google-using-to-build-grounding-snippets/
Published: 2026-02-24
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
I’ve been reverse-engineering Google’s Gemini grounding pipeline (AI Mode, Gemini Chat…etc) by examining the raw groundingSupports and groundingChunks returned by the API. Specifically, I’m interested in the snippet construction step, the part where, given a query and a retrieved web page, the system selects which sentences to include in the grounding context supplied to the […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

I’ve been reverse-engineering Google’s Gemini grounding pipeline (AI Mode, Gemini Chat…etc) by examining the raw groundingSupports and groundingChunks returned by the API. Specifically, I’m interested in the snippet construction step , the part where, given a query and a retrieved web page, the system selects which sentences to include in the grounding context supplied to the model.

From examining the extracted sentences against full source content, I’ve observed:

Note: I’ve successfully fine-tuned microsoft/deberta-v3-large and it produces fairly similar results to what Google does. Here’s a demo .

Below: full pipeline diagram, raw grounding snippets, and one source article annotated to show which sentences were extracted (green) vs skipped.

Google’s extractive summarization takes place as part of their model grounding pipeline — the system that connects Gemini’s generative output to real web sources.

When a user enters a prompt, a query fanout model deconstructs it into single-intent queries — essentially a separation of concerns where a multi-faceted prompt is broken into individual dimensions of intent.

For each fanout query, Google’s search index returns a ranked list of relevant results. A selection step narrows these down to a limited set, typically 5–20 sources per query.

Here’s where the extractive summarization happens: for each selected result, the system builds a grounding snippet relative to the specific query. Page content is chunked into sentences, each chunk is scored against the query, and the highest-scoring chunks are assembled into the final snippet — joined by ellipses ( ... ) where non-contiguous. Because the snippet is query-dependent, the same page will yield different extractions for different fanout queries.

The complete set of grounding snippets across all sources is then supplied to the model as grounding context , alongside the user prompt, any attached media, and personalization signals (history, user data, location, time, etc.).

Once the model synthesizes its final answer, each generative claim is supported by one or more grounding sources. Attribution annotation is attached by the system using internal indexation logic — mapping each claim back to specific source sentences.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
