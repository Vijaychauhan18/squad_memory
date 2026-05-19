---
source: /Users/vijaychauhan/Downloads/gov.uscourts.dcd.223205.1436.0_2.pdf
title: DOJ v. Google Search Remedies - Ranking And GenAI Systems 2025
scraped: 2026-04-25
published_on: 2025-09-02
tags: google doj, rankembed, rankembedbert, glue, navboost, ai overviews, ai mode, grounding, rag, fastsearch, quality raters
topic: retrieval_architecture, ai_search, click_behavior_systems
intent: research, diagnostics, system_architecture
role: coral, researcher
confidence: high
canonical: true
canonical_group: Retrieval architecture, ai search, click behavior systems
use_for: ranking_signal_interpretation, ai_search_architecture, click_signal_analysis, grounding_analysis, long_tail_query_analysis
avoid_for: simplistic_ctr_claims
canonicalized_on: 2026-04-26
canonicalized_by: phase8_promote_canon
---

# Core Concept
This note captures the opinion’s most important disclosures about Google’s ranking and retrieval stack: raw signals, top-level signals, Glue, Navboost, RankEmbed, human rater data, grounding, FastSearch, AI Overviews, and the role of search indexes in GenAI quality.

## AI Overviews And AI Mode
- The court says AI Overviews use a custom Gemini-based model to summarize search results on the SERP (`pages 23-25`).
- AI Overviews only trigger when Google believes the output is both high quality and a net add to the page (`page 25`).
- Google told the court that AI Overviews increased user satisfaction and increased U.S. Search query volume by about 1.5% to 2% after launch (`page 25`).
- The opinion also records evidence that Google’s first-party AI features can reduce interaction with third-party organic results, though pages cited as corroborating links inside AI Overviews may receive more clicks than if they appeared only as traditional blue links (`page 25`).
- The court says AI Mode is another GenAI feature inside Search and that users ask longer questions there than in traditional search (`pages 23, 42`).

## LLM Limits And Why Grounding Matters
- The opinion says LLMs are constrained by factuality and recency issues and by the limits of their training data (`pages 32, 36`).
- Grounding is defined as anchoring model output on factual information from an outside database such as a search index (`pages 36-38`).
- RAG is treated as a grounding technique and sometimes used interchangeably with grounding (`page 36`).
- Grounding reduces hallucinations and helps with freshness by letting models access current web information (`pages 37-38`).
- The opinion explicitly says grounded systems can translate user prompts into search queries, send those queries to a search engine, and use the retrieved material to generate a response (`page 38`).

## Search Index As GenAI Infrastructure
- The court says search-index quality matters not only for classic search but also for GenAI products that rely on grounding (`pages 143-144`).
- A weak index harms GenAI quality because the model can only ground against what the search system can actually retrieve (`pages 38, 143-144`).
- The opinion uses this as one reason access to Google’s search index could accelerate rival development, especially for long-tail coverage (`pages 143-145`).

## FastSearch
- The court says Google uses a proprietary technology called FastSearch to ground Gemini responses (`page 39`).
- FastSearch is based on RankEmbed signals and returns abbreviated, ranked web results for model consumption (`page 39`).
- The opinion says FastSearch is faster than the main Search product but is not the same thing as the normal Google SERP (`pages 39, 183`).
- The court rejects forced FastSearch syndication because its primary use case is GenAI grounding and it is less reliable than the main Search product (`page 183`).

## Raw Signals, Top-Level Signals, And Search Quality
- The opinion says raw signals include the number of clicks, page content, and the terms within a query (`page 141`).
- It says signals can be aggregated into more signals, and then combined into top-level signals (`page 142`).
- It specifically names quality and popularity as top-level signals (`page 142`).
- The opinion also says user-interaction data helps Google decide crawl frequency and index freshness, not only ranking (`page 142`).

## Glue And Navboost
- The court describes Glue as a super query log containing:
  query text, language, user location, device type, ranking information, the 10 blue links and triggered SERP features, clicks, hovers, duration, and query interpretation or suggestion data (`page 157`).
- Navboost is described as a memorization system that aggregates click-and-query data about results shown on the SERP (`page 157`).
- The opinion also says Glue contains Navboost information (`page 157`).
- This is one of the clearest public records that click and interaction systems are stored as broad SERP-behavior data, not just isolated link-click counters.

## RankEmbed And RankEmbedBERT
- RankEmbed and RankEmbedBERT rely on two main data sources: 70 days of search logs and human rater quality scores, with the percentage redacted in the opinion (`page 158`).
- The court describes RankEmbed as a deep-learning retrieval model with strong natural-language understanding (`page 158`).
- It highlights semantic matching: RankEmbed can retrieve useful documents even when the query lacks exact terms found on the page (`page 158`).
- The opinion says RankEmbed particularly helped Google with long-tail queries (`page 158`).
- It also says RankEmbed used far less training data than earlier models while improving quality (`page 158`).

## Human Raters
- The opinion says human rater scores are part of the data used to train RankEmbed family models (`page 158`).
- That means human evaluations are not just downstream auditing; they feed ranking-model training upstream.
- This makes the Quality Rater Guidelines more operationally relevant for SEO than a simple “raters do not directly rank pages” talking point would imply.

## User-Side Data And What It Means For Clicks
- The opinion defines User-side Data as the pairing of a query and the returned response, along with user interactions (`page 156`).
- Examples include which link or vertical a user clicks, hover behavior, and whether the user clicks back and how quickly (`page 156`).
- The court calls user-interaction data the raw material Google uses to improve search services (`page 156`).
- This supports the strongest careful reading of click data: clicks are important, but as upstream training and improvement material inside broader systems.

## GenAI Training Limits
- The opinion says Google does not use click-and-query data to pre-train base Gemini models (`pages 158-159`).
- It says the Search team does post-train Gemini models for search-specific uses, including the MAGIT model used for AI Overviews (`page 159`).
- Google uses some form of “Search data” for MAGIT, but the court says the evidence was too sparse to justify forcing disclosure of GenAI training data (`page 160`).
- The court also says the evidence did not show that Google’s GenAI products were superior because of search user-interaction data (`page 160`).

## SEO Reading
- Clicks are best treated as raw behavioral inputs that can train retrieval and ranking systems.
- Human rater data matters because it becomes model-training material, especially for nuanced and long-tail queries.
- Search index quality is now directly relevant to AI visibility because grounded answers depend on retrieval.
- FastSearch and similar retrieval shortcuts matter for GenAI answer generation, but they are not the same as the full search product.

## How The Team Should Use This
- **Coral (SEO)**: Use this note when explaining why click data is not a simplistic direct factor but still deeply relevant.
- **Researcher / Kelp**: Use this as a primary-source backbone when validating claims about RankEmbed, rater data, or grounding.
- **Bill / Patent brain**: Pair this with `google-patent-us8661029b1-implicit-user-feedback.md`, `hobo-human-quality-raters.md`, and `hobo-popularity-signal.md` to connect public patents, leaks, and court-verified disclosures.












































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Google

### Cross-Source Signals
- **Google**: Core Concept.

### Consensus
- Sources converge that `retrieval architecture, ai search, click behavior systems` should be treated as a repeatable operating concern, not a one-off tactic.

### Tension / Caveat
- No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon.

### Squad Action
- Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.
<!-- phase10:end -->
