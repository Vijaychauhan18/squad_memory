---
source: https://dejan.ai/blog/live-blog-hacking-gemini-embeddings/
title: Live Blog: Hacking Gemini Embeddings
scraped: 2026-03-25
published_on: 2025-05-24
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

# Live Blog: Hacking Gemini Embeddings

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/live-blog-hacking-gemini-embeddings/
Published: 2025-05-24
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Prompted by Darwin Santos on the 22th of May and a few days later by Dan Hickley, I had no choice but to jump on this experiment, it’s just too fun to skip. Especially now that I’m aware of the Gemini embedding model. The objective is to do reproduce the claims of this research paper […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Prompted by Darwin Santos on the 22th of May and a few days later by Dan Hickley, I had no choice but to jump on this experiment, it’s just too fun to skip. Especially now that I’m aware of the Gemini embedding model.

The objective is to do reproduce the claims of this research paper which claims that all embeddings share common geometry in multi-dimensional space and can therefore be mapped to each other, or even reverse engineered. I’m a little skeptical at this stage but happy to give it a try.

Rishi Jha , Collin Zhang , Vitaly Shmatikov , John X. Morris

We introduce the first method for translating text embeddings from one vector space to another without any paired data, encoders, or predefined sets of matches. Our unsupervised approach translates any embedding to and from a universal latent representation (i.e., a universal semantic structure conjectured by the Platonic Representation Hypothesis). Our translations achieve high cosine similarity across model pairs with different architectures, parameter counts, and training datasets. The ability to translate unknown embeddings into a different space while preserving their geometry has serious implications for the security of vector databases. An adversary with access only to embedding vectors can extract sensitive information about the underlying documents, sufficient for classification and attribute inference.

I’ll be live blogging as I do things so keep an eye on this post as things develop.

Observation: The gemini-embedding-exp-03-07 model produces 3,072-dimensional vectors.

The original vec2vec paper reported the following metrics for different model pairs:

Our results show moderate alignment with the paper’s findings, achieving reasonable cosine similarity between the MxbAI and Gemini embedding spaces.

To better understand the structure of each embedding space, we’ve created PCA visualizations that project the high-dimensional embeddings into 2D space:

We’ve also analyzed the similarity relationships within and between embedding spaces:

The significant difference in embedding dimensions (MxbAI: 1024 vs Gemini: 3072) suggests that:

The stark difference in translation performance between directions is particularly noteworthy:

The vec2vec paper demonstrated that embedding spaces from different models can be aligned through linear transformations. Our results show that this holds true even when:

However, our results also highlight an important limitation: the translation quality is highly dependent on the direction of translation when embedding spaces have significantly different dimensionalities.

Both mixedbread-ai/mxbai-embed-large-v1 and gemini-embedding-exp-03-07 support MRL (Matryoshka Representation Learning) dimensionality reduction so the feature extraction was adjusted and now we work with consistent embeddings.

This script implements Vec2Vec, an unsupervised embedding translation model inspired by the paper “Harnessing the Universal Geometry of Embeddings” . It learns to map embeddings from two different vector spaces (e.g., Gemini and MxbAI) into a shared latent space using deep residual networks, without any labeled alignment. The architecture includes input/output adapters, a shared backbone, and adversarial discriminators to align both original and latent distributions. Training optimizes reconstruction, cycle-consistency, vector space preservation, and GAN losses. The trainer includes evaluation utilities and checkpointing, making the framework modular and extensible for cross-domain embedding alignment.

PS C:\projects\gemini\analysis> python vec2vec_quickstart.py –compare INFO:vec2vec_implementation:Loaded 39 embeddings of dimension 1024 from gemini.csv INFO:vec2vec_implementation:Loaded 39 embeddings of dimension 1024 from mxbai.csv

Cosine similarity between same documents in different spaces: Mean: -0.0068 Std: 0.0213 Min: -0.0535 Max: 0.0465

Mean cosine similarity: Input space: -0.0068 ± 0.0213 Latent space: 0.0346 ± 0.0455 INFO:vec2vec_evaluation:Visualizing latent space… INFO:vec2vec_evaluation:Plotting similarity heatmaps… INFO:vec2vec_evaluation:Saving translated embeddings… INFO:vec2vec_evaluation:Saved translated embeddings to translated_embeddings INFO:vec2vec_evaluation: Demonstration: Finding similar documents across spaces

Gemini document 0 (https://dejan.ai/blog/gemini-system-prompt/): Top 5 similar MxbAI documents after translation:

Gemini document 1 (https://dejan.ai/blog/how-gemini-selects-results/): Top 5 similar MxbAI documents after translation:

Gemini document 2 (https://dejan.ai/blog/search-query-quality-classifier/): Top 5 similar MxbAI documents after translation:

Gemini document 3 (https://dejan.ai/blog/query-intent-via-retrieval-augmentation-and-model-distillation/): Top 5 similar MxbAI documents after translation:

Gemini document 4 (https://dejan.ai/blog/resource-efficient-binary-vector-embeddings-with-matryoshka-representation-learning/): Top 5 similar MxbAI documents after translation:

pipeline ran end-to-end, but the learned mapping barely moved the needle:

mean_cos_sim_1to2…………. 0.1613 mean_cos_sim_2to1…………. 0.0324 std_cos_sim_1to2………….. 0.0307 std_cos_sim_2to1………….. 0.0230 top1_acc_1to2…………….. 0.0200 top1_acc_2to1…………….. 0.0100 top5_acc_1to2…………….. 0.0900 top5_acc_2to1…………….. 0.0400 top10_acc_1to2……………. 0.1500 top10_acc_2to1……………. 0.0800 mean_rank_1to2……………. 47.1500 mean_rank_2to1……………. 48.3100 cycle_error_1…………….. 0.1456 cycle_error_2…………….. 0.2661 INFO:vec2vec_evaluation:Computing latent alignment…

Mean cosine similarity: Input space: 0.0031 ± 0.0313 Latent space: 0.1729 ± 0.2319

Gemini document 0 (https://www.engadget.com/products/sony/bravia/kdl-46hx800/): Top 5 similar MxbAI documents after translation:

Gemini document 1 (https://www.engadget.com/2010-07-13-book-review-you-are-not-a-gadget.html): Top 5 similar MxbAI documents after translation:

Gemini document 2 (https://www.engadget.com/products/garmin/nuvi/1250/): Top 5 similar MxbAI documents after translation:

Gemini document 3 (https://www.engadget.com/products/nikon/coolpix/s3100/): Top 5 similar MxbAI documents after translation:

Gemini document 4 (https://www.engadget.com/sony-a-7-c-review-smart-small-clumsy-153031933.html): Top 5 similar MxbAI documents after translation:

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
