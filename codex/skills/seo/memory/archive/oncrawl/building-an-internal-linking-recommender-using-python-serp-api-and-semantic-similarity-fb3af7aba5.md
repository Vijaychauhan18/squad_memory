---
source: https://www.oncrawl.com/on-page-seo/building-internal-linking-recommender-python-serp-api-semantic-similarity/
title: Building an internal linking recommender using Python, SERP API, and semantic similarity
scraped: 2026-03-25
published_on: 2026-02-24
tags: live_feed, phase1_ingest, oncrawl, publication, technical-seo, ai-visibility, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Oncrawl
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Building an internal linking recommender using Python, SERP API, and semantic similarity

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/on-page-seo/building-internal-linking-recommender-python-serp-api-semantic-similarity/
Published: 2026-02-24
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
Learn how to build an internal linking recommender using Python. Discover the step-by-step guide on how to automate link discovery at scale.

## Extracted Body
Internal linking is essential for SEOs because it directly impacts how authority flows across your site, influences user engagement, and affects crawlability and indexation rates as well as user flow efficiency for UX metrics.

However, implementing an effective internal linking strategy at scale can be time-consuming and virtually impossible to do manually. That’s why SEOs are always looking for ways to automate the process.

This article provides a step-by-step guide to building an internal linking recommender : a tool that can suggest the top five most relevant pages for internal linking opportunities, based on a specific URL or a main query.

The goal is to simplify decision-making, improve accuracy in selecting related pages, and create a fully relevant and scalable linking structure.

Internal linking becomes more complex and different challenges arise the larger the site. What works for a 100-page site becomes unmanageable at 1,000 pages and nearly impossible at 10,000+. That brings about three core challenges:

The more URLs there are, the harder it becomes to identify the best linking opportunities in regards to semantic similarity.

Without systematic tracking, some site sections accumulate excessive internal links while others remain orphaned or under-linked.

Internal linking isn’t a one-time task. As you publish new content, existing pages need updated links to maintain relevance. Manual maintenance quickly becomes a bottleneck that limits content velocity.

These issues affect the flow of link equity and make it harder to secure top positions in search results.

The internal linking recommender addresses several of the key challenges. It creates stronger semantic connections among pages, boosting topical authority while automating repetitive work.

The automation frees SEO teams to focus on strategy development rather than manual link placement.

Beyond efficiency, the tool enhances user experience through better navigation and increases engagement. Proper internal linking also allows pages to gain authority without requiring external links, and thus reducing off-page SEO costs. [Case Study] How Prisjakt improved user experience thanks to a better internal linking structure With over 4.6 million product pages, Prisjakt needed to define which product pages they wanted to highlight with their internal linking strategy so as to improve their customers’ user experience. Read the case study Approaches for internal linking There are various methods for internal linking. Each has its distinct trade-offs between accuracy, scalability, and technical complexity. We’ll go through all of them so you can determine which one is the best fit for your specific needs.

The biggest drawback is that it does not create precise semantic connections between content, which can negatively impact topical authority.

Hybrid approach (SERP + semantic similarity) and why it wins

The hybrid approach, combining SERP analysis with semantic similarity, offers the best balance for most sites. It leverages Google’s own relevance signals while maintaining semantic precision, making it the foundation of the internal linking recommender tool we will build in the following sections. The tool will automate most of this process and significantly reduce manual work.

This tool has been tested on several websites and has delivered strong results. You can see examples of performance growth in the images below.

To run the tool, you need Python 3.11 or higher installed and you should install the required libraries (such as openai , scikit-learn , google-auth , etc. ) via the requirements.txt file.

You’ll also need an OpenAI API key for embeddings, a Serper.dev account to scrape SERP results, and Google Service Account credentials to read and write data in a Google Sheet.

If you are not familiar with Python, the libraries, or APIs, the next section provides detailed setup instructions.

This section guides you through setting up and running the tool. We’ll start with a high-level overview of the pipeline, then walk through how to set up and run the tool.

Generates embeddings for the main content in urls_rawdata.csv and stores them in vectorized_urls.csv .

Important note : Content embeddings are cached after the first run, so subsequent executions only process new or changed content, significantly reducing API costs.

The setup process includes five main steps. Follow them in order to make sure everything works correctly.

A virtual environment provides an isolated workspace that keeps your project’s packages separate from other projects and from the system-wide Python installation. This prevents conflicts and ensures everything runs smoothly.

Verification: After activation, your terminal prompt should show (venv) at the beginning.

With your virtual environment activated, install all the required libraries using the following command:

If you encounter a “pip not found” error, use the following command:

Expected output: You should see packages being installed with progress indicators.

In this step, you need to open the config folder and replace the placeholders with your own API keys.

4a. Serper API The first API required for this tool comes from Serper. It provides the SERP data for internal link discovery.

1. Create a free account at [serper.dev](https://serper.dev).

2. Navigate to [serper.dev/api-keys](https://serper.dev/api-keys).

5. Paste the key on a single line with no quotes, spaces, or extra characters.

Tip : The API key should be on a single line without quotes or spaces.

4b. OpenAI API The second API is from OpenAI, which is used for generating embeddings.

Important note : To use the OpenAI API, you need to add credits to your account:

The third thing you’ll need is a Google Cloud service account credential so the tool can read and write data in Google Sheets.

​​The service account needs access to Google Sheets and Drive APIs.

Open the config.py file in the config folder and update the following section:

Replace the values above with your own, like in the example below:

Scrape your pages and add the URLs along with their main content into the urls_rawdata.csv file located in the Files folder.

If you’re new to scraping, check out the article about “ Data Scraping and Custom Fields ” and consider using Oncrawl.

Important note : This step can also be automated as a module within the internal linking recommender tool, but I preferred to keep it manual so you handle it yourself. Automating it could introduce complexities that might disrupt the entire process.

Return to the config.py file in the config folder and update the following line by entering your own website address:

You can also run the scraping on a specific route. For example, if you use “ site:yoursite.com/mag ”, the tool will work only on that particular section of your website.

To improve the quality of the results, it is recommended to prepare a list of URLs to which you do not want to link and update the excluded_urls.txt file. Keep in mind that you can use RegEX in this file as well.

Important note : If you do not want to exclude any URLs, delete the placeholder inside the excluded_urls.txt file.

There are other options in the SERP configuration section, such as MAX_SERP_PAGES , which you can adjust.
