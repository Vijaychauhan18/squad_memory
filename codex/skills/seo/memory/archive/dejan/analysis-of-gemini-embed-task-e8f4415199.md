---
source: https://dejan.ai/blog/analysis-of-gemini-embed-task-based-dimensionality-deltas/
title: Analysis of Gemini Embed Task
scraped: 2026-03-25
published_on: 2025-07-16
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

# Analysis of Gemini Embed Task

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/analysis-of-gemini-embed-task-based-dimensionality-deltas/
Published: 2025-07-16
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
When generating vector embeddings for your text using Gemini Embed there are several embedding optimisation modes: For each one you get slightly different embeddings, each optimised for the task at hand. The embeddings for semantic similarity are the most unique from all other types while retrieval query, retrieval document and fact verification embeddings are most […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

When generating vector embeddings for your text using Gemini Embed there are several embedding optimisation modes:

For each one you get slightly different embeddings, each optimised for the task at hand.

The embeddings for semantic similarity are the most unique from all other types while retrieval query, retrieval document and fact verification embeddings are most similar to all others.

This is the visual representation of the full spectrum of Gemini’s embedding dimensions for the following sentence:

“DEJAN AI uses mechanistic interpretability to understand how Gemini works.”

Top 10 most variable dimensions across task types (by range):

Top 10 least variable dimensions across task types (by range):

A quick visual inspection immediately gives a clue into just how similar the embeddings are between different task types with only a slight shift in values showing faint but perceptible lanes between the task types.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
