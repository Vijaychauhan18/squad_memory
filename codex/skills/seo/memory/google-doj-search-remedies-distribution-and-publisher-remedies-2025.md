---
source: /Users/vijaychauhan/Downloads/gov.uscourts.dcd.223205.1436.0_2.pdf
title: DOJ v. Google Search Remedies - Distribution, Syndication, And Publisher Pressure 2025
scraped: 2026-04-25
published_on: 2025-09-02
tags: google doj, defaults, oems, carriers, samsung, motorola, search access points, syndication, publishers, google extended
topic: search_market_structure, distribution_strategy, publisher_ecosystem
intent: research, diagnostics, market_analysis
role: coral, researcher, pinchy
confidence: high
canonical: true
canonical_group: Search market structure, distribution strategy, publisher ecosystem
use_for: default_distribution_analysis, access_point_analysis, publisher_risk_analysis, syndication_research, genai_distribution_analysis
avoid_for: legal_advice
canonicalized_on: 2026-04-26
canonicalized_by: phase8_promote_canon
---

# Core Concept
This note captures the market-structure side of the remedies opinion: how search access points work, how Google updated its OEM and carrier contracts, how syndication remedies are supposed to reduce Google’s scale moat, and why the court acknowledged publisher pain but refused to impose publisher-specific controls.

## Defaults And Access Points
- The opinion treats access points as the most efficient distribution channels for general search and repeats that Google paid billions to secure them (`pages 5, 13-14`).
- The court says default search placement matters because user habit, brand, and switching friction make defaults extremely powerful (`pages 5, 187-188`).
- It rejects choice screens anyway, saying courts should avoid product-design mandates and the evidence did not show that choice screens would meaningfully improve competition (`pages 9, 187-191`).

## New AI Search Access Points
- The court says GenAI products can become search access points, though they are not purely search tools yet (`pages 46-50`).
- Google has explored new AI access points as part of a strategy to continue Search growth and diversification (`page 50`).
- The Gemini app can expose Search-related topics through a `G` button that kicks the user into a more traditional Google results page, but the opinion says this currently drives little traffic to Search (`pages 50-51`).
- Circle to Search is a new Android search access point that lets users search by circling part of the screen and can in principle work with a non-Google engine if the OEM supports it (`page 52`).
- Google Lens is a visual search access point in Chrome, but its current integration only works when Google Search is the default engine in the browser (`pages 52-53`).

## GenAI Distribution And OEM Deals
- The opinion records that rivals like OpenAI and Perplexity have already secured some OEM and partner distribution, including Apple, T-Mobile, Yahoo, DuckDuckGo, Microsoft, and Motorola (`pages 46-47`).
- Google also entered Gemini-related distribution and promotion agreements with Samsung, Motorola, and Lenovo (`pages 47, 53-58`).
- Samsung’s April 19, 2025 U.S. RSA moved to an access-point-by-access-point and device-by-device payment model and did not require exclusive distribution (`pages 54-55`).
- Samsung’s January 1, 2025 Gemini Commercial Agreement tied payments to preinstallation, placement, default invocation, hot-word activation, AICore, and Gemini Nano requirements on qualified devices (`pages 55-57`).
- Motorola’s updated agreements similarly increased flexibility but still tied some revenue outcomes to placement and promotion requirements (`pages 57-60`).
- Carrier agreements with AT&T, Verizon, and proposed T-Mobile terms also moved toward access-point-by-access-point and device-by-device structures with fewer outright exclusivity restrictions (`pages 59-61`).

## Search Index Remedy
- The court says a comprehensive and current search index is critical to high-quality search results (`pages 140-145`).
- It narrows Plaintiffs’ proposed index-sharing remedy so it only covers web-crawled content, not third-party feeds and partnership data (`page 145`).
- It rejects sharing of overly broad signals derived only partly from user-side data because that would spill too far into Google’s proprietary engineering (`pages 146-147`).
- The court allows only a one-time snapshot of narrowed search-index data because competitors can use that to build their own index afterward (`page 162 footnote`).

## The 80-20 Problem
- The opinion repeatedly says competitors can get to the first 80% of useful queries much faster than the last 20% (`pages 143-144, 176`).
- Long-tail and rare queries are the hard part because they depend on obscure or infrequently seen sources (`pages 143, 176`).
- The court uses this reasoning to justify syndication caps and to explain why Google’s scale remains structurally important.

## Search Syndication Remedy
- The court orders Google to provide narrowed search syndication services to qualified competitors (`pages 8, 168-183`).
- It rejects fully open-ended use rights and narrows the remedy largely toward ordinary commercial terms (`pages 173-183`).
- It sets a first-year cap of 40% of annual queries for syndication use because rivals should build toward answering the first 80% of queries themselves (`page 180`).
- It rejects synthetic-query rights for quality improvement because the record did not show the requested linkage strongly enough (`page 179`).
- It refuses to require FastSearch syndication (`page 183`).

## Search Text Ads Syndication And Ads Transparency
- The court says Google must offer search text ads syndication on narrowed terms (`pages 8, 180-186`).
- It rejects some of Plaintiffs’ more aggressive ad-data remedies as too disconnected from the proven antitrust wrong (`page 199`).
- It does require public disclosure of material changes to search text ad auctions to improve pricing transparency (`pages 9, 199-203`).

## Publisher Pressure And Google Extended
- The opinion explicitly acknowledges an existential publisher problem: grounded GenAI responses synthesize multiple sources into narrative answers, so users visit publisher sites less often than in traditional search (`pages 207-208`).
- The court says publishers depend on Google crawling for search traffic, which weakens their leverage (`page 208`).
- It records that Google Extended lets publishers opt out of foundation-model training and grounding for the Gemini app and Vertex AI, but not of use in AI Overviews or Search model fine-tuning (`pages 208-209`).
- A publisher that wants to stop appearing in AI Overviews effectively has to opt out of crawling altogether, which risks disappearing from Google’s index and SERP (`page 209`).
- Even with those findings, the court rejects the proposed publisher remedies because there was not enough factual record, no direct publisher testimony, and the conduct was not the same category of wrong as Google’s unlawful distribution agreements (`pages 209-210`).

## SEO Reading
- Distribution is a ranking-adjacent moat. Query access shapes who gets the data to improve search quality.
- Search interfaces are fragmenting into AI apps, assistants, browsers, visual search, and OS-level shortcuts.
- The index is still the core strategic asset behind both classic SEO and AI visibility.
- Publisher traffic compression from AI products is now acknowledged in a federal court opinion, which makes it a stronger strategic risk than a speculative industry talking point.

## How The Team Should Use This
- **Coral (SEO)**: Use this note when the problem is market access, search interfaces, defaults, or publisher traffic loss.
- **Pinchy (orchestrator)**: Use it for strategic planning around where search distribution may move next.
- **Researcher / Kelp**: Use it when validating claims about OEM agreements, access points, syndication, or publisher optionality.












































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Google

### Cross-Source Signals
- **Google**: Core Concept.

### Consensus
- Sources converge that `search market structure, distribution strategy, publisher ecosystem` should be treated as a repeatable operating concern, not a one-off tactic.

### Tension / Caveat
- No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon.

### Squad Action
- Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.
<!-- phase10:end -->
