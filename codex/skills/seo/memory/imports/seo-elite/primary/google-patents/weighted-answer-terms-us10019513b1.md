---
source: https://patents.google.com/patent/US10019513B1/en
title: US10019513B1 - Weighted answer terms for scoring answer passages - Google Patents
scraped: 2026-05-18
tags: google, patent, answer_scoring, term_vectors, question_answering
topic: answer_scoring
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: answer-passage scoring, term-vector weighting, and answer-quality estimation hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US10019513B1 - Weighted answer terms for scoring answer passages - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US10019513B1/en

## Why This Matters
answer-passage scoring, term-vector weighting, and answer-quality estimation hypotheses

## Extracted Passages
- Methods, systems, and apparatus, including computer programs encoded on a computer storage medium, for generating answer terms for scoring answer passages. In one aspect, a method includes accessing resource data describing a set of resources, identifying question phrases in the resources, for each identified question phrase in a resource, selecting in the resource a section of text subsequent to the question phrase as an answer, the answer having a plurality of terms, grouping the question phrases into groups of question phrases, and for each group: generating, from the terms of the answers for each question phrase in the group, answer terms and for each answer term, an answer term weight, and storing the answer terms and answer term weights in association with one or more queries.
- This application claims priority under 35 USC § 119(e) to U.S. Patent Application Ser. No. 62/036,457, filed on Aug. 12, 2014, the entire contents of which are hereby incorporated by reference.
- The Internet provides access to a wide variety of resources, such as image files, audio files, video files, and web pages. A search system can identify resources in response to queries submitted by users and provide information about the resources in a manner that is useful to the users.
- Users of search systems are often searching for an answer to a specific question, rather than a listing of resources. For example, users may want to know what the weather is in a particular location, a current quote for a stock, the capital of a state, etc. When queries that are in the form of a question are received, some search engines may perform specialized search operations in response to the question format of the query. For example, some search engines may provide information responsive to such queries in the form of an “answer,” such as information provided in the form of a “one box” to a question.
- Some question queries are better served by explanatory answers, which are also referred to as “long answers” or “answer passages.” For example, for the question query [why is the sky blue], an answer explaining Rayleigh scatter is helpful. Such answer passages can be selected from resources that include text, such as paragraphs, that are relevant to the question and the answer. Sections of the text are scored, and the section with the best score is selected as an answer.
- In general, one innovative aspect of the subject matter described in this specification can be embodied in methods that include the actions of accessing resource data describing a set of resources; identifying question phrases in the resources; for each identified question phrase in a resource, selecting in the resource a section of text subsequent to the question phrase as an answer, the answer having a plurality of terms; grouping the question phrases into groups of question phrases, and for each group: generating, from the terms of the answers for each question phrase in the group, answer terms and for each answer term, an answer term weight, and storing the answer terms and answer term weights in association with one or more queries.
- Particular embodiments of the subject matter described in this specification can be implemented so as to realize one or more of the following advantages. Answers can be checked for likely accuracy without a prior knowledge of the answer. A potentially large number of answer text sections for corresponding question phrases can be analyzed, and the contribution of particular answer text passage for answers that are likely to be the most accurate is increased. In some implementations, the pre-processing of answer text is used to generate weighted term vectors prior to query time. Thereafter, use of the weighted term vector at query time provides a lightweight but highly accurate scoring estimate of the accuracy of an answer passage. This improves the technology of answer generation. In particular, the generation of the term vector facilitates the ability to harness a multitude of available relevant answers, including those excluded from the top ranked resources for a query, by which the relevance of a candidate answer can be judged. Accordingly, long answers that are more likely to satisfy the informational need of users are more likely to surface.
- The details of one or more embodiments of the subject matter described in this specification are set forth in the accompanying drawings and the description below. Other features, aspects, and advantages of the subject matter will become apparent from the description, the drawings, and the claims.
- 1. A method performed by data processing apparatus, the method comprising: accessing resource data describing a set of resources;
- for each identified question phrase in a resource, selecting in the resource a section of text subsequent to the question phrase as an answer, the answer having a plurality of terms;

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

