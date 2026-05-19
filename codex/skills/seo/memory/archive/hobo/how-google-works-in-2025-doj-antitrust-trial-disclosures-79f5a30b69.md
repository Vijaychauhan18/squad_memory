---
source: https://www.hobo-web.co.uk/how-google-works/
title: How Google Works in 2025 - DOJ Antitrust Trial Disclosures
scraped: 2026-03-23
published_on: 2025-07-10
tags: live_feed, phase1_ingest, hobo, publication, quality, leak-systems, archive_backfill, historical_source
topic: quality_systems
intent: research, monitoring, source_selection, leak_systems
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Archive backfill - Hobo Web
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How Google Works in 2025 - DOJ Antitrust Trial Disclosures

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/how-google-works/
Published: 2025-07-10
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
Find out how Google works using testimonies from he antitrust case, United States et al. v. Google LLC, initiated by the US Department of Justice (DOJ) in 2020.

## Extracted Body
This is a preview of Chapter 1 from my new ebook – Strategic SEO 2025 – a PDF which is available to download for free here . Published on: 10 July 2025 at 06:07

TL;DR Google’s DOJ trial disclosures confirm that search ranking hinges on two top-level signals – Quality (Q*) and Popularity (P*) – powered by modular systems like Navboost, Topicality, and PageRank, with user interaction data at the core. SEO success now depends on trust, authority, user engagement, freshness, and adapting to potential legal-driven changes in Google’s architecture.

SEO really can be broken down, based on Google V DOJ evidence, into “Minding your P*s and Q*s”. “Knowing your A, B and Cs”, “dotting your I’s” and “crossing your T*s”.

Two Core Signals Drive Ranking: Google’s system reduces to Quality (Q*) and Popularity (P*) , revealed in DOJ trial documents.

Modular Architecture: Underlying systems like Topicality (T*), Navboost, and RankBrain feed into those top-level signals.

User Data Is Central: Clicks, scrolls, Chrome visit data, dwell time, and pogo-sticking are leveraged as critical ranking feedback.

Hand-Crafted Signals Dominate: Most ranking factors are engineered manually, not black-box ML, for control and stability.

Freshness Matters: Google boosts recency for queries where timeliness is essential (news, events), balancing against historical clicks.

Links Still Core: PageRank (distance from trusted sources), anchor text, and backlink quality remain crucial authority signals.

Context Layers Refine Results: Location and personalisation heavily shape what individual users see beyond the “universal” rank.

AI as Final Layer: RankBrain, BERT, and MUM don’t replace hand-crafted signals — they refine them with semantic understanding.

⚖️ Legal Impact Ahead: DOJ remedies may force changes to Google’s ranking systems, shaping SEO strategy going forward.

The antitrust case, United States et al. v. Google LLC , initiated by the US Department of Justice (DOJ) in 2020, represents the most significant legal challenge to Google’s market power in a generation.

While the legal arguments focused on market monopolisation, the proceedings inadvertently became a crucible for technical disclosure, forcing Google to all but reveal the long-guarded secrets of its search engine architecture.

The trial’s technical revelations were not incidental; they were central to the core legal conflict.

The DOJ’s case rested on the premise that Google unlawfully maintained its monopoly in general search and search advertising through a web of anticompetitive and exclusionary agreements with device manufacturers and browser developers, including Apple, Samsung, and Mozilla.

These contracts, often involving payments of billions of dollars annually, ensured Google was the pre-set, default search engine for the vast majority of users, thereby foreclosing competition by denying rivals the scale and data necessary to build a viable alternative.

This legal challenge created a strategic paradox for Google.

To counter the DOJ’s accusation that its dominance was the result of illegal exclusionary contracts, Google’s primary defence was to argue that its success is a product of superior quality and continuous innovation – that users and partners choose Google because it is simply the best search engine available .

This “superior product” defence, however, could not be asserted in a vacuum.

To substantiate the claim, Google was compelled to present evidence of this superiority, which necessitated putting its top engineers and executives on the witness stand. Individuals like Pandu Nayak, Google’s Vice President of Search, and Elizabeth Reid, Google’s Head of Search, were tasked with explaining, under oath, the very systems that produce this acclaimed quality.

Consequently, the act of defending its market position legally forced Google to compromise its most valuable intellectual property and its long-held strategic secrecy.

The sworn testimonies and internal documents entered as evidence provided an unprecedented, canonical blueprint of Google’s key competitive advantages.

At the heart of these revelations is the central role of user interaction data .

A recurring theme throughout the testimony was that Google’s “magic” is not merely a static algorithm but a dynamic, learning system engaged in a “two-way dialogue” with its users.

Every click, every scroll, and every subsequent query is a signal that might teach the system what users find valuable.

This continuous feedback loop, operating at a scale that Google’s monopoly ensures no competitor can replicate, is the foundational resource for the powerful ranking systems detailed in the trial.

The trial testimony and exhibits dismantle the popular conception of Google’s ranking system as a single, monolithic algorithm . Instead, they reveal a sophisticated, multi-stage pipeline composed of distinct, modular systems, each with a specific function and data source . This architecture is built upon a foundation of traditional information retrieval principles and human-engineered logic, which is then powerfully refined by systems that leverage user behaviour data at an immense scale .

While initial trial exhibits hinted at this modularity, the later unredacted remedial opinion in the DOJ v. Google case provided the definitive, high-level blueprint. The court revealed that Google has two “fundamental top-level ranking signals” that are the primary inputs for a webpage’s final score: Quality (Q*) and Popularity (P*) . These two signals also help Google determine how frequently to crawl webpages to keep its index fresh.

This analysis details the core components of this architecture, showing how the previously revealed systems of Topicality (T*) , Navboost , and Q* are the essential building blocks for Google’s top-level signals.

The following table summarises the confirmed two-pillar architecture. The systems detailed in the original trial are now best understood as the underlying components that feed into these two fundamental signals.

The foundational systems revealed during the trial provide the mechanics for the top-level signals.

The Quality Score (Q*) is the internal system that assesses the overall trustworthiness and quality of a website or domain . It is a hand-crafted, largely static score that functions as the core of the top-level Quality signal . Its key data inputs include PageRank and the link distance from trusted “seed” sites, which align perfectly with the remedial opinion’s description of the Quality signal .

The top-level Popularity (P*) signal is powered by a combination of systems that measure user engagement and link structures.

Contrary to the prevailing narrative of an all-encompassing artificial intelligence, the trial revealed that Google’s search ranking systems are fundamentally grounded in signals that are “hand-crafted” by its engineers .

This deliberate engineering philosophy prioritises control, transparency, and the ability to diagnose and fix problems, a stark contrast to the opaque, “black box” nature of more complex, end-to-end machine learning models.

The deposition of Google Engineer HJ Kim was particularly illuminating on this point. He testified that “ the vast majority of signals are hand-crafted ,” explaining that the primary reason for this approach is so that “ if anything breaks, Google knows what to fix “.

This methodology is seen as a significant competitive advantage over rivals like Microsoft’s Bing, which was described as using more complex and harder-to-debug ML techniques.

The process of “hand-crafting” involves engineers analysing relevant data, such as webpage content, user clicks, and feedback from human quality raters, and then applying mathematical functions, like regressions, to define the “curves” and “thresholds” that determine how a signal should respond to different inputs.

This human-in-the-loop system ensures that engineers can modify a signal’s behaviour to handle edge cases or respond to public challenges, such as the spread of misinformation on a sensitive topic.

This foundational layer of human-engineered logic provides the stability and predictability upon which more dynamic systems are built.

“Q* (page quality (i.e., the notion of trustworthiness)) is incredibly important. If competitors see the logs, then they have a notion of “authority” for a given site.” February 18, 2025, Call with Google Engineer HJ Kim (DOJ Case)

I agree – if this information were made available, it would be abused.

The emergence of these distinct systems – T* for query-specific relevance, Q* for static site quality, and Navboost for dynamic user-behaviour refinement – paints a clear picture of a modular, multi-stage ranking pipeline.

The process does not rely on a single, all-powerful algorithm.

Instead, it appears to be a logical sequence: initial document retrieval is followed by foundational scoring based on relevance (T*) and trust (Q*).

This scored list is then subjected to a massive re-ranking and filtering process by Navboost , which leverages the collective historical behaviour of users.

Only the small, refined set of results that survives this process is passed to the final, most computationally intensive machine learning models.
