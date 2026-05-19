---
source: https://yoast.com/recap-of-aprils-contributor-day/
title: A week with us: Recap of April's contributor day & our team update
scraped: 2026-03-23
published_on: 2021-04-16
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

# A week with us: Recap of April's contributor day & our team update

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/recap-of-aprils-contributor-day/
Published: 2021-04-16
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This April we had another WordPress contributor day at Yoast! We tested full site editing, and learned a lot in the process!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

On April 9th, 2021, we held our sixth internal contributor day at Yoast. It’s also the third one since we have a team of full-time sponsored contributors to WordPress.org. We decided to dedicate the day to testing, as we did for our previous event . Here is what we did.

The WordPress project is now deep into Phase 2 of Gutenberg , which addresses customization. Its goal is to take blocks outside of post and page content into other areas of the site. Once this phase is completed, everything will be a block, and users will be able to edit entire areas that previously required coding skills. For example, Phase 2 includes significant changes such as block-based themes.

We decided to focus on testing full site editing from different perspectives to give as much diverse feedback as possible to the team working on these features.

This time we had over 40 Yoasters joining us! Even more impressive, over 20 of them were still standing after over six hours of testing and coding on camera via Zoom.

We always start Contributor Days with a short introduction, so everyone can get a feeling of what it means to contribute to WordPress. Then, we share more detailed instructions about the day ahead.

The organizing team – a joint effort by our team and the Yoast community team – strives to make it as clear as possible for colleagues to join. So, we prepared a document with all the information. Feel free to make a copy of it in your Google Drive or download it to organize a testing drive for your organization as well!

At the end of the day, we were joined by two special guests for a Q&A session: Riad Benguella , the lead developer of the Gutenberg Project, and Matías Ventura , the lead architect.

It was great to have them with us. We briefly recapped what we did during the day and got to ask some questions that ranged from UX to integration with WP core. More than anything, it was a great occasion to have a conversation with people that work on WordPress full time, like my team does, and are invested every single day to make it better for its millions of users. I like to call them colleagues because, in the realm of open-source, we truly are colleagues.

A lot! We collected 30 test reports, and these, together with our developers’ work, resulted in over 25 issues opened in GitHub and a recap of the most common findings. You can read them in the call for testing comments .

I will not lie. Most of us were confused by the current UX and UI of the full site editing experience. For some of our colleagues, this was the first time using the block editor for a whole day. For all of us, except for Ari and Carolina, it was the first time we ever saw full site editing in action.

After some initial struggle, everyone was able to complete the task: create a restaurant-themed header. And, as you can tell from this gallery, we had some fun doing it.

Some Yoasters, none of whom from the design team, produced some very sleek designs

In the last two weeks, my focus was on hybrid themes. With parts of Full Site Editing approved for WordPress 5.8 , theme-authors will need a way to slowly transition from PHP templates to HTML templates. In preparation for that, a lot of fixes were done in Gutenberg for the template hierarchy – both for files in the theme as well as user-generated custom templates . Further improvements to FSE for developers included adding a supports_block_templates function , fixing bugs with the site-editor , and many other smaller fixes.

During our internal Contributors day, I coordinated with other developers from Yoast. We tested the site editor, and I helped my colleagues contribute, make some more pull requests in the project, fixing accessibility and UX issues.

Last Tuesday, I was a guest at a show called WP Cafe, together with designer Mel Choyce-Dwan and the hosts Mark Wilkinson and Keith Devon. Even though I was nervous beforehand, the show was a lot of fun, and we talked about building Twenty Twenty-One but also about block patterns and full site editing.

Great episode! Carolina and Mel give a glimpse into the past (how Twenty Twenty-One came to be) and into the future, with full site editing coming. Great questions, worth an hour of your time, for sure🙌 https://t.co/b7jqFq2XOn

The week was very busy, and the team had our last session in the management training program together. Of course, we also had the contributor day.

On Monday, I spent most of the day reading the reports and watching recordings from all the Yoast testers that helped out at the contributor day. I found this rewarding, and I learned new insights about how users perceive the different WordPress editors and what they may find difficult. We have a lot of work ahead of us to make navigating and editing easier, but I am hopeful. This kind of user feedback is important at this early stage. The feedback was forwarded to the Gutenberg project as issues and comments on the GitHub repository. Some of the problems have already been solved and will be included in the next version of the Gutenberg plugin.

In mid-March, I tested positive for COVID, and I have yet to regain my ability to function for more than a few hours a day. So in the past two weeks, I mostly focused on internal tasks.

I also did prep work for WordPress 5.8 , the upcoming release, now officially scheduled for July 20th 2021.

Over the past couple of weeks, I’ve started doing regular triage on the Gutenberg GitHub repository . The issues I’m currently going through are related to CSS changes , documentation , good first issues , and a bit about accessibility .

Another thing I’ve been doing is continuing to reach out for the Google Season of Docs. Among other things, there was a meeting with the French WordPress documentation team to tell them about some GSOD projects that WordPress is proposing and possibly recruit some interested people.

Of course, there was also the Contributor Day at Yoast, which we all attended. During the day, I helped with the Full Site Editing user testing.

For the last two weeks, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8, the next major release, as part of my duties as a Core Committer. I was also working on some tickets for WordPress 5.7.1, the latest minor release.

I’ve started chipping away at some long-standing coding standards issues in WordPress core with the ultimate goal for all of the core code to comply with its own coding standards, WPCS. I made thirty-one commits to WordPress core and triaged new incoming tickets into Trac (the bug tracking system that WordPress uses).

Last week was all about the Yoast contributor day. I joined Francesca, Justin, and a bunch of other Yoasters in testing full site editing. We went through the full site editing (FSE) outreach program’s user tests, which tasked us with things like making a site header, building a homepage with blocks, editing templates, and more. It was a good opportunity for me to get up to speed with the current state of FSE, as well as observe a bunch of people who had never seen FSE before or didn’t have much experience with Gutenberg in general. It brought a whole lot of issues to light that will be super useful in improving how user-friendly FSE is at launch. That was great!

Francesca used to be the lead of the WordPress core team working full time on the open-source project with some of the brightest minds in the industry. She is an accomplished educator, community leader, and public speaker.

We care about the protection of your data. Read our privacy policy.
