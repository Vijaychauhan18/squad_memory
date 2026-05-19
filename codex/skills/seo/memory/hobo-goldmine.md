---
source: https://www.hobo-web.co.uk/google-goldmine/
title: What Is 'Goldmine'? Google's Quality Judge For SERPS Leaked
scraped: 2026-03-20
tags: goldmine, titles, snippets, serp rewriting, query rewriting, google leak, on-page seo
topic: document_quality_system
topic_assigned_by: phase9_merge_summaries
topic_assigned_on: 2026-05-19
---

## Core Concept
Goldmine is Hobo’s name for a leaked Google scoring engine that evaluates candidate SERP elements, especially titles, by comparing publisher input against alternatives from headings, links, URLs, and page content.

## Key Takeaways
- Your HTML title is only one candidate; Google may test it against H1s, internal anchor text, off-domain anchors, and body-derived alternatives.
- Goldmine is not just about rewriting titles. Hobo presents it as a blueprint for how Google evaluates many SERP-facing elements.
- Signal coherence matters because Goldmine appears to score alignment between title, URL, body, and trust-related signals.
- Boilerplate, truncation, duplication, and weak prominence are not cosmetic issues; they are measurable quality defects.
- Goldmine interacts with user-feedback systems. A poor chosen title can depress clicks and feed bad downstream signals into NavBoost.
- The existence of sibling systems such as SnippetBrain, Muppet, and Radish supports the idea that Google uses specialized evaluation engines for each displayed SERP element.

## Frameworks/Methods Covered
- **Alternative title evaluation**: publisher title versus page-derived and link-derived candidates
- **Signal coherence model**: title, H1, URL, intro, and body should reinforce the same topic
- **SERP feedback loop**: title choice influences clicks, which influences later ranking systems

## Data/Stats
- Published: October 22, 2025
- Hobo highlights candidate sources like `sourceTitleTag`, `sourceHeadingTag`, `sourceOnsiteAnchor`, and `sourceOffdomainAnchor`
- Example Goldmine-related factors called out include `goldmineBodyFactor`, `goldmineUrlMatchFactor`, `goldmineTrustFactor`, and boilerplate/truncation flags

## How The Team Should Use This
- **Coral (SEO)**: Audit title-H1-URL alignment before publishing. If Google can’t trust the title, it will rewrite it.
- **Plankton (Writer)**: Write strong, distinct H1s and introductions that support the page’s main claim and give Google better candidate text.
- **Developer / Chitin**: Preserve clean heading hierarchy, visible title prominence, and non-boilerplate templates.
- **Current (Marketing)**: Titles should promise a clear payoff and match the actual landing-page experience, otherwise CTR and engagement both suffer.
- **Key insight for the team**: Metadata is no longer a command. It is evidence in a competition against the rest of your page.
