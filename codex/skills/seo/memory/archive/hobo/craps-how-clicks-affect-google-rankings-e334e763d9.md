---
source: https://www.hobo-web.co.uk/craps/
title: Craps: How Clicks Affect Google Rankings
scraped: 2026-03-23
published_on: 2025-10-12
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

# Craps: How Clicks Affect Google Rankings

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/craps/
Published: 2025-10-12
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
The ultimate ranking factor is the demonstrated ability to satisfy user intent, and the Craps model is the primary record of that satisfaction.

## Extracted Body
Disclaimer : This is not official. Any article (like this) dealing with the Google Content Data Warehouse leak requires a lot of logical inference when putting together the framework for SEOs, as I have done with this article. I urge you to double-check my work and use critical thinking when applying anything for the leaks to your site. My aim with these articles is essentially to confirm that Google does, as it claims, try to identify trusted sites to rank in its index. The aim is to irrefutably confirm white hat SEO has purpose in 2026 – and that purpose is to build high-quality websites. This article was first published on: 12 October 2025: Feedback and corrections welcome .

This will be my only article on the subject of clicks in Google Search.

I’ve gone to a certain depth, but the aim of the article is just to show how important user satisfaction is. I have stopped short of expanding in some areas (as I did with my link-building article ), as none of my articles are designed for abusing the system.

They are here to direct a strategy based on satisfying users and increasing rankings, not hacking Google.

Google representatives publicly and repeatedly denied that user click data was a significant ranking factor.

Analysts on the Google Search team, such as Gary Illyes, often described clicks as a “ very noisy signal ,” unsuitable for direct use due to potential manipulation.

In a particularly blunt dismissal of theories around dwell time and click-through rates (CTR), Illyes was quoted as saying:

“ Dwell time, CTR , whatever Fishkin’s new theory is, those are generally made up crap . Search is much more simple than people think. “

I remember that comment at the time and thinking it was a little stand out… Googlers don’t hate on folk in public in my experience.

These denials fuelled a long-standing debate in the SEO community, largely because they flew in the face of public experiments that suggested the opposite.

The Content Warehouse leaks and DO trial confirmed unequivocally – Google does use clicks when determining ranking .

But was Gary Ilyes pulling the greatest one-liner in SEO history, an iconic, ironic joke that evidently just flew over everyone’s heads?

During his time at Moz, Rand Fishkin (now of Sparktoro ) conducted several famous public experiments to test the theory that a high volume of clicks could influence a page’s ranking.

In one test, he sent out a tweet asking his followers to search Google for “REDACTED” and click the link to his blog. According to his analysis, after about 175-250 people participated, the page “shot up to the #1 position.” Fishkin concluded, “This clearly indicates (that in this particular case at least) that click-through-rate significantly influences rankings .”

In a second, even more dramatic experiment, he asked his followers to search for “REDACTED” and click on the result for REDACTED, which was ranking at number ten.

Over a 2.5-hour period, 375 people clicked the link. The result, as Fishkin noted, was that the website “shot up from number ten to the number one spot on Google.”

Google’s public response to these tests was that they did not prove direct usage of clicks for ranking. In a discussion with Rand Fishkin, Google’s Andrey Lipattsev suggested that the temporary ranking change was likely due to other factors, guessing that “ the burst of searches, social mentions, links, etc may throw Google off a bit and then they figure it out over time. “

This official stance – that clicks were too “noisy” and “gameable” for direct use – was maintained for years.

This Content Warehouse revelation carries a profound layer of irony in Illyes’s choice of words.

The documentation reveals a core ranking system module explicitly named “ Craps ,” which is defined as the system that processes “click and impression signals.”

The metrics it tracks – goodClicks , badClicks , and lastLongestClicks – are direct, quantifiable measures of user satisfaction that serve as sophisticated proxies for the very concepts of CTR and dwell time that were being derided .

“Dwell time, CTR, whatever Fishkin’s new theory is, those are generally made up crap. Search is much more simple than people think.” Gary Ilyes 2019 Reddit Thread

Whether this was a deliberate, meta-textual joke – a hidden admission veiled in dismissive language – is impossible to know.

Regardless of intent, the coincidence is striking and serves as a perfect encapsulation of the dynamic between Google’s public relations and its internal engineering reality: the very “crap” being publicly derided was, in fact, a named and critical component of the internal ranking architecture – called Craps .

I take my hat off to you, sir. The best one-liner from a Googler yet.

A.J. Kohn , who runs the firm Blind Five Year Old, has been a long-time proponent of the importance of user signals.

In fact, it was his blog I remember reading for the first time about all this, and I’ve referenced it many times over the years. It was he who introduced me to clicks and pogosticking in 2008 . A seminal SEO article , I have always thought. His thoughts always stuck with me.

Kohn frames the relationship between Google and SEO professionals as a high-stakes poker game , which explains the historical disconnect between the company’s public statements and its internal operations.

As A.J. Kohn stated, “We were playing a game of poker with Google, essentially, as SEOs. You know, when there are three suited cards when you hit the turn and I stare down Google and say, do you have a flush? I do not expect them to tell me the truth, right?” Kohn further explained, “ Like they’re not going to tell me what’s in their hand because that’s, they’re trying to win “.

For a decade, A.J. Kohn’s original research has pointed to the use of what he calls “implicit user feedback” – a term for the user click data Google collects from search results.

Citing Google’s own foundational patents, Kohn has argued that they are “littered with references” to this concept.

His analysis of internal Google presentations, made public during the antitrust trials, provides direct confirmation.

One such presentation from 2017 states, “ Yes, Google tracks all user interactions to better understand human value judgements on documents. “

Another from 2020 elaborates that the “basic game” is to start with a small amount of ‘ground truth’ data, then “look at all the associated user behaviors, and say, ‘ Ah, this is what a user does with a good thing! This is what a user does with a bad thing! ‘”

According to A.J. Kohn, this process is the very “ source of Google’s magic .”

The accidental publication of internal Google Content Warehouse API documentation in March 2024 provided an unprecedented look into the mechanics of modern search.

The leak provided a direct “blueprint” of the data structures that underpin Google’s ranking systems.

At the heart of this revelation is the QualityNavboostCrapsCrapsData protocol buffer, a module internally codenamed “ Craps .”

This data structure is the engine that captures, aggregates, and transports the user interaction signals that fuel Google’s most powerful ranking systems.

It is the raw material from which user satisfaction is measured.

The QualityNavboostCrapsCrapsData protocol buffer is the core data structure that captures the user interaction signals for the NavBoost system .

Understanding this data model is equivalent to understanding what Google values and how it quantifies user behaviour.

This protobuf serves as the container for click and impression data associated with a specific query-URL pair.

Each CrapsData message represents a summary of user interactions for one search result in the context of one search query, further segmented by various slices. It is not a log of a single user’s activity but rather an aggregation of many users’ interactions over time.

The key attributes country , device , and language define the primary slices for which data is aggregated separately. This ensures that when evaluating a URL for a query from a mobile user in France, the system uses a CrapsData record containing aggregated clicks from other mobile users in France, not from desktop users in the United States.

The sliceTag attribute provides an additional layer of flexibility, allowing for the creation of arbitrary new slices, indicating a system designed for continuous experimentation and refinement.

The structure of the CrapsData protobuf reveals a system in constant evolution.

It contains fields that are clearly marked as legacy (e.g., mobileData ), fields that are currently in use (e.g., mobileSignals ), and fields that are designated for future rollouts (e.g., squashed , unsquashed ).
