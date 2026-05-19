---
source: https://dejan.ai/blog/teaching-ai-models-to-be-better-search-engines-a-new-approach-to-training-data/
title: Teaching AI Models to Be Better Search Engines: A New Approach to Training Data
scraped: 2026-03-25
published_on: 2025-02-12
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

# Teaching AI Models to Be Better Search Engines: A New Approach to Training Data

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/teaching-ai-models-to-be-better-search-engines-a-new-approach-to-training-data/
Published: 2025-02-12
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
A recent patent application* reveals an innovative method for training AI models to become more effective at understanding and answering human queries. The approach tackles a fundamental challenge in modern search technology: how to teach AI systems to truly understand what people are looking for, rather than just matching keywords. The Core Innovation The traditional […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

A recent patent application* reveals an innovative method for training AI models to become more effective at understanding and answering human queries. The approach tackles a fundamental challenge in modern search technology: how to teach AI systems to truly understand what people are looking for, rather than just matching keywords.

The traditional way of training search AI requires massive amounts of human-labeled data – real questions paired with their ideal answers. This is expensive, time-consuming, and often limited in scope. The newly proposed method takes a different approach: it uses advanced AI language models to automatically generate diverse, high-quality training examples.

Let’s say the system encounters this passage: “The film follows the story of American scientist John Smith and his role in the development of the elixir of life.”

The technology could improve various real-world applications:

At its core, the patent introduces a novel two-stage distillation process that transforms the traditional approach to training embedding models. This architecture is particularly noteworthy for how it leverages large language models (LLMs) to generate and validate training data.

The first stage employs few-shot prompting of an LLM to generate both tasks and queries. What makes this approach unique is its explicit separation of task description from query generation. The LLM receives a passage and generates two distinct outputs: a task description that defines the type of retrieval required, and a relevant query for that task. This separation allows for much finer control over training data diversity.

The second stage introduces a sophisticated approach to relevance scoring that combines two distinct prompting strategies: Query Likelihood and Relevance Classification. Query Likelihood assesses how likely a passage would generate the given query, while Relevance Classification directly evaluates the relevance of a passage to the query. These scores are combined using Reciprocal Rank Fusion to create a final ranking function.

The model employs a dual-encoder architecture with separate towers for query and document processing. The query tower processes both the task description and the query, while the document tower handles the passage and any associated metadata like titles. This separation allows for efficient retrieval during inference while maintaining the ability to encode rich contextual information.

For multilingual applications, the patent introduces SAP as a novel approach. Instead of direct translation or cross-lingual generation, SAP first creates an extractive summary in the source language, then uses this summary as context for generating queries in target languages. This approach helps maintain semantic coherence across languages while generating natural-sounding queries.

Rather than assuming the seed passage is the optimal answer, the system implements a global ranking strategy to identify potentially better matches. This approach recognizes that the original passage might not be the best answer to the generated query, leading to higher quality training data.

The system employs a two-pronged approach to hard negative mining:

This dual approach helps create more challenging and effective training examples.

The training process utilizes contrastive learning with temperature-scaled similarity scores. The loss function is designed to push query embeddings closer to positive passage embeddings while pulling them away from negative examples, with careful consideration given to batch composition and temperature scaling.

The system’s performance is evaluated on two major benchmarks:

Key metrics include cross-lingual transfer performance, zero-shot generalization capability, retrieval accuracy at various thresholds, and query generation diversity.

*Systems and Methods for Generating Instruction Fine-tuning Dataset for a General Purpose Embedding Model – #20250045316

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
