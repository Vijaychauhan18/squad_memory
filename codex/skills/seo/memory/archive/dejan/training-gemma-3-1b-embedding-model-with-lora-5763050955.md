---
source: https://dejan.ai/blog/gemma-embed/
title: Training Gemma‑3‑1B Embedding Model with LoRA
scraped: 2026-03-25
published_on: 2025-06-27
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

# Training Gemma‑3‑1B Embedding Model with LoRA

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/gemma-embed/
Published: 2025-06-27
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
In our previous post, Training a Query Fan-Out Model, we demonstrated how to generate millions of high-quality query reformulations without human labelling, by navigating the embedding space between a seed query and its target document and then decoding each intermediate vector back into text using a trained query decoder. That decoder’s success critically depends on […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

In our previous post, Training a Query Fan-Out Model , we demonstrated how to generate millions of high-quality query reformulations without human labelling, by navigating the embedding space between a seed query and its target document and then decoding each intermediate vector back into text using a trained query decoder.

That decoder’s success critically depends on having an embedding encoder whose latent geometry is fully under our control: off-the-shelf models (e.g. mxbai embed large) optimize for general semantic similarity, not for invertibility, so their embeddings cannot reliably be mapped back into meaningful queries.

To bridge that gap, this article introduces Gemma-Embed , a bespoke 256-dim embedding model built by fine-tuning google/gemma-3-1b-pt with LoRA adapters and contrastive objectives. By training our own encoder, we lock in a consistent, L2-normalized latent space that the subsequent query decoder can invert with high fidelity.

Together, these steps automate query fan-out, boost retrieval performance, and open the door to interpretable, language-agnostic search suggestions.

To power a query fan‑out decoder that inverts embeddings back to natural language queries, we need an embedding encoder whose latent geometry we control. Since no off‑the‑shelf Gemma‑3 embedding model exists, we fine‑tune google/gemma‑3‑1b‑pt with LoRA and contrastive objectives to produce high‑quality, L2‑normalized 256‑dim embeddings.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
