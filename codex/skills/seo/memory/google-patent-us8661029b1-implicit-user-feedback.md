---
source: https://patents.google.com/patent/US8661029B1/en, https://patents.google.com/patent/US8938463B1/en, https://patents.google.com/patent/US10229166B1/en, https://patents.google.com/patent/US11188544B1/en, https://gofishdigital.com/blog/user-click-through-rates-and-search-result-rankings-at-google/, https://searchengineland.com/patent-suggests-how-ctr-time-on-page-could-be-used-in-search-rankings-if-google-did-that-sort-of-thing-314281, https://www.searchenginejournal.com/the-facts-about-google-click-signals-rankings-and-seo/572827/, https://patents.justia.com/patent/8661029
title: Google Patent US8661029B1 - Implicit User Feedback
scraped: 2026-04-25
tags: google patents, implicit user feedback, click signals, long clicks, dwell time, presentation bias, search satisfaction
topic: patent_research, click_signals, search_satisfaction
intent: research, diagnostics, strategy
role: coral, researcher
confidence: high
canonical: true
canonical_group: Google Patent Core 2026
use_for: search_satisfaction_audits, title_and_snippet_diagnostics, long_click_hypotheses, user_signal_interpretation
avoid_for: ctr_manipulation_tactics, claiming_individual_clicks_directly_rank_pages
---

# Core Concept
`US8661029B1` describes a system that converts aggregated implicit user feedback into a query-document relevance measure, then sends that measure to a rank modifier engine to help re-rank future search results.

## Official Patent Record
- Publication: `US8661029B1`
- Title: `Modifying search result ranking based on implicit user feedback`
- Prior art date: `2006-11-02`
- Filing date: `2006-11-02`
- Publication date: `2014-02-25`
- Assignee: `Google LLC`
- Inventors: `Hyung-Jin Kim`, `Simon Tong`, `Noam M. Shazeer`, `Michelangelo Diligenti`
- Legal status on the Google Patents record: `Active, expires 2031-01-31`

## Patent Family And Related Records
- The Google Patents family record shows continuations under the same title published as `US9235627B1` on `2016-01-12`, `US9811566B1` on `2017-11-07`, `US10229166B1` on `2019-03-12`, `US11188544B1` on `2021-11-30`, and `US11816114B1` on `2023-11-14`.
- The same family also sits next to closely related user-feedback patents such as `US8938463B1` on presentation bias, `US9092510B1` on temporal elements of user feedback, and `US8694511B1` on populations.
- This matters for audits because the underlying idea was preserved and refined over many years instead of appearing as a one-off filing.

## Practical Mechanism
- The system stores result-selection logs tied to query-document pairs, including clicks, viewing time, language, country, result position, unclicked results, shown titles, and shown snippets.
- It converts those logs into weighted click fractions rather than using raw clicks directly.
- Longer views, long clicks, and last clicks can receive stronger positive weight than short clicks.
- The resulting relevance measure is passed to a rank modifier engine, which can then adjust future rankings.
- The system includes anti-spam controls such as one-vote-per-cookie or IP ideas, abnormal behavior filtering, and smoothing for low-volume query-document pairs.

## What The Surrounding Public Analysis Adds
- Bill Slawski's 2019 analysis highlights that the patent is not only about click-through rate. He points to richer logging around unclicked results, query class, user type, language, country, titles, snippets, and user behavior patterns.
- Search Engine Land's March 21, 2019 coverage emphasizes the same caveat SEOs should keep: a patent does not prove production use, but it does show a concrete design for using longer-view behavior and query context to modify rankings.
- Search Engine Journal's April 23, 2026 article places the patent in a more modern frame: clicks are better understood as raw behavioral input that can be aggregated, transformed, or used as training data rather than treated as a simplistic one-click ranking factor.

## Important Related Mechanics Around The Patent
- `US8938463B1` expands the family by modeling presentation bias, comparing actual click behavior against predicted click behavior so the system can discount attractive positions, snippets, or layouts that inflate clicks without proving true relevance.
- Later continuations such as `US10229166B1` and `US11188544B1` keep the same core logic but show how the claims evolved around richer logging, device context, and more explicit weighting and ranking application.
- The original and later versions repeatedly separate raw feedback collection from the later ranking stage, which is the cleanest way to interpret the family.

## Research Lineage Around The Patent
- The Justia patent record lists earlier work that helps explain the knowledge base behind this invention, including Joachims on clickthrough data, Agichtein on web-search ranking with user behavior, Bar-Ilan on presentation bias, Craswell on click graphs, and Radlinski on implicit feedback and query chains.
- That lineage matters because this patent is better read as part of a broader information-retrieval tradition around inferred satisfaction, not as an isolated SEO myth about CTR.

## SEO Reading
- The strongest safe interpretation is not "CTR is a ranking factor."
- The stronger interpretation is that Google explored systems for converting aggregate interaction patterns into cleaner relevance signals after correcting for noise, bias, and spam.
- For SEO work, this makes title accuracy, snippet honesty, intent match, and post-click usefulness more important than clickbait.
- It also reinforces why short-click-heavy pages, misleading SERP copy, and weak satisfaction after the click are risky even if they earn attention.

## What To Reuse
- Write titles and descriptions that attract the right click, not the most clicks.
- Match the page opening, first-screen content, and main promise to the query intent immediately.
- Reduce pogo-stick behavior by answering the core question quickly before expanding.
- Localize and segment important pages when intent, country, or language meaningfully changes.
- Treat user satisfaction as a quality-system concern, not as a hackable CTR trick.

## Audit Lens
- Inspect whether the SERP promise and landing-page experience match cleanly.
- Check if titles and snippets are specific, honest, and intent-aligned rather than curiosity-bait.
- Look for pages likely to generate fast returns to search because the answer is delayed, vague, or mismatched.
- Distinguish navigational queries from informational queries, because success patterns differ by query class.
- For multi-market sites, inspect whether language or country variants are likely creating weak satisfaction signals due to localization mismatch.

## Real Audit Questions
- Does the result snippet promise the same thing the page immediately delivers?
- Is the page satisfying the query fast enough for its intent type?
- Are important answers visible early, or buried below irrelevant intros, ads, or clutter?
- Would a short visit indicate success for this query, or failure?
- Are there locale, device, or audience mismatches that could degrade satisfaction even when the content is broadly relevant?

## Caveat
Use this patent as evidence that Google has explored sophisticated implicit-feedback systems. Do not present it as proof that any individual click, dwell time event, or CTR tweak directly changes rankings in live Google Search today.




















































<!-- phase10:begin -->
## Evidence Fusion

Evidence confidence: medium
Freshness status: current
Distinct sources: Google

### Cross-Source Signals
- **Google**: Core Concept.

### Consensus
- Sources converge that `patent research, click signals, search satisfaction` should be treated as a repeatable operating concern, not a one-off tactic.

### Tension / Caveat
- No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon.

### Squad Action
- Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.
<!-- phase10:end -->
