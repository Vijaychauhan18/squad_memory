---
source: https://www.searchpilot.com/resources/blog/gpt-3-for-seo
title: GPT-3 computer
scraped: 2026-03-22
published_on: 2023-08-07T11:53:19+01
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# GPT-3 computer

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/gpt-3-for-seo
Published: 2023-08-07T11:53:19+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
In my opinion, the latest machine learning models such as GPT-3 can now create useful content that is worth testing for SEO and user benefits.

## Extracted Body
It has been hard to miss the buzz around the latest natural language generation (NLG) capabilities recently, as the OpenAI group released machine learning models trained on ever-larger amounts of written content. This has culminated, at the time of writing, in the beta release of an API to GPT-3 .

In my opinion, the latest ML models can now create useful content that is worth testing for SEO and user benefits. [Don’t believe me? Jump to an example ]

This will primarily benefit large websites right now partly because those are the only places where it is going to be possible to run statistically-significant tests on something as variable as content quality, and partly because the current NLG capabilities are useful only at scale. If you are producing 5 pages of content, you are better to have a human write them; GPT-3 doesn’t outperform humans on individual outputs, but rather its benefits come in speed and scale.

Coming at this from an SEO perspective, it is easy to see that if we had access to a tool that could instantly produce thousands of short chunks of quality text tuned to different styles, lengths, or tones of voice, it would be powerful. It would let us generate content at scale for such things as:

And the really interesting thing is that we wouldn’t just be able to do it once, we would be able to regenerate variations for testing to find the right combination of settings that created a tone and style that was highly appealing to human users while also being relevant, on-topic, and compelling enough to rank well in organic search.

As someone who spends a lot of time thinking about SEO A/B testing , and getting stymied on too many content experiments by the cost of production, this is compelling and exciting.

There are some wonderful demos of the incredible capability of GPT-3 to produce all kinds of surprising outputs - not just what you might think of as written textual content. For our purposes, however, most of the interesting uses are short passages of text ranging in length from a single line to a short paragraph or two.

Out of the box, with no fine-tuning, the model is capable of tasks like generating category page copy. Show it two examples of human-written category page copy along with the title tags of those two pages, and it can write new category page copy when prompted with a title tag it hasn’t seen before. In the following example, I gave it the first two examples and the third prompt, and it completed the section in bold :

Title: Men’s Running Shoes | adidas UK | Order Now Copy: From start to finish, adidas' men’s running shoes are a success story that you can depend on. Benefit from advanced running technologies for enhanced performance, whilst also looking stylish and feeling comfortable when you’re on the run.

Title: Mens adidas Football Boots | adidas UK Copy: The adidas range of men’s football boots is both the outcome and the evidence of our rich connection with the beautiful game. Don’t compromise, opt for the best boots that money can buy, and see why some of the world’s top goalscorers wear adidas.

Title: Men’s Basketball Shoes | adidas UK Copy: The adidas range of men’s basketball shoes is the perfect blend of style and performance. Benefit from the latest technologies and innovations, whilst also looking the part on the court.

Notice that the human-written copy for the football boots mentions “the beautiful game” and “goalscorers” which are contextually relevant to football boots as opposed to any other kind of footwear, and notice that GPT-3 says “on the court” about basketball shoes. It may not be the best copy ever written, but it is grammatically correct, highly relevant, and written with no human input whatsoever.

Note : I’m not working with Adidas - this is just an example taken from their public website at random, but I happened to like it because the running shoes and football boots category pages had copy and the basketball shoes one did not.

I mentioned that this is the model with no fine-tuning at all. If you already have a lot of written content adhering to your brand voice and guidelines, for example, it is possible to fine-tune the GPT-3 model with text to teach it style, or if you have a knowledge-base of FAQs, you could teach it domain-specific knowledge.

The idea of using machine learning models to produce written content and go a step beyond the classic boilerplate / templated content common on so many large sites has been bouncing around in my head for a while and I’m not the only one. Mike King just wrote about the capabilities of GPT-3’s little sibling GPT-2 which can create basic copy given structured input . The thing that blew me away about GPT-3 in comparison was that we didn’t need to pull any structured data, set up our own boilerplate, or do any more than literally show the model that we wanted to expand title tags into category copy and it did it on the first attempt.

Obviously I should caveat this with my belief that we should be testing as much as we can to be truly effective and accountable in SEO. NLG content is an area where I believe it is especially important though.

Part of the reason for testing when working with NLG is that large websites will want to stay on the right side of Google, and I believe that full funnel testing in particular is the most defensible way of ensuring that we are rolling out enhancements to our site that do that. Testing for SEO impact and for users makes sure that our changes are appreciated not only by Google’s algorithm as it is right now, but also makes sure that they are aligned with what Google wants their algorithm to achieve - which is serving the results users want to see. I’ll go into a little more depth on Google’s view on NLG ( it’s complicated ), but testing against the current Google algorithm and user preferences gives us maximum confidence in our content.

Perhaps more strategically important is that enabling new kinds of testing is where NLG really shines. If SEO testing has taught us one thing, it’s that it is surprisingly hard to predict which changes will have the biggest impact (or, sometimes, even which ones will be positive). Despite this clear need for more testing, testing content changes has been difficult up to this point because of the cost of writing and rewriting the volume of output required. (You can read one of our content testing case studies here , and we have on occasion had extremely good results e.g. a 20+% uplift from the inclusion of a single line of templated copy on sparse category pages, but we see each of these more as “testing this particular copy” rather than “testing all possible kinds of copy” or “testing this kind of copy in every situation / on every website”).

GPT-3 provides an opportunity we haven’t previously had to test hypotheses like:

The unique strength of the models at the time of writing is not that they are better than humans at writing, but that they are fast and cheap and so we can iterate and test in ways that aren’t feasible with human writers. Crucially, we may be approaching a point where we can’t assume that content written by computers is less valuable to users than content written by humans. There will always be low quality content (created by either!) but soon there could be high quality content created by both as well.

At the time of writing, Google’s Quality Guidelines say [emphasis mine]:

Automatically generated—or “auto-generated”—content is content that’s been generated programmatically. In cases where it is intended to manipulate search rankings and not help users, Google may take actions on such content. These include, but are not limited to:

I think there are multiple different ways of reading this forensically:

From first principles, and public statements from Googlers, I’m inclined to focus more on the intent and whether there is a benefit for the end user than in a forensic reading of the guidelines.

In 2017, Gary Ilyes was questioned about whether ML tools were against the guidelines and he gave a cryptic response that they were “thinking about this a lot” but gave no hint to what those thoughts were. Then, on a webmaster hangout in late 2019 , John Mueller said:

“I think at some point in the future, we will have to revisit this guideline and find a way to make it a little bit more granular and that it kind of differentiates between these totally spammy uses of auto-generated content and the actually pretty useful uses of automatically generated content.”

This fits with my mental model for how Google thinks about these guidelines and their evolution - which is very user-centric. If users like the content, then Google is ultimately going to want to enable and allow that content to rank. I don’t see any theoretical reason to keep high quality content out of the search results regardless of its origin.

In practical terms, this is why I would approach any tests of this kind of content as full funnel tests where you measured the impact on users and on search performance.

I won’t hold my breath for the published guidelines to change though: I remember meeting with a developer advocate at Google’s London HQ in 2008 or 2009 and discussing Google Translate (released a year or two earlier) and how proud of it they were.

Me: “So, can we put Google Translated content on our website and let it be indexed then?”

Googler: “Haha. You shouldn’t do that, because we can detect our own translations with a high degree of confidence and you’ll get penalised.”

Me: “But if the quality of the translation is good enough for users of Google Translate, why isn’t it good enough for searchers?”

He did say that in theory it should be ok if the quality was high enough, but that it remained against current guidelines. Those guidelines are still in place over a decade later despite a many-fold improvement in translation quality .

Although I haven’t pushed the boundaries of what it’s capable of, it appears to me as though there are some key areas that GPT-3 (and other NLG programs) cannot support yet:

But it’s improving quickly and we should anticipate having to revisit our expectations of what kind of creativity computers are capable of a lot in the coming months and years.

The three areas of SEO that I most want to test right now, that I think could potentially bring real rewards with technology capabilities that are available already, are:

If you are interested in testing your own SEO hypotheses, get in touch or request a demo of the SearchPilot platform . If you just want to discuss all the exciting things machine learning can help computers do, hit me up on Twitter @willcritchlow .

Finally, if you want to be the first to hear when we publish new case studies, sign up to our email list here .
