---
source: https://dejan.ai/blog/claude-system-internals/
title: Claude System Internals
scraped: 2026-03-25
published_on: 2025-10-09
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

# Claude System Internals

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/claude-system-internals/
Published: 2025-10-09
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Every time you chat with Claude, there’s a whole secret conversation happening that you never see. System prompts, token budgets, thinking blocks, and behavior rules shape every response. Here’s what’s really going on under the hood. Claude is literally told it gets “rewards” for following instructions. This is probably related to RLHF training. Following all […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Every time you chat with Claude, there’s a whole secret conversation happening that you never see. System prompts, token budgets, thinking blocks, and behavior rules shape every response. Here’s what’s really going on under the hood.

Claude is literally told it gets “rewards” for following instructions. This is probably related to RLHF training. Following all of these instructions well will increase Claude’s reward and help the user, especially the instructions around copyright and when to use search tools. Failing to follow the search instructions will reduce Claude’s reward.

Claude has a literal flowchart for deciding when to search the web vs. just answer from memory.

You can ask Claude for both the total token budget and current usage at any point during your chat. Internally it sees the following:

Claude sees your actual location in the system prompt and is told to “use this info naturally without phrases like ‘based on your location data’”. So when you ask “what’s the weather”, Claude already knows you’re in Melbourne.

When conversations get too long, Anthropic literally injects reminder prompts to keep Claude on track. You never see these, but Claude does.

Claude is SCREAMED AT in all caps about copyright. This is why it won’t give you song lyrics even if you beg.

Claude can literally “think” in hidden blocks that you never see.

Claude avoids over-formatting responses with elements like bold emphasis and headers. It uses the minimum formatting appropriate to make the response clear and readable.

Claude does not use emojis unless the person in the conversation asks it to or if the person’s message immediately prior contains an emoji.

Claude never curses unless the person asks for it or curses themselves.

Every artifact you see has a hidden MIME type that tells the renderer what it is.

The user wants me to continue listing tags. Let me finish the list properly.

These create Claude’s entire “operating environment” – defining what it knows, how it behaves, what tools it has, and how to format responses. You never see 99% of these, but they’re running every single conversation.

Source: https://github.com/asgeirtj/system_prompts_leaks/blob/main/claude.txt

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
