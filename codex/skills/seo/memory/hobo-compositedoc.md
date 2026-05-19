---
source: https://www.hobo-web.co.uk/compositedoc/
title: The CompositeDoc: Google's Core Document Data Structure Leaked
scraped: 2026-03-18
tags: CompositeDoc, google leak, document structure, indexing, authority, rich media, structured data, technical SEO
topic: document_quality_system
topic_assigned_by: phase9_merge_summaries
topic_assigned_on: 2026-05-19
---

## Core Concept
CompositeDoc is the master data structure in Google's Content Warehouse that combines every signal about a document — from basic content to authority metrics, technical directives, rich media, and structured data — into a single unified record used across the ranking pipeline.

## Key Takeaways
- CompositeDoc is described as "the Rosetta Stone of Google's index" — it's the complete picture of how Google sees any given page
- Document identity signals include URL, language, content type, and canonical status — basic but foundational
- Authority and quality signals are embedded at the document level, not just the site level — granular scoring
- Technical directives (noindex, nofollow, canonicalization) are explicit fields — they are not interpretations, they are hard rules
- Rich media signals (images, video, structured data) have their own scoring within CompositeDoc
- Content classification fields determine which vertical/feature a page might appear in (news, shopping, local, etc.)
- Strategic synthesis: the unified document model means every SEO decision affects multiple interrelated fields
- The structure confirms that structured data (Schema.org) directly populates CompositeDoc fields — it's not optional

## Frameworks/Methods Covered
- **Section 1**: Document Identity and Content Fundamentals — URL, language, content type, canonical
- **Section 2**: Authority and Quality anatomy — how authority signals are stored at document level
- **Section 3**: Technical Directives — crawling, indexing, and canonical controls
- **Section 4**: Rich Media, Structured Data, and Content Classification — how Schema.org data maps to fields
- **Section 5**: Strategic Synthesis — unified framework for a signal-driven SEO approach

## Data/Stats
- Word count: 8,081
- 5 sections + references
- 3 images, 38 internal links, 13 external links
- Includes actual leaked schema diagram image

## How The Team Should Use This
- **Chitin (Dev)**: CompositeDoc confirms that technical directives are hard-coded fields, not "guidelines" — canonical tags, noindex, and hreflang must be implemented correctly
- **Coral (SEO)**: Structured data directly populates CompositeDoc fields — implementing Schema.org markup isn't just for rich results, it's feeding Google's core document model
- **Plankton (Writer)**: Content classification fields mean your content type matters — is this an article, a product page, a how-to? Correct content type signals activate the right ranking verticals
- **Current (Marketing)**: Understanding CompositeDoc means understanding that @learnaiwithvijay competes differently in each vertical — AI content may qualify for different SERP features than standard blog posts
- **Key insight**: CompositeDoc reveals that SEO is not about optimising one thing — it's about correctly populating all the relevant fields in Google's document model simultaneously
