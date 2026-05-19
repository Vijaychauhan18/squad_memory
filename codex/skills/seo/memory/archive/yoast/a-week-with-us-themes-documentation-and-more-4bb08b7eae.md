---
source: https://yoast.com/themes-documentation-and-more/
title: A week with us: Themes, documentation and more!
scraped: 2026-03-23
published_on: 2021-05-06
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

# A week with us: Themes, documentation and more!

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/themes-documentation-and-more/
Published: 2021-05-06
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Find out what the WordPress core team at Yoast has been up to in this past week! We'll tell you about our work on themes, documentation and more!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

The WordPress core team at Yoast had another productive week! We’ve been working hard on improving themes and documentation and kept preparing the ground for the new WordPress release. There are also some other interesting initiatives and projects the team members are pushing forward full speed ahead. Curious to learn more? Read on!

This week was Greek/Orthodox Easter, so I took a couple of days to spend with family. It was a nice break, and recharging my batteries is always a good thing. I worked on a handful of improvements to the WordPress editor and did lots of code reviews.

Block themes handle comments using a comment-form block. That block contains a form, and a submit button, but one of the issues we had was inconsistent styling. When a theme author styles buttons for their theme, all buttons should follow their style. This was not the case with the comment-form button, so I submitted a pull request to fix that inconsistency ( #31338 ). This PR adds the button block’s classes to the comment-form button and removes the hardcoded styles. As a result, form buttons can now inherit styles from the button block.

I’ve always been a vocal advocate of using relative font sizes ( em and rem units) over absolute units (px). Pixels served us well for many years. However, we now live in a world where people can consume content on devices ranging from a 2-inch smartwatch to a 70-inch smart-TV. Pixels don’t have the same value as they did in the old days. To fix that, I submitted a pull request which was merged, changing the behavior of font-size pickers ( #31314 ). Designers are no longer forced to use pixels for font sizes and can use other units.

I continued working on the pull request to auto-generate anchors for all headings ( #30825 ). There were complications with the history feature (undo/redo) in the editor, so the PR has not been merged yet. When the user changes the content of a heading, the anchors get auto-updated. However, that anchor generation was creating a new step in the undo/redo history, breaking the expected behavior. I fixed the issue and refactored the implementation, so history now works as expected. Having anchors for all headings will be a huge improvement, so I hope we can merge that feature this week.

With WordPress 5.8 coming soon, we need to stabilize some features. One of these is the theme.json file for themes. Until recently, that was called experimental-theme.json. So, a pull-request was merged to rename the file – while at the same time making sure that pre-existing block themes using the previous filename don’t break ( #29981 ).

Every week, I try to join at least one testing or triage session. The so-called “APAC Core Triage Sessions” on Tuesdays begin at seven o’clock in the morning, my local time, and are a good way to start the day. They are a great reminder of how expansive WordPress is. They also help me not to get stuck in my little bubble where I only focus on a few things. I get to hear about problems that users are experiencing, look at code that I might not have worked with before, and learn from others.

I continued updating the tutorial on how to create a block theme. I always have to remind myself not to write at too much length. However, it is not easy to know how much background information or details to include. Of course, that’s because the experience and knowledge of the reader will vary. I also want to set aside some time to re-read the documentation team’s style guide . I hope I’ll pick up some tips for improvements.

This week I continued working on the pull requests I started last week. They are: a letter-spacing control, a link toggle option for the site logo block, and some changes to the post content block. I had a hiccup with the letter-spacing control that turned out to be a problem with my local developing environment. I managed to ping the entire core editor team to review the problem. But, I was told I am not the first person to make that mistake (phew). I have also tested the next format for the experimental-theme.json file (which is a configuration file used in full site editing). And, I spent time troubleshooting how page templates are loaded.

I submitted one theme-related pull request for WordPress core, which was to remove the link to the featured tab from the “Add themes” view in the WordPress admin area ( #49487 ). The themes displayed in this tab are random, and they have not been selected to be featured to new WordPress users.The tab had already been removed from the theme directory on the WordPress.org website. With this pull request, the options in the admin area and the website will match again.

It was a busy, busy week. And finally, my energy level is more or less back to normal! I love when things that have been stalling for a while get a sudden push forward and see the light of day. The past seven days have seen the culmination of several open issues in my ever-growing to-do list. Let me tell you all about them.

Months ago – ok, almost half a year ago – we had an internal discussion about the various WordPress updater classes. We talked about how some are in better shape than others and what could be done to improve them overall. We came up with the Update the Updater initiative, but I didn’t manage to follow through with it. With the kick-off of the 5.8 release, which doesn’t see me directly involved, I finally have more time to dedicate to this.

Thanks to Sergey, there is a list of issues that are related to the topic. So, I was able to post a recap for everyone that wants to be part of the initiative. Together with the maintainers of the Upgrade/Install component , we are finally diving into it! On Tuesday, May 4th, 2021, the first meeting was held, and we already have tasks lined up.

I care deeply about this project. I recently read a book by Dr. Brené Brown, Dare to Lead, where she lays out a very simple and powerful truth.

The goal of the team handbook is to clarify some topics that are particularly relevant to us since we will always be remote. I am trying to cover as much as possible. That includes communication guidelines and advice on communication online in an open-source project. Writing about these topics means I have to first do in-depth research and distill the information, so it won’t be overwhelming.

I have one more page to go – it takes me an incredible amount of time to edit because I am very verbose. And then v.1 of our handbook is ready!

At the beginning of March, WordPress 5.7 was released, and the presence of women, blacks, indigenous, people of color (BIPOC), and non-binary people was quite high again. And yet, all the publications that talk about diversity, equity, and inclusion (DE&I) never write about WordPress and its efforts in this field. So I took to LinkedIn and shared some frustration about it. I also sent request for help: connect me with people that want to have their story heard. Surprisingly – usually don’t get much traction on social media – I got plenty of replies, and this last week I did two more interviews about it. They will be in Italian, but I will report back if I’ll ever manage to get something published in English.

It is always surprising to me that tech publications outside of the WordPress bubble don’t talk more about the platform that powers over 41% of the web. This is especially because this is not a closed-source project where users get to see what has changed only after it has changed. Everyone can see what is going on in the project, what changes are coming, and I hope more end-users will be curious about this piece of software. After all, as Josepha put it:

The best outcomes are the result of collaboration with the people who use WordPress the most.

I continued to do the triage of Gutenberg issues and WordPress Core tickets on Trac. For WordPress, I particularly triaged the Bundled Theme component. Here’s the list of tickets I went through.

On GitHub, I’ve triaged CSS styling issues and also created a couple of PRs ( 31408 and 1220 ).

I also continued to work on the WordPress Test team . Among other things, I gave feedback on Tonya ‘s proposal to reboot the team. I also participated in the first bi-weekly triage meeting of the test team.

I’m also still working on the e2e tests in WordPress Core. I was able to give feedback on the first e2e test that is still in the pull request stage. And I myself wrote my first e2e test in Core which I will continue to work on, and create new ones.

For Yoast, I’ve released a package that lays the groundwork for implementing e2e tests in our plugin, which I will also continue to iterate on.

Finally, like every week, I paired with my colleagues Josee and Dennis to work on our developer documentation portal at Yoast.

For the last week, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8 , the next major release, as part of my duties as a Core Committer.

I made eight commits to WordPress core, led a meeting for new core contributors, and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

Work moves ahead on the design issues for WordPress 5.8. It’s tough to keep up with everything that is happening. So many people are doing great work on lots of features. But we’re still missing a design release lead! In the design team, we’re working on a plan to chaperone some people towards this role to have more people to handle releases. There are many great designers active in WordPress. Now our challenge is to support them in taking the next step and leading.

Tim is our UX designer and one of the illustrators at Yoast. Using his prior knowledge as a game developer, he is focused on improving the experience and flow of our products, and does his best to make it look good while he’s at it.

We care about the protection of your data. Read our privacy policy.
