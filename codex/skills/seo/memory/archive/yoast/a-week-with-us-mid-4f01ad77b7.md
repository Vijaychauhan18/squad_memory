---
source: https://yoast.com/a-week-with-us-performance-review-time/
title: A week with us - Mid
scraped: 2026-03-23
published_on: 2021-07-08
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

# A week with us - Mid

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/a-week-with-us-performance-review-time/
Published: 2021-07-08
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Find out what the WordPress core team has been getting up to this week, including performance reviews and more fixes and improvements!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

In the past few days, the team has been busy with different tasks. Some related to the WordPress current release, some related to the company rituals, like mid-year performance reviews. Our team is working separately from the Yoast plugins release cycles, and it’s hard to identify goals since our tasks depend heavily on how the WordPress open source project is going, and where we are needed. Let’s hear from everyone.

I continued working on the project we have nicknamed “ Update the Updater “. It is an effort to improve the WordPress plugin & Theme updaters, and we made a lot of progress.

I collaborated with Sergey and we established a weekly co-working session where we go over things and figure out ways to make things better.

After consulting with Omar and Sergey, I built an initial proof-of-concept implementation for a database-upgrading API.

We also improved our implementation to make updates more secure. The idea is to keep backups of existing versions prior to an update. If the update process fails, then the backup gets restored. This should significantly reduce the risk of plugin & theme updates. After we polish this implementation some more, we’ll make a request to port these improvements to WordPress Core.

The release date for WordPress 5.8 is closing in, and with it, the amount of stress our team is under also increases.

This past week I wrote a developer note , detailing some performance improvements that we included in WordPress 5.8, and followed-up by replying to comments.

I started thinking of my goals for WordPress 5.9 and they will include the following:

The above items are early ideas and goals, but a plan like that does help me focus.

This was a first for me… As part of this amazing team, we had to write a “mid-year performance review”. I’ve never had to do something like this before so it did take me a few hours to compile. I liked the format. The aim was to evaluate our goals, self-reflect, identify pain points and opportunities to grow, and ultimately improve the team as a whole.

With all the other priorities this past week, my Gutenberg contributions were rather limited. I focused on small bug fixes, and making life easier for other developers by reviewing their code and helping get improvements merged in Gutenberg.

This week, I have continued working on reducing the requirements for submitting themes to WordPress.org. I am eager to move forward with the changes and sometimes things do not move as fast as I would like. There are lots of discussions within the Themes team about how to give theme authors more freedom and keep themes secure. We hope to publish the first proposal for requirement changes soon. You can follow the work in progress in the different GitHub repositories . I have created and reviewed pull requests for updating automated checks and solving bugs in the Theme Check plugin . Dion Hulse , from the WordPress.org Meta team, has proposed a solution for a problem that prevented block themes from being uploaded to the theme directory. I have learned that to contribute more to the theme review action tool, I need to learn more about Jest and Puppeteer, the stack used by WordPress to run end-to-end tests . I am gaining a better understanding of what will be possible to test with theme review action.

There have been some issues with the dark mode in Twenty Twenty-One and WordPress 5.8. A solution has not been found yet and it is unclear how the dark mode will be managed in 5.8 ( #53530 ).

On Wednesday, I participated in a hallway hangout about theme.json, the theme configuration file coming in WordPress 5.8. I enjoyed this and I think we should do more of these hangouts.

I have tested updates to the free and premium versions of the Yoast SEO plugin with the WordPress 5.8 release candidate. I also need to take the time to read about existing issues and keep myself informed of what other more experienced testers are finding.

As I am spending more time on testing, I found that I miss coding and staying up-to-date with changes to Gutenberg. So while opening an issue on the Gutenberg GitHub repository, I also submitted a one-line pull request to add a link color control to the list block .

Performance reviews are always nerve-wracking because you want to do well. This is not my first performance review, but it is my first at Yoast. While I was employed at a government agency in a different field, we had yearly performance reviews, but they were not as detailed and well-planned as the one at Yoast.

The performance review has three parts, and I have only completed the first. I was happily surprised by the depth of it, and how it encouraged me to reflect over the past six months. I am still nervous about the next parts, where I will find out if I have done well. After that, we will make plans for the rest of the year.

Last week I was off for a much-needed vacation. Nothing to report but I have a reminder for our readers: please, pace yourself and remember to rest when you need it. Especially, if like our team, you work on open source a lot, you know it can be emotionally charged and time-intensive.

I came back to receive my first mid-year performance review and prepare to deliver the reviews to the rest of the team. It is an interesting process: we are called to self-evaluate our knowledge and personal development and re-arrange the course of action if needed, also in our personal development plan which we prepared in January.

In a “Hup, hup, hup” life ( see core value number 8 ), it feels important to be able to sit down, self-reflect, review, refine, and move forward. This is my first time ever receiving and giving such a structured review. It was intimidating at first and liberating once I started pouring words on paper.

As I mentioned in the introduction, our team flow is not strictly tied to Yoast’s. We work on WordPress. But we do so on behalf of a company and not as volunteers. Lately, I have been feeling that these two entities need to work closer together. And I have been also thinking about how open source seems to follow the dreaded famine and feast cycle, common in small businesses. How do we, and other sponsored contributors, help everyone avoid contribution burnout? How can we make the chaotic bazaar preserve its flat hierarchy while also introducing stability, predictability, and sustainability? Lots of food for thought for the next months and I will make sure to document it here.

I’ve spent quite a bit of time working on my mid-year performance review. This is the second time I’ve had to do something like this. Let’s just say that it was both interesting and time-consuming. I was able to reflect on my work at Yoast, and in the WordPress project, on what could be improved, etc.

The triage and scrub meetings with the WordPress test team are usually a good opportunity to see how each of the contributors is doing, and how we can help each other. For last Tuesday’s triage, we went through the testing report tickets for WordPress 5.8 and 5.8.1 . I particularly tested this ticket related to a problem with blocks in the new widget page.

I also resumed triaging on the Gutenberg repository, focusing on CSS and frontend issues.

I’ve been working with the QA team at Yoast on the e2e test package we’re creating for our products. So I spent some time learning how Jenkins works, and how we could use it to automate e2e tests with the package.

For the last week, my main focus was to put some finishing touches on the WordPress 5.8 Release Candidate, as part of my duties as a Core Committer.

I made twenty five commits to WordPress core, mostly some documentation cleanup for new features in the 5.8 release. I also triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

Together with Ari, I worked on the Updater project to make updating plugins and themes more reliable. Currently, we’re testing an approach to keep a backup of an existing plugin or theme version before performing an update, and only removing the backup once the update is fully completed.

Along with my colleagues, I worked on a mid-year performance review. This was the first time I had to do that, and I liked it. Reflecting on our goals, personal and professional development, learning new skills, and making incremental improvements to our workflows always sounds like a good idea.

Francesca used to be the lead of the WordPress core team working full time on the open-source project with some of the brightest minds in the industry. She is an accomplished educator, community leader, and public speaker.

We care about the protection of your data. Read our privacy policy.
