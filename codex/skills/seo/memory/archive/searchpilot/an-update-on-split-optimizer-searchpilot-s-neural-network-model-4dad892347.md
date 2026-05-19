---
source: https://www.searchpilot.com/resources/blog/an-update-on-split-optimizer-searchpilots-neural-network-model
title: An update on Split Optimizer: SearchPilot’s neural network model
scraped: 2026-03-25
published_on: 2024-11-22
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

# An update on Split Optimizer: SearchPilot’s neural network model

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/an-update-on-split-optimizer-searchpilots-neural-network-model
Published: 2024-11-22
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
We’ve optimized our proprietary neural network model, Split Optimizer. Discover how customers benefit from more tests with positive results, faster capabilities, and deeper analytics.

## Extracted Body
Unsurprisingly, one of the things our clients tell us that they care about most is the ability to predict more uplifts with greater confidence.

In this article, we’ll explore how the latest updates we’ve made to our Split Optimizer, our sensitive neural network model does exactly that.

Spoiler alert: in our testing sample, we went from 13% of a sample of tests being positive at the 95% confidence interval to 29% being positive at the 95% confidence interval .

We don’t just help our customers run individual SEO tests. We help them design entire experimentation programs. When you’re running an experimentation program, it’s important to remember that you’ll have some winning tests, some losing tests, and some tests that are inconclusive or insignificant. All of these test results are valuable to your business .

Losing tests highlight things you should avoid. This enables you to stay ahead of the competition, and, sometimes, they even point the way to the future winners. And the tests that don’t result in any measurable impact help with efficiency. They show you what isn’t worth implementing or maintaining and ensure your engineers only work on features that deliver meaningful results.

Despite all of this valuable insight, we know that everyone wants more winning SEO tests. Not only is it human nature, but we also know that winning SEO tests are often the source of the most substantial and most concrete business impacts. So we know anything we can do to uncover them including confidently identifying even smaller uplifts is going to pay off for our customers.

Back in 2019, we moved away from Causal Impact, the industry-standard open-source tool at the time. Instead, we moved towards a neural network model that was twice as sensitive and allowed us to identify uplifts that were much smaller than before.

So, the Split Optimizer isn’t new. And we’re not announcing any new features . But, a major focus of our research and development has been further, ahem, optimizing the Split Optimizer. And I’m pleased to announce we’ve made some breakthroughs.

We've improved the way we train our models with two new approaches.

We won’t dive into the mathematics and statistics in this article. But let’s look at what these approaches mean when it comes to real tests.

From the SEO analytics data below, you can see the test is not significant at the 95% confidence level. It’s borderline at 90% confidence. This is exactly the kind of test where we’d like to know the truth: is this predicted uplift real or not?

We used our two new models on the same data. The image below shows that both get progressively better bottom ends of their confidence ranges at both 90% and 95%.

This is what we mean by better models. The midpoint of the range typically barely changes, but the confidence intervals grow tighter, enabling more tests to be declared statistically significant. But looking at just one test doesn't tell us a great deal. So, let's explore some benchmarking data, shall we?

We ran our previous best model over a representative sample of real, old tests.

The purple bar reflects our previous best model. It was found that 13% of the tests showed statistical significance. Note that this was already double the sensitivity of Causal Impact .

With Local Optimizer, that 13% jumps to 18% or 19% at 95% confidence.

From there, we threw more computer power at it and ran a much more extensive search for the best-performing examples to train the model. We call this Global Optimizer 10 . This model reached statistical significance on almost 29% of the tests in the sample. That’s more than double our existing best model! You can watch the full video about this here .

Most importantly, these improved results don’t compromise the accuracy of the model. Instead, we are creating more sensitive models that can detect smaller uplifts at any given confidence interval.

Initially, this new method will only be deployed in The Long Room, where our professional services team can test it on real experiments. While we carried out the R&D on a robust sample of tests, we still want to be prudent before deploying this change as the default model by running more real-life tests through it. Our professional services team works closely with the data science and engineering team to identify which tests are good candidates for Split Optimizer.

Getting more winners is most of our customers’ top priority. And we attack that problem in a variety of ways. This includes things like helping them identify more ambitious SEO tests more easily and gathering additional data from Googlebot crawls and Google Search Console. But statistical breakthroughs like this are one of our most powerful tools. So, we're looking forward to bringing this increased power and greater win rate to all our customer accounts. Want to find out more? Speak to one of our experts about taking SearchPilot for a test flight today.
