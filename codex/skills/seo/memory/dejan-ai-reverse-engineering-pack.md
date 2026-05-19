---
source: dejan.ai, dejanmarketing.com
title: DEJAN AI Reverse Engineering Pack
scraped: 2026-03-20
tags: ai reverse engineering, grounding, selection rate, ai mode, fan out, machine readability
topic: ai_reverse_engineering
intent: diagnosis, reverse_engineering, ai_selection, ai_search
role: pinchy, coral, researcher
confidence: high
canonical: true
canonical_group: AI reverse engineering
use_for: grounding_snippets, selection_rate, ai_mode, fan_out, machine_readability
avoid_for: generic_link_building, customer_support
---

# DEJAN AI Reverse Engineering Pack

Source snapshot date: 2026-03-20
Primary sources: `dejan.ai`, `dejanmarketing.com`

## Core Thesis

Use DEJAN when the task is about AI-search reverse engineering rather than generic SEO advice. The pack is strongest on grounding behavior, snippet selection, hidden query fan-out, AI Mode/tool orchestration, machine-readable extraction, and older technical SEO heuristics that still explain modern retrieval failures.

## What This Adds To The SEO Library

- A `selection rate` lens instead of rank-only thinking.
- A grounding-first diagnostic workflow: which snippet survives, gets selected, and shapes the answer.
- A system view of AI search as retrieval plus routing plus tool use plus synthesis.
- Browser/client-code reverse engineering as a proxy for chunking and extractability.
- A legacy DEJAN layer for hidden content, canonicals, duplicate handling, trust cues, and link context.

## Use It When

- You need to reverse engineer Google AI Mode, AI Overviews, Gemini grounding, citations, or snippet extraction.
- A page ranks but is not being cited or selected.
- You need a checklist for differentiating retrieval failure, routing failure, selection failure, and synthesis failure.
- You want historical DEJAN heuristics to explain visibility issues before blaming the model.

## Highest-Signal DEJAN Ideas

- `SRO` = Selection Rate Optimization.
- Grounding is selective and transient.
- Ranking and selection are different layers.
- Hidden fan-out queries matter.
- AI search products behave like orchestrated tool systems.
- Browser and client code can expose real chunking/embedding constraints.
- Older technical SEO issues still affect AI visibility because LLM layers inherit retrieval constraints.

## Local Detailed References

- `~/.codex/memories/dejan-ai-reverse-engineering-2026-03-20.md`
- `~/.codex/skills/dejan-ai-reverse-engineering/references/dejan-ai-notes.md`
- `~/.codex/skills/dejan-ai-reverse-engineering/references/dejan-models-and-systems.md`
- `~/.codex/skills/dejan-ai-reverse-engineering/references/dejan-legacy-technical-seo.md`
- `~/.codex/skills/dejan-ai-reverse-engineering/references/reverse-engineering-checklist.md`

## Squad Use Angle

- Pair with `ahrefs-ai-visibility-guide.md` for operating-system level AI visibility strategy.
- Pair with `hobo-google-leak-decoded.md` and `hobo-navboost.md` when you need leak-era system framing.
- Use this DEJAN note when the work is more experimental, diagnostic, or reverse-engineering heavy than the Ahrefs/Hobo notes alone.































































































































<!-- phase9:begin -->
## Canonical Synthesis

This canonical note is reinforced by 1 merge candidate(s) and 6 supporting note(s) in the local memory library.

### Supporting Note Digest
- `dejan-sro-grounding-snippets.md`: Source: dejan.ai/blog/category/ai-seo/sro/Author: Dan Petrovic, DEJAN AIPosts analyzed: 5 (Sep 2025 – Feb 2026) What is SRO? SRO — Selection Rate Optimization — is a new discipline coined by DEJAN that addresses visibility in AI-powered search (Google AI Mode, Gemini Chat, AI Ove.
- `dejan-search-grounding-is-transient.md`: There is a fundamental misconception about how Google’s AI search and Gemini chatbot process retrieved web content. It is widely understood that these systems use Retrieval-Augmented Generation (RAG) to search the web, pull snippets from pages, and ground their answers in factual.
- `dejan-rufus-under-the-hood-what-drives-amazon-s-ai-shopping-assistant.md`: What’s Publicly Known About the Pipeline, Backend, and Response Anatomy. Rufus is not “one model that magically answers.” Public Amazon/AWS descriptions point to a multi-component system: Speculative schema: Pipeline: request → answer Step A — Input + context assembly Public desc.
- `dejan-reverse-prompting-reconstructing-prompts-from-ai-generated-text.md`: We fine-tuned Google’s Gemma 3 (270M) to reverse the typical LLM workflow: given an AI-generated response, the model reconstructs the most likely prompt that produced it. We generated 100,000 synthetic prompt-response pairs using Gemini 2.5 Flash, trained for a single epoch on a.
- `dejan-is-query-length-a-reliable-predictor-of-search-volume.md`: The answer is no. There’s a widely held intuition in SEO and ecommerce search: short queries have high volume, long queries have low volume. “laptop” gets millions of searches. “left handed ergonomic vertical mouse wireless” does not. It feels obvious. But is query length actuall.
- `dejan-fanout-query-analysis.md`: When AI models like Gemini, GPT or Nova answer a question using web search, they don’t just run your query as-is. They generate their own internal search queries, or fanout queries. A single user prompt can trigger multiple fanout queries as the model breaks down the question, ex.
- `ahrefs-query-fan-out.md`: Query fan-out is a technique used by AI search platforms (Google AI Overviews, Perplexity, ChatGPT Search) that automatically expands a single user query into multiple sub-queries to generate more comprehensive answers. When someone searches "best AI tools for marketing", the AI may fan out into 5–10 hidden sub-queries before synthesizing an answer.

### Retrieval Guidance
- Start with this note for the topic baseline and open the supporting notes only when you need source-specific evidence or edge cases.
- Use the attached digest to avoid re-reading overlapping notes during planning and research.
<!-- phase9:end -->



























































































































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: high
Freshness status: current
Distinct sources: Ahrefs, DEJAN

### Cross-Source Signals
- **Ahrefs**: Query fan-out is a technique used by AI search platforms (Google AI Overviews, Perplexity, ChatGPT Search) that automatically expands a single user query into multiple sub-queries to generate more comprehensive answers. When someone searches "best AI tools for marketing", the AI may fan out into 5–10 hidden sub-queries before synthesizing an answer.
- **DEJAN**: DEJAN AI Reverse Engineering Pack.

### Consensus
- The strongest notes agree that AI answer selection depends on retrieval fit, grounding, and sub-query expansion, not only rank position.
- Reverse-engineering work is most useful when it explains why a page is selected, not just whether it ranks.
- Recurring source signals: dejan, ai-reverse-engineering.

### Tension / Caveat
- Platform behavior changes quickly, so reverse-engineering notes are powerful but should be checked against fresh source behavior before making hard bets.

### Squad Action
- Use this canon first for AI Mode, fan-out, grounding, and selection questions before opening raw reverse-engineering notes.
<!-- phase10:end -->
