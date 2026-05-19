---
source: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-adding-price-review-schema-product-pages
title: Impact on SEO performance of price and review schema
scraped: 2026-03-22
published_on: February 10, 2021
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

# Impact on SEO performance of price and review schema

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-adding-price-review-schema-product-pages
Published: February 10, 2021
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
This week’s #SPQuiz on Twitter asked our followers which they thought was most beneficial for organic traffic: just review schema, both review and price schema, or that there no difference between the two. The majority believed that the answer was both types of schema together. However, the majority in this case was incorrect. We ran two tests on the same website, one with both schemas and one with just reviews.

## Extracted Body
If you aren't familiar with the fundamentals of how we run controlled SEO experiments that form the basis of all our case studies , then you might find it useful to start by reading the explanation at the end of this article before digesting the details of the case study below. If you'd like to get a new case study by email every two weeks, just enter your email address here .

This week’s #SPQuiz on Twitter asked our followers which they thought was most beneficial for organic traffic: just review schema, both review and price schema, or that there no difference between the two.

The majority believed that the answer was both types of schema together. However, the majority in this case was incorrect. We ran two tests on the same website, one with both schemas and one with just reviews. The first was inconclusive and the second had an estimated uplift of 20%!

Recently, Google has seemingly limited the types of rich snippets a single result can have at once, which has made deciding what structured data markup to implement on your website more complicated. While there has been a craze around rich results like FAQ snippets, for example, we’ve found the addition of FAQ schema can be net negative if FAQ snippets displace price and review rich snippets .

Ecommerce websites are a great example because users want to be able to compare one result against another before clicking through. Review and price snippets are a clear way to demonstrate to users that your product is more appealing, and can help to improve your organic click-through-rates.

One of our ecommerce customers had a set of product pages that consistently underperformed against their other product page templates when they began working with us. We identified that these pages lacked structured data, and recognised that winning review and price snippets was an immediate opportunity.

Although the customer had collected reviews for their products, these were not previously displayed on the page due to limitations they had with implementing changes on their website.

When we ran this test, we did two things; we added the actual review data to the page and we also added structured data with JSON-LD to win the price and review snippets. The price was already displayed on the page below the H1:

The result was inconclusive, meaning there was no detectable impact on organic traffic. When we did some research into why we might have not seen the results we expected, we found that the price displayed in the search results wasn’t necessarily showing us in the best light compared to competitors due to different bundling and minimum order sizes.

We decided to do a second follow-up test, where we only added the review markup, hypothesising that not having competitive pricing was making searchers less likely to click on our customer’s search results.

The on-page changes in the second version of the test were the same as before, but this time in the structured data we only included the information to win review snippets, without including price information. Here is a mock-up of how this looked in search results:

This was the impact on organic traffic, when we added just the review snippets:

This test was a big win, resulting in an estimated 20% uplift to organic traffic for this set of our customer’s product pages! The positive result in the second test supports our hypothesis that the price data wasn’t helping our click-through-rates in the first iteration, reminding us of two important lessons:

This result also meant that our customer was able to make an internal business case to get this change implemented, and our ability to function as a meta-CMS meant that we could roll out the change in the interim so they could immediately realise the gains to organic traffic.

To receive more insights from our testing keep an eye on your inbox, and please feel free to get in touch if you want to learn more about this test or about our split testing platform more generally.

The most important thing to know is that our case studies are based on controlled experiments with control and variant pages:
