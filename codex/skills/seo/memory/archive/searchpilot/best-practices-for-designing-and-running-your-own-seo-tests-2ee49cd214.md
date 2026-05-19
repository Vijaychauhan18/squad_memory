---
source: https://www.searchpilot.com/resources/blog/seo-test-best-practices
title: Best practices for designing and running your own SEO tests
scraped: 2026-03-22
published_on: 2023-08-09T15:36:39+01
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

# Best practices for designing and running your own SEO tests

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/seo-test-best-practices
Published: 2023-08-09T15:36:39+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Simply running SEO tests isn’t enough to guarantee success or even valuable data insights. But by establishing the right setup, processes, and systems to run tests, teams can better trust the entire process. Learn from this comprehensive playbook on what to consider when designing an SEO test, and start testing yourself!

## Extracted Body
For better or worse, SEO split testing has a perception of being complex and understood by few.

This has many unintended consequences, from marketers thinking they don’t need it to marketers being too intimidated by the concept of it that they never learn and run their own tests.

That’s a shame because if you are running a high-traffic website, there is a great chance you’ll benefit from running your own controlled SEO testing.

In this post, I’m going to share some strategies for how to design and run your own tests, including:

In an SEO context, controlled SEO testing is the ability to take your hypothesis, set up groups of control and variant pages, and then roll it out to some pages (variant) and not to others (your control). You can then apply statistical analysis to figure out whether that was a good idea or not.

For instance, one of my favourite examples is when we ran a bunch of tests to see the impact of content quality on category pages (this is a similar one where we tested removing boilerplate text ) for a large ecommerce customer. This customer had some text already on their category pages (i.e. The classic boilerplate copy and standard keywords.) It didn’t read as great, unique content on each one of those pages. And, we ran a test that tested writing better copy for a subset of those pages.

So, we wrote new text for the pages that were changing and then identified a control group of pages that looked statistically similar to the pages we were changing. (Note: SearchPilot does that automatically) . Then, we rolled out that change just to those subset of pages and then analysed the results to figure out if that was a good idea.

Now that you know what controlled testing is and why it matters, here is how to design your ideal setup.

For an ideal setup, you want to have a solid backlog of tests you want to run with a good range of bold hypotheses. Then, you want to be collating and prioritising the tests you want to run based on your unique needs.

You also want the ability actually to execute these tests, build them, deploy them, run them efficiently and quickly , ideally without involving tons of different teams.

The dream is essentially to run them as fast as your website will allow. So the bigger your website, the more tests you could be running in parallel and potentially the quicker you can reach statistical significance. You also always want to have a test running in every site section that can have one running. So, if you run the best, boldest hypotheses and always have them running across all the possible site sections, you can maximise your learning and results.

Of course, the reality is that’s very hard to achieve given resourcing constraints on smaller teams and complexity questions on larger teams.

Here’s how we recommend building the most effective SEO testing program possible:

One of the most critical aspects of designing SEO tests is having bold hypotheses .

You really want to test things that are big enough to move the needle.

You want to be able to test some big things that might be big wins. By its nature, that means it’s risky. It might be a big loss as well. And that’s why we test. By writing and testing bolder hypotheses, you minimise the risk of having false positive or false negative outcomes. The end result is you get more confident in what you see in the statistics.

What we see happening with a lot of SEO teams is that they’ve built out a complicated way of being able to run some tests with the help of their engineering and data science teams. They’ve kind of cobbled together a process across multiple teams, but they can run maybe one test a month. Whereas, at SearchPilot, we are pushing a lot of our customers to say, actually, the best practice is to step up that cadence. It depends on how big your website is, but some should be running hundreds a year rather than five or ten a year.

This is a message from one of our large customers talking about their testing cadence and win-rate:

When they are running dozens, or hundreds of tests a year, you’re hopefully testing big stuff, and you’ve got great statistical analysis to go with that. That’s how you 10x your learning and results.

A key component of running more tests faster is training and documentation. You need to make sure the entire marketing team is bought in and has whatever level of knowledge they need to do their job. So, an SEO analyst might need to know how to build tests, while a VP of marketing might need to know how the data is going to be presented and what that means.

Everyone needs to understand why we’re testing, what tests look like, what the results look like, and how to understand them.

Your business isn’t stagnant, so neither should your SEO testing practices be. However, when it comes to how often you should tweak your process, this will depend on the organisation.

SEO testing best practices don’t change that quickly. For instance, in our company, we’ve had a couple of major evolutions where we’ve gone, for example, from causal impact to our own proprietary neural network model, which roughly doubled the sensitivity of the experiments that we could run. And we also rolled out full funnel testing where we could test user experience at the same time as we could test SEO changes. But aside from some of those big things, it’s been more of a continuous process of gradually tweaking and improving the sign-off processes or the analysis approach.

Here are some of the most common mistakes that we see SEO teams make and how to avoid them.

One of the biggest mistakes we see is not having a systematic approach to testing. Having different, ad hoc approaches means you aren’t creating a proper hypothesis and are likely just trying to analyse results after the fact.

Doing it this way is very hard to not spot effects and be confident that you’re seeing an effect that is really due to the change that you made as opposed to other trends like seasonality, what your competition is doing, or Google changes.

When you come from an organisation that is slow to run tests, you might be incentivised to cherry-pick only a select few tests that are likely to have the safest outcomes. This can often result in playing small, which reduces not only your learnings but also the chance of big wins. After all, if you never sign off on a bold test, you can never get a bold result.

There are two main failure modes we see when it comes to best practices and testing:

Both of these approaches are suboptimal because you definitely want to be testing wild card things that might not be exactly Google’s recommended approach. They don’t always know what’s going to work.

Not to mention, we’ve seen over and over again in tests that our team has run that tried and true SEO wisdom doesn’t produce the same results for every organisation. The classic example of this is keyword title inclusion, where we’ve seen negative outcomes in a few cases (see, for example adding video to titles and adding seasonal messaging ).

There’s a natural tendency when you get presented with data that says, for example, you’ll see an average 6% uplift, to go spot check one of the URLs, just to see it in real life. The problem is that we’re often dealing with big data here. So, there may not be a representative URL. The computers are doing the job for us, which is summarising what’s going on across 10,000 pages, and we can’t eyeball 10,000 pages.

We need to strike a balance between a healthy degree of skepticism with being able to trust what the statistical analysis is telling us.

After all, we’re running these tests for business, not science . If you never trust the results enough to deploy anything, the business won’t reap any of the potential benefits. That’s where our default to deploy framework has come in handy.

For instance, I advise people to get comfortable with this by looking at the quality of the model before running the test. Oftentimes, especially on large traffic websites, you can see it’s really good at predicting what’s going on. I find that gives me confidence that if that line starts diverging after the experiment rollout, then I’m more confident that it was as a result of the change that we made.

With this approach, we are looking to rule out big drops, big problems, or even small drops, depending on the website. So, if we have a very strong hypothesis, we have the best guess that it’s positive, and the downside marginal losses are likely to be limited. We should default to deploy, even though we haven’t reached statistical significance on that particular test.

If you’ve never run an SEO test before, then this process will take time. You’ll likely iterate on it as your marketing team—and the company as a whole—gets more confident in this approach.

However, if you are looking to speed up your learning, our team at SearchPilot can help. Request a demo here .
