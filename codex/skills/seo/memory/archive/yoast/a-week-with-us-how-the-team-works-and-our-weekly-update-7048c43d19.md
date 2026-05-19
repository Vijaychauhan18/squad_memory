---
source: https://yoast.com/how-the-team-works-and-weekly-update/
title: A week with us: How the team works and our weekly update
scraped: 2026-03-23
published_on: 2021-02-24
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

# A week with us: How the team works and our weekly update

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/how-the-team-works-and-weekly-update/
Published: 2021-02-24
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week, Justin shows us how the WordPress Core team works and stays in touch with each other. Plus, an update from every team member!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Welcome back to our weekly post. Today, I want to share how the WordPress Core team at Yoast works. If you don’t know the team yet, that’s okay, we have a post on who we are and what we do that you can check out to get to know us!

In this post, I’m going to talk about the different aspects of how we work, how we make decisions, how we communicate, and everything else that goes on in our WordPress Core team at Yoast.

Our main means of communication is our corporate Slack, which we use to communicate with everyone who works at Yoast. There are different channels for the different teams at Yoast, so naturally, we have our own one too.

We also have an ongoing Zoom meeting where everyone from our team can join in when they want, and work while chatting with colleagues. It’s really a great way to stay connected, while we’re all working remotely. We also send direct messages to each other to discuss more personal things, or to coordinate activities before presenting them to the team or to everyone working at the company.

Every morning, we say hello to each other in our team channel, we share the latest updates on what we’re working on, and how we’re doing. We also share with the rest of the team if there are any blockers regarding our work.

Blockers can be all sorts of things: a pull request that is not quickly reviewed, difficult collaboration timezones, an internet cut, even cold weather… You see, it can be absolutely anything. The idea is to share this with others so that if necessary, a team member or a company member can help unblock the issue that you’re facing.

These standups were introduced by our team lead, Francesca, and it’s a real delight and a great opportunity to find out how everyone in the team is doing on a daily basis. The idea is based on this advice from Erin Casali .

Once a week we have a team meeting, where we discuss the latest updates on our work, and also the main direction that the team’s efforts will take. It’s also the perfect opportunity to see Sergey’s cats, Francesca’s new hat and her funny remote meeting cards .

Sometimes we have Omar at these meetings to discuss WordPress software architecture issues, or Joost to talk about advanced SEO or to share good news (yes Joost often shares good news when he comes to one of our meetings).

Once a week we also have a 1&1 meeting with Francesca to talk more about our individual work, our personal development plan, the direction we want to give to our work, projects of contribution to WordPress that we are particularly interested in or anything else we want to talk about. Personally, these meetings are my favorite and I look forward to them every week.

Twice a month, we meet with Josepha Haden , the executive director of the WordPress project, and with other teams of sponsored WordPress contributors from other companies. These are high-level meetings to synchronize our contribution efforts, get updates on major WordPress projects, and share blockers that are relevant to mention and discuss with Josepha.

I hope I’ve given you an insight into how our WordPress Core team works. Of course, there are lots of other fun things that I haven’t mentioned yet. For example, we sometimes have spontaneous meetings with two or more colleagues for one-time things or when it’s necessary.

Keep an eye on the blog for more updates on the work of our team. Bye, and see you all next week.

Last week was all about two very important tasks for WordPress Core: helping the current release squad with landing WordPress 5.7 safely to Release Candidate 1 and checking with component maintainers about their status within the project. Are they active? Do they need a break? Do they need support? And what they are planning for WordPress 5.8.

The WordPress 5.7 team is doing a smashing job! They are very efficient and focused, so my help isn’t required that often. In fact, I don’t think it’s required at all. But I love being able to contribute to WordPress, so I find tasks here and there for myself ;-)

In terms of schedule, scope, and squad, WordPress 5.8 is not confirmed yet. So my tasks there are mostly exploratory: What can we do? What resources do we have? Who are the people that can support the next WordPress release? After I gather as much information as possible, I forward it to Josepha so she can direct us.

Last week, my main focus was to continue reviewing tickets for the upcoming major release of WordPress , as part of my duties as the Core Tech lead. I made twenty-four commits to WordPress Core, ran mission control for WordPress 5.7 Beta 3, and triaged new tickets coming into Trac (the bug tracking system that WordPress uses).

Now that the first release candidate of 5.7 has been released, I’ll start reviewing enhancements and bug fixes for WordPress 5.8.

The past week has been all about documenting my increased involvement in the WordPress design team. I wrote a lengthy Handbook page about becoming, being and surviving being a WordPress design release lead (although I haven’t reached the survivor phase yet haha). And I’m working on a retrospective post for the design team blog about my experience with WordPress 5.7 development. What went well, what could improve, and what the 5.8 lead could pick up. These writings also led me to start writing a doc for other people at Yoast who may be interested in contributing to design but don’t know how or lack context. With that I hope to share the knowledge I have built up over the years so others can do what I do too.

The work I’ve been doing for the past couple of months has paid off and Full Site Editing stylesheets for blocks will get loaded a lot more efficiently from now on. The related pull-request was merged in Gutenberg so I’m super excited for the future of WordPress and our continued sustainability efforts.

I’ve began working on things we need to focus on in order to get a Minimum Viable Product (MVP) of Full-Site-Editing (FSE) in WordPress 5.8, including changes that will need to happen in the templating system . We’ll also need to focus on some minimum styles for FSE templates for layouts and alignments so themes can opt-in to automatic styles.

This past week I finally completed two important web accessibility courses. I am looking at the different ways that I can continue learning, practicing and contributing to the WordPress accessibility team. The accessibility team provides accessibility expertise and resources, and they also test bugs and new features.

WCAG (short for Web Content Accessibility Guidelines), is an international standard for how to make web content more accessible. All new or updated code released in WordPress must conform with the WCAG 2.1 guidelines at level AA, and this is a big task. One thing that the team is working on right now is improving the WordPress accessibility coding standards and the documentation about WCAG. You can learn more about the accessibility team on their website. I have been splitting my time between WordPress version 5.7 and full site editing. Now that the first release candidate of 5.7 has been released, I plan to focus on the MVP of full site editing, including documentation. The WordPress documentation team is kicking off the work on the full site editing end-user documentation with two sprints on the 25th and 26th of February.

The work that I was doing on the WordPress Test Instructions document is complete. And I was able to present it at last week’s devchat. Now the next step is to use this document as the basis for implementing e2e testing in Core. This is an important project, so I hope that interested contributors will soon take the lead on it.

I am also continuing my work on the restructuring of the Gutenberg developer documentation, which is progressing quite well.

Justin is a member of the WordPress Core team at Yoast. His work focuses on improving the documentation systems for different parts of WordPress as well as creating a better onboarding experience for new WordPress contributors.

We care about the protection of your data. Read our privacy policy.
