---
source: https://www.searchpilot.com/resources/blog/what-is-seo-split-testing
title: [Updated 2026] What is SEO A/B testing? A guide to setting up, designing and running SEO split tests
scraped: 2026-03-22
published_on: 2026-01-16
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

# [Updated 2026] What is SEO A/B testing? A guide to setting up, designing and running SEO split tests

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/what-is-seo-split-testing
Published: 2026-01-16
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Running A/B experiments for SEO, as opposed to for users, is a complicated subject. There’s a lot of confusion over things like test design, controlling for external factors and some of the tools that can help you run experiments. This is a guide that covers all of that and more along with case studies and example tests.

## Extracted Body
SEO testing, also known as SEO A/B testing or SEO split-testing, involves changing a subset of randomly selected web pages to assess the impact of these changes on their organic search traffic. These modified pages are compared with a control group to account for external variables like seasonality or competition. Unlike user testing, which measures the impact of changes on website visitors, SEO testing evaluates how these alterations affect search engine rankings and visibility. While that might sound straightforward, there’s a lot of confusion around SEO testing, so this guide hopefully helps to explain the main things to consider when designing SEO tests.

The first thing that leads to confusion around SEO testing is language. A lot of what we see in the SEO world, often called SEO testing, is instead anecdotal evidence or badly controlled tests. I cover examples of both in this blog post: From Instincts to Impact - How to Design Robust SEO Experiments .

So to avoid doubt, when we talk about SEO testing at SearchPillot, we’re talking about running randomised controlled SEO tests. Unfortunately using SEO testing software like SearchPilot to run randomised controlled experiments hasn’t always been an option and still isn’t for many businesses. Instead, SEOs have had to rely on their hunches, best practices, or badly controlled tests to reverse engineer Google.

In clinical research, the robustness of your testing methodology is known as the ‘hierarchy of evidence’. My colleague Sam Nemzer wrote about this in The Hierarchy of Evidence for Digital Marketing Testing.

If your goal is to determine causal relationships (and it should be), randomised controlled experiments are widely considered the best way to do that.

In a randomised controlled experiment, a representative sample of the population you care about is randomly divided into either control subjects or variants.

The advantage of randomisation is that it helps control for any bias in the bucketing.

In the SEO world, the “population” that we care about is a population of pages, not people. Even still, the process is the same. Pages should be randomly assigned as a control or variant page. Without randomisation, you could accidentally (or deliberately) exaggerate the impact of a test

Here are some examples of other testing methodologies broken into two categories, badly controlled vs observational.

Some websites and parts of websites aren’t suitable for running SEO split tests. To be able to run tests, there are two primary requirements:

How much traffic? That’s a good question, and it depends on your website. Generally speaking, the more stable your traffic patterns are, the easier it will be to run experiments with less traffic. The more irregular the traffic to your website is, the more traffic you will need to build a robust traffic model.

We generally work with sites with at least hundreds of pages on the same template and at least 30,000 organic sessions per month to the group of pages you want to test on. This does not include traffic to one-off pages such as your homepage.

Can you test if you have less traffic? We’ve got some customers that test on sections of their site that only get a couple of thousand sessions per month, but the changes in traffic need to be much higher to be able to reach statistical significance.

The more traffic and pages you have, the easier it will be to reach statistical significance and the smaller the detectable effect can be.

Although not an exhaustive list, some example types of sites that are good for testing are:

By far, one of the most common questions we get is some version of:

That’s not surprising, given product teams and marketers have been doing user A/B testing for a long time, but there are some key differences.

One of the other differences between user testing and SEO testing is the way that the changes are made to the page. Changes made to a site using client side tools likely aren’t visible to Google.

Most user testing tools use client-side methods to change the page during the test. That means the user requests the old version of the page from the server, the file arrives in the user’s browser, unchanged, and then JavaScript makes the change. One of the known drawbacks of client-side A/B testing tools is “flickering”. Users will often see the old version of the page before it quickly changes to the new version. See the image below.

While flickering isn’t a great user experience, it’s generally not considered to impact the validity of the test results from a user perspective. Still, when testing the impact of a change on search engines like Google, using JavaScript can cause significant problems or even invalidate the results.

We’ve written a whole page about why server-side testing is better so I won’t repeat it here. However, the main point is that while Google understands more JavaScript than ever, it’s still not perfect and we frequently see uplifts in our tests from moving content from being client-side rendered to server-side.

This is most important if the JavaScript is slow to execute. There’s evidence to suggest that Google only waits five seconds for content to render , so anything that changes after this point will not be taken into consideration for ranking.

That’s pretty important if the point of the test is to see what Google thinks of the change.

For those reasons, SearchPilot is a server-side SEO A/B testing platform, that way, we can be sure that search engines see the changes that we are making and that we get the full benefit of those changes.

When testing for users, you make two versions of a page you want to test, and your testing platform will randomly assign users to either the A or B version of the page.

User metrics like conversion rate are then compared, and a winner will be declared if there is a statistically significant difference between the two pages.

We can’t do SEO A/B testing in that way for a couple of reasons:

The image below shows it clearly. With user testing, we see two versions of each page. With SEO testing, there is only one.

Before you can start a test, you need a group of pages that all have the same template. For instance, on an e-commerce website, you could select a group of category pages or product pages; on a travel site, you could use destination pages or flight pages. See the example travel site below.

In reality, it’s unlikely that we would ever run a test on only six pages, but the principles are the same whether there are six, 600 or 6 million pages. Keeping it simple will make it easier to explain everything, especially when we get to the test analysis section.

Although there are many differences between SEO testing and user testing, one common thing they both have is it’s essential to start with a solid hypothesis before you begin. We have a separate blog post that goes into more detail here: How to write a strong SEO hypothesis

I like to use this hypothesis framework from Conversion.com. You can see how I’ve applied the framework to the flight’s page template below as an example.

We know that: Google gives different levels of importance to content depending on its position on the page.

We believe that: Moving the content higher in the page will increase the importance of that text and therefore the relevancy of the page for our target keywords.

We’ll know by testing: Pages with content lower on the page compared to pages with the content higher on the page and observing organic traffic to each group of pages and measuring the difference in organic traffic.

Once you know what you want to test, you next have to decide which pages will be control pages and which will be variants.

Deciding which pages should be in each bucket is one of the most important, yet least understood, parts of SEO testing. There are two main criteria to consider:

SearchPilot has a proprietary bucketing algorithm that automatically creates buckets that match both of those criteria.

After the buckets have been selected, the change needs to be made to just the variant bucket of pages. Once the change has been made, there will be two different templates live at the same time, but there will only be one version of each page.

Notice that half of the flight pages in the example below have the content higher on the template. Those are the variant pages.

The fact that there is only one version of each page is a crucial point to note. It’s a common point of confusion for people new to SEO testing or those used to running user based A/B tests.

Regardless of whether a user or a search engine requests a page, they will see the same thing. This is covered in more detail in the section on the difference between SEO A/B testing and user A/B testing .

The explanation I’m about to go through is a deliberate attempt to simplify the math(s) involved in SEO A/B testing. Our engineering team has spent almost a decade building a neural network to analyse SEO experiment results, so it’s unrealistic that I’ll be able to give a comprehensive explanation in a blog post. Still, I’ll do my best to cover the basics.

You can also read how we doubled the sensitivity of our SEO testing platform by moving to our neural network instead of the causal impact model that we used to use.

Before the test begins, we need to understand the organic traffic patterns to the control and variant pages historically before any changes are made. To do this, we use historical data to the two groups of pages (usually about 100 days of data) and use that to build a model.

In the image above, you’ll see there are four lines, two are solid, actual traffic to control and variant pages, and two dotted lines, the models for the control and variant pages that we built using the existing historical data.

At this point, we have a few critical pieces of data that we need for SEO testing:

To build a forecast, we use the models to predict what we think the traffic to these groups of pages would be in the future if we made no changes to either set of pages.
