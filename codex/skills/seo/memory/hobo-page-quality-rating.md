---
source: https://www.hobo-web.co.uk/google-pq-page-quality-rating/
title: The Google Leak, Page Quality Rating (PQ) and the Rater Connections
scraped: 2026-03-20
tags: pq, page quality, quality raters, sitequalitystddev, pqdata, google leak, trust
topic: document_quality_system
topic_assigned_by: phase9_merge_summaries
topic_assigned_on: 2026-05-19
---

## Core Concept
Hobo argues that Google's leaked `pqData` and `siteQualityStddev` fields are the machine-side implementation of Page Quality concepts from the Quality Rater Guidelines, with site consistency functioning as a practical ranking factor.

## Key Takeaways
- `pqData` is presented as encoded page-level quality input, which suggests Google turns subjective page quality concepts into numeric document signals.
- `siteQualityStddev` is framed as a consistency measure across a site’s pages, not just a quality score for one URL.
- Strong pages do not fully protect a domain if weak pages increase variance. Quality inconsistency becomes a site-wide risk.
- Hobo links John Mueller’s comments about consistency to this leak field, treating page quality spread as an operational SEO issue.
- Pruning, merging, or rewriting weak pages is not just cleanup. In this model it improves the statistical profile of the whole site.
- The quality rater framework is not treated as motivational advice here. Hobo interprets it as a usable proxy for predicting algorithmic quality signals.

## Frameworks/Methods Covered
- **PQ to machine signal mapping**: rater concepts become encoded per-page quality data
- **Site variance model**: lower spread in quality equals more predictable trust
- **Quality consistency audit**: identify weak sections that drag down a high-performing domain

## Data/Stats
- Published: January 12, 2026
- Key leak fields: `siteQualityStddev`, `pqData`
- Core thesis: page-level quality is encoded individually, then rolled up into a site-level consistency profile

## How The Team Should Use This
- **Coral (SEO)**: Run audits by section, not only by top pages. Look for quality variance across categories and legacy content.
- **Plankton (Writer)**: Rewrite weak articles until they meet the same editorial bar as the site’s best assets.
- **Developer / Chitin**: Surface thin templates, outdated archives, poor UX sections, and broken-support pages that create low-trust experiences.
- **Current (Marketing)**: Stop sending paid or social traffic to pages that would fail a serious page quality review.
- **Key insight for the team**: Google may reward not just excellence, but consistency of excellence. A messy archive can weaken a strong brand.
