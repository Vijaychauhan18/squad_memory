---
source: https://dejan.ai/blog/reverse-prompting/
title: Reverse Prompting: Reconstructing Prompts from AI
scraped: 2026-03-22
published_on: 2026-03-18
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

# Reverse Prompting: Reconstructing Prompts from AI

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/reverse-prompting/
Published: 2026-03-18
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
We fine-tuned Google’s Gemma 3 (270M) to reverse the typical LLM workflow: given an AI-generated response, the model reconstructs the most likely prompt that produced it. We generated 100,000 synthetic prompt-response pairs using Gemini 2.5 Flash, trained for a single epoch on a consumer GPU, and built a Streamlit app that sweeps 24 decoding configurations […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

We fine-tuned Google’s Gemma 3 (270M) to reverse the typical LLM workflow: given an AI-generated response, the model reconstructs the most likely prompt that produced it. We generated 100,000 synthetic prompt-response pairs using Gemini 2.5 Flash, trained for a single epoch on a consumer GPU, and built a Streamlit app that sweeps 24 decoding configurations to produce ranked prompt candidates. The model demo runs on CPU and is available here .

Large language models take prompts and produce responses. We wanted to see if a small model could learn to do the opposite: take a response and work backwards to the prompt.

This isn’t about recovering the exact original prompt, but to surface the most plausible prompts, ranked by model confidence. Think of it as asking: “What question would most naturally lead to this answer?”

The training pipeline has two stages, both powered by Gemini 2.5 Flash via Vertex AI.

Stage 1: Prompt generation. We generated 100,000 diverse prompts across five categories designed to cover different user behaviours:

Each API call generated a batch of 100 prompts as JSON with thinking disabled. We ran 100 concurrent calls, stored results in SQLite, and had the full dataset in minutes.

Stage 2: Response generation. Each of the 100,000 prompts was sent back to Gemini 2.5 Flash to produce a corresponding AI assistant response. Same concurrency, same speed. The result: 100,000 prompt-response pairs ready for training.

The key design decision was how to format the training data. We needed the model to learn a clear boundary between the response (input) and the prompt (target). We settled on a simple separator:

During tokenization, we masked the loss over the response and separator tokens (setting labels to -100) so the model only learns to predict the prompt portion. This is critical: without masking, the model would waste capacity learning to reproduce the response text rather than focusing on the reverse mapping.

Sequences were capped at 2,048 tokens. Tokenization was batched in groups of 5,000 to manage memory, then concatenated into a single dataset.

A larger model would almost certainly perform better, but the goal was a practical tool that could run anywhere, not a benchmark result.

Training was straightforward. Full fine-tune, single epoch, on an NVIDIA RTX 4090.

One epoch was sufficient. The loss curve showed steady convergence without signs of underfitting, and we wanted to avoid overfitting on synthetic data where the model might memorise specific phrasing patterns rather than learning the general reverse mapping.

A single generation pass from the model produces one candidate prompt. To get a diverse set of candidates, we sweep across 24 contrastive search configurations by varying two parameters:

Contrastive search balances token probability with a degeneration penalty, which encourages diverse yet coherent outputs. Different configurations produce different candidate prompts from the same input.

Each candidate is then scored by perplexity: we run the full sequence (response + separator + generated prompt) through the model and compute the average token-level log probability over the prompt portion. Lower perplexity means the model finds that prompt more natural given the response.

The top 10 candidates are displayed with per-token confidence visualisation, where each word’s opacity reflects how confident the model was in predicting it.

Paste mode is the primary interface. Paste any AI-generated text, click Reconstruct Prompts, and the model generates ranked candidates. The results include a prompt table with perplexity scores and per-token confidence bar charts, a key phrases panel that extracts the most important shared phrases across candidates, and a word frequency heatmap.

URL mode is experimental. Enter a URL and the app scrapes the page content via the DataForSEO API, converts it to markdown, and runs it through the model. This isn’t the intended use case since the model was trained on AI assistant responses, not web pages. But it produces interesting results: the reconstructed “prompts” reveal what the model considers the core semantic intent of the page content. It’s less prompt reconstruction and more semantic summarisation through the lens of “what question would this page answer?”

Prompt engineering. Understanding what prompts lead to certain outputs helps refine prompt design. If you have an output you like, reverse prompting can suggest more efficient or precise ways to get there.

Content analysis. Running web content through the model reveals what the model perceives as the core intent behind the text. This could be useful for understanding how AI models interpret and categorise content.

AI content forensics. While this isn’t a detector (it doesn’t classify text as AI-generated or not), the confidence scores and perplexity values could serve as signals. Text that was genuinely produced by an AI assistant in response to a clear prompt may produce lower-perplexity reconstructions than text that wasn’t.

Training data curation. When building datasets, reverse prompting can help verify that responses actually match their intended prompts, or surface cases where the mapping is ambiguous.
