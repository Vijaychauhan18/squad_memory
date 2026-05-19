---
source: https://www.hobo-web.co.uk/craps/
title: Craps: How Clicks Affect Google Rankings
scraped: 2026-03-20
tags: craps, navboost, clicks, bad clicks, good clicks, last longest click, user satisfaction
topic: click_behavior_systems
topic_assigned_by: phase9_merge_summaries
topic_assigned_on: 2026-05-19
---

## Core Concept
Craps is Hobo’s interpretation of the leaked Google protocol that aggregates click and impression signals per query-URL pair, turning user behaviour into durable ranking evidence for NavBoost.

## Key Takeaways
- Google does not just count clicks; it classifies them into positive and negative satisfaction signals.
- `goodClicks`, `badClicks`, and `lastLongestClicks` are treated as direct proxies for user satisfaction, dissatisfaction, and task completion.
- The data is sliced by country, language, and device, which means rankings can differ because user behaviour differs by context.
- Google appears to aggregate behaviour beyond individual URLs, using directory- and host-level patterns to build a reputation for sections of a site.
- Click data is privacy-controlled through user diversity thresholds and anti-spam heuristics, which makes manipulation harder than simple CTR tests imply.
- Hobo treats Craps as the raw measurement layer, with NavBoost acting as the re-ranking layer that consumes this behavioural evidence.

## Frameworks/Methods Covered
- **Query-URL click ledger**: aggregate interactions for one result in one query context
- **Sliced user-satisfaction model**: evaluate performance by device, country, and language
- **Topical neighbourhood effect**: host/path sections inherit behavioural reputation
- **Good click economy**: optimize for task completion, not just clickbait attraction

## Data/Stats
- Published: January 13, 2026
- Key fields highlighted: `impressions`, `clicks`, `goodClicks`, `badClicks`, `lastLongestClicks`, `patternLevel`, `voterTokenCount`, `unscaledIpPriorBadFraction`
- Hobo reiterates NavBoost’s rolling history as roughly 13 months of aggregated interaction data

## How The Team Should Use This
- **Coral (SEO)**: Improve title-snippet match and search intent fit so clicks turn into satisfying sessions, not pogo-sticks.
- **Plankton (Writer)**: Structure pages to resolve the query fast, then deepen the answer so the session ends on your page.
- **Developer / Chitin**: Group high-quality content into logical directories so section-level behavioural reputation compounds in your favour.
- **Current (Marketing)**: Brand familiarity matters because recognized brands earn the click more often and feed the behavioural loop.
- **Key insight for the team**: Ranking gains are not just earned before the click. They are earned after the click by ending the search journey well.
