---
source: https://yoast.com/learning-teaching-and-contributing/
title: A week with us: Learning, teaching, and contributing
scraped: 2026-03-23
published_on: 2021-07-15
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

# A week with us: Learning, teaching, and contributing

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/learning-teaching-and-contributing/
Published: 2021-07-15
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week, the team continued preparing for the final WordPress 5.8 release on July 20th. Also, they spent some time on education. Find out more!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

This week, the team continued preparing for the final WordPress 5.8 release on July 20th. In addition, the team started looking into some early tasks for WordPress 5.9, worked on theme review tools, and spent some time on education. Curious to learn more? Keep reading!

A few days ago I created a dev-note in make.w.org . That post received a lot of comments, and one of those comments brought to my attention the fact that the block-styles API does not account for the recent improvements in block-stylesheets loading. To remedy that omission I created a new ticket and a patch in WP-Core ( #53616 ). The patch didn’t make it in WP 5.8 due to time constraints, but it is scoped for WP 5.9. Further improving block-styles loading, I added a new excerpt_allowed_wrapper_blocks filter in core ( #1479 ).

On the core themes front, I tested & reviewed patches related to an issue we’re currently having with dark mode and the Twenty twenty-one theme ( #53429 ).

Work on the “Update the updater” project continued this week as well, and we made significant progress. We added a method to clean up the rollbacks folder after a plugin has been successfully installed. We also completely refactored the code so it now runs more efficiently.

What’s more, in order to improve user experience and reduce the risk of failures, we added a new section in the Site Health screen. In that screen, we included checks to ensure the rollbacks folder can be accessed and the server has writing permissions to it.

One of the things I find inefficient in the WordPress editor is the way it handles the columns block. The current implementation uses some arbitrary breakpoints and CSS flexbox to accomplish layouts. I experimented a lot with CSS grid, only to come to the conclusion that using CSS flex was the right choice. Flex and grid are both amazing, but they have different applications. However, I still think we can improve the current implementation. To that end, I started experimenting with a way to stop relying on CSS media queries and looked for a way to automatically wrap columns when they no longer fit on one row, based on the user’s settings. A proof-of-concept implementation for this is currently being worked on in #33330 .

This week we also merged a patch in Gutenberg to add a new “separator” argument in the “post-terms” block. Though that block is not directly exposed, variations of it are used and available as the “post-categories” and “post-tags” blocks.

We have identified a lot of issues regarding child themes of a block-based theme, so I started working on solving these issues. This is still a work in progress, but if you’re curious to see what I’ve been working on, you can see it on #33445 .

Just like previous weeks, most of my time has been spent on QA and theme review tools. I have also continued my training via Yoast SE O academy. I haven’t planned any longer vacations this summer. Instead, I have taken a few Fridays off and my updates for these weeks may be a bit shorter.

I have not done any self-studies of Jest and Puppeteer this week. I plan to take the time next week to go through and learn from the tests that Justin has been working on. I have focused on regression testing of Duplicate Post and Yoast SEO, and testing with WordPress 5.8. The plugins have a short release schedule but I am happy with the pace and workload right now.

Work continues on the tools used for testing themes before adding them to the theme directory. Steve from the WordPress.org Meta team has tidied up our list of requirements. He has presented them in a table format that hopefully is easier to work with. Next, we are documenting which tool is currently used or can be used for which requirement. For example static code reviews or end-to-end tests. Theme authors are starting to engage more by asking questions and submitting code via pull requests, which is positive. During this week’s themes team meeting , there was a discussion about how we can prevent spam and keyword stuffing in the theme description. This will require some exploration, perhaps there are existing spam prevention tools we could use for identifying spam in this text. One thing that the themes team has left to do this week is to set the quarterly goals for Q3. I also submitted a small pull request to update the how-to guide for creating block themes: #33382 .

I have not contributed much lately but I am following Sergey’s and Ari’s work. On Thursday, I did some edge case testing of the plugin- and theme upgrade flows when the server has low disk space. I think that the messages that are displayed by WordPress when there is not enough disk space need to be improved, but it might be out of scope for the project.

This week, I continued my exploratory quest: how can our team bridge between the WordPress.org project and Yoast? I also learned new skills and actually contributed to WordPress!

In the team, we all have some level of knowledge of the Yoast products. We all have used the SEO plugin, more or less. However, we didn’t have much experience with the SEO Premium plugin, and near none with the other plugins .

Is it necessary to know our products to contribute to WordPress? Yes and no. But mostly yes. We are given immense freedom and trust by the company to focus on WordPress and I believe the minimum we can do is highlighting new features or bugs that might affect our products. In some cases, the same features/issues/bugs could affect other companies whose products are based on WordPress.org. This is the so-called extenders ecosystem , which is, after all the one that users interact with. WordPress can not be used without a theme, for example, and the majority of people also use a plugin or two (or sixty-four according to a friend of mine 🙀) to extend the core functionality.

By knowing our products, we can understand better how product-based companies interact with core and we can champion solutions that will benefit a large part of the industry. This is why we are working on the updater for example.

Our company has a staggering number of talented software developers. Do they all know WordPress like the palm of their hand? Of course not! And we are here to help.

Yoast championed the holistic approach to SEO years ago and I think the same should be used to software development: yes, it’s more difficult because you have to keep track of loads of moving parts. But once you get the hang of it, you kind of feel like Neo seeing the Matrix for the first time.

With these two goals in mind, I have started a conversation with our Engineering Manager, Irene Strikkers , about the coexistence of these entities. I will document it in this blog, hoping that it might help more companies that decide to sponsor contributors to WordPress.

I am dedicating a good chunk of time to learning this summer. This week, I completed the Google Analytics for Beginners course and I even got the certification to prove it!

I am also working through the SEO copywriting course from our Academy and learning some fascinating facts about how Google reads.

I also managed to squeeze in some proper contributing! I attended a test scrub, a test meeting, I hosted the weekly dev-chat and I had a long conversation with our friend Tonya Mork about QA and the upcoming release of PHP 8.1.

This week, I have a few days off. Also, I’m working on automated tests for an internal Yoast project until the end of August. So not much to update until then.

Last week I started looking into some early tickets for WordPress 5.9, as part of my duties as a Core Committer.

I made seventeen commits to WordPress core, mostly some cleanup for coding standards, documentation, and unit tests. I also triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

Together with Ari, I continued working on the Updater project to make updating plugins and themes more reliable. Currently, we’re testing an approach to keep a backup of an existing plugin or theme version before performing an update, and only removing the backup once the update is fully completed.

I also worked on modernizing the WordPress unit test suite by using more appropriate assertions and native PHPUnit functionality where possible. See tickets #53363 and #53491 for more details.

PHP 8.1 release is planned for November 25, 2021 . WordPress 5.9 is currently planned for December 2021 and should aim to support PHP 8.1 as much as possible.

I have created ticket #53635 to look into various compatibility fixes required for PHP 8.1 support.

WordPress Core Committer and plugin author, also working on Polyglots, Support, and Meta teams. Co-founder of Russian WP community.

We care about the protection of your data. Read our privacy policy.
