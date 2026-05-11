---
title: SRO — Selection Rate Optimization
type: wiki
skill: dejan-ai-reverse-engineering
priority: p1
confidence: 0.91
last_updated: 2026-04-08
tags: [sro, selection_rate, ai_overview, grounding, dejan, ai_search]
related: [[query-fan-out-mechanics]], [[grounding-chunk-optimization]], [[ai-overview-ranking-factors]]
---

# SRO — Selection Rate Optimization

## What it is
SRO (Selection Rate Optimization) is DEJAN's AI-native successor to CTR optimization. Where CTR measures clicks on a blue link, SRO measures how often your content is **selected as a grounding source** inside an AI answer.

Ranking #1 does not mean you get selected. Getting selected does not require ranking #1.
These are two separate dashboards. Treat them separately.

## The core distinction
| Classic SEO | AI-native SEO (SRO) |
|---|---|
| Optimize for ranking position | Optimize for grounding selection |
| Track clicks | Track citation frequency |
| CTR as signal | Selection rate as signal |
| Full page indexed | ~1/3 of page survives extraction |
| User reads your page | LLM reads a distilled fragment |

## Why ~1/3 of your page survives
DEJAN's Nov 2025 study: roughly one third of page content survives into cited grounding text. Google/Gemini use DomDistiller-style extraction — reader-mode stripping of nav, ads, footers, hidden content, and decorative text. What remains is the main content block only.

**Operational rule:** Identify the exact sentence blocks likely to survive extraction — not the whole article.

## How to improve SRO on a page
1. **Front-load the answer** — put the grounding-worthy sentence in the first 2 lines of each section, not buried in narrative setup
2. **Self-contained blocks** — each section must make sense if extracted alone, stripped of the surrounding page
3. **Short, factual, explicit claims** — vague statements don't get selected; precise claims do
4. **Visible by default** — content in tabs, accordions, or JS-rendered blocks has lower survival rate through DomDistiller
5. **Avoid duplicate clusters** — canonical confusion redistributes selection weight across competing pages

## How to measure it
- Compare ranking position against actual grounded snippets or citations
- Measure what % of your source page appears in cited text
- Use multiple prompt variants — fan-out means different sub-queries select different chunks
- Rewrite candidate passages as short factual blocks and retest selection

## Separate transient from durable wins
Grounding is transient — it is not stored in the model's weights. Every query is re-grounded.
Brand bias (primary bias) is durable — it lives in the model's latent associations.

Optimizing SRO = winning the transient layer.
Building brand authority = winning the durable layer.
Both matter. Neither substitutes for the other.

## Sources (DEJAN)
- SRO & Grounding Snippets (2026-03-01)
- How much of your content survives the AI Search filter? (2025-11-08)
- What extraction method is Google using to build grounding snippets? (2026-02-24)
- In AI SEO #10 is the new #1 (2025-11-09)
