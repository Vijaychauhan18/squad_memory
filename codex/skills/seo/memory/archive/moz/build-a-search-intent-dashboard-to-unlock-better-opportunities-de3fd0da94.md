---
source: https://moz.com/blog/build-a-search-intent-dashboard-to-unlock-better-opportunities
title: Build a Search Intent Dashboard to Unlock Better Opportunities
scraped: 2026-03-23
published_on: 2024-08-29
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Build a Search Intent Dashboard to Unlock Better Opportunities

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/build-a-search-intent-dashboard-to-unlock-better-opportunities
Published: 2024-08-29
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
If you’ve ever labored for hours classifying keywords by topic and search intent, only to end up with a ton of data you don’t really know what to do with, then this post is for you.

## Extracted Body
If you’ve ever labored for hours classifying keywords by topic and search intent only to end up with a ton of data you don’t know what to do with, then this post is for you.

I will share how to take all that sweet keyword data you’ve categorized, put it into a Power BI dashboard, and start slicing and dicing to uncover a ton of insights.

Every great search analysis starts with keyword research, and this one is no different. Moz Keyword Explorer offers some incredible features to help with keyword research:

Ranking Keywords By Site : Start with your site's analytics to find search terms driving clicks and (hopefully) conversions.

Keyword Suggestions : Discover a wealth of suggested terms, questions, and phrases related to your search terms.

Keyword Lists : Expand your keywords by adding modifiers and combining terms directly within Moz, offering a simpler way to manage and grow your keyword strategy.

SERP Analysis : Pull search volume, difficulty, and other vital metrics for expanded keyword Insights.

Search intent : Classify keywords by their intent —whether informational, transactional, or navigational to understand your user’s needs.

STAT : Ideal for handling large datasets. Upload your bulk keyword list and use STAT’s robust analytics to pull keyword data and SERP features.

Please note that while these tools are a great way to scale keyword collection, they require you to clean your data to ensure that all keywords are at least somewhat relevant to your business and audience.

Once I have built an initial keyword list, I’ll upload it to STAT and let it run for a few days to get an initial data pull. I can pull the ‘People Also Ask’ and ‘Related Searches’ reports in STAT to further refine my keyword list. I aim to get to at least 5,000 keywords, but the more, the merrier.

For this blog post, I have collected about 19,000 keywords for a client in the "window treatments space."

Bucketing keywords into categories is an age-old challenge for most digital marketers, but it’s a critical step in understanding the distribution of your data.

If you’re doing keyword research, use the robust keyword grouping and filtering capabilities of Moz’s Keyword Explorer. This tool allows you to organize your keywords by categories based on shared lexical similarities or themes identified through Moz’s sophisticated algorithms.

Start by inputting your initial seed keywords into Moz’s Keyword Explorer. This will generate a list of relevant keywords based on your input

Use the tool’s filtering options to narrow down your keywords based on metrics like search volume, difficulty, or relevancy. This step helps you identify the most impactful keywords for further categorization.

Moz offers the ability to explore keyword suggestions that are lexically similar to your seed keywords. You can group these suggestions by varying degrees of lexical similarity, making it easier to see which keywords naturally cluster together around specific topics or themes.

Once you’ve identified clusters of similar keywords , create and manage the lists within Moz. This is particularly useful for keeping your keyword research organized and focused on distinct categories relevant to your client’s business and audience.

Bucketing keywords into categories is an age-old challenge for most digital marketers but it’s a critical step in understanding the distribution of your data. One of the best ways to segment your keywords is by shared words. If you’re short on AI and machine learning capabilities, look no further than the trusted Ngram analyzer. I love to use this Ngram Tool from guidetodatamining.com — it ain’t much to look at, but it’s fast and trustworthy.

After dropping my 19,000 keywords into the tool and analyzing by unigram (or 1-word phrases), I manually select categories that fit with my client’s business and audience. I also make sure the unigram accounts for a decent amount of keywords (e.g. I wouldn’t pick a unigram that has a count of only 2 keywords).

Using this data, I then create a Category Mapping table and map a unigram, or “trigger word”, to a Category like the following:

You’ll notice that for “curtain” and “drapes” I mapped both to the Curtains category. For my client’s business, they treat these as the same product, and doing this allows me to account for variations in keywords but ultimately group them how I want for this analysis.

Using this method, I create a Trigger Word-Category mapping based on my entire dataset. It’s possible that not every keyword will fall into a category and that’s okay — it likely means that keyword is not relevant or significant enough to be accounted for.

Similar to identifying common topics by which to group your keywords, I’m going to follow a similar process but with the goal of grouping keywords by the intent modifier.

Search intent is the end goal of a person using a search engine. Digital marketers can leverage these terms and modifiers to infer what types of results or actions a consumer is aiming for.

For example, if a person searches for “white blinds near me,” it is safe to infer that this person is looking to buy white blinds as they are looking for a physical location that sells them. In this case, I would classify “near me” as a transactional modifier.

If, however, the person searched “living room blinds ideas,” I would infer their intent is to see images or read blog posts about living room blinds. I might classify this search term as being at the informational stage, where a person is still deciding what products they might be interested in and, therefore, isn’t quite ready to buy yet.

There are two ways you can group keywords by intent using Moz’s Keyword Explorer :

Enter a keyword in Keyword Suggestions , such as “Mountain bike.” Next, click filter at the top and enter “near me” to find transactional near me searches ideal for bike shops with a physical location.

Alternatively, you can filter by search intent and drill down to view all transactional keywords related to “Mountain bike”

I followed the same process as building out categories to build out my intent mapping, and the result is a table of intent triggers and their corresponding intent stage.

There are tons of resources on how to get started with the free tool Power BI, one of which is from Seer's founder Will Reynold’s video series on using Power BI for Digital Marketing . This is a great place to start if you’re new to the tool and its capabilities.

Note: It’s not necessarily about the tool (although Power BI is a super powerful one). It’s more about being able to look at all of this data in one place and pull insights from it at speeds that Excel just won’t give you. If you’re still skeptical about trying a new tool like Power BI at the end of this post, I urge you to get the free download from Microsoft and give it a try.

Power BI’s power comes from linking multiple datasets together based on common “keys." Think back to your Microsoft Access days, and this should all start to sound familiar.

First, open Power BI and you’ll see a button called “Get Data” in the top ribbon. Click that and then select the data format you want to upload. All of my data for this analysis is in CSV format, so I will select the Text/CSV option for all of my data sources. You have to follow these steps for each data source. Click “Load” for each data source.

In the Power BI ribbon menu, click the button called “Edit Queries." This will open the Query Editor, where we will make all of our data transformations.

The main things you’ll want to do in the Query Editor are the following:

Make sure all data formats make sense (e.g., keywords are formatted as text, numbers are formatted as decimals or whole numbers).

Create a domain column in your Top 20 report based on the URL column.

Close and apply your changes by hitting the "Edit Queries" button, as seen above.

On the left side of Power BI is a vertical bar with icons for different views. Click the third one to see your relationships view.

In this view, we are going to connect all data sources to our ‘Keywords Bridge’ table by clicking and dragging a line from the field ‘Keyword’ in each table and to ‘Keyword’ in the ‘Keywords Bridge’ table (note that for the PPC Data, I have connected ‘Search Term’ as this is the PPC equivalent of a keyword, as we’re using here).

The last thing we need to do for our relationships is double-click on each line to ensure the following options are selected for each so that our dashboard works properly:

We are now ready to start building our Intent Dashboard and analyzing our data.

In this section, I’ll walk you through each visual in the Search Intent Dashboard (as seen below):

Axis: I’ve nested the URL under Domain so I can drill down to see this same breakdown by URL for a specific Domain

Filter: Top 10 filter on Domains by count of distinct keywords

Value: Count of distinct keywords, shown as a Percent of the grand total
