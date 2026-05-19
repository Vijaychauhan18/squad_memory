---
title: "Google Patent WO2025102041A1 — User Embedding Models for Personalization of Sequence Processing Models"
skill: seo
type: patent
patent_id: WO2025102041A1
assignee: Google LLC
published: 2025-05-15
filed: 2024-11-11
priority: p1
confidence: 0.88
tags: [patents, personalization, user_embeddings, llm_prompting, user_signals, ranking]
related: [[google-patent-us11875086b2-user-input-adapt-results]], [[navboost-behavioral-signals]]
---

# Google Patent WO2025102041A1 — User Embedding Models for Personalization

## What it covers
Compresses long user history into compact learned embeddings (vectors) that are injected as soft prompts into an LLM. Enables personalised search and generative responses without passing the full raw history as tokens. Allows modelling significantly longer histories than text-based methods permit — potentially years of user behaviour.

## Core mechanism
1. User interaction history (queries, clicks, dwell, accepted results) → embedding model
2. Compact user embedding generated (history compressed, not truncated)
3. Embedding injected as soft prompt tokens at the front of every LLM inference call
4. LLM's output is conditioned on both the query and the user's compressed history

## SEO signals
- **Long-horizon user history is now a live ranking input** — not just recent session signals but potentially months of behaviour affect what gets shown
- **Repeated positive engagement with a domain boosts future citations for that user** — brand recall and return visits matter mechanically
- **New users see different results** — a page that ranks well for new users may be demoted for users with established topic history elsewhere

## Practitioner implication
Brand-building and direct return traffic are not just soft signals — this patent confirms they feed a measurable ranking embedding. Sites that earn repeat visits from the same users build compounding ranking advantages for those users. Newsletter lists and direct traffic are SEO assets.

## URL
https://patents.google.com/patent/WO2025102041A1
