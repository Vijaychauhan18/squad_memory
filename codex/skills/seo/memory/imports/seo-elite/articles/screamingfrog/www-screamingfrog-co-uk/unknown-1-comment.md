---
source: https://www.screamingfrog.co.uk/blog/generate-markdown-at-scale/#comments
title: Using the Screaming Frog SEO Spider to Generate Markdown at Scale
scraped: 2026-05-15
tags: elite_article, seo, screamingfrog, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# Using the Screaming Frog SEO Spider to Generate Markdown at Scale

Source expert/publication: screamingfrog
Source homepage: https://www.screamingfrog.co.uk/blog/
Original URL: https://www.screamingfrog.co.uk/blog/generate-markdown-at-scale/#comments
Published: unknown

## Why This Matters
SEO & search marketing news and chatter from Screaming Frog.

## Extracted Article Passages
- LLMs, RAG pipelines and various AI-powered tools are now a regular part of a lot of SEOs’ workflows, and a common starting point for many of them is getting content out of web pages and into a clean, usable format at scale.
- Markdown has emerged as the format of choice for most of these use cases. It’s lightweight, preserves the structure of the page, and is well understood by virtually every LLM out there. The challenge is that web pages are full of stuff you don’t want to carry across with the content. Navigation, cookie banners, ads, sidebars and footers are just a few examples, and stripping them out manually on every page is obviously not going to fly if you’re working with thousands of URLs.
- Thankfully, the Screaming Frog SEO Spider can handle this for you using its Custom JavaScript feature. In this guide, we’ll walk through two methods for generating markdown of every page on a site during a crawl, and we’ll share a Python script that takes the SEO Spider’s CSV export and turns it into individual .md files for use downstream.
- Before getting into the how, it’s worth briefly covering why this format has become such a common choice within AI workflows.
- There are a fair few use cases for content in this format. You might be building a knowledge base for a chatbot on a client’s site, preparing training data for fine-tuning, running competitor analysis through an LLM, getting all examples of a writing style for creating new content, or keeping a clean plain-text archive of a site ahead of a migration. In all of these, getting to clean markdown is the first step.
- Before getting into the how-to, it’s worth flagging an ongoing debate around all of this. Some site owners have started experimenting with serving raw markdown files to LLM crawlers, either alongside their normal HTML or as a replacement, on the basis that it’s cheaper to serve and easier for a bot to parse. Cloudflare even have a one-button solution that automatically converts your HTML to Markdown for requests from agents.
- This approach hasn’t necessarily been well received. Earlier this year, Google’s John Mueller called it “a stupid idea” on Bluesky, questioning whether LLM crawlers even recognise a .md file as anything other than a plain text blob.
- It’s a fair concern, and we’d largely agree with it. Maintaining a parallel, machine-facing version of your site introduces problems around trust and verification (how does a crawler know the markdown matches what a user would actually see?) as well as the ongoing cost of keeping the two versions in sync.
- That’s not what this guide is about though. We’re covering the opposite use case: extracting content that already exists on a site into clean markdown, for use in downstream tooling. Think RAG pipelines over your own content, content audits, training data preparation, migration archives or competitor analysis. A one-off or periodic extraction for a specific purpose, not a live feed served to crawlers.
- We’ve got two different methods to cover, and both make use of the SEO Spider’s Custom JavaScript feature. We’d recommend starting with the first one, as it requires no configuration and works well on the vast majority of sites. If it misses the mark on something, the second method gives you more control over what’s being extracted.
- Both methods require JavaScript rendering to be enabled in the SEO Spider (Configuration > Spider > Rendering > JavaScript), since the Custom JavaScript feature runs against a fully rendered page.
- Put them together and you’ve got a full HTML-to-markdown pipeline that runs within the SEO Spider’s rendering process. Readability figures out where the content is, and Turndown formats it. There’s nothing to configure per site, and no maintenance to worry about when a site redesigns.
- Head over to Configuration > Custom > Custom JavaScript in the SEO Spider, and click ‘Add’ to create a new snippet. Give it a sensible name (‘Page Markdown’ works), and paste in the following:
- There’s a bit more going on here than just the core Readability-and-Turndown steps, so it’s worth briefly walking through what the snippet does:
- With JavaScript rendering enabled and the snippet saved, go ahead and start your crawl as normal. Once it’s underway, click over to the Custom JavaScript tab and you’ll see a new column for the snippet, containing the generated markdown for each page.
- If you’re working with a clean URL structure, consider leveraging the Include feature, for example:

## Retrieval Use
- Use when the task maps to `screamingfrog` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

