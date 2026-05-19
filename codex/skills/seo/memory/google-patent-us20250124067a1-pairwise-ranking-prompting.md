---
title: "Google Patent US20250124067A1 — Method for Text Ranking with Pairwise Ranking Prompting"
skill: seo
type: patent
patent_id: US20250124067A1
assignee: Google LLC
published: 2025-04-17
filed: 2024-10-11
priority: p1
confidence: 0.90
tags: [patents, pairwise_ranking, llm_ranking, information_gain, ranking_signals, content_differentiation]
related: [[google-patent-us20200349181a1-information-gain]], [[ai-overview-ranking-factors]]
---

# Google Patent US20250124067A1 — Text Ranking with Pairwise Ranking Prompting

## What it covers
Instead of assigning absolute relevance scores, an LLM is prompted to compare two candidate documents head-to-head against the query. Pairwise judgments are aggregated into a final ranking. Supports both generation mode and probability-scoring mode. Order-insensitive design makes it more robust than pointwise scoring.

## Core mechanism
1. Retrieve a candidate set of documents for a query
2. LLM receives a prompt: "Given query Q, is Document A or Document B more relevant?"
3. Multiple pairwise comparisons aggregated (e.g. tournament-style)
4. Final ranking derived from aggregated pairwise wins
5. Order-insensitive: result is stable regardless of presentation order

## SEO signals
- **Information gain is a direct competitive advantage** — a document with unique, specific information wins head-to-head against a generic page on the same keyword
- **Differentiation beats optimisation** — keyword density, header structure, and on-page signals are less predictive when two pages are being directly compared on substance
- **Generic pages lose by construction** — if two pages cover the same topic, the one with more specific data, examples, or unique analysis wins every comparison

## Practitioner implication
This is the strongest patent confirmation yet that information gain is a real ranking lever. Stop adding "comprehensive" sections that repeat what competitors say. Add something they don't have: original data, specific numbers, counter-intuitive findings, or a unique framework.

## URL
https://patents.google.com/patent/US20250124067A1
