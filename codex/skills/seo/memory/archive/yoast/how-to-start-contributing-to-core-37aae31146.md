---
source: https://yoast.com/start-contributing-to-core/
title: How to start contributing to Core
scraped: 2026-03-23
published_on: 2021-03-17
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

# How to start contributing to Core

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/start-contributing-to-core/
Published: 2021-03-17
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
In this week's core blog post, Sergey tell you more about how you can contribute to WordPress Core. And, the team give their weekly update!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Last week, Francesca wrote about two Yoasters sharing their experience of being a part of the WordPress 5.7 release squad. She interviewed Tim Hengeveld as the Design focus lead and me, Sergey Biryukov , as the Core tech lead.

This week, I’d like to dive into the topic of contributing and answer some common questions from new core contributors. Read on to learn more about making WordPress !

If you’re thinking about contributing, I’d suggest checking out the FAQ for New Contributors in the Core team handbook. It’s a great place to start. There are also new contributors chats every 2nd and 4th Wednesday of the month, at 19:00 UTC in the WordPress Slack #core channel . Anyone is welcome to ask any questions on contributing. Hope to see you there!

The first 20-30 minutes are usually for questions about submitting pull requests or patches, working with Trac (the bug tracking system that WordPress uses), deciding which tickets to work on , or contributing to core in general.

The second section is for discussing specific core tickets any contributor may have questions on. For example, how to proceed with making some required changes, is the patch complete, does it need documentation or tests, what are the next steps, etc. If no tickets are brought up, the meeting facilitator performs a quick bug scrub to help move some tickets forward.

The meeting might end 10-15 minutes before the top of the hour to leave a little breathing room for the weekly core dev chat .

Sure! I think it’s actually the easiest way. Just make sure to add a Trac ticket URL you’ve been working on to your PR description, and it will be automatically linked to the ticket. See GitHub Pull Requests for Code Review for more details.

This handbook section suggests some ideas: Finding Bugs to Fix .

Generally, I would recommend looking at the list of “good first bugs” to get started or a similar list of “good first issues” for the Gutenberg project (WordPress block editor). If you’re on Twitter, you can also follow @GoodFirstBugs . These are well-contained tasks designed to help you get familiar with WordPress core code, processes, and contributing, and not send you down a rabbit hole.

If nothing catches your eye on that list, I suggest looking at the tickets for the next major release (currently WordPress 5.8), grouped by workflow. You can also filter tickets by keywords and view tickets marked as needs-patch, needs-testing, needs-design, or needs-design-feedback in the current milestone. Those are the ones that have a higher priority and need some attention.

Writing code is just one of many ways to contribute. It’s perfectly OK to start with testing the current beta version or nightly build, triaging tickets , adding missing docs, fixing a typo, and other non-code-related tasks.

Any significant contribution to a ticket deserves “props” on the commit message , which are later parsed for the release credits list and badges on WordPress.org profiles.

Some tickets can have multiple patches iterating on a solution or exploring different approaches. For tickets that already have a patch, testing an existing patch and giving feedback is a great way to move them forward.

The Triage Team aims to review all open tickets on Trac and move them closer to a resolution. This includes confirming reported bugs, reviewing and testing patches, providing feedback, pinging other contributors for information, making sure the workflow keywords are accurate, etc.

You can find more details on triaging tickets in these articles:

If you’re interested in joining the Triage team, please join the #core channel on WordPress Slack, ask for the next steps, and experienced contributors would be happy to onboard you.

You can just pick a ticket you’re interested in and start working. Before making significant time investments, though, it might be a good idea to ask for advice in the comments or in the #core channel on WordPress Slack.

You can ask someone to assign it to you, though it’s not strictly required. The Owner field can be left blank, even if there is a patch. Usually, the ticket owner is the person who oversees the ticket and moves it forward, though they do not necessarily have to work on the implementation. It can be a committer, component maintainer, or experienced contributor actively reviewing the patch. See Roles on Trac for more details. Generally, it is enough to just write in the ticket comments that you’ve started working on it.

Once you think the ticket is ready for review, you can ping the component maintainers . That said, not every component has an active maintainer, and not every maintainer might be readily available. So, sometimes it might be easier to bring up the ticket in the #core channel on WordPress Slack, and one of the active committers will take a look.

Keep an eye on the Upcoming WordPress Meetings page for the next new core contributor meeting, and add it to your calendar. They happen every 2nd and 4th Wednesday of the month, at 19:00 UTC. If you have any questions on contributing to core before that, just bring them up in the #core channel on WordPress Slack any time outside of any ongoing meeting or in the open floor section of the weekly dev chat, and someone should follow up.

My focus remains on tickets required for the FSE (Full Site Editing) MVP (minimum viable product). The goal is to merge FSE in WordPress 5.8 by the end of April, so there’s not much time, and everyone seems to be working towards that goal.

It’s great to see the community come together to accomplish that, but at the same time, stress is high, and so is a general feeling of worry. That feeling can mostly be attributed to developers not having a clear vision of an MVP. The Gutenberg contributors are confident about the timeline. The problem is that it’s not entirely clear what “getting there” means.

If you want to help and contribute to FSE and get it through the finish line faster, this ticket is a good place to start.

There is a sense of urgency to improve full site editing and the site editor to get it closer to a minimum viable product. Gutenberg is a very large project, and it can be difficult to prioritize among the 2.819 open issues.

I try to help out with triage, adding labels to issues, and reproducing problems. I am now a member of the Gutenberg core team, which means that I can commit changes to the plugin. So far, I have reviewed plenty of pull requests but only committed two.

We have now reached mid-March, and this was one of those weeks where I definitely felt like I have only been a “real” developer for three months. The block editor code is difficult to learn. It is not as easy as “just” learning React. And even if the documentation in the block editor handbook helps, the reason why different choices were made in the code is rarely documented.

Last week WordPress 5.7 was released, and I always underestimate how much time the final days keep me occupied! Not to mention the adrenaline rush of knowing that I am helping shipping code to 40% of the web. And usually, after all that excitement, I experience a day or two of tiredness.

With a new release out, I step into the dev-chat host’s role, while Core kicks off another release cycle and gets a new release coordinator. This means that on Wednesdays, I am busy after hours for the chat and the post-chat. Interesting conversations might spark from the chat, so they continue in the Core Slack channel or in direct messages. When Daylight Saving Timezone kicks in, chats are going to be 22:00 for folks in Central Europe. I love hosting them, and they are definitely worth a late night.

This week, I’m working on the retrospection for the project of restructuring the developer documentation of the block editor . I plan to publish a post about what worked for the project, what we learned, and the next steps.

In addition to that, I’ve started coordinating WordPress’s participation in the Google Season of Docs. This year will be the second year that WordPress has applied. So I’m working on the WordPress application , assembling a team, gathering ideas for the Season of Docs, etc.

Last week, my main focus was to continue reviewing tickets for the next major release of WordPress as part of my duties as a Core Committer. I made fifteen commits to WordPress Core, ran mission control for WordPress 5.7, led a meeting for new core contributors, and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

Now that WordPress 5.7 “Esperanza” is released, I’ve started reviewing enhancements and bug fixes for WordPress 5.8.

WordPress 5.7 was released last week! That wraps up my time as a release lead for design. It’s been an exciting opportunity that I talked about at length in last week’s interview . Now is a time for evaluation with the team to hopefully better prepare future candidates for the role. Then, it’s back to the regular process of looking at tickets that need designs!

Do you have any questions for our team? Maybe you want to join us for dev chats, and you are a bit worried about stepping into the Core channel? Let us know!

We would love to use this space for dialogue and not only for broadcast. Ask us anything!

WordPress Core Committer and plugin author, also working on Polyglots, Support, and Meta teams. Co-founder of Russian WP community.

We care about the protection of your data. Read our privacy policy.
