---
source: https://www.hobo-web.co.uk/on-page-seo/
title: The Definitive Guide to On-Page SEO after the Google Leak
scraped: 2026-03-23
published_on: 2025-10-13
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

# The Definitive Guide to On-Page SEO after the Google Leak

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/on-page-seo/
Published: 2025-10-13
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
Discover a new, evidence-based SEO strategy based on the Google Content Warehouse leak. This guide explains how ranking systems like Mustang and NavBoost, along with signals for site authority and content effort, fundamentally change on-page optimisation for serious practitioners.

## Extracted Body
This is part 1 of 2 of my evidence-based framework for SEO (Search Engine Optimisation) strategy . Part 2 is my final post on Hobo SEO Blog (Thursday) .

TLDR : Based on the revelations from the Google Content Warehouse, an effective on-page SEO strategy should be built around the following core principles (which I explore in this article) :

This guide is for serious SEO practitioners. Want to know more? Here it is:

The accidental publication of Google’s internal Content Warehouse API documentation in March 2024 represents the most significant event in the history of Search Engine Optimisation.

Traditionally, the SEO industry operated on a combination of official guidance, reverse engineering, and hard-won intuition.

The leak, spanning over 2,500 pages and detailing 14,014 attributes across 2,596 modules, has irrevocably shifted this paradigm from one of inference to one of evidence

It provides an unprecedented, though incomplete , blueprint of the data points Google’s systems collect and evaluate to rank the web .

The most fundamental revelation from this documentation is the definitive dismantling of the myth of a single, monolithic “Google Algorithm.”

Google Search does not rely on one overarching formula but on a sophisticated, multi-layered ecosystem of interconnected microservices and specialised systems, each performing a distinct function, sometimes competing with each other within a broader processing pipeline.

Understanding this architecture is the new prerequisite for effective on-page SEO, as it reframes the objective from optimising for a single score to optimising a page’s successful passage through a series of distinct evaluation gates .

The leak reveals that for every document it processes, Google creates a master data object known as a CompositeDoc .

This can be thought of as the central file or container that holds all the disparate signals and attributes associated with a single URL.

It is within this CompositeDoc that the various modules and scores – from on-page quality signals ( qualitysignals ) and technical data ( robotsinfolist ) to user engagement metrics ( perDocData ) and link information ( anchors ) – are stored and organised.

This structure confirms that Google’s evaluation is a process of aggregation, where dozens of specialised analyses are compiled into a single, comprehensive profile for a webpage before it is ranked.

Insights from the DOJ v. Google antitrust trial, corroborated by the leak, reveal that Google’s ranking philosophy is built on two fundamental, top-level signals: a site-level quality score known as Q* (pronounced “Q-star”) and a popularity signal known as P* .

A trial exhibit stated plainly that “Q* (page quality (i.e., the notion of trustworthiness)) is incredibly important “.

This Q* score functions as a query-independent, largely static measure of a site’s overall quality.

The P* signal, meanwhile, captures the popularity of websites by using Chrome browsing data and analysing the number of links (anchors) between pages.

These two pillars serve as foundational inputs that guide subsequent processes, including how frequently a site’s pages are crawled.

Analysis of the leaked modules reveals a clear, sequential processing flow for how a document is scored, ranked, and ultimately presented to a user.

This pipeline consists of several key stages, each with its own set of priorities and signals.

At the heart of the initial ranking process lies a system named Mustang .

The documentation identifies Mustang as the primary engine responsible for the initial scoring, ranking, and serving of search results . This system is where the foundational, intrinsic qualities of a web page are evaluated.

Many of the traditional on-page SEO factors – such as the relevance of a title tag to a query , the originality of the content , and the presence of spam signals – are likely processed and scored within this core system.

A page’s journey through the ranking process begins here; a page must first qualify based on its fundamental on-page characteristics to even be considered for subsequent, more dynamic evaluations .

The DOJ trial revealed that “ Topicality ” is a formal, engineered system within Google, designated as T* .

Its explicit function is to compute a document’s fundamental, query-dependent relevance , serving as a “base score” that answers the question: how relevant is this document to the specific terms used in this search query ?

These three signals are combined in what was described as a “relatively hand-crafted way” to generate the final T* score, allowing engineers to understand and adjust how each factor contributes to relevance.

Once Mustang has produced an initial set of rankings, a powerful re-ranking system called NavBoost comes into play.

The leak provides overwhelming confirmation of this system, which was previously alluded to in documents from the DOJ antitrust trial.

NavBoost is one of Google’s strongest and most influential ranking signals , and its function is to adjust the initial rankings based on vast logs of user behaviour data. The system is trained on a rolling 13-month window of aggregated user click data.

The documentation reveals that NavBoost operates on click and impression data from systems internally referred to as “Glue” (a comprehensive query log) and “Craps” (a system for processing click and impression signals).

This system doesn’t just count raw clicks; it analyses nuanced patterns of user engagement to determine satisfaction.

A page that performs well in Mustang’s content-based evaluation can be significantly promoted or demoted by NavBoost depending on how real users interact with it in the search results.

The QualityNavboostCrapsAgingData module further reveals that this click data is segmented into age-based buckets, such as lastWeekBucket and lastMonthBucket , showing that the system analyses user behaviour in the context of a document’s age. Read more about the Google Craps system .

This stage acts as a crucial validation layer, where the theoretical relevance of a page is tested against its demonstrated utility.

Following the initial scoring by Mustang and the user-behaviour adjustments by NavBoost, the leak reveals a final, powerful layer of the system known as “Twiddlers.”

These are re-ranking functions that provide Google with final editorial control over its search results. A Twiddler can adjust the score of a document or change its ranking entirely based on a specific set of criteria, acting as a final overlay to fine-tune the SERPs.

The documentation references several types of these re-ranking functions, illustrating their versatility:

This multi-stage architecture – Mustang for initial scoring, T* for relevance, NavBoost for user validation, and Twiddlers for final editorial adjustments – fundamentally alters the strategic calculus of on-page SEO.

A page can be perfectly optimised with relevant keywords and structured content to achieve a high score from Mustang, but if users consistently click on it and immediately return to the search results, it will be demoted by NavBoost.

Similarly, a page that satisfies both Mustang and NavBoost could still be suppressed by a Twiddler if it’s in a sensitive niche like product reviews and is deemed to be of low quality.

Therefore, modern on-page SEO is not about achieving a single, static score; it is about ensuring a page successfully qualifies, is validated, and avoids demotion at each distinct gate in the ranking pipeline.

The leak provides a fascinating look into the very structure of Google’s index, revealing it is not a monolithic, flat database but a highly structured and tiered system designed for efficiency.

This architecture, managed by systems like Alexandria , SegIndexer , and TeraGoogle , has direct implications for how content is valued and accessed.

The index is arranged in tiers based on a document’s importance and update frequency.

The most critical, frequently updated, and regularly accessed content is stored in high-speed flash memory for rapid retrieval. Less important content is kept on solid-state drives, while rarely updated or accessed content is relegated to standard hard drives.

This tiered structure means that a page’s perceived quality and freshness can determine its physical placement within Google’s infrastructure, affecting how quickly it can be processed and served in rankings.

This sophisticated storage system maintains an extensive historical record of the web.

The leak confirms that Google keeps a copy of all versions of every page it has ever indexed, with analysis suggesting it primarily uses the last 20 changes to a URL when analysing links.

This, combined with the documentHistory demotion for new URLs, underscores that changing a URL is a significant and costly action. See here for more on how to SEO URLs .

It potentially resets the page’s history, discarding the accumulated trust and forcing the new URL to start over.

This reinforces the critical importance of careful URL planning and the use of permanent (301) redirects when changes are absolutely necessary.

The leaked documentation confirms that the ranking URL is far from a simple, passive address for a document. Instead, Google’s systems treat the URL and its host domain as an active source of signals that are evaluated for trust, history, context, and potential spam.

This analysis begins before the content of the page is even fully considered, establishing a foundational layer of trust – or distrust – that influences all subsequent evaluations

For years, Google representatives have publicly and repeatedly denied the existence of a “sandbox” – a probationary period where new websites are temporarily suppressed in search results. The leaked documentation directly contradicts these statements.

Within the PerDocData module, the documentation details an attribute named hostAge .

Its description explicitly states that it is used “to sandbox fresh spam in serving time”. This is further supported by the registrationinfo attribute, which stores the creation and expiration dates of the domain, and the domainAge attribute, which tracks the age of the entire domain, reinforcing the concept of temporal trust.

This system is not a blanket penalty but appears to be a risk-management feature designed to observe a new host and prevent low-quality or spammy sites from achieving prominent rankings before they have established a track record.

Hostage does not mandate a blanket penalty for every new site. It strictly identifies a mechanism for neutralising fresh spam . However, because the line between an unverified new site and sophisticated fresh spam is so blurry to an algorithm, the practical effect on the SERPs often looks identical. This is the very gap where a disconnected entity splits.

The only way to bypass or accelerate through that algorithmic suspicion is by ensuring every single page relentlessly puts the customer first, forcing those positive interaction signals as quickly as possible.

hostAge (type: integer(), default: nil) – The earliest firstseen date of all pages in this host/domain. These data are used in twiddler to sandbox fresh spam in serving time . It is 16 bit and the time is day number after 2005-12-31, and all the previous time are set to 0. If this url’s host_age == domain_age, then omit domain_age Please use //spam/content/siteage-util.h to convert the day between epoch second. Regarding usage of Sentinel values: We would like to check if a value exists in scoring bundle while using in Ranklab AST. For this having a sentinel value will help us know if the field exists or has a sentinel value (in the case it does not exist). 16-bit

This temporal evaluation extends beyond the host level to individual pages. The documentation references a demotion factor called documentHistory . This signal indicates that a “page without history, or a URL that is new to Search” will have its score negatively impacted.

A brand-new website launching its first pages is subject to both the hostAge sandbox at the domain level and the documentHistory demotion at the page level. In contrast, a new page published on an established, trusted domain would bypass the hostAge filter but would still need to overcome the initial hurdle of the documentHistory demotion.

This structure suggests a “temporal trust” model where Google’s default state for any new digital asset – be it a host or a page – is one of inherent distrust.

The mechanism for graduating from this probationary status is likely the accumulation of positive signals, such as a history of positive user engagement ( goodClicks ) and the acquisition of high-quality backlinks, which serve to validate the asset’s quality and utility.

Google’s systems actively parse the URL string itself for signals, particularly for date information. The leak identifies an attribute called syntacticDate and another called urldate , both of which are dates extracted directly from the URL or the page’s title.

For example, publishing an article with the URL /blog/best-laptops-for-2024/ creates a permanent, unchangeable syntacticDate signal of “2024.”

While this may be beneficial in the short term, in subsequent years it can create a signal conflict if the content is updated.

An article updated for 2025 with a new byline date will still carry the immutable “2024” signal in its URL, potentially confusing freshness systems.

This provides a strong, data-backed argument for using evergreen URL structures that omit dates or other volatile keywords, thereby avoiding built-in signal conflicts and preserving the historical value of the URL over the long term.

In an AI-powered search ecosystem, these stable, descriptive URLs become even more critical, acting as a “ Canonical Source of Ground Truth ” that helps AI systems confidently connect a piece of content to a specific entity.

While domain-level and user-behaviour signals are critically important, the foundation of on-page SEO remains the content and structure of the page itself.

The leaked documentation provides an unprecedented look into the specific attributes and scores that Google’s Content Warehouse uses to deconstruct, analyse, and evaluate the textual and structural elements of a ranking URL.

These features are likely primary inputs for the Mustang ranking system.

The analysis of a page begins with its most fundamental elements: the title and the body content. The leak confirms several long-held SEO best practices and reveals new layers of sophistication in how content is scored.

The leak reveals that Google’s understanding of “freshness” is far more advanced than simply looking at a publication date. The system uses a trio of attributes to build a comprehensive picture of a document’s timeliness, along with signals about significant updates.

This multi-faceted approach is a clear defence against “freshness spam,” where a publisher might simply change the content BylineDate without actually updating the content.

A true content freshness strategy must focus on updating the core substance of the information, not just the metadata.

Beyond the raw text, Google’s systems evaluate who wrote the content, how it is structured, and even how it is visually presented.

The leak confirms that technical page experience signals are stored on a per-document basis, moving them from abstract best practices to concrete, measured attributes.

The voltData module contains page UX signals, while the desktopInterstitials attribute specifically targets and likely penalises the use of intrusive pop-ups on desktop devices.

The viewport meta tag is also a critical signal, essential for mobile-friendliness and a core part of the overall Quality (Q*) score.

This provides definitive evidence that a poor user experience, enforced through technical means, can be a direct negative factor for a page. Mobile seo should be your priority .

To synthesise these findings, the following table outlines the most critical on-page attributes revealed in the leak, their function, and their strategic implications for SEO.

Among the most strategically significant revelations from the leak is the existence of an attribute named contentEffort . This metric represents a sophisticated, machine-learning-driven attempt to quantify a previously abstract concept: the amount of human effort invested in creating a piece of content.

Defined in the documentation as an “LLM-based effort estimation for article pages,” contentEffort is a variable within the QualityNsrPQData module, placing it at the heart of Google’s page quality evaluation systems.

This attribute is not just another signal; it appears to be the technical foundation of Google’s “Helpful Content System” (HCS) , which aims to reward content created for people and penalise content made primarily for search engines .

The contentEffort score seems to be calculated based on an assessment of the “ease with which a page could be replicated”.

Content that is generic, formulaic, or lacks unique insight can be easily reproduced by competitors or AI models and would likely receive a low contentEffort score.

Conversely, content that is rich with original research, expert interviews, custom visuals, and deep analysis is difficult and expensive to replicate, signalling a high-value, non-commoditised asset deserving of a higher score.

A low contentEffort score may act as a primary classifier for unhelpful content, potentially triggering the site-wide demotion associated with the HCS.

Perhaps the most significant area where the leak exposed a chasm between Google’s public statements and its internal practices is the role of user engagement data in ranking.

For years, Google spokespeople have consistently downplayed or outright denied the use of clicks and other user behaviours as direct ranking signals, often framing them as useful only for evaluation or personalisation.

The documentation paints a very different picture, providing overwhelming evidence that user interaction data, collected from both search results and the Chrome browser, is a primary mechanism for validating and re-ranking content.

This reveals a two-part definition of quality within Google’s systems.
