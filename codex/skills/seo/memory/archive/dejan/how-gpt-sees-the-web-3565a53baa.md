---
source: https://dejan.ai/blog/how-gpt-sees-the-web/
title: How GPT Sees the Web
scraped: 2026-03-25
published_on: 2025-11-13
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

# How GPT Sees the Web

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/how-gpt-sees-the-web/
Published: 2025-11-13
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
A Technical Walkthrough of Web Search, Snippets, Expansions, Context Sizes, and Sliding Windows Many people assume GPT “views” the web the way humans do: full pages, HTML, images, layout, and complete articles. Reality is very different. GPT doesn’t browse. It doesn’t load pages. It doesn’t ingest entire documents. What it sees is controlled, windowed, and […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Many people assume GPT “views” the web the way humans do: full pages, HTML, images, layout, and complete articles. Reality is very different. GPT doesn’t browse. It doesn’t load pages. It doesn’t ingest entire documents. What it sees is controlled, windowed, and heavily restricted.

When GPT requests a web search result, it receives a small structured object :

These snippets behave like compact search-engine result cards.

Each snippet comes with a retrieval ID. GPT can request more with:

Fetches a larger slice of text from the same page , centered around a line number.

Follows an outgoing link from the snippet. The new page is fetched as another snippet, using the same rules as the original search.

Each call retrieves a new window of text. This creates a sliding-window browsing pattern.

In theory: it can see many parts of a page. In practice: no , because of strict limits:

So despite multiple expansions, GPT cannot reconstruct or reproduce entire pages.

Each open call returns only a fixed window, even if the page is thousands of words long.

Everything demonstrated here uses the same Web Search tool available in the Assistants API. Developers enabling Web Search in their assistants get the same capabilities.

In the Assistants configuration panel, developers choose how large the web context should be.

We tested a live page using increasing context sizes and repeated expansions. This illustrates exactly how GPT “walks” through a page using windows.

“From Free-Text to Likert Distributions: A Practical Guide to SSR for Purchase Intent Oct 15, 2025 — by Dan Petrovic” dejan.ai “# Author: Dan Petrovic … ## BlockRank: A Faster, Smarter Way to Rank Documents with LLMs 10 Nov 2025 — by Dan Petrovic” dejan.ai

“Instead of sending a user to one “best” page, Google’s AI Mode assembles an answer from short text extracts … 9 Nov 2025 — by Dan Petrovic” dejan.ai

“Dan Petrovic is the most prominent AI SEO … applies his AEO framework to numerous global brands.” dejan.ai

“Beyond Rank Tracking: Analyzing Brand Perceptions Through Language Model Association Networks Featuring Dan Petrovic … Posted On March 18, 2025” SEO Week

“Large Language Models (LLMs) have revolutionized many areas of natural language processing, and information retrieval is no exception. A promising new paradigm called In-Context Ranking (ICR) leverages the contextual understanding of LLMs to re-rank a list of candidate documents for a given query. However, this power comes at a cost: the computational complexity of the attention mechanism …” dejan.ai

“# BlockRank: A Faster, Smarter Way to Rank Documents with LLMs 10 Nov 2025 — by Dan Petrovic — in Machine Learning Large Language Models (LLMs) have revolutionised many areas of natural language processing, and information retrieval is no exception. A promising new paradigm called In-Context Ranking (ICR) leverages the contextual understanding of LLMs to re-rank a list of candidate documents for a given query. However, this power comes at a cost: the computational complexity of the attention mechanism in LLMs scales quadratically with the length of the input context, making it slow and expensive to rank a large number of documents.” dejan.ai

“How BlockRank Works: A Two-Pronged Approach Based on these insights, BlockRank introduces two key innovations to the standard LLM architecture and fine-tuning process:

BlockRank modifies the attention mechanism to enforce the observed block sparsity. This is achieved by restricting the attention flow as follows: • Document tokens only attend to other tokens within the same document and to the initial instruction tokens. • Query tokens attend to all tokens in the prompt (instructions and all documents) to gather the necessary context for ranking. This structured attention pattern reduces the computational complexity from quadratic (O(n²)) to linear (O(n)), resulting in a significant speed-up in both training and inference.” dejan.ai

“Performance: Faster and More Accurate The BlockRank paper presents a comprehensive evaluation of the method on several standard information retrieval benchmarks. The results are impressive: • State-of-the-art performance: On the BEIR benchmark, BlockRank outperforms existing state-of-the-art listwise rankers like FIRST, RankZephyr, and RankVicuna. • Significant speed-up: BlockRank is 4.7x faster than a standard fine-tuned Mistral-7B model when ranking 100 documents. • Scalability: BlockRank can rank up to 500 documents (≈100 000 tokens) in under a second, with its latency scaling linearly with the number of documents.” dejan.ai

You can see sequential slices, but not all slices , and not the full article.

“## Open-Source Implementation The authors have released the code for BlockRank on GitHub [2], making it easy for researchers and practitioners to use and build upon their work. The repository includes: • The core BlockRank attention implementation in both standard PyTorch and optimized Triton kernels. • The auxiliary attention loss module. • Training and evaluation scripts. • A pre-trained BlockRank model based on Mistral-7B, available on Hugging Face. • A quickstart notebook to help you get started. The code is well-documented and provides a solid foundation for experimenting with BlockRank on your own datasets.

“## Conclusion BlockRank is a significant step forward in making LLM-based in-context ranking more practical and accessible. By identifying and exploiting the inherent structure of the attention mechanism for this task, the authors have developed a method that is both faster and more accurate than existing approaches. The open-source release of the code and a pre-trained model further lowers the barrier to entry for using this powerful technique. As LLMs continue to grow in size and capability, methods like BlockRank that focus on efficiency and scalability will become increasingly important. We’re excited to see how the community will build upon this work and apply it to new and challenging information retrieval problems.

[1] Gupta, N., You, C., … & Yu, F. (2025). Scalable In-context Ranking with Generative Models. arXiv preprint arXiv:2510.05396. https://arxiv.org/abs/2510.05396 [2] BlockRank GitHub Repository. https://github.com/dejanai/BlockRank”

Cancel reply Your email address will not be published. Required fields are marked * Name * Email * Website Save my name, email, and website in this browser for the next time I comment. I am a robot. I am a human. ←Previous: In AI SEO #10 is the new #1 DEJAN AI Marketing Agency AI Rank Privacy Policy | Dan Petrovic | Noli esse malus.”

Switching to High context makes each window taller , so expansions return:

The sliding window becomes more efficient but still cannot reveal the full page.

I’m wondering how the HTML/HTTP response gets transformed into plain text. Presumably, there’s a preprocessing step that extracts the content from the page. I’m curious to understand the limitations of that preprocessing.

Yes. Very similar to that of Google’s and many other RAG solutions out there.

Amazing research! Loved the article. Thank you for sharing. You mention GPT generates a score: “Optional metadata such as date or score”

Do you have any past research on that worth taking a look at? If not, how or what do you know about how that score is generated, what the range of possible values are, and where it’s used?

OpenAI’s classifier scores are internal unfortunately, but Google’s Vertex API still has them.

Prior writings on GPT/openAI grounding: https://dejan.ai/blog/gpt-file_search-tool/ https://dejan.ai/blog/gpt-5-made-seo-irreplaceable/ https://dejan.ai/blog/does-schema-help-with-ai/

Your article’s conclusion—that LLMs interact with the web through highly curated text chunks rather than full HTML pages—is a foundational technical fact for modern AI search.

Questions: Was this analysis performed exclusively using the native Web Search tool within the OpenAI Assistants API, or does it reflect broader observations across different proprietary LLM grounding systems? Are the open() and snippet size limitations consistent across models like GPT-4, GPT-4o, and other vendors?”

“When the model calls open(), how is the window/chunk determined? Is it based purely on a fixed line count, or does the system use any semantic chunking (e.g., stopping the chunk at the nearest H-tag or the end of a complete paragraph) to ensure the returned window is meaningful?”

Can you elaborate on the quality of the plaintext extraction? Are complex elements like semantic tables (not just visual layout tables) or structured data (Schema markup) reliably translated into a usable, consumable plaintext format for the model?”

“As LLMs become truly multimodal, how do you foresee them incorporating image/audio/video context? Will the tool evolve to also return an image/audio/video URL and a descriptive ALT text snippet alongside the main text chunk, or will the visual aspect remain entirely separate?”

“If content producers deliberately try to ‘spam’ or over-optimize the plaintext extraction to force their content into snippets, what defensive measures do you anticipate the LLM providers will implement to ensure quality and relevance?”

Interesting. How important do you think Schema Markup is? for GPT to understand the page better.

I don’t know about “meta descriptions” though, just seems to weak and spammy for them to regard it. And it seems to me they dehumanize the article too, extracting what they need technically in tune with the topic context and how they answer a question. I’d like to know more deeply about how they answer because that will dictate what they’re going to include. “Expanding the window” is the most intreguing question for GEO: does this mean designing content to lead the bot to explore more on that page or on another page, via deeper information pointers? Can we make the bot read more based on what it finds?

The fact it doesn’t follow links is really odd. User experiences and solutions are multipage events, so you’d think they’d progress a little. So much to learn!

Who from does the GPT receive the “small structured objects”? I understand the Chats do not crawl and index content on their own (reasonable), but who does the crawl and provides the data?

The answer seems obvious, but for some reason You are not stating it in the article 🙂

This part? “Everything demonstrated here uses the same Web Search tool available in the Assistants API.”
