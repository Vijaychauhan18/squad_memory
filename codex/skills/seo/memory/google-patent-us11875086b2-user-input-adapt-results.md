---
title: "Google Patent US11875086B2 — Using User Input to Adapt Search Results"
skill: seo
type: patent
patent_id: US11875086B2
assignee: Google LLC
granted: 2024-01-16
filed: 2021-06-30
priority: p1
confidence: 0.91
tags: [patents, user_signals, navboost, dialogue, re_ranking, suppression, promotion]
related: [[navboost-behavioral-signals]], [[google-patent-us11886828b1-generative-summaries]]
---

# Google Patent US11875086B2 — Using User Input to Adapt Search Results

## What it covers
An automated assistant sequentially presents search results during a dialogue session. It modifies which result types surface based on what the user accepts, skips, or references by attribute. Suppression and promotion signals carry forward into subsequent searches within the session.

## Core mechanism
- User accepts a result → that result type gets promoted in follow-up queries
- User skips or bounces → that result type gets suppressed
- Attribute-level references ("show me more like that one") trigger cluster-level adjustments
- Signals persist across the session, not just a single SERP

## SEO signals
- **Session-level carry-forward** — a single bad interaction suppresses a domain for the rest of the session
- **Dialogue completion matters** — pages that satisfy intent and end the dialogue positively get promoted
- **Bounce and re-query are immediate suppression signals** — landing page quality directly modifies short-session ranking

## Practitioner implication
Intent match on the landing page is a ranking signal, not just a UX metric. A page that triggers a back-click and re-query signals suppression that persists within the session. AIO/AI Mode sessions with this architecture make every click-decision a live ranking adjustment.

## URL
https://patents.google.com/patent/US11875086B2
