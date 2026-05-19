---
source: https://www.hobo-web.co.uk/perdocdata/
title: The PerDocData: Google's Leaked Core Document Model
scraped: 2026-03-18
tags: perdocdata, google leak, document model, ranking signals, spam signals, freshness, clicks, authority
topic: ranking_architecture
topic_assigned_by: phase9_merge_summaries
topic_assigned_on: 2026-05-19
---

## Core Concept
PerDocData is Google's core per-document data structure revealed in the Content Warehouse leak — it's the "Rosetta Stone" of how Google evaluates every individual document, encompassing authority, semantic understanding, click signals, freshness, and spam demotions in a single model.

## Key Takeaways
- PerDocData is the foundational unit of Google's index — every page has one, and it stores all the signals used to rank it
- Authority and trust signals (PageRank equivalents) are stored per-document, not just per-site
- Semantic understanding goes beyond keywords — NLP entity extraction, topic classification, and intent signals are all present
- NavBoost/CRAPS click data is directly stored in PerDocData — user signals ARE document signals
- Freshness is a temporal signal with multiple attributes: crawl date, content modification date, and link freshness
- SpamPerDocData is a sub-structure containing demotion signals — a separate "spam layer" on top of quality signals
- Technical signals (page speed, mobile-friendliness) are also stored at document level
- Specialised content types (video, images, local, news) have their own signal extensions within PerDocData

## Frameworks/Methods Covered
- **Content Warehouse architecture**: How PerDocData sits within the broader Google Content Warehouse
- **Protocol Buffer structure**: PerDocData as a protocol buffer with nested sub-structures
- **Authority/Trust quantification**: How link-derived authority is stored per-document
- **SpamPerDocData**: The demotion signal layer (separate from quality signals)
- **Temporal signals**: Multiple freshness dimensions (crawl, content modification, link activity)
- **Specialised content extensions**: Per-format signal extensions for different content types

## Data/Stats
- Word count: 7,666
- 12 major sections covering all PerDocData components
- 70 external reference links — comprehensive academic-style analysis
- Key sub-structures: ContentData, SpamPerDocData, NavBoostCrapsData, QualitySignals

## How The Team Should Use This
- **Coral (SEO)**: The PerDocData model confirms that every on-page, off-page, and technical signal is stored at the document level — audits should check all three layers, not just keywords
- **Plankton (Writer)**: Content modification dates matter — updating existing articles signals freshness without creating new pages (PerDocData tracks content deltas)
- **Chitin (Dev)**: Technical signals in PerDocData include page experience signals — Core Web Vitals, mobile-friendliness, and HTTPS are all document-level stored signals
- **Current (Marketing)**: SpamPerDocData means paid link schemes and scaled content abuse create document-level demotion records that persist — avoid all grey-hat tactics
- **Key insight**: PerDocData is why you can't "trick" just one part of Google's system — all signals are aggregated at the document level and cross-validated
