---
source: https://www.hobo-web.co.uk/how-to-run-hobo-seo-dashboard/
title: How To Run Hobo SEO Dashboard (Multi-Site)
scraped: 2026-03-22
published_on: 2025-04-26
tags: live_feed, phase1_ingest, hobo, publication, quality, leak-systems, archive_backfill, historical_source
topic: quality_systems
intent: research, monitoring, source_selection, leak_systems
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Archive backfill - Hobo Web
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How To Run Hobo SEO Dashboard (Multi-Site)

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/how-to-run-hobo-seo-dashboard/
Published: 2025-04-26
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
How to run and operate the Hobo SEO Dashboard after it is set up. Despite how powerful it is, it really is quite straight forward.

## Extracted Body
Before features in the Hobo SEO Dashboard that interact with Google Search Console (such as automatically adding clients, fetching performance data, or checking property types) can function, you must enable the necessary APIS and link your Apps Script project to a Google Cloud Platform (GCP) project. Whilst the linked article provides full details, the basic steps involve:

Go to the Google Cloud Console and create a new project or select an existing one.

Within your GCP project, navigate to APIS & Services > Library and enable the Google Search Console API . Ensure the Google Drive API and Google Sheets API are also enabled (these are often enabled by default for Apps Script).

Go to APIS & Services > OAuth consent screen . Configure it (User Type, App Name, Support Email, Developer Contact). Add the necessary scopes required by the script (the script will usually prompt for these during authorisation, but common ones include webmasters.readonly , drive , spreadsheets , script.external_request , userinfo.email , script.scriptapp ).

In the Google Apps Script editor for your spreadsheet, go to Project Settings (the gear icon ⚙️). Scroll down to the Google Cloud Platform (GCP) Project section and enter the Project Number of the GCP project you configured. Click Set Project .

(Refer to the full guide on how to set up Google Search Console API for detailed instructions and screenshots.)

NOTE: The first time you run Hobo SEO Dashboard, you will be asked to authorise it. Hobo SEO Dashboard is designed to be PRIVATE .

A compilation of usage tips based on the Hobo SEO Dashboard menu structure and associated functions:

The Hobo SEO Dashboard is designed to run automatically and autonomously. You can turn it on, it will take about an hour to set itself up. Once activated, it will start to produce reports for every account in your Search Console. Note, it does not email until you specifically set it up to email.

When Report Scheduler is set to Activate Automated Reporting, all the functionality below runs automatically over the course of the day, all within your API limits.

It is designed to be very frugal, work on a Personal Gmail workspace and stay well within Google’s free API thresholds.

When you select this, it takes 30 minutes to initialise. When this option is selected, a series of scripts will run for 6 minutes to set the initialisation phase up and prepare your sheet for reporting.

NOTE: When Automatic Reporting is turned on, this function will periodically stop and start the reporter to perform its functions on any client report.

This completely stops the Hobo SEO Dashboard from performing any functions.

When Deactivate Automated Reporting is selected, the reporter disables any set triggers and is now completely dormant.

Note, you can turn this on and off at your leisure, but note that each time you do, it will cause an iteration of multiple scripts.

TIP : Turn off the automation every now and then and reinitialise the reporter so the system will optimise itself. Select Activate Automated Reporting to update to the latest version if another version is available. (Beta)

You can stop the reporter at any time. NOTE – When the reporter is stopped, and automatic reporting is set to ON, the reporter will initiate itself again to begin running reports. To turn off the autonomous agent, select tip 2 – Deactivate Automatic Reporting to completely stop the reporter. You can turn it on and off when you choose. It is designed to run continuously.

This runs automatically every hour or so. The optimal runtime for this is every hour. Use Select Client to browse your sites instead, for quick access.

CRITICAL NOTE : When Load Next Client is selected , it triggers a series of cleanup functions on your sheet and reinitializations that take ten minutes to complete on occasion. When loading and cleaning, the reporter will go into RESETTING mode, and no reports will run until this process is complete, and scheduling takes over again, if you have Activate Automated Reporting selected.

At any time, you can select a new client to load, and the report will reset itself. If left, the Dashboard will prepare a report for that client.

Selecting a new client takes you to the Domain Stats tab in the Hobo SEO Dashboard , where you can browse algorithmic impacts for a year. Historic Domain stats are in beta.

The reset functionality takes 5 minutes to completely reset, sometimes longer. This is to ensure the Dashboard is completely cleaned of previous report data. While the reset is underway, the report will pause its functionality and automatically restart when ready.

This will publish the contents of the currently loaded Dashboard report to a new Google Sheet (the Client Report). If a report has been previously generated, it will update that report.

To successfully publish a client report, the reporter must have processed Search Console and crawl reports (see Tip 5 and Tip 6 above). If you do not have Screaming Frog, it will skip this and prepare Search Console data.

In your Clients tab in Hobo SEO Dashboard , or your Clients Archiver tab , row 111, select YES to archive any site. If you delete a site from your tab, it will be pulled back into the sheet when the sheet automatically imports your list of Search Console sites. This is why Dashboard archives clients. Sites archived will move to the Clients Archiver tab to the other. Note: To delete a client, simply delete the column in the Clients tab.

In your Clients Archiver tab , row 111, select NO to unarchive any site. Sites unarchived will move from the Clients Archiver sheet to the Clients tab. Note: To delete a client, simply delete the column in the Clients tab.

This will sync your clients from Search Console. Note, this is done automatically by the system every 4 hours. Note that this is time-consuming and resource-intensive when selected manually.

If you have Screaming Frog data files in your Google Drive, this will create clients in your Hobo SEO Dashboard based on the websites you have crawled. Note, this is automatically done by the system, too.

For full documentation on bulk emailing functionality, see The Client Bulk Mailer System in the Hobo SEO Dashboard.

For more about Hobo SEO Dashboard, check out the Hobo SEO Dashboard Overview .

See also How to Set Up SEO Dashboard or set up Screaming Frog in Hobo SEO Dashboard .
