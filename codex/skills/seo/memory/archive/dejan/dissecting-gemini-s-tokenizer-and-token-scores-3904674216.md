---
source: https://dejan.ai/blog/gemini-toknizer/
title: Dissecting Gemini’s Tokenizer and Token Scores
scraped: 2026-03-25
published_on: 2025-06-05
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

# Dissecting Gemini’s Tokenizer and Token Scores

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/gemini-toknizer/
Published: 2025-06-05
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
As a technical SEO, you might be diving into machine learning (ML) to understand how tools like Google’s Gemini process text. One foundational concept is subword tokenization—breaking words into smaller pieces called “tokens.” While tokens themselves are context-agnostic (they don’t consider surrounding words), they do carry an inherent bias: each token’s likelihood reflects how prominent […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

As a technical SEO, you might be diving into machine learning (ML) to understand how tools like Google’s Gemini process text. One foundational concept is subword tokenization —breaking words into smaller pieces called “tokens.” While tokens themselves are context-agnostic (they don’t consider surrounding words), they do carry an inherent bias : each token’s likelihood reflects how prominent that subword was in the training data. In other words, tokens that appeared frequently during training end up with higher scores, and this directly influences downstream ML models.

By using the following tool, you can inspect which subwords are common or rare , helping you anticipate how Google’s Gemini might treat certain tokens in content, prompts and search queries.

This tool is not a simulation. It uses Gemini’s actual trained SentencePiece model.

Before diving into scores, it helps to recall why we use subword tokenization at all:

SentencePiece’s unigram approach proceeds roughly as follows:

These learned log-likelihoods are the “raw scores” we’ll explore. In many applications (like our Streamlit demo), we normalize them across the entire vocabulary so that end users can see a “percentage-style” bar indicating each token’s relative importance during training.

It is tempting to read “log-likelihood” as simply “how often did this exact subword occur in the training data?” In reality, SentencePiece’s unigram training infers each piece’s probability by optimizing corpus reconstruction. Concretely:

[math] \text{maximize } \prod_{w \in \text{corpus}} \sum_{\text{tokenizations } t \rightarrow w} \prod_{u \in t} P(u). [/math]

During this optimization, each subword piece [math]u[/math] gets assigned a probability [math]P(u)[/math]. Taking the log yields the “log-likelihood” or “score” used internally.

When presenting these scores to readers or end users, it’s helpful to describe them as a “likelihood of the token appearing in the training data” , with these caveats:

[math] \text{Normalized}(u) = \frac{\log P(u) – \min \log P}{\max \log P – \min \log P}. [/math]

Render “Normalized” as a percentage (0 % = least likely piece; 100 % = most likely piece).

Because some readers might confuse this with “the probability a model would generate this token next,” emphasize:

“These are unnormalized log-probabilities from tokenizer training (unigram), not the conditional probabilities you’d get from a full language model.”

You can say, for instance: > “A higher-scoring token was more central to reconstructing the training data and thus was retained in the final vocabulary.”

In other words, “importance during tokenizer training” and “likelihood of appearing” are two sides of the same coin under the unigram model.

Token Likelihood (Unigram Score). Each subword piece in our SentencePiece-based Gemini tokenizer carries a unigram log-likelihood —a number learned during tokenizer training to maximize the model’s ability to reconstruct the corpus. Intuitively, tokens that appeared more frequently (or that helped reconstruct many different words) receive higher log-probabilities. In our visualization, we then linearly map these raw log-scores into a [math][0,1][/math] range and display them as percentages (0 % = lowest “importance,” 100 % = highest). Note that this is a global, context-agnostic measure: it does not depend on what comes before or after. Rather, it reflects how “likely” that piece was under the SentencePiece unigram model of the training data.

#### Token Likelihoods in Action When you type a sentence like “The quick brown fox jumps over the lazy dog” , our interface will break it into subword pieces such as:

For each subword, we look up its learned unigram log-likelihood (e.g., [math]“Ġthe”[/math] might have [math]\log P = -2.1[/math], [math]“Ġquick”[/math] [math]\log P = -5.3[/math], [math]“Ġfox”[/math] [math]\log P = -6.2[/math]). After computing the global min and max over all ~50 K tokens, we map these values into [math][0,1][/math]. Suppose:

[math] \text{Normalized} = \frac{-2.1 – (-9.8)}{-1.5 – (-9.8)} = \frac{7.7}{8.3} \approx 0.928 \,(\approx 92.8\%). [/math]

[math] \text{Normalized} = \frac{-6.2 – (-9.8)}{-1.5 – (-9.8)} = \frac{3.6}{8.3} \approx 0.434 \,(\approx 43.4\%). [/math]

Visually, [math]“Ġthe”[/math] will show a long, nearly full bar (indicating it was extremely common), while [math]“Ġfox”[/math] will be roughly halfway (moderately common).

Framing these SentencePiece scores as a “likelihood of the token appearing in the training data” is accurate when you emphasize:

By clarifying these points in your article, readers will gain a clear understanding of why some subword pieces are deemed more “important,” how the normalization step works, and what these bars truly signify. This transparent framing helps set proper expectations and prevents misinterpretation: the bars represent global importance during tokenizer training , not “the probability that your model will output this next.”

Below is an in-depth look at the actual gemini-1.5-pro-002.spm.model file (a SentencePiece “unigram” tokenizer).

When you load gemini-1.5-pro-002.spm.model with SentencePieceProcessor (using sp.Load("…/gemini-1.5-pro-002.spm.model") ), you discover:

In other words, this tokenizer defines 256000 distinct “subword” pieces.

Any piece with a score of 0.0 is reserved (not “learned” from the corpus) and typically used for padding, special markers, or placeholders.

Each subword piece u in a SentencePiece unigram model carries a log-likelihood \log P(u). In this particular .spm.model , the raw score range is:

When you display these as “percentages” in a UI, you usually normalize:

[math]Normalized(u) = ( log P(u) – (–255494) ) / ( 0 – (–255494) ) = ( log P(u) + 255494 ) / 255494[/math]

After normalization, the most frequent/important token(s) map to 100 %, while the rarest mapped pieces approach 0 %.

If you sort all 256000 pieces by their raw score descending (i.e. most common first), you’ll find that the very highest log-score (0.0) belongs to special control tokens, for example:

However, ignoring control tokens, the most frequent real subwords (highest negative log-score closest to 0.0) might look like:

[math]Normalized → \frac{-702.0 – (-255494)}{0 – (-255494)} \approx \frac{254792}{255494} \approx 0.997\ (\approx 99.7\%).[/math]

At the other extreme, the rarest or least “useful” subwords—often obscure Unicode glyphs or extremely rare sequences—have scores around –255494.0. For instance:

A SentencePiece .spm.model is a Protocol Buffer that contains two main sections:

internally SentencePiece deserializes the Protocol Buffer into:

Under the hood, each piece’s log-probability was learned by the Unigram LM trainer :

The resulting binary file is about 4.24 MB on disk. When sphere-packed into memory, it occupies slightly more, but SentencePieceProcessor is extremely efficient about lookups and decoding.

In other words, this section peels back the curtain on Gemini’s SentencePiece vocabulary: each token has a learned log-likelihood (reflecting global frequency/importance) and a unique textual form (including standard English subwords, punctuation, Unicode code‐points, and special placeholders). Understanding these internal stats helps you see exactly which building blocks Gemini will use when it tokenizes any text you throw at it.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
