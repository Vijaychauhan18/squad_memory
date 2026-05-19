---
source: https://www.searchpilot.com/resources/blog/split-testing-javascript-for-seo
title: Early Results from Split Testing JavaScript for SEO
scraped: 2026-03-22
published_on: 2023-08-07T09:56:00+01
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Early Results from Split Testing JavaScript for SEO

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/split-testing-javascript-for-seo
Published: 2023-08-07T09:56:00+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Despite the claims from Google, we regularly find that there are still downsides to relying on their JavaScript crawling and processing capabilities. This post tells the story of one of our earliest split tests comparing pages requiring JavaScript for the full experience against the performance of those pages when we removed the reliance on JavaScript.

## Extracted Body
We’ve been testing what happens when pages rely on JavaScript to render properly - and one of our first tests showed an uplift when we removed a reliance on JS:

When @distilled ran an SEO split test to remove a reliance on JavaScript, they saw an uplift in search performance https://t.co/JOmPXReGbq pic.twitter.com/7bhzHxV0qK

As many of you know, we believe that it’s increasingly important to be testing your hypotheses about what will affect your search performance. As digital channels mature, and as Google rolls more and more ML into the algorithm, it’s increasingly hard to rely on best practices. To make this easier, we have been rolling out our SEO split testing platform to more and more of our clients and customers.

As we get our platform deployed on a wider range of sites with different architectures and technologies, we’re able to start testing more and more of the assumptions and best practices held around the industry.

You can check out a bunch of case studies that we have already published on our site (and sign up for our case study email list here ) - and you can find more details in this presentation (particularly slide 73 onwards ) that my colleague Dom gave at a recent conference. We also included some teaser information in this post about a big win that added £100k / month in revenue for one customer even while only deployed on the variant pages (half of all pages).

One thing that we were excited to get to test was the impact of JavaScript. Google has been talking about rendering JavaScript and indexing the resulting DOM for some time, and others around the industry have been testing various aspects of it , figuring out when it times out , and finding out the differences between inline, external, and bundled JS .

I wrote a Moz post on how I believe that JavaScript rendering and indexation works at Google , but the very short version is that I think it happens in a separate process / queue to both crawling and regular indexing. I think there is a delay downside, and possibly even more than that.

We recently had a chance to observe some of the effects of JS in the wild. One of our consulting clients - iCanvas - was relying on JavaScript to display some of the content and links on their category pages (like this one ). Most of our customers on the SearchPilot are not consulting clients of Distilled, but iCanvas is a consulting client with the SearchPilot deployed (I’ve written before about how the ability to split-test is changing SEO consulting ).

With JavaScript disabled, there were a load of products that were not visible, and the links to the individual product pages were missing (it’s worth noting that the pages showed up correctly in fetch and render in Google Search Console). We wanted to make the consulting recommendation that performance may be improved by showing this information without relying on JavaScript - but this is the classic kind of recommendation that is hard to make without solid evidence. There is clearly a cost to making this change, and it’s hard to know how much of a benefit there is.

Before our change, the pages looked like this with JS disabled:

After the change, they looked more like this (which is exactly how they used to look with JS enabled):

[It’s worth noting that although the change we made here was technically a CSS change, the test is measuring the effect of removing JavaScript dependence - we just moved a feature from JS-reliant to non-JS-reliant]

Using our split-testing platform, we rolled out a change to 50% of the category pages to change them so that the information users might be looking for was visible on page load even with JavaScript disabled. The other 50% of pages remained unchanged and continued to rely on JavaScript.

We then automatically compared the performance of the updated pages with a forecast of what would have happened if we had not rolled out the change (this is called a “counterfactual”) [ more here ]. This showed that the pages we had updated to remove the reliance on JavaScript were getting a statistically-significant amount more traffic than we would have expected if the change had no effect:

The platform’s analysis showed a greater than 6% uplift in organic search performance to these set of pages, which amounted to over 3,000 additional sessions per month. This was an amazing win for such a small change (the chart above comes from the dashboard built into our SearchPilot platform).

As an aside, the mathematicians on our team are constantly working on refinements to the way we detect uplifts with statistical confidence (see Google’s paper Inferring causal impact using Bayesian structural time-series models for more background). We use a variety of synthetic tests, null tests and cross-checked data sources to make improvements to the accuracy and sensitivity of the automated analysis. We also apply a variety of treatments to the analytics data to account for various behaviours (dominant pages, sparse traffic distribution, seasonal products etc.), as well as some modifications to how Google’s Causal Impact methodology is employed.

In the test above we have since improved the accuracy of the analysis (it did even better than the initial analysis suggested!), which is exciting. It also means we are capable of detecting tests that result in smaller uplifts than previously possible, helping lead to improved performance and improved attribution.

The main takeaway is that you should avoid the assumption that JavaScript-driven pages will perform well in search even if Google is able to render them. We need to continue running more JS tests, but in the meantime, we strongly recommend testing whether your reliance on JavaScript is hurting your site’s organic search performance.
