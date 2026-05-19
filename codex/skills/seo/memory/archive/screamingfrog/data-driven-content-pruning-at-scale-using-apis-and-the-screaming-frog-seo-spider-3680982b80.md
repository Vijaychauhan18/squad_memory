---
source: https://www.screamingfrog.co.uk/blog/data-driven-content-pruning/
title: Data-Driven Content Pruning at Scale Using APIs and the Screaming Frog SEO Spider
scraped: 2026-03-25
published_on: 2026-01-12
tags: live_feed, phase1_ingest, screamingfrog, screaming-frog, publication, technical-seo, crawling, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Screaming Frog Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Data-Driven Content Pruning at Scale Using APIs and the Screaming Frog SEO Spider

Source: Screaming Frog Blog
Homepage: https://www.screamingfrog.co.uk/blog/
Original URL: https://www.screamingfrog.co.uk/blog/data-driven-content-pruning/
Published: 2026-01-12
Strength: technical SEO, crawling, site architecture, large-site workflows

## Summary
One of the most important projects that comes to mind for SEOs when it comes to crawl budget optimisation and improving topical authority is content pruning. Content pruning refers to the process of removing, merging, or updating low-value or low-traffic content, which helps reduce the volume of poor-quality pages. The...

## Extracted Body
Posted 12 January, 2026 by Liam Lesani in Screaming Frog SEO Spider , AI

One of the most important projects that comes to mind for SEOs when it comes to crawl budget optimisation and improving topical authority is content pruning.

Content pruning refers to the process of removing, merging, or updating low-value or low-traffic content, which helps reduce the volume of poor-quality pages.

The challenge, however, is that content pruning projects are often faced with various difficulties such as identifying pages that can be removed, finding those that need off-page actions or content updates, managing the risk of traffic loss, convincing stakeholders, and more.

In this article, we aim to explain the content pruning process step by step, examine common challenges, and provide practical solutions for executing it effectively.

This article is a guest contribution from Liam Lesani , SEO Team Lead at Welltopia.

When we want to start a content pruning project, we come across several different methods for evaluation. In the following sections, we will go through all of them and finally decide which one suits our case best.

In this method, we usually check everything manually for each URL, such as traffic, publish and update dates, content quality, and so on. We then make the necessary changes right away and store the results in a tool like Google Sheets or Excel.

The main problem with this approach is that it is not scalable. Even if we want to apply it to a medium-sized website with at least ten thousand pages, it becomes practically impossible.

Another issue is that aside from the time it takes, the outcome can be quite subjective. This is especially common when it comes to evaluating content quality. If a team is responsible for this process, things get even more complicated, and the likelihood of human error across the workflow increases.

Another approach for content evaluation is using LLMs and Python, which can work well if implemented correctly, but it usually comes with several challenges.

If I were to summarise the key advantages briefly, they are:

It is generally recommended to use this method alongside the data-driven approach for content updates and merging.

One of the biggest fears SEOs have about large-scale content pruning is traffic loss after the pruning process. This fear usually stems from two main reasons. The first is accidentally deleting pages that actually receive traffic, and the second is a drop in topical authority, which can lead to ranking declines and ultimately lost traffic. In such situations, only a data-driven approach can help because:

The next fear is facing stakeholders and convincing them. This often happens when you have done a manual review, but stakeholders such as a marketing manager or content marketing manager may not approve the pruning project. At this stage, you need to present data to persuade them to give the green light.

In the following sections, I will walk you through, step by step, building a data-driven pruning framework.

This stage consists of two main parts: collecting data from sources such as GSC, GA, and others, and analysing the data based on various metrics like clicks, impressions, and more. We then define scoring and ranking for the content to get a clear view of its performance.

This stage also has two main components: the action plan and the care plan. In the action plan, we define precise actions for each page, such as keep, prune, update, check, or improve. In the care plan, we estimate potential traffic loss if we plan to remove pages that currently receive traffic, identify topics, design a new content strategy, and take measures to minimise traffic loss while ensuring our topical authority within each topic is not harmed.

Coordinate with the technical team to carry out the project. At this stage, it is recommended to prepare a comprehensive document outlining your concerns, the data, and other relevant details, and submit a clear SEO ticket to the technical team.

Keep track of the content you have decided to retain so that, in case of any ranking drops, you can quickly design a recovery strategy if needed.

One of the main reasons that motivated us to create a framework for content pruning is that it allows us to establish an organised system that not only saves us time but also ensures we don’t miss anything.

Over the past few months, I’ve worked on several content pruning projects and realised how much having a structured approach can speed up and simplify content analysis. For this reason, I decided to create a comprehensive Google Sheets template to make my work easier in future projects.

As I mentioned, in addition to the main metrics, we also have three scoring metrics and three flags that we want to use for more accurate ranking and identification of our content. Let’s quickly go through them.

GSC Score: (Clicks per Day × Impressions per Day) ÷ Average Position

By multiplying clicks and impressions, we capture both visibility and engagement. Dividing the result by the average position normalises the score, giving more weight to pages that not only appear frequently but also rank well.

GA Score: [New Users per Day × Page Views per Session × (Average Session Duration × 24)] ÷ Bounce Rate

This metric evaluates the quality of traffic and on-site engagement using GA data. A higher GA Score indicates a page attracts new, highly engaged visitors who interact with multiple pages and spend more time on the site. This score helps identify top-performing pages in terms of user behaviour and engagement quality.

This score measures the relative authority of a page based on its backlink profile. Each page’s strength is normalised against the maximum observed values in the dataset, ensuring a fair comparison. The ½ coefficient balances both components, authority and referring domain count, equally.

We have three flags in total, each calculated as true or false. Outdated applies to posts where the modified date is over a year old, Underperforming applies to posts ranked above position 20 with a CTR below one percent, and Opportunity applies to posts in position 2.5 or better where the CTR is below the CTR Study. By CTR Study, we mean the average CTR for positions equal to or better than 2.5.

In general, five actions have been defined, which you can adjust according to your needs:

Our workflow is very simple. Just add data into the GSC, GA, Ahrefs, and Publish & Update Sheets , and enter the URLs in the Main Sheet . All other metrics will automatically populate using formulas.

For data collection, one of the easiest methods is using the Screaming Frog SEO Spider’s API Access, which allows you to gather data from various sources effortlessly. All you need to do is go to Configuration > Crawl Config > API Access and connect the APIs of the different tools to the SEO Spider.

If you haven’t used this feature before, you can easily learn how to connect each tool through the links below.

In the next step, you need to select the metrics you want from the Metrics section for each tool and set your desired date range.

Tip: Preferably, the data dates for GSC and GA should match. If GA was inactive for the chosen period or only a shorter range is available, make sure to document this in the final document and dashboard you plan to create.

Next, set the SEO Spider’s Mode to List and enter your list of URLs. Then, export the data from the Search Console and Analytics sections and transfer it to your content pruning sheet.

Note: Make sure that the start and end dates you use in the GSC and GA Sheets match the dates you entered in the API Access settings in the SEO Spider.

Finally, enter the list of URLs in the Main Sheet so that all the data is imported automatically.

Visualising data not only gives us a clear overall view, but it is also a powerful tool for communicating with and persuading stakeholders. Relying solely on a table in Google Sheets makes it difficult to convey exactly what is happening and what our goals are.

Additionally, in a platform like Looker Studio, you can create interactive dashboards and customise everything. You can easily use filters and controls, and accessing the data becomes much simpler and more convenient.

The good news is that you don’t have to create visualisations from scratch. There is a pre-designed dashboard that you can easily customise and add any other elements you need based on your project.

As shown in the image, click on the three dots in the top-right corner, then select Make a copy.

First, just like in the images, click on New Data Source and then select Create Data Source.

Next, the list of Looker Studio connectors will appear. Find the Google Sheets connector and click on it.

After that, locate the sheet you want, then in the top right corner click Connect, followed by Add to Report so your data source is added.

Click the Edit button in the top-right corner, then click on any table or section to customise it according to your needs.

When customising a dashboard or creating a new one from scratch, there are a few key points to keep in mind.

Who are you presenting this data to, and which metrics matter most to them? Are you only presenting to the SEO team, or will it also be shown to people with less SEO knowledge?
