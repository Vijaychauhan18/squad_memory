---
source: https://patents.google.com/patent/US8145617B1/en
title: US8145617B1 - Generation of document snippets based on queries and search results - Google Patents
scraped: 2026-05-18
tags: google, patent, snippets, paragraph_selection, query_matching
topic: snippet_generation
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: snippet generation, paragraph scoring, and snippet selection hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US8145617B1 - Generation of document snippets based on queries and search results - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US8145617B1/en

## Why This Matters
snippet generation, paragraph scoring, and snippet selection hypotheses

## Extracted Passages
- A document retrieval system generates snippets of documents for display as part of a user interface screen with search results. The snippet may be generated based on the type of query or the location of the query terms in the document. Different snippet generation algorithms may be used depending on the query type. Alternatively, snippets may be generated based on an analysis of the location of the query terms in the document.
- The present invention relates to an information retrieval system for generating snippets of documents in a large scale corpus, such as the World Wide Web.
- Information retrieval systems, generally called search engines, are now an essential tool for finding information in large scale, diverse, and growing corpuses such as the World Wide Web. Generally, search engines create an index that relates documents (or “pages”) to the individual words present in each document. A document is retrieved in response to a query containing a number of query terms, typically based on having some number of query terms present in the document. The retrieved documents are then ranked according to other statistical measures, such as frequency of occurrence of the query terms, host domain, link analysis, and the like. The retrieved documents are then presented to the user, typically in their ranked order, and without any further grouping or imposed hierarchy. In some cases, a selected portion or snippet of text of a document is presented to provide the user with a preview of the content of the document. Depending on the query terms and the document, the snippet may not provide useful information to the user to assess the relevance of the document to the query.
- There is a need for an information retrieval system and methodology that can provide more meaningful snippets.
- The present invention includes a system and methodology for generating snippets of documents retrieved during a search based on query terms. The snippet is generated based on the location of the query terms in the document. In one aspect, the paragraphs including the query terms are scored based on the length of the paragraph and the distance of the paragraph from a location of the document, such as the beginning of the document. A snippet is generated using a paragraph selected based on the score of the paragraph, such as the highest score.
- In another aspect, a snippet generating algorithm is selected based on the type of a query. The selected snippet generation algorithm generates a snippet of the document. The query type may be based on the form of the query terms or the location of query terms in the document. Thus, depending on the type of query, different snippet generation algorithms will be selected, and different types of snippets generated.
- The features and advantages described in the specification are not all inclusive and, in particular, many additional features and advantages will be apparent to one of ordinary skill in the art in view of the drawings, specification, and claims. Moreover, it should be noted that the language used in the specification has been principally selected for readability and instructional purposes, and may not have been selected to delineate or circumscribe the inventive subject matter.
- FIG. 1 is a block diagram illustrating the software architecture of a search system according to the present invention.
- FIG. 2 is a flowchart illustrating an exemplary methodology for generating a snippet according to the present invention.
- 1. A method for generating a snippet of a document, the method comprising: receiving a query comprising one or more query terms;
- identifying one or more paragraphs of the document, each identified paragraph including one or more of the query terms;

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

