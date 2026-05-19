---
source: https://yoast.com/diversity-performance-improvements-and-more/
title: A week with us: Yoast Diversity fund, performance improvements, and more!
scraped: 2026-03-23
published_on: 2021-05-14
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

# A week with us: Yoast Diversity fund, performance improvements, and more!

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/diversity-performance-improvements-and-more/
Published: 2021-05-14
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Find out what the WordPress core team has been doing this week at Yoast. We're talking about performance improvements, diversity and more!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

On May 5th, we re-launched the Yoast Diversity fund . Started in 2018 as a way to increase the diversity of speaker line-ups at tech conferences, it pivoted this year to reflect the changes in the new COVID reality. Are you a self-sponsored contributor to the project? or do you contribute to its outreach around the world (by teaching classes, or speaking at online conferences about it)? You have time to apply for a grant until May 31st.

Over the course of the past 9 months, we pushed a lot of commits in the Gutenberg project with the goal of improving WordPress environmental sustainability and overall performance. All these changes lived in the Gutenberg plugin until now and were only available to a scarce few. With WordPress 5.8 coming soon, we wanted these to be available to everyone. This week I focused on back-porting all these changes to WordPress Core. I submitted and merged a patch for tickets #50328 and #52620 .

This is a huge improvement for the WordPress ecosystem, and we’re hoping theme authors and site owners will soon start taking advantage of these optimizations. With these new changes, a site can now only load styles for blocks rendered on a page. The previous behavior was to always print these styles regardless of whether a block exists on a page or not – resulting in extra data transferred on each page-load. With this new patch merged, small stylesheets can now also be inlined. This will further reduce requests from the browser and improve the performance of all WordPress sites.

I dedicated most of this week to WordPress Core and back-porting things we need for v5.8, so I was not as active in contributing to Gutenberg.

This week I have worked on updating the tutorial for how to create a block theme, and while doing this I created a very basic example theme and also found a few bugs. I have reviewed quite a few pull requests related to the new post blocks that will be included in WordPress 5.8. Some are temporary solutions, like this pull request to update the CSS for the comments block: #30382, or bugfixes like removing a duplicate block support from the site logo block: #31544 . I also briefly looked into how to split the post author block into multiple blocks so that theme authors can create more flexible designs, but I have put this on hold until there is more feedback on the issue .

Version 10.6 of Gutenberg is released this week, and the TT1 blocks theme needs to be updated so that a new version can be published in the theme directory. The contributors are still working on converting styles from Twenty Twenty-One to global styles and theme.json.

This Friday, May 14, there will be a hallway hangout about “universal themes” — the concept of themes that can work either with the customizer or template editing.

I often say that our team is a great representation for diversity:

We are committed to providing a friendly, safe and welcoming environment for all, regardless of gender, sexual orientation, disability, ethnicity, religion, age, caste, social class, preferred operating system, programming language, or text editor, among other identifying characteristics.

I subscribe to Chimamanda Ngozi Adichie’s call to action: we should all be feminists . And we shouldn’t stop there. Diversty of any kind is valuable because it brings, well, diverse experiences and points of view. I invite you to check our “ Gender, stereotypes and prejudice; a sociological exploration ” story to learn more about the topic.

After you are done with that — watch the videos as well! — I ask you to think about “How could you add diversity to the WordPress project?” and apply for the fund. And if you have questions about it, please ping me or Taco on Twitter, or in the WP.org Slack. (He is @tacoverdo and I am @francina). You can also catch the recording of the podcast we recorded yesterday for the Torque Social Hour .

So this is what I have been doing this week: promoting the initiative everywhere I can and reaching out to people that I know are doing good things in the WordPress space to invite them to apply for the fund. Bonus points! You’ll get to write on this blog and get to work with my team, who are simply amazing, besides being diverse 😉

My work routine is pretty much set for the next few months. On one hand I’m working on the implementation of e2e tests in WordPress Core, and on the other hand I’m continuing to review the Gutenberg documentation pull requests. All this is interspersed with my regular activities at Yoast, mainly the maintenance of our developer platform, and the e2e testing implementation of our plugins.

In the last few days, I started implementing e2e tests in WordPress Core. First, I created the tests for the Core categories here . I am currently working on improving these tests, as well as writing new ones for Core users .

For most of the last week, I was on a holiday. While I enjoyed my time off, since WordPress is not only my job, but also one of my hobbies, I still worked on some tickets 🙂

I made seventeen commits to WordPress Core and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

Last week I was occupied with supporting one of our internal teams on a new project, so my WordPress contributions were limited to responding to some issues.

Ari is a member of the WordPress core team where he gets to work full time on the open-source project with some of the brightest minds in the industry. He is an accomplished contributor with a focus on sustainability & accessibility.

We care about the protection of your data. Read our privacy policy.
