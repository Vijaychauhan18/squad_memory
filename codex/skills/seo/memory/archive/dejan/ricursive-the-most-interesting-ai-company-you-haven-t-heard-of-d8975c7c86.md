---
source: https://dejan.ai/blog/ricursive/
title: Ricursive: The Most Interesting AI Company You Haven’t Heard Of
scraped: 2026-03-25
published_on: 2025-12-03
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

# Ricursive: The Most Interesting AI Company You Haven’t Heard Of

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/ricursive/
Published: 2025-12-03
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
There’s a concept in AI that sounds like science fiction but is now being pursued seriously: recursive self-improvement. The idea is simple. Build an AI system that improves the hardware it runs on. Train a better AI on that improved hardware. Use that AI to design even better hardware. Repeat. This isn’t theoretical anymore. Two […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

There’s a concept in AI that sounds like science fiction but is now being pursued seriously: recursive self-improvement.

The idea is simple. Build an AI system that improves the hardware it runs on. Train a better AI on that improved hardware. Use that AI to design even better hardware. Repeat.

This isn’t theoretical anymore. Two researchers who actually demonstrated a working version of this loop at Google are now building a company around it.

Anna Goldie and Azalia Mirhoseini launched Ricursive Intelligence last month. They raised 35 million from Sequoia at a 750 million valuation — before shipping a product.

That valuation makes more sense when you look at what they’ve already built.

In 2020, Goldie and Mirhoseini published a paper in Nature describing a deep reinforcement learning system that could design chip layouts. The AI treats chip floorplanning like a game — placing components one at a time, receiving feedback on the quality of each placement, and updating its policy to get better.

The system, later named AlphaChip, produces layouts in hours that match or beat what human engineers create over weeks or months. More importantly, it learns: the more chip designs it sees, the faster and better it gets.

This wasn’t a research demo. AlphaChip has been used in production at Google for four generations of TPUs — the chips that power Gemini, Imagen, and most of Google’s AI infrastructure. It’s also been used for Axion (Google’s Arm-based CPU), other chips across Alphabet, and has been adopted externally by companies like MediaTek.

The recursive loop is already real. AlphaChip was trained on TPUs. It designed the next generation of TPUs. The next version of AlphaChip was trained on those new TPUs.

Their credentials are unusual even by AI research standards.

Anna Goldie : Stanford NLP PhD (under Chris Manning), three degrees from MIT (CS, Linguistics, and a Masters in EECS). She co-founded the ML for Systems team at Google Brain, worked on Constitutional AI and retrieval-augmented LLMs at Anthropic, and most recently led LLM research on Gemini at DeepMind. MIT Technology Review named her one of their 35 Innovators Under 35 in 2021. She delivered keynotes at Google Developer Day in China — in Mandarin — to audiences of 10 million.

Azalia Mirhoseini : PhD from Rice University (Best ECE Thesis Award), now an Assistant Professor at Stanford running the Scaling Intelligence Lab. She’s also a Senior Staff Scientist at DeepMind. Beyond AlphaChip, she co-authored the foundational Mixture-of-Experts (MoE) paper in 2017 — the architecture that now powers most frontier LLMs including GPT-4 and Gemini. Also named to MIT Technology Review’s 35 Under 35.

They’ve worked together for nine years — starting at Google Brain on the same day. The AlphaChip project began when both were independently drafting a moonshot proposal for “AI for chip design.” Jeff Dean emailed them the same idea before they could hit send.

Phase 1 : Tackle the long poles of chip design. Reduce the current 2-3 year design cycle to weeks.

Phase 2 : End-to-end automation. Given a workload, design the entire chip through to GDS2 (the format sent to foundries like TSMC for manufacturing). This would let any company — AR/VR, robotics, autonomous vehicles, space tech — build custom silicon without dedicated chip design teams.

Phase 3 : Vertical integration. Build their own chips, train their own models, and use AI to design hardware that runs AI better and faster. Close the recursive loop completely.

The endgame is explicit: they believe this path leads toward artificial superintelligence.

The current chip ecosystem is a bottleneck. Designing custom silicon takes years, costs hundreds of millions, and requires engineering talent that maybe a dozen companies in the world can assemble. Even well-funded AI labs are dependent on Nvidia’s roadmap.

If Ricursive succeeds, this changes. Their pitch is a “Cambrian explosion of custom silicon” — where any company can specify a workload and receive manufacturable chip designs in weeks.

This isn’t just about making AI cheaper to run. Different AI architectures want different hardware. Right now, algorithms are designed around the chips we have. Accelerating chip design could unlock entirely new model architectures that wouldn’t make sense on today’s hardware.

Beyond the founders, Ricursive has assembled people from Google, Nvidia, Cadence, and Apple. Several worked directly on AlphaChip at Google, including Ebrahim Songhori, Jiwoo Pak, and Yi-Chen Lu.

They’re operating out of a house near Stanford. According to the WSJ, five researchers were recently spotted “scrunched before giant computer screens… dissecting research papers and parsing through lines of code.”

The vibe is early-stage and technical. No marketing fluff. Just people who’ve already done this once, now trying to do it at scale.

I’ve spent three years studying machine learning and its intersection with systems. This is one of the most technically grounded ambitious visions I’ve seen.

It’s not a pitch deck about future capabilities. They have four generations of production chips with layouts generated by their method. The recursive loop already exists — they’re trying to accelerate it.

Is the $750M valuation justified? That depends on execution. But the people, the prior results, and the thesis are all unusually strong.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
