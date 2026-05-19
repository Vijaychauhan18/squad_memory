---
source: https://patentcore.digital/blog/search-with-stateful-chat-patent-us20240289407a1/, https://patents.google.com/patent/US20240289407A1/en
title: Google Patent US20240289407A1 - Stateful Chat Search
scraped: 2026-04-21
tags: google patents, stateful chat, ai mode, synthetic queries, grounding, multi turn search
topic: patent_research, ai_search, retrieval_architecture
intent: research, strategy, diagnostics
role: coral, researcher, pinchy
confidence: high
canonical: true
canonical_group: Google Patent Core 2026
use_for: ai_mode_like_architecture, session_search, query_fan_out, grounding_and_verification
avoid_for: saying_ai_mode_equals_this_patent_exactly
---

# Core Concept
`US20240289407A1` describes a multi-turn search framework where retrieval, context persistence, generative models, synthetic queries, and grounding operate in one stateful session.

## Official Patent Record
- Publication: `US20240289407A1`
- Title: `Search with stateful chat`
- Prior art date: `2023-02-28`
- Filing date: `2024-02-27`
- Publication date: `2024-08-29`
- Assignee: `Google LLC`
- Inventors: `Mahsan Rofouei`, `Anand Shukla`, `Qing Wei`, `Chi Tang`, `Ryan Brown`, `Enrique Piqueras`
- Legal status: `Pending`

## Practical Mechanism
- The system receives a query and contextual information tied to the user or device.
- It generates generative-model output, then creates one or more synthetic queries.
- It retrieves documents responsive to both the original and synthetic queries.
- It processes state data to classify the query and choose downstream generative models.
- Patent Core highlights a grounding layer where generated output is semantically verified against source documents.

## SEO Reading
- This is one of the clearest architecture notes for session-aware search and AI Mode style behavior.
- A page may be surfaced because it helps one sub-query or follow-up in a session, not because it wins a single ten-blue-links ranking contest.
- Groundable passages, follow-up coverage, and consistent topic context become more important than isolated keyword wins.

## What To Reuse
- Build pages that answer the main query plus adjacent implied questions.
- Write chunkable sections that are easy to ground, cite, or summarize.
- Make entity references, factual claims, and supporting evidence explicit enough for verification.
- Use this note whenever the task is about query fan-out, AI-search visibility, or multi-turn retrieval logic.

## Small Details Worth Remembering
- The claims explicitly mention contextual information such as prior queries, prior result pages, prior result documents, schedule data, and location data.
- The system creates one or more synthetic queries from generative-model output, then retrieves documents against both original and synthetic intents.
- State data can include an aggregate embedding built from the query, context, synthetic queries, and selected documents.
- Downstream model selection is conditional, meaning not every query should go through the same generative path.

## E-E-A-T And Audit Lens
- Pages that support multi-turn research should cover follow-up questions, subtopics, and adjacent entities naturally.
- Trust is reinforced when generated summaries can be verified against precise source passages.
- Sites with weak passage boundaries or vague claims are less useful in grounded, stateful systems.

## Real Audit Questions
- Does the page help only the seed query, or also the likely follow-up questions in the same session?
- Are there discrete, factual chunks that can be grounded and cited?
- Is the page internally consistent enough for embedding-based verification?
- Would the page still be useful after the first turn of a conversation, or only as a single-shot article?

## Caveat
The patent is a strong architecture clue, not a guarantee that a public Google product maps one-to-one onto every described component.






















































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Google

### Cross-Source Signals
- **Google**: Core Concept.

### Consensus
- Sources converge that `patent research, ai search, retrieval architecture` should be treated as a repeatable operating concern, not a one-off tactic.

### Tension / Caveat
- No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon.

### Squad Action
- Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.
<!-- phase10:end -->
