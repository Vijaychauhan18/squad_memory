---
source: https://moz.com/blog/cwv-common-ground-seo-developers
title: Core Web Vitals: Finding Common Ground Between SEOs and Developers
scraped: 2026-03-23
published_on: 2022-04-05
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Core Web Vitals: Finding Common Ground Between SEOs and Developers

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/cwv-common-ground-seo-developers
Published: 2022-04-05
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
How do we start conversations and support initiatives that get developers and SEOs all working towards the same goal? Is Core Web Vitals the common ground we need? In this conversation with Moz Developer, Lucas Rasmussen, we explore his recent project aimed at improving our A/B testing experience…

## Extracted Body
Working with developers to align on technical and SEO priorities is a challenge faced by many in-house SEOs, and by SEO agencies offering recommendations. How do we start conversations and support initiatives that get developers and SEOs all working towards the same goal? Is Core Web Vitals the common ground we need?

In this conversation with Moz Developer, Lucas Rasmussen, we explore his recent project aimed at improving our A/B testing experience and how it overlapped with Core Web Vitals.

Lucas: I’m a Web Developer at Moz. I manage the Moz website and content management system (CMS).

Question: What was the main objective of your recent Cloudflare project?

Lucas: I started a project based around making an A/B testing suite for the Moz website that focused on improving split test results and a better more consistent visitor experience. The problem we had to solve was to run client side A/B tests without a different customer/page experience. When someone loads the page as part of an A/B test, the page flashes white for a split second and it affects the experience, which affects the overall validity of the test. We wanted to do better for Moz.

We chose to create a system using Cloudflare, where Cloudflare automatically shows two different types of pages. This way we could build a system where the A/B test page loads just as fast as if it wasn’t an experiment.

I had an ambitious goal of getting average page load time across the whole site down to two seconds.

Lucas: All-in-all it took around 2-3 weeks to complete with an additional two weeks of planning. This also involved changes with our CMS, and a few misplays along the way.

We needed some help from our engineers, learning how Cloudflare workers actually work. They are very powerful!

The core work took one week in its entirety, working out what needs to be done — getting feedback, responding to that, and actually doing the work.

Lucas: I’m tracking my results in the Cloudflare dashboard specific to Web Analytics. We are currently limited to 30 days of tracking, I’d love to see more to see changes over time.

It might be worth noting that if you want more data, Moz Pro Performance Metrics section of Site Crawl displays historical data for up to 90 days for tracked URLs.

I’m keeping an eye on what’s going on with the page load time, especially the request time. When the timing goes up, that’s a flag that there is a problem somewhere. It indicates to me that something isn't cached.

Looking back at our ambitious goal of getting average page load time across the whole site down to 2 seconds. We have currently plateaued at 2.6 seconds. But we are tracking a large portion of users across the whole site.

Question: What was the most enjoyable part of the project for you?

Lucas: Turning it on and seeing the impact and change to page load time — l Ioved being able to see real-world results. And in this case IT WORKED. There are so many changes you can make and you think they are going to change something, and even if you know they are going to make a difference, you might not see the impact... When I changed users to cached the difference was significant, from around 1,500 milliseconds to 200 milliseconds.

Question: What do you know about the importance of Core Web Vitals?

Lucas: I do have visibility into Core Web Vitals as a concept. LCP (Largest Contentful Paint) in particular is a metric I track in the Analytics dashboard.

If SEO practitioners are looking to explore their Core Web Vitals and start conversations with their developers, they can do that through the Moz Pro interface.

The Performance Metrics feature in Moz Pro really enables SEOs to automate and streamline performance analysis so you can collect and track performance in one place. It also allows you to identify critical pages that need to be optimized. Get a holistic viewpoint on how your pages are performing for core web vitals and performance, alongside other additional SEO data like page authority, rankings, traffic and other crawl issues. We provide non-technical, non-jargony language that helps you understand how you can start fixing things to improve those scores.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
