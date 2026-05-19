---
source: https://www.hobo-web.co.uk/e-e-a-t-quality-score/
title: E-E-A-T is the Goal, Q-Star is the System, Site_Quality is the Score
scraped: 2026-03-23
published_on: 2025-09-22
tags: live_feed, phase1_ingest, hobo, publication, quality, leak-systems, archive_backfill, historical_source
topic: quality_systems
intent: research, monitoring, source_selection, leak_systems
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Archive backfill - Hobo Web
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# E-E-A-T is the Goal, Q-Star is the System, Site_Quality is the Score

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/e-e-a-t-quality-score/
Published: 2025-09-22
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
In short, E-E-A-T is Quality Score. Or thereabouts.

## Extracted Body
Based on ground truth evidence from antitrust DOJ trial documents reviewed, the content data warehouse leak, Google Quality Rater guidelines, Google Search Essentials, and over 20 years experience in SEO (search engine optimisation), and some admitted logical inference of my own, I present that E-E-A-T is a condensation of Q-Star (Q*) and ‘Site_Quality’ score is the output.

For all intents and purposes, E-E-A-T is Q-Star. E-E-A-T is Quality Score, or a proxy of it, at least.

Conceptually speaking, E-E-A-T is Google’s doctrine codified.

Google’s philosophy is built on a single, foundational concept: Trust .

The Search Quality Rater Guidelines (QRG), the E-E-A-T framework within it, and the Helpful Content Update are not separate initiatives; they are interconnected systems designed to define, measure, and reward trust .

According to Google’s own documentation, “ Of these aspects, trust is most important “.

The other components – Experience, Expertise, and Authoritativeness – support the central concept of Trust.

A page can demonstrate expertise, but if it is untrustworthy, it will be assigned the lowest possible quality rating because, as the September 11 2025, guidelines state, “ Trust is the most important member of the E-E-A-T family because untrustworthy pages have low E-E-A-T no matter how Experienced, Expert, or Authoritative they may seem “.

This is especially true for “Your Money or Your Life” (YMYL) topics, where a lack of trustworthiness can cause real-world harm.

“‘Even the most fascinating content, if tied to an anonymous profile, simply won’t be seen because of its excessively low rank.’ Cited to Eric Schmidt, ex-Google, 2014.

The phrase “ Brands are how you sort out the cesspool ” was a statement by former Google CEO Eric Schmidt in 2008, suggesting that in the rapidly expanding and largely unregulated internet, trusted brands act as a signal of quality and reliability, helping users navigate through a sea of potentially false or low-quality content.

He saw brands not as the problem, but as the solution to the challenges posed by the “cesspool” of information online, offering a way to organise and trust the content available.

The concept of a site-level quality score is not new; its lineage can be traced back to the 2011 Google Panda update, which was Google’s first major attempt to “reduce rankings for low-quality sites” on a site-wide basis.

The modern Q* system, called Q-Star internally, is the direct descendant of this initiative – a composite score that reflects a site’s overall credibility and utility, independent of any specific query.

Sworn testimony from Google’s Vice President of Search, Hyung-Jin Kim, during the DOJ vs. Google trial, underscored the system’s foundational role.

Kim noted, “Q* (page quality, i.e., the notion of trustworthiness) is incredibly important” and testified that the “ Quality score is hugely important even today . Page quality is something people complain about the most” .

He recounted that Google formed a Page Quality team in response to “content farms” flooding search results, developing methods to identify authoritative sources and demote low-quality pages. This quality score is “generally static across multiple queries and not connected to a specific query,” making it a persistent reputation metric that is “largely related to the site rather than the query” . In short, Google uses this system to “consistently reward pages that demonstrate experience, expertise, authority, and trust (E-E-A-T), and that reputation persists across queries” .

Here’s a visualisation of the content data warehouse leak modules and attributes and how it all comes together:

Mike King did a great write-up at the time. I remember when this leaked, this was he first thing I looked for – a quality score module.

If the Q* system is the “engine” that calculates quality; the 2024 leak provided us with its official parts list. It is worth noting when referring to this leak that Google confirmed it was legit and commented on it (from sworn testimony in the recent Google V DOJ Antitrust Trial ): “ There was a leak of Google documents which named certain components of Google’s ranking system, but the documents don’t go into specifics of the curves and thresholds. The documents alone do not give you enough details to figure it out, but the data likely does. ”

I examined a component module named GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals , which, based on its description and attributes, is the technical confirmation of the entire “Quality Score” concept.

A message containing per doc signals that are compressed and included in Mustang and TeraGoogle. For TeraGoogle, this message is included in perdocdata which means it can be used in preliminary scoring.

Let’s deconstruct this. These are “compressed signals” used for “preliminary scoring.” The documentation adds a stark warning:

CAREFUL: For TeraGoogle, this data resides in very limited serving memory (Flash storage) for a huge number of documents.

This is a document’s essential “rap sheet.” These are the few, critical signals Google must be able to access instantaneously for every document in its index to make a foundational judgment of quality before applying more complex, query-time calculations.

This module is the “cheat sheet” that feeds the Q* system. And what’s on it? A literal roll-call of quality factors. This module is where Google stores the inputs for its quality score, which we can group by theme:

These are the foundational “at-a-glance” scores for the document and site:

A long list of negative signals that act as “demerits” against the document:

These are positive scores or highly specific classifiers for niche content:

Signals that define what the site is about , which is foundational to its authority:

Finally, the module’s contents prove the Quality Score isn’t a static, unchanging number but a living, breathing system that is constantly being tested and refined:

This module is the technical confirmation of our thesis. It’s not the final score, but the raw ingredients fed directly into the Q* system. It is the “rap sheet,” “cheat sheet,” and “test lab” for Google’s organic Quality Score all rolled into one.

Further confirming the existence and function of a site-level quality score, Mark Williams-Cook discovered and analysed a separate Google API endpoint exploit.

As detailed in a previous analysis on Hobo Web, this exploit provided a real-time view into how Google scores websites, revealing a Site_Quality attribute that functions as a critical gatekeeper for visibility.

Williams-Cook’s analysis of over 90 million queries revealed that Google calculates this score at the subdomain level on a scale of 0 to 1.

Interestingly, he identified a specific threshold: sites with a quality score below 0.4 were found to be ineligible for prominent search features like Featured Snippets and “People Also Ask” boxes .

This demonstrates that a site must pass a fundamental quality check before its content can even compete for these highly visible SERP features. His research confirmed that this score is derived from the same types of signals mentioned in the main leak and DOJ trial: brand visibility (branded searches), user interactions (clicks), and anchor text relevance.

These findings provide a quantitative layer to the concept of siteAuthority, showing that it is not just an abstract idea but a measurable score with direct, threshold-based consequences for a site’s ranking potential.

The Helpful Content Update (HCU) acts as the primary algorithmic enforcement mechanism for these principles. Initially a separate system, the HCU is now fully integrated into the main core ranking algorithm. As Google’s Search Liaison Danny Sullivan stated, “ It is now part of a ‘core ranking system that’s assessing helpfulness on all types of aspects.”

The HCU is designed to reward “people-first” content that leaves a visitor feeling they have had a “satisfying experience”.

A satisfying experience is intrinsically linked to Trust. The update penalises content that erodes trust, such as pages that merely summarise what others have said without adding value. In this way, the HCU and E-E-A-T are “very closely aligned,” with the update serving to algorithmically identify the signals of helpfulness and trustworthiness that the QRG asks human raters to look for.

Ultimately, the Q* score is the technical culmination of this entire trust-based evaluation. The principles laid out in the QRG and enforced by the HCU are the inputs that the Q* system is engineered to measure.

A high Q* score is the algorithmic reflection of a site that successfully demonstrates the signals of trust, experience, and expertise that Google’s guidelines prioritise.

If a site has good content and solid links, why might it still fail to rank? The Disconnected Entity Hypothesis provides a compelling answer, and its foundation lies in a specific instruction given to Google’s human Quality Raters.

The hypothesis posits that Google’s updates target “Disconnected Entities”—websites lacking a strong, verifiable connection to a trusted real-world entity . This isn’t just a theory; it’s based on the explicit instructions in the QRG. Specifically, Section 2.5.2 instructs raters to locate who owns and operates a website and who is responsible for the content .

A lack of this information is what defines a disconnected entity. When a site fails this fundamental transparency test, its quality signals have no entity to attach to. This breaks the entire E-E-A-T evaluation:

Experience & Expertise cannot be verified without a known author or organisation.

Authoritativeness is diluted because links and mentions don’t point to a recognised entity.
