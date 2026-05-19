---
source: https://moz.com/blog/user-signals-as-a-ranking-factor
title: User Signals as a Ranking Factor & US vs. Google
scraped: 2026-03-23
published_on: 2023-12-19
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

# User Signals as a Ranking Factor & US vs. Google

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/user-signals-as-a-ranking-factor
Published: 2023-12-19
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Explore the debate of whether or not user signals are a ranking factor in this article with Tom Capper.

## Extracted Body
Some of you may be familiar with the ongoing US vs. Google antitrust case in the USA. In this piece, I want to give a broad overview of what this is about and what it means for SEO, as well as how it has surprisingly rekindled, maybe even confirmed some long-standing SEO conspiracy theories.

US vs. Google is an antitrust case by the US Department of Justice against Google. This is likely to be a historic case — for example, a similar case in the past concerning Microsoft abusing its operating system monopoly in the browser space famously resulted in Microsoft having to make it easier for users to choose alternative browsers to Internet Explorer.

Much of the mainstream coverage so far, and also Google’s own public response — “people use Google because it’s useful” — is centered on the analogous case of search engine choice on both Android and iOS. Particular attention has been given to their deal with Apple, which gives them huge market share and the advantages that come with that (like unique quantities of user data). This part of the case is relatively simple to understand from an SEO or layperson’s perspective because we all experience search engines and our own experience of ending up using Google over alternatives. That said, what would count as anti-competitive vs. reasonable business dealing here is not intuitive to a non-lawyer like myself.

The DoJ, however, judging by their press release , is at least as interested in a different part of the case — Google’s vertical advertising monopoly, which is more arcane in that it relates to various platforms that lay people have likely never heard of. On the other hand, this is a traditional case of a company with a monopoly in one area (search) arguably gaining unfair advantages in other areas (advertising), like Microsoft and browsers, without the added complexity of a third party like Apple.

The default search engine issue is a little more obviously relevant from an SEO perspective. What if Google stopped being the default search engine on Apple or even Android devices? Well, it’s already not the default on Microsoft devices, and we know how that goes. I don’t know about you, but the first thing I do on a fresh Windows install is get rid of the built-in Bing search bar and download Firefox and/or Chrome. Then again, Apple has been making serious moves in the search space, so perhaps they could be a more credible second player here than Bing. Having to optimize for two search engines would likely complicate the work of SEOs, especially if Apple’s search engine is more app-centric. If users liked what they got with Apple, this could even impact the value of websites themselves, as opposed to apps.

A shake-up of Google’s ad platforms, presumably separating the three levels above or perhaps forcing Google to allow other ad vendors to sell ads on Google search results pages, would have mostly second-order effects on SEO. Perhaps organic search is more important in a world where paid search is more complex. Or is it less important in a world where paid search is more competitive? It’s hard to say which is more likely at this stage. Similarly, many websites that compete in organic search are funded by display ads — what happens if that is disrupted? Or boosted?

One of the supposed advantages of Google’s monopoly position, which it has been allegedly abusing, is the user interaction data from its own search results. This will be of great interest to many SEOs. There is a longstanding hypothesis that Google is using interaction data from its own SERPs to inform and improve rankings. For example, perhaps if you are in position two but everyone scrolls past position one to click on you, that means you deserve to be in position one. Or, perhaps if everyone who clicks through to your site immediately hits the back button and chooses a different result, that means you shouldn’t rank here.

Many SEOs (myself included) have strongly believed that this is happening in at least some form (more on that later) for some time. You can see this Whiteboard Friday from Cyrus a couple of years ago or real-world experiments from Rand from many years ago. Back in 2018, I also touched on the theory a couple of times on the Distilled blog — one of those pieces lives on here , and another has been taken down, but I’ve reuploaded it here . Below is a screenshot of the relevant section from the original article:

On the other hand, as that screenshot shows, Google themselves always denied this to a greater or lesser extent, sometimes at point blank, sometimes on slight technicalities like John above. Many SEOs treat Google’s word as absolute gospel on such topics, and indeed, I have been publicly pilloried on Twitter and elsewhere for taking their line with a pinch of salt in the past.

With all of the above in mind, it’s easy to see why many SEOs got excited about this piece of evidence back in September from Eric Lehman, a former Google engineer.

“Pretty much everyone knows we’re using clicks in rankings. That’s the debate: ‘Why are you trying to obscure this issue if everyone knows?'” he went on to say. Ouch.

Another exhibit, the 2016 Search All Hands presentation, includes this remarkable slide:

“If a document gets a positive reaction, we figure it is good. If the reaction is negative, it is probably bad.”, the speaker notes go on to say.

And on this next slide, “...if you search right now… your responses will benefit people who come after you.” Other documents go on to discuss specific signals measured — attention, clicks, scrolls, query refinement. All stuff that many of us have suggested for many years…

Of course, it’s tempting for slightly conspiratorial SEOs such as myself to take a quick victory lap here, but unfortunately, it may not be as clear-cut as it initially appears.

There are a few different levels of possible user data integration in the algorithm. Roughly from least to most:

There is no user data integration in Google algorithm whatsoever.

Some historical user data is used as a training set for traditional ranking factors like links or semantic relevance. See also: Panda .

Live user data is periodically refreshed for re-training of the algorithm.

Core updates incorporate fresh user data automatically into the algorithm.

The algorithm responds in real-time to user data (as suggested by Rand’s experiments referenced above).

These quotes from Eric Lehman (and, at this point, a bunch of other Google evidence) are arguably compatible with any of these except (1). That said, if user data was only ever training data, especially historical training data, why the concern that SEOs would attempt to mess with it? So, I tend to think 3+ is implied here, and that last Search All Hands slide above appears to agree with me.

Adding further nuance fuel to the caveat dumpster fire, Lehman also suggested in an email in 2018 that “Huge amounts of user feedback can be largely replaced by unsupervised learning of raw text.” The context here is important — Lehman was theorizing about how competitors might catch up to Google’s lead. So this is not suggesting that Google would abandon user data, but rather that there might be a (second rate?) substitution available to their rivals.

Roughly at the same time as this revelation, Gary Illyes was busy revealing to PubCon that links are “no longer a top three ranking signal.” This is almost certainly a coincidence in terms of timing, but it does beg the question — if not links, then what? User signals? Brand? Potentially, this is also another “please stop trying to manipulate this signal” game, so who knows!

Yes, probably. Slightly more probably than before. I hope that helps.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
