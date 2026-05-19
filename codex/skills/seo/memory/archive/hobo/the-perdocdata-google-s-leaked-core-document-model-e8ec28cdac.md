---
source: https://www.hobo-web.co.uk/perdocdata/
title: The PerDocData: Google's Leaked Core Document Model
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

# The PerDocData: Google's Leaked Core Document Model

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/perdocdata/
Published: 2025-10-05
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
Having spent 25 years analysing Google’s results pages, the leak of the PerDocData model is nothing short of a Rosetta Stone. At Hobo, I’ve always worked from the evidence we had, and to be fair, my analysis concludes that Google spokespeople has been open about this stu,ff in past briefings, albeit scattered across the web, ... Read more

## Extracted Body
Having spent 25 years analysing Google’s results pages, the leak of the PerDocData model is nothing short of a Rosetta Stone .

At Hobo, I’ve always worked from the evidence we had, and to be fair, my analysis concludes that Google spokespeople has been open about this stu,ff in past briefings, albeit scattered across the web, but this leak provides the blueprint SEOs have been looking for.

This article analyses the PerDocData structure, which can be understood as the comprehensive ‘digital dossier’ Google keeps on every single URL it indexes. It’s the central repository, the master file, that consolidates the vast array of signals we’ve spent our careers trying to influence.

This is no longer theory; this is documented data architecture.

The most critical finding from my analysis confirms a long-standing debate within the SEO community. Google’s ranking process is not a single, monolithic algorithm. Instead, it’s a pipeline.

A URL first achieves a relevance-based ranking, but crucially, it is then subjected to a series of re-ranking systems – internally called “Twiddlers” – that prioritise user-centric and quality-focused signals.

This is the mechanism behind why a keyword-optimised but low-quality page can get an initial foothold but will ultimately fail to maintain visibility.

For me and my team, this architecture fundamentally validates the strategic shift we’ve been advocating for years. The game is no longer just about establishing relevance. To achieve and maintain top rankings, you must prove your value to the subsequent “Twiddlers.”

This means our focus on user experience, content quality, and demonstrable authority isn’t just best practice—it’s a direct response to how Google’s core ranking pipeline is built.

To comprehend the significance of PerDocData , one must first understand its environment: the Google Content Warehouse (leaked in 2024) ..

This is not a simple database but a vast, sophisticated Application Programming Interface (API) and toolset designed for storing, managing, and analysing the web at an immense scale. It serves as the central repository where Google processes and organises all information it gathers about web content, acting as the foundational data layer for its search algorithms.

A document’s journey from discovery to being served in search results is a multi-stage pipeline. PerDocData is the data object that is populated and referenced throughout this process.

The process begins with Google discovering URLs through various means, including following links from known pages, processing submitted sitemaps, and other proprietary methods. This is the initial entry point into the system.

Once a URL is discovered and crawled, its content is fetched, rendered, and analysed. The processed document and its associated metadata are then stored in a suite of indexing systems. The documentation points to TeraGoogle as a primary system for long-term storage, with other systems like Alexandria also playing a role.

A critical component of this stage is a system named SegIndexer , which is responsible for placing documents into different tiers within the index. The scaledSelectionTierRank attribute provides a direct window into this system, confirming the long-held theory that Google maintains a tiered index with specific internal names: “Base, Zeppelins, and Landfills.”

A document’s rank within these serving tiers is a language-normalised score, indicating its fractional position within the index quality hierarchy.

This architecture dictates that links from documents residing in higher-quality tiers (like Base) carry significantly more weight than those from lower tiers (like Landfills).

This creates a distinct “link equity economy” where the value of a backlink is determined not just by the authority of the linking page itself, but also by the indexed “neighbourhood” it inhabits.

After indexing, the initial scoring and ranking of documents are handled by a primary system called Mustang . This system conducts the first-pass evaluation, creating a provisional set of results based on a multitude of signals stored within the PerDocData object for each document. This stage likely focuses on core relevance and foundational authority signals.

The process does not end with Mustang. The provisional results are passed to a powerful subsequent layer of the system known as “Twiddlers.” These are re-ranking functions that adjust the order of search results after Mustang’s initial ranking is complete. Twiddlers act as a fine-tuning mechanism, applying boosts or demotions based on specific, often dynamic, criteria. Examples referenced in the documentation include a FreshnessTwiddler , which boosts newer content, and a QualityBoost function. Another specific example is the SiteBoostTwiddler , which likely uses site-level signals to adjust rankings.

This multi-stage architecture reveals that search engine optimisation is not about solving for a single algorithm. It is a multi-stage optimisation problem. A document must first possess strong foundational relevance signals to pass the initial Mustang ranking.

Subsequently, it must exhibit the specific qualities – such as demonstrable user engagement, freshness for time-sensitive queries, or exceptional page experience—to be promoted by the various Twiddlers.

A page could rank well in the initial pass but be demoted by a Twiddler if it generates poor user click signals, or fail to be boosted if it is not considered fresh for a query that deserves it. A successful SEO strategy must therefore cater to both stages of this process.

The PerDocData object is structured as a Protocol Buffer, or Protobuf . This is a language-neutral, platform-neutral, and extensible mechanism for serialising structured data, developed and used extensively across Google’s infrastructure. Its selection is not arbitrary; it is critical for operating at Google’s scale. Key characteristics that make it suitable include:

Within the Content Warehouse, the PerDocData model is arguably the most interesting and critical Protobuf message for SEO analysis. It is the primary container for the vast majority of document-level signals used for indexing and serving search results. It is a key component of a larger CompositeDoc message, which aggregates all known information about a single URL. PerDocData is where on-page factors, quality scores, spam signals, freshness metrics, and user engagement data are stored and made accessible to the ranking pipeline.

This category includes signals that measure the overall trust, authority, and reputation of a page or an entire domain. These are foundational to Google’s assessment of a source’s reliability.

These attributes focus on the quality, originality, and value of the content on the page itself, separate from site-level metrics.

This group of signals is dedicated to identifying and filtering manipulative or low-value content designed to cheat the ranking systems.

These signals are derived from user interactions with the search results, providing direct feedback on the relevance and satisfaction of a given page.

These attributes help Google determine how important recent information is for a given query and how up-to-date a specific document is.

This category covers how Google understands the meaning, topics, and intent behind the content on a page, moving beyond simple keywords.

These signals relate to a page’s technical health, accessibility, and the user’s experience interacting with it, including speed and mobile-friendliness.

This group includes attributes essential for local search and serving results to a global audience in the correct language.

These are classifiers and data stores for specific types of content that require unique ranking considerations, such as books, videos, or scientific papers.

The PerDocData model provides clear evidence that Google’s evaluation of a document is heavily contextualised by the authority of the domain on which it resides. This transcends individual page metrics and points to a holistic, site-wide assessment.

The existence of attributes like siteAuthority and references to NSR (Normalized Site Rank) confirms that Google calculates a proprietary, site-level quality score. NSR is described as a sophisticated system for evaluating a website’s overall reliability, integrating a multitude of factors to assign a score that directly influences search rankings.

This definitively proves that while Google representatives correctly state they do not use third-party metrics like Moz’s Domain Authority, they have their own internal, and far more complex, equivalent. The long-debated concept of “domain authority” is therefore not a myth; it is a core, calculated metric within the Content Warehouse. This means that strategic activities aimed at building sitewide trust, brand recognition, and a clean backlink profile have a direct, measurable impact on a data point used in ranking. Further evidence of this holistic evaluation comes from attributes like fireflySiteSignal , an internal project name for another set of site-level signals that contribute to ranking changes.

The PageRankPerDocData module confirms that PageRank, while no longer a public-facing metric, remains a core ranking system. The documentation also references homepagePagerankNs , indicating that the PageRank of a site’s homepage is stored as a distinct and important signal. Furthermore, the historical toolbarPagerank attribute confirms that the public-facing 0-10 score was a stored value, cementing its past importance in the ecosystem. The role of PageRank has evolved significantly from its original conception. It is no longer a simple measure of link volume but has been integrated with anti-spam systems like Penguin to better combat link manipulation. It now serves as a foundational link equity signal that is factored into the broader calculation of a site’s overall authority.

The domainAge and hostAge attributes provide concrete evidence that Google tracks the inception date of hosts and domains, using this data specifically to “sandbox fresh spam.” This confirms that while age itself may not be a direct ranking boost, it is used as a trust signal in spam evaluation.

Finally, the queriesForWhichOfficial attribute is a powerful signal, storing the specific query, country, and language combinations for which a document is considered the definitive “official page.” This is a direct mechanism for ensuring that brand homepages or official entity sites rank for their primary navigational queries.

Google’s public-facing Search Quality Rater Guidelines provide a conceptual framework for content quality through concepts like E-E-A-T and YMYL. The PerDocData structure reveals how these abstract concepts are likely translated into concrete data points.

E-E-A-T (Experience, Expertise, Authoritativeness, and Trustworthiness) is not a single, direct score but a classification derived from an aggregation of many underlying signals. The various metrics within PerDocData serve as the inputs to a model that determines a page’s E-E-A-T level. For example:

For topics classified as YMYL (Your Money or Your Life)—such as health, finance, and safety—Google’s systems hold content to a significantly higher standard. The documentation provides concrete evidence of this with specific attributes like ymylHealthScore and ymylNewsScore . These fields store the outputs of dedicated classifiers for YMYL content in the health and news verticals. For documents identified as YMYL, the weighting of signals like siteAuthority , author credibility (via entity analysis), and factual accuracy is almost certainly increased dramatically.

The PerDocData model illustrates a fundamental evolution in Google’s content analysis: a definitive shift from matching keyword strings to understanding real-world entities and concepts.

The EntityAnnotations module is central to this process. It attaches specific Knowledge Graph entities that have been extracted from the page’s content. This transforms a simple document from a collection of words into an interconnected node in a web of knowledge. It allows Google to understand the things a page is about (e.g., the person “Harrison Ford,” the film series “Star Wars”) rather than just the text strings it contains. This process is facilitated by an internal system likely referred to as Webref , which provides the unique machine-readable IDs for entities, enabling the system to disambiguate between concepts with the same name (e.g., Apple the company versus apple the fruit).

Furthering this semantic understanding is the site2vecEmbeddingEncoded attribute. This represents a compressed vector embedding—a numerical representation—of an entire site’s content. In this machine learning model, the site’s collective themes and topics are mapped into a multi-dimensional space. This allows Google to mathematically measure the topical similarity between documents and even entire websites. It provides a quantifiable way to determine a site’s core focus and assess whether a new piece of content is topically consistent with the rest of the domain.

This technical implementation confirms that “topical authority” is not a vague marketing term but an algorithmically calculated concept. A website that maintains a tight focus on a specific set of related topics will generate a more coherent and powerful vector representation in this embedding space. Conversely, if a website focused on finance were to publish an article about gardening, the vector for that new article would be mathematically distant from the site’s established vector. This “topical deviation” can be measured and is likely used as a negative or dilutive signal, providing a technical basis for the long-standing strategic advice to maintain a clear topical focus and prune content that deviates from a website’s core subject area.

The granularity of analysis extends to the most basic on-page elements. Attributes like originalTitleHardTokenCount and titleHardTokenCountWithoutStopwords show that Google is not just reading titles, but analysing their structure and composition, counting the number of “hard tokens” (meaningful words) they contain.
