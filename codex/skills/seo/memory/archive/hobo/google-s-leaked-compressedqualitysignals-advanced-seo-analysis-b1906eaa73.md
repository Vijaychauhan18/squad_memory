---
source: https://www.hobo-web.co.uk/compressedqualitysignals/
title: Google's Leaked CompressedQualitySignals: Advanced SEO Analysis
scraped: 2026-03-23
published_on: 2025-10-05
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

# Google's Leaked CompressedQualitySignals: Advanced SEO Analysis

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/compressedqualitysignals/
Published: 2025-10-05
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
In my latest article about Google Content Warehouse leak I delve into the most important module of the whole leak (in my opinion). Navigating the world of search engine optimisation for a quarter of a century is to live in a state of perpetual adaptation. From the early, chaotic days of the monthly “Google Dance” ... Read more

## Extracted Body
In my latest article about Google Content Warehouse leak I delve into the most important module of the whole leak (in my opinion). Navigating the world of search engine optimisation for a quarter of a century is to live in a state of perpetual adaptation.

From the early, chaotic days of the monthly “Google Dance” to the seismic, industry-redefining shifts of named updates like Panda, Penguin, and the Helpful Content system, the landscape has been in constant, often turbulent, motion.

For years, the profession was locked in a reactive cycle: dissecting each new algorithm, chasing ranking ghosts, and attempting to reverse-engineer a black box. However, after decades of observation, a clearer picture emerges. The endless parade of updates is not a series of disconnected events, but a relentless, iterative march towards a consistent set of core principles.

The true art of modern SEO lies not in reacting to the latest tremor, but in understanding the tectonic plates of quality, authority, and user satisfaction that have been moving beneath the surface all along. This analysis moves beyond the named updates to examine the persistent, architectural signals that have been the true drivers of search evolution from the very beginning.

Before delving into the detailed analysis of the individual signals, it is crucial to clarify the relationship between the GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals module and the Q* system .

The CompressedQualitySignals module is not Q* itself. Rather, it is the collection of critical data inputs that the Q* system uses to perform its calculations.

Think of it this way: the module is the essential “cheat sheet” or “rap sheet” containing the pre-computed, compressed data points for a document – signals like siteAuthority, pandaDemotion, and navDemotion. Q* is the overarching system that reads this cheat sheet to calculate the final, aggregate quality score for a site or page.

Therefore, the module provides the data , while Q* is the system that processes that data to make a foundational judgment on quality.

Within the intricate architecture of Google’s search infrastructure lies a foundational component that profoundly influences a document’s ranking potential long before a user submits a query.

This component is the GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals module, a highly optimised message containing a curated set of per-document signals. Its purpose is to provide a rapid, at-a-glance quality assessment that feeds into Google’s primary ranking and serving systems, namely Mustang and TeraGoogle. Understanding this module is not merely a technical exercise; it is to understand the very first gate a document must pass to be considered for prominent ranking.

The module’s description reveals its critical role: “A message containing per doc signals that are compressed and included in Mustang and TeraGoogle.” This seemingly simple statement encapsulates a core principle of Google’s engineering: efficiency at a colossal scale. The signals are pre-calculated and stored for every document, forming a persistent quality profile. Their inclusion in two key systems highlights their dual function:

Preliminary scoring is a fundamental process in modern search engines, designed to manage immense datasets with finite computational resources. It functions as an initial quality filter, allowing the system to quickly triage billions of documents and discard those that are of demonstrably low quality before they enter the more resource-intensive phases of ranking. This initial culling is not a minor step; it is a decisive one that determines whether a document is even a candidate for ranking in the first place.

The documentation for this module contains a stark warning that underscores the importance of these signals: “CAREFUL: For TeraGoogle, this data resides in very limited serving memory (Flash storage) for a huge number of documents.” This hardware constraint is the driving force behind the module’s design. The limited, high-speed memory necessitates that only the most vital, information-dense signals are stored. Their presence in this exclusive set is a testament to their immense weight in the ranking process. These are not trivial data points; they are the distilled essence of a document’s quality, compressed to their most efficient form (e.g., converting floating-point values into 10-bit integers to save space).

This principle of compression also echoes a known spam detection technique. While the module’s compression is for data storage, research has shown that high textual compressibility can itself be a signal of low-quality, repetitive content like doorway pages. Thus, the engineering principle of compression is intertwined with the conceptual challenge of identifying low-quality content.

The very existence and architectural placement of the CompressedQualitySignals module confirm that a document’s fate is heavily influenced by pre-computed factors. Google maintains a persistent, pre-calculated “rap sheet” on every document, and this rap sheet forms the basis of all subsequent, more dynamic ranking calculations. The signals within this module are chosen because they are the most fundamental indicators of quality. They are the gatekeepers to the main ranking stages within Mustang, and a poor score here can effectively disqualify a document before the race has even begun. Therefore, any advanced SEO strategy must look beyond query-time factors and focus on building a fundamentally strong profile that positively influences these core, persistent signals.

At the heart of the CompressedQualitySignals module lies a set of signals that codify one of the most debated concepts in SEO: authority. For years, Google’s public stance has been to downplay the idea of a single, site-wide authority score. However, this internal documentation provides unequivocal evidence of such a system, centred around a core signal named siteAuthority and integrated into a comprehensive quality framework known as Q*.

The module contains a trio of signals that collectively define a site’s authoritative standing:

The term “Qstar” (or Q*) appears to be Google’s internal name for the aggregate quality score assigned to a document or site, with siteAuthority being a key input. This Q* score is the algorithmic embodiment of the E-E-A-T framework (Experience, Expertise, Authoritativeness, and Trust). Within this framework, Trust is considered the most critical component, as untrustworthy pages are deemed to have low E-E-A-T regardless of their other attributes. The unauthoritativeScore directly attacks the “Authoritativeness” and “Trust” pillars of E-E-A-T, thereby severely damaging a page’s overall Q* score.

The lineage of the siteAuthority signal reveals its connection to another core system: Normalised Site Rank (NSR). The documentation states that siteAuthority is converted from quality_nsr.SiteAuthority, linking it directly to a sophisticated, machine-learning-driven system designed to normalise and compare the quality of web content on a scale. This system is highly granular, computing site-level scores (Host NSR) by analysing a domain in sections, or sitechunks. This approach allows Google to derive a holistic authority score from a detailed, piece-by-piece evaluation of a website. The presence of a deprecated nsrConfidence signal further illustrates the system’s complexity, showing that Google even scores its own confidence in its NSR calculations.

The calculation of siteAuthority has evolved far beyond the original PageRank algorithm. It is a multi-vector composite score that fuses data from several distinct sources:

siteAuthority is not a simple link metric that can be easily manipulated. It is a persistent, composite score, calculated at the site or sub-domain level, that is “generally static across multiple queries”. This score functions as a site’s reputational baseline, blending link graph analysis, user behaviour signals, and topical focus. This creates a significant barrier to entry for new sites and a deep competitive moat for established, authoritative ones. An SEO strategy focused solely on acquiring links is therefore fundamentally incomplete. To influence this core signal, a strategy must also generate positive user engagement and maintain a clear, consistent topical focus.

The CompressedQualitySignals module serves as a living archive of Google’s most significant algorithmic shifts, and none are more prominent than the family of signals related to the Google Panda update. First launched in February 2011, Panda marked a pivotal moment in Google’s history, shifting the focus of SEO towards content quality. The signals in this module demonstrate that Panda is not a relic of the past but an active, integrated component of the core algorithm that continues to apply a powerful, site-wide demotion factor based on content quality.

The module contains a clear lineage of Panda-related signals, showing its evolution over time:

The Panda update was Google’s response to the proliferation of “content farms”—websites that mass-produced low-quality, “thin” content designed solely to rank for a vast number of keywords. It was designed to algorithmically identify and demote such sites, thereby rewarding sites with original, in-depth, and valuable content. Initially rolled out as a periodic filter, Panda was eventually integrated directly into Google’s core ranking algorithm, making its assessment continuous.

These signals are the technical manifestation of that integration. They algorithmically measure the core issues that Panda was designed to combat, including:

A crucial characteristic of the Panda algorithm, confirmed by both historical analysis and the nature of these signals, is its site-wide application. Panda affects the ranking of an entire site or significant sections of it, not just the individual pages that are of low quality. The pandaDemotion signal, being derived from SiteQualityFeatures, reinforces this principle. This means that a website with a substantial number of low-quality pages can have its overall visibility suppressed, negatively impacting the performance of even its highest-quality content.

The pandaDemotion signal functions as a form of “algorithmic debt.” Each low-quality page on a domain contributes to this debt. Once a certain threshold is crossed, a site-wide demotion is applied, acting as a handicap that actively suppresses the ranking potential of the entire domain. This explains a common frustration among webmasters: simply adding new, high-quality content often fails to improve a site’s overall performance if the pre-existing “debt” from old, low-quality pages is not addressed first. This debt must be “paid down” by systematically improving, consolidating, or removing the offending content. The system is designed to penalise the host for harbouring poor content, not just the individual pages themselves. This makes content audits, pruning, and quality hygiene not just best practices, but essential maintenance tasks to avoid accruing a persistent, site-wide penalty.

While content quality and site authority are foundational, the CompressedQualitySignals module makes it clear that Google’s assessment does not end there. A powerful set of signals is dedicated to quantifying user behaviour, both on the search results page and on the destination site itself. These signals are not mere correlational data points; they are tangible, pre-computed demotion factors that algorithmically punish a poor user experience. This system operates through a direct feedback loop, where negative user interactions are collected by a system called Navboost, processed by a system called CRAPS, and ultimately stored as demotion scores.

The module contains several signals that directly penalise negative user engagement:

Navboost is the data collection engine that fuels these behavioural signals. It is a vast system that stores and analyses user interaction data over a rolling 13-month period. It moves beyond simple click counts to capture a nuanced view of user satisfaction, including:

If Navboost is the data collector, CRAPS is the data processor. While the name’s origin is internal, it is thought to stand for Click and Results Prediction System. It is the ranking system that ingests the raw click and impression signals from Navboost and translates them into actionable scores. A key feature of this system is “squashing,” a normalisation function that prevents a single large signal (e.g., a sudden viral spike in clicks) from disproportionately manipulating the rankings, ensuring a more stable and balanced assessment of long-term user behaviour. The craps* signals stored in the CompressedQualitySignals module are the compressed, pre-computed output of this system.

This interconnected system creates a direct causal chain from user behaviour to a persistent ranking signal:

This feedback loop demonstrates that Google does not just reward good user experience; it actively and algorithmically punishes bad user experience. Signals like navDemotion and serpDemotion are not abstract concepts but tangible, pre-computed integer values that function as direct demotion multipliers in the ranking formula. A poor user experience is not a neutral attribute that simply fails to provide a boost; it is a quantifiable liability that actively harms a site’s visibility. This elevates user experience from a “best practice” to a critical, technical component of SEO, as failures in site architecture, usability, and intent matching result in a direct, measurable, and persistent penalty.

Beyond the broad, systemic demotions for low-quality content and poor user experience, the CompressedQualitySignals module contains a roster of signals designed to penalise specific, well-defined manipulative tactics. These signals function as algorithmic penalties, targeting practices that Google has historically sought to discourage. They provide a clear blueprint of what to avoid and demonstrate how Google has codified the enforcement of its spam policies directly into its preliminary scoring architecture.

The following table provides a consolidated overview of these algorithmic demotions, serving as a quick-reference guide for diagnosing potential penalties.

Google’s ranking algorithm is not a monolithic entity applying a single set of rules to all content. The CompressedQualitySignals module reveals the existence of specialised, fine-tuned sub-systems designed to evaluate specific, high-impact content verticals. This is most evident in the sophisticated set of signals for product reviews and the dedicated score for user-generated content (UGC). These signals demonstrate that Google applies different, context-aware quality criteria based on the type of content it is evaluating, moving far beyond a generic assessment of quality.

The module contains an entire suite of signals dedicated to the nuanced evaluation of product reviews, showing a system designed not just to demote poor content but to actively identify and promote exceptional examples:

This collection of signals reveals a multi-faceted system. It operates at both the page level (PromotePage, DemotePage) and the site level (PromoteSite, DemoteSite), indicating that Google assesses both individual reviews and the overall quality of a domain as a review source. The presence of a productReviewPUhqPage signal, likely standing for “Ultra High Quality Page,” shows a distinct classification for content that is not just good, but exceptional.

This entire system is the direct algorithmic implementation of Google’s Helpful Content Update and its specific guidelines for writing high-quality product reviews . These guidelines call for content that is written “by people, for people” and prioritises user value over search engine manipulation. The signals are designed to measure the very criteria outlined in these guidelines, such as:

A page that successfully meets these criteria would likely receive a positive score from signals like productReviewPPromotePage and productReviewPUhqPage, while a site that consistently publishes thin, unoriginal affiliate reviews would be penalised by productReviewPDemoteSite.

This signal, a score that is multiplied by 1000 and floored, is designed to assess the “effort” within a user-generated content page. This is a critically important signal in the current search landscape, where Google has made an explicit and significant pivot towards surfacing more authentic UGC, forum discussions, and conversational content from platforms like Reddit and Quora in its search results.

Google now views high-quality UGC as a valuable source of “information gain”—fresh perspectives and real-world experiences that cannot be found in professionally produced content. The ugcDiscussionEffortScore is the mechanism for distinguishing valuable UGC from low-quality spam. “Effort” in this context is likely a proxy for a collection of metrics that indicate a substantive and meaningful conversation, such as:

For websites that host community forums, Q&A sections, or comment threads, this signal represents a new frontier of SEO, sometimes referred to as “Community SEO” or “UGC SEO”. Optimising for a high ugcDiscussionEffortScore by fostering genuine, in-depth community engagement can provide a significant competitive advantage, as it aligns directly with Google’s stated goal of bringing more authentic, people-driven content into the SERPs.

The existence of these specialised signal sets proves that Google’s quality assessment is context-aware. A generic “write good content” strategy is no longer sufficient. To succeed, a content strategy must be precisely tailored to the specific quality criteria that Google has developed and codified for that content vertical. A product review must be approached differently from a forum discussion, as each is being measured against a distinct and specialised set of algorithmic yardsticks.

The CompressedQualitySignals module not only provides a snapshot of Google’s current ranking priorities but also offers a glimpse into the advanced mechanisms that drive its semantic understanding and its constant, dynamic evolution. Signals related to topical embeddings reveal how Google moves beyond keywords to a conceptual understanding of content, while a suite of experimental signals lays bare the framework for live, continuous testing of its core algorithms.

This signal stores versioned data related to topic embeddings. An embedding is a powerful machine-learning concept where words, sentences, or entire documents are represented as numerical vectors in a multi-dimensional space. The proximity of these vectors to one another allows a system to mathematically determine semantic similarity. In this context, topicEmbeddingsVersionedData is the raw data that allows Google to understand the core topics of a page and, by aggregation, an entire website.

This semantic understanding is not an abstract exercise; it is a critical input for calculating a site’s authority. As discussed in Section 1, signals like siteFocusScore and siteRadius are used to measure how topically coherent a website is. A site with a tight topical focus, where the embeddings of its pages are closely clustered, is considered more authoritative on that topic. The topicEmbeddingsVersionedData signal provides the foundational semantic data that fuels this crucial part of the authority calculation. The “versioned” aspect indicates that Google is continuously refining its embedding models and can test new versions alongside old ones.

The documentation for these signals is exceptionally revealing. It explicitly states that these fields are not propagated to the main index shards but are populated at serving time. Their purpose is to enable rapid Live Experiments, referred to internally as “0DayLEs,” with new components for the Q* quality score system.
