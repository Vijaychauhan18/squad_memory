---
source: https://www.hobo-web.co.uk/how-human-quality-raters-are-used-new-evidence-from-doj-v-google-antitrust-trial/
title: DOJ v. Google Disclosure: How Human Quality Raters Are Used
scraped: 2026-03-20
tags: quality raters, rankembed, google doj, eeat, ranking models, training data
topic: site_trust_system
topic_assigned_by: phase9_merge_summaries
topic_assigned_on: 2026-05-19
---

## Core Concept
Hobo argues that human quality rater scores are not merely evaluation benchmarks but direct training data for core Google ranking models such as RankEmbed and RankEmbedBERT.

## Key Takeaways
- Rater scores help train ranking models rather than only auditing the output of those models.
- This turns the Quality Rater Guidelines into a practical blueprint for what Google is trying to operationalize at scale.
- Hobo positions rater feedback and search logs as paired training inputs, combining human judgment with user behaviour.
- The disclosure matters most for long-tail and nuanced queries, where human notions of usefulness and trust are harder to infer from simple metrics.
- Public Google statements that raters do not directly rank pages remain technically true at page level, but Hobo shows the aggregate effect is systemically direct.
- SEO strategy should therefore optimize for what trained human reviewers would call credible, useful, and trustworthy, not just what a crawler can parse.

## Frameworks/Methods Covered
- **Rater-to-model pipeline**: human scores become training data for ranking models
- **QRG as blueprint**: public rater guidance mirrors the traits Google wants its systems to learn
- **Human plus behavioural training loop**: rater judgments and search logs co-shape ranking systems

## Data/Stats
- Published: September 19, 2025
- Hobo highlights RankEmbed and RankEmbedBERT as models trained on search logs plus human rater scores
- The article links rater-trained systems to better handling of complex long-tail queries

## How The Team Should Use This
- **Coral (SEO)**: Use the QRG as an operational audit checklist, not just background reading.
- **Plankton (Writer)**: Write for a skeptical expert human first; machine models are being taught from that standard.
- **Developer / Chitin**: Support trust signals that humans notice immediately, including authorship clarity, references, ownership, and UX credibility.
- **Current (Marketing)**: Brand trust and clear editorial positioning improve the kinds of judgments Google appears to train against.
- **Key insight for the team**: If a trained human would not trust the page, a trained model is increasingly unlikely to either.
