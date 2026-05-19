---
source: https://dejan.ai/blog/how-do-people-use-ai-assistants/
title: How do people use AI assistants?
scraped: 2026-03-25
published_on: 2025-12-05
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

# How do people use AI assistants?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/how-do-people-use-ai-assistants/
Published: 2025-12-05
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Carried by the inertia of “search query” mentality, AI SEO professionals often oversimplify how people interact with their AI assistants in chat sessions. Our analysis of ~1M real user chat sessions reveals a more complex picture. Key Findings The dataset contains 4.4 billion characters across 613 million words and 3.9 million conversation turns. The average […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Carried by the inertia of “search query” mentality, AI SEO professionals often oversimplify how people interact with their AI assistants in chat sessions. Our analysis of ~1M real user chat sessions reveals a more complex picture.

The dataset contains 4.4 billion characters across 613 million words and 3.9 million conversation turns . The average conversation is 4.7 turns, with a median of 2 turns, suggesting many users ask a single question and receive a single response.

The large gap between mean and median word counts (732 vs 430) indicates a right-skewed distribution, most conversations are relatively short, but a long tail of verbose sessions pulls the average up.

Assistants produce roughly 1.5x more content than users, unsurprising given that users ask questions and assistants provide detailed answers.

The stark difference between user mean (2,088 chars) and median (320 chars) reveals an important pattern: most user messages are short prompts , but some users paste long documents for summarization or analysis, dramatically inflating the average.

The median user contributes only 16-17% of the conversation’s content while receiving 83-84% from the assistant. This aligns with the typical pattern: short question in, long answer out.

At the aggregate level, users contribute about 40% of total content , higher than the per-session median because heavy users (those pasting long documents) contribute disproportionately to the total character count.

Over 80% of conversations contain fewer than 1,000 words . The sweet spot is 100-500 words (33.7%), representing a typical “question and answer” exchange. Only 4.2% of sessions exceed 2,500 words—these likely represent complex tasks like document editing, code review, or extended tutoring sessions.

To help us define the primary interaction types we surveyed the major AI platforms and compiled the following list AI chat type list:

We classified 24,259 conversations from the same dataset to understand what users are actually trying to accomplish when they interact with AI assistants and how much of this activity signals commercial intent.

Nearly two-thirds of conversations have no commercial intent whatsoever. Users are writing, brainstorming, learning, and chatting, not researching products or making purchase decisions.

The remaining 35% show some commercial signal , ranging from early-stage awareness (“what types of X exist?”) to active transaction support (“how do I buy Y?”).

Awareness dominates the commercial funnel at 10% of all sessions. Users frequently ask AI to help them understand a problem space before they even know what product category might solve it.

Consideration is the second-largest stage (8.5%), representing users actively comparing and evaluating options. This is prime territory for affiliate content and product recommendations.

Post-purchase outpaces transaction support suggesting users turn to AI more for help after buying (setup, troubleshooting) than during the purchase itself.

The 25% “Other” category warrants attention—these are sessions that don’t cleanly fit our taxonomy. Many may be jailbreak attempts, roleplay scenarios, or highly specialized requests.

Brainstorming and Planning together account for 14% of all conversations. Users treat AI as a thinking partner for creative and organizational tasks.

Conversation at 6.2% represents pure social/emotional interaction—people chatting with AI for companionship, venting, or entertainment.

Sessions were classified using Gemma 3 12B into 42 categories across a two-level taxonomy:

This analysis represents 24,259 classified sessions (~3% of the full 837,989 dataset). Classification is ongoing.

Thanks Dejan! This clarifies the potential strategy for marketers. Seems like writing for bots is a viable awareness strategy on some level, but the influence doesn’t extend to the BOFU for now.

Hey Dan! I was curious, where did the 1M-user chat dataset come from? And is it available anywhere for public or research access?

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
