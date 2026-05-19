---
source: https://www.hobo-web.co.uk/qualitynsrpqdata/
title: Google's Leaked QualityNsrPQData: The Core of Page Quality Assessment
scraped: 2026-03-18
tags: QualityNsrPQData, NSR, normalized site rank, page quality, google leak, quality signals, autopilot
topic: document_quality_system
intent: diagnostics, research, audit
role: pinchy, coral, researcher
confidence: high
canonical: true
use_for: nsr, page_quality, site_authority, subchunk_quality
avoid_for: social_content, customer_support
---

## Core Concept
QualityNsrPQData is the leaked Google data structure that powers page quality assessment — its central metric is Normalised Site Rank (NSR), a site-wide authority score that acts as a prior for all individual page quality judgements.

## Key Takeaways
- NSR (Normalised Site Rank) is a real, computable site authority score — it's not just PageRank, it's a normalised composite authority signal
- NSR acts as a "quality prior" — high-NSR sites get benefit of the doubt on quality before their content is fully evaluated
- Content quality is assessed on a spectrum: from "vital" (highest quality) to thin/spam at the bottom
- Link signals (quantity, quality, anchor text diversity) are explicitly stored in this structure — links still matter significantly
- "Autopilot" signals represent automated quality adjustments applied without human review
- "Subchunk" signals allow Google to assess quality at the paragraph/section level, not just the whole page
- Signal versioning is present — Google maintains historical quality snapshots, meaning past quality affects current ranking
- The structure confirms that site-wide quality affects individual page rankings — one bad section can hurt the whole site

## Frameworks/Methods Covered
- **NSR (Normalised Site Rank)**: The central authority score — how it's calculated and applied
- **Content Quality Spectrum**: The gradient from "vital" to "thin" — and what signals determine placement
- **Link Signal Analysis**: How link quality, quantity, and anchor text diversity feed into NSR
- **Autopilot System**: Automated quality adjustments that apply without manual intervention
- **Subchunk Signals**: Paragraph-level quality assessment capability
- **Signal Versioning**: How historical quality data influences current scoring

## Data/Stats
- Word count: 4,736
- 7 major sections including NSR analysis, content quality, links, autopilot, and strategic synthesis
- 26 external reference links
- Key finding: NSR is the central pillar — build site authority first, then individual page quality follows

## How The Team Should Use This
- **Coral (SEO)**: NSR means domain authority building is not optional — every link building effort contributes to the site-wide quality prior that lifts all pages
- **Plankton (Writer)**: Subchunk signals mean individual sections of an article can hurt quality scores — no filler paragraphs, every section must earn its place
- **Chitin (Dev)**: Signal versioning means historical content quality matters — don't delete old content without understanding its contribution to site-wide NSR
- **Current (Marketing)**: Building NSR through quality links and brand mentions is a long-term investment that compounds — start now, don't wait
- **Key insight**: QualityNsrPQData confirms that site authority is a prerequisite for page-level SEO to work at full effectiveness — @learnaiwithvijay should prioritise building NSR through quality backlinks and brand authority before aggressive content scaling































































































































<!-- phase9:begin -->
## Canonical Synthesis

This canonical note is reinforced by 5 merge candidate(s) and 0 supporting note(s) in the local memory library.

### Supporting Note Digest
- `hobo-page-quality-rating.md`: Hobo argues that Google's leaked `pqData` and `siteQualityStddev` fields are the machine-side implementation of Page Quality concepts from the Quality Rater Guidelines, with site consistency functioning as a practical ranking factor.
- `hobo-goldmine.md`: Goldmine is Hobo’s name for a leaked Google scoring engine that evaluates candidate SERP elements, especially titles, by comparing publisher input against alternatives from headings, links, URLs, and page content.
- `hobo-content-effort.md`: Hobo presents `contentEffort` as a leaked Google quality signal that attempts to estimate how much real labour, expertise, and originality went into an article, making low-cost mass content structurally disadvantaged.
- `hobo-compressedqualitysignals.md`: CompressedQualitySignals is described as the most important module in the entire Google Content Warehouse leak — it's the compressed quality scoring layer used in Mustang (page-level) and TeraGoogle (site-level) preliminary scoring that determines where pages enter the ranking pipeline.
- `hobo-compositedoc.md`: CompositeDoc is the master data structure in Google's Content Warehouse that combines every signal about a document — from basic content to authority metrics, technical directives, rich media, and structured data — into a single unified record used across the ranking pipeline.

### Retrieval Guidance
- Start with this note for the topic baseline and open the supporting notes only when you need source-specific evidence or edge cases.
- Use the attached digest to avoid re-reading overlapping notes during planning and research.
<!-- phase9:end -->



























































































































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Hobo

### Cross-Source Signals
- **Hobo**: QualityNsrPQData is the leaked Google data structure that powers page quality assessment — its central metric is Normalised Site Rank (NSR), a site-wide authority score that acts as a prior for all individual page quality judgements.

### Consensus
- The leak-oriented sources agree that document quality is modeled systemically rather than through one simple page-level factor.
- Quality signals cluster around effort, structure, and page-level scoring rather than isolated keyword tuning.
- Recurring source signals: google leak, page quality.

### Tension / Caveat
- Quality scoring appears systemic, but no single leaked field should be treated as a complete ranking explanation on its own. Current evidence is still source-concentrated, so treat it as directional rather than fully cross-validated.

### Squad Action
- Use this canon when the task is page quality, document modeling, or quality-system interpretation from the leaks.
<!-- phase10:end -->
