---
source: https://patents.google.com/patent/US8392443B1/en
title: US8392443B1 - Refining search queries - Google Patents
scraped: 2026-05-18
tags: google, patent, query_refinement, entities, query_expansion
topic: query_refinement
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: query refinement, entity-based reformulation, and query-follow-up hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US8392443B1 - Refining search queries - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US8392443B1/en

## Why This Matters
query refinement, entity-based reformulation, and query-follow-up hypotheses

## Extracted Passages
- Methods, systems, and apparatus, including computer program products, for refining search queries. In one implementation, a method includes obtaining a submitted search query, and in response to obtaining the search query: obtaining search results responsive to the search query; selecting a document from a group of documents identified by the search results; generating from a subset of one or more entities associated with the document one or more candidates for refined search queries, including: identifying one or more terms in the search query, where the one or more terms occur in the search query in a particular order relative to each other, and combining the one or more terms with the entity to generate a candidate, where the one or more terms occur in the particular order relative to each other; and identifying one or more of the candidates as being refined search queries for providing with the search results.
- This application claims the benefit under 35 U.S.C. §119(e) of U.S. Patent Application No. 61/160,841, titled “Refining Search Queries,” filed Mar. 17, 2009, which is incorporated herein by reference.
- This specification relates to data processing, and in particular, to computer implemented search services.
- Internet search engines provide information about Internet accessible resources (e.g., web pages, images, documents, multimedia content) that are responsive to a user's search query by returning a set of search results in response to the query. A search result includes, for example, a Uniform Resource Locator (URL) and a snippet of information for resources responsive to a query. The search results can be ranked (e.g., in an order) according to scores assigned to the search results by a scoring function.
- In general, one aspect of the subject matter described in this specification can be embodied in methods that include the actions of obtaining a submitted search query, and in response to obtaining the search query: obtaining search results responsive to the search query; selecting a document from a group of documents identified by the search results; generating from a subset of one or more entities associated with the document one or more candidates for refined search queries, including: identifying one or more terms in the search query, where the one or more terms occur in the search query in a particular order relative to each other, and combining the one or more terms with the entity to generate a candidate, where the one or more terms occur in the particular order relative to each other; and identifying one or more of the candidates as being refined search queries for providing with the search results. Other embodiments of this aspect include corresponding systems, apparatus, and computer program products.
- These and other embodiments can optionally include one or more of the following features. Generating the one or more candidates further includes determining that an entity is a candidate when a score associated with the entity is beyond a threshold score. Generating the one or more candidates further includes replacing a first identified term with a synonym of the first identified term when combining the one or more terms with the entity. The documents are each associated with a ranking, and selecting the document includes selecting a document with a ranking beyond a threshold ranking.
- The method further includes ranking each of the one or more entities according to a respective frequency of occurrence of the entity as a previously-submitted search query; and determining that the subset of the identified entities includes only the entities with a ranking beyond a threshold rank. The method further includes ranking each of the one or more entities according to a measure of a respective frequency of occurrence of the entity in the group of documents; and determining that the subset of the identified entities includes only the entities with a ranking beyond a threshold rank. The measure is an inverse document frequency (IDF).
- Particular embodiments of the subject matter described in this specification can be implemented to realize one or more of the following advantages. Refining search queries reduces how much user interaction is required to obtain alternatives to an input search query and perform searches using one or more of the alternatives. In addition to saving time, providing refined search queries can increase the precision, accuracy, and coverage of a search by capturing alternatives to the input search query that are directed to what a user may consider to be relevant to the search. The captured alternatives can help users better understand context associated with the input search query, help users better understand different, possible interpretations of the input search query, and help users resolve ambiguities caused by the different, possible interpretations.
- The details of one or more embodiments of the subject matter described in this specification are set forth in the accompanying drawings and the description below. Other features, aspects, and advantages of the subject matter will become apparent from the description, the drawings, and the claims.
- 1. A computer-implemented method comprising: obtaining a submitted search query, and in response to obtaining the search query: obtaining search results responsive to the search query;
- selecting a document from a group of documents identified by the search results;
- generating, from each entity text string in a subset of one or more entity text strings associated with the document, one or more candidates for refined search queries, including: identifying three or more terms in the search query that each have a respective term score satisfying a term threshold, where the three or more terms occur in the search query in a particular order relative to each other, and

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

