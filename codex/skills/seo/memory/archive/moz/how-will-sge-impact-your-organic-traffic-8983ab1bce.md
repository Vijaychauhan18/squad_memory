---
source: https://moz.com/blog/sge-impact-on-organic-traffic
title: How Will SGE Impact Your Organic Traffic?
scraped: 2026-03-23
published_on: 2023-12-12
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

# How Will SGE Impact Your Organic Traffic?

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/sge-impact-on-organic-traffic
Published: 2023-12-12
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Zach discusses Google’s Search Generative Experience, including a step-by-step template that will allow you to estimate the traffic losses or gains your site may experience.

## Extracted Body
Google search is perpetually in a state of flux. Perhaps one of the more dramatic shake-ups in recent years is Google’s introduction of artificial intelligence (AI) capabilities within search results. This feature is known as Google Search Generative Experience (SGE). It is a response to the growing adoption of the now-familiar chat interface of AI tools such as ChatGPT.

As we’ve seen with the introduction of new experiences within Google search results, they can have a wide range of impacts on your organic traffic. Factors such as search intent, your niche, and your current organic keyword rankings will determine SGE’s impact on your site’s organic traffic.

In this article, we will discuss SGE and walk through a step-by-step template that will allow you to estimate the traffic losses or gains your site may experience. Let’s get into it.

Google Search Generative Experience (SGE) is an experimental feature that incorporates AI-generated responses into search results. SGE results are based on web sources and attempt to synthesize them into a succinct response to a search query. SGE results contain links to their sources, as shown below.

These results also contain pre-populated follow-up questions to ask Google’s AI, along with a now-familiar chat interface to give it your own prompts. Google will give you a new, unique response to a follow-up to this topic, such as ‘How do you measure brand authority?’

It's worth noting that not all AI responses will be perfectly accurate. In this case, Domain Authority is a link-centric metric, not related to content quality.

In this case, we again have the confusion about DA being a content metric and the inaccurate suggestion that search engines use DA to determine rankings. Not to our knowledge!

It is important to begin considering the impacts of SGE on your SEO because, as with many SERP and algorithm changes, it presents risks and opportunities. It’s another way Google is keeping searches within its ecosystem while at the same time providing SEOs with a new ‘feature’ to explore and optimize for. Tom Capper covered this in detail in his 2023 MozCon talk, which is available to purchase , or you could always join us at the 2024 event for the live experience.

We’ve already seen Google’s introduction of other SERP (Search Engine Results Page) features impact organic traffic for websites in the past. For example, the introduction of Knowledge Cards led to increases in zero-click search and other risks to organic traffic. Over time, Google has presented its searchers with more and more information right from search results. This has gradually reduced the need for people to click elsewhere and incentivized them to remain on Google’s own site, where they can shop, book flights, click on PPC ads, and more. Now, the ability for users to interact with AI has entered the mix. SGE results, like SERP features, can also have a positive impact on your organic traffic. I f your link is included in the SGE response for a keyword for which you’re not currently ranking, you have an opportunity to gain net new traffic.

Google’s SGE results take up a ton of vertical space in search. Aside from the massive Knowledge Panels users will see when searching the names of top news stories or public figures, we haven’t seen SERP features quite this loud in search results. Google is also pairing Knowledge Panels with SGE components in the same SERP. Searches have the ability to generate an AI response above the Knowledge Panel in this example.

In order to see SGE responses in search results, you will need to have a Google account and enroll yourself in Google Labs .

Even if you are enrolled in Google Labs, SGE results will not appear for every search. This is part of the reason we wanted to conduct this study in the first place — to understand whether SGE will impact our most important keywords.

In order to determine the impact of SGE on your site’s organic traffic, you will need to conduct some research on how SGE may impact your top keywords.

Below, I will describe the steps taken to build this SGE impact model — the assumptions, process, and reasons these decisions were made. We built this tool to help us forecast the impact SGE will have on our own organic traffic internally at Moz.

There is still uncertainty surrounding the rollout of SGE beyond its current pool of experimental testers within Google Labs, but we wanted to prepare forecasts for our organic traffic covering a range of scenarios. We attempted to forecast SGE’s impact from optimistic (SGE phases out) to pessimistic (SGE is present for all Google searches).

We hope that this exercise and the accompanying free template will help you better understand the potential traffic impact of SGE on your own website. First, let’s get into the methodology.

First, we needed to create assumptions about the click-through rates (CTRs) of SERPs as they currently exist, without the presence of SGE. This will help establish a baseline for our keywords and give us something to measure against when we incorporate searches containing SGE.

The quickest way to establish CTR benchmarks is to use the results of a CTR study , such as this example from Advanced Web Ranking. This is a good way to establish data-backed assumptions without having to conduct your own research. This study has been collecting CTR data since 2015 and was updated as of August 2023 at the time of writing.

To create much more unique benchmarks for your own site, Google Search Console is a fantastic source to understand your site’s CTRs by position. This is a simple process if you’re up for following a few more steps.

First, log into your Google Search Console account and export all of your ‘Search Results’ data to CSV, Excel, or, my preference, Google Sheets.

Once you have your data in a spreadsheet, create a new column that is a rounded version of your ‘position’ column, which will include two decimal places. This will give us a clean 1-10 ranking structure to work with. Google Sheets has a =ROUND() formula that makes this easy.

Once you have your Rounded Position column, create a Pivot Table. Highlight your Rounded Position and CTR columns and select Insert > Pivot Table.

In the Pivot Table builder, use Rounded Position as your Rows and CTR as your Value. Remember to summarize your value by ‘Average.’ You can also create a filter to include only Rounded Positions 1—10, as shown below.

You will have a CTR assumptions table that looks a bit like this, serving as an effective and personalized CTR breakdown for your own site.

If you prefer non-branded CTR assumptions only, you can optionally remove your branded search terms from this dataset before creating your pivot table. For this SGE impact exercise, I recommend including branded search terms in your SGE research, as well as your assumptions. This will help you understand the impact SGE may have on the entire scope of your website, including your own product names or brand strength .

When you’ve settled upon your organic CTR benchmarks for positions 1—10, paste them into the ‘CTR Assumptions’ tab of the model in Column B.

This is where things require a bit of creativity. There is no view within Google Search Console for clicks, position, or CTR from Google SGE at the time of writing. This data is not available for Bing’s AI counterpart at this time either. You will not be able to determine the exact CTR for your site from SGE responses, so we will need to come up with our own assumptions. While SGE click-through rate data does not exist within any of Google’s tools available to the public, several studies have measured the CTRs of other SERP features, such as Knowledge Cards, that we can use as a guideline.

While there are several significant differences between existing Knowledge Cards and the new SGE interface, there are also many similarities. These features both generally appear above traditional ‘blue link’ organic results. They both take up screen real estate that would otherwise be occupied by organic links. They both allow users to click through to a website but also present information within the SERP that may eliminate the need to do so.

After Knowledge Cards were introduced, Moz’s research found that page one Knowledge Cards have an average CTR of 12.68% . In our experiments, we used this as our optimistic assumption for SGE click-throughs. In this scenario, SGE results become extremely popular pathways for users to leave Google for third-party websites, with each link in an SGE results carousel capturing a significant portion of available traffic. So, for our analysis of SGE’s impact on Moz.com keywords, we used a top range to our CTR assumption of 12.68%. This value has been built into the template.

How likely is this? In my opinion, not very. But this is why it’s the upper bound of our assumption.

For our pessimistic scenario for SGE, we assumed that the optimistic 12.68% CTR may be diluted by up to 10 links in the AI results. We’ve seen anywhere between 3—10 links in SGE responses.

Optional SGE results occur when you have the ability to generate one at the top of search results, but it does not happen automatically.

If a result is marked as ‘Optional’ in the ‘SGE Response?’ column of the template, we automatically reduce our optimistic and pessimistic CTR forecasts by half, assuming that roughly half of users will elect to generate an SGE response. This assumption can also be modified in the template.

We will assume that organic links will lose the CTR equivalent of one organic search position. In other words, if an SGE box is present, the estimated CTR of a position one keyword will adjust to the estimated CTR of position 2. In this case, the estimated CTR for position one would drop from 24.1% to 9.9%, according to the benchmarks we loaded into column B of our CTR Assumptions tab.

We decided on this adjustment due to similar CTR decrease patterns observed when Knowledge Cards are present.

As of now, there are three possibilities when it comes to SGE visibility in search results. We will have to adjust our estimated CTRs accordingly, depending on whether users see AI responses by default or need to prompt them manually.

This is when an SGE box appears automatically as soon as you search a query.

If a result is marked as ‘Yes’ in the ‘SGE Response?’ column of the template, we assume the full values of our click-through-rate assumptions for SGE detailed above.

If there is no SGE result for a keyword and no ability to generate one, there will be no impact on CTR according to this model. It is perhaps nearly as valuable to understand the keywords where SGE is not a factor so that you can spend your time optimizing for AI responses more efficiently.

Feel free to use these assumptions in your own model. If you find them outrageous, which they may prove to be a few years from now, feel free to disregard them. The free template linked at the end of this article makes it easy to change assumptions for both organic search and SGE click-through rates.

The purpose of this exercise is not to perfectly predict how the general public will interact with SGE. We don’t know that yet, but we have some data points from past changes to Google results to help guide us. The idea behind this exercise is to get an early read on which of your most valuable organic keywords may be impacted by this potential rollout. Moreover, this model will directionally indicate the traffic loss (or gain) you may experience across a range of SGE rollout scenarios.

To perform this analysis, you will need a sample of keywords to work with. Keep in mind that to fill out this template, you will need to manually examine search results for each keyword, so keep your list manageable.

Whatever sample of keywords you choose, make sure you know the percentage of total organic traffic that they represent. Try to analyze a set of keywords that represents at least 50% of your site’s traffic. Keep in mind that for a large site, a keyword set that represents 50% of traffic may contain only high volume and branded keywords, which is not a representative sample of the search internet behind the other 50%. Consider including some lower-volume keywords that are particularly important to your brand or revenue.

This will help you understand the impact SGE will have on the majority of your site traffic and make stronger statements about SGE’s impact to your stakeholders or clients.

Some sites have an extremely long-tail of keyword click volumes, meaning that the majority of your site’s organic search clicks will be spread across thousands of keywords. If this is true for your site, select a number of keywords that will work for you. The larger the percentage of site traffic that you are able to analyze, the stronger your statements will be.

This template requires manual analysis of SERPs for the keywords that you choose. At the time of this writing, there are no tools available to collect data from SGE’s experimental testing stage at scale. That may change in the future, and you will be able to check SGE results for your entire set of keywords automatically. For now, this will require some manual effort.

Export your queries from Google Search Console. You will need the query, clicks, impressions, CTR, and average position to add to the template.

Then, paste your keywords into column A of the template and GSC metrics into columns C—F. This is the only data you will need to manually enter into the Google Sheet before analyzing SERPs unless you decide to change your CTR assumptions.
