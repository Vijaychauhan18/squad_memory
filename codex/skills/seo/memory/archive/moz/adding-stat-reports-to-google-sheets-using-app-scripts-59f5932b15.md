---
source: https://moz.com/blog/add-stat-reports-to-google-sheets
title: Adding STAT Reports to Google Sheets Using App Scripts
scraped: 2026-03-23
published_on: 2022-01-12
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

# Adding STAT Reports to Google Sheets Using App Scripts

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/add-stat-reports-to-google-sheets
Published: 2022-01-12
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
The team at MacMillan Search has generated a lot of value by combining automated STAT reports with Google Sheets through the script they share in this post. From adding ranking details to other tool’s outputs to giving the content teams up-to-date “People Also Ask” reports, the end result has…

## Extracted Body
The team at MacMillan Search has generated a lot of value by combining automated STAT reports with Google Sheets. From adding ranking details to other tool’s outputs, to giving the content teams up-to-date “People Also Ask” reports, the end result has proven to be a great time-saver in our week-to-week SEO workflows by reducing manual work and providing standard outputs that easily integrate with any spreadsheet.

STAT’s wealth of keyword rankings details is very useful for enterprise SEOs to understand both the macro and micro details of their rankings. Google Sheets is one of the most common cloud-based spreadsheets platforms, and is easy to share between teams and organizations. That’s why SEOs use both of these tools regularly when analyzing keyword data.

Despite this, documentation on how to integrate STAT into Google Sheets is limited. To address this gap, we created our own script!

Not everyone likes CSVs: We leverage the STAT reports to provide clients with direction. Having to download a CSV and open it every week isn’t for everyone. With this script, you can set a weekly ticket with a link to the spreadsheet, and review the output regularly .

It saved us time: SEO is a marathon, not a sprint. When we identify an opportunity, there is ongoing work that will have us reviewing reports regularly. The weekly ticket approach to review a spreadsheet shaves some time off of each task, and over the course of the engagement, this saved time adds up.

Cleaner output : Using Vlookups, Uniques, etc., you can create a summary page of this information, highlighting what clients and/or readers care about. You can also integrate this information with other data sources.

Create automation without using an API : Automation, when done correctly, saves time. Using this script with triggers opens the door to automation.

The STAT knowledge base has a great resource on reports . The only thing we would get specific on is the naming of the report and the recipient email.

What you name your report is not as important as keeping it clear and concise. This makes scaling to other projects with similar reports cleaner and easier. You will also use this report name as one of the variables in the scripts.

We also suggest placing the company or project name at the end of the report name in parentheses (e.g. “(MacMillan Search)”). This makes it easier to find the report in your email.

It’s important to use a Gmail-enabled email for the account where you’ll be building the sheet. This way, Google has an easier time getting the app script to extract the CSV from the email.

For our clients, weekly data is the most useful — enough detail to spot trends, but not so much that it becomes just noise to be ignored. For reports with limited fluctuations (e.g. People Also Ask), monthly might be satisfactory.

Select “Run this report immediately” to confirm that your report works, right after creating the script. This way, you’re ready to set your triggers and let the data flow.

The rest of the settings are specific to what details you want from your report.

Create a new sheet in Google Drive under the account associated with your report’s recipient email. Then you’re ready to add the script:

3. A few things will need to be edited to work with your data:

var COMPANY_NAME updated to the company or project name you used while creating the STAT Report

var REPORT_NAME updated to the name of your report minus the company name and parentheses

var SHEET_NAME updated to the name of the sheet (the tab on the bottom) in the spreadsheet

4. Confirm the Script works by saving it, refreshing the sheet, and when the menu “Manual Update” loads, select “Import Keywords”.

5. The first time you run this you will get an “Authorization Required” pop-up:

Select “Continue”, follow the steps, and select “Import Keywords” under the menu again.

Your spreadsheet should now be populated with all of the details from your CSV.

Setting this sheet up to automatically update as the report comes out is very easy using Apps Script “Triggers”. To set up the triggers:

6. Select type of time-based trigger “Week Timer” for weekly reports, “Month Timer” for monthly reports, etc.

7. In our time zone, our reports usually come out late Sunday, so we pick early Monday morning:

The result is a spreadsheet that regularly updates, populated by an emailed STAT report.

We’ve found many uses for this script — anywhere we reference rank. And, since a project might take time to get implemented, we can provide current ranking information without leveraging the API.

We’re curious to learn how you leverage it as well. If you find the script useful, reach out to us on LinkedIn and let us know what you’re using it for.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

Michael is an expert in SEO strategy, specializing in strategy implementation for B2B software and service companies. 13 years of experience in SEO and 22 in digital marketing have seen Mike in both agency leadership and in-house marketing roles, ultimately leading him to work with some of the largest SaaS companies as Principal Consultant of MacMillan Search.

Turn any keyword into a winning content plan in seconds. Try Moz’s new AI Content Brief, where real SEO data meets creative inspiration.

Why did Google remove the long-standing &num= parameter, and what happens now? We explain the industry-wide impact on SERP scraping costs and detail the specific changes taking effect in Moz Pro.
