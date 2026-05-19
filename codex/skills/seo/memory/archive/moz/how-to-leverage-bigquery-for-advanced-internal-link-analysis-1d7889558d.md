---
source: https://moz.com/blog/bigquery-advanced-link-analysis
title: How to Leverage BigQuery for Advanced Internal Link Analysis
scraped: 2026-03-23
published_on: 2024-05-08
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

# How to Leverage BigQuery for Advanced Internal Link Analysis

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/bigquery-advanced-link-analysis
Published: 2024-05-08
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Discover the potential of BigQuery for SEO. Dive deep into advanced internal link analysis and enhance your SEO strategies.

## Extracted Body
Like any SEO consultant, I thrive on data. Yet, when analyzing internal links for websites with seven million pages, even the most reliable tools like Excel and SEO software often fell short.

Thankfully, I discovered the capabilities of BigQuery, a part of the Google Cloud ecosystem that allows you to analyze large data sets by connecting them to Looker Studio for easy visualization. Together, they’ve significantly reduced analysis time and eased my stress.

In this blog, I'll show you how to import internal link data from an SEO tool like Moz Pro into BigQuery and visualize it in Looker Studio for easy insights.

Stripping away the technical jargon, BigQuery is a database in the cloud where you can store and analyze massive amounts of data. Picture a gigantic spreadsheet with significantly enhanced capabilities. BigQuery uses structured query language (SQL) for data analysis, structuring, and transformation. Though it initially appears complex (I love comparing it to a rocket cockpit), it becomes quite manageable even for first-time users with some training.

Meanwhile, Google Cloud is a cloud computing service provided by Google. Broadly, it offers possibilities like:

Cloud storage : Enables storing large files online, which can be imported into BigQuery.

Cloud function : Facilitates code execution. For example, using Python to extract data from an API such as keyword tools, Google Search Console, or Google Analytics.

Compute engine : Provides the capability to operate a virtual computer in the cloud, which is helpful for Screaming Frog .

Though I've only begun to explore the possibilities, Google Cloud offers a myriad of other functionalities.

2. Log in and click “Console” at the top right to access the hub.

3. If this is your first visit, select your country and agree to the Terms of Service.

4. To create a new project, click the selector at the top left marked (1). Then, click “New Project” at the top right of the dialog box marked (2).

5. Name your project. A simple name is convenient, especially when you manage multiple projects. For this guide, I'll use “internal-link-analysis.”

Initially, BigQuery appears empty, but soon, you'll establish a dataset and a table. Think of the dataset as a folder on your computer that organizes your data and the table as an Excel file within that folder.

An organized architecture might seem tedious for individual analysis. Still, it’s critical for scalability when integrating various data sources like Google Ads, Search Console, GA4, or SEO tools' APIs across numerous clients.

For novices to Google Cloud, there's an opportunity to leverage free credits. It’s a cheaper way to familiarize yourself with the platform without immediate financial commitment. I'll discuss pricing and key considerations later, but remember that BigQuery and Google Cloud have minimal costs.

First, you'll need a CSV containing all your internal links.

At the very least, your file should have a column for the source (origin of the internal link) and a column for the destination (where the link leads). However, if possible, include additional columns for the anchor, status code, and type of link (such as image, text, and hreflang) to enrich your analysis.

For example, I used data from my agency's website. While it’s a small site with 1,678 pages (including redirects and erroneous pages), it contains 338,656 links when accounting for CSS, JavaScript, sitemaps, and more. Although manageable in a raw Excel sheet, applying custom formulas and filters could become challenging.

Type: Identifies whether the link is from a sitemap, hreflang, canonical, simple hyperlink, image, CSS, etc.

Alt Text: If the link is an image, this column contains its alt attribute text.

Status: The status of the destination (e.g., canonicalized, non-indexable).

Link position: Indicates if the link is in the navigation, head, content, or elsewhere. Ensure the tool settings are accurate.

Link origin: Specifies whether the link is only present in the HTML or the rendered HTML post-JavaScript execution. This is helpful in troubleshooting JavaScript-rich websites.

With the file ready and a Google Cloud account set up, what's next?

1. If your file is under 100 MB, upload it directly via the BigQuery interface

Although the process is similar to the first option, I'll explore the second option (as my file exceeds 100 MB).

1. Return to the Cloud Hub and click “Cloud Storage” at the bottom left.

Note: You need a free trial for this step. Otherwise, you could split your 200 MB file into two and import it twice using the first option. However, this solution is time-consuming and isn’t efficient.

5. Leave the other options and public access settings as they are.

6. Once confirmed, upload your CSV file by clicking on "Upload File" and selecting your CSV.

1. Click on the Google Cloud logo on the top left, then navigate to BigQuery on the bottom left of the page.

4. Once you click on Cloud Storage, you should see it in (1). Choose CSV format (3). Then, click browse in the middle line, go to your bucket, and select your CSV (2).

5. Create the dataset by clicking on “Dataset” (1), then “Create Dataset”. Give the popup a name (2), and remember that “Dataset” is similar to a folder. Use underscore as a separator between two words. Select the same region as the cloud storage (3). Click “Create new dataset” (4).

6. Name the table (5) (it’s like the Excel file, and use “dash” as a separator between two words).

7. Click on auto detect (1), and BigQuery automatically detects the table format according to your CSV. For specific cases, you can fill in the info manually.

8. For advanced options (you have to scroll to the bottom of the window and click on the black arrow to see all the options), you can put “1” in “header rows to skip” (2) because you have 1 line that contains the column names in your CSV and you don’t want this line to be in your dataset.

9. In advanced options (accessible by scrolling down and clicking the black arrow), set "1" in "header rows to skip" (2) to exclude the column names row from your dataset. Opt for "Quoted newlines" (3) to maintain integrity for lines within quotes. Without altering other settings, click on "Create Table" (4).

Your table is now in BigQuery and ready to be linked to Looker Studio. Although it's a good starting point, you can enhance this table with SQL, which I'll explore next. To check the table, go to BigQuery and click table (1), which will open a new tab (2) for reviewing the table schema and previewing data.

To deepen your analysis, you’ll need to categorize your table. The goal is to view internal links by URLs and categories. Although I'm not an SQL expert, I can leverage ChatGPT to get the desired output.

In Looker Studio, you might use ‘ CASE WHEN Regex Match ’ in a custom field, which could slow down your dashboard for extensive datasets. Hence, my preference for SQL.

The objective is to categorize each URL (Destination & Source) based on primary categories. For example, my site's URL structure:

‘ https://universem.com/fr-be/on... ` follows a Domain > Language > Main-category > Sub-category format.

The challenge is to extract and sometimes merge elements (e.g., “agence” in French, “agency” in English, and “agentschap” in Dutch represent the same category). The English version, lacking the /en/ structure, adds a wrinkle to the process.

1. After explaining my requirements to ChatGPT, I used the generated basic code in a new tab in BigQuery.

2. Next, copy-paste the code into a newly created tab in BigQuery. To do this, initiate a new tab by clicking the blue "+" at the top (1).

3. Then, replace the designated table name (1) (format: project.dataset.table). A green arrow at the top right (2) indicates that the code is operational yet rudimentary, requiring refinements for advanced URL categorization.

4. The complete code extends the conditions for the two cases. For example, when the page URL contains /ons-agentschap/|/our-agency/|/notre-agence/ (where "|" means "or"), it is categorized as “Agency.” The same logic applies to other categories, except the home page, which is identified by exact URLs that match A, B, or C.
