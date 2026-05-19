---
source: https://dejan.ai/blog/how-long-are-web-pages/
title: How Long Are Web Pages?
scraped: 2026-03-25
published_on: 2025-12-14
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

# How Long Are Web Pages?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/how-long-are-web-pages/
Published: 2025-12-14
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
A Token Count Analysis of 45,000 Real-World URLs We recently analyzed 44,684 web pages and measured their content length using Gemini’s token counter. The results reveal fascinating insights about the true scale of web content—and why it matters for AI applications. Metric Value Total Pages Analyzed 44,684 Page Content Tokens 464,854,727 Total Tokens (all) 541,062,817 The median […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

We recently analyzed 44,684 web pages and measured their content length using Gemini’s token counter. The results reveal fascinating insights about the true scale of web content—and why it matters for AI applications.

The median web page contains roughly 3,200 tokens —equivalent to about 2,400 words or approximately 5 pages of text. However, the average is significantly higher at 10,400 tokens, indicating a strong right-skew from lengthy documents.

Half of all web pages fall between 1,000 and 5,000 tokens. This represents the “typical” article, blog post, or informational page.

Nearly 1 in 5 pages (18%) contain between 10,000 and 50,000 tokens—these are longer articles, comprehensive guides, or pages with significant supplementary content.

The top 1% of pages exceed 140,000 tokens —roughly 100+ pages of text. These are typically:

The largest page in our dataset contained over 3 million tokens —equivalent to approximately 4-5 full-length novels.

With major LLMs offering context windows from 32K to 2M tokens, our findings suggest:

While the typical page sits around 3,000 tokens, the distribution has a remarkably long tail. AI systems consuming web content need to account for this variance—both for context management and cost optimization.

Before publishing this analysis, I ran a poll on LinkedIn asking people to predict the average page size in tokens:

131 people voted. The most popular answer was 1,000 tokens (38%), followed closely by 10,000 tokens (34%). The actual answer? 10,403 tokens on average.

Only a third of respondents got it right. The majority underestimated—perhaps expecting a page of text to be shorter than it actually is when tokenized. What’s interesting is that the median (3,201 tokens) would have made “1,000” a more defensible answer, but averages get skewed heavily by those outlier documents.

The 7% who guessed 100,000 weren’t entirely wrong either—they just described the 99th percentile rather than the average.

The more I learn from your research studies, the less I think OpenAI can win (I’m saying this with $ on the table)

Thank you for doing both median, mode, and explaining those edge cases.

It’s funny how the outlier data you see in school – the ones you’d throw out – are in practice the hard problems that tell you what organizations are shooting to be that 99th percentile…

Because when you operate in the trillions, your errors are in the millions.

It’ll be very interesting to see what comes next on the web now that machine translations become more acceptable. Will we see model collapse or will there finally be better multilingual results and answers?

Thank you for sharing the kind of 99th percentile work as well.

Yeah those million token URLs really broke my pipeline and I was wondering if there was bug in my code, spent days trying to figure it out and then I LOOKED AT THE DATA and was like… oh…..

I wonder if cost is the same always or maybe the initial chunking cost more but – as long as they don’t want to rerank the answer – it doesn’t cost at all.

I’d say their chunking pipeline is the most efficient one on the planet and would love to get my hands on it 🙂

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
