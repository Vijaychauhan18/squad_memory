---
source: https://www.searchpilot.com/resources/blog/business-not-science
title: We're doing business, not science. How to make sense of SEO A/B test results
scraped: 2026-03-23
published_on: 2025-04-07T14:26:05+01
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

# We're doing business, not science. How to make sense of SEO A/B test results

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/business-not-science
Published: 2025-04-07T14:26:05+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
When a test is based on a strong hypothesis, and yet our analysis is failing to reach statistical significance, we should make a consulting-style call on whether to recommend that the customer deploys the change. In many cases, where we believe that we are improving the site, or making it more discoverable from information retrieval first principles, and where the cost is not prohibitive, we should default to deploy. The primary purpose of testing in many cases is to avoid deploying changes that

## Extracted Body
Editor’s note: this article is based on an internal memo Will wrote for our Professional Services team called Default to Deploy . It’s reproduced here with minimal edits to make it suitable for an outside audience. There has always been a lot of debate about the best ways for companies to incorporate testing into their marketing, and where teams should sit on the pragmatic–dogmatic spectrum. This memo lays out the SearchPilot approach, and the ways we advise our customers to use their test data and results.

When a test is based on a strong hypothesis , and yet our analysis is failing to reach statistical significance for our chosen level of confidence, we should make a consulting-style call on whether to recommend that the customer deploys the change to their whole site / section.

In many cases, where we believe that we are improving the site, or making it more discoverable from information retrieval first principles, and where the cost is not prohibitive, we should default to deploy with the objective of compounding many small gains and taking our customers’ sites to states that will be valued more highly by the search engines in the future. We are aware that there are many possible small uplifts that we cannot detect with statistical confidence. The primary purpose of testing in many cases is to avoid deploying changes that have a negative impact while moving quickly and deploying proven and likely winners.

This is because we are doing business, not science . In scientific environments, high confidence in the result, and the ability to extrapolate from our discoveries are the priority. In business, we are typically seeking to beat the competition and should make decisions incorporating our prior beliefs, on evidence much closer to balance of probabilities, and using the test data mainly to justify the costs of changes and to avoid the damaging effects of negative impacts.

We can summarise all this as follows: we are here to help our customers capture any competitive benefit available, statistically significant or not. Default to deploy .

We will generally want to run all tests for at least some consistent time before attempting to make a call. This is based on our assumption that all real effects will take some time to be visible because of the need for a recrawl / reindex. After that point, when we would expect to start seeing whatever results we are going to see, we should start considering pragmatic decisions.

When in the top half of the quadrant below, we should weigh the benefits of quick decisions to deploy with the benefit of waiting for more data to get higher confidence or greater certainty of the magnitude of the uplift. The top half is about balance of probabilities, avoiding drops, and winning in the long run, while the bottom half is more about justifying the cost of the change and getting ROI data.

Note : strength of hypothesis in what follows is subjectively-defined as it will depend on context, but a good way of thinking about it is that strong hypotheses are those that are like recommendations we might make in a consulting environment where we couldn’t test and had no specific data on likely success.

When we have reached statistical significance on a test , we can say things like:

It’s very common, however, to find ourselves in a situation where a test has not reached statistical significance. In these cases, I argue that we should behave differently in each of the four quadrants above depending on the combination of costliness of change and strength of hypothesis. Here are some examples of how we might think about a test in each quadrant:

We only recommend deploying this kind of change when we reach true statistical significance.

We might recommend rolling back (not deploying the change we tested) for any of four reasons:

We are all discovering as we go what the most effective recommendations are in a test-driven SEO world. We want to find ways of thinking and communicating that make customers happy and align with our way of driving effective, accountable search results. We should be seeking to serve customers’ genuine best interests with the best recommendations we can make.

The reason I started thinking about this particular angle is that I noticed a trend as we started having more and more people across the company running tests, analysing data, and making recommendations to our customers. In write-up after write-up, I saw different consultants say some variation of “this test is inconclusive, so we should roll it back” . In particular, the thing that most motivated me to think about how we could do this better was seeing us make that recommendation when our statistical analysis showed an upwards trendline that was never going to reach statistical significance at the 95% level but that was indicating that we’d predict an uplift on the balance of probabilities .

In the long run, we aim to be successful by giving our customers a genuine competitive advantage. At the margin, if we have to choose between being certain something brings an uplift, or capturing any uplift that is there, we should choose the latter especially when we believe there is only a small chance of a negative impact.

When we are competing against consulting recommendations made without testing, our biggest wins come from never deploying losers as well as deploying winners. We can beat non-data-led consulting with a strategy of “only deploy winners” but that should lose over time to a strategy of “deploy winners plus strong inconclusive results”.

Beyond customer relationship benefits / risks, I see two primary effectiveness reasons for taking the kind of pragmatic approach I describe here:

We know that there are uplifts that are too small for us to detect with statistical confidence - both in theory and in practice. There is a world of marginal gains that are smaller than this that compound and can add up to a competitive advantage if we can on average deploy more small positive changes than negative ones.

When we build hypotheses from our understanding of theoretical information retrieval, or from user preferences that we believe Google might move their algorithms towards in the future, we may run tests that are not immediately positive, but that have a positive expected future return .

If we only allow ourselves to deploy changes that are provably beneficial already, we may lose out to competitors who are prepared to act on speculation or announcements of what Google might value more highly in the future.

Beyond the statistical risks (most obviously, the risk of deploying the occasional change that is actually negative), the biggest strategic challenge to this approach is that when we look back at a sequence of tests and enhancements, we won’t have strong numerical arguments for all of them to compare to their implementation cost. It’s worth remembering that statistical confidence is worth something in the reviews / retrospectives that look at uplifts generated by the activity. We may find some customers push more towards waiting longer for statistical confidence and / or tweaking and re-running tests in search of stronger uplifts because they particularly value this confidence. This is fine, but our default approach is to seek the greatest business benefit for our customers rather than the greatest certainty.

One of the other risks with this approach is the chance that serious experimentation teams and individuals with a scientific bent may feel that we are being misleading or dishonest. I believe my suggestions are compatible with their opinions for the most part, but it is easy for misunderstandings to arise, or for us to use language that might cause someone not to trust us.

Key point to note: any language like nearly significant or trending to significance is widely derided and mocked . I have attempted to outline language we should use in situations where we haven’t proved the result we hoped for, but in any case, I believe we should try to avoid this style of talking about our results.

What ends up connecting my view together with the stricter scientific view is two basic facts:

Lizzie Eardly presented at CXL Live and gave a passionate talk arguing:

She argued this strongly and strenuously, but her actual advice is not necessarily entirely at odds with my recommendations in this document:

You can read more of the Skyscanner team’s thinking on their experimentation blog in the series they call statistical ghosts (see articles linked from that overview, especially the first in the series ).

I think I am mainly arguing that when a test hasn’t reached statistical significance then at worst we should act as if the data is noise rather than the temptation to assume it is evidence that the test has failed.

There is much confusion around hypothesis testing - in particular caused by the language of null which does not mean “no effect” - it refers to the null hypothesis and the p-value which is all about accepting or rejecting said hypothesis. Calling it “null” makes us tempted to assume we have proven that there is no effect when we declare a test null, whereas in fact, we have shown only that it is plausible that the magnitude of effect observed could have come from a situation where there is no real effect (see: The Null Ritual [PDF]). As such, we should seek to refer to tests that do not reach statistical significance as “inconclusive” rather than “null”.

At the same CXL conference, I had a chance to quiz Lukas Vermeer who is in charge of experimentation at Booking.com about the ideas underpinning my argument here. He said that his advice, when someone comes to him with a inconclusive test result off a decent hypothesis is “deploy if you like, but don’t claim you have learned something” . In other words, you can use the strength of the hypothesis to make the case that you should deploy anyway, but don’t use the lower performance thresholds to make the case for additional tests in the same area or for developing new features based on the test.
