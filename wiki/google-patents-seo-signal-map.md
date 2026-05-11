---
title: Google Patents — SEO Signal Map
type: wiki
skill: seo
priority: p1
confidence: 0.82
last_updated: 2026-04-08
tags: [patents, google_patents, navboost, ranking_signals, click_behavior, indexing, query_classification, patent_research]
related: [[navboost-behavioral-signals]], [[ai-overview-ranking-factors]], [[sro-selection-rate-optimization]]
gaps: [navboost_patent, hcu_classifier, knowledge_graph_entity, passage_ranking, ai_grounding_patent]
---

# Google Patents — SEO Signal Map

## How to use this article
Patent evidence is **directional, not operational proof**. Use it to sharpen hypotheses, not to claim a patent = a live ranking factor. The best patents expose score modification logic, query-to-document mapping, click-log aggregation, and snippet-generation — things that align with observable SEO behavior.

**Key rule:** When a patent claim aligns with a reproducible SEO test result, the combination is worth acting on. A patent alone is not enough.

## Current patent coverage (last harvested: 2026-04-03)
- **Queries succeeded:** search ranking, ranking search results, query click logs, query classification, search snippets, document scoring, site quality, indexing engine, reference queries, user navigation ranking adjustment, implicit feedback navigation
- **Queries that 503'd (gap):** navboost click signal, language model grounding search, generative search grounding, helpful content classifier, knowledge graph entity search, passage ranking/retrieval, multi-task unified model
- **Patents captured:** 12 SEO-relevant (filtered from 25; 13 removed as non-SEO)

## High-value patents by theme

### Click Behavior & NavBoost-adjacent
**US11816114B1** — Modifying search result ranking based on implicit user feedback
- Inventors: Hyung-Jin Kim, Simon Tong, Noam Shazeer, Michelangelo Diligenti
- Published: 2023-11-14 | Priority: 2006-11-02
- Core mechanism: relevance-ratio framework — long-view vs short-view click satisfaction adjusts base ranking scores using resource-group score-modifier logic
- SEO signal: **behavioral feedback loops modify ranking continuously, not just at crawl time**
- Family note: this continuation applies to speech input and audio — shows the framework is multimodal

**US9811566B1** — Modifying search result ranking based on implicit user feedback (earlier)
- Published: 2017-11-07 | Same inventor family as above
- Confirms the same implicit feedback framework has been live since at least 2006

### Query Classification & Understanding
**US20250124076A1** — Query Categorization Based on Image Results
- Inventor: Anna Majkowska | Published: 2025-04-17 | Priority: 2009-12-29
- Core mechanism: adjusts weights on example queries based on comparing query classification against correct categorization
- SEO signal: **query classification determines which documents enter the candidate set at all** — intent misclassification = no retrieval, not just lower ranking

### Snippet Generation
**US9619565B1** — Generating content snippets using a tokenspace repository
- Inventor: Jeffrey Dean | Published: 2017-04-11 | Priority: 2004-08-13
- Core mechanism: tokenspace-based snippet generation from indexed document content
- SEO signal: **snippet text is generated from tokenized content, not raw HTML** — implications for how structured vs unstructured content gets excerpted
- Connection to grounding: same tokenspace logic likely feeds modern grounding chunk selection

### Document Scoring & Ranking Modifiers
**US10394830B1** — Sentiment detection as a ranking signal for reviewable entities
- Published: 2019-08-27 | Priority: 2007-12-05
- Core mechanism: ranking reviewable entities based on sentiment in review texts
- SEO signal: **review sentiment = ranking signal for local/review-heavy pages**

**US10095752B1** — Clustering news content + cluster-level scoring
- Published: 2018-10-09 | Priority: 2002-09-20
- Core mechanism: document score influenced by cluster-level parameters (document, source, cluster score combined)
- SEO signal: **topical cluster authority aggregates upward** — one strong page lifts the cluster score, not just itself

**US9563692B1** — Result-based query suggestions
- Inventor: Paul Haahr | Published: 2017-02-07 | Priority: 2009-08-28
- SEO signal: query suggestions are result-informed — good results drive future query expansion

### Indexing & Crawl Architecture
**US10210256B2** — Anchor tag indexing in web crawler
- Published: 2019-02-19 | Priority: 2003-07-03
- Core mechanism: link log pairing source-target documents for anchor indexing
- SEO signal: **anchor text is indexed at crawl time via link logs**, not just at the destination page

**US9788179B1** — Detection and ranking of entities from mobile onscreen content
- Published: 2017-10-10 | Priority: 2014-07-11
- SEO signal: entity detection is part of the indexing pipeline, not a post-ranking layer

## Known patent gaps (data not yet ingested)
These are high-priority areas where we have NO patent-level evidence yet:

| Gap | Why it matters |
|---|---|
| NavBoost click signal patent | Core behavioral ranking mechanism — all 503'd in harvest |
| HCU / helpful content classifier | Quality signal for post-HCU recovery strategy |
| Knowledge Graph entity search | Entity authority + brand association signals |
| AI grounding / LLM search results | Direct evidence for AI Overview ranking mechanics |
| Passage ranking (US11615148B2) | Passage-level indexing = chunk-level grounding connection |

**Action:** When user provides direct patent data, ingest these 5 areas first via Nautilus.

## How to query this knowledge
For any ranking hypothesis, check:
1. Is there a patent that confirms the mechanism?
2. Is there a DEJAN study that empirically observed it?
3. Is there a GSC signal (CTR, impressions, position change) correlating with the behavior?

All three = act on it. Patent alone = hypothesis only.
