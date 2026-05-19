---
source: https://www.oncrawl.com/content-marketing/building-tools-to-understand-content-performance/
title: Building tools to understand content performance
scraped: 2026-03-23
published_on: 2020-09-03
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

# Building tools to understand content performance

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/content-marketing/building-tools-to-understand-content-performance/
Published: 2020-09-03
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
Content is one of the primary forces driving an inbound marketing strategy, and SEO in an integral part of making that work.

## Extracted Body
Content is one of the primary forces driving an inbound marketing strategy, and SEO in an integral part of making that work. Generally, this will cover the basics of on-page SEO: article structure, keyword placement, meta tags, title tags, alt text, headings, structured data, and use of formatting to create informally structured data in lists and tables.

Auditing on-page SEO as part of content management, using Oncrawl.

This falls under the umbrella of technical SEO when you start to mass-optimize or monitor, whether through site audits or regular crawls, through machine generated natural language meta descriptions, snippet control tags, or structured data injection.

However, the intersection of technical SEO and content marketing is even greater where content performance is concerned: we look at the same primary data, such as page rank on the SERPs, or number of clicks, impressions, and sessions. We might implement the same sorts of solutions, or use the same tools.

Content performance is the measurable result of how the audience interacts with the content. If content is driving inbound traffic, then measures of that traffic reflect how well or how poorly that content is doing its job. Every content strategy should, based on concrete objectives, define its particular KPIs. Most will include the following metrics:

The difficulty is in placing the cursor: what numbers mean that you have good content performance? What is normal? And how do you know when something is not doing well?

Below, I’ll share my experiment to build a “proof of concept” of a low-tech tool to help answer these questions.

Here are some of the questions I wanted to answer as part of my own review of content strategy:

To answer any of these questions, though, you need to know what “normal” content performance looks like on the site you’re working with. Without that baseline, it’s impossible to quantitatively say whether a specific piece or type of content performs well (better than the baseline) or not.

The easiest way to set a baseline is to look at average sessions per day after publication, per article, where day zero is the publication date.

This will produce a curve that looks something like this, showing a peak of initial interest (and possibly the results of any promotion you do, if you haven’t limited your analysis to sessions from search engines only), followed by a long tail of lower interest:

Real data for a typical post: a peak on or shortly after the publication date, followed by a long tail which, in many cases, eventually brings in more sessions than the original peak.

Once you know what each post’s curve looks like, you can compare each curve to the others, and establish what is “normal” and what isn’t.

If you don’t have a tool to do this, this is a pain in the neck.

When I started this project, my goal was to use Google Sheets to construct a proof of concept–before committing to learning enough Python to change how I examine content performance.

To start with, you need to establish a list of the content you want to examine. For each piece of content, you’ll need the URL and the publication date.

You can go about getting this list however you want, whether you build it by hand or use an automated method.

I used an Apps Script to pull each content URL and its publication date directly from the CMS (in this case, Wordpress) using the API, and wrote the results to a Google Sheet. If you’re not comfortable with scripts or APIs, this is still relatively easy; you can find multiple examples online of how to do this for Wordpress.

Keep in mind that you’re going to want to compare this data with session data for each post, so you’ll need to make sure that the “slug” on this sheet matches the format of the URL path provided by your analytics solution.

I find it’s easier to build the full slug (URL path) here, in column E above, rather than modifying the data pulled from Google Analytics. It’s also less computationally heavy: there are fewer lines in this list!

Example formula to create a full URL for this site: look up the category number provided by the CMS in a table and return the category name, which is placed before the article slug, matching the URL pattern for this site (https://site.com/categoryName/articleSlug/)

If you don’t have access to the backend, you can create your list by scraping this information from your website itself, for example, during a crawl. You can then export a CSV of the data you want, and import it into a Google Sheet.

Setting up a data field in Oncrawl to scrape publication dates from a website’s blog.

Data, including URL and scraped publication date, in Oncrawl’s Data Explorer, ready for export.

Next, you need a list of sessions per content piece and per day. In other words, if a piece of content is 30 days old and received visits every day during that period, you want to have 30 rows for it–and so on for the rest of your content.

The Google Analytics add-on to Google Sheets makes this relatively easy.

From the Google Analytics view with the data you want, you can request a report of:

We’re interested in the number of sessions. Landing Pages This lists sessions for each landing page separately.Date This lists sessions for each date separately, rather than giving us a 1000-day total..

Using segments of your Google Analytics data is extremely helpful at this stage. You can, for example, limit your report to a segment containing only the content URLs you are interested in analyzing, rather than the entire site. This significantly reduces the number of rows in the resulting report, and makes the data much simpler to work with in Google Sheets.

Furthermore, if you intend to look only at organic performance for strictly SEO purposes, your segment should exclude acquisition channels which can’t be attributed to SEO work: referrals, email, social…

Don’t forget to make sure that the limit is sufficiently high enough that you aren’t going to truncate your data by mistake.

To calculate the number of days since publication for each data point in the article we have to join (or, if you’re a Data Studio user, “blend”) the data from the sessions report to the data in your list of content pieces.

To do so, use the URL or URL path as a key. This means the URL path needs to be formatted the same way in both the CMS table and the Google Analytics report.

I created a separate table so that I could scrub any parameters off of the landing page in my Analytics report. Here’s how I set up my columns:

Note that my lookup key–the full URL path–is not the leftmost column in my data; I’ve had to shift column E before column C for the purposes of the VLOOKUP.

If you have too many rows to fill this in by hand, you can use a script like the one below to copy the content in the first row and fill in the next 3450 or so:

To calculate normal session numbers, I’ve used a pretty straightforward pivot table, paired with a graph. For simplicity’s sake, I’ve started by looking at the average number of sessions per day after publication.

Here’s the average versus the median of sessions over the 1000 days following publication. Here we begin (?) to see the limits of Google Sheets as a data visualization project:

This is a B2B site with weekday session peaks across the full site; it publishes articles a few times per week, but always on the same days. You can almost see the weekly patterns.

In this case, for visualization purposes, it would probably be best to look at rolling 7-day averages, but here’s quick version that merely smooths by weeks since publication:

Despite this long-term view, for the next steps I’ll be limiting the graph to 90 days after publication in order to stay within Google Sheets’ limits later on:

Now that we know what the average post looks like on any given day, we can compare any post to the baseline to find out whether it is over- or under-performing.

This gets quickly out of “hand” if you’re doing it manually. Puns aside, let’s at least try to automate some of this.

Every post (that is less than 90 days old), needs to be compared to the baseline we’ve just established for each day in our 90-day window.

For this proof of concept, I calculated the percent difference from the daily average.

For a rigorous analysis, you will want to look at the standard deviation of sessions per day, and establish how many standard deviations the individual content piece’s performance is from the baseline. A session count that is three standard deviations from the average performance is more likely to be an anomaly than something that differs from the average for that day by over X%.

I used a pivot table to select every piece of content (with sessions in the past 90 days) that has at least one day of anomalies during that period:

In Google Sheets, pivot tables are not allowed to create more than 100 columns. Hence the limitation of 90 days for this analysis.
