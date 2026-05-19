---
source: https://dejan.ai/blog/caps/
title: CAPS: A Content Attribution Payment Scheme for the AI Era
scraped: 2026-03-25
published_on: 2025-09-30
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

# CAPS: A Content Attribution Payment Scheme for the AI Era

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/caps/
Published: 2025-09-30
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
The Problem: A Broken Content Ecosystem We’re watching the collapse of the web’s economic model in real-time, and everyone knows it. AI assistants have fundamentally changed how people consume information. Why wade through ten articles when Claude, ChatGPT, or Gemini can synthesize an answer in seconds? Why maintain 100 browser tabs for research when AI […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

We’re watching the collapse of the web’s economic model in real-time, and everyone knows it.

AI assistants have fundamentally changed how people consume information. Why wade through ten articles when Claude, ChatGPT, or Gemini can synthesize an answer in seconds? Why maintain 100 browser tabs for research when AI can connect the dots for you? The user experience is undeniably better—not because AI provides better quality than human research, but because humans will always trade some quality for massive time and effort savings.

The numbers bear this out. Traditional search traffic is declining. Publishers are hemorrhaging ad revenue. Quality journalism is becoming economically unviable. Meanwhile, AI platforms are training on and retrieving from this very content to provide their valuable summaries—without the economic feedback loop that sustains content creation.

The current system has created a parasitic relationship: AI platforms extract value from content while publishers watch their business models crumble. Something has to give.

Paywalls and robots.txt blocking Publishers can block AI crawlers, but this is economic suicide. If your content isn’t in the AI’s training data or retrieval systems, you become invisible to the next generation of users. You’re choosing between slow death (blocked from AI) and fast death (AI cannibalizes your traffic).

Litigation and licensing deals The New York Times sues OpenAI. News Corp signs deals with Google. These create a two-tier system: major publishers with legal teams get paid, everyone else gets exploited. It’s not scalable, it’s not fair, and it doesn’t solve the systemic problem.

Current ad models Traditional display advertising is already failing. The problem isn’t ads themselves—it’s the lack of true personalization and the low “right time, right place” factor. Most ads are visual pollution that users have learned to ignore or block.

Post-hoc citation bolting Some AI systems like Gemini use “generate-then-ground” approaches—they create an answer first, then try to find sources that support it. This is a bandaid solution that doesn’t truly attribute content and can’t reliably compensate creators. ( I’ve written extensively about this problem )

Here’s the brutal truth: current AI architectures fundamentally cannot attribute their outputs to specific training data.

When Claude or GPT generates text, that knowledge is diffused across billions of neural network parameters. There’s no metadata layer saying “this sentence came from The Guardian, that insight from Nature.” By design, attribution to pre-training data isn’t possible without a fundamental architectural shift—perhaps something like attaching metadata to model weights themselves.

This means the only reliable way to provide attribution right now is through explicit grounding: the AI must synthesize its answer after retrieving specific sources (search results → page content → generated answer). This is why Google’s approach of grounding in web search results is the right architecture for attribution, while generate-first approaches are technically incapable of fair compensation.

Here’s a framework that realigns all stakeholder incentives:

1. Micropayments for Grounded Content When an AI grounds its response in actual content retrieval—fetching and using a publisher’s article to generate an answer—that publisher receives a small licensing fee comparable to an ad click value. This isn’t charity; it’s paying for the intellectual property the AI is using in real-time.

2. Ad-Free Attribution Traffic The publisher doesn’t show ads on pages when users click through from AI-attributed results. Why? Because they’ve already been compensated through the micropayment. This improves user experience and removes the perverse incentive to maximize ad impressions over content quality.

3. Hyper-Contextual AI Answer Monetization AI platforms (Google, Microsoft, Anthropic, OpenAI) recuperate the cost of content micropayments by monetizing the AI answer itself through advertising. But these aren’t the intrusive banner ads users hate—they’re hyper-relevant ads matched to the exact query, at the exact moment of intent.

For the ML and infrastructure community to make this work, several pieces need to fall into place:

AI systems must retrieve and ground before or during generation, not after. This is the only technically feasible way to provide reliable attribution with current technology. Generate-then-ground approaches are insufficient for fair compensation.

The good news? This infrastructure is being built right now. Cloudflare’s Net Dollar initiative, Google’s Agents-to-Payments (AP2) protocol , and the X402 Foundation are all working on exactly this type of micropayment infrastructure.

How do we prevent low-quality or AI-generated spam from gaming the system to farm micropayments?

We don’t need to solve this—it’s already solved. This is a search quality problem, not an AI problem. Google, Bing, and other search engines have spent two decades building:

The AI layer sits on top of an already-filtered corpus. If content is spammy enough to game micropayments, it’s already being demoted by core search quality systems and won’t be retrieved for grounding in the first place.

For major publishers: Custom negotiated licensing deals (like Spotify with major labels). News Corp, Nine Entertainment, ABC, Guardian—these organizations will want structured agreements reflecting their scale and influence.

This doesn’t need to be perfect on day one. It needs to be fair enough to be sustainable and transparent enough to be trusted.

For Australian publishers, this is existential. Our media landscape is already concentrated, with News Corp and Nine dominating. Regional journalism is dying. The ABC is under constant budget pressure.

When international AI platforms harvest Australian content without compensation, they’re extracting value from our information ecosystem while contributing nothing back. This is particularly acute for:

CAPS provides a framework where quality Australian content gets compensated regardless of traffic volume. A regional paper’s investigative report that AI uses to answer queries across the country gets paid—even if users never visit the site.

This isn’t just theoretical. Major infrastructure players are actively building the foundations:

Cloudflare’s Net Dollar – A micropayment system designed specifically for AI-driven internet interactions. Cloudflare processes ~20% of all web traffic; if anyone can implement universal micropayments, it’s them.

Google’s AP2 Protocol – Agents-to-Payments protocol for autonomous AI agents to transact with web services. This is Google acknowledging that the agentic web needs an economic layer.

X402 Foundation (Cloudflare + Coinbase) – Building open standards for AI-to-web payment infrastructure.

Content signals and AI policies – Cloudflare and others are developing standardized ways for publishers to signal usage preferences and pricing to AI systems.

These aren’t press releases—they’re actual technical infrastructure being deployed. The economic plumbing for CAPS is being installed right now.

This is a call to the technical community, policy makers, and industry leaders:

I’m not naive enough to think I can dictate technical architecture to you. Instead, I’m posing the challenge: How do we build reliable, scalable attribution systems that enable fair compensation?

Google, Microsoft, Anthropic, OpenAI—you have the power to implement this. You also have the motivation: regulatory pressure is mounting, litigation is expensive, and killing your content sources is unsustainable.

Early movers get goodwill and competitive advantage. Late movers get regulated.

Engage constructively. Yes, traffic is declining. Yes, AI feels threatening. But blocking AI is choosing irrelevance. CAPS provides a framework where your quality content generates sustainable revenue regardless of traffic patterns.

This needs guardrails and standards, but not heavy-handed regulation that stifles innovation. Focus on:

I’m putting this framework forward not because I think I can single-handedly move the needle—I’m a realist about my influence —but because the Australian SEO and digital publishing community needs a coherent technical vision to advocate for.

Too many agencies are peddling hot air and fluff about “AI disruption” without proposing actual solutions. Too many thought leaders are either doom-posting about AI destroying the web or blindly cheerleading innovation without acknowledging the economic damage.

CAPS is a concrete proposal. It’s technically feasible with current infrastructure. It aligns incentives. It preserves quality content creation while embracing AI’s benefits.

The conversation needs to move from “AI is ruining publishing” to “here’s how we build a sustainable AI-era content ecosystem.”

Nick LeRoy raised several sharp questions that deserve direct answers. Some of these have clear solutions within the CAPS framework; others remain genuinely open problems.

Love this post and I think it makes a ton of sense for a traditional publisher. I wonder though, how it would work for govt properties, edus, and I assume it benefits the established. If I start a new site, what threshold do I have to meet to start getting paid (assuming it…

Government and educational institutions present a unique case because they’re not profit-motivated content creators yet they produce enormous volumes of high-quality, authoritative content that AI systems heavily rely on.

The short answer: They don’t need to participate in micropayments the same way commercial publishers do.

Government content (.gov) is publicly funded and exists to serve citizens. If AI systems ground answers in ABS statistics, legislation.gov.au, or health.gov.au content, there’s no obvious injustice in that usage taxpayers already paid for it. The same logic applies to much educational content, particularly from public universities.
