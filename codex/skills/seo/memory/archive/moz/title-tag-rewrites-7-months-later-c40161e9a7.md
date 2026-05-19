---
source: https://moz.com/blog/title-tag-rewrites-7-months-later
title: Title Tag Rewrites: 7 Months Later
scraped: 2026-03-23
published_on: 2022-03-28
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Title Tag Rewrites: 7 Months Later

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/title-tag-rewrites-7-months-later
Published: 2022-03-28
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Back in August, we analyzed 10,000 SERPs and found that Google was rewriting 58% of the title tags we were able to track. In September, after some serious objections from the SEO community, Google made changes so that “title elements are now used around 87% of the time” . This immediately raises…

## Extracted Body
Back in August, we analyzed 10,000 SERPs and found that Google was rewriting 58% of the title tags we were able to track. In September, after some serious objections from the SEO community, Google released the following statement :

Based on your feedback, we made changes to our system which means that title elements are now used around 87% of the time, rather than around 80% before.

This immediately raises two questions. First, has the situation improved? Second, why the huge mismatch between our numbers (and similar numbers by others in the community)?

We collected new data on March 2, 2022 from the MozCast 10,000-keyword tracking set. Here are the basic stats, which are very similar to what we found in August 2021:

So, let’s compare the August 2021 rewrites to the March 2022 rewrites:

Technically, the numbers did go down, but this probably isn’t the news you had hoped to hear. If 57% of titles in our study were rewritten, then — I think we can all agree with this math — 43% did not get rewritten. So, how do we reconcile our 43% with Google’s 87%?

First off, our definition of “rewrite” is extremely broad, and it covers truncation, where Google just runs out of physical space. In August, I took a pretty simplistic view of truncation, but let’s try to give Google some benefit of the doubt. I’m going to dig into three forms of truncation, starting with the simplest:

The simplest form of truncation is when Google cuts off a long title but preserves the original text from the beginning. For example:

No one is doing anything wrong here — the IRS’s <title> is accurate and descriptive, but Google ran out of space. They didn’t take any liberties with the text.

Let’s review another form of truncation, with this example from the Linksys website:

Again, Google truncated a long <title>, but here they removed the branded text from the beginning and started with the more unique, descriptive text. Is this a rewrite? Technically, yes, but it’s a direct excerpt and the “...” clearly implies truncation to searchers.

Finally, we have situations where Google uses a portion of the <title> tag, but they don’t clearly indicate truncation with an ellipsis (“...”). Here’s an example from Congress.gov, a site Google is unlikely to view as spammy or in need of editorial revisions:

I don’t think Google’s trying to hide the truncation here by removing the ellipsis — the truncated title is a complete thought/phrase within the original title. In some cases, is this the excerpt the creator would have chosen? Maybe not, but I would still generally call this truncation.

All told, these three forms of truncation accounted for almost exactly one-third of the “rewrites” that we observed. These forms were distinct enough that we could separate them. From here on out, it gets a bit more complicated.

In addition to truncating long titles, Google sometimes adds information they deem relevant to the end of a display title. The most common addition is “brand” information (using the term loosely) that wasn’t present in the original <title> tag. For example:

I kind of love this title, and you should definitely ride Top Thrill Dragster at Cedar Point if you’re a coaster fan, but notice here how Google has appended “Touring Ohio” to the end of the display title. This kind of add-on is very common, occurring in almost 14% of our observed rewrites.

In some cases, adding the brand text caused Google to truncate the title prior to the addition. See this example from Goodreads …

While the rewrite here is intended to be beneficial, this can cause problems with long brand names. Anecdotally, though, Google seems to be doing a better job of this in the past few months, and most brand identifiers are of reasonable length.

Finally, in a few cases, Google appended location information. For example:

It’s not clear what situations trigger this added location information, but it does show that Google is considering appending other forms of relevant information that could drive future rewrites and go beyond brand tagging.

We can argue about whether truncation and addition are real, Capital-R Rewrites, so how about the situations where Google is clearly making substantial changes? Some of these situations — even working with a moderately-sized data set — are hard to classify, but I’ll cover some major categories.

I almost said “keyword stuffing,” but that’s a judgment call and isn’t always fair in these cases. Granted, there are legitimate cases of keyword stuffing, like this example:

Prior to August 2021, Google might’ve just truncated this title, but now they’re saying “Yeah, no” and replacing the entire mess. Other cases aren’t so clear, though. Consider this one:

AMC hasn’t really done anything spammy here — this <title> tag is likely a direct reflection of their site architecture. In this case, though, Google has gone beyond truncation and rewritten the title, including replacing pipes with hyphens, removing “Movie Times” (which is arguably redundant with “Showtimes”) and pushing the site/brand up.

Some people have too much to say, and some people are too quiet (I’m afraid I know which side I fall on). Here’s a case where the title didn’t quite provide enough information:

In many of these cases, like displaying just the brand name, a generic placeholder like “Home”, or – in one notable case – a code placeholder (“{{title}}”), it’s likely the culprit is an overzealous CMS default setting. These are clearly Capital-R Rewrites, but I would argue that Google is generally adding value in these situations by rewriting.

Sometimes, we marketers get a little carried away with colorful language (in this case, the family-friendly kind). Google still seems to be disproportionately rewriting <title> tags with certain superlatives, even when they may not seem excessive. Take this example:

This is a case where Google replaced the <title> with the contents of an <h1> — while it’s not a bad rewrite, it does feel aggressive to me. It’s hard to see how “21 Best Brunch Recipes” is wildly over the top or how “21 Easy Brunch Recipes” is a major improvement.

It’s hard to measure the real head-scratchers, but anecdotally, it does appear that Google’s rewrite engine has improved since August 2021, in terms of the truly bizarre edge cases. Here’s a funny one, though, from Google.com itself:

Even Google thinks that Google said “Google” too many times in this <title> tag. I suspect the rewrite engine flagged the word “Google” as redundant, but I’d definitely call this a misfire.

I made myself a to-do of creating a “pie chart with nuance,” and I now realize that’s impossible. So, here’s a pie chart that’s slightly less misleading. Many rewrites are hard to categorize and count, but let’s take a look at the data if we carve out the truncation scenarios (all three) and the additions:

Separating truncations and additions, we’re left with about 30% of <title> tags being rewritten in our data set. Keep in mind that many of these rewrites are minor and some probably involve forms of truncation and/or addition that were difficult to detect programmatically.

Flipping this around, we have 70% of titles not being rewritten. How do we reconcile that with Google’s 87%? It could just be a function of the data set, but let’s carefully re-read that quote from the beginning of the post:

Note the highlighted text — Google is specifically saying that they used the <title> element/tag 87% of the time. They may have subtracted from, added to, or slightly modified that original data (they don’t really say). So, the 13% of cases here is likely only when Google is pulling the display title in search from some other area of the page (body content, headers, etc.).

As to the bigger question of how much Google toned down rewrites after the initial outcry, it’s difficult to measure precisely, but I’d say “Not very much.” It does appear that some edge cases — including mishandling of parentheses and brackets — did improve, and I think Google turned down the volume a bit overall, but changes to titles remain fairly common and the reasons for these changes are similar to August 2021.

Dr Pete is a cognitive psychologist and resident Marketing Scientist at Moz.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
