---
source: https://moz.com/blog/ziff-davis-llm-study
title: Ziff Davis's Study Reveals That LLMs Favor High DA Websites
scraped: 2026-03-23
published_on: 2025-02-04
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

# Ziff Davis's Study Reveals That LLMs Favor High DA Websites

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/ziff-davis-llm-study
Published: 2025-02-04
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Discover the key findings from a Ziff Davis study on LLM training data and how it can help you improve your efforts to rank for generative search features.

## Extracted Body
For years, SEOs have relied on Domain Authority (DA) as a benchmark for assessing a website’s authority. While Moz has consistently stated that DA is not a Google ranking factor, the metric has remained a key point of discussion in the industry.

New research from Ziff Davis sheds more light on how Domain Authority correlates with LLM content preferences, suggesting that the future might not be so different from the present.

Ziff Davis , a major publisher with brands like PCMag, Mashable, IGN, and Moz, faces the same challenges as other media companies. They suspect that Large Language Models (LLMs) are training on their content without licensing agreements. Hence, it’s difficult to determine which content is being favored.

The study set out to address this issue. Researchers analyzed datasets like Common Crawl, C4, OpenWebText, and OpenWebText2 to understand how LLMs are trained, what types of content they prefer, and how these choices influence AI behavior and output.

If you want to skip the rest of the article, I’ve summarized the key findings below:

The Ziff Davis study examined four key datasets that are crucial in training large language models:

It’s important to note that these datasets aren’t created equal. More curated datasets, like OpenWebText and OpenWebText2, contain a higher proportion of authoritative content , while unfiltered sources like Common Crawl pull from a much wider but lower-quality pool of web pages. The difference in dataset impacts how LLMs learn and generate responses.

The study used Comscore’s web traffic to determine which publishers to analyze. Researchers focused on the top 15 portfolio publishers in the Media category as of August 2020, representing the most widely visited news and media organizations.

The selection process excluded single-property publishers, non-media tech firms, and user-generated content platforms in favor of more established commercial publishers.

The study used Moz’s Domain Authority (DA) to measure the influence and quality of web content in LLM training datasets. While DA is not a search ranking factor, it’s a recognized metric that predicts a website’s likelihood to rank in SERPs based on factors like backlinks, domain history, and site size​.

To analyze LLM content preferences, the study compiled Moz DA scores for all URLs found in Common Crawl, OpenWebText, OpenWebText2, and C4. The findings revealed a strong correlation between dataset curation and DA distribution. Meanwhile, uncurated datasets contained mostly low-DA sites, while curated datasets were heavily weighted toward high-DA publishers​.

The Ziff Davis study makes it clear that while these models may scrape everything indiscriminately, they place a higher weighting on curated datasets to prioritize quality.

Curation shapes how LLMs process and generate content. Raw datasets like Common Crawl pull from the open web with a mix of high and low-quality sources. In contrast, curated datasets like OpenWebText and OpenWebText2 filter out low-quality content to create a higher concentration of reliable information.

This intentional, selective process improves model accuracy, response quality, and content relevance. It also explains why high-authority websites dominate AI outputs.

LLMs don’t treat all web content equally. The Ziff Davis study confirms that high-DA commercial publishers dominate curated datasets.

We used a combination of Moz API and Google Collab to run a bulk DA analysis for all URLs featured in the study.

84.2% of analyzed publishers had an average DA of 60 or higher, showing a clear preference toward established media brands. As datasets become more curated, the proportion of high-DA content increases, with publishers like The New York Times and News Corp appearing more frequently.

Nothing is free in life, and AI companies know it. The backlash from publishers over copyrighted content has forced AI companies to broker exclusive licensing deals with a select group of publishers like News Corp and Axel Springer. Many of these publishers have seemingly used robots.txt rules as leverage in these negotiations.

Click here to download the graphic as a PDF and explore the source links.

Does this mean that publishers with licensing agreements feature more?

No. While publishers with AI partnerships appear more frequently in OpenWebText2 than in the WebText top 1000, the correlation isn’t absolute.

Three of the top five publishers in OpenWebText 2 (NYT, Advance, and Gannett) do not have licensing agreements with OpenAI. Also, the WebText top 1000 contains a higher percentage of these publishers than OpenWebText2 (13.47% vs. 12.04%). Suffice it to say that AI partnerships do not guarantee higher dataset representation. It’s also worth noting that the NYTimes blanket blocks almost all AI crawlers in its robots.txt, so its presence in this dataset is an indication that the makers of these datasets wanted to use NYTimes content, but not that they were able to do so.

Every major publisher thrives on high-quality content —from breaking news and investigative journalism to data-led reports and expert analysis. Looking at the top publishers featured in the Ziff Davis study, we see household names like:

These publishers dominate search, earn backlinks naturally , and are frequently used in LLM training datasets, reinforcing their credibility.

Despite volatile SERPs and the rise of AI-generated answers, content remains the foundation of a website’s authority.

While Moz’s Domain Authority (DA) isn’t a ranking factor, the Ziff Davis study confirms it’s a strong directional indicator of site authority, which aligns with the high-quality sources favored in LLM training​.

In a Moz roundup on the Google Leaks, Rand Fishkin pointed out , “ Google has been misleading marketers for years when saying they don’t use any form of website authority .” Supporting this statement, a study by Tom Pool on Google's Helpful Content Update (HCU) found that websites with higher DA scores were more likely to be HCU winners.

While building authority is a combination of different elements, the central tenets remain the same:

AI models face the same challenges with identifying authoritative sources as Google and may well solve them in the same way.

If LLMs favor high-authority websites, then backlinks from these sites carry weight—not just in Google search rankings but potentially in generative AI visibility.

But the reality is that link building is getting harder . Spammy outreach and low-value links don’t move the needle. Instead, focus on creating content that naturally attracts media attention and citations.

Brand Authority is shaping up to be just as important as Domain Authority. The numbers don’t lie—57.9% of the publishers in the Ziff Davis study had a Brand Authority score of 40 or higher. Moz’s Jonathan Berthold used a combination of Moz API and a custom Google Collab script to do a bulk URL analysis for Brand Authority score.

The numbers align with Tom Capper’s study findings, which showed that sites with strong brand signals were more likely to benefit from Google’s algorithm changes, while weaker brands struggled to compete​.

According to Amanda Milligan , a few tactics that work for Brand Authority include:

I’m not sure anyone is surprised about the outcome of the Ziff Davis study, as it confirms what we’ve long suspected. However, it’s important to note that these websites and publishers didn’t become giants overnight. They spent years investing in high-quality content, earning backlinks, and building credible brands. To optimize for generative AI search, SEOs should follow the same playbook: publish unique content that naturally attracts relevant backlinks and establishes topical authority.

I am the Senior Content Marketing Manager at Moz, where I support initiatives such as the blog, podcast, webinars, and GTM strategies. I'm also the founder of The Freelance Coalition for Developing Countries , a UK nonprofit providing free resources and training for BIPOC marketers globally.

You can now track your AI Visibility with the all-in-one SEO tool marketers trust.

How does Google's AI Overview expand user queries? Tom Capper reveals 10 fan-out categories you can use to improve your prompt tracking and keyword research.

Is prompt tracking draining your budget? Learn a lean strategy to cut bloated prompts, track AI visibility smarter, and focus on what drives brand growth.

Is AI helping your SEO or sabotaging it? Discover the hidden risks of LLMs and the practical strategies to protect your brand visibility.
