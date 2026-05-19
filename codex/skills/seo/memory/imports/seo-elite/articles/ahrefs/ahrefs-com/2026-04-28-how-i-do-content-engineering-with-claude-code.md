---
source: https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/
title: How I Do Content Engineering with Claude Code
scraped: 2026-04-28
tags: elite_article, seo, ahrefs, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# How I Do Content Engineering with Claude Code

Source expert/publication: ahrefs
Source homepage: https://ahrefs.com/blog/
Original URL: https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/
Published: 2026-04-28

## Why This Matters
Back in August 2025, I shared the AI content process I had developed for the Ahrefs blog. It used ChatGPT projects and custom GPTs to speed up certain types of content creation from several days to a couple of hours, … Read more ›

## Extracted Article Passages
- Back in August 2025, I shared the AI content process I had developed for the Ahrefs blog. It used ChatGPT projects and custom GPTs to speed up certain types of content creation from several days to a couple of hours, but still required tons of manual intervention.
- Now, barely eight months later, I’m sharing our new process. I use Claude Code and 23 custom skill files, chained together, to generate publish-ready article drafts in six to twelve minutes. We have published around 15 articles with this new process, and updated some 30 or so more.
- I’ve been using AI to help create content marketing since 2020. It has been useful in effortful, piecemeal ways. But today it is good enough to automate important parts of content marketing with no loss in quality (and even a significant gain in some areas, like research). Or as I put in a recent article: AI content wasn’t good enough. Now it is.
- As a result, I suggested a pretty bold direction in our company Slack, back in February:
- Check out this episode of the Ahrefs podcast to watch me demo our content automation system to Ahrefs’ CMO, Tim Soulo.
- Before we get to the good stuff, I once again want to direct your attention to some important caveats:
- AI content is not, by default, good. This process works well because it mirrors our existing human editorial process, built from decades of collective content marketing experience. Or as someone in a LinkedIn comment put it, very articulately:
- “Ryan’s SKILL files are good because Ryan already knew what to put in them. Most people using blank-slate tools don’t have 13 years of editorial experience to build from. The gap isn’t just in the tool. It’s in the person behind it too.”
- This process is geared specifically towards informational SEO content. I only use this process on topics that I understand well, so that I can review each article to validate its claims, correct misinformation, and make sure I feel happy putting it out into the world.
- I also focus primarily on topics that Ahrefs has already covered (in some capacity), allowing us to use hundreds of existing, high-quality articles as a reference point for new content.
- I could use this process to scale the Ahrefs blog to tens of thousands of articles. I will not. It would not be in the interests of Ahrefs or our customers.
- Instead, I am using this workflow to help us maintain an evergreen library of useful content on a handful of core topics. My goal is to remove drudgery and focus human grey matter on the parts of marketing that benefit most from it.
- At the heart of this process are ~23 skill files that correspond to different parts of the Ahrefs editorial process, from conducting keyword research to topic gap analysis to structural outlining:
- Each skill file includes a Markdown-formatted explanation of how Claude (or any LLM) should conduct each process, best-practice examples to emulate, and formatting instructions for the expected output.
- Many of these skills are adapted from our existing, human-written process documentation. Others are written from scratch, and some are generated and edited entirely by AI.
- Every skill can be used in isolation, but I also created a main skill ( blog-pipeline ) that instructs the LLM to trigger each of these skills in a particular order, working sequentially through every process to take a keyword idea through to (nearly) finished article:

## Retrieval Use
- Use when the task maps to `ahrefs` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

