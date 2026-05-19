---
source: https://patents.google.com/patent/US9953049B1/en
title: US9953049B1 - Producing a ranking for pages using distances in a web-link graph - Google Patents
scraped: 2026-05-18
tags: google, patent, seed_distance, link_graph, authority
topic: link_graph
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: authority flow and seed-set ranking hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US9953049B1 - Producing a ranking for pages using distances in a web-link graph - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US9953049B1/en

## Why This Matters
authority flow and seed-set ranking hypotheses

## Extracted Passages
- One embodiment of the present invention provides a system that produces a ranking for web pages. During operation, the system receives a set of pages to be ranked, wherein the set of pages are interconnected with links. The system also receives a set of seed pages which include outgoing links to the set of pages. The system then assigns lengths to the links based on properties of the links and properties of the pages attached to the links. The system next computes shortest distances from the set of seed pages to each page in the set of pages based on the lengths of the links between the pages. Next, the system determines a ranking score for each page in the set of pages based on the computed shortest distances. The system then produces a ranking for the set of pages based on the ranking scores for the set of pages.
- This is a continuation of U.S. application Ser. No. 11/546,755, filed Oct. 12, 2006, the disclosure of which is hereby incorporated by reference in its entirety.
- The present invention generally relates to techniques for ranking pages on the web. More specifically, the present invention relates to a method for producing a ranking for pages on the web by computing shortest distances from a set of seed pages to each of the pages to be ranked, wherein the seed pages and the pages to be ranked are interconnected with links.
- The relentless growth of the Internet has been largely fueled by the development of sophisticated search engines, which enable users to comb through billions of web pages looking for specific pages of interest. Because a given query can return millions of search results it is important to be able to rank these search results to present high-quality results to the user.
- A popular search engine developed by Google Inc. of Mountain View, Calif. uses PageRank® as a page-quality metric for efficiently guiding the processes of web crawling, index selection, and web page ranking. Generally, the PageRank technique computes and assigns a PageRank score to each web page it encounters on the web, wherein the PageRank score serves as a measure of the relative quality of a given web page with respect to other web pages. PageRank generally ensures that important and high-quality web pages receive high PageRank scores, which enables a search engine to efficiently rank the search results based on their associated PageRank scores.
- PageRank scores are computed based on the web link-graph structure, wherein the web pages are the nodes of the link-graph which are interconnected with hyperlinks. In this model, PageRank R for a given web page p can be computed as:
- ∀ p ∈ P , R ⁡ ( p ) = ( 1 - d ) + d ⁢ ∑ q ⁢ → p ⁢ R ⁡ ( q )  q  out , ( 1 ) wherein P is the set of all the web pages, |q| out is the out-degree of a specific page q in the set P, and 0<d<1 is a damping factor.
- However, the simple formulation of Equation (1) for computing the PageRank is vulnerable to manipulations. Some web pages (called “spam pages”) can be designed to use various techniques to obtain artificially inflated PageRanks, for example, by forming “link farms” or creating “loops.”
- One possible variation of PageRank that would reduce the effect of these techniques is to select a few “trusted” pages (also referred to as the seed pages) and discovers other pages which are likely to be good by following the links from the trusted pages. For example, the technique can use a set of high quality seed pages (s 1 , s 2 , . . . , s n ), and for each seed page i=1, 2, . . . , n, the system can iteratively compute the PageRank scores for the set of the web pages P using the formulae:
- 1. A method, comprising: obtaining data identifying a set of pages to be ranked, wherein each page in the set of pages is connected to at least one other page in the set of pages by a page link;
- obtaining data identifying a set of n seed pages that each include at least one outgoing link to a page in the set of pages, wherein n is greater than one;
- accessing respective lengths assigned to one or more of the page links and one or more of the outgoing links; and

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

