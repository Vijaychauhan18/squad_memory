---
source: https://www.oncrawl.com/ai/what-ai-bots-really-doing-your-site/
title: What AI bots are really doing on your site
scraped: 2026-04-28
tags: elite_article, seo, oncrawl, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# What AI bots are really doing on your site

Source expert/publication: oncrawl
Source homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/ai/what-ai-bots-really-doing-your-site/
Published: 2026-04-28

## Why This Matters
At SMX Paris 2026, Maxime Guernion (Head of SEO at Havas Market) and I discussed AI crawling from the perspective of understanding what AI does with your content, noting that your data isn’t really yours anymore. I’ve been seeing this trend emerge in log files over the past few m

## Extracted Article Passages
- At SMX Paris 2026, Maxime Guernion (Head of SEO at Havas Market) and I discussed AI crawling from the perspective of understanding what AI does with your content, noting that your data isn’t really yours anymore.
- I’ve been seeing this trend emerge in log files over the past few months. For over 15 years, I’ve been analyzing server logs: billions of lines. Googlebot, Bingbot, and all their cousins. Every visit to a URL leaves a footprint on the server, revealing what search engines actually do on a site, far from what they claim to do.
- Today, new players are showing up in the logs. GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, and a dozen others. They’re crawling on a massive scale, and most SEO teams don’t know exactly what they’re doing on their sites.
- The numbers speak for themselves: according to Cloudflare Radar data over the last 12 months (March 2025 -> March 2026), GPTBot and ClaudeBot account for 12% and 9.2% of global bot traffic, respectively. ClaudeBot is now on par with Bingbot, and all three are just behind Googlebot (48%). In the space of a year, AI bots have gone from being minor signals to major players in web crawling.
- Figure 1 — Distribution of bot traffic over 12 months: Googlebot 48%, GPTBot 12%, ClaudeBot 9.2%, Bingbot 9.2%. Source: Cloudflare Radar, worldwide.
- However, when I talk to SEO teams, even those with senior-level professionals, the conclusion is often the same: we know that AI crawlers are out there, but we don’t really know what they’re doing with the data. And above all, we don’t know what to make of it.
- This article is an attempt to clarify things: I share what I’ve observed in the field, with my clients, in logs, in robots.txt files, and in the sometimes erratic behavior of these new crawlers. The goal isn’t to scare anyone or sell a fantasy: it’s to lay the groundwork for understanding what’s actually happening.
- When people talk about “AI bots,” they often lump them all together, but that’s a mistake. Not all AI bots do the same thing, and confusing them can lead to poor decisions.
- By analyzing the documentation from the major market players and reviewing the logs of dozens of websites over the past 12 months, it becomes clear that there are four main types of LLM bots, each with very different functions.
- Their mission: to crawl web content to improve their models. GPTBot (OpenAI) and ClaudeBot (Anthropic) are the most well-known.
- They crawl on a large scale, often without any apparent logic for prioritizing content based on your site’s structure. OpenAI makes this clear in its documentation :
- “GPTBot is used to crawl content that may be used in training our generative AI foundation models.”
- These bots are more similar to what Googlebot does: they crawl to index and identify potential sources of answers for AI search engines.
- OAI-SearchBot (OpenAI), Claude-SearchBot (Anthropic), and PerplexityBot are among them. This is a fundamental distinction: blocking OAI-SearchBot in your robots.txt file could potentially cause your site to disappear from ChatGPT Search results. Blocking GPTBot means refusing to be used for training. These are not the same strategic choices.
- Moreover, Claude-SearchBot is fairly new, and many media sites that restrict these types of bots do not yet block it. It’s important to stay vigilant in order to detect these new agents and decide whether to restrict them (or not) early on. [Ebook] Mastering SEO in a query fan-out world Learn how query fan-out is reshaping SEO strategy. Get practical frameworks for building visibility in AI-powered search. Read the e-book Fetch bots (on-demand) ChatGPT-User, Claude-User, Perplexity-User: these bots retrieve data in real time, at a user’s request. When someone asks ChatGPT a question and the model needs up-to-date information, it sends ChatGPT-User to fetch the page.
- “Because these actions are initiated by a user, robots.txt rules may not apply.”

## Retrieval Use
- Use when the task maps to `oncrawl` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

