---
source: https://dejan.ai/blog/what-does-gemini-think-about-your-brand/
title: What does Gemini think about your brand?
scraped: 2026-03-25
published_on: 2025-01-29
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

# What does Gemini think about your brand?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/what-does-gemini-think-about-your-brand/
Published: 2025-01-29
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Inside Chrome Dev, there’s a quantized version of Google’s flagship model Gemini for those who have it enabled. The model does many things from summarization, translation, writing assistance all the way to scam prevention. The model definition is a secret, but its weights are stored as a 3GB .bin file on the user machine. Inside […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Inside Chrome Dev, there’s a quantized version of Google’s flagship model Gemini for those who have it enabled. The model does many things from summarization, translation, writing assistance all the way to scam prevention. The model definition is a secret, but its weights are stored as a 3GB .bin file on the user machine.

Inside \User Data\optimization_guide_model_store\55\ folder is a file called on_device_model_execution_config.pb which defines a prompt for Gemini’s role in scam detection.

The model receives clean text from Chrome and returns two items:

Here’s an example of the above implemented with trafilatura and Gemma, a distilled version of Gemini with approximately equal capability as Gemini Nano.

Google’s on-device scam detection classifier then takes over and makes a decision on whether the page is trustworthy or not.

Freaking cool. This gives a different perspectives that computing power happens at the end users devices. As web is vast, this makes sense too.

And also, this is the reason more ram is needed for the chrome browsers too. As there are so many memes around chrome using so much computing resources like cpu, ram even for normal browsing.

I understand that this information could, in some way, be sent to Google. I wonder if there’s a way to configure the system to log who accesses these files, when, and what is accessed

In Ububunt: cat ~/.config/google-chrome/optimization_guide_model_store/51/EFB5C153BB14D509/AF672ACE476F3DC7/on_device_model_execution_config.pb

Example contents: Who is the first president of the US? washington

Exploratory APIs and early-stage APIs are available to Early Preview Program (EPP) participants: https://developer.chrome.com/docs/ai/join-epp

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
