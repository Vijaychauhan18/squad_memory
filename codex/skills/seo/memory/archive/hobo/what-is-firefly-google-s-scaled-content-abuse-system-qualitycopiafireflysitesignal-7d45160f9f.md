---
source: https://www.hobo-web.co.uk/firefly/
title: What is 'Firefly'? Google's Scaled Content Abuse System: QualityCopiaFireflySiteSignal
scraped: 2026-03-23
published_on: 2025-10-12
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

# What is 'Firefly'? Google's Scaled Content Abuse System: QualityCopiaFireflySiteSignal

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/firefly/
Published: 2025-10-12
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
An analysis of the leaked Google system, QualityCopiaFireflySiteSignal, reveals how it likely detects "scaled content abuse." Learn what site-wide signals, like content velocity and user engagement, Google uses to enforce its spam policies.

## Extracted Body
Disclaimer : This is not official. Any article (like this) dealing with the Google Content Data Warehouse leak requires a lot of logical inference when putting together the framework for SEOs, as I have done with this article. I urge you to double-check my work and use critical thinking when applying anything for the leaks to your site. My aim with these articles is essentially to confirm that Google does, as it claims, try to identify trusted sites to rank in its index. The aim is to irrefutably confirm white hat SEO has purpose in 2025 – and that purpose is to build high-quality websites. Feedback and corrections welcome .

For over two decades, our work in Search Engine Optimisation (SEO) has been a process of reverse-engineering a black box.

Strategies were built on a foundation of correlation, empirical observation, and the careful interpretation of public guidance.

The March 2024 Core Update, arriving concurrently with an unprecedented leak of Google’s internal Content Warehouse API documentation , represents a fundamental paradigm shift.

This leak, corroborated by sworn testimony from the U.S. Department of Justice (DOJ) v. Google antitrust trial , provides the SEO industry with its first look at the architectural blueprints of Google’s ranking systems, moving the practice from an art of inference to a science of architectural alignment.

My article presents a forensic analysis of one of the most intriguing components revealed in this leak: a protobuf named QualityCopiaFireflySiteSignal.

The central premise is that this specific technical attribute serves as a key enforcement mechanism for Google’s recently evolved “scaled content abuse” policy.

This policy, which rebranded the older “spammy automatically generated content” guidelines, shifted the focus from the method of content creation to the intent and outcome of publishing content at scale.

The leaked documentation primarily consists of property definitions for protocol buffers, or “protobufs”. These are not the scoring functions or algorithms themselves; rather, they are the structured data containers-the very schematics for the information-that Google’s various ranking and demotion systems access and process. Understanding these data structures is akin to an architect studying a building’s foundations; it reveals the principles upon which the entire edifice is constructed .

My investigation builds upon previous analyses published on the Hobo SEO blog in 2025, which have deconstructed other critical components of Google’s quality assessment framework, such as the QualityNsrPQData model and the contentEffort attribute .

This article is the next logical step, connecting the high-level policy against scaled abuse to the specific, site-level data structure seemingly designed to detect it. We will deconstruct the evidence, trace the evolution of Google’s philosophy, and provide strategic imperatives for thriving in this new era of architectural transparency.

Google’s fight against low-quality, manipulative content is as old as the search engine itself, but its policies have evolved significantly to keep pace with the changing tactics of spammers.

The direct predecessor to the current policy was known as “ spammy automatically generated content “. As defined in early 2024, this policy targeted:

“Content that’s been generated programmatically without producing anything original or adding sufficient value; instead it’s been generated for the purpose of manipulating search rankings and not helping users.”

The focus was on the method of creation. This was effective in an era when automated content was often easily identifiable as machine-generated gibberish or poorly “spun” text. However, the rise of sophisticated generative AI rendered this distinction increasingly obsolete.

Modern AI can produce content that is grammatically correct, coherent, and often indistinguishable from low-effort human writing, creating a grey area that spammers were quick to exploit.

Recognising this, Google updated its spam policies in March 2024, rebranding the section to “scaled content abuse”. The new, method-agnostic definition is far broader:

“When many pages are generated for the primary purpose of manipulating search rankings and not helping users. This abusive practice is typically focused on creating large amounts of unoriginal content that provides little to no value to users, no matter how it’s created.”

This was a strategic and necessary evolution. It future-proofed the policy against any new technology for content generation by shifting the focus to two timeless indicators of spam: the unhelpful outcome (large volumes of unoriginal content) and the manipulative intent (to game search rankings).

Google’s Search Liaison, Danny Sullivan, has been unequivocal about this philosophical shift.

His commentary reveals an awareness that the SEO community was misinterpreting Google’s stance on AI, believing that any content which appeared to be high quality was acceptable. Sullivan clarified the reality:

“…we don’t really care how you’re doing this scaled content, whether it’s AI, automation, or human beings. It’s going to be an issue.”

He further cautioned against the flawed definition of “quality” that some were adopting, noting that AI is proficient at creating “really nice generic things that read very well” but which do not necessarily provide unique value or originality.

This directly addresses the problem of AI being used to flood the web with plausible-sounding but ultimately unhelpful content.

This modern policy is not a new invention but the culmination of a long-standing battle

It echoes the work of Matt Cutts, former head of Google’s webspam team, who for years fought against scaled, low-value content in forms like article directories and manipulative guest blogging networks. Cutts consistently warned against any tactic that produced a “ton of useless content” purely for the sake of acquiring links or rankings.

The core principle-penalising low-effort content created for machines rather than people-has remained constant.

The “scaled content abuse” policy is simply the latest and most robust articulation of that principle, supported by John Mueller’s consistent advice that quality is a holistic, site-wide consideration, not just a page-level attribute.

The name of the protobuf itself – QualityCopiaFireflySiteSignal – is not an arbitrary string of code. Within Google’s engineering culture, naming conventions are often highly descriptive.

A forensic, word-by-word analysis of this name provides a powerful indication of its function.

It describes a system that assesses site-wide quality (Quality, SiteSignal) by looking for patterns of excessive volume (Copia) using a sophisticated (potential) heuristic algorithm ( Firefly ) to identify abuse. And perhaps, to identify quality too.

The purpose of this article is to focus on the parts of it that could be used to identify scaled content abuse .

The leaked documentation provides a succinct, powerful summary of the module’s purpose: “ fireflySiteSignal – Contains Site signal information for Firefly ranking change. “ This single line confirms its role in altering rankings.

The protobuf definition then provides the exact data points that constitute this signal. This is the raw input. By analysing each attribute, we can understand precisely how Google quantifies a site’s behaviour to detect scaled abuse.

These attributes measure how users interact with the site in Google’s search results, providing a ground-truth signal of whether the scaled content is actually helpful.

These attributes provide a quantitative measure of the scale and quality of a site’s content production, directly addressing the “Copia” (abundance) aspect of the signal.

These attributes provide temporal context and a unique identifier, allowing the system to track a site’s behaviour over time.

The confirmation that Google extensively uses click data, as evidenced by attributes like dailyGoodClicks and the underlying NavBoost system, stands in stark contrast to years of public statements from its representatives who have consistently downplayed or denied the use of user engagement signals as a direct ranking factor.

John Mueller, a prominent Search Advocate at Google, has repeatedly dismissed the idea. In one statement, he argued against the viability of using click-through rates (CTR) for ranking:

“If CTR were what drove search rankings, the results would be all click-bait. I don’t see that happening.”

In another hangout, he went further, suggesting Google doesn’t even have visibility into on-site user actions, which would preclude their use as a ranking signal:

“So in general, I don’t think we even see what people are doing on your web site. If they are filling out forms or not, if they are converting and actually buying something… So if we can’t see that, then that is something we cannot take into account. So from my point of view, that is not something I’d really treat as a ranking factor.”

Gary Illyes, another analyst on the Google Search team, has echoed this sentiment, often describing click data as unreliable for direct ranking purposes. He has referred to clicks as a “very noisy signal” and stated that using them directly would be problematic due to manipulation and scraping activities. In a particularly blunt dismissal, Illyes was quoted as saying:

“Dwell time, CTR, whatever Fishkin’s new theory is, those are generally made up crap. Search is much more simple than people think.”

These public denials created a long-standing debate within the SEO community. The leaked documentation and DOJ trial testimony have now provided concrete evidence that resolves this debate, confirming that while Google may not use raw CTR as a simplistic, direct input, it absolutely uses sophisticated, aggregated, and normalised click data via systems like NavBoost to evaluate and re-rank search results.

A fascinating footnote to this history of denial lies in Illyes’ choice of words . His dismissal of click-based theories as “ made up crap ” takes on a layer of profound irony when viewed through the lens of the leak. The documentation reveals a ranking system module explicitly named “ Craps ,” which is defined as the system that processes “click and impression signals.”

It is, in essence, the very system that handles the data Illyes was publicly dismissing . The metrics it processes-goodClicks, badClicks, and lastLongestClicks-are direct, quantifiable measures of user satisfaction that serve as sophisticated proxies for the very concepts of CTR and dwell time that were being derided.

Whether this was a deliberate, meta-textual joke on Illyes’ part-a hidden admission veiled in dismissive language-is impossible to know. Look to the sentence structure itself (“…made up crap. Search is much more simple…”) as a potential, albeit highly speculative, nod to the truth.
