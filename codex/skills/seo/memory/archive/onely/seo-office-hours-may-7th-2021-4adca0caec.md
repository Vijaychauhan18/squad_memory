---
source: https://www.onely.com/blog/seo-office-hours-may-7th-2021/
title: SEO Office Hours - May 7th, 2021
scraped: 2026-03-23
published_on: 2021-05-10
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# SEO Office Hours - May 7th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-may-7th-2021/
Published: 2021-05-10
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on May 7th, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on May 7th, 2021.

4:16 – “Bing is open about using machine learning to adjust the weights of the ranking signals in their search algorithm. What about Google – does it use machine learning in search?”

John confirmed that Google does use machine learning to adjust weights of search ranking factors based on user behavior.

He also specified that not all ranking factors are influenced by machine learning.

“For some elements, we definitely use machine learning, for other elements, we don’t use it as much.”

As an example, he said focusing on user clicks in a machine learning model would result in Google primarily surfacing the clickbait content.

The follow-up question was specifically about Google Page Experience update and whether Google will incorporate it into the ranking algorithm using machine learning.

“I don’t know. I mean, the different weightings of different parts of the algorithms are something that is pretty tricky to do because you can’t just manually say, oh, this is weighted 10%, and then suddenly everything else is 10% less overall.

You kind of need to watch out for the whole system. (…) Maybe we use the values directly from machine learning, maybe we adjust them manually, maybe we just start with something manual and see how it goes, I honestly don’t know.”

13:58 – Many services allow you to better manage and track the affiliate links on your site. What they offer is sometimes referred to as “link cloaking” – every affiliate link is “covered” with a “nofollow” internal link that’s redirected to the affiliate page with a 302 redirect. Does this go against the Google guidelines?

He added, “The important part for affiliate links is that there’s a nofollow attached or that we can’t crawl through the links, so if you have a nofollow or that bounce URL that you have on your site is blocked by robots.txt, then you have everything right.”

29:00 – An interesting discussion on redirects began after Barry Schwartz commented on the previously covered topic of redirects and SEO . Barry was contacted by an inhouse SEO team of an eCommerce store whose dev team was planning a migration. The problem was the devs wanted to ease into the migration by fully redirecting the site 5 times in the coming year, slightly modifying the URL structure in each iteration. Barry called this an “SEO suicide”.

John agreed and added that whenever you are restructuring your site, you should try to move to the final destination as soon as possible. He said:

“Every redirect step that you take, it takes a while to be processed and you will see fluctuations in search when that happens. If you take everything and you do it once, you have it done with. Whereas, if you do everything once a month, then, like, every month you have that time of things trying to resettle down.”

If you’re struggling to implement a migration, contact us, and we’ll develop an SEO migration plan with you.

32:03 – A website has content on the main page that’s loaded with client-side JavaScript. It’s not essential to the overall content of the homepage, but aims to enrich the user experience. The team is thinking of ways to minimize the impact of executing JavaScript on Web Performance. They consider loading the content after several seconds of inactivity, or when user first interacts with the page. What’s the best approach to take in order to make sure robots can read this content?

John said that since this content doesn’t seem really critical, maybe it’s fine if Googlebot doesn’t pick it up.

That being said, he gave an explanation of how Googlebot looks at web pages:

“ We usually recommend (…) using the IntersectionObserver , which is (…) a browser API that essentially lets you know which parts of the page are visible at the moment. And Googlebot uses that when we render the page. And we render the page in the way that we take a really long viewport, like a really long monitor, and we try to load the page. And we tell the page, like, this is your viewport – this tall. And then we give the page time to load the content that would be visible.

So essentially with that setup, if you recognize that this part of the content is visible and you show it, then we’ll be able to index that. (…) The other way is where we have to watch out for a scroll event or for someone to click a “Load more” button, something like that. That’s usually something that Googlebot tends not to do. (…) So that’s something where probably we would not be able to pick up that content, but if you’re using IntersectionObserver, probably we would be able to. ”

41:25 – “Can a small amount of English text on a non-English language page negatively impact its rankings?”

Usually not. “Depending on the amount of text, we would recognize that there are multiple languages on a page and what might happen is that we show that link, like, there’s something here in another language and would you like to have it translated?

But essentially, that’s not a ranking issue, it’s more, kind of a usability may be a bit confusing for users in some cases.”

Find out more about using multiple languages within one URL with our International SEO article.
