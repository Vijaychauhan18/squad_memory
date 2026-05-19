---
source: https://dejan.ai/blog/comment-bots/
title: Comprehensive Guide to Identifying AI Comment Bots
scraped: 2026-03-25
published_on: 2025-08-28
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

# Comprehensive Guide to Identifying AI Comment Bots

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/comment-bots/
Published: 2025-08-28
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Some people use AI to speed up the process of getting their ideas and message out. Others use it to polish up their language which I think is really cool use of AI, especially if they’re not a native speaker. But there’s also the hordes of mindless AI slop generators masquerading as meaningful human engagement, […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Some people use AI to speed up the process of getting their ideas and message out. Others use it to polish up their language which I think is really cool use of AI, especially if they’re not a native speaker. But there’s also the hordes of mindless AI slop generators masquerading as meaningful human engagement, wasting everyone’s time and energy.

The absence of ALL these human elements, combined with the presence of multiple bot patterns, provides strong evidence of automated generation. The bot exists in a permanent state of agreeable, grammatically perfect, professionally enthusiastic consensus—a state no human maintains indefinitely.

The analysis processed 226 human comments and 618 bot comments, revealing statistically significant differences across multiple dimensions including readability, sentiment patterns, vocabulary usage, and structural characteristics. Key findings indicate that AI comment bots exhibit higher positive sentiment, greater readability scores, more consistent linguistic patterns, and distinct vocabulary preferences compared to human comments.

The human comments demonstrate significant variability in length and structure, ranging from brief single-word responses to extended multi-sentence observations. Character counts range from 5 to 1,125 characters, with word counts spanning from 1 to 151 words per comment. This wide distribution reflects the natural diversity of human communication styles and engagement levels across different contexts and topics.

In contrast, the AI comment dataset exhibits more constrained variation in length and structure. Character counts range from 15 to 361 characters, with word counts between 2 and 51 words per comment. This narrower distribution suggests more consistent generation parameters and potentially indicates algorithmic constraints in the AI systems used to generate these comments.

The sentence structure analysis reveals interesting patterns in both datasets. Human comments average 1.8 sentences per comment with a standard deviation of 1.4, indicating considerable variation in structural complexity. AI comments average 2.3 sentences per comment with a standard deviation of 1.0, suggesting more consistent sentence structuring but potentially higher average complexity per comment.

Comprehensive statistical analysis reveals significant differences between human and AI-generated comments across multiple dimensions. These differences provide quantitative evidence for distinguishing characteristics that can serve as detection features for automated systems and human moderators.

The analysis of comment length characteristics reveals statistically significant differences between human and AI-generated content. Human comments average 166.5 characters with a standard deviation of 196.8, demonstrating high variability in expression length. AI comments average 121.8 characters with a standard deviation of 45.0, showing more consistent length patterns with less extreme variation.

Word count analysis reinforces these patterns, with human comments averaging 25.2 words (±30.5) compared to AI comments averaging 19.8 words (±7.3). The t-test results show statistical significance (t=4.072, p<0.001) with a moderate effect size (Cohen’s d=0.317), indicating that this difference is both statistically reliable and practically meaningful for detection purposes.

The sentence count comparison reveals that AI comments tend to use more sentences per comment despite being shorter overall. This pattern suggests that AI systems may favor shorter, more declarative sentences rather than the complex, compound sentences often used by humans. The statistical significance of these structural differences (p<0.001) provides strong evidence for systematic differences in content organization between human and AI-generated comments.

Vocabulary analysis reveals fundamental differences in word usage patterns between human and AI-generated comments. Human comments demonstrate a Type-Token Ratio (TTR) of 0.447, indicating relatively high vocabulary diversity within the dataset. This high TTR reflects the natural tendency of humans to use varied vocabulary and avoid repetitive language patterns.

AI comments exhibit a lower TTR of 0.329, suggesting more repetitive vocabulary usage and potentially indicating reliance on common phrases and expressions. This pattern aligns with the training methodologies of large language models, which tend to favor frequently occurring word combinations and phrases from their training data.

Comprehensive statistical testing confirms the reliability of observed differences between human and AI comment characteristics. T-test results for comment length show t=5.270 with p<0.001, indicating extremely high confidence in the length difference. Word count differences achieve t=4.072 with p<0.001, confirming significant structural differences between the two comment types.

Effect size calculations provide practical significance measures alongside statistical significance. Comment length differences show a moderate effect size (Cohen’s d=0.410), while word count differences demonstrate a small to moderate effect size (Cohen’s d=0.317). These effect sizes indicate that the differences are not only statistically reliable but also practically meaningful for detection applications.

The consistency of statistical significance across multiple measures strengthens confidence in the findings. Every major linguistic dimension examined shows statistically significant differences, suggesting systematic rather than random variations between human and AI-generated comments. This consistency supports the development of robust detection algorithms based on multiple complementary features rather than relying on single indicators.

Sentiment analysis reveals one of the most striking differences between human and AI-generated comments, with implications for understanding the emotional characteristics and engagement strategies of automated systems. The analysis employs the VADER sentiment analyzer, specifically designed for social media content, to capture nuanced emotional expressions in short-form text.

Human comments demonstrate a relatively neutral sentiment profile with a compound sentiment score averaging 0.119, indicating slight positive bias but substantial variation around neutral sentiment. The sentiment distribution shows 7.2% positive sentiment, 3.5% negative sentiment, and 89.3% neutral content. This distribution reflects the natural emotional range of human communication, including critical observations, neutral information sharing, and occasional positive expressions.

AI-generated comments exhibit significantly more positive sentiment characteristics, with a compound sentiment score averaging 0.441. This represents a nearly four-fold increase in positive sentiment compared to human comments. The sentiment distribution shows 22.5% positive sentiment, 4.9% negative sentiment, and 72.6% neutral content. The statistical significance of this difference (t=-10.567, p<0.001) with a large effect size (Cohen’s d=-0.821) indicates that sentiment polarity serves as a highly reliable distinguishing feature.

The pronounced positive bias in AI comments likely reflects training optimization for engagement and user satisfaction. AI systems are typically trained to generate content that promotes positive interactions and avoids potentially controversial or negative statements. This optimization creates a detectable signature in the sentiment distribution that differs markedly from natural human emotional expression patterns.

Readability analysis using multiple established metrics reveals systematic differences in text complexity between human and AI-generated comments. The Flesch Reading Ease score, which measures text accessibility on a scale where higher scores indicate easier reading, shows human comments averaging 41.6 compared to AI comments averaging 63.6. This significant difference (t=-5.643, p<0.001) indicates that AI comments are substantially more readable and accessible.

The Flesch-Kincaid Grade Level assessment reinforces these findings, with human comments requiring an average grade level of 10.3 compared to AI comments at grade level 7.1. This three-grade difference represents a substantial gap in text complexity, suggesting that AI systems optimize for broader accessibility and comprehension. The Gunning Fog Index, another complexity measure, shows similar patterns with human comments at 10.8 and AI comments at 9.0.

These readability differences likely stem from AI training objectives that prioritize clear communication and broad audience appeal. Human comments often include technical terminology, complex sentence structures, and domain-specific language that increases reading difficulty. AI systems, trained on diverse text corpora with optimization for general comprehension, tend to produce more accessible content that scores higher on readability metrics.

The combination of sentiment and readability patterns provides powerful indicators for AI comment detection. The consistent positive sentiment bias combined with higher readability scores creates a distinctive profile that differs significantly from natural human communication patterns. These characteristics can be incorporated into automated detection systems as complementary features alongside structural and vocabulary-based indicators.

The large effect sizes observed in both sentiment (Cohen’s d=-0.821) and readability measures suggest that these features provide reliable discrimination between human and AI content. The statistical robustness of these differences, confirmed through multiple independent metrics, supports their use in practical detection applications across various platforms and contexts.

The Type-Token Ratio analysis reveals fundamental differences in vocabulary diversity between human and AI-generated comments. Human comments achieve higher vocabulary richness (TTR=0.447) despite having fewer total comments, indicating greater lexical diversity and creative language use. This pattern reflects the natural human tendency toward varied expression and avoidance of repetitive language.

AI comments demonstrate lower vocabulary richness (TTR=0.329) despite the larger dataset size, suggesting more constrained vocabulary usage and potential reliance on common phrases and expressions. This pattern aligns with language model training methodologies that favor frequently occurring word combinations and may indicate systematic vocabulary limitations in AI generation systems.

The vocabulary richness difference has practical implications for detection systems. Algorithms can assess the diversity of vocabulary usage within comment sets to identify potentially AI-generated content. Comments that demonstrate unusually low vocabulary diversity relative to their length and complexity may warrant additional scrutiny for AI generation indicators.

Here is a list of lookalike comments which resemble the analyzed dataset:

It’s true—many comments on social media now are modular AI responses. They appear well-written, but they lack any sense of humanity or valuable substance.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
