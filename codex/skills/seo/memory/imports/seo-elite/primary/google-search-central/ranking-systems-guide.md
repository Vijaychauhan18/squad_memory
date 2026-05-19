---
source: https://developers.google.com/search/docs/appearance/ranking-systems-guide
title: A guide to Google Search ranking systems
scraped: 2026-05-18
tags: google, official, ranking_systems, pagerank, systems
topic: ranking_systems
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: public ranking systems baseline and ranking update interpretation
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# A guide to Google Search ranking systems

Source type: official_doc
Original URL: https://developers.google.com/search/docs/appearance/ranking-systems-guide
Page updated label: 2025-12-10 UTC

## Why This Matters
public ranking systems baseline and ranking update interpretation

## Extracted Passages
- Google uses automated ranking systems that look at many factors and signals about hundreds of billions of web pages and other content in our Search index to present the most relevant, useful results, all in a fraction of a second. This page is a guide to understanding some of our more notable ranking systems. It covers some systems that are part of our core ranking systems, which are the underlying technologies that produce search results in response to queries. It also covers some systems involved with specific ranking needs.
- Our ranking systems are designed to work on the page level, using a variety of signals and systems to understand how to rank individual pages. Site-wide signals and classifiers are also used and contribute to our understanding of pages. Having some good site-wide signals does not mean that all content from a site will always rank highly, just as having some poor site-wide signals does not mean all the content from a site will rank poorly.
- We regularly improve our ranking systems through rigorous testing and evaluation and provide notice of updates to our ranking systems when those might be useful to content creators and others.
- You can also visit our How Search Works site to understand how our ranking systems , combined with other processes, work together so that Google Search delivers on our mission to organize the world's information and make it universally accessible and useful.
- Bidirectional Encoder Representations from Transformers ( BERT ) is an AI system Google uses that allows us to understand how combinations of words express different meanings and intent.
- Google has developed systems to provide helpful and timely information during times of crisis, whether those involve personal crisis situations, natural disasters, or other wide-spread crisis situations:
- Searches on Google may find thousands or even millions of matching web pages. Some of these may be very similar to each other. In such cases, our systems show only the most relevant results to avoid unhelpful duplication. Learn more about how deduplication works and how to see omitted results if desired, when deduplication happens.
- Deduplication also happens with featured snippets . If a web page listing is elevated to become a featured snippet, we don't repeat the listing later on the first page of results. This declutters the results and helps people locate relevant information more easily.
- Our ranking systems consider the words in domain names as one of many factors to determine if content is relevant to a search. However, our exact match domain system works to ensure we don't give too much credit for content hosted under domains designed to exactly match particular queries. For example, someone might create a domain name containing the words "best-places-to-eat-lunch" in hopes all those words in the domain name would propel content high in the rankings. Our system adjusts for this.
- We have various "query deserves freshness" systems designed to show fresher content for queries where it would be expected. For example, if someone is searching about a movie that's just been released, they probably want recent reviews rather than older articles from when production began. For another example, ordinarily a search for "earthquake" might bring back material about preparation and resources. However, if an earthquake happened recently, then news articles and fresher content might appear.
- We have various systems that understand how pages link to each other as a way to determine what pages are about and which might be most helpful in response to a query. Among these is PageRank, one of our core ranking systems used when Google first launched. Those curious can learn more by reading the original PageRank research paper and patent . How PageRank works has evolved a lot since then, and it continues to be part of our core ranking systems.
- We have systems that work to identify and surface local sources of news whenever relevant, such as through our "Top stories" and "Local news" features.
- Multitask Unified Model ( MUM ) is an AI system capable of both understanding and generating language. It's not currently used for general ranking in Search but rather for some specific applications such as to improve searches for COVID-19 vaccine information and to improve featured snippet callouts we display .
- Neural matching is an AI system that Google uses to understand representations of concepts in queries and pages and match them to one another.
- We have systems to help ensure we are showing original content prominently in search results, including original reporting , ahead of those who merely cite it. This includes support of a special canonical markup creators can use to help us better understand what is the primary page if a page has been duplicated in several places.
- Google has policies that allow the removal of certain types of content. If we process a significant volume of such removals involving a particular site, we use that as a signal to improve our results. In particular:
- Passage ranking is an AI system we use to identify individual sections or "passages" of a web page to better understand how relevant a page is to a search.
- RankBrain is an AI system that helps us understand how words are related to concepts. It means we can better return relevant content even if it doesn't contain all the exact words used in a search, by understanding the content is related to other words and concepts.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

