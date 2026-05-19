---
source: https://dejan.ai/blog/googles-new-url-context-tool/
title: Google’s New URL Context Tool
scraped: 2026-03-25
published_on: 2025-05-21
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

# Google’s New URL Context Tool

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/googles-new-url-context-tool/
Published: 2025-05-21
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Google’s just released a new system which allows Gemini to fetch text directly from a supplied page. OpenAI had this ability for a while now, but for Google, this is completely new. Previously their models were limited to the Search Grounding tool alone. Gemini now employs a combination of tools and processes with the ability […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Google’s just released a new system which allows Gemini to fetch text directly from a supplied page. OpenAI had this ability for a while now, but for Google, this is completely new. Previously their models were limited to the Search Grounding tool alone.

Gemini now employs a combination of tools and processes with the ability to search the web and then deeply “read” specific webpages. This allows it to ground its responses in real-world data. Let’s explore two key internal capabilities: a search tool and a browsing tool (URL context) , and understand how they interact, especially when “Grounding with Google Search” is enabled.

🚨BIG UPDATE FOR SEO🚨 ✅Gemini App can get content from live pages. ✅Gemini via API and URL grounding now does too.* ❌ AI Mode does not. *Spotted by @RedCardinal https://t.co/FSAIgEdnOT

At its heart, Gemini’s ability to understand the internet relies on what can be termed “URL Context.” This means it can take a specific web address (URL), access its content, and understand what’s written there. For an AI like Gemini, this is often managed through an internal function, let’s call it browse for simplicity.

What this browse tool does: When Gemini is provided with one or more URLs, it uses this browse capability to visit each page. It then extracts the main textual content and the page’s title. This is akin to the AI carefully reading a specific document.

An Example of browse in Action: Imagine a user asks Gemini: “Can you summarize the article at https://dejan.ai/blog/gemini-grounding/ ?”

Gemini’s internal process would then involve executing a command similar to this:

With this information, Gemini can then synthesize a summary for the user, citing the article as the source for its information.

But what happens if the user doesn’t provide a specific URL? For instance, a query like: “What AI models does Dejan AI offer?” This is where Gemini’s search capability, perhaps through an internal tool like concise_search , becomes essential.

What this concise_search tool does: It takes the user’s query, performs a web search, and returns a list of relevant URLs, typically with snippets of content. This is like Gemini consulting a vast digital library catalog.

An Example of concise_search : For the query “dejan ai models” , Gemini would internally execute:

The Output (as seen above): Gemini receives a list of search results. For “dejan ai models,” these results include links to DEJAN’s “Our Models” page, Dan Petrovic’s Hugging Face profile listing various models, and an article about LinkBERT. These results often point to URLs like https://vertexaisearch.cloud.google.com/... , which are part of Google’s infrastructure for providing grounded search results.

When “Grounding with Google Search” is enabled for Gemini, it doesn’t just pick one tool over the other; it orchestrates a sophisticated workflow. This is guided by a set of internal instructions that tell Gemini how to combine these capabilities.

Understanding this process reveals how crucial high-quality, clearly structured content is:

By combining broad web search with deep reading of specific pages, Google’s Gemini can provide answers that are not only comprehensive but also grounded in the information available on the internet, making it a powerful tool for information retrieval and synthesis.

No. Our tests suggest Google fetches page information from internal storage. A server logger was created for the purpose of testing. When prompted, Gemini “fetched” the page text but server log files recorded no visit.

Additional test was performed where we changed the title of a page and requested Gemini fetches the latest information from that URL. It returned the old title.

Finally, this very article was published and Gemini failed to fetch its content on request. Instead the same generic tool response was supplied to the model:

“I’m sorry. I’m not able to access the website(s) you’ve provided. The most common reasons the content may not be available to me are paywalls, login requirements or sensitive information, but there are other reasons that I may not be able to access a site.”

In contrast when you send GPT to it there’s clear entry in our log file:

Perhaps by accident, right after prompting Grok there was a bunch of rogue, unsigned requests via: 94.156.41.18, 45.130.33.251, 85.254.114.95, 207.90.46.241, 45.145.136.243 and 157.97.127.99:

I managed to get hold of Gemini’s internal tool instructions:

While the previous sections described Gemini’s internal logic and tools in a more conceptual way, Google also provides specific documentation for developers using the Gemini API. This documentation sheds more light on the official “URL context tool,” which aligns with the browse functionality discussed earlier.

According to Google’s Gemini API documentation, the URL context tool is an experimental feature designed to let developers provide Gemini with URLs as additional context directly within a prompt. The model can then retrieve content from these URLs to inform and enhance its responses. This is particularly useful for a variety of tasks, including:

Developers can leverage the URL context tool in two main configurations:

The Gemini API documentation provides code examples (Python, Javascript, REST) showing how developers can integrate this. For instance, in Python, it involves using google.genai and its Tool types, specifically types.UrlContext .

A key aspect highlighted is the url_context_metadata that can be returned in Gemini’s response. This metadata provides information about the URLs that were retrieved and processed, including their status (e.g., success or failure in retrieval). This metadata can also show the actual URLs that were retrieved, which sometimes might be vertexaisearch.cloud.google.com/grounding-api-redirect/... URLs, indicating that the content was processed through Google’s grounding infrastructure, even if the original URL was different.

As of the documentation, this experimental URL context tool is supported by models such as:

This developer-focused information from the Gemini API documentation confirms the core capabilities discussed earlier: Gemini’s ability to directly process URL content is a fundamental feature, whether invoked by an agent through a browse command or by a developer through the url_context tool in the API. The “Grounding with Google Search” feature then leverages this URL processing ability to provide even more comprehensive and contextually aware responses by first discovering relevant URLs through search.

[…] Purpose: This is an internal code block that shows how external tools are accessed and utilized, primarily Google Search. […]

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
