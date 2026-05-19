---
source: https://patents.google.com/patent/US7599914B2/en
title: US7599914B2 - Phrase-based searching in an information retrieval system - Google Patents
scraped: 2026-05-18
tags: google, patent, phrase_based_search, duplicate_detection, query_expansion
topic: phrase_based_retrieval
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: phrase-level retrieval, duplicate elimination, query expansion, and document-description generation hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US7599914B2 - Phrase-based searching in an information retrieval system - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US7599914B2/en

## Why This Matters
phrase-level retrieval, duplicate elimination, query expansion, and document-description generation hypotheses

## Extracted Passages
- An information retrieval system uses phrases to index, retrieve, organize and describe documents. Phrases are identified that predict the presence of other phrases in documents. Documents are the indexed according to their included phrases. Related phrases and phrase extensions are also identified. Phrases in a query are identified and used to retrieve and rank documents. Phrases are also used to cluster documents in the search results, create document descriptions, and eliminate duplicate documents from the search results, and from the index.
- The present invention relates to an information retrieval system for indexing, searching, and classifying documents in a large scale corpus, such as the Internet.
- Information retrieval systems, generally called search engines, are now an essential tool for finding information in large scale, diverse, and growing corpuses such as the Internet. Generally, search engines create an index that relates documents (or “pages”) to the individual words present in each document. A document is retrieved in response to a query containing a number of query terms, typically based on having some number of query terms present in the document. The retrieved documents are then ranked according to other statistical measures, such as frequency of occurrence of the query terms, host domain, link analysis, and the like. The retrieved documents are then presented to the user, typically in their ranked order, and without any further grouping or imposed hierarchy. In some cases, a selected portion of a text of a document is presented to provide the user with a glimpse of the document's content.
- Direct “Boolean” matching of query terms has well known limitations, and in particular does not identify documents that do not have the query terms, but have related words. For example, in a typical Boolean system, a search on “Australian Shepherds” would not return documents about other herding dogs such as Border Collies that do not have the exact query terms. Rather, such a system is likely to also retrieve and highly rank documents that are about Australia (and have nothing to do with dogs), and documents about “shepherds” generally.
- The problem here is that conventional systems index documents are based on individual terms, rather than on concepts. Concepts are often expressed in phrases, such as “Australian Shepherd,” “President of the United States,” or “Sundance Film Festival”. At best, some prior systems will index documents with respect to a predetermined and very limited set of ‘known’ phrases, which are typically selected by a human operator. Indexing of phrases is typically avoided because of the perceived computational and memory requirements to identify all possible phrases of say three, four, or five or more words. For example, on the assumption that any five words could constitute a phrase, and a large corpus would have at least 200,000 unique terms, there would approximately 3.2×10 26 possible phrases, clearly more than any existing system could store in memory or otherwise programmatically manipulate. A further problem is that phrases continually enter and leave the lexicon in terms of their usage, much more frequently than new individual words are invented. New phrases are always being generated, from sources such technology, arts, world events, and law. Other phrases will decline in usage over time.
- Some existing information retrieval systems attempt to provide retrieval of concepts by using co-occurrence patterns of individual words. In these systems a search on one word, such as “President” will also retrieve documents that have other words that frequently appear with “President”, such as “White” and “House.” While this approach may produce search results having documents that are conceptually related at the level of individual words, it does not typically capture topical relationships that inhere between co-occurring phrases.
- Accordingly, there is a need for an information retrieval system and methodology that can comprehensively identify phrases in a large scale corpus, index documents according to phrases, search and rank documents in accordance with their phrases, and provide additional clustering and descriptive information about the documents.
- An information retrieval system and methodology uses phrases to index, search, rank, and describe documents in the document collection. The system is adapted to identify phrases that have sufficiently frequent and/or distinguished usage in the document collection to indicate that they are “valid” or “good” phrases. In this manner multiple word phrases, for example phrases of four, five, or more terms, can be identified. This avoids the problem of having to identify and index every possible phrases resulting from the all of the possible sequences of a given number of words.
- 1. A computer-implemented method of selecting documents in a document collection in response to a query, the method comprising: receiving a query;
- identifying an incomplete phrase in the query, wherein other phrases predicted by the incomplete phrase in the document collection include only phrase extensions of the incomplete phrase;
- replacing the incomplete phrase with a phrase extension, wherein the phrase extension of the incomplete phrase is a super-sequence of the incomplete phrase that begins with the incomplete phrase, and wherein the incomplete phrase predicts the phrase extension based on a measure of an actual co-occurrence rate of the phrase extension and the incomplete phrase exceeding an expected co-occurrence rate of the phrase extension and the incomplete phrase in the document collection, the expected co-occurrence rate of the phrase extension and the incomplete phrase being a function of a plurality of occurrences of the phrase extension and the incomplete phrase in the document collection;

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

