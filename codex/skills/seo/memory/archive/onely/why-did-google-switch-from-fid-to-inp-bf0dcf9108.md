---
source: https://www.onely.com/blog/difference-between-fid-and-inp/
title: Why did Google Switch from FID to INP?
scraped: 2026-03-23
published_on: 2024-04-10
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Why did Google Switch from FID to INP?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/difference-between-fid-and-inp/
Published: 2024-04-10
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Read the newest posts on our blog to make sure you're not missing out on anything!

## Extracted Body
Both Interaction to the Next Paint (INP) and First Input Delay (FID) metrics help to evaluate website responsiveness. They answer the question of how the page responds to user actions. Why did the INP replace the FID as a new Core Web Vital then?

(Read our Ultimate Guide on Core Web Vitals to make sure you know all of them.)

This article will cover key similarities and differences between FID and INP metrics. After reading it, you will understand why the weaknesses of FID encouraged Google to switch to INP.

We will explain why INP is a 2024 Core Web Vital and why it matters.

As the introduction mentions, it’s all about how the page reacts to the user’s actions . Both FID and INP metrics measure website responsiveness.

FID and INP are based on real interactions . There is no FID or INP measurement if a user just opens the page and reads the article without performing any action. LCP and CLS will be measured even in that case.

See how it looks when there is no user click, tap or key-press. No FID and INP score is visible.

By way of comparison, here is an example of a session with many clicks. Both FID and INP were measured.

LCP and CLS scores are easy to observe in lab tests . You can reload the page and see the scores using any web performance tool supporting CWV. FID or INP cannot be so easily replicated. To measure them, you need to imitate real interactions. If you have limited data about users’ behavior, you need to replicate interactions on your own.

FID measures only the first input delay, focusing on the first user’s interaction .

INP collects data about all interactions during a session. Then INP reports the worst interaction, so the one that took the longest time (you can read about exceptions in this article ).

While testing your website, you may notice that FID is measured once at the beginning. With INP, interaction time is reported for all interactions you perform. Each time you experience your longest interaction time up until now, the INP value is updated.

FID measures only input delay . INP measures not only the input delay, but also processing and presentation delays.

This means that FID reports only the time needed for the browser’s readiness to respond to users’ actions.

INP reports the total time between click, tap or key-press and the first visual effect on the screen.

INP scores are, on average, currently worse than FID. According to httparchive.org, most websites are passing the FID threshold on both mobile and desktop .

Regarding INP, over 30% of websites still need to prepare for the new Core Web Vital on mobile devices.

One of the reasons might be that web publishers were focused on FID till March 2024. However, the other reason could be that a good INP score is harder to achieve because all user interactions have to be optimized.

The above mentioned differences imply that INP is a more user-centered metric than FID because the next paint is more important for users than the browser’s readiness to process the event. Also, all interactions make a difference for real visitors , not just the first.

INP says more about user-perceived page responsiveness than FID.

The INP metric can be considered more useful in 2024 to evaluate your website comprehensively. Users should benefit more from the optimized INP scores than the FID measurements.

INP gives a real look into page responsiveness as a whole and helps to evaluate how easy and quick it is to use the website.

Google introduced INP as a new Core Web Vital to “ better evaluate the quality of a webpage’s user experience “.

Source: https://developers.google.com/search/blog/2023/05/introducing-inp

INP replaced FID, because these two metrics are the most similar ones, concentrating on website responsiveness.

It would not make sense, as LCP and CLS are about entirely different aspects of web performance.

Thanks to the change, this updated collection of metrics: CLS, LCP, and INP – gives a basic but comprehensive look into website health.

Probably to keep CWV simple , containing the aforementioned most important three elements. Additionally, this metric was made redundant in many cases, as most websites achieved good FID scores. Adding INP instead of FID will differentiate websites scores more, while giving a great benchmark for measuring interactions.

You will view INP instead of FID to monitor your progress in the GSC. Now, your goal is to achieve good INP scores.

Keeping good FID scores is still recommended as it affects your users’ satisfaction, but FID will no longer decide if you pass CWV.

Worried about this change? If you need our help, contact us and let us know!

Our dedicated team specializes in Technical SEO Services , elevating your website’s performance effortlessly.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
