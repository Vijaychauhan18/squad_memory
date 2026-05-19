---
source: https://www.searchpilot.com/resources/blog/seo-testing-for-ecommerce
title: The importance of SEO testing for ecommerce websites
scraped: 2026-03-22
published_on: 2023-08-09T15:44:30+01
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

# The importance of SEO testing for ecommerce websites

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/seo-testing-for-ecommerce
Published: 2023-08-09T15:44:30+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Ecommerce websites are pressed to drive high volumes of traffic, and convert customers, making them a great fit for SEO split-testing. By using SEO split-testing ecommerce websites can test theories, launch tests quickly and make data-informed changes based on results. Instead of going off of assumptions of what’s best or what might drive the most traffic, teams can now work off of tests and results.

## Extracted Body
One of the biggest concerns we hear from ecommerce SEO teams is the inability to directly connect their efforts to business outcomes. To make a difference with SEO you need budget and leaders that support you, but when you aren’t able to track business results budget is hard to come by and career progression for those involved in SEO becomes more difficult.

SEO A/B testing , a.k.a. SEO split-testing, can solve some of these issues by eliminating much of the guesswork and making it easier to tie the work you are doing to business KPIs.

In this post, we’re sharing the basic principles of SEO testing, how this can work for ecommerce websites as well as five specific case studies:

Controlled SEO split testing is when you split a group of statistically similar pages into control and variant groups, change the variant pages and evaluate the outcomes using mathematical modeling.

To be able to run tests, there are two primary requirements:

Using this SEO split-testing process, there are nearly limitless tests you can run on an ecommerce website to drive increased organic traffic and sales.

Now that you understand what’s possible, here are some examples of SEO split tests that our customers have run.

Does optimizing your image alt text for specific keywords make a difference for ecommerce websites? This is one of the most common suggestions from SEO agencies.

In fact, Google says it uses alt text to inform rankings for Google Image search , and John Mueller has previously said (2017) that it can be used to inform desktop rankings like any other on-page text.

We decided to put this to the test with one of our ecommerce customers who wanted to add alt text to product images on all of their category pages .

Each page included images for all the different products, with most pages having 24 options as the default view. Previously, none of these images had alt text on them.

Our recent experiment found that adding keyword-rich alt text had no detectable impact on organic traffic to these pages.

Does using the React framework increase organic search performance?

This question is coming up more often as more companies rely on JavaScript frameworks such as React, Angular or Vue.js. These frameworks can add increased functionality to websites and allow websites to behave more like apps than traditional collections of webpages.

However, from an SEO standpoint, there are some potential pitfalls - without careful consideration, it’s possible to make your content inaccessible to search engines, or at the very least increase the demands on search engine bots to have to render the JS components of a page in order to index your content.

We put this to the test with one of our ecommerce customers. This customer implemented React so they can provide an enhanced user experience for the purchase process and page speed improvements.

We tested this by using request modification to add a request header to variant pages which directed the host server to return the new, SSR React-based product page in place of the existing version of the page.

In fact, this change led to a 13% uplift, compared to the old version:

Breadcrumbs and breadcrumb markup are often considered SEO “best practice.” However, even if you’re able to get the rich snippet from breadcrumb markup, it may not improve your pages’ performance and click through rate, as we saw in one experiment.

For instance, we ran a test with one of our ecommerce customers, who had breadcrumbs on their product and category pages, but an error in the structured markup prevented them from appearing in the search snippets at the time. They tested fixing their breadcrumb markup so that their breadcrumbs would show up in the search results as intended.

Our hypothesis was that after fixing the breadcrumb markup, the breadcrumbs would display in the search results and drive more clicks to the pages. Additionally, correcting any markup errors may help Google better understand the site’s structure and how product pages relate to their parent category pages and vice versa. This could result in improved rankings for the product and / or category pages.

Here’s how the control and variant pages looked in the search results page.

We measured the impact on the product pages (e.g. /green-high-waisted-bikini-bottoms), subcategory pages (e.g. /clothing/swimwear) as well as the high-level category pages (e.g. /clothing).

The result was surprising. The change’s impact on the high-level category pages was negative for SEO, with an estimated 7% loss in organic traffic:
