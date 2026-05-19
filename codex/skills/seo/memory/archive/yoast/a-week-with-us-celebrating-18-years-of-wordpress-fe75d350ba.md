---
source: https://yoast.com/celebrating-eighteen-years-of-wordpress/
title: A week with us: Celebrating 18 years of WordPress
scraped: 2026-03-23
published_on: 2021-05-27
tags: live_feed, phase1_ingest, yoast, publication, seo-education, wordpress-seo, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Yoast SEO Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# A week with us: Celebrating 18 years of WordPress

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/celebrating-eighteen-years-of-wordpress/
Published: 2021-05-27
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week’s post falls on the 18th birthday of WordPress. So, let's look back at what our team did this week and when they started using WordPress!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

This week’s post falls on the 18th birthday of WordPress.org. What a ride it has been! Many Yoasters contributed to WordPress over the years and we are very proud to have a dedicated team of contributors for it. Some of us have been contributing for over fifteen years and have been early adopters of the platform as users. And some of us started our path as users and contributors a bit later. But as Sergey likes to put it, we all work as one for the greater good.

If you want to read more about the history of WordPress, here are some resources for you:

Read on to see what the team has been up to this week and when we all started using WordPress.

This week I focused on WordPress 5.8 in combination with Gutenberg, as well as improving the code quality in the Gutenberg project. The current phase is one of the most stressful ones in the release process since the team needs to decide what is ready to be shipped, and then port things from Gutenberg to WP-Core. Follow-up fixed can be performed in later stages in the release process (during alpha/beta/RC), but this week was the last opportunity we had to include something in WordPress.

One of the missing blocks in WordPress 5.8 is the site-logo block. I focused on back-porting the block from Gutenberg to WP-Core. However, it was decided to switch from using theme-mods to settings. The decision improves the data structure for site-logos and they will no longer be dependent on the theme. As a result of this structural change, more time is needed in order to update the block. I submitted a pull request to update the block to the new structure in #32229 and once that gets merged we’ll be able to continue with porting the block to WP 5.8.

In addition to the site-logo block, I spend a big part of my time doing code reviews and making sure that things that have to be included in WordPress Core are properly vetted in Gutenberg first, prior to them getting ported to core.

I submitted a number of pull-requests, fixing linting errors in numerous packages: Fixed warnings in the edit-navigation package ( #32196 ), the edit-post package ( #32195 ), edit-widgets ( #32155 ), rich-text ( #32142 ), nux ( #32145 ), reusable-block ( #32141 ), edit-site ( #32156 ), core-data ( #32198 ), and finally the editor package ( #32153 ).

One of the long-standing issues in the editor is the fact that non-Latin characters get stripped from slugs. To fix that, I submitted a pull request in #32232 .

The first version of WordPress I used was 1.5 (Billy Strayhorn). I wanted to build a personal site, found WordPress, and then got hooked because of WordPress-MU (also known as WordPressμ, later merged in WP 3.0 as “multisite”).

This week I tested Gutenberg 10.7 RC1 and participated in bug scrubs for WordPress 5.8. I also spent time learning more about unit tests, and continued my JavaScript course.

I started updating the Theme Check plugin, which is used to check the code of themes that are added to the WordPress theme directory. The plan is to have one set of checks that runs on all types of themes. And another set of checks that are only used on themes with PHP templates.

I have participated in discussions about how to organize the developer documentation for block themes. To get started, I did a review of the current Theme Developer Handbook on WordPress.org. I’ve also listed pages and sections that need to be updated.

I don’t remember exactly what my first WordPress version was, maybe 2.5 or 2.6. WordPress was recommended to me by a friend but I was hesitant at first because I didn’t know PHP. I always wanted to self-host. And by then the technology behind the website had become more interesting than the blogging that got me there.

The past week was a “bits and bobs” kind of week for me. Not a clear focus but a lot of smaller items to take care of. Including speaking at a couple of events in Italy about diversity, WordPress and open source. I must confess, I always underestimate how long it takes me to prepare for these online. So I didn’t manage to do as much as I wanted from my ever-growing to-do list.

I mostly keep an eye out on Trac and Slack for the features and enhancements cut-off date. This is something that I proposed: definitely not the first one to do so, but in this specific iteration, I got the conversation re-started and set the dates. So any new enhancement and feature that will land on WordPress 5.8 have been merged and the focus for the next two weeks will be on defect work aka fixing old bugs.

The first version of WordPress I used was 2.9 Carmen. I was a .com user first and then moved to .org after winning a giveaway for an online class that taught me about self-hosting WordPress.

I continued to improve the Yoast e2e tests package . Among other things, I added the initial tests for the blocks of our plugin (FAQ, Breadcrumbs and How-to). Additionally, I’m working on fixing some compatibility issues on the package.

With the upcoming feature freeze of WordPress 5.8 and the betas period , I’ve slowed down a bit my work on e2e tests in Core, to do more triage, and bug fix on Gutenberg and WordPress Core.

The first time I used WordPress was in 2016. When in college, a teacher asked me to maintain my school’s website. I was already very interested in software programming, so he must have assumed I knew WordPress. That was with version 4.3.

The past week I was hard at work on an internal project. So, unfortunately, I could not dedicate many hours towards WordPress contribution.

This must have been around 2007, when I started a webcomic at the time I went to art school. The WordPress plugin ComicPress was the main way to make a webcomics website back then (if you wanted to host it yourself). That’s also when I first saw Yoast SEO, which had a lot of illustrations in it back then. So of course, I was keen to use it! Though I don’t think I understood anything about SEO back then and just installed it and forgot it ha!

For the last week, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8 , the next major release, as part of my duties as a Core Committer.

I made fourteen commits to WordPress core and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

The first version of WordPress I used was 1.5 “Strayhorn”. I discovered WordPress while building some websites for my university. After reading some blogs on personal development, I was wondering what CMS they used. It turned out to be WordPress, which quickly grabbed my attention due to its simplicity, extensibility, and amazing community.

Francesca used to be the lead of the WordPress core team working full time on the open-source project with some of the brightest minds in the industry. She is an accomplished educator, community leader, and public speaker.

We care about the protection of your data. Read our privacy policy.
