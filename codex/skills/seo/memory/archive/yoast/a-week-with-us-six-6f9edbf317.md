---
source: https://yoast.com/six-month-anniversary-of-the-team/
title: A week with us: Six
scraped: 2026-03-23
published_on: 2021-04-22
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

# A week with us: Six

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/six-month-anniversary-of-the-team/
Published: 2021-04-22
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week marked our team's six-month anniversary! Read about that and what the team has been up to in this post.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

It’s been over six months now since the WordPress core team at Yoast was formed, so it’s our six-month anniversary! We’re learning to work as a team, and we’re constantly refining our working and communication methods.

On April 15, 2021, we had an internal hackathon, and we discussed this blog, amongst other things. We are testing a new format: our weekly updates will be more detailed to provide as much information and context as possible. All of us have topics that are dear to us, and we want to deep-dive into them. So, stay tuned for more focused articles!

Parts of full site editing are coming to WordPress 5.8. Therefore, there are many things we have to take care of before that release. With that in mind, I worked on improving blocks and design tools available both to theme authors and WordPress users.

As part of the Gutenberg core team, it’s our responsibility to review code on a daily basis, give feedback and ensure that the code we ship is stable. So, a big part of my daily routine is testing and reviewing code written by others.

Debugging reported issues and finding solutions to our users’ problems is an important part of our job description. This week, one of the things that caught my eye was the fact that users were unable to use any non-pixel units in padding controls. Padding controls are a relatively new addition to the group block. Also, they are an essential tool to theme authors using block templates. I debugged the issue and identified the problem. After bringing it up in the weekly core editor meeting on Slack, @jorgefilipecosta created a pull request. And, after reviewing it, I merged it earlier today: #31057 .

There is also a significant desire to allow using non-pixel values for font sizes documented in multiple GitHub tickets. I gave feedback on some of them. In addition, I closed an older pull request that attempted that but was no longer valid (#25825). Also, I created a new issue in the G2 repository to discuss how to accomplish that ( #300 ).

On the sustainability front, I discussed a core ticket for enqueuing only assets for rendered blocks ( #50328 ) with contributors on Slack. Also, I gave feedback on a ticket for spitting block styles in classic themes ( #31013 ). That last feedback will result in a new pull request in the next few days. This will make it easier for classic themes to opt-in to more efficient block-styles loading.

Moreover, the Q theme was updated on GitHub. Since this was the first block theme to be released, many developers use it to debug and contribute to Gutenberg. Therefore, it’s important I keep it up to date with all the Gutenberg improvements and structural changes. It’s also a good way for me to better understand what changed, what has the potential to break, and what theme authors will have to do to keep their products updated and working properly.

WordCamp Greece 2021 was on April 16, 17 & 18. It was one of the most well-organized online WordCamps I’ve attended during this last year and a pleasant surprise. I attended a few interesting talks, and Yoast was present in multiple ways. Our CEO, Marieke van de Rakt, held a talk about “How to improve the SEO fitness of your site”. This was very informative and fun! In case you missed the talks, they will soon be available on WordPress.tv , as well as on the Greek WordPress Community YouTube channel .

On Saturday, I was in the Yoast booth with my colleagues Samah and Isidoros. We had some fun conversations and enjoyed the day.

Sunday was contributor day, so of course, I had to be there. I answered questions that contributors may have had regarding Gutenberg, met new people from the Greek community, and had long discussions. It reminded me of the things that make WordCamps great: meeting new people you can connect with. I can’t wait for the next one!

Part of my daily routine is reading new notifications from the Gutenberg GitHub repository . Since WordPress is a global project, there is movement in it 24/7. I usually start by following up on questions and answers and triaging issues that have no labels. This can be time-consuming but necessary to maintain an overview of the changes that people propose and make to Gutenberg.

With help from Sergey and Ari, I updated a pull request for a new post comment link block. This was merged a few days later. The new block is intended for full site editing and displays the number of comments a post or page has and links to the comment area. It uses code from the post comment count block . It doesn’t have any advanced options yet, but the plan is to allow users to customize their link text and not stop at showing the number of comments.

Like all new blocks, it also needs an icon specifically made for the block. I have not created any SVG icons for Gutenberg yet, and I trust the designers involved with the project to come up with something cool and easy to understand.

I spent some time testing pull requests related to full site editing:

I worked on small improvements for the post excerpt block and the post content block. Two of the pull requests were to ensure that the blocks do not output empty HTML tags when the block is empty. The second pull request was to update the placeholder for the read more text in the post excerpt block.

As a result of the latest Yoast contributor day, I opened over fifteen issues, including one about gradient support for paragraph blocks: #30982 . ;-)

It’s not just code around Gutenberg! I caught up with the G2 component system and its implementation .

I have found it a bit difficult to prioritize which full site editing tickets to work on because many of the remaining issues require advanced coding solutions and, not least, lengthy discussions until we can arrive at a decision. So, I posted some questions about the status of the items planned for 5.8 in the official WordPress slack channel and what to prioritize. Héctor Prieto later published a post about the next steps on WordPress.org.

As part of my tasks as Theme Team representative, I also wrote a draft post for the team blog.

In the past two weeks, the team had lots of meetings and two contributor days, one internal and one external. When this happens, I miss focusing on the accessibility issues, but I plan to get back to those soon. I did manage to test an accessibility-related pull request for the save panel .

My time is divided between managing the team and contributing to WordPress core myself. The past month I wasn’t able to work full time because of COVID, but it seems like I am mostly back in the game.

April 1st (no joke!) marked our six-month anniversary as the Yoast WordPress core team. Sergey has been working here for over five years, and Ari and Justin joined in August, but we became a team on October 1st when I joined as the team lead. A few days after, Carolina joined us, and since then, we have been working on building the team and building WordPress.

We are the first completely remote team, so, together with the board and HR, we are figuring some things out along the way. It’s a fascinating process. We all have different work experiences and backgrounds, not to mention that we have to figure out our procedures aligned and working for people spread over four time zones and three continents.

My main goal for the first quarter of 2021 was to finalize the team handbook, but due to my health, I have fallen behind. Luckily for me, there is plenty of material around to learn about issues that remote teams face and how other companies addressed them, so I’m quickly catching up. I plan to finish the first version of our very own handbook by the end of the month and then start on a new goal for Q2. More on that in the upcoming weeks, since the project will involve all our team members, and we discussed it at length during our internal contributor day.

I have one-on-one meetings with my direct reports: one for each day. On Fridays, I have my call with Joost to report on the team’s work, my own work, and to have a good chat about broader issues.

At the end of March, I published the proposed schedule for WordPress 5.8 , and after Josepha Haden Chomphosy – WordPress.org Executive Director – approved it, I published the release page . If you are interested in the WordPress release cycle, I suggest you bookmark it. The page gets updated regularly with links to bug scrubs, test scrubs, blog posts, chats, etc.

I published the agenda for the weekly dev-chat and attended it. I really enjoy hosting them, but I am thankful that my co-representative for the core team, JB Audras, was able to take care of those while I was recovering.

Unlike some of my team members which have very specific focuses, I work on different topics every week, internal and external, and in a variety of Make WordPress teams.

I try to spend some time every week triaging issues in GitHub. This week, I:

What’s more, I check my notifications and submitted pull requests every day to stay on top of things.

I worked on updating the parties involved about the WordPress application to Google Season of Docs (GSOD). Unfortunately, I was informed that the application was not accepted. Also, I wrote an update on our call for projects ideas post , and I talked with some interested mentors for the GSOD. Some team members are still interested in working on the projects, so hopefully, not all is lost.

In addition, I attended the documentation team weekly meeting to share the news about GSOD and update the rest of the team about my plans for the next quarter (Q2).

In addition to my work on WordPress, I work on some internal projects, like our developer platform. This week, I worked on two developer platform issues related to the Yoast SEO plugin FAQ block and an old post on our developer blog.

I have also written my goals for Q2, something that we are experimenting with inside the team, and came up with some ideas for topics that I want to write about on this blog.

For the last two weeks, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8 , the next major release, as part of my duties as a core committer.

Also, I’ve continued chipping away at some long-standing coding standards issues in WordPress core with the ultimate goal for all of the core code to comply with its own coding standards, WPCS .

Moreover, I made eleven commits to WordPress core, participated in some other commits , and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

Similar to Justin, my WordPress involvement varies a lot from week to week. Since I only have Wednesday as the day I contribute, every week can bring something different. Some Wednesdays I might work on improving design team documentation and act as a notetaker for the design team meeting, on others I might make some mockups or respond to requests for feedback (for example, this week we looked at a design tweak for the Site Health widget ). And, most other Wednesdays, I try to triage some tickets in the ever-present backlog of the design team .

Justin is a member of the WordPress Core team at Yoast. His work focuses on improving the documentation systems for different parts of WordPress as well as creating a better onboarding experience for new WordPress contributors.

We care about the protection of your data. Read our privacy policy.
