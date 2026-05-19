---
source: https://moz.com/blog/transitioning-to-ga4
title: Transitioning to GA4: Is this the Right Analytics Move for Your Team?
scraped: 2026-03-23
published_on: 2022-07-25
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

# Transitioning to GA4: Is this the Right Analytics Move for Your Team?

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/transitioning-to-ga4
Published: 2022-07-25
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
As you've likely heard, Google plans to fully retire Universal Analytics for GA4. Here's what you should know before the transition.

## Extracted Body
Back in March, Google announced that the current version of Google Analytics Universal (commonly known as Universal Analytics) will be deprecated as of July 1, 2023, in favor of the new version, GA4 .

As a part of this transition, Google will be dropping support and tracking for Universal Analytics (UA), which has been the standard reporting tool for millions of websites since 2012. According to Google , historic data from Universal Analytics will be accessible for " at least six months" after the July 2023 retirement date. Keeping it ambiguous, Google adds:

"In the coming months, we'll provide a future date for when existing Universal Analytics properties will no longer be available. After this future date, you'll no longer be able to see your Universal Analytics reports in the Analytics interface or access your Universal Analytics data via the API."

While 2023 may seem like ample time to prepare for this transition, the truth is you need to check a few boxes sooner rather than later, especially if there are important year-over-year (YoY) metrics that need to be tracked without disruption. In short order, capturing data for next year's YoY metrics means that your business will need to take action before the end of summer 2022 to ensure:

YoY reporting (including access to historical data) – the full functionality you want/need from your data and analysis toolset

Your team is prepared to use the new tools (regardless of what new solution you choose)

Though Google "strongly encourages" users to make the transition to GA4 “as soon as possible”, we’d argue that – given the scale of the change and the work/resources it will require to properly transition to GA4 (as outlined in more detail below), now is the right time to pull up and evaluate your data tracking stack.

It’s too easy to make assumptions about needs and requirements being met based on “what we’ve always used,” and end up backed into a corner.

Instead, let’s explore this in detail and consciously select the right platform for your needs.

The transition from GA Classic to Universal Analytics was simple. All you needed to do was update the tracking code on your website. Your data was the same. The interface, metrics, etc. – all largely the same. That's not the case this time around.

Google made some big changes in GA4 that may take time to adjust to. This has many implications, including large differences in:

the base skills/knowledge set needed for people using the new platform

the data set itself (GA Universal data is not compatible with GA4 data)

access to certain (well-loved) functionality, and even some metrics. Some will no longer be available OR require a thorough setup to access.

In short, GA4 is quite literally a re-imagining of how to track and measure website interaction. Much like the transition from USB to USB-C , this means changes to systems/processes, tools, skills/training, and potentially your annual budget, to ensure a smooth transition.

The most glaring difference between Universal Analytics and GA4 is the reporting interface.

Compared to Universal Analytics, GA4's interface is more simplified and streamlined. This is because some of the metrics, views, and reports you see in Universal have either been removed or replaced.

The updated interface looks much like Google Data Studio in the way analytics are presented. So if you're familiar with Data Studio, then navigating GA4's interface may be more intuitive for you.

Still, changing from what's known and normal always comes with some level of pain and processing. Even for those who are well-trained in the world of Universal Analytics, adjusting to a new reporting interface will come with some confusion – and perhaps some roadblocks and resistance.

Once you start perusing the new interface, you'll notice that Google has changed some of the terminology. "Behavior" is now "Engagement", "Segments" have become "Comparisons", and "Channels" is now "User Acquisition". The "All Pages" reports have been renamed as "Pages and Screens".

Google has also reorganized the "Audience" reports, and the information that used to be in the "Audience" reports are now in other sections, including "User" and "Acquisition" sections.

Navigating GA4 won't necessarily be a frictionless experience, especially for those who are regularly immersed in Universal Analytics.

Universal Analytics and GA4 use different measurement models. While UA relies on a session- and pageview-based data model, GA4 stands on an event-based model. With GA4, any interaction can be recorded as an event.

The somewhat confusing thing about this change is that, in UA (and all previous versions of Google Analytics), an event has an action, category, label, and its own hit type. But in GA4, there is no action, category, or label.

For example, in GA4, you can have an event called page_view, and this event can contain parameters: page_title, page_referrer (previous page URL), and page_location (current page URL).

Automatically-collected events: You don’t have to manually activate these events. GA4 automatically tracks them when you install the GA4 base code. Examples include first_visit, session_start, and user_engagement.

Enhanced measurement events: GA4 also collects these events automatically, but you’ll need to enable (or disable) enhanced measurement settings in your Data Stream depending on your website functionality. These events include outbound clicks, scrolls, file downloads, and site searches.

Recommended events: These events are not implemented in GA4, but Google recommends that you set them up. If you need an event that’s not collected automatically or is not a part of the enhanced measurement events, you can check for it in recommended events. Examples of recommended events include sign_up, login, and purchase.

Custom events: These are events that you can create and implement by yourself. You should only use custom events when you need to track an event that you can’t find in the first three categories. You’ll need to write and design custom code to implement the custom event you want to track. Fortunately for the less code-savvy, Google has rolled out a tool to assist in importing custom events from Universal Analytics to GA4.

Overall, this approach actually allows more flexibility and configurability to WHAT is measured on your site.

However, with more flexibility comes more set up and forethought, so having a documented measurement plan is HIGHLY recommended for GA4.

If you use BigQuery, then you'll be happy to know that GA4 connects natively to it. With Universal Analytics, the only way users can export data from GA is through the enterprise version (GA360). But with GA4, users can export data at no additional cost.

Keep in mind the way data is structured in GA4 is different from how it's structured in Universal Analytics. So you might need to remap your GA4 data before you'll be able to move it into BigQuery (we find this GA3 to GA4 tool helpful in formatting historical data to align with GA4.) Once you've done that, you'll be able to run SQL queries more easily.

The BigQuery integration is available, so we definitely recommend setting it up ASAP. Why? Well, GA4 only stores data for a maximum of 14 months (and default settings are only two months), so for accurate YoY comparisons, you'll need to rely on this year’s BigQuery datasets you gather now or suffer the losses.

Some existing features like views, custom metrics, and content groups will no longer be supported. If your team relies on these existing features, adapting to GA4 will likely involve figuring out how to fill certain measurement gaps. And if the transition becomes too compromising and painful, keep in mind that there are alternatives.

As you've likely gathered, moving from GA Universal to GA4 is not a light undertaking. Between adapting to GA4's new reporting and measurement models and learning its revised labeling and terminology, it's going to be a heavy transition no matter what your situation entails. Consequently, now is the time to verify that the outcome of all this work will in fact meet your needs.

All users of Universal Analytics (that's close to… well, everyone, really), will need to start planning for how and where to continue measuring your website performance.

You'll also need to take action to save your data for 1) posterity and 2) YoY reporting, given that the data set is NOT compatible, nor will be available to you (if you don't take steps to preserve it). AKA: we also need to plan for when this needs to happen.

In terms of the how and where, ultimately, there are three primary options (four if your team takes a hybrid approach of combining options 2 and 3), each of which is outlined below.

The first option is the big one on most people’s minds. That is, opting to use GA4 and taking the proper steps to preserve data integrity and seamless measurement.

If you determine that GA4 is the right fit, the major boxes to check involve identifying measurement gaps and revising KPIs (or measurement protocols) to fill these gaps. You'll also need to start collecting data (now) for later YoY reporting needs, as well as ensuring your team is up-to-speed on the new GA4 interface.

Given that the interface in GA4 is considerably different from the interface in Universal, any teams currently using the latter will likely require additional time and training to adapt to the new structure.

Due to some of the identified gaps, we're exploring options for both free and paid alternatives to GA4 for our own team. Among the free analytics tools worth considering are Clarity , Clicky , and Mixpanel . While the free versions of these tools are great, some offer upgradeable paid options for more robust capacity/capabilities.

Some businesses may find that their requirements are better met by moving to paid tools or premium versions of certain analytics products. Of those worth exploring are Matomo , Adobe Analytics , Heap , Kissmetrics , Heap , and Woopra . The latter two offer free plans but, in our experience, they’re highly limited.

Keep in mind that not all of these analytics tools offer the same level of utility and features, and don’t forget about privacy and security to support GDPR and CCPA regulations, a growing concern for many brands.

While any new tool would require onboarding, many of them offer training as part of the client onboarding process. Most of these analytics options also offer a free trial, so you can vet a platform hands-on before committing to it.

On-premise/first-party enterprise solutions can deliver greater utility, privacy, and compliance, depending on how they’re leveraged. Platforms like Matomo and Countly do offer on-premise implementation, meaning that your company would own ALL of the user data, instead of being passed through to Google Analytics (or any other third party).

If you have other owned digital platforms, coupling an on-premise analytics suite with solutions like Looker (owned by Google!) or PowerBI can allow you to access data across different teams and properties easily.
