---
source: https://yoast.com/working-on-wp-5-8-gutenberg/
title: A week with us: Working on WordPress 5.8 and Gutenberg
scraped: 2026-03-23
published_on: 2021-06-17
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

# A week with us: Working on WordPress 5.8 and Gutenberg

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/working-on-wp-5-8-gutenberg/
Published: 2021-06-17
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week, the WordPress core team worked on bug-hunting and -fixing for WordPress 5.8, and more! Curious? Read this article to learn more!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

This was a week full of developments! WordPress 5.8-beta2 was released on June 15, so we are now in a bug-hunting and bug-fixing stage. We are organizing another contributor day at Yoast, where all of our colleagues come together to improve WordPress. Our team has been hard at work, and you can read all about our work below.

Like last week, I continued working on the WordPress editor (Gutenberg) and WordPress Core for the upcoming 5.8 release. I focused on bug fixes and code-quality improvements. I also did many code reviews on code pushed by other contributors to ensure we move the project forward.

I merged an improvement I submitted last week, enhancing the way we define CSS Units in editor controls ( #32482 ). This change increases consistency across all our controls and improves code quality by reducing the required code.

I continued working on allowing multiple stylesheets per block ( #32510 ). Once this gets merged, theme authors and plugin developers will have more tools in their arsenal to style blocks sustainably and efficiently.

Since we need to keep WordPress and Gutenberg synchronized, we occasionally need to backport things from one to the other. In #32611 , I backported a function from WordPress Core to Gutenberg, easing future releases and merges.

We merged #31239 to improve the performance and future sustainability of block styles. Instead of loading a big stylesheet containing styles for all blocks, opinionated block styles will only be added when the block gets rendered on the page.

Continuing with performance improvements, an issue was reported for the latest posts block. When there are many authors on a site, the block was getting a list of all authors to display in a dropdown. This process causes a significant load in databases with thousands of users registered, so #32620 will fix that issue when merged.

Allowing site owners to design their sites more efficiently is of the utmost importance in this Gutenberg phase. Unfortunately, it was not possible to use decimals when adding paddings and margins to blocks until now. #32692 fixes that issue.

I fixed a bug reported a few days ago with the automatic skip-links that get added in block templates. The fix was committed to WordPress Core, and also backported to Gutenberg ( #32451 ).

An issue was reported in WordPress for themes trying to style a block that doesn’t have styles by default. Since I fixed that same issue in Gutenberg a few weeks ago, I backported that fix to WordPress in #1370 .

One of the projects our team is currently working on is improving the WordPress Updater for plugins and themes. This week we had a multi-hour collaborative session in which we all examined the WordPress code, went through tickets, and started coming up with a plan on how to move forward and what needs improving.

This week I fixed a merge conflict and followed up on three pull requests I was working on a while back. One is a link toggle for the new Site title block. I did keyboard testing of changes made to the template editor, #32642 , and opened an issue about the template creation and selection flow when the template is missing a name ( #32643 ).

I am making progress on listing all requirements from the test tools in one public place so that everyone can get a better overview. I found more undocumented checks in than I had predicted. The following steps are to decide if the checks should be kept at this severity level and document them. Theme Check : A user reported an issue in the plugin support forum that I plan to work on, and there are pull requests waiting for review.

I spend half of my time with the QA team at Yoast. To help me learn, the team has prepared practice tasks in Jira, which is a system that is new to me. So this week, I have continued to set up tools like third-party services and plugins I need for testing. In addition, I took a short course about Jira. And to become more familiar with the plugin features, I took classes from the Yoast SEO academy.

I have tested the changes in Yoast SEO 16.5 , which was released on Tuesday, and found a minor bug with the onboarding of new users that activate both Yoast SEO and Elementor.

Since last Friday, I focused my efforts on the WordPress test team.

We are currently at the stage of setting up end-to-end (e2e) tests in WordPress Core. Recently, a new e2e test has been pushed on the WordPress repo, the dashboard test . So, I took the opportunity to refactor the code and the pull requests of the e2e tests for categories and users . The goal was to make the tests more efficient and to make them follow the standards.

I’ve also been working on triaging the tickets that need to be tested on Core Trac. On top of that, I took part in the team’s test scrubs, where we tested the widget editor in WordPress 5.8 . We were able to detect things that don’t work and report some bugs like this one .

For the last week, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8 , the next major release, as part of my duties as a Core Committer. I made eight commits to WordPress core and triaged new tickets incoming into Trac (the bug tracking system WordPress uses).

One notable change was about the Requires PHP and Requires at least plugin headers, which could previously be specified either in the plugin’s main PHP file or in readme.txt as a fallback. This has now changed for WordPress 5.8; only placing them in the plugin’s main PHP file will be supported from now on. The same goes for themes, the Requires PHP and Requires at least headers should be placed in the theme’s style.css file instead of readme.txt .

The reason for this change is that any data in readme.txt is meant for the Plugin or Theme Directory only and not for WordPress core. The core should retrieve all the necessary data from the plugin’s main PHP file or the theme’s style.css file instead. See changeset [51092] and ticket #48520 for more details.

At Yoast, everyone is encouraged to grow both personally and professionally. Last week, I took two courses: Pomodoro® Training Part 01 and New Adventures In Front-End, 2021 Edition.

This is a training by Francesco Cirillo, the creator of the Pomodoro technique. He was very engaging and managed to keep my attention for the whole time. It turned out there is more to the technique than just setting a timer: it now makes more sense to me.

Following the technique is hard, it requires discipline and quite a shift in how I think about time, days, plans, goals, and even myself as a person. However, since the creator is a developer, a lot of the concepts he mentions resonate with me, especially incremental improvements.

I can see this fitting well with Getting Things Done by David Allen, parts of which I also apply in my daily work. Fun fact: I was a co-editor of the Russian translation of Getting Things Done («Как привести дела в порядок») in its first edition back in 2007.

This is a workshop by Vitaly Friedman, co-founder of Smashing Magazine and front-end/UX consultant. Front-end development seems to get more and more complicated, and this was a bit outside of my comfort zone, as I don’t deal with the front end that often, but I immediately knew this could be helpful in my future work on WordPress.

The workshop focuses on building fast and scalable experiences. I’m currently on day two of a five-day schedule, and these are just some of the things that I’ve learned:

Ari is a member of the WordPress core team where he gets to work full time on the open-source project with some of the brightest minds in the industry. He is an accomplished contributor with a focus on sustainability & accessibility.

We care about the protection of your data. Read our privacy policy.
