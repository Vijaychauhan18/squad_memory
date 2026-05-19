---
source: https://patents.google.com/patent/US9424353B2/en
title: US9424353B2 - Related entities - Google Patents
scraped: 2026-05-18
tags: google, patent, related_entities, entity_search, serp_enrichment
topic: related_entities
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: entity expansion, related-entity blocks, and search-result enrichment hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US9424353B2 - Related entities - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US9424353B2/en

## Why This Matters
entity expansion, related-entity blocks, and search-result enrichment hypotheses

## Extracted Passages
- Methods, systems, and apparatus, including computer programs encoded on computer storage media, for receiving a first search query from a user device; receiving search results for the first search query provided by a search engine, wherein each of the search results identifies a respective resource; determining from the search results that the first search query relates to a first entity of a first entity type; determining that one or more entities of a second entity type have a predetermined relationship with the first entity; and transmitting information identifying the one or more entities of the second type to the user device as part of a response to the first search query.
- This application claims the benefit under 35 U.S.C. §119(e) of U.S. Patent Application No. 61/601,975, filed Feb. 22, 2012, entitled “Related Entities”, which is incorporated by reference herein in its entirety.
- Internet search engines aim to identify Internet resources (e.g., web pages, images, text documents, multimedia content) that are relevant to a user's needs and to present information about the resources in a manner that is most useful to the user. Internet search engines return a set of search results in response to a user submitted query. Internet search engines generally include one or more services that can classify particular received queries. Such services may include services that classify queries as one or more of: a query that is pornographic, i.e., is seeking pornographic results or for which a large number of search results identifying resources that have been classified as pornographic are returned; a query that is navigational to a particular resource, i.e., is seeking that particular resource; a query that is a local query, i.e., is seeking information about a business located near the user; or a query that is seeking a particular item of information, e.g., is looking for an item of information that is an answer to a question posed in the query.
- This specification describes technologies relating to identifying entities that are related to an entity to which a search query is directed.
- In general, one innovative aspect of the subject matter described in this specification can be embodied in methods that include the actions of receiving a first search query from a user device; receiving search results for the first search query provided by a search engine, wherein each of the search results identifies a respective resource; determining from the search results that the first search query relates to a first entity of a first entity type; determining that one or more entities of a second entity type have a predetermined relationship with the first entity; and transmitting information identifying the one or more entities of the second type to the user device as part of a response to the first search query.
- Other embodiments of this aspect include corresponding computer systems, apparatus, and computer programs recorded on one or more computer storage devices, each configured to perform the actions of the methods. A system of one or more computers can be configured to perform particular operations or actions by virtue of having software, firmware, hardware, or a combination of them installed on the system that in operation causes or cause the system to perform the actions. One or more computer programs can be configured to perform particular operations or actions by virtue of including instructions that, when executed by data processing apparatus, cause the apparatus to perform the actions.
- These and other embodiments can optionally include one or more of the following features. The first entity type can be the same as the second entity type. Determining that one or more entities of the second entity type have a predetermined relationship with the first entity can include: accessing an index that maps each of a plurality of entities to one or more related entities and identifies a relationship between the entity and one or more related entities.
- The method can further include: obtaining data identifying the first entity and the first entity type; obtaining data identifying the one or more entities of the second entity type and the relationship between the first entity and the one or more entities of the second entity type; and generating a mapping between the first entity and the one or more entities of the second entity type in the index.
- 1. A method performed by one or more computers, the method comprising: maintaining a related entity index that, for each of a plurality of entities, maps one or more related entities to the entity and identifies a relationship between the entity and the one or more related entities;
- maintaining an authoritative resources index that, for each entity of the plurality of entities, maps one or more authoritative resources to the entity, wherein each of the one or more authoritative resources is a resource whose occurrence in search results for a received search query has been determined to be an indicator that the received search query is directed to the entity;

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

