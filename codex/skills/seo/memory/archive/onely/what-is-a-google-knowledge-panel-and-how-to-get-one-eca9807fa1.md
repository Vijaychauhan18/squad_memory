---
source: https://www.onely.com/blog/google-knowledge-panel/
title: What is a Google Knowledge Panel and How To Get One?
scraped: 2026-03-23
published_on: 2021-11-05
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# What is a Google Knowledge Panel and How To Get One?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/google-knowledge-panel/
Published: 2021-11-05
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Knowledge Panels serve information about entities right in search results - learn how to get a panel for your brand to improve its visibility!

## Extracted Body
Knowledge panels are infoboxes that appear in Google’s search results and show essential information about an entity and the connections between entities.

As we read in one of Google’s articles on knowledge panels , “Our systems aim to show the most relevant and popular information for a topic within a knowledge panel.”,

Understanding how Google generates knowledge panels and determines what data to show is vital for getting a knowledge panel for your business, brand, or perhaps for yourself.

Let’s see how knowledge panels can appear in search results and what you can do to get a panel for your organization, brand, or yourself.

To find the most in-depth information, I turned straight to the source and analyzed what Google’s patents tell us about how knowledge panels are generated!

A knowledge panel displaying crucial information about your business can significantly improve your search visibility. It can increase your engagement with customers, help you generate leads and turn them into business for your company.

Knowledge panels can appear in response to queries for entities in the Knowledge Graph.

Knowledge Graph is a database introduced by Google in 2012 populated with entities and information about them. Google can use the Knowledge Graph data to generate knowledge panels automatically.

This information can be taken from numerous authoritative sources and updated as information about an entity changes. There is also an option for the entities to suggest a change to their knowledge panels.

There are a few patents granted to Google that provide helpful details on:

I will describe the methods and concepts provided by the patents on the above topics and explain some things to optimize the information about your entity for knowledge panels.

The patent, filed soon after Google announced the introduction of the Knowledge Graph, is a comprehensive resource of methods for generating knowledge panels in search results.

Knowledge panels are generally provided for queries containing a reference to a particular entity. According to the patent, these entities can include “a person, place, country, landmark, animal, historical event, organization, business, sports team, sporting event, movie, song, album, game, work of art, or any other entity.”

The patent points out several key advantages of presenting knowledge panels in search results:

Presenting the knowledge panel with the search results reduces the number of web pages users have to visit in order to obtain factual information for which the users are searching, thereby reducing the time required for the users to find information that satisfies their informational needs. Knowledge panel templates developed for particular types of entities enable content relevant to the entities to be displayed to users. Knowledge panels can improve users’ search experiences, particularly for queries directed to learning, browsing, or discovery. For example, the knowledge panel supplies users with basic factual information or a summary of information about a particular entity referenced in a search query. Knowledge panels can assist users in navigating to related content seamlessly and naturally. Knowledge panels can supply new content that may not otherwise be encountered by a user without selecting several search results. Knowledge panels can also help users obtain information faster than they would if the users were required to click through multiple search results to obtain the information.

The general process for providing a knowledge panel looks like this:

The patent discusses knowledge panel templates, which specify types of content items to be included in the panel and contain placeholders for different content items, e.g., a title, one or more images, a set of facts, etc.

The system may use different templates, depending on the entity type and the information that may be presented. There are also templates for subtypes of entity types.

For example, the “person” entity type may also have a template for an “actor,” “singer,” or a “historical figure.”

All knowledge panel templates include certain standard content items, such as a title, image, description, and at least one fact about an entity. In addition, these items tend to be located in the same places to keep the panel format consistent.

The title of a knowledge panel can be the entity’s name or alias, and it may differ from the search query for which the panel was generated.

For example, a query may reference an alias or shortened name of a celebrity, but the title of the provided panel may include their full legal name.

Knowledge panels include factual information related to the particular entity, often presented as summaries of relevant details.

For example, a knowledge panel for a nation may contain its map and flag, official language, and other related facts.

When determining what facts to display in a knowledge panel, Google may consider past search queries referencing the given entity and provide details that answer these queries.

For instance, if a significant number of past queries referenced a person’s height, it may be included in this person’s knowledge panel.

The patent also tells us that, e.g., for a landmark, a panel can include:

It means that the information can be taken from multiple resources, in this case – two different websites.

Panels may contain images, as well as other interactive features, like audio or video files.

Queries received by the system can be associated with numerous distinct meanings. The system can identify content related to each of these meanings. In some situations, the panel can contain content for two or more distinct meanings.

According to the patent, knowledge panel results may vary in size. They tend to be larger than regular search results, taking up space of two, three, or more standard search results, but can also be the same size or smaller than a typical result.

Knowledge panels can also be located inline or adjacent to regular search results or in place of the other results. Looking at search results today, it seems that Google settled for adjacent positioning for desktop and inline for mobile.

This is another patent that focuses on methods for providing knowledge panels within search results when users are looking for specific entities.

The patent explains that topicality, determined with a partial topicality score, measures topical relatedness between a factual entity and search results.

For example, an official web page for a particular celebrity may have a higher topicality score than a web page containing content about many different celebrities.

The primary process for generating a knowledge panel is similar to the method from the previous patent, but a few elements are different.

After identifying the factual entities referenced by the search query, the system selects a particular entity for generating a knowledge panel. Then it measures topicality between the identified entities and the obtained search results before generating a knowledge panel based on, e.g., the content available for the entity.

The patent explains that there is an entity index containing data about known entities, including information about entity aliases.

The system may check whether the query refers to a known entity by comparing the received query or terms it contains to the entity index. The entity index could be a reference to the Knowledge Graph, which serves a similar purpose for Google.

Queries can refer to more than one entity or terms considered to be aliases of multiple entities.

The patent provides a lot of details on how multiple entities can be displayed in knowledge panels.

For such queries, associated with multiple distinct meanings, the system may provide the following types of knowledge panels:

The dominant entity knowledge panel can include, for a dominant entity:

There are a few factors that the system may consider in providing a knowledge panel for a query.

The patent provides an example of a Famous Actor who is associated with movie appearances and music.

We also read that the information regarding movies, albums, or songs associated with an entity can be shown in a table.

I have already described knowledge panel templates in my analysis of the Providing Knowledge Panels With Search Results patent, and this patent adds more to it.

When determining whether a knowledge panel should be shown, the system may look at not only what content is available for the entity but also the type of this content.
