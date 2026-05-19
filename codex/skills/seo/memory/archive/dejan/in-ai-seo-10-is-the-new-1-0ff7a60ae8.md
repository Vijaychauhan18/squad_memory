---
source: https://dejan.ai/blog/in-ai-seo-10-is-the-new-1/
title: In AI SEO #10 is the new #1
scraped: 2026-03-25
published_on: 2025-11-09
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

# In AI SEO #10 is the new #1

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/in-ai-seo-10-is-the-new-1/
Published: 2025-11-09
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Instead of sending a user to one “best” page, Google’s AI Mode assembles an answer from short text extracts (snippets) taken from multiple sources on the first results page. Our study compares those extracted snippets with their full source pages and checks where in the SERP those sources sit. AI tends to rely on several […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Instead of sending a user to one “best” page, Google’s AI Mode assembles an answer from short text extracts (snippets) taken from multiple sources on the first results page. Our study compares those extracted snippets with their full source pages and checks where in the SERP those sources sit.

AI tends to rely on several page-one results at once; the supplied snippets are often more on-point for the query than the broader page; and sheer length of a page doesn’t make it more likely to be used. Because the model pulls from many page-one listings, a result sitting in position ten can still be surfaced alongside position one inside the same AI answer.

The piece frames this as a shift in distribution: what gets seen by the model (a tight, representative passage) matters as much as the overall page, and “page one” functions more like a pooled source list than a ranking podium.

Abstract — We analyze 213 model responses comprising 1,394 snippet–page pairs to quantify how well retrieval “snippets” align semantically with user prompts compared to their source pages. Using embedding-based cosine similarity, snippets are, on average, more aligned with prompts than the full pages they come from (Δ = cos(p,s) − cos(p,g) = 0.0247 , 95% CI [0.0219, 0.0276], t = 16.91, p = 8.79×10⁻⁵⁹; Cohen’s d = 0.453). Alignment remains largely stable as the number of retrieved sources increases (Pearson r between N and mean cos(p,s) = 0.045 ). Relevance is concentrated: the median top‑1 similarity share per response is 0.172 , and a median k = 5 top snippets cover 80% of cumulative prompt↔snippet similarity. Diff‑based residual analyses were excluded due to instability. Results support retrieval settings that emphasize top‑k snippets (≈5–7) and snippet‑level scoring for reranking and summarization.

Systems that cite grounding sources often surface short “snippets” from web pages. Whether those snippets faithfully capture the prompt‑relevant content—and how that changes with the number of sources—matters for both user trust and summarization quality. We evaluate semantic retention using embedding-based similarity over a mined dataset of prompts, snippets, and source-page texts. We exclude a separate LLM diff–tagging experiment due to reliability concerns.

Prompts were mined via a search‑tool workflow that stores raw model outputs and parsed snippet sources in a local SQLite database. Pages were fetched and cleaned, yielding prompt–snippet–page triplets for analysis. Embeddings were computed with google/embeddinggemma‑300m and cosine similarity was used for alignment metrics. Full workflow and metric computation are implemented in the analysis app and embedding utility; the raw miner app populates the database. app embed miner

Let p be the prompt, s a snippet, and g its source page. We compute:

Interpretation. Snippets are consistently more prompt‑aligned than their source pages. The effect is statistically decisive and practically non‑trivial.

Interpretation. Increasing sources does not erode average snippet alignment; the relationship is near‑flat.

Interpretation. A small head of highly aligned snippets dominates. Roughly five top snippets suffice for most of the achievable alignment signal.

Across 213 prompts and 1,394 snippet–page pairs, snippets are systematically closer to the prompt than their full source pages, with a moderate effect size and overwhelming statistical support. Alignment scales neutrally with the number of sources, while usefulness is concentrated in a small head: about five top snippets capture most of the alignment signal. These findings justify retrieval strategies that (i) privilege snippet‑level scoring, (ii) summarize from a compact top‑k set, and (iii) monitor Δ and k₈₀ as operational quality indicators.

This is a histogram showing how well snippets represent their full source pages. The x-axis shows similarity scores from 0 to 1 (where 1 is perfect match), and the y-axis shows how many queries fall into each range. The red dashed line marks the average at 0.916, meaning snippets capture 91.6% of their source page’s meaning on average. Most bars cluster on the right side, showing high similarity.

If your data shows high similarity (most bars on the right, above 0.9): Your content structure is working well. Google can extract representative snippets from your pages. Keep doing what you’re doing.

If you see scores below 0.8: You have a problem. Your snippets don’t accurately represent your pages, which means:

Action: Find the pages with low representativeness scores (bottom 20%) and audit them. Look for pages that jump between multiple topics or bury important information. Restructure these pages to have clear, focused sections.

This scatter plot compares overall search quality to snippet quality. Each dot represents one query. The x-axis shows how well the entire set of search results matches the query. The y-axis shows how well just the snippets match the query. The red diagonal line represents “equal performance” – dots above the line mean snippets perform better than overall results. Colors show snippet-page similarity (yellow = high, purple = low).

If most dots are on or above the diagonal line: Your snippet extraction is working well. Snippets are as good as or better than full results for matching queries. This is ideal for AI visibility.

If many dots fall below the line: Your full search results are better than their extracted snippets. This means:

Action: For queries where dots are far below the line, identify which pages were returned. Check where the most valuable content is located on those pages. Restructure to move key information to the top or into clearly marked sections with descriptive headings.

This bar chart shows how many snippets Google typically returns per query. The x-axis lists the number of snippets (1 through 10), and the y-axis shows how many queries returned that count. You can see most queries return either 4, 8, or 10 snippets. Very few queries return just 1-3 snippets. The average is 6.5 snippets per query.

This fundamentally changes SEO strategy. Google shows Gemini multiple snippets (average 6.5), not just the top result. This means:

Action: Stop obsessing over position 1 for every keyword. Instead:

This scatter plot directly compares snippet quality (x-axis) to full page quality (y-axis) for each query. Each dot is one query. The black diagonal line means “equal quality” – dots above the line mean full pages performed better than snippets, dots below mean snippets performed better. The colors show snippet-page representativeness (red = high, blue = low). Most dots cluster along or below the diagonal.

Dots below the line (snippets win): Your extraction is adding value by focusing content. The snippet is more relevant than the bloated full page. This is good.

Dots above the line (pages win): Full pages are more relevant than their snippets. This happens when:

Most dots should be red/orange colored: This means even when snippets are more focused, they still accurately represent the full page content.

This box plot shows whether having more snippets per query hurts or helps quality. Each green box represents queries grouped by snippet count (1, 2, 3, etc.). The box shows the range of quality scores for that group – the line in the middle is the median, the box shows the middle 50% of values, and circles show outliers. The y-axis measures snippet-page representativeness from 0 to 1.

Key finding: Quality stays consistently high across all snippet counts. More snippets does NOT dilute quality.

Action: Review your content strategy. If you’re trying to create one massive comprehensive article to dominate a topic, consider splitting it into 3-5 focused articles targeting related queries. Each can rank page one and contribute to AI answers.

This heatmap shows how different metrics relate to each other. Each cell shows the correlation between two metrics. Red means positive correlation (when one goes up, the other goes up), blue means negative correlation (inverse relationship), white means no correlation. The numbers show correlation strength from -1 to +1. The diagonal is always 1.0 because everything correlates perfectly with itself.

sim_prompt_all and snip_mean (0.93): Strong positive correlation. When overall search quality is high, snippet quality is high. This is expected.

page_std and snip_page_mean (-0.65): Strong negative correlation. When page similarity scores vary wildly (inconsistent quality across pages), snippet-page alignment suffers. This tells you inconsistent pages produce worse snippets.

n_snippets and everything else (around 0.05): Almost no correlation. Number of snippets doesn’t predict quality. More is not better or worse.

Action: Audit your pages for topical consistency. Pages that jump between multiple unrelated topics or mix quality levels will hurt snippet extraction. Split them into focused single-topic pages.

This histogram shows “semantic tension” – the mathematical difference between how well a snippet matches a query versus how well the full page matches. The x-axis shows delta values (positive means snippet wins, negative means page wins). The red line at zero represents equal performance. The orange dashed line shows the average delta of +0.0253. The yellow box highlights that 67.6% of snippets have positive delta (they outperform their source pages).

Data: 1,394 individual snippets from your granular CSV file.

This is THE critical metric for AI visibility. Positive delta means Google’s extraction is working – it’s pulling the most relevant parts and giving them to Gemini.

Negative delta cases (32.4%): The full page is more relevant. This happens when the query needs information from multiple sections or context from elsewhere.

Action: Audit pages with negative delta. Your most valuable content is probably buried mid-article or scattered across sections. Restructure to make your best content snippet-friendly (extractable as a coherent 200-300 word chunk).

This line chart shows quality metrics across rank positions 1-10. The blue line (left y-axis) shows how well snippets match queries. The orange line (right y-axis) shows how well snippets represent their source pages. Both lines stay relatively flat across all positions, meaning quality doesn’t significantly drop from position 1 to position 10.

Traditional SEO: You MUST rank top 3 because click-through rates drop dramatically after that.

AI search reality: Positions 1-10 are nearly equal in quality. Google feeds all of them to Gemini.

Action: Review all keywords where you currently rank positions 4-10. These are NOW valuable for AI citations (previously considered “losses”). Stop abandoning these keywords. Instead, invest in maintaining these page-one positions and add more related page-one rankings rather than fighting for position 1 on one keyword.

This scatter plot shows snippet length on the x-axis (in characters) and snippet quality on the y-axis (how well it matches the query). Each dot is one snippet. The colors show representativeness (yellow/green = high). If length mattered, you’d see a clear upward or downward trend – dots moving up or down as you go right. Instead, the dots are randomly scattered with no pattern.

The correlation between length and quality is 0.05 – essentially zero.

Action: Audit your content strategy. If you’re writing long-form content just to be “comprehensive,” stop. Instead, write focused content that directly addresses specific queries, regardless of final word count. A focused 1,500-word article beats an unfocused 4,000-word article for AI visibility.

This histogram shows representativeness scores – how faithfully snippets capture their source pages’ meaning. The x-axis goes from 0 (not representative at all) to 1 (perfectly representative). The y-axis shows frequency. The red line marks the mean at 0.92 (92%). The green box notes that 88.7% of snippets score above 0.9. The distribution is heavily skewed left with most values clustered at the high end.
