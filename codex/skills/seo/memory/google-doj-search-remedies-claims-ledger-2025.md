---
source: /Users/vijaychauhan/Downloads/gov.uscourts.dcd.223205.1436.0_2.pdf
title: DOJ v. Google Search Remedies - Claims Ledger 2025
scraped: 2026-04-25
published_on: 2025-09-02
tags: google doj, ai overviews, ai mode, grounding, rag, fastsearch, rankembed, navboost, glue, user-side data, defaults, publishers, google extended, syndication
topic: ai_search, retrieval_architecture, search_market_structure
intent: audit_support, evidence, research, routing
role: coral, researcher, pinchy, bill
confidence: high
canonical: true
canonical_group: Ai search, retrieval architecture, search market structure
use_for: page_level_claim_support, audit_evidence, quote_checking, timeline_validation, market_structure_analysis
avoid_for: legal_advice, simplistic_ranking_factor_claims
canonicalized_on: 2026-04-26
canonicalized_by: phase8_promote_canon
---

# Core Concept
This note is the page-level evidence ledger for the September 2, 2025 DOJ remedies opinion. Use it when you need court-backed claims about Search, AI Overviews, grounding, FastSearch, defaults, OEM and carrier distribution, RankEmbed, Glue, Navboost, human rater training, syndication, or publisher traffic pressure.

## Event Ledger
- October 20, 2020: DOJ and states filed the original search monopoly case against Google.
- December 2020: additional states and territories filed the Colorado action.
- September 12, 2023 to November 16, 2023: liability trial.
- August 5, 2024: liability ruling found Google unlawfully maintained monopoly power in general search services and general search text ads.
- September 2, 2025: remedies memorandum opinion filed.
- September 10, 2025: court directed the parties to submit a revised final judgment consistent with the opinion.

## AI Overviews And AI Mode Claims
- AI Overviews are a Search feature that uses a custom Gemini-based model to summarize search results on the SERP (`pages 23-25`).
- AI Overviews were introduced in 2024 (`page 24`).
- AI Overviews do not trigger on every query; Google says they appear when the answer is high quality and a net add to the page (`page 25`).
- AI Overview triggering depends on relevance signals and other signals generated from Search results (`page 25`).
- Google told the court that U.S. Search queries increased by about 1.5% to 2% after AI Overviews launched (`pages 25, 48`).
- Google also presented evidence that users who use AI Overviews search more and are more satisfied (`page 25`).
- The opinion records evidence that first-party AI features can reduce interaction with traditional organic results (`page 25`).
- The opinion also records evidence that corroborating links inside AI Overviews may receive more clicks than the same pages would get as ordinary blue links (`page 25`).
- AI Mode is a newer GenAI feature in Search that lets users dig deeper on some aspects of Search (`page 26`).
- Google testified that AI Mode and AI Overviews are expanding the types of queries users type into Google Search (`pages 106, 139`).
- The opinion says users ask longer questions in AI Mode than in traditional search (`pages 26, 42`).

## Grounding, RAG, And FastSearch Claims
- The opinion says LLMs face factuality and recency limits and cannot rely only on pretraining (`pages 32, 36-38`).
- Grounding is the mechanism that lets a model bring in current factual information from an outside source such as a search index (`pages 36-38`).
- The court treats retrieval-augmented generation and grounding as closely related systems for improving answer quality (`pages 36-38`).
- Grounded systems can turn a prompt into search queries, send those queries to a search engine, retrieve results, and synthesize a response from that material (`page 38`).
- Google uses a proprietary technology called FastSearch to ground Gemini responses (`page 39`).
- FastSearch is based on RankEmbed signals and produces abbreviated ranked web results for model consumption (`page 39`).
- FastSearch is faster than the main Search product because it retrieves fewer documents, but it is lower quality than Search's fully ranked web results (`page 39`).
- The court refused to require FastSearch syndication because it is mainly a grounding technology and is not Google's normal SERP (`page 183`).

## Access Point And Distribution Claims
- The opinion treats search access points as the most efficient search distribution channels and repeats that Google paid heavily to control them (`pages 5, 13-14, 187-188`).
- The court says search access points are expanding beyond classic browser search bars into AI apps, assistants, visual search, and device-level entry points (`pages 46-53`).
- Google estimated that as of March 28, 2025 the Gemini app had roughly 140 million daily queries, compared with 1.2 billion for ChatGPT, over 200 million for MetaAI, 75 million for Grok, 50 million for DeepSeek, and 30 million for Perplexity (`page 46`).
- Rival GenAI companies had already secured some OEM or partner distribution with Apple, T-Mobile, Yahoo, DuckDuckGo, and Microsoft (`page 46`).
- Google entered Gemini distribution and promotion agreements with Samsung, Motorola, and Lenovo (`page 47`).
- Within the Gemini app, users can access Search through a related-search `G` icon that surfaces search-related topics and corroborating material (`page 51`).
- Circle to Search is treated as a new Android search access point because users can execute a query by circling part of the screen and receive a SERP (`page 52`).
- Google Lens in Chrome only works as currently integrated when Google Search is the default browser search engine (`page 53`).
- Samsung's Gemini commercial arrangement tied payments to preinstallation, placement, default invocation, hot-word activation, and device qualification rules (`pages 55-57`).
- To qualify as a Gemini Qualified Device, Samsung hardware had to ship with the Gemini app preinstalled and placed in specified locations (`page 55`).
- Motorola's updated agreements also tied some outcomes to placement and promotion obligations for Gemini and related Google products (`pages 57-60`).
- Carrier agreements with AT&T, Verizon, and proposed T-Mobile terms moved toward device-by-device and access-point-by-access-point structures rather than the older broader exclusivity model (`pages 59-61`).

## Search Index, Ranking, And Data Claims
- The opinion says a comprehensive and current search index is critical to high-quality search results (`pages 140-145`).
- Search index quality matters not just for classic search, but for GenAI quality because grounded systems depend on retrieval (`pages 38, 143-145`).
- The court adopts the `80-20` problem: competitors may reach the first 80% of useful queries relatively quickly, but the last 20% of long-tail and rare queries remains much harder (`pages 143, 176, 180-181`).
- Raw signals include the number of clicks, page content, and the terms inside a query (`page 141`).
- Raw signals can be generated with simple counting methods and then aggregated into additional signals (`pages 141-142`).
- Those aggregated signals are then combined into top-level signals that contribute to final scoring (`page 142`).
- The opinion specifically names quality and popularity as top-level signals (`page 142`).
- Signals developed through deep-learning systems like RankEmbed are also treated as top-level signals (`page 142`).
- User-interaction-derived signals help Google decide how often to crawl pages and how to maintain index freshness, not only how to rank documents (`page 142`).
- User-side Data is defined as data collected from the pairing of a user query and the returned response (`page 156`).
- The court also describes User-side Data as user-interaction data or click-and-query data (`page 156`).
- Examples include the link or vertical a user clicks, hover behavior, and whether a user clicks back quickly (`page 156`).
- Glue is described as a super query log containing query text, language, user location, device type, ranking information, shown blue links, triggered search features, clicks, hovers, duration, and query interpretation or suggestion data (`page 157`).
- The opinion says Glue contains Navboost information (`page 157`).
- Navboost is described as a memorization system that aggregates click-and-query data about web results delivered to the SERP (`page 157`).
- RankEmbed and RankEmbedBERT rely on two main sources of data: 70 days of search logs plus scores generated by human raters (`page 158`).
- The opinion says those rater scores are used by Google to measure the quality of organic search results (`page 158`).
- RankEmbed is described as an AI-based deep-learning retrieval or ranking system with strong natural-language understanding and particular value on long-tail queries (`page 158`).
- The opinion treats human rater data as upstream model-training material, not merely downstream evaluation rhetoric (`page 158`).
- Google's Search team post-trains Gemini base models for search-specific uses (`page 159`).
- One such post-training model is MAGIT, which helps produce AI Overview responses in the desired format (`page 159`).
- Google uses `Search data` to train MAGIT (`page 159`).
- The court says the evidence on exactly what Search data is used, how much is used, and how important it is was sparse (`page 160`).
- The court also says the record did not prove that Google's scale advantage in Search had been shown to create a direct GenAI quality advantage through this training route (`page 160`).

## Remedy And Syndication Claims
- Google is barred from entering or maintaining exclusive contracts tied to Search, Chrome, Google Assistant, and the Gemini app (`pages 7-8, 214-224`).
- The court rejected Chrome divestiture and contingent Android divestiture (`pages 111-119, 214-224`).
- The court rejected a broad payment ban and allowed Google to continue paying distribution partners under narrowed restrictions (`pages 119-128, 214-224`).
- The court ordered narrowed search-index sharing focused on Google's web-crawled content rather than the full internal ecosystem of third-party feeds and partnerships (`pages 145-150`).
- The court rejected broader requests that would expose too much proprietary engineering or broader derived-signal infrastructure (`pages 146-147, 160-168`).
- Google must offer narrowed search syndication to qualified competitors (`pages 168-183`).
- The first-year syndication cap is 40% of annual queries (`pages 180-181`).
- The court says the 40% cap is consistent with evidence that rivals should be able to build toward answering the first 80% of queries themselves (`pages 180-181`).
- The tapering structure is intended to force competitors to rely less on Google over time (`page 181`).
- Google must offer narrowed search text ads syndication remedies (`pages 180-186`).
- The court requires public disclosure of material changes to search text ad auctions (`pages 199-203`).
- The judgment term is six years and includes a Technical Committee (`pages 7-10, 224-230`).

## Publisher Pressure And Google Extended Claims
- The opinion explicitly acknowledges that grounded GenAI responses can synthesize multiple sources into narrative answers and reduce visits to publisher sites (`pages 207-208`).
- The court says publishers depend on Google's crawling and index inclusion for traffic, which weakens their bargaining leverage (`page 208`).
- Google Extended lets publishers opt out of the use of their content for training foundation models and for grounding the Gemini app or Vertex AI (`page 208`).
- Google Extended does not let publishers opt out of use in AI Overviews or Search-model fine-tuning (`page 208`).
- A publisher that wants to avoid appearance in AI Overviews would effectively have to opt out of crawling altogether (`page 209`).
- The court says that is not a tenable choice because it may remove the publisher from Google's index and SERP visibility (`page 209`).
- The court rejected publisher-specific remedies because the factual record was thinner, there was not enough direct publisher testimony, and the proposed relief was not tightly matched to the proven antitrust violation (`pages 209-210`).

## Retrieval Guidance
- Start with `google-doj-search-remedies-opinion-2025.md` for the canonical frame.
- Use this ledger when the task needs page-level support, claim checking, or exact evidence points.
- Pair this with `google-doj-search-remedies-ranking-and-genai-2025.md` for ranking and retrieval questions.
- Pair this with `google-doj-search-remedies-distribution-and-publisher-remedies-2025.md` for defaults, OEMs, syndication, and publisher-pressure questions.

## How The Team Should Use This
- **Coral (SEO)**: Use this when an audit needs court-grade support for AIOs, grounding, ranking systems, defaults, or publisher traffic pressure.
- **Researcher / Kelp**: Use this as the fastest page-reference source before quoting or paraphrasing the opinion.
- **Pinchy / Bill**: Use it when connecting patent memory, leak memory, and court-verified disclosures into one architecture narrative.

## Caveat
This note is best used as primary-source architecture evidence and market-structure evidence. It should not be used to overclaim that every disclosed component is a simple live ranking factor in isolation.












































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Google

### Cross-Source Signals
- **Google**: Core Concept.

### Consensus
- Sources converge that `ai search, retrieval architecture, search market structure` should be treated as a repeatable operating concern, not a one-off tactic.

### Tension / Caveat
- No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon.

### Squad Action
- Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.
<!-- phase10:end -->
