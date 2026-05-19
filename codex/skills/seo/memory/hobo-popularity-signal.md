---
source: https://www.hobo-web.co.uk/doj-v-google-disclosure-the-popularity-signal-p-score/
title: DOJ v. Google Disclosure: The Popularity Signal (P*)
scraped: 2026-03-20
tags: popularity, p-star, chrome data, navboost, links, google doj, user behaviour
topic: click_behavior_systems
topic_assigned_by: phase9_merge_summaries
topic_assigned_on: 2026-05-19
---

## Core Concept
Hobo frames `P*` as a top-level Google popularity signal that blends Chrome visit data, link connectivity, anchor structures, and user interaction evidence to promote well-linked, widely visited documents.

## Key Takeaways
- Popularity is disclosed as a fundamental ranking signal alongside quality, not a side metric.
- Hobo interprets `P*` as broader than PageRank because it combines browser behaviour, anchors, and interaction data.
- Chrome-derived visit evidence suggests Google can evaluate real-world popularity beyond the search result click itself.
- Link structures still matter, but their value is tied to actual navigation and usage, not only static graph theory.
- Popularity also affects crawl prioritisation, which means stronger pages may get fresher indexing and faster recrawl.
- `P*` reinforces the idea that reputation, navigation patterns, and link architecture work together rather than separately.

## Frameworks/Methods Covered
- **P* signal model**: browser visits + anchors + interaction patterns
- **Popularity plus quality pairing**: top-level signals work together to produce rank potential
- **Crawl frequency implication**: quality and popularity influence how often Google revisits content

## Data/Stats
- Published: September 14, 2025
- Article cites DOJ remedial opinion passages describing popularity as a top-level signal
- Hobo highlights “Chrome visit data” and “number of anchors” as the clearest public disclosures of `P*`

## How The Team Should Use This
- **Coral (SEO)**: Treat internal linking and SERP CTR work as popularity engineering, not isolated optimizations.
- **Plankton (Writer)**: Create assets people actually revisit, share, and navigate between, not just pages that rank once.
- **Developer / Chitin**: Improve site architecture so important pages are easy to reach, well linked, and reinforced by clear anchor text.
- **Current (Marketing)**: Brand demand and repeat visits matter because popularity is partly behavioural, not only link-based.
- **Key insight for the team**: A page that is merely indexable is not enough. Google appears to reward content that becomes a destination.
