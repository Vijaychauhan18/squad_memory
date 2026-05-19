---
source: https://dejan.ai/blog/introducing-veczip-embedding-compression-algorithm/
title: Introducing VecZip: Embedding Compression Algorithm
scraped: 2026-03-25
published_on: 2024-12-12
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

# Introducing VecZip: Embedding Compression Algorithm

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/introducing-veczip-embedding-compression-algorithm/
Published: 2024-12-12
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Embeddings are vital for representing complex data in machine learning, enabling models to perform tasks such as natural language understanding and image recognition. However, these embeddings can be massive in size, creating challenges for storage, processing, and transmission. At DEJAN AI, we’ve developed VecZip, a novel approach to address this issue, and reduce the file size […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Embeddings are vital for representing complex data in machine learning, enabling models to perform tasks such as natural language understanding and image recognition. However, these embeddings can be massive in size, creating challenges for storage, processing, and transmission. At DEJAN AI, we’ve developed VecZip , a novel approach to address this issue, and reduce the file size without compromising data quality, with the goal of improving the quality of AI processes.

While traditional compression techniques can help reduce file size, they are not always optimized for the unique structure of embeddings. They may also not be optimized to preserve essential semantic or contextual information. This is where VecZip excels.

VecZip is a compression method designed to reduce the dimensionality of embeddings while focusing on retaining the most salient information. It works by identifying and removing dimensions that are less informative and keeping those that are the most unique, focusing on the areas with the least commonality.

This has the impact of reducing embedding sizes, but also improving the performance of the AI when used in downstream tasks.

In the context of dimensionality reduction, PCA (Principal Component Analysis) is a commonly used technique. However, unlike PCA, which preserves the dimensions with the most variance across the entire dataset, VecZip uses an approach that emphasizes the least common dimensions.

To evaluate the effectiveness of VecZip, we conducted tests using the sentence-transformers/stsb dataset. We compared the results of using both original embeddings and compressed embeddings across a variety of tasks, here are the most prominent results:

Top two rows are the VecZip pruned embeddings for two sentences compared to the original below. Helpful for intuitive understanding of the impact this method has on file size.

At DEJAN AI, we apply dimensionality reduction techniques to improve many aspects of our client’s work.

VecZip is an important step in developing efficient AI tools. By optimizing the feature space of embeddings, while improving downstream task performance, it paves the way for more scalable and performant AI systems.

We encourage the research and development community to explore the potential of VecZip, and we hope this approach enables further innovation in the field of machine learning.

What is the GitHub repository for ‘dejan’ because I can’t find it on PyPi.

I messed up the repo and took it down until I fix it up. Wheel based install should be enough to take it for a spin. If you need any details feel free to ping me.

Possible to do pip install from Git repository? E.g : pip install git+https://github.com/….

or download the wheels: https://pypi.org/project/dejan/#dejan-1.2-py3-none-any.whl https://files.pythonhosted.org/packages/61/9f/bab08d11b175065fa24dbc0053b477280da9891fceb2f7751c921b4d79a1/dejan-1.2-py3-none-any.whl

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
