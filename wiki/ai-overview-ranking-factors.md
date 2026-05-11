---
title: AI Overview Ranking Factors — Full Playbook
type: wiki
skill: seo
priority: p1
confidence: 0.88
last_updated: 2026-04-08
tags: [ai_overview, grounding, selection_rate, navboost, eeat, fan_out, sro, ranking_factors]
related: [[sro-selection-rate-optimization]], [[query-fan-out-mechanics]], [[grounding-chunk-optimization]], [[google-patents-seo-signal-map]]
---

# AI Overview Ranking Factors — Full Playbook

## The two-layer model
AI Overview visibility is NOT a single ranking. It is two separate competitions:

```
Layer 1 — RETRIEVAL (classic SEO)
  ↓ Is your page in the retrieval candidate pool?
  ↓ Ranking, indexing, crawl health, NavBoost signals

Layer 2 — SELECTION (AI-native SEO)
  ↓ Is your specific text selected as a grounding chunk?
  ↓ Content structure, self-contained blocks, DomDistiller survival
```

Winning Layer 1 but losing Layer 2 = you rank #1 but never get cited.
Winning Layer 2 requires deliberate optimization that classic SEO does not cover.

## Layer 1 factors — Retrieval (what gets you into the pool)

### NavBoost signals (behavioral)
Source: Google Leak 2024 + implicit feedback patent family (US11816114B1)
- Dwell time / long clicks — primary positive signal
- Pogo-sticking back to SERP — negative signal
- Return visits to same page — strong positive (indicates satisfied intent)
- CTR relative to position expectation — above/below baseline triggers adjustment
- These signals adjust base ranking scores continuously via resource-group score-modifier logic

**For AI Overviews specifically:** pages with strong NavBoost tend to have higher primary bias — the model's latent preference before grounding begins. Primary bias is durable; grounding selection is transient.

### Technical retrieval requirements
- Page indexed, rendering correctly, no canonical confusion
- Mobile-first indexing: content visible in mobile DOM
- No duplicate clusters on same domain splitting selection weight
- Core Web Vitals: poor LCP/CLS correlates with pogo-stick behavior → NavBoost penalty

### E-E-A-T signals for retrieval eligibility
- Author attribution with named credentials → signals expertise for retrieval classifiers
- Entity recognition: brand/organization entities identified in indexing pipeline (US9788179B1)
- Topical cluster authority: strong cluster lifts individual page retrieval probability (US10095752B1)

## Layer 2 factors — Selection (what gets extracted from your page)

### Content structure (most impactful)
1. **Self-contained sections** — each 200-400 word block makes sense alone
2. **Answer-first sentences** — grounding-worthy claim in line 1, not line 4
3. **Explicit, factual language** — "The visa processing time is 7-10 days" beats "visa timing varies"
4. **FAQ schema** — maps directly to grounding chunk structure, prioritized in selection
5. **No JS-dependent primary content** — DomDistiller doesn't execute JS

### Fan-out coverage (second most impactful)
A single query fans out to 10+ sub-queries. Your page must cover multiple sub-query intents to win multiple citation slots.

Example — "vietnam tour packages" fan-out:
- Explicit: tour packages, itineraries, operators
- Implicit sub-queries: vietnam visa process, best time to visit, cost breakdown, group vs private, safety, vietnam highlights by region

If your page covers only the surface query, you win 1-2 slots. If you cover 5+ sub-queries, you compete for 5+ slots.

### DomDistiller survival factors
- Visible by default — no tabs, accordions, collapsed content for primary info
- Clean semantic HTML — `<h2>`, `<p>`, `<ul>` (reader-mode friendly)
- ~1/3 of page survives extraction on average (DEJAN 2025 study)
- Identify which 1/3 survives on your specific pages and optimize those blocks first

## Primary bias — the durable layer
Primary bias = the model's latent preference for your brand/entity before any grounding happens. It lives in model weights, not in grounding.

Building primary bias:
- Brand mentions across authoritative sources (entity association training signal)
- Consistent E-E-A-T signals across all pages (author, organization, credentials)
- Topical authority depth — being the recognized entity on a topic cluster
- This takes months to shift; it is not a content sprint

Transient grounding wins can be achieved in weeks. Durable primary bias shifts take quarters.

## Diagnostic framework — when you're not appearing in AI Overviews

```
Step 1: Does the query type trigger grounding?
  → Informational/factual = yes | Navigational = rarely | Transactional = sometimes
  → If no: different content strategy needed

Step 2: Are you in retrieval pool?
  → Check ranking for head query and likely fan-out sub-queries
  → If not ranking for sub-queries: content gap problem

Step 3: Is your content surviving DomDistiller?
  → Check: any primary content behind JS/tabs/accordions?
  → Any hidden content issues? (Legacy SEO problem that still kills AI visibility)

Step 4: Are your blocks self-contained and front-loaded?
  → Read each H2 section in isolation. Does it make sense alone?
  → If no: rewrite for grounding structure

Step 5: Is there a duplicate content or canonical issue splitting weight?
  → Multiple pages competing for same query = diluted selection probability
```

## Quick wins checklist
- [ ] Add FAQ schema to all informational pages
- [ ] Rewrite intro of each H2 section — answer in first sentence
- [ ] Identify fan-out sub-queries per target keyword, add dedicated sections
- [ ] Audit for hidden primary content (tabs, accordions) — move to visible
- [ ] Check for duplicate pages competing on same queries → consolidate or canonical
- [ ] Add author attribution with credentials to all pages targeting AI-eligible queries

## Token cost reference
- Full playbook retrieval from wiki: ~700 tokens
- vs. retrieving raw chunks for same question: ~3,200 tokens
- Use this article as the first retrieval result; supplement with raw chunks only if deeper detail needed
