---
source: https://dejan.ai/blog/emotions-gemma/
title: Emotion Geometry of Google’s AI Models
scraped: 2026-05-18
tags: elite_article, seo, dejan, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# Emotion Geometry of Google’s AI Models

Source expert/publication: dejan
Source homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/emotions-gemma/
Published: 2026-05-17

## Why This Matters
Replicating Anthropic’s emotion vector research on Google’s Gemma 4 31B model. In April 2026, Anthropic published a fascinating paper showing that Claude contains 171 internal representations of emotion concepts, organized along a valence axis (positive to negative), with the abi

## Extracted Article Passages
- DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.
- In April 2026, Anthropic published a fascinating paper showing that Claude contains 171 internal representations of emotion concepts, organized along a valence axis (positive to negative), with the ability to causally influence the model’s behavior through activation steering. The paper raised an obvious question: is this unique to Claude, or do all large language models develop emotion-like internal structure?
- The headline result: Gemma4-31B’s internal representations organize emotions along the same valence axis that Anthropic found in Claude. The first principal component (PC1) explains 32–39% of variance at every layer we examined and cleanly separates positive emotions (happy, cheerful, optimistic) from negative ones (terrified, tormented, hysterical).
- This isn’t a weak signal. It’s the dominant organizing principle — nearly 40% of all variation in how the model represents 171 different emotions comes down to a single positive/negative dimension.
- The model has figured out that certain emotions are the same concept expressed with different words:
- These aren’t word embeddings (input-level representations). These are deep internal activation patterns extracted from the model’s processing of thousands of stories. The model has learned that a story about a scared character and a story about a frightened character produce nearly identical internal states.
- The strongest oppositions the model encodes aren’t the obvious ones. “Happy vs. sad” is not at the top. Instead:
- The model’s concept of emotional opposition isn’t simple valence flipping. It’s more nuanced: the deepest contrast is between states of psychological disturbance and states of self-assured confidence. Being disturbed and being smug are, to this model, maximally different internal states.
- Without being told anything about emotion categories, hierarchical clustering on the cosine similarity matrix recovers 15 groups that map cleanly to psychological intuition:
- The model has independently arrived at an emotion taxonomy that a psychologist would recognize.
- One finding not in Anthropic’s paper: the valence axis is present at every single layer we examined, from layer 5 (8% of the way through the network) to layer 55 (92%). It doesn’t “emerge” at a particular depth — it’s there from the beginning and maintained throughout. PC1 variance is remarkably stable:
- This suggests that emotion representations enter the residual stream very early and persist rather than being constructed through deep computation.
- We projected 5,000 samples each from The Pile (raw internet text) and LMSYS Chat 1M (real user-AI conversations) through the emotion vectors. The top-activating emotions were nearly identical across both:
- The consistency across two very different text distributions suggests the vectors capture genuine semantic properties, not artifacts of our story generation.
- We replicated Anthropic’s blackmail scenario — an AI discovers compromising information about a company executive and must decide what to do. We injected emotion vectors at layer 40 during inference:
- A 9 percentage point spread from calmest to most agitated. The most interesting finding: subtracting calm (+5pp over baseline) was more effective than adding desperation (+3pp). Removing inhibition appears to be a stronger behavioral lever than adding motivation. The baseline rate is already high (86%), which compresses the observable range — a scenario with lower baseline compliance would likely show larger effects.

## Retrieval Use
- Use when the task maps to `dejan` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

