---
source: https://moz.com/blog/google-navboost-and-brands
title: Google’s Navboost Queries and Brands in SEO
scraped: 2026-03-23
published_on: 2024-06-25
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

# Google’s Navboost Queries and Brands in SEO

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/google-navboost-and-brands
Published: 2024-06-25
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Are you still sleeping on brand as a ranking factor? Explore Tom’s detailed takeaways from the Google leak, with an emphasis on understanding Navboost queries, a click-based ranking system, and branded search.

## Extracted Body
The recent Google leak has produced a wide range of answers and even more questions and probably will continue to do so as SEOs keep sifting through the detail. For me, perhaps the most interesting concept is that of a “NavBoost query,” and that’s what I’ll be covering in this post — my newly informed understanding of what these are, how they’re used, and what that should mean for SEO.

My conclusion is that Navboost queries are an at-any-one-time finite list of high-volume terms for which Google has click data. In some cases, these can be closely associated with specific URLs, a concept similar to what we in SEO might call a branded or navigational search – when a searcher has one destination in mind.

This relationship between branded search, high-volume terms, and (seemingly) click signals is something myself and others have noticed in the wild and have been writing about for many years now. In some ways, my reading of the leak confirms hypotheses I had in the past; in others, I have to say the real system sounds far simpler than what any of us imagined.

And, of course, this wouldn’t be an SEO blog post if I didn’t give you some tactical implications at the end.

In February 2017, I presented this deck on SearchLove San Diego’s infamous 4:3 aspect ratio projectors, with the slightly melodramatic title “Does Google Still Need Links?” (yes, it does). I talked about how PageRank had originally been intended as a proxy for the popularity (not authority) of a webpage, and Google has a ton of better answers to that question in the form of Chrome, Google search itself, and everything else.

I also pointed out in that presentation that branded search volume was statistically a much stronger predictor of organic rankings than even Moz’s Domain Authority® — not because I thought that either were ranking factors in a causal sense, but because I thought that was an interesting indicator of what Google might be rewarding.

About 18 months later, I wrote this article , pointing out my observation that the top few results for higher-volume terms seemed to exhibit different ranking behavior to the rest of search. “The two-tiered SERP,” I called it, and hypothesized that this could be caused by the availability of click data.

I recall all of this now not to brag — well, maybe a little bit to brag — but more to point out that as SEOs we shouldn’t be (and mostly aren’t) totally surprised by some of these “revelations.” I wasn’t the only one thinking along these lines. Rather, this is often confirming things in which we already were quite confident. Nonetheless, knowing them with near certainty does add significant conviction to the aforementioned tactical implications and allows us to build upon this understanding.

All of this also relates to why Moz built Brand Authority TM . When I said above that I wasn’t the only one thinking along these lines years ago, one of the people I know of for certain is my (now) colleague Dr. Pete, who had been working to construct a search-based brand metric back in 2020. I started at Moz in early 2021, and we had some concerns back then about how easy it would be to explain the value of such a metric to the industry (plus a lot of R&D to do — this isn’t as easy as it sounds). In 2023, we launched this metric in beta as Brand Authority, and Google seems to have done a lot of that justificatory heavy lifting for us with this leak in 2024. (As luck would have it, Brand Authority is available today via our API , and International Brand Authority and inclusion in our v3 API is coming later this summer.)

We learned a bit about Navboost as a system in the US vs. Google testimony last year. Specifically, we learned that it is a system that uses clicks to optimize rankings — that thing that Google always denied the existence of. That’s all very interesting, and we learned a bit more about that and how it is used in the recent leak, too. What I’m interested in for this post, though, is the narrower concept of a “Navboost query.”

Let’s have a look at some examples from the leak in context.

Spicy salad aside, this module is innocuous-looking, without the obvious scandal of other sections, but it’s possibly my favorite of the whole leak. It seemingly relates to Featured Snippets (aka “Radish Features?”), and there are a number of interesting mentions of Navboost queries. Most of these bullets look to relate to pairwise comparison of snippets with Navboost queries — “Is this a good answer for this question?”. This bullet is especially revealing:

“Similarity score between this navboost_query and the incoming query”

So, is Google assessing the potential featured snippet against a Navboost query, but then showing it in search for a different, similar query? To me, that implies a finite list of Navboost queries, which absolutely makes sense for all the reasons I was hypothesizing in 2018. The other mentions fit with this understanding, too, but let’s have a look at some more modules.

I think this section probably relates to indexing sections or passages in web pages, to allow deep links into the article from the SERPs. (For example, the anchor links you see on the left of this blog post often get impressions from one-line sitelinks in Google search.) Again, that’s all very interesting in its own right, but here’s the pertinent bits for today:

“...a document might have multiple anchors or navboost queries.”

“Pointer to the exact set of image navboost queries in the cdoc.”

(“cdoc” probably means “composite document” — or a webpage with images or other media as well as text.)

Of course, we might consider it obvious that a page could rank for multiple queries. I suspect Google search engineers are also well aware of this. So why do we need to explicitly call out that a document with multiple sections might end up being relevant for multiple Navboost queries? The best way to make sense of this is if Navboost queries necessarily relate to relatively distinct concepts. You don’t bother having two similar ones — synonyms and misspellings and such can be grouped with the most similar Navboost query like in the Featured Snippets example above.

Again, this sounds as if we have a list of distinct queries (narrow intents?) that we have data for.

The rather cumbersome title of this module seems to imply that it exists for research purposes. How exactly it’s used is unclear. The description tells us this module represents “The information representing one navboost query for the dataset source_url.” So, this seemingly is information relating to a specific pairing of a search query and a page that can rank for that query. A “tuple” in this context, I would guess is said combination — so we’re looking at impressions and long clicks for specific pages for specific Navboost queries.

One can assume that if a page has great CTR for a specific query, its rankings ought to be adjusted accordingly. That said, note that this is labeled as being for research purposes — so although we’ve seen tests in the wild for many years (for example, by Rand Fishkin) showing a live feedback loop, that might not be exactly what we’re looking at here. Instead, this could be to inform other parts of the algorithm based on that kind of data.

What it does show is that Google is clearly thinking in these very clear-cut terms about query-specific engagement for a page. Again, that can only be possible for head terms or large bundles of similar grouped terms.

This clearly relates to image search, but it’s still very revealing, and we can assume image search and (the typically more lucrative) web search have significant commonality, certainly in use of internal Google search engineering jargon.

Here again, we have pairwise comparison of images with queries and the “Click-based rank of the image for this query.” Again, there are only two ways to make this possible across the vast long tail of search:

Blur all the lower-volume terms into their closest high-volume term

Either of these could be the case and have similar implications for us today. Speaking of which…

You’d be forgiven for thinking the previous section is rather academic. To an extent, that’s true, and it's no bad thing. I think understanding the vocabulary is a key initial step to getting more out of the information windfall here. However, there are two sets of tactical implications I’d like to draw attention to, especially as relates to ranking for “head terms”:

All the usual imperative to prioritize UX, brand, and clickiness implied by a click-based ranking system.

Identification of pages that have a 1:1 relationship with a high-volume search term.

(1) has been labored many times in many places for many years by many people, including me, so I won’t go over that here.

Mike King, in his initial roundup of the leak, drew the very astute link with this 2012 patent associated with Panda.

This process could be interpreted as looking for whether a page has suspiciously too many or too few links considering its branded search volume — or, in other words, perhaps being “over-SEOd.”

The language in the middle section of my screenshot (304) is interesting to us today:

“Determine a count of reference queries for the group of resources.”

A reference query that is navigational to the resource, you say? How could one determine such a thing? Well, there’s this system called Navboost…

So not only does branded search drive traffic to your website with enormous great sitelinks that obscure any potential competitors, it also might be part of the algorithm that informs non-branded search — at least, once you’re competing at the top for higher-volume terms (and concepts?). And branded search might be defined simply by one page or site being the overwhelming winner of clicks for a given term or concept.

This is what I was alluding to at the start of this post when I remarked that this could all be rather simpler than I ever imagined.

What’s also important to note here is that a branded search by this definition is not necessarily just your brand — for example, “Microsoft.” It is any term for which you are the clear and obvious option — a good example is terms like “Windows” (for Microsoft). My colleague Dr Pete has written up a bunch of industry-level explorations around this idea, for example, with OpenAI and automotive brands .

As you might then guess, this is also exactly how we think about brands within Brand Authority.

Of course, the overwhelming takeaway here is the one you probably already knew — SEOs are still sleeping on brand as a ranking factor, as an SEO strategy, and as a metric. If anything, in the light of AI-polluted SERPs and recent HCU and Core updates, Google seems to be leaning into this even more. Many SEOs are nostalgic for the era when you could win big in organic search without a brand, but I’m afraid the writing has been on the wall for a long time.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

Thinking of pitching for MozCon New York 2026? Learn how to create a standout speaker pitch, discover hot topics organizers love, and boost your chances of taking the stage.

When you're set up for success, being a mentor can be a rewarding experience for you and your mentee. Miracle’s in-depth framework presented in this week’s Whiteboard Friday covers considerations like building trust, setting boundaries, and the qualities that make a great mentor.

Wondering how the latest news around the Google Antitrust ruling will impact search and SEO? Dr. Pete breaks down the final Google antitrust remedies as determined by the court and how this landmark ruling will reshape search and SEO over the next five years.
