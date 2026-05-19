---
source: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-react
title: What's the SEO impact of using React on product pages?
scraped: 2026-03-22
published_on: June 23, 2021
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

# What's the SEO impact of using React on product pages?

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-react
Published: June 23, 2021
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
This week in #SPQuiz, we asked our Twitter followers what they thought would happen to an ecommerce site’s product pages' SEO performance if we served them via the React JavaScript framework. Just over half of our Twitter followers thought this change wouldn’t have a detectable impact, with the remainder being split between positive and negative. Perhaps this reflects SEOs' faith in frameworks such as React, with them having been around for a few years now.

## Extracted Body
If you aren't familiar with the fundamentals of how we run controlled SEO experiments that form the basis of all our case studies , then you might find it useful to start by reading the explanation at the end of this article before digesting the details of the case study below. If you'd like to get a new case study by email every two weeks, just enter your email address here .

This week in #SPQuiz, we asked our Twitter followers what they thought would happen to an ecommerce site’s product pages' SEO performance if we served them via the React JavaScript framework.

Just over half of our Twitter followers thought this change wouldn’t have a detectable impact, with the remainder being split between positive and negative. Perhaps this reflects SEOs' faith in frameworks such as React, with them having been around for a few years now.

In fact, this result was positive for SEO performance, providing a 13% uplift. You can read more about this result and why it may have come about below.

Over the last few years, a lot of companies have taken the decision to use JavaScript frameworks such as React, Angular or Vue.js. These frameworks can add increased functionality to websites, and can allow websites to behave more like apps than traditional collections of webpages. From an SEO standpoint, there are some potential pitfalls - without careful consideration, it’s possible to make your content inaccessible to search engines, or at the very least increase the demands on search engine bots to have to render the JS components of a page in order to index your pages.

That being said, it’s possible to work around these pitfalls by server-side rendering (SSR) the important parts of pages. SSR means that for the initial request for a page, the JS components have to be run server-side before the HTML of the page is sent to the browser. This ensures that even browsers without JS running will be able to render the page.

One of our ecommerce customers decided to implement the React framework on their product pages for a few reasons, including an enhanced user experience for the purchase process, and improvements to page speed. They implemented it with SSR, and there were no changes to the content of the page apart from some minor design tweaks. Despite that, we decided to test its impact on SEO performance to make sure it didn’t have an unforeseen adverse impact, and to see if the UX and speed improvements would lead to increased organic traffic.

We tested this by using request modification to add a request header to variant pages which directed the host server to return the new, SSR React-based product page in place of the existing version of the page.

This test resulted in a 13% uplift for the new, React-based product page, compared to the old version.

The new product page also proved to be beneficial for conversion rate in a separate CRO test. For these reasons, the customer deployed this new product page template across their websites.

In this particular case, the React page was well built for SEO, in that all of the relevant content and meta tags were in place in the source code, due to the fact that it was server-side rendered. If that had not been the case, we may have seen a completely different result, as most SEOs who have seen a badly implemented JS framework deployment can probably attest.

In this case, however, there was no negative impact of the template change, and it appeared that the improved UX and page speed of the new template were sufficiently beneficial to return a marked improvement in SEO performance.

The most important thing to know is that our case studies are based on controlled experiments with control and variant pages:
