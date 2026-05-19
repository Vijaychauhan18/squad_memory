---
source: https://www.hobo-web.co.uk/core-web-vitals-seo-after-the-google-content-warehouse-api-data-leaks/
title: Core Web Vitals SEO After The Google Content Warehouse API Data Leaks
scraped: 2026-03-23
published_on: 2025-10-03
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

# Core Web Vitals SEO After The Google Content Warehouse API Data Leaks

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/core-web-vitals-seo-after-the-google-content-warehouse-api-data-leaks/
Published: 2025-10-03
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
This article dissects the Google Content Warehouse API documentation leak in March 2024 with Core Web Vitals under the spotlight.

## Extracted Body
This article will dissect what the Google internal Content Warehouse API documentation leak in March 2024 tells us about Google’s real priorities, specifically focusing on how it reframes our understanding of Core Web Vitals (CWV) .

We will explore how these public-facing metrics are the tip of a very large iceberg – an iceberg composed of deep user behaviour analysis, powerful click-based re-ranking systems, and a vast collection of data points that go far beyond what Google publicly discusses.

My own work has long focused on the critical importance of website speed .

The data is unequivocal: 53% of mobile visits are abandoned if a page takes longer than three seconds to load .

The principles behind Core Web Vitals are not new to me or my readers; they are simply the quantification of a user-first philosophy SEOs like me have long advocated.

The leak doesn’t change the entire strategy; it just gives us a rare glimpse at the engineering schematics that power it.

It confirms that the focus must shift from attempting to please a secretive machine to demonstrably satisfying a now-quantifiable human user.

Google’s journey toward measuring user experience has been a long and evolutionary one.

It didn’t begin with Core Web Vitals. Its roots can be traced back to major quality updates like Panda in 2011, which aimed to demote low-quality content – a principle the leak confirms still influences current algorithms. This was followed by more explicit moves, such as making site security (HTTPS) a signal in 2014 and the mobile Page Speed update in 2018 .

This culminated in the formal announcement of Core Web Vitals in May 2020 , a key component of what Google called the “ Page Experience Update “. For the first time, Google provided a defined set of “real-world, user-centred metrics that quantify key aspects of the user experience”. The goal was to measure the “delightfulness” of a web page, moving beyond simple load times to capture a more holistic view of a user’s interaction.

The Google Content Data Warehouse Api leak contains references to both mobileCwv and desktopCwv and is explicitly used for “ranking changes,” cementing the direct connection between these metrics and ranking outcomes. For mobile specific research see my article: The Definitive Guide to Mobile SEO .

A critical part of this history is the evolution of the metrics themselves, which demonstrates Google’s refining understanding of user experience. On 12 March 2024, Google officially replaced First Input Delay (FID) with Interaction to Next Paint (INP) as the core responsiveness metric .

FID was a limited metric; it measured only the input delay of the first interaction a user had with a page . A site could pass the FID test with flying colours but still be sluggish and unresponsive for every subsequent interaction.

INP provides a far more comprehensive and meaningful measure. It assesses a page’s overall responsiveness by observing the latency of all click, tap, and keyboard interactions throughout the entire user session , reporting the longest interaction observed (while ignoring outliers).

This shift is crucial because it aligns with Chrome usage data showing that 90% of a user’s time on a page is spent after it loads. The change from FID to INP signals a strategic move by Google from measuring an isolated page load event to evaluating the quality of the entire user journey. It creates a technical performance metric that more closely mirrors genuine user satisfaction—or frustration.

Today, the Core Web Vitals consist of three specific metrics, each measuring a distinct facet of the user experience. To pass the overall assessment, a page must meet the “Good” threshold for all three, measured at the 75th percentile of page loads. This means that at least three out of every four users visiting your page should have an experience that meets the ‘Good’ benchmark.

The table below summarises the current metrics and their performance thresholds as defined by Google.

While LCP, INP, and CLS are the public metrics we are told to optimise for, the Content Warehouse API leak reveals that Google’s internal systems for measuring the underlying principles of user experience are far more direct and extensive.

The documentation confirms long-held theories and exposes the raw data points that CWV scores are, in effect, a proxy for.

The leak, corroborated by testimony from the DOJ v. Google antitrust trial, dismantles the myth of a single “Google Algorithm,” revealing instead a multi-layered processing pipeline. A page must successfully pass through a series of evaluation gates to rank.

The initial scoring is handled by a core system named Mustang , which evaluates foundational on-page factors. After this, the NavBoost system—using a rolling 13-month window of user click data—re-ranks results based on user behaviour. Finally, a layer of re-ranking functions called “Twiddlers” provides final editorial control, boosting content for things like freshness ( FreshnessTwiddler ) or quality ( QualityBoost ), or applying demotions.

This pipeline extends beyond traditional blue links. A parallel system named Glue uses user interaction data to rank universal search features like video carousels and knowledge panels. A final system called Tangram then assembles all these elements onto the search results page. This architecture proves that SEO is not about optimising for a single score, but about ensuring a page and its associated assets provide a satisfying experience at each distinct stage.

For years, Google spokespeople have publicly dodged or denied confirming using data from the Chrome browser for ranking purposes .

The leak suggests this is, at best, a semantic simplification .

The documentation explicitly references a module named chrome-api-data and contains attributes that are direct measures of site-wide engagement from Chrome users, such as chromeInTotal (total site views from Chrome) and siteClicks .

Most critically for our discussion, it includes an attribute called time-to-first-byte-per-doc .

Time to First Byte (TTFB) is a foundational server response metric; it measures how long it takes for a browser to receive the first byte of data from the server.

It is a precursor to every other speed metric and has a direct impact on LCP . The leak strongly implies that Google collects this performance data directly via Chrome, giving its systems near real-time performance insights long before that data is aggregated and anonymised for the public Chrome User Experience Report (CrUX).

Perhaps the most significant revelation related to user experience is the extensive detail on a system called NavBoost. While its existence was confirmed in the DOJ antitrust trial, the leak provides the technical specifics. The documentation describes it as “one of Google’s strongest ranking signals” and confirms it uses aggregated click data from user search journeys to re-rank results.

The system stores metrics that are unambiguous measures of user satisfaction, including:

These attributes represent a powerful feedback loop. When a user clicks a result and then quickly returns to the search page (a behaviour known as “pogo-sticking”), that is a classic badClick .

It signals to Google that the page did not satisfy the user’s intent. Conversely, a lastLongestClick indicates the user found what they were looking for and ended their search journey on that page—a strong signal of satisfaction. The documentation also references a SERP Demotion attribute, a direct signal for demotion based on user dissatisfaction observed on the search results page, likely measured by these very click patterns.

The connection to Core Web Vitals here is direct and causal. A poor technical experience is a leading cause of negative behavioural signals. Imagine a user clicks on your page. If it’s slow to load (poor LCP) and the layout shifts just as they try to tap a button (poor CLS), they will become frustrated and immediately click back.

This action is logged by NavBoost as a badClick . Core Web Vitals can therefore be understood as a preventative measure . By optimising for CWV, we are proactively improving the technical user experience to avoid triggering the negative behavioural flags that are measured by far more powerful and direct ranking systems like NavBoost. A good CWV score isn’t just about passing a test; it’s about preventing the negative user behaviour that these confirmed, high-impact systems are designed to detect and penalise.

Further cementing the importance of these metrics, the leak contains a specific model dedicated to storing Core Web Vitals data: GoogleApi.ContentWarehouse.V1.Model.IndexingMobileVoltCoreWebVitals . The documentation describes this as carrying the “field data metrics extracted from UKM aggregated 75-percentile data”. This is a direct confirmation that the very same 75th percentile field data we see in public CrUX reports is ingested and stored as a core attribute for mobile documents.

Interestingly, the model includes an attribute for fid , the now-deprecated First Input Delay.

Its presence suggests that even as public-facing metrics evolve, Google may retain historical data points for internal analysis and comparison , or that parts of the documentation reflect a snapshot in time during the transition to INP.

The connection is made even more explicit with another model found in the leak: GoogleApi.ContentWarehouse.V1.Model.IndexingMobileVoltVoltPerDocData . The description for this module is unambiguous, stating it is a protocol buffer where “The data is used for ranking changes.”

This model acts as a container for the page experience signals that are directly actioned for ranking. The documentation clarifies that “Only CWV signals and secure signal are stored” in this particular buffer, while other factors like MobileFriendliness are stored separately.

This finding is critical. It moves beyond simply confirming that Google stores CWV data and provides direct evidence of a specific data structure whose stated purpose is to use Core Web Vitals and HTTPS status for “ranking changes”.

The leak also confirms that Google’s systems understand the anatomy of a webpage with remarkable granularity. An attribute named pageregions indicates that Google encodes the positional ranges for different parts of a document, such as the header, footer, and main content. This strongly implies that content and links within the main body are valued more highly than those in boilerplate sections, directly impacting how signals like LCP (which often occur in the main content) are contextualised.

Furthermore, the documentation reveals that Google tracks the average weighted font size of terms, suggesting that words visually emphasised in headings or through bolding are given more weight. The documentation also reveals that core ranking systems like Mustang have a maximum number of tokens (words) they will process for a given page. This implies that extremely long content may be truncated, reinforcing the importance of placing the most critical information early in the document.

Most strategically, an attribute called contentEffort appears to be the technical foundation of the “Helpful Content System.” Described as an “LLM-based effort estimation,” this score likely quantifies the human effort invested in creating a piece of content , algorithmically separating high-value, original work from generic, easily replicated articles.

Core Web Vitals do not exist in a vacuum. They are a prominent component of a broader constellation of signals that Google’s core ranking systems use to evaluate the overall “Page Experience”. This framework also includes established factors like:

Within this group, CWV represents the most technically complex and dynamic set of signals, requiring ongoing attention.

The DOJ trial also confirmed the existence of a site-wide quality score , internally designated as Q * (pronounced “Q-star”).

This largely static, query-independent score functions as a domain authority metric, influencing the ranking potential of all pages on a site. The original PageRank algorithm is now understood to be just one of several inputs into this broader Q* signal.

A poor site-wide quality score can limit the performance of even the best individual pages , reinforcing the idea that page experience signals like Core Web Vitals contribute to a holistic assessment of a domain’s overall trustworthiness and quality.
