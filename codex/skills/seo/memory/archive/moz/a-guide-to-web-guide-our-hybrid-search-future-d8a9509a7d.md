---
source: https://moz.com/blog/guide-to-web-guide
title: A Guide to Web Guide: Our Hybrid Search Future
scraped: 2026-03-22
published_on: 2025-12-16
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

# A Guide to Web Guide: Our Hybrid Search Future

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/guide-to-web-guide
Published: 2025-12-16
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Is Google Web Guide the future of search? Dr. Pete analyzes Google's new hybrid search interface, breaking down the 10 types of "query fan-out" that drive results and explains why search marketers need to prepare for a more conversational search style.

## Extracted Body
To read the industry news, you’d think that Google search was hurtling toward an all-AI future, but the reality is that most search (even AI Mode ) is a hybrid of AI/LLMs — specifically, Gemini — and the core organic search algorithms Google has been refining for over two decades. Google Web Guide (currently in beta) gives us a glimpse of what that hybrid search future might look like. On the surface, it looks a lot like traditional search, but it’s powered by multiple AI layers, including complex query fan-out.

Google Web Guide is a hybrid search result that was introduced in Google Labs in late July of 2025. It combines Google’s organic search results with AI (Gemini) features, using query fan-out to surface sub-topics and additional results. If you haven’t seen a Google Web Guide result, here’s a partial screenshot:

1. Organic results (FastSearch) I was recently looking to replace some failing hardware (ok, I was also eyeing Cyber Monday deals), so let’s dig into a Web Guide result for “wireless gaming mice.”

At the top of this result, you’ll see something that looks very familiar:

These results look organic because they (mostly) are organic. Note the button to show “quick matches” – these results come from Google’s FastSearch technology, which is based on RankEmbed and uses core technology similar to regular search, but is designed to be faster and more efficient. FastSearch is also used for grounding Gemini.

2. AI/LLM summary Under those mostly-organic results (usually, two of them), we get the “Web Guide” header and an AI-generated summary. This summary seems to be for all results, although the example below is focused on a couple of specific products (note the highlighting):

Next, the real fun begins. This is where query fan-out kicks in …

3. Subtopic fan-outs Query fan-out was introduced with AI Mode back in May. It attempts to break a query down into subtopics and follow-ups to get a broader snapshot of what a searcher might want. Fan-out queries happen behind the scenes in AI Mode and AI Overviews , but Web Guide surfaces them indirectly.

After the Web Guide summary, we see blocks of organic results. Each block has a header and description, followed by up to four (currently) visible results, like this one:

Each of these sections is the product of a query fan-out. Although the fan-out itself isn’t displayed, Web Guide generates the fan-out queries, runs the fan-out searches, ranks the most relevant results for each fan-out, and then summarizes those results. The headers aren’t the fan-outs, as far as we know, but they are the end result of the fan-outs.

Here’s a list of all of the subtopic/fan-out headers on this result:

Note that the number of fan-out sections on any given result has varied quite a bit during testing (and across queries). In a moment, we’ll get into how we think the query fan-out process works, based on observed Web Guide results.

AI and Gemini are also working in less obvious ways within Web Guide. Look at the following search snippet:

This text isn’t the page’s Meta Description , and it’s not lifted directly from the content. It’s a summary based on the perceived intent of the searcher , which explains how the page serves that intent. In other words, instead of just summarizing the page, Google/Gemini is trying to tell you why it thinks that page is relevant.

Here’s another example, from a forum, that pulls out a relevant quote:

Arguably, this is good for searchers and can lead to more relevant clicks. As search marketers, however, this is another evolution of search that forces us to let go of control of our content and look at the bigger picture of what a searcher might want.

Putting it all back together, here’s a visual summary of a Web Guide result:

Web Guide certainly feels a lot more organic than AI Mode, but the reality is a bit more complicated. Let’s talk about what’s happening behind the scenes.

When Google launched AI Mode, Liz Reed (VP & Head of Google Search), wrote that:

AI Mode uses our query fan-out technique, breaking down your question into subtopics and issuing a multitude of queries simultaneously on your behalf. This enables Search to dive deeper into the web than a traditional search on Google ...

While “multitude” may be an exaggeration, AI Mode visually confirmed that Google ran additional searches and analyzed multiple SERPs (this message seems to be gone now). Typically, this was in the ballpark of a half-dozen searches. For example:

When Web Guide launched in Google Labs, Justin Wu (Group Product Manager, Search) also confirmed the use of query fan-out in Web Guide results, saying:

Similar to AI Mode, Web Guide uses a query fan-out technique, concurrently issuing multiple related searches to identify the most relevant results.

Beyond some insight from patents , though, Google has revealed very little about how query fan-out works or what types of fan-outs they typically use.

This is the question we’ve been exploring at Moz over the past few months. Based on Web Guide headers, could we start to piece together the types of query fan-outs Google might be performing and generate our own fan-out queries?

Using observed headers, we set out to understand how the fan-out process might operate. This involved a fair bit of deduction, and the end result isn’t a model of exactly how Google works, so much as a framework for understanding the broader process.

Our research eventually settled on a 10 fan-out taxonomy, illustrated below:

These 10 fan-out types are loosely organized as a journey. What is the searcher trying to achieve, and what are the steps they might take along that journey toward an eventual action? Let’s dive into each one and look at some examples.

As we move toward this hybrid world, it can help to move away from traditional search queries and towards questions (or, in LLM lingo, “prompts”). So, all of the following examples are based on the question: “What are the best wireless mice for gamers?”

In an AI/LLM world, there are many ways to say roughly the same thing. Semantic fan-outs are queries or prompts with different words, but similar meaning. For example:

Entity fan-outs expand on an entity — a person, place, thing, or brand. For example:

Follow-up is probably self-explanatory — what is the searcher likely to ask next? The next two fan-out types are variations on follow-ups, but some general examples are:

An attribute fan-out is a follow-up focusing on a specific feature or attribute, such as:

What about the follow-up after the follow-up? Anticipate fan-outs look two or more steps ahead, sometimes even at post-transactional questions. For example:

The next three fan-out types dive into the informational intent space. Factual fan-outs focus on just that: facts, data, and specifics. For example:

Tutorial fan-outs dive deeper into a topic, such as how-to guides. The three informational fan-outs are strong candidates for content marketing. Examples include:

Perspective fan-outs focus on human perspectives and opinions, including discussions and forums, which Google leans on heavily. Some examples are:

The last two fan-out types move down the funnel toward an action or transaction. Comparison fan-outs compare two or more items or concepts. For example:

Finally, Transact fan-outs move into a clear commercial or transactional space. The searcher is ready to take an action, such as a purchase. Examples include:

Note that these 10 fan-out types aren’t exhaustive or mutually-exclusive. Our goal is to provide a framework to understand why and how fan-out happens, and illustrate how mapping fan-outs can help marketers better understand the searcher’s journey.

Let’s revisit our earlier visual map and plug in some of the examples we’ve covered:

Here’s the good news — hybrid search is at least partially organic, and Web Guide leans heavily on core Google search algorithms. Moving toward a hybrid future, here are three things that we have to keep in mind:

1. Search is a conversation Whether it’s refining a query and clicking on results or a literal back-and-forth with an LLM, search is a conversation. Natural language is our default mode as humans, and the shift toward conversational search has been happening for well over a decade.

2. We’re going to have to let go No matter how well you craft your content, headers, or meta descriptions, Google is going to summarize and interpret them more and more. Like you, I’m sometimes frustrated by this, but it’s important to focus on moving the searcher in a mutually beneficial direction, even if that means giving up on trying to control every step they take.

3. Ranking is going to get messy Hybrid search and Web Guide, in particular, still have rankings, but consider two things. First, if a given fan-out better serves the searcher’s needs, they might prefer that section of results. In other words, result #6 could be the most relevant if it’s the first result in a fan-out that most aligns with a searcher’s intent and needs. Two, and possibly more alarming, the results within any given fan-out are probably coming from the top organic rankings of that sub-query. In other words, result #7 could actually be result #1 or #2 on a different query. That means we’re going to have to compete on multiple sub-queries to rank on any given Web Guide results page.

You’ve probably heard marketers talking as if a Gemini-only, AI Mode future is inevitable. I think that’s extremely unlikely, for a lot of reasons, but let’s focus on the two big ones.

Even OpenAI has admitted that hallucinations are a feature of LLMs, not a bug. Search-grounding and retrieval-augmented generation (RAG) can help, but they don’t solve the underlying problem. LLMs are probabilistic language simulators, and they have many limitations.

Even without hallucinations, LLMs are poorly suited to some tasks, such as navigational and local searches. So, you already see Google adding links and features to AI Mode, essentially turning it into a hybrid search result.
