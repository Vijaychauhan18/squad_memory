---
source: https://www.hobo-web.co.uk/the-q-metric-google-quality-score/
title: The Quality Signal (Q*) - Q-Star - Google Quality Score for Organic Search Results
scraped: 2026-03-23
published_on: 2025-07-10
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

# The Quality Signal (Q*) - Q-Star - Google Quality Score for Organic Search Results

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/the-q-metric-google-quality-score/
Published: 2025-07-10
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
This is a preview of Chapter 3 from my new ebook - Strategic SEO 2025 - a PDF which is available to download for free.

## Extracted Body
Disclosure : I use generative AI when specifically writing about my own experiences, ideas, stories, concepts, tools, tool documentation or research. My tool of choice is in this process is Google Gemini Pro 2.5 Deep Research and Chatgpt 5. This is not offical advice from Google. All content was verified as correct by Shaun Anderson. See our AI policy .This is a preview of Chapter 3 from my new ebook – Strategic SEO 2025 – a PDF which is available to download for free here . This article was first published on: 10 July 2025

The trial also brought to light a previously secret internal metric known as Q* (pronounced “Q-star”), which functions as a measure of a website’s overall quality and trustworthiness.

This revelation is significant because it apparently confirms the existence of a site-level quality score , something Google representatives have publicly and repeatedly avoided confirming (in these exact terms) for years.

According to trial exhibits, Q* is “an internal metric that assesses the trustworthiness of a whole website (most often the domain)”. To avoid confusion, Q*is completely different from the known Google Quality Score in Google Ads.

A crucial characteristic of Q* is that it is largely static and query-independent .

If a website earns a high Q* score, it is considered a high-quality, reliable source across all related topics for which it might rank.

This explains why certain authoritative domains consistently appear in search results for a wide range of queries.

Like the T* system, Q* is described as being “deliberately engineered rather than machine-learned,” reinforcing the theme of human oversight in Google’s foundational ranking systems.

A key input into the Q* score is a modern, evolved version of Google’s original breakthrough algorithm, Google Pagerank .

Testimony revealed that PageRank is still an important signal , but its function is now framed as measuring the “ distance from a known good source “.

The system uses a set of trusted “seed” sites for a given topic; pages that are closer to these authoritative seeds in the web’s link graph receive a stronger PageRank score, which in turn contributes to a higher Q*.

The confirmation of a domain-level authority score like Q* stands in stark contradiction to years of public communications from Google.

“‘Even the most fascinating content, if tied to an anonymous profile, simply won’t be seen because of its excessively low rank.’ Cited to Eric Schmidt, ex-Google, 2014.

In response, Google developed internal Page Quality metrics – sometimes referenced as “QScore” or “QRank” – to judge the overall authority, expertise, and trustworthiness of a page or site.

Google’s Hyung-Jin Kim (VP of Search) described this as a “page quality (i.e., the notion of trustworthiness)” score, often denoted internally as Q * (“Q-star”).

He noted in testimony that “Q is incredibly important”* and that Google formed a dedicated “Page Quality” team ~17 years ago when low-quality content farms were proliferating justice.gov .

The idea behind Q* is to algorithmically assess factors like a site’s reputation, authority, and compliance with quality guidelines, independent of any specific query .

Kim explained that this quality signal is “generally static across multiple queries and not connected to a specific query” , meaning if a site is deemed high-quality and reliable, that status boosts its rankings for all relevant searches justice.gov .

(However, query context can be factored in at times – for example, even a generally high-quality site might be outranked by a more expert site for a very niche technical query justice.gov .)

Crucially, Google’s modern quality score integrates PageRank as one input .

Kim confirmed that “PageRank…is used as an input to the Quality score.” justice.gov In other words, a page’s base PageRank (its link-based importance) contributes to its overall “authority” score Q*, alongside other factors (possibly site reputation, expert reviews, etc.).

The Quality score thus acts as an aggregate authority metric – sometimes called an “authority score” – that can boost or dampen a page’s search rankings.

Pages with strong Q scores (earned via trusted backlinks, original content, good user signals, etc.) are systematically favoured.

This became especially important after Google’s 2011 “Panda” update , which targeted shallow content. Kim alluded to this, noting the team had started to tackle content farms that “paid students 50 cents per article” , flooding Google with thin pages justice.gov .

The solution was to algorithmically identify “the authoritative source” for a given topic and reward it justice.gov .

In effect, Google began demoting pages that had decent link popularity but poor overall quality, and promoting those with true authority. Kim emphasised that “Quality score is hugely important even today. Page quality is something people complain about the most.” justice.gov

“We figured that site is trying to game our systems… So we will adjust the rank. We will push the site back just to make sure that it’s not working anymore.” Gary Illyes, Google 2016

Indeed, with the rise of generative AI content, Google’s reliance on such quality signals has only grown ( “nowadays, people still complain about [quality] and AI makes it worse” , he noted, justice.gov ).

How Q works internally: Google treats the quality score as a mostly query-independent ranking factor attached to pages or sites .

Q* is “largely static and largely related to the site rather than the query”, justice.gov – essentially a measure of a site’s authoritative strength.

At query time, this quality score is combined with the query-dependent relevance score. While Google hasn’t publicly detailed the formula, one can think of the ranking system as first evaluating relevance (does the page match the keywords/intents?) and then adjusting results based on authority/quality .

A high Q* can significantly boost a page’s position, while a low-quality score can sink an otherwise relevant page.

In practice, Google’s regular updates and ranking tweaks often boil down to recalibrating this “authority” component.

Notably, many signals feed into Q*: PageRank and link signals (for authority) , content assessments (for expertise) , TrustRank-like signals (for trustworthiness) , and even user engagement data .

For example, internal documents indicate Google also uses a “popularity signal that uses Chrome data” (likely aggregated Chrome usage statistics) as well as click feedback loops like NavBoost justice.gov stradiji.com .

(NavBoost, described by Google’s Dr. Eric Lehman, is essentially a big table counting how often users click on a result for a given query over the past year stradiji.com – a way to boost pages that searchers consistently prefer).

These additional signals are beyond PageRank, but they complement the goal of Q*: to measure overall quality and user satisfaction .

PageRank itself, once the star of Google’s algorithm, now works behind the scenes as one signal feeding into these broader quality and ranking frameworks.

Mark Williams Cook , of Candour , did some exceptional work in this area, and I was lucky enough to chat with him about it at the time – “ The endpoint exploit we found literally had a metric called ‘site_quality’, which at minimum determined if you got some kind of rich results ”.

Insights from a fascinating talk on “ Conceptual Models of SEO ” reveal a deeper, more nuanced layer to how Google evaluates websites, moving far beyond traditional metrics like keyword density or backlink counts.

Based on data allegedly retrieved from a Google exploit, the speaker outlines a compelling case for a master metric: a “Site Quality Score.”

This score appears to function as a foundational assessment of a site’s authority, directly impacting its ranking potential and eligibility for prominent search features.

The core of the discovery is a “Site Quality Score” that Google allegedly calculates for every single website, scored on a scale from 0 to 1 at the subdomain level .

This isn’t just another data point; it acts as a critical qualifier.

The speaker revealed a specific threshold: sites with a quality score below 0.4 were found to be ineligible for Rich Results like Featured Snippets or “People Also Ask” boxes.

This implies that no amount of on-page optimisation for these features will succeed if a site hasn’t first passed this fundamental quality check.

It’s a heat race you must qualify for before you can even compete.

So, what constitutes this all-important score? According to Mark, who likes to reference Google patents, like I do, the calculation depends on whether Google has sufficient user data for a site.
