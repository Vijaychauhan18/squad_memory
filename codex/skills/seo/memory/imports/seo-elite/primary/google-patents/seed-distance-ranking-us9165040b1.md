---
source: https://patents.google.com/patent/US9165040B1/en
title: US9165040B1 - Producing a ranking for pages using distances in a web-link graph - Google Patents
scraped: 2026-05-18
tags: google, patent, seed_distance, link_graph, trust
topic: link_graph
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: trusted-neighborhood and graph-distance hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US9165040B1 - Producing a ranking for pages using distances in a web-link graph - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US9165040B1/en

## Why This Matters
trusted-neighborhood and graph-distance hypotheses

## Extracted Passages
- Methods, systems, and apparatus, including computer programs encoded on a computer storage medium, for producing a ranking for pages on the web. In one aspect, a system receives a set of pages to be ranked, wherein the set of pages are interconnected with links. The system also receives a set of seed pages which include outgoing links to the set of pages. The system then assigns lengths to the links based on properties of the links and properties of the pages attached to the links. The system next computes shortest distances from the set of seed pages to each page in the set of pages based on the lengths of the links between the pages. Next, the system determines a ranking score for each page in the set of pages based on the computed shortest distances. The system then produces a ranking for the set of pages based on the ranking scores for the set of pages.
- The present invention generally relates to techniques for ranking pages on the web. More specifically, the present invention relates to a method for producing a ranking for pages on the web by computing shortest distances from a set of seed pages to each of the pages to be ranked, wherein the seed pages and the pages to be ranked are interconnected with links.
- The relentless growth of the Internet has been largely fueled by the development of sophisticated search engines, which enable users to comb through billions of web pages looking for specific pages of interest. Because a given query can return millions of search results it is important to be able to rank these search results to present high-quality results to the user.
- A popular search engine developed by Google Inc. of Mountain View, Calif. uses PageRank® as a page-quality metric for efficiently guiding the processes of web crawling, index selection, and web page ranking. Generally, the PageRank technique computes and assigns a PageRank score to each web page it encounters on the web, wherein the PageRank score serves as a measure of the relative quality of a given web page with respect to other web pages. PageRank generally ensures that important and high-quality web pages receive high PageRank scores, which enables a search engine to efficiently rank the search results based on their associated PageRank scores.
- PageRank scores are computed based on the web link-graph structure, wherein the web pages are the nodes of the link-graph which are interconnected with hyperlinks. In this model, PageRank R for a given web page p can be computed as:
- ∀ p ∈ P , R ⁡ ( p ) = ( 1 - d ) + d ⁢ ∑ q → p ⁢ R ⁡ ( q )  q  out , ( 1 ) wherein P is the set of all the web pages, |q| out is the out-degree of a specific page q in the set P, and 0≦d≦1 is a damping factor.
- However, the simple formulation of Equation (1) for computing the PageRank is vulnerable to manipulations. Some web pages (called “spam pages”) can be designed to use various techniques to obtain artificially inflated PageRanks, for example, by forming “link farms” or creating “loops.”
- 1. A method for producing a ranking for pages on the web, comprising: receiving a plurality of web pages, wherein the plurality of web pages are inter-linked with page links;
- receiving n seed pages, each seed page including at least one outgoing link to a respective web page in the plurality of web pages, wherein n is an integer greater than one;
- assigning, by one or more computers, a respective length to each page link and each outgoing link;

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

