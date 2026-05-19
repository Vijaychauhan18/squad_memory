---
source: https://moz.com/blog/llm-competitive-research-gap-analysis
title: How To Use LLMs for Competitive Research and Gap Analysis
scraped: 2026-03-22
published_on: 2025-03-04
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

# How To Use LLMs for Competitive Research and Gap Analysis

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/llm-competitive-research-gap-analysis
Published: 2025-03-04
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Raise your local SEO visibility with complete local SEO management.

## Extracted Body
Your content strategy is failing because it's built on guesswork.

Keyword research and a few Reddit threads might make you think you understand your audience, but you're missing the whole picture without comprehensive audience research.

If you decide to do manual audience research, it takes forever, and even with a full team, it’s easy to overlook key opportunities.

LLMs help you discover deeper audience insights and reveal how competitors meet audience needs you’ve missed.

In this post, I'll show you how to use LLMs to find audience insights, audit content, and identify high-impact content opportunities.

Understanding what your audience cares about is the foundation of any content strategy . AI can transform scattered data into actionable insights, pulling information from platforms where your audience spends time.

Here’s how I approach it, using the Pooch & Mutt site as an example.

Competitor websites reveal how your audience behaves and what content captures their attention. LLMs, like Microsoft Copilot and Google Gemini, simplify competitor research .

Open your chosen LLM and start with a basic prompt like: Tell me about poochandmutt.co.uk. The AI revealed that they specialize in functional dog food, targeting dogs with health issues. Their products use natural ingredients and are vet-approved, which helps me understand their unique selling points (USPs).

You could then get a basic understanding of a site’s consumer sentiment for further insight. I like using the Google Chrome Extension Instant Data Scraper for this step.

Go to the site’s main review platform, such as Trustpilot, and scrape the testimonials using the Instant Data Scraper Chrome extension to gather them at scale. Next, create a new Google sheet and add your scraped reviews/testimonials.

You can then feed that sheet to your LLM of choice and analyze their reviews/testimonials with targeted questions, including:

You can repeat these steps for competitor sites to gather unique insights about your competition. Make sure to review the output for accuracy, as LLMs can hallucinate.

Reddit offers unfiltered insights into what your audience cares about. LLMs can identify active subreddits and surface popular discussions.

For Pooch & Mutt, I used Google Gemini. With a clear understanding of the target audience, I asked:

"What subreddits are UK dog owners likely to discuss dog nutrition? Please research and give me back some real subreddits with the community size."

The output categorized subreddits into large, medium, and small communities, with descriptions for each. It hallucinated member counts, but the general estimations were useful. I’d focus on medium to smaller communities for better engagement. Then, cross-reference to confirm the subreddits exist.

A quick follow-up is asking Gemini: "Please export this into a spreadsheet." It generates a table with an Export to Sheets button, which is ideal if you use Google Workspace.

While the export can be messy (my sheet title ended up as "Please export this into a spreadsheet" ), it’s an easy way to build a database. Rename the sheet, append new findings, and you’ll quickly build a comprehensive list.

Next, scrape keywords from the gathered subreddits. Using the method in this Moz article by Amin Foroutan, you can build a custom keyword tool with Python and ChatGPT .

Pro Tip: Always cross-reference subreddits manually because LLMs sometimes suggest inactive or irrelevant communities.

Google Gemini can surface breaking news and trending topics, though its effectiveness depends on the industry. It works well for fast-moving sectors like tech or finance. For slower industries, like pet care, the results can be outdated.

For Pooch & Mutt, I used a simple prompt: "What’s the latest news about dog nutrition?" Gemini highlighted the XL Bully ban, which was accurate at the time but reflected older news. This is common in less active industries, so always cross-reference with reliable sources like Google News.

Gemini occasionally includes source links, but accuracy varies. This feature remains useful but imperfect until Google fully integrates real-time news into Gemini. Always verify findings before acting on them.

Google Discover offers a window into trending topics and content formats that resonate with your audience. Analyze Discover data from Google Search Console (GSC) to find patterns that inform your content strategy.

Start by exporting 12 months of Discover data from Google Search Console (GSC). It shows which pages earned visibility on Discover , helping you identify seasonal spikes, recurring topics, and content types that consistently perform well.

Go deeper with a crawler like Sitebulb to extract content from Discover URLs. It includes title tags, article content, publication dates, and metadata.

Once you have this dataset, stitch it to your GSC export using the following VLOOKUP formula in Google Sheets:

It creates a unified dataset, matching each Discover URL with its performance metrics.

Once you have your dataset, feed it into Google Discover GPT . The GPT highlights key themes, content characteristics, and performance insights from your Google Discover data.

For Pooch & Mutt, this analysis showed that how-to guides and step-by-step tutorials consistently outperformed listicles, especially when they were under 1,500 words and paired with concise, benefit-driven H1s .

Pro Tip : Use the User Persona Generator alongside Discover insights.

Combine Discover insights with audience data from the AI User Persona Generator. Feed it your URL or GA data to build detailed personas based on user engagement patterns. It ensures your content strategy aligns with actual audience interests.

AI SEO tools can optimize your title tags and H1s based on what performs best in Discover. I used a prompt like: " Based on my top-performing Discover content, suggest 10 title tag variations for my dog nutrition guides with high CTR ."

H1s under 60 characters with actionable language (“How to,” “Best,” “Guide to”) consistently performed better.

Before filling content gaps, you must understand what’s already on your site. AI content tools can automate content audits and theme tagging in Google Sheets.

Use Moz Site Crawl to extract all internal URLs. For Pooch & Mutt, I filtered the crawl to focus on blog and product pages, but you can adjust depending on your priorities. You can also use your sitemap to simplify the process​.

Once you have your URLs, import them into Google Sheets. Use the OpenAI API to apply the GPT formula, which assigns themes to each URL based on predefined categories.

To set it up, go to Extensions > Apps Script in Google Sheets and add the GPT script to Sheets using this video guide . Once installed, you can use ChatGPT in your sheets and add your prompts.

“Add your prompt here” — add what you would usually add in ChatGPT

For each URL, GPT categorized the content by predefined themes:

I used the formula below and optimized the prompt for accuracy.

You can copy the prompt's structure above, replacing your themes and example URL strings for more accurate categorization.

I prefer tagging by URL string using the formula =SPLIT(A2, "/") , but you could also tag by title tags or H1s if that better summarizes your page content​.

Each URL had a corresponding theme in the next column. The image above shows Pooch & Mutt’s blog URLs were categorized by theme, making it easy to identify content patterns​.

AI-generated tags aren’t perfect, so manual cleanup is essential. For Pooch & Mutt, GPT sometimes miscategorized content—like tagging a general dog health article as dog diarrhea.

Once you’ve tagged content, overlay Google Analytics (GA) conversion data by URL to reveal which themes drive the most traffic, conversions, and revenue.

Pro Tip : Always include an Other category. It catches content that doesn’t fit core themes and prevents disorganized outputs.
