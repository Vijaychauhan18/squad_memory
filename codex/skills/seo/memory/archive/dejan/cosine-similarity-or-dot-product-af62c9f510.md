---
source: https://dejan.ai/blog/cosine-similarity-or-dot-product/
title: Cosine Similarity or Dot Product?
scraped: 2026-03-25
published_on: 2025-06-19
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

# Cosine Similarity or Dot Product?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/cosine-similarity-or-dot-product/
Published: 2025-06-19
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Google’s embedder uses dot product between normalized vectors which is computationally more efficient but mathematically equivalent to cosine similarity. How Googler’s work and think internally typically aligns with their open source code (Gemini -> Gemma) and Chrome is no exception. It’s why I look there for answers and clarity on Google’s machine learning approaches. After […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

How Googler’s work and think internally typically aligns with their open source code (Gemini -> Gemma) and Chrome is no exception. It’s why I look there for answers and clarity on Google’s machine learning approaches.

After examining the Chrome codebase, I found the following key evidence regarding the similarity method used:

The core similarity calculation is implemented in the ScoreWith method of the Embedding class in vector_database.cc :

This implementation is calculating the dot product of two embedding vectors.

The code shows that embeddings are normalized to unit length:

And in the FindNearest method in VectorDatabase , there’s a check to ensure the query embedding has unit magnitude:

There are no direct references to “cosine” or “cosine similarity” in the codebase.

Based on the evidence, the code is using dot product between normalized vectors for similarity calculation.

When vectors are normalized to unit length (magnitude = 1), the dot product is mathematically equivalent to cosine similarity. This is because:

When |A| = |B| = 1 (normalized vectors), this simplifies to:

Therefore, the code is effectively implementing cosine similarity by:

This approach is computationally more efficient than calculating the full cosine similarity formula, as it avoids the division operation while producing the same result for normalized vectors.

The archive contains a Chromium component called history_embeddings that implements a service for embedding and searching browser history using vector embeddings.

The component implements a semantic search system for browser history that:

The approach is effective and computationally efficient. Sounds like Google to me.

With impact of vector magnitudes on similarity score, are there scenarios where using dot-product might accidentally exaggerate similarity, like for vectors with large magnitudes? Or are web content/passage embeddings too few dimensions to worry about that?

Absolutely. If direction is more important than intensity, use cosine similarity or normalize embeddings before computing dot-product.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
