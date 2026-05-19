---
source: https://dejan.ai/blog/ai-seo-deep-dive-tom-critchlow-dan-petrovic/
title: AI SEO Deep Dive
scraped: 2026-03-25
published_on: 2025-11-19
tags: live_feed, phase1_ingest, dejan, practitioner, reverse-engineering, grounding, archive_backfill, historical_source
topic: ai_reverse_engineering
intent: research, monitoring, source_selection, ai_selection
role: researcher, seo, pinchy
confidence: high
canonical: false
canonical_group: Archive backfill - DEJAN / Dan Petrovic
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# AI SEO Deep Dive

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/ai-seo-deep-dive-tom-critchlow-dan-petrovic/
Published: 2025-11-19
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
I recently sat down with strategic SEO consultant Tom Critchlow for a deep-dive conversation about the mechanics of AI Search. We moved past the usual LinkedIn hype and “get-rich-quick” prompt engineering advice to look under the hood of Large Language Models (LLMs) like Gemini and GPT. We explored a fundamental shift in AI SEO industry: moving from Click-Through […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

I recently sat down with strategic SEO consultant Tom Critchlow for a deep-dive conversation about the mechanics of AI Search. We moved past the usual LinkedIn hype and “get-rich-quick” prompt engineering advice to look under the hood of Large Language Models (LLMs) like Gemini and GPT.

We explored a fundamental shift in AI SEO industry: moving from Click-Through Rate (CTR) to Selection Rate Optimization (SRO) .

If you are still tracking a list of static prompts to measure your AI visibility, you are looking at the wrong metrics. Here is the technical reality of how Google’s AI works, and how we can actually influence it.

To understand how to optimize for AI, we first have to admit a hard truth: Nobody fully knows why these models do what they do. Not Google, not Anthropic, not the team behind Grok.

These systems have moved from “Small Language Models” (like BERT) to massive parameter counts where reasoning capabilities are emergent properties. Because we cannot open up Gemini and look at the weights (as we might with an open-source model like Gemma), we have to rely on Mechanistic Interpretability .

In SEO terms, this means “poking the stick” at the model. We probe it to see what activates it. We are trying to understand the model’s psychology and biases to predict its behavior.

When a user asks a complex question in AI Overviews, the model doesn’t just hallucinate an answer. It performs Grounding (RAG) .

Crucial distinction: Google tends to ground a single fact with multiple sources, whereas OpenAI often maps one fact to one URL.

What does the model actually see? It doesn’t see your beautiful CSS or your schema markup in its raw form. It sees text, markdown, and occasionally raw HTML elements like <b> tags or <div> structures. If your content relies on the rest of the page to make sense, you will lose.

Many SaaS tools are selling “AI Rank Tracking” where they monitor a specific prompt daily. I disagree with this approach. It’s busy work.

LLMs are probabilistic. They use sampling and temperature settings that ensure if you ask the same question twice, you might get different answers.

Instead of tracking rankings, we need to measure Brand Saliency and Primary Bias .

We can map these probabilities to build a graph of what the AI “thinks” your brand is. We can then ask the model: “Would you recommend [Brand] for [Service]?” and measure the probability of the token “Yes” appearing.

This isn’t a ranking. It is a confidence score . It tells us the model’s inherent bias toward your brand for a specific intent.

If we can’t trust static rankings, we must look at Consideration Sets .

Through Citation Mining , we can see which URLs the model browsed but rejected, and which URLs it selected for the final answer.

When we analyzed the data, we found that Google prefers certain domains repeatedly for specific topics. By analyzing the Grounding Snippets (the exact chunks of text the model used), we can reverse-engineer what the model finds attractive.

Is it the formatting? The density of information? The directness of the answer? Once we know the “Look-Alike” content Google prefers, we can optimize our own pages to match that pattern.

This leads us to the most important concept of the new era: Selection Rate Optimization.

In the past, we optimized for clicks (CTR). Now, we optimize for Selection . We want our content to be the “irresistible” chunk that the model must use to answer the user’s query.

This allows us to iterate at lightning speed. We aren’t waiting for Google to crawl and index; we are simulating the AI’s choice mechanism to find the perfect content structure.

Two specific tactics emerged from our conversation that you can apply today:

Because Google grabs “chunks” of your page rather than the whole thing, every section of your content must stand on its own.

If you say “It is highly efficient” in a paragraph, and the model extracts just that paragraph, it doesn’t know what “It” refers to. You must explicitly name your product or service in every logical chunk. We call this Semantic Compression —ensuring the context travels with the snippet.

We found that internal links within your content maximize the chance of Google generating a literal hyperlink in the AI answer.

But you can’t just stuff links anywhere. The model learns from the web (sites like TechCrunch, Wired, etc.) where links naturally occur.

I trained a model called LinkBERT to predict the most probable location for a link within a sentence. By placing your internal links exactly where the model expects them to be, you increase the likelihood of that link surviving the generation process and appearing in the final AI Overview.

Technical SEO, content creation, and authority building are the backbone and the “memory” of these models. AI is simply the presentation layer .

To win in this layer, we must stop treating Google like a static database and start treating it like a probabilistic engine. We must understand its biases, analyze its selection criteria, and optimize our selection rate.

Great read! Which Selection model is preferable in the SRO pipeline?

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
