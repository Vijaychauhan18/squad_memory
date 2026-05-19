---
source: https://www.oncrawl.com/ai/calculating-real-ai-search-ctr-log-files/
title: Calculating your real AI search CTR with log files
scraped: 2026-05-12
tags: elite_article, seo, oncrawl, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# Calculating your real AI search CTR with log files

Source expert/publication: oncrawl
Source homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/ai/calculating-real-ai-search-ctr-log-files/
Published: 2026-05-12

## Why This Matters
“Is our website being cited by ChatGPT?” has to be one of the most popular questions we get from our customers at OMcollective these days. It is the new frontier of digital visibility, but many brands are currently measuring the wrong thing. Analytics tools only show a few referr

## Extracted Article Passages
- “Is our website being cited by ChatGPT?” has to be one of the most popular questions we get from our customers at OMcollective these days. It is the new frontier of digital visibility, but many brands are currently measuring the wrong thing. Analytics tools only show a few referral clicks but are blind to visibility, and prompt tracking tools are simulated data at best.
- To find the truth, we have to look at the server logs. Several months of testing and analyzing, and multiple discussions with Jérôme Salomon from Oncrawl prior to our BrightonSEO talks on this topic, have made it clear that many LLMs use identifiable bots for their retrieval process.
- As Jérôme noted in his research for Oncrawl , bots like ChatGPT-User bot pull content in real time using a method called RAG (retrieval augmented generation).
- The catch is that a bot visit does not automatically mean you were visibly cited in a response. The important takeaway is that the crawl is just the very first step in a rather complex pipeline. It is not proof of visibility, and it is certainly not a guarantee that a user will ever see your brand name.
- To bridge the gap between a bot simply “seeing” your page and a human seeing it, let alone “clicking” it, we need a metric that accounts for the entire journey.
- This is why click-through rate (CTR) is one of the most important metrics to measure your performance in AI search. It filters out the noise of the crawl and focuses on the actual business value generated. To calculate it accurately, however, we first have to clean up the data.
- If you look at your raw logs and simply count the rows where the user agent is ChatGPT-User, you are looking at a “noisy” metric. In our experience, raw counts can overstate actual content retrieval by as much as 40% to 60%. Log files are our best source of truth, but they require an approach that takes the data from “noise to signal” in order to be useful.
- Not every bot visit is a success. If a bot hits a 404 page, a 500 error, or a 301 redirect, no content was retrieved for the LLM to process.
- To get a clean number, you must only count 200 (OK) and 304 (Not Modified) responses. With Oncrawl’s AI Search Lens this clean-up is automatically done for you.
- If you want to find out how many prompts you were part of the answer, you’ll also have to remove session clustering noise.
- AI bots don’t browse like humans. They often crawl a page in rapid-fire bursts, so you might see five log lines from the same IP address for the same URL within one second. These are not five separate “retrievals” for five different users; they are a single visit event. To fix this, we recommend clustering visits from the same IP within a 5-second window into a single session.
- On a recent project, one of our clients saw their “total visits” drop from 12,000 to 7,400 after applying these filters. This 7,400 represents the “clean” retrieval count, the real number of times your content actually entered the AI pipeline. While raw logs can be messy, this filtered data is the most powerful signal an SEO can own.
- Even after you clean your log files, you are still only measuring “retrieval.” This is where things get humbling for many SEOs.
- A study by AirOps analyzed over half a million pages retrieved by ChatGPT across 15,000 different prompts. The results were startling: only 15% of retrieved pages were actually cited in a final response. The other 85% were essentially discarded by the model during the synthesis phase and will only be visible in the “More” section of the right hand pane.
- Figure 1: This visual shows the ‘More’ sources pane in ChatGPT. Notice how many links are hidden here/ These are ‘retrieved’ but not ‘cited’ in the main answer, leading to nearly zero CTR.
- This happens because of a process called fan-out . When a user asks a question, ChatGPT might trigger multiple internal searches to find the best answer. It might pull 20 pages, compare them, and then only use the three most relevant ones to build the final response.

## Retrieval Use
- Use when the task maps to `oncrawl` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

