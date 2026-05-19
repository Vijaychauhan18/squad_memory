---
source: https://www.onely.com/blog/my-ultimate-guide-to-indexing-seo-isnt-indexed/
title: My Ultimate Guide to Indexing SEO Isn’t Indexed
scraped: 2026-03-23
published_on: 2021-03-30
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

# My Ultimate Guide to Indexing SEO Isn’t Indexed

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/my-ultimate-guide-to-indexing-seo-isnt-indexed/
Published: 2021-03-30
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
According to the URL Inspection Tool in the Google Search Console, our recent article wasn't indexed. Or was it?

## Extracted Body
Last week, I published my Ultimate Guide to Indexing SEO – a rather long piece of content that covers most aspects of indexing and solving issues around getting your pages indexed by Google.

It was published on March 25th, right after the presentation I gave on the same topic at BrightonSEO.

I shared the guide with the attendees as a useful resource for further research.

The next day, after ~30 hours from the guide being published, my colleague wrote to me: “Hey Tomek, your Ultimate Guide to Indexing is not indexed on Google yet.”

I don’t want to brag, but this is a seriously valuable and unique piece of content. Google should index it without much hesitation.

So I was fairly sure some bugs must have happened on Google’s end. And I wasn’t wrong.

The Ultimate Guide’s URL was reported as “Discovered – currently not indexed.”

Google Search Console also showed no internal links pointing to this page.

I thought: “Wait, there are links on our Blog and I am sure Google saw them!”

To make sure, I used the URL Inspection tool with our Blog homepage.

I looked inside the crawled HTML, and my intuition wasn’t wrong. There WAS a link pointing to the Ultimate Guide.

Discovered – currently not indexed: The page was found by Google, but not crawled yet. source: Google

So Google discovered the Ultimate Guide but didn’t even crawl it.

Normally, I would wait longer before getting suspicious, and check if other pages were affected by this issue.

The page that wasn’t indexed was The Ultimate Guide to Indexing SEO!

Server log analysis is essentially a tool SEOs can use to spy on Googlebot. You can use them to check which pages were visited, and when. Quite powerful.

If you happen to be a Googler reading this and you want to investigate, here is the exact footprint:

The obvious question that comes to mind is: “ Is this just a reporting bug from Google Search Console?”

It turned out that Google indexed an improper version of the page, and I have no idea why,

When you search for “Ultimate Guide to Indexing SEO”, you’ll find the page, but…

Google indexed the version with no trailing slash. Which, according to our server logs, was never crawled by Googlebot. So why did it happen? It’s not the canonical version, and there are no links on our site pointing to the URL without the slash!

I saw similar patterns multiple times on other websites. For instance, I saw a few big brands that suffered from a temporary bug when the HTTP version was ranking instead of HTTPS.

Is this just a reporting bug? Or is Google missing ranking signals from the canonical version, with the trailing slash?

I was able to investigate the issue and, at the very least, notice that the reporting in GSC was wrong.

But many site owners won’t go looking for the answer in their server logs.

Indexing issues are often self-induced. But just like in the case of my Ultimate Guide, Google’s systems sometimes don’t work as expected.

And in my case, it’s just one page. Here’s a story showing that this can happen on a much larger scale.

Recently, a friend of mine, who is working for a popular news publisher, got his website permanently de-indexed. It stopped showing up in Google Search, Google Discover, and Google News.

The situation lasted for 2 weeks, then it went back to normal. They didn’t get any notification from Google.

And it’s not even the first time this happened to that company. They previously had a different domain fully deindexed for 2 weeks.

Then, with no action taken on their end, Google started showing their domain in search results again. Why does this happen?

Google Search is a very complex system, and it’s expected that bugs will happen every now and then.

There are many ways to get help from Google in these cases: We have fantastic Google representatives helping the community, recording SEO Office-hours, and answering questions on Twitter and in the Google Webmaster forums.

That being said, I can’t shake the feeling that Google could be more transparent when it comes to indexing bugs that happen every single day and give us more meaningful advice on solving them.

Have you ever had similar problems with your content? Did you manage to diagnose the issue, or did you simply wait it out? Let me know!

And if you need any help with indexing bags, contact Onely for technical SEO consulting.
