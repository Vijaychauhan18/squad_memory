---
source: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-forcing-google-respect-meta-descriptions-data-nosnippet
title: Which is better: our meta description or Google's?
scraped: 2026-03-22
published_on: November 19, 2020
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

# Which is better: our meta description or Google's?

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-forcing-google-respect-meta-descriptions-data-nosnippet
Published: November 19, 2020
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
This week on Twitter, we asked our followers what they thought would happen to organic traffic when we forced Google to respect meta descriptions, instead of pulling content from elsewhere on the page into search results. This is what they thought: This was by far our closest #SPQuiz result so far, with a tie for Positive and Inconclusive, each on 35.7%, and Negative not too far behind in third place.

## Extracted Body
If you aren't familiar with the fundamentals of how we run controlled SEO experiments that form the basis of all our case studies , then you might find it useful to start by reading the explanation at the end of this article before digesting the details of the case study below. If you'd like to get a new case study by email every two weeks, just enter your email address here .

This week on Twitter, we asked our followers what they thought would happen to organic traffic when we forced Google to respect meta descriptions, instead of pulling content from elsewhere on the page into search results. This is what they thought:

This was by far our closest #SPQuiz result so far, with a tie for Positive and Inconclusive, each on 35.7%, and Negative not too far behind in third place. It seems our followers' opinions were incredibly divided, with no consensus on what would happen.

In fact, the smallest group were correct! Forcing Google to respect meta descriptions turned out to harm organic traffic in this case, as you’ll see when you read the details below.

A recent study by Portent’s Evan Hall found that around 70% of search results have a snippet in their search results that is not taken from the page’s meta description. There are various reasons why this might happen - Google may choose to rewrite descriptions to include phrases that the searcher includes in their query, or simply that it perceives to be more relevant to users. Some pages don’t even have meta descriptions, while some websites use the same meta description across wide swaths of their pages, which means it’s easy for Google to find something more suitable to use in search results.

One particular SearchPilot customer had noticed that their meta descriptions on a location-related page type were consistently being ignored by Google. Instead, snippets of text were often being pulled in from the site’s navigation menu and facets, listing nearby locations. This wasn’t a case where the meta descriptions were missing or irrelevant - the SEO team were pretty confident that they had written good descriptions!

Luckily, there was a solution at hand. Since September 2019, Google has provided the option of adding data-nosnippet attributes to elements, which instruct Google not to use that part of the page for snippets in search results.

For this test, we added a data-nosnippet attribute to a div just inside the body tag to the variant group of pages. This prevented Google from pulling any content from the body of the page, including the navigation and facets that it was previously using. In effect, this forced Google to revert back to the meta description (which is found in the head of the page, not the body).

We observed this change having the desired impact: Google began using the pages’ actual meta descriptions across the board, rather than other snippets of text from the page.

This test immediately started trending downwards, and within two weeks, had hit statistical significance for a negative result! We gathered another couple of weeks of data, and overall this test showed a 3% negative impact on organic traffic for pages we applied it to.

It turns out Google knows best (in this case - check out some of our other case studies to see when we’ve proven Google wrong about other things). Google has access to so much user data, and clearly in this case, Google was able to lean on that data to provide a snippet that was attracting more clicks than our descriptions, even though it may appear to us to have generally been junk scraped from the page!

After seeing this test result, we decided to test adding nearby location names to meta descriptions, taking after Google’s intervention, but doing it in a way that should have made more sense to users. This followup test was inconclusive, showing that even doing a “better” version of what Google had tried wasn’t a significant improvement. After this, we decided just to let Google do its thing!

To receive more insights from our testing sign up to our case study mailing list , and please feel free to get in touch if you want to learn more about this test or about our split testing platform more generally.

The most important thing to know is that our case studies are based on controlled experiments with control and variant pages:
