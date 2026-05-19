---
source: https://www.searchpilot.com/resources/blog/wayfairs-framework-for-picking-seo-tests
title: Wayfair's Framework for Picking SEO Tests
scraped: 2026-03-22
published_on: 2026-01-23
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Wayfair's Framework for Picking SEO Tests

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/wayfairs-framework-for-picking-seo-tests
Published: 2026-01-23
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
I hosted this webinar with Rodney Perez, Global SEO Manager at Wayfair, because I keep hearing the same thing from smart SEO teams: 'coming up with good test ideas is the hard part.'

## Extracted Body
I hosted this webinar with Rodney Perez, Global SEO Manager at Wayfair, because I keep hearing the same thing from smart SEO teams: 'coming up with good test ideas is the hard part.'

Rodney's team has been doing this at scale for a long time, so I wanted to unpack the messy middle: where ideas come from, how they turn into hypotheses, how they get picked, and how results get shared so the whole company pays attention.

What follows is a recap of the main themes from that conversation.

Strong test ideas start with people: curiosity, pattern recognition, and the habit of noticing shifts in search results, changes made by competitors, and variations in on-site performance.

Capture ideas early , then turn them into debatable hypotheses using a simple 'if, then, because' structure.

Prioritise without fake precision: use lightweight RICE scoring (Reach, Impact, Confidence, Effort) with sizing (S, M, L, XL), then sanity-check the output to catch bias.

A good test plan makes execution smoother: clear hypothesis, test type, group balancing, duration and buffers, primary KPIs plus guardrails, implementation detail, risks, and live monitoring so you can pivot if needed.

Reporting is how experimentation spreads: write a high-level 'test read' with an executive summary, share results across the business (wins and failures), and let the best stories travel upward into leadership conversations.y.

Wil opened with a warning I want more people to internalize: broad claims about AI traffic often say more about the dataset than the world.

He has cross-client data broken down by industry, and his view did not match the recent 'ChatGPT traffic is down' narrative. In his numbers, overall volume was strong, while some verticals (like SaaS) were down. So two people can look at real data and walk away with opposite conclusions, because their sample is skewed.

The point was not 'trust my numbers'. The point was: default to nuance. Segment before you generalize, and treat industry-level differences as the starting point, not an edge case.

If your idea backlog is weak, your testing cadence turns into busywork. You ship lots of changes, learn little, and trust erodes.

Rodney framed ideation as a team habit, not a once-a-quarter brainstorm. The best ideas tend to come from people who stay curious, notice patterns, and keep asking 'why is that happening?' while they do normal work: watching search results, reviewing performance, talking to product and engineering, and seeing what competitors are doing.

Rodney described a setup where SEO analysts do most of the ideation work, with a data analyst partnering closely to design tests and write up results.

That structure matters because it keeps ideation connected to execution. The people proposing tests are close to the data, and the people doing the statistical work are involved early enough to shape the plan, not handed a half-formed idea at the end.

Some ideas 'bubble up' from day to day pattern recognition: a competitor starts doing something new, a template behaves oddly in Search Console, a page type stalls, or a new feature launches and you want to know if it helps.

Other ideas come from deliberate planning sessions. Wayfair runs planning cycles (Rodney mentioned every six months) where SEO, product, and engineering sit together and trade notes: what each team is building, what changed recently, what failed before, what might be worth revisiting, and what they could learn from each other. The key is that it is not only improvisation and not only a rigid backlog review. It is both.

Rodney talked about maintaining a backlog document so those 'oh, we should test that' moments do not vanish after the meeting ends. Then, when cross-functional sessions happen, they bring the backlog in, while still leaving room for new ideas created live by bouncing thoughts around the room.

He gave a relatable example outside of work (crossing a street and predicting what happens). The point was that humans already think this way. The framework simply forces clarity: what change are we making, what outcome do we expect, and why do we believe it. Early on, the team writes rough versions. Later, the test plan tightens them into something precise, tied to a KPI and an SEO mechanism (bots, users, or both).

Wayfair uses RICE scoring (Reach, Impact, Confidence, Effort) to compare ideas against each other.

They keep effort sizing lightweight (S, M, L, XL) rather than pretending to estimate exact engineering hours up front. Then they do what Rodney and I both think is non-negotiable: a sense check after scoring, because people can accidentally bake bias into the inputs (everyone wants their idea to look like 'XL impact'). The score helps create a shared language; the gut check helps prevent the score from becoming the boss.

I asked whether they use their history of tests to guide what to do next, and Rodney confirmed they do.

The backlog is not only a list of things to try. It is also evidence you can reference when you are building a roadmap and need to justify impact assumptions. If a class of tests has produced winners before, that can raise confidence. If something has consistently failed, that can save months of repeating the same mistake with new packaging.

Rodney laid out what they include so execution is clean across SEO, product, engineering, and the data partner.

It starts with the hypothesis, plus the test type, how groups will be balanced, which KPI will be used for balancing, test duration, and whether to include buffer periods. He also called out a real-world problem everyone recognises: major search changes can land mid-test, so you need to plan for that risk rather than pretend the environment is stable.

Beyond the main KPI, Rodney emphasised guardrail metrics and potential risks.

He used an example many ecommerce teams will recognise: adding short introductory copy above the main content. It can help users understand the page and can expand keyword coverage by adding synonyms and context. In that case, keyword coverage and impressions might be primary indicators, while page experience and user behaviour changes become guardrails. The point is not to measure everything, it is to avoid shipping a 'win' that quietly hurts something you care about.

If a test group is clearly down massively, you do not keep running it for weeks out of stubbornness. You pause, investigate what caused it, and iterate. This sounds obvious, yet lots of programs skip this and only look at results at the end, when the damage is already done and the time is already wasted.

When we shifted to reporting, Rodney called the test read the core building block for leadership communication.

It packages what happened in a high-level way first (an executive summary), then backs it up with the details that make the result trustworthy: how it was balanced, duration, whether there was a core update, what the primary KPIs did, and what level of statistical confidence they have (or if it is directional). Wayfair shares these results broadly across the company, including failed tests, so teams learn together instead of repeating mistakes in parallel.

One of my favourite moments was Rodney describing how results can show up far beyond the SEO team.

Test outcomes get passed to leadership through normal reporting lines, and sometimes become part of bigger narratives about business performance. He mentioned the experience of seeing SEO test results referenced in leadership contexts like investor communications. That only happens when the testing program is consistent, the write-ups are clear, and the organisation trusts the method.

Rodney shared a concrete example of internal storytelling: noticing that PLP traffic was changing, then proving why.

He described larger SERP presentation shifts they started noticing around August 2023, where classic blue links gave way to more product packs (what many teams think of as organic shopping-style placements - see our recent webinar on the topic and my interview with ecommerce expert Brodie Clark ). That pushes users more directly toward product pages, which changes what matters most on-site. Their message to the business was simple: pay attention to PDPs and to the feeds and structured data that influence how products appear in these layouts.

We also talked about a nuance that can confuse teams in product search.

In some Merchant Center contexts, an 'impression' can be triggered by an interaction that feels like a click (you click a product in the grid and you are still on Google). The click to your site happens later. Rodney agreed this can make impressions a useful early signal, especially because it is higher volume than site clicks. He also pointed out that brand awareness can influence those early interactions, since Google shows the merchant name and users may be choosing based on trust, not only the photo.

Rodney described a mix of formal touchpoints (reviews, structured meetings) and informal learning through discussion and feedback. His emphasis was on coaching: understanding each person's strengths, helping them build confidence in pattern recognition and reasoning, and learning together rather than treating training like a one-way lecture.

A thread running through all of this is that search can be your biggest channel while still feeling hard to steer. Metrics can be weird, search results keep shifting, and even good ideas die without a clean way to test and share results.

SearchPilot makes SEO (and GEO) testable so leaders can move from guessing to knowing.

We run controlled experiments across category pages, product detail pages, navigation, and content, then deliver clear uplift with timelines and confidence. Teams progress from quick validation to a steady test cadence to full control, turning search into a performance channel you can plan and fund.

For ecommerce teams focused on product grids, Merchant Center feeds, and variant handling, the first step is a focused test plan. Measurement tracks impressions, clicks, and revenue so leaders can see the real impact.

Stop trying to predict the future. Experiment to discover it. If you want tailored test ideas for your top PLPs and PDPs, schedule a demo and we’ll share a starter list and a clear path from validation to velocity to control.
