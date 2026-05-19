---
title: "Google Patent WO2024064249A1 — Prompt-Based Query Generation for Diverse Retrieval"
skill: seo
type: patent
patent_id: WO2024064249A1
assignee: Google LLC
published: 2024-03-28
filed: 2023-09-21
priority: p1
confidence: 0.87
tags: [patents, query_fan_out, synthetic_queries, retrieval, topical_authority, entity_coverage]
related: [[google-patent-us20240289407a1-stateful-chat]], [[google-patent-us12189697-informational-grounding]]
---

# Google Patent WO2024064249A1 — Prompt-Based Query Generation for Diverse Retrieval (PROMPTAGATOR)

## What it covers
Uses an LLM to generate synthetic query-document training pairs from a small number of seed examples, then trains a task-specific retrieval model on them. Enables effective retrieval with minimal labelled data. Underpins how AI search systems fan out to multiple sub-queries from a single user input.

## Core mechanism
1. Seed examples (few query-document pairs) provided to LLM
2. LLM generates diverse synthetic training pairs covering the topic space
3. Task-specific retrieval model trained on synthetic data
4. Retrieval model used to find relevant documents for novel queries

## SEO signals
- **Topic breadth determines retrieval candidacy** — a page only covering the exact search term may miss the synthetic sub-queries generated for retrieval
- **Entity coverage at the page level matters** — pages that cover related entities, sub-topics, and related questions have higher probability of appearing in any synthetic query sweep
- **Sparse coverage = retrieval gaps** — a site with thin topical coverage is systematically excluded from diverse retrieval even if its primary keyword ranking is strong

## Practitioner implication
This is patent-level confirmation of the "topic cluster" model. A single page ranking for a keyword is not enough — the surrounding content ecosystem determines whether your site is retrieved at all for AI-search query fan-out. Internal linking between related pages helps retrieval models find the full topic.

## URL
https://patents.google.com/patent/WO2024064249A1
