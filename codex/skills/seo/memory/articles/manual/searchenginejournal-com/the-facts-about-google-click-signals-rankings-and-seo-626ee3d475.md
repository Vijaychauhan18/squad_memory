---
source: https://www.searchenginejournal.com/the-facts-about-google-click-signals-rankings-and-seo/572827/
title: The Facts About Google Click Signals, Rankings, And SEO
scraped: 2026-04-25
published_on: 2026-04-23
tags: manual_ingest, dashboard, on_demand_capture, searchenginejournal-com
topic: manual_ingest
intent: research, manual_ingest, knowledge_capture, chunk_growth
role: researcher, seo, developer
confidence: medium
canonical: false
canonical_group: Manual URL Ingest - Dashboard
use_for: rapid_knowledge_capture, vector_db_enrichment, article_retrieval
avoid_for: final_strategy_without_manual_review
---

# The Facts About Google Click Signals, Rankings, And SEO

Source: Manual URL Ingest
Publisher Host: searchenginejournal.com
Homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/the-facts-about-google-click-signals-rankings-and-seo/572827/
Published: 2026-04-23
Strength: Instant dashboard capture into durable squad memory.

## Capture Context
- Run ID: `20260425T055241Z`
- Target DB: `/Users/vijaychauhan/squad_memory/squad_memory.db`
- Capture Mode: `dashboard_manual_ingest`

## Metadata
Author: https://www.facebook.com/martinibuster
Schema types: NewsArticle

## Section Outline
- Clicks Are A Raw Signal
- Raw Signals Are Data To Be Further Processed
- How Raw Signals Are Typically Used
- 70 Days Of Search Logs
- What Is Google’s RankEmbed?
- What About Google’s Click Ranking Patent?
- Last Year's Google Ranking Factors Changes, Explained
- Google Validates Leak, Igniting Questions Around Search Transparency
- How To Think About SEO, Content & PR Measurement (Indicated In The Google Leak)

## Summary
How Google's systems treat click data, and the straight facts about what it means for SEO and rankings.

## Extracted Body
How Google's systems treat click data, and the straight facts about what it means for SEO and rankings.

- April 23, 2026
- 8 min read

- 2.1K READS

Clicks as a ranking-related signal have been a subject of debate for over twenty years, although nowadays most SEOs understand that clicks are not a direct ranking factor. The simple truth about clicks is that they are raw data and, surprisingly, processed with some similarity to human rater scores.

### Clicks Are A Raw Signal

The DOJ Antitrust memorandum opinion from September 2025 mentions clicks as a “raw signal” that Google uses. It also categorizes content, human rater scores, and search queries as raw signals. This is important because a raw signal is the lowest-level data point. Raw signals are generally processed into higher level ranking signals or used for training a model like RankEmbed and its successor, RankEmbedBERT.

- Directly observed
- But not yet interpreted or used for training data

The DOJ document quotes professor James Allan, who gave expert testimony on behalf of Google

> “Signals range in complexity. There are “raw” signals, like the number of clicks, the content of a web page, and the terms within a query. …These signals can be created with simple methods, such as counting occurrences (e.g., how many times a web page was clicked in response to a particular query). Id. at 2859:3–2860:21 (Allan) (discussing Navboost signal) “

He then contrasts the raw signals with the signals “at the other end of the spectrum”

> “At the other end of the spectrum are innovative deep-learning models, which are machine-learning models that discern complex patterns in large datasets. Deep models find and exploit patterns in vast data sets. They add unique capabilities at high cost.”

Professor Allan explains that “top-level signals” are used to produce the “final” scores for a web page, including popularity and quality.

### Raw Signals Are Data To Be Further Processed

Navboost is mentioned several times in the September 2025 antitrust document as popularity data. It’s not mentioned in the context of clicks having a ranking effect on individual sites.

> “…popularity as measured by user intent and feedback systems including Navboost/Glue…”

And elsewhere, in the context of explaining why some of the Navboost data is privileged

> “They are ‘popularity as measured by user intent and feedback systems including Navboost/Glue’…”

In the context of explaining why some of the Navboost data is privileged

> “Under the proposed remedy, Google must make available to Qualified Competitors …the following datasets: 1. User-side Data used to build, create, or operate the GLUE statistical model(s); 2. User-side Data used to train, build, or operate the RankEmbed model(s); and 3. The User-side Data used as training data for GenAI Models used in Search or any GenAI Product that can be used to access Search. Google uses the first two datasets to build search signals and the third to train and refine the models underlying AI Overviews and (arguably) the Gemini app.”

Clicks, like human rater scores, are just a raw signal that is used further up the algorithm chain (for example, to train AI models) to improve the matching of web pages to queries or to generate a quality or relevance signal that is then added to the rest of the ranking signals used by a ranking engine or a rank modifier engine.

#### How Raw Signals Are Typically Used

### 70 Days Of Search Logs

The DOJ document makes reference to using 70 days of search logs. But that’s just eleven words in a larger context.

> “70 days of search logs plus scores generated by human raters”

I get it, it’s simple and direct. But there is more context to it

> “RankEmbed and its later iteration RankEmbedBERT are ranking models that rely on two main sources of data: [Redacted]% of 70 days of search logs plus scores generated by human raters and used by Google to measure the quality of organic search results.”

The 70 days of search logs are not click data used for ranking purposes in Google, AI Mode, or Gemini. It’s data in aggregate that is further processed in order to train specialized AI models like RankEmbedBERT that in turn rank web pages based on natural language analysis.

That part of the DOJ document does not claim that Google is directly using click data for ranking search results. It’s data, like the human rater data, that’s used by other systems for training data or to be further processed.

### What Is Google’s RankEmbed?

RankEmbed is a natural language approach to identifying relevant documents and ranking them.

> “The RankEmbed model itself is an AI-based, deep-learning system that has strong natural-language understanding. This allows the model to more efficiently identify the best documents to retrieve, even if a query lacks certain terms.”

It’s trained on less data than previous models. The data partially consists of query terms and web page pairs

> “…RankEmbed is trained on 1/100th of the data used to train earlier ranking models yet provides higher quality search results. …Among the underlying training data is information about the query, including the salient terms that Google has derived from the query, and the resultant web pages.”

That’s training data for training a model to recognize how query terms are relevant to web pages.

> “The data underlying RankEmbed models is a combination of click-and-query data and scoring of web pages by human raters.”

It’s crystal clear that in the context of this specific passage, it’s describing the use of click data (and human rater data) to train AI models, not to directly influence rankings.

### What About Google’s Click Ranking Patent?

Way back in 2006 Google filed a patent related to clicks called, Modifying search result ranking based on implicit user feedback . The invention is about the mathematical formula for creating a “measure of relevance” out of the aggregated raw data of clicks (plural).

The patent distinguishes between the creation of the signal and the act of ranking itself. The “measure of relevance” is output to a ranking engine, which then can add it to existing ranking scores to rank search results for new searches.

> “A ranking Sub-system can include a rank modifier engine that uses implicit user feedback to cause re-ranking of search results in order to improve the final ranking presented to a user of an information retrieval system. User selections of search results (click data) can be tracked and transformed into a click fraction that can be used to re-rank future search results.”

That “click fraction” is a measure of relevance. The invention described in the patent isn’t about tracking the click; it’s about the mathematical measure (the click fraction) that results from combining all those individual clicks together. That includes the Short Click, Medium Click, Long Click, and the Last Click.

Technically, it’s called the LCIC (Long Click divided by Clicks) Fraction. It’s “clicks” plural because it’s making decisions based on the sums of many clicks (aggregate), not the individual click.

- Summation: The “first number” used for ranking is the sum of all those individual weighted clicks for a specific query-document pair.
- Normalization: It takes that sum and divides it by the total count of all clicks (the “second number”).
- Statistical Smoothing: The system applies “smoothing factors” to this aggregate number to ensure that a single click on a “rare” query doesn’t unfairly skew the results, especially for spammers.

> “A base LCC click fraction can be defined as: LCC_BASE=[#WC(Q,D)]/[#C(Q,D)+S0) where iWC(Q.D) is the sum of weighted clicks for a query URL…pair, iC(Q.D) is the total number of clicks (ordinal count, not weighted) for the query-URL pair, and S0 is a smoothing factor.”

That formula describes summing and dividing the data from many users to create a single score for a document. The “query-URL” pair is a “bucket” of data that stores the click behavior of every user who ever typed that specific query and clicked that specific search result. The smoothing factor is the anti-spam part that includes not counting single clicks on rare search queries.

Even way back in 2006, clicks is just raw data that is transformed further up the chain across multiple stages of aggregation, into a statistical measure of relevance before it ever reaches the ranking stage. In this patent, the clicks themselves are not ranking factors that directly influence whether a site is ranked or not. They were used in aggregate as a measure of relevance, which in turn was fed into another engine for ranking.

By the time the information reaches the ranking engine, the raw data has been transformed from individual user actions into an aggregate measure of relevance.

- Thinking about clicks in relation to ranking is not as simple as clicks drive search rankings.
- Clicks are just raw data.
- Clicks are used to train AI systems like RankEmbedBert.
- Clicks are not directly influencing search results. They have always been raw data, the starting point for systems that use the data in aggregate to create a signal that is then mixed into ranking decision making systems at Google.
- So yes, like human rater data, raw data is processed to create a signal or to train AI systems.

Read the 2006 Google patent, Modifying search result ranking based on implicit user feedback .

#### Last Year's Google Ranking Factors Changes, Explained

#### Google Validates Leak, Igniting Questions Around Search Transparency

#### How To Think About SEO, Content & PR Measurement (Indicated In The Google Leak)
