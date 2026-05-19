---
source: https://dejan.ai/blog/better-clustering/
title: Better Vector Clustering With Head Noun Extraction
scraped: 2026-03-25
published_on: 2025-11-28
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

# Better Vector Clustering With Head Noun Extraction

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/better-clustering/
Published: 2025-11-28
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Let’s do a mental exercise. Glance over the following list and group them in your mind: Most people arrive at the following clustering schema: Socks Laptops Bulldozers blue thermal socks cheap gaming laptops cheap diesel bulldozer cheap ankle socks blue lightweight laptops blue rental bulldozer used cushioned socks used touchscreen laptops blue compact bulldozer cheap […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Note: In the above example we’re using MRL 256 to reduce dimensionality.

After that we’ll cluster them by similarity of their embeddings. In this specific example we’ll use FAISS index which builds implicit clusters represented as Voronoi cells each one with a “topical centroid”.

Standard embeddings create a “semantic soup.” The vector for “cheap laptop” is a mathematical average of “cheap” and “laptop.” Because “cheap” is a very strong concept, it pulls the vector towards other “cheap” things, ignoring the physical object.

Obviously it’s not all as simple as the above example, our large-scale NLP analysis of search queries reveals a wide variety of patterns:

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
