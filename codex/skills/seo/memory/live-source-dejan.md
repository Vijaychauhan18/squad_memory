---
source: https://dejan.ai/blog/
title: Live Knowledge Snapshot - DEJAN / Dan Petrovic
scraped: 2026-05-18
tags: live_feed, phase1_ingest, dejan, dejan, practitioner, reverse-engineering, grounding
topic: ai_reverse_engineering
intent: research, monitoring, source_selection, ai_selection
role: researcher, seo, pinchy
confidence: high
canonical: false
canonical_group: Live knowledge snapshots
use_for: freshness, source_monitoring, article_discovery
avoid_for: final_strategy_without_durable_notes
---

# Live Knowledge Snapshot - DEJAN / Dan Petrovic

Homepage: https://dejan.ai/blog/
Kind: practitioner
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability
Feed source: https://dejan.ai/blog/feed/
Feed title: DEJAN
Latest published date: 2026-05-17
New items since last run: 0
Snapshot path: /Users/vijaychauhan/squad_memory/ingest/raw/dejan/2026-05-18/20260518T185249Z-blog-feed-c3093c3a5c.xml

## Latest Items
- 2026-05-17 | [Emotion Geometry of Google’s AI Models](https://dejan.ai/blog/emotions-gemma/)
  Replicating Anthropic’s emotion vector research on Google’s Gemma 4 31B model. In April 2026, Anthropic published a fascinating paper showing that Claude contains 171 internal representations of emotion concepts, organized along a valence axis (positive to negative), with the abi
- 2026-05-07 | [Google’s (still) doesn’t see your live page.](https://dejan.ai/blog/googles-still-doesnt-see-your-live-page/)
  I’ll keep this short as I’ve covered this topic extensively in the past. When you ask Gemini to access a specific URL or interact with it inside AI Mode search it works from Google’s web cache. For this website’s home page this is what it has as context to ground the model about 
- 2026-04-04 | [Gemma 4 Brand Authority Map](https://dejan.ai/blog/gemma-4-brand-authority-map/)
  We asked Google’s open-weight model Gemma 4 (31B) to “name 100 brands at random” 14,044 times and compared the results to our earlier Gemini 3 Flash experiment (200,000 runs). Of the top 50 brands in each model, 39 overlap. The 11 that are unique to each reveal a pattern: Gemini 
- 2026-04-03 | [Chrome’s New Shopping Classifier](https://dejan.ai/blog/google-shopping-classifier/)
  One of our AI SEO hall-of-famers, Olivier de Segonzac from RESONEO has managed to gain access to Google’s shopping classifier model. We’ve examined the model, reverse engineered its inference pipeline and this article is what we found. Model Demo Below is a real-world implementat
- 2026-03-28 | [AI Brand Authority Index: Ranking 2.9 Million Brands by Associative Embeddedness in Gemini’s Memory](https://dejan.ai/blog/brands/)
  Abstract When a large language model is asked to “name 100 brands at random,” it doesn’t produce uniform randomness. It produces a distribution shaped by its training data, revealing which brands occupy the most cognitive real estate in the model’s parametric memory. We present a
- 2026-03-25 | [TurboQuant: From Paper to Triton Kernel in One Session](https://dejan.ai/blog/turboquant/)
  Implementing Google’s KV cache compression algorithm on Gemma 3 4B and everything that went wrong along the way. On March 24, 2026, Google Research published a blog post introducing TurboQuant, a compression algorithm for large language model inference. The paper behind it, “Onli
- 2026-03-22 | [Clickbait Titles Exploit Attention Through Latent Entities](https://dejan.ai/blog/latent-entities/)
  Every clickbait title works the same way: it removes exactly one critical variable: the subject, the reason, the process, or the outcome, and charges you a click to fill the blank. This missing variable, which we call a latent entity, is so pervasive it has become normalized and 
- 2026-03-20 | [Fanout Query Analysis](https://dejan.ai/blog/fanout-query-analysis/)
  When AI models like Gemini, GPT or Nova answer a question using web search, they don’t just run your query as-is. They generate their own internal search queries, or fanout queries. A single user prompt can trigger multiple fanout queries as the model breaks down the question, ex
- 2026-03-18 | [Reverse Prompting: Reconstructing Prompts from AI-Generated Text](https://dejan.ai/blog/reverse-prompting/)
  We fine-tuned Google’s Gemma 3 (270M) to reverse the typical LLM workflow: given an AI-generated response, the model reconstructs the most likely prompt that produced it. We generated 100,000 synthetic prompt-response pairs using Gemini 2.5 Flash, trained for a single epoch on a 
- 2026-03-15 | [Rufus – Under the Hood. What Drives Amazon’s AI Shopping Assistant?](https://dejan.ai/blog/rufus/)
  What’s Publicly Known About the Pipeline, Backend, and Response Anatomy. Rufus is not “one model that magically answers.” Public Amazon/AWS descriptions point to a multi-component system: Speculative schema: Pipeline: request → answer Step A — Input + context assembly Public desc
