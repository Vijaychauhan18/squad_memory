---
source: https://moz.com/blog/title-tag-rewrite-case-study
title: Tackling 8,000 Title Tag Rewrites: A Case Study
scraped: 2026-03-23
published_on: 2021-09-16
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

# Tackling 8,000 Title Tag Rewrites: A Case Study

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/title-tag-rewrite-case-study
Published: 2021-09-16
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Let's take an in-depth look at Moz.com title tags that were re-written by Google, including three case studies where we managed to fix bad rewrites.

## Extracted Body
I recently dug into over 50,000 title tags to understand the impact of Google’s rewrite update . As an SEO, this naturally got me wondering how the update impacted Moz, specifically. So, this post will be a more focused examination of a site I have deep familiarity with, including three case studies where we managed to fix bad rewrites.

As an author, I take titles pretty personally. Imagine if you wrote this masterpiece:

… and then you ended up with a Google result that looked like this:

Sure, Google didn’t do anything wrong here, and it’s not their fault that there’s an upper limit on what they can display, but it still feels like something was lost. It’s one thing to do a study across a neutral data set, but it’s quite another when you’re trying to understand the impact on your own site, including articles you spent hours, days, or weeks writing.

I’m not going to dig deep into the methodology, but I collected the full set of ranking keywords from Moz’s Keyword Explorer (data is from late August) and scraped the relevant URLs to pull the current <title> tags. Here are a few of the numbers:

Note that just under 2,000 of these “rewrites” were really pre-update (...) truncation. The majority of the rest were brand rewrites or removals, which I’ll cover a bit in the examples. The number of significant, impactful rewrites is hard to measure, but was much smaller.

While I have reservations about Google rewriting title tags (more on that at the end of this post), I tried to go into this analysis with an open mind. So, let’s look at what Google got right, at least in the context of Moz.com.

Our CMS automatically appends our brand (“ - Moz”) to most of our pages, a situation that’s hardly unique to our site. In some cases, this leads to an odd doubling-up of the brand, and Google seems to be removing these fairly effectively. For example:

While the CMS is doing its job, “Moz - Moz” is repetitive, and I think Google got this one right. Note that this is not simple truncation — the additional text would have easily fit.

Okay, I’m not sure I want to admit this one, but occasionally we test title variations, and we still live with some of the legacy of rebranding from “SEOmoz” to “Moz” in 2013. So, some areas of our site have variations of “ | SEO | Moz”. Here’s how Google handled one variety:

While it’s a bit longer, I suspect this is a better extension for our Q&A pages, both for us and for our visitors from search. I’m going to call this a win for Google.

I have no idea what the original intent of this <title> tag was (possibly an experiment):

While there’s nothing terribly wrong with the original <title> tag, it’s probably trying too hard to front-load specific keywords and it’s not very readable. In this case, Google opted to use the blog post title (from the <H1>), and it’s probably a good choice.

It may seem strange to cover examples where Google did an okay job, but in some ways these bother me the most, if simply because they seem unnecessary. I feel like the bar for a rewrite should be higher, and that makes the gray areas worth studying.

For some of our more evergreen pieces, we put the Moz brand front-and-center. In a number of cases, Google shuffled that to the back of the title. Here’s just one example:

There’s nothing inherently wrong with this rewrite, but why do it? We made a conscious choice here and — while the rewrite might be more consistent with our other content — I’m not sure this is Google’s decision to make.

This is a variation on #4, conceptually. Some of our Whiteboard Friday video titles end in “- Whiteboard Friday - Moz”, and in this example Google has split that and relocated half of it to the front of the display title:

Whiteboard Friday is a brand in and of itself, but I have a feeling that #4 and #5 are really more about delimiters in the title than the brand text. Again, why did this trigger a rewrite?

You might be thinking something along the lines of “Google has all the data, and maybe they know more than we do.” Put that thought on hold until the end of the post.

Here’s an example where Google opted for the post title (in the <H1>) instead of the <title> tag, with the end result being that they swapped “remove” for “delete”:

This isn’t really a single-word substitution (so much as a total swap), and I don’t know why we ended up with two different words here, but what about the original title — which is extremely similar to the post title — triggered the need for a rewrite?

One quick side note — remember that Featured Snippets are organic results, too, and so rewrites will also impact your Featured Snippets. Here’s that same post/rewrite for another query, appearing as a Featured Snippet:

Again, there’s nothing really wrong or inaccurate about the rewrite, other than a lack of clarity about why it happened. In the context of a Featured Snippet, though, rewrites have a greater possibility of impacting the intent of the original author(s).

It’s the moment you’ve been waiting for — the examples where Google made a mess of things. I want to be clear that these, at least in our data set, are few and far between. It’s easy to cherry-pick the worst of the worst, but the three examples I’ve chosen here have a common theme, and I think they represent a broader problem.

Here’s an example of rewrite truncation, where Google seems to have selected the parenthetical over the main portion of the title:

Many of the bad examples (or good examples of badness) seem to be where Google split a title based on delimiters and then reconstructed what was left in a way that makes no sense. It seems especially odd in the case of a parenthetical statement, which is supposed to be an aside and less important than what precedes it.

In other cases, Google uses delimiters as a cutting-off point, displaying what’s before or after them. Here’s a case where the “after” approach didn’t work so well:

This is user-generated content and, granted, it’s a long title, but the resulting cutoff makes no sense out of context. Standard (...) truncation would’ve been a better route here.

Here’s a similar example, but where the cutoff happened at a hyphen (-). The title style is a bit unusual (especially starting the sub-title with “And”), but the cutoff turns it from unusual to outright ridiculous:

I get what Google’s trying to do — they’re trying to use delimiters (including pipes, hyphens, colons, parentheses, and brackets) to find natural-language breaks, and split titles at those breaks. Unfortunately, the examples demonstrate how precarious this approach can be. Even the classic “Title: Sub-title” format is often reversed by writers, with the (arguably) less-important portion sometimes being used first.

Ultimately, some rewrites will be good-to-okay and most of these rewrites aren’t worth the time and effort to fix. Over half of the Moz <title> rewrites were minor brand modifications or brand removal (with the latter usually being due to length limits).

What about the objectively bad rewrites, though? I decided to pick three case studies and see if I could get Google to take my suggestions. The process was relatively simple:

Update the <title> tag, trying to keep it under the length limit

If the rewrite didn’t take, update the <H1> or relevant on-page text

Here are the results of the three case studies (with before and after screenshots):

This one was really our fault and was an easy choice to fix. Long story short, a data migration led to a special character being corrupted, which resulted in this:

I’m not blaming Google for this one, but the end result was a strange form of truncation that made “Google Won’t” look like “Google Won”, and made it appear that this was the end of the title. I fixed and shortened the <title> tag, and here’s what happened:

Interestingly, Google opted to use the <H1> here instead of the shortened <title> version, but since it fixed the main issue, I’m going to call this a win and move on.

Here’s another one where Google got it wrong, breaking the <title> tag at a parenthetical that didn’t really make any sense (similarly to the examples above):

Since this was a recent and still-relevant post, we were eager to fix it. Interestingly, the first fix didn’t take. I had to resort to changing the post title (<H1>) as well, and removed the parentheses from that title. After that, Google opted for the <title> tag:

This process may require some trial-and-error and patience, especially since the GSC reindexing timeline can vary quite a bit. Most of these updates took about a day to kick in, but I’ve recently heard anywhere from an hour to never.

Our final case study is a complex, multi-delimiter title where Google decided to split the title based on a phrase in quotation marks and then truncate it (without the “...”):

Although the main portion of the rewrite is okay, unfortunately the cutoff makes it look like the author is telling readers to ditch Moz. (Marketing wasn’t thrilled about that). I opted to simplify the <title> tag, removing the quote and the parentheses. Here’s the end result:

I managed to sneak in all of the relevant portion of the title by switching “And” out with an ampersand (&), and now it’s clear what we should be ditching. Cue the sigh of relief.

While there’s potentially a lot more to be done, there are two takeaways here:

You need to prioritize — don’t sweat the small rewrites, especially when Google might change/adjust them at any time.

The bad rewrites can be fixed with a little time and patience, if you understand why Google is doing what they’re doing.

I don’t think this update is cause for panic, but it’s definitely worth getting a sense of your own rewrites — and especially patterns of rewrites — to make sure they reflect the intent of your content. What I found, even across 8,000 rewrites, is that there were only a handful of patterns with maybe a few dozen examples that didn’t fit any one pattern. Separating the signal from the noise takes work, but it’s definitely achievable.
