---
source: https://yoast.com/working-on-wordpress-and-gutenberg/
title: A week with us: Working on WordPress & Gutenberg
scraped: 2026-03-23
published_on: 2021-04-29
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

# A week with us: Working on WordPress & Gutenberg

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/working-on-wordpress-and-gutenberg/
Published: 2021-04-29
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week, our WordPress core team has been working on improving WordPress and Gutenberg. Read on to find out what they've been working on!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

This week, our WordPress core team at Yoast worked on improving the code quality of WordPress and Gutenberg, as well as performance, theme tools, documentation, and design, among other things. Like we do every week, we would like to give you an update on what everyone one of us has been working on. Read on for more details!

I started working on a new pull request to improve performance for block themes. It continues to build on the efforts I started last year by splitting block styles and conditionally load them when a block gets rendered ( #25220 ), as well as inlining small block styles ( #28358 ). This time the focus was on splitting the theme.css file and conditionally load parts of it when needed ( #31239 ). In the process of doing that, I found – and fixed – another small bug in our styles inlining method ( #31268 ).

The code we write in WordPress gets shipped to millions of websites, so it’s important we keep the codebase clean, well-documented and maintainable. This week there were a series of pull requests to improve code quality:

I haven’t worked a full week this time. But I have helped out by reviewing updates to the documentation for themes, custom block styles and block patterns in the block editor handbook. The information about block styles is being moved to its own page and the theme section is being re-organized. I’ve also finally started updating the tutorial for how to create block themes. It will need iterations and I don’t expect it to be ready this week or the next.

I have worked on creating a new letter-spacing control. I’ve never created a new control (or component) before so it was challenging and a lot of fun. I got to work with code in Gutenberg that I have not touched before. I hope that it will soon be reviewed so that I can learn from the feedback (#3111 8 ) .

While the site title and tagline blocks are waiting for the letter-spacing control, I started working on a link toggle option for the custom logo block. The pull request is not complete yet and needs a few changes (#31162) . I still have three pull requests for the post content and post excerpt blocks that are awaiting reviews.

My updates are never as exciting as the other team members. And that’s fine. As a team lead, I believe my role is to facilitate and coach my team to success. I spend time contributing to WordPress too and I’m very comfortable being behind the scene so other people can shine :)

Our internal handbook is almost done! Since none of us is a native English speaker, I thought it would be useful to have a glossary section with some acronyms and jargon. For example, do you know what rubber-ducking is? Do you know what “FWIW” stands for? I expect the page to grow over time as we encounter more obscure terms as we go!

WordPress 5.8 is one month away from feature freeze time. It’s time to put the band together. I published a call for volunteers and the post received a good number of applications. The next step is forming the group, making sure that everyone has the information they need, and seeing WordPress coming together again. There is a new public channel to coordinate the release in the WordPress.org Slack channel. You are invited to join so you can see observe how the software gets done.

I have been battling with my WordPress-develop local environment for a few days now. I have to say it’s very frustrating. Whilst I am not a backend developer, I do have a long experience with HTML and CSS. I am willing and able to contribute with some code and testing, but alas, I need Docker or VVV to do so. I have been thinking about this while nuking everything, reinstalling and trying to debug the issue. And I wonder how many people out there are able to contribute and are put off by the setup?

I keep regularly triaging issues on Gutenberg and WordPress. For Gutenberg, I mainly did pull request reviews on adding and editing pages on the developer documentation ( 31060 , 31055 , 31167 ).

I also participated in the early bug scrub for WordPress 5.8 during which I tested patches on a number of tickets on Trac. See this post for more details on the tickets.

There was also an interesting discussion this week with the documentation team about our involvement in the WordPress releases and the various documentation tasks that are related to them. Having been a member of release squads several times as a documentation lead, it was important for me to bring my point of view on this. The summary of the meeting hasn’t been published yet, but you can read the backlog on the Slack Make here .

For the last week, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8 , the next major release, as part of my duties as a Core Committer.

I’ve continued chipping away at some long-standing coding standards issues in WordPress core with the ultimate goal for all of core code to comply with its own coding standards, WPCS . I made eight commits to WordPress core and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

With WordPress 5.8 gleaming on the horizon, I’m turning my focus to the design issues that need to be solved. Full Site Editing is planned to ship with 5.8, so there’s plenty of work that can be done to make it the best it can be at launch. The design team is spread thin, so if you’re interested in design, anything you can do to help out would be appreciated. Take a look at what to expect from full si t e editing , how to contribute to the design team , or if you’re feeling ambitious, read my guide on leading a design release.

WordPress Core Committer and plugin author, also working on Polyglots, Support, and Meta teams. Co-founder of Russian WP community.

We care about the protection of your data. Read our privacy policy.
