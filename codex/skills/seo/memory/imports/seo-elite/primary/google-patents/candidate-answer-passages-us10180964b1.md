---
source: https://patents.google.com/patent/US10180964B1/en
title: US10180964B1 - Candidate answer passages - Google Patents
scraped: 2026-05-18
tags: google, patent, answer_passages, question_queries, passage_selection
topic: answer_passages
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: medium
canonical: true
canonical_group: Primary source patent
use_for: question answering, candidate answer passage generation, and answer-box selection hypotheses
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# US10180964B1 - Candidate answer passages - Google Patents

Source type: patent
Original URL: https://patents.google.com/patent/US10180964B1/en

## Why This Matters
question answering, candidate answer passage generation, and answer-box selection hypotheses

## Extracted Passages
- Methods, systems, and apparatus, including computer programs encoded on a computer storage medium, for generating candidate answer passages. In one aspect, a method includes receiving a query determined to be a question query data identifying resources determined to be responsive to the query; for each resource in a top-ranked subset of the resources: identifying a plurality of passage units in the resource; applying a set of passage unit selection criterion to the passage units, each passage unit selection criterion specifying a condition for inclusion of a passage unit in a candidate answer passage, wherein a first subset of passage unit selection criteria applies to structured content and a second subset of passage unit selection criteria applies to unstructured content; and generating, from passage units that satisfy the set of passage unit selection criterion, a set of candidate answer passages.
- This application claims priority under 35 USC § 119(e) to U.S. Patent Application Ser. No. 62/036,945 filed on filed Aug. 13, 2014, the entire contents of which are hereby incorporated by reference.
- The Internet provides access to a wide variety of resources, such as image files, audio files, video files, and web pages. A search system can identify resources in response to queries submitted by users and provide information about the resources in a manner that is useful to the users.
- Users of search systems are often searching for an answer to a specific question, rather than a listing of resources. For example, users may want to know what the weather is in a particular location, a current quote for a stock, the capital of a state, etc. When queries that are in the form of a question are received, some search engines may perform specialized search operations in response to the question format of the query. For example, some search engines may provide information responsive to such queries in the form of an “answer,” such as information provided in the form of a “one box” to a question.
- Some question queries are better served by explanatory answers, which are also referred to as “long answers” or “answer passages.” For example, for the question query [why is the sky blue], an answer explaining Rayleigh scatter is helpful. Such answer passages can be selected from resources that include text, such as paragraphs, that are relevant to the question and the answer. Sections of the text are scored, and the section with the best score is selected as an answer.
- In general, one innovative aspect of the subject matter described in this specification can be embodied in methods that include the actions of receiving a query determined to be a question query that seeks an answer response and data identifying resources determined to be responsive to the query and ordered according to a ranking; for each resource in a top-ranked subset of the resources: identifying a plurality of passage units in the resource, each passage unit being content from the resource and being eligible for inclusion into a candidate answer passage; applying a set of passage unit selection criterion to the passage units, each passage unit selection criterion specifying a condition for inclusion of a passage unit in a candidate answer passage, wherein a first subset of passage unit selection criteria applies to structured content and a second subset of passage unit selection criteria applies to unstructured content; and generating, from passage units that satisfy the set of passage unit selection criterion, a set of candidate answer passages, each candidate answer passage being eligible to be provided as an answer passage with search results that identify the resources determined to be responsive to the query and being separate and distinct from the search results. Other embodiments of this aspect include corresponding systems, apparatus, and computer programs, configured to perform the actions of the methods, encoded on computer storage devices.
- Particular embodiments of the subject matter described in this specification can be implemented so as to realize one or more of the following advantages. Candidate answer passages are generated from both structured content and unstructured content according to corresponding selection criteria. This allows the user to not only receive prose-type explanations, but also to receive a combination of prose-type and factual information, which, in turn, may be highly relevant to the user's informational need.
- When scoring the candidate answer passages, both query dependent and query independent signals are used. In the case of the former, the query dependent signals may be weighted based on the set of most relevant resources, which tends to surface answer passages that are more relevant than passage scored on a larger corpus of resources. This, in turn, reduces processing requirements and readily facilitates a scoring analysis at query time.
- 1. A method performed by data processing apparatus, the method comprising: receiving a query determined to be a question query that seeks an answer response and data identifying resources determined to be responsive to the query and ordered according to a ranking;
- for each resource in a top-ranked subset of the resources: identifying a plurality of passage units in the resource, each passage unit being content from the resource and being eligible for inclusion into a candidate answer passage;
- applying a set of passage unit selection criterion to the passage units, each passage unit selection criterion specifying a condition for inclusion of a passage unit in a candidate answer passage, wherein a first subset of passage unit selection criteria applies to structured content and a second subset of passage unit selection criteria applies to unstructured content; and

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

