---
source: https://patentcore.digital/blog/patent-us20250103662/, https://patents.google.com/patent/US20250103662A1/en
title: Google Patent US20250103662A1 - Transformers with Link-Based Ranking
scraped: 2026-04-21
tags: google patents, transformers, link based ranking, document signals, source trust, ai retrieval
topic: patent_research, ai_search, document_quality
intent: research, system_architecture, strategy
role: coral, researcher, developer
confidence: high
canonical: true
canonical_group: Google Patent Core 2026
use_for: source_trust, document_signals, llm_search_architecture, authority_and_freshness_strategy
avoid_for: claiming_this_abandoned_application_is_production_proof
---

# Core Concept
`US20250103662A1` describes a way to inject document-level web signals into transformer attention so a model does not only read the tokens, but also the quality of the page that produced them.

## Official Patent Record
- Publication: `US20250103662A1`
- Title: `Unifying transformers with link based ranking`
- Prior art date: `2023-09-21`
- Filing date: `2023-09-21`
- Publication date: `2025-03-27`
- Assignee: `Google LLC`
- Inventor: `Antonino Gulli`
- Legal status: `Abandoned`

## Practical Mechanism
- The model tokenizes a web page into a training sequence.
- It associates the page with document-level signals such as author, ranking, traffic statistics, creation date, modification date, and interaction metrics.
- A normal attention matrix is built first.
- The attention weights are then adjusted up or down according to page-level relevance thresholds and document signals.

## SEO Reading
- The strong SEO takeaway is that trust and authority may matter inside the model's reading process, not only in a post-hoc ranking layer.
- Patent Core frames this as source trust becoming structural to understanding, not merely decorative metadata.
- This aligns with a broader shift where machine systems may prefer content from better-understood, better-maintained, and more-used sources.

## What To Reuse
- Treat authorship, freshness, engagement, and site-level reputation as inputs to machine readability and selection probability.
- Strengthen document quality signals on the page, not only via backlinks.
- Use this note when explaining why weak-source content may lose even when the wording looks competent.
- Pair it with E-E-A-T and quality-system notes when diagnosing AI-surface invisibility.

## Small Details Worth Remembering
- The disclosed signals include author, ranking, traffic, creation date, modification date, and interaction metrics.
- The adjustment happens at the attention-matrix level, meaning source signals can affect what the model focuses on while reading.
- The patent uses threshold logic to boost or suppress attention weights according to document relevance.
- The web-page case is the most useful SEO reading, but the architecture is generalized to other modalities too.

## E-E-A-T And Audit Lens
- This is one of the clearest patent families for why authorship, freshness, reputation, and engagement may matter inside AI retrieval systems.
- Experience and expertise are not only narrative qualities here; they may become source-level confidence priors.
- Weak author signals, stale pages, and low-trust hosts can undermine otherwise decent text.

## Real Audit Questions
- Is authorship visible, credible, and semantically connected to the topic?
- Are freshness cues and modification patterns real and useful rather than cosmetic?
- Do engagement patterns suggest the page is actually helpful once visited?
- Would a model see this document as a strong source, or only as token text from a weak container?

## Caveat
This is an application with `Abandoned` status. The architecture insight is still useful, but it should be handled as directional evidence rather than proof of the current production stack.






















































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Google

### Cross-Source Signals
- **Google**: Core Concept.

### Consensus
- Sources converge that `patent research, ai search, document quality` should be treated as a repeatable operating concern, not a one-off tactic.

### Tension / Caveat
- No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon.

### Squad Action
- Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.
<!-- phase10:end -->
