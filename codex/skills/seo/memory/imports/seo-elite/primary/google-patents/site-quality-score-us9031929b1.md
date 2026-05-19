---
source: https://patents.google.com/patent/US9031929B1/en
title: US9031929B1 - Site quality score - Google Patents
scraped: 2026-05-18
tags: google, patent, site_quality, ranking, quality_score
topic: site_quality
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: predictive or measured site-quality score hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US9031929B1 - Site quality score - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US9031929B1/en

## Why This Matters
predictive or measured site-quality score hypotheses

## Extracted Passages
- Methods, systems, and apparatus, including computer programs encoded on computer storage media, for determining a first count of unique queries, received by a search engine, that are categorized as referring to a particular site; determining a second count of unique queries, received by the search engine, that are associated with the particular site, wherein a query is associated with the particular site when the query is followed by a user selection of a search result that (a) was presented, by the search engine, in response to the query and (b) identifies a resource in the particular site; and determining, based on the first and second counts, a site quality score for the particular site.
- This application claims the benefit under 35 U.S.C. §119(e) of U.S. Provisional Application Ser. No. 61/583,602, filed on Jan. 5, 2012 entitled “SITE QUALITY SCORE,” the entirety of which is hereby incorporated by reference.
- This specification relates to ranking search results of search queries submitted to an Internet search engine.
- Internet search engines aim to identify resources, e.g., web pages, images, text documents, multimedia content, that are relevant to a user's information needs and to present information about the resources in a manner that is most useful to the user. Internet search engines generally return a set of search results, each identifying a respective resource, in response to a user-submitted query.
- This specification describes how a system can determine a score for a site, e.g., a web site or other collection of data resources, as seen by a search engine, that represents a measure of quality for the site. The score is determined from quantities indicating user actions of seeking out and preferring particular sites and the resources found in particular sites. A site quality score for a particular site can be determined by computing a ratio of a numerator that represents user interest in the site as reflected in user queries directed to the site and a denominator that represents user interest in the resources found in the site as responses to queries of all kinds The site quality score for a site can be used as a signal to rank resources, or to rank search results that identify resources, that are found in one site relative to resources found in another site.
- In general, one innovative aspect of the subject matter described in this specification can be embodied in methods that include the actions of determining a first count of unique queries, received by a search engine, that include a reference to a particular site; determining a second count of unique queries, received by the search engine, that are associated with the particular site, wherein a query is associated with the particular site when the query is followed by a user selection of a search result that (a) was presented, by the search engine, in response to the query and (b) identifies a resource in the particular site; and determining, based on the first and second counts, a site quality score for the particular site.
- Other embodiments of this aspect include corresponding computer systems, apparatus, and computer programs recorded on one or more computer storage devices, each configured to perform the actions of the methods. A system of one or more computers can be configured to perform particular operations or actions by virtue of having software, firmware, hardware, or a combination of them installed on the system that in operation causes or cause the system to perform the actions. One or more computer programs can be configured to perform particular operations or actions by virtue of including instructions that, when executed by data processing apparatus, cause the apparatus to perform the actions.
- These and other embodiments can optionally include one or more of the following features. A query includes a reference to the particular site when the query includes a site label identifying the particular site. A query includes a reference to the particular site when the query includes a term that has been determined to be a term that refers to the particular site. A query includes a reference to the particular site when the query is a query that has been determined to be a navigational query to the particular site. The user selection of a search result is an action received from a user that causes the resource identified by the search result to be presented, at least in part, to the user. Determining the site quality score comprises computing a ratio of a numerator and a denominator, wherein the numerator is based on the first count, and wherein the denominator is based on the second count. The numerator is based on the first count reduced by a threshold value. The numerator is a maximum of (a) a lower-bound value and (b) the first count reduced by a threshold value. The denominator is based on the second count raised to a power that is greater than zero and less than one. The denominator is a sum of a base value plus the second count raised to a power that is greater than zero and less than one.
- In general, another innovative aspect of the subject matter described in this specification can be embodied in methods that include the actions of determining a first count of user selections, received by a search engine, of search results that were presented in response to queries that are categorized as referring to a particular site; determining a second count of user selections, received by the search engine, of search results that identify resources in the particular site; and determining, based on the first and second counts, a site quality score for the particular site.
- 1. A computer-implemented method, the method comprising: determining a first count of unique queries, received by a search engine, that are categorized as referring to a particular site;
- determining a second count of unique queries, received by the search engine, that are associated with the particular site, wherein a query is associated with the particular site when the query is followed by a user selection of a search result that (a) was presented, by the search engine, in response to the query and (b) identifies a resource in the particular site; and
- determining a site quality score for the particular site including computing a ratio of a numerator based on the first count and a denominator based on the second count, wherein (i) the numerator is based on the first count reduced by a threshold value which is a predetermined threshold value, (ii) the denominator is based on the second count raised to a power that is greater than zero and less than one, or (iii) both.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

