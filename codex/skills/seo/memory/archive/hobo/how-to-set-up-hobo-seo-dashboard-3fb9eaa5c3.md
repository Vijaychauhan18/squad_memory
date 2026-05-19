---
source: https://www.hobo-web.co.uk/how-to-set-up-hobo-seo-dashboard/
title: How to set up Hobo SEO Dashboard
scraped: 2026-03-22
published_on: 2024-09-28
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

# How to set up Hobo SEO Dashboard

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/how-to-set-up-hobo-seo-dashboard/
Published: 2024-09-28
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
Hobo SEO Dashboard is a Google Sheets tool that helps marketers, SEOs, and website developers perform an SEO audit report on any website. SEO Dashboard will autonomously run regular reports on every client in your Search Console according to the schedule you set. When set up, you can rely on it to automatically publish and ... Read more

## Extracted Body
Hobo SEO Dashboard is a Google Sheets tool that helps marketers, SEOs, and website developers perform an SEO audit report on any website.

SEO Dashboard will autonomously run regular reports on every client in your Search Console according to the schedule you set.

When set up, you can rely on it to automatically publish and then manage updating SEO audit reports for every client in your Search Console account.

Hobo SEO Dashboard uses 4 Google APIs to run in Google Sheets (for setup):

When you go through the setup procedure, make sure all APIs are set up (all are listed in the video above, although adding Google Drive API and Google Docs API is missing from the video).

Follow the rest of this guide to get Hobo SEO Dashboard started.

Hobo SEO Dashboard is designed to work within Google’s free API limits, even on a personal Gmail account. It was developed on a free account and still is. It takes moments to set up.

Set up your Google APIs first, after copying the Master Sheet which was shared with you.

It only takes a few minutes for you to set up Hobo SEO Dashboard in Google Sheets and you can start navigating your Search Console clients.

IMPORTANT NOTE – AT STEP 5 – Once you have your API setup ready, we HIGHLY suggest the first function you run from the top menu in Hobo SEO Dashboard is Hobo Admin – Report Scheduler Activate Automated Reporting.

The Hobo SEO Dashboard is a unique and powerful tool designed for SEO professionals, agencies, and multi-site managers.

Operating entirely within your Google Sheets environment and driven by Google Apps Script, it automates vast portions of technical SEO auditing and reporting.

It primarily integrates data from Google Search Console (GSC) and analyses Screaming Frog crawl exports (via its Hobo SF component) to deliver insights.

Unlike subscription-based SaaS platforms, the Hobo SEO Dashboard functions within your personal Google ecosystem (Sheets, Drive, Apps Script).

This approach prioritises data privacy, offers potential long-term cost savings via a lifetime license, and provides significant efficiency through automation.

This guide covers the essential steps for both the initial system setup (connecting to Google Cloud) and the critical configuration of individual websites within the ‘Clients’ tab.

This part focuses on connecting the Hobo SEO Dashboard sheet to the necessary Google services.

And that’s it, connected to Google. For a complete walkthrough of the Google API set up, see How to Set Up Google Search Console API – A walkthrough .

The next step you should do (or the first) is Hobo Admin” – “Set Admin” and add your Pagespeed API and your details. A form will pop up in your Dashboard sidebar when selected for you to fill out. This will populate the Clients tab with system-wide settings.

Also, the Hobo SEO Dashboard is now set up to run basic reporting by default. It takes 30 minutes for the system to initialise. Check back once it has had time to set up. Within an hour or two, it should be producing its first reports.

Once the initial setup is done, the ‘Clients’ tab within the Hobo SEO Dashboard Google Sheet becomes your primary control centre.

Each website you manage (pulled from GSC) is represented as a “client” in its own column. The dashboard automatically cycles through these columns to perform checks and generate reports.

While the dashboard aims for maximum automation with sensible defaults, this tab allows for fine-grained control over each site’s configuration.

While the tab contains many rows, they generally fall into these categories:

Setting up the Hobo SEO Dashboard involves a one-time connection to Google Cloud Platform APIS.

Following that, the ‘Clients’ tab serves as the dynamic control centre where you manage each website’s specific settings.

By understanding the interplay between automated data synchronisation (from GSC) and your ability to manually override or provide specific inputs (like API keys, test URLS, email addresses, and audit toggles), you can fully leverage the dashboard’s power for efficient, customised, and automated SEO reporting. Remember to primarily focus on setting the Canonical Domain (Row 2) correctly and then adjusting other user-input fields and toggles as needed for each client.

The information presented herein is derived solely from the provided technical documentation snippets for the Hobo SEO Dashboard.

Before using Hobo SEO Dashboard features that depend on data from Google Search Console (GSC), a series of configuration steps within the Google Cloud Platform (GCP) are mandatory.

This setup process is fundamental as it grants the dashboard the necessary permissions to securely access GSC data via Google’s Application Programming Interfaces (APIS). Failure to complete these prerequisites will prevent the GSC-related functionalities of the dashboard from operating correctly.

The required steps involve several distinct action s within the Google Cloud environment:

Executing these steps necessitates a degree of technical familiarity with the Google Cloud Platform.

The process involves navigating GCP interfaces, understanding API management concepts, and configuring authorisation settings.

This suggests that the tool is potentially aimed at users who possess this technical capability or have access to this comprehensive guidance.

The architecture, relying on the user’s own GCP project, also implies that user data (fetched from GSC, processed, and potentially stored in Drive/Sheets) remains within the user’s Google account boundary, offering a level of data control and ownership.

Once the Google Cloud Platform prerequisites are successfully addressed, attention can turn to the initial configuration within the Hobo SEO Dashboard itself.

This involves personalising the dashboard with administrative details and populating it with the website properties (clients) to be monitored.

To ensure reports and the dashboard interface reflect the correct branding and contact information, the administrator’s name and the company’s details should be set.

A key setup step is importing the list of websites managed through Google Search Console into the Hobo SEO Dashboard.

This leverages the existing verified property list within the user’s GSC account, streamlining the process significantly, particularly for users managing numerous sites, such as digital marketing agencies or multi-site businesses. This avoids the laborious and error-prone task of manually entering each website URL.

The combination of automated client synchronisation and a manual import trigger offers operational flexibility. The automatic updates handle routine synchronisation, while the manual option allows for immediate updates, for instance, after adding new sites to GSC. However, users should consider the potential performance impact and time required for manual imports, weighing the need for immediate synchronisation against the efficiency of the automated background process.

The Hobo SEO Dashboard incorporates an automated reporting function designed to generate SEO reports on a predefined schedule.

This section outlines the procedures for enabling and disabling this automation using the specific menu options provided. Controlling the automation schedule is distinct from manually triggering or stopping individual report runs (covered in Section 4).

To enable the system to automatically generate reports according to its schedule, the activation command must be used.

To stop the scheduled, automatic execution of the SEO reporter, the deactivation command should be employed.

The clear separation of “Activate” and “Deactivate” commands within the Report Scheduler menu provides unambiguous control over the automation’s core scheduling mechanism.

Beyond the scheduled automation, the Hobo SEO Dashboard provides options for direct manual control over the reporting process. This allows for initiating report generation on demand or interrupting a current ly running process. These manual controls are located under a different menu structure (Hobo Controls) compared to the automation schedule settings (Hobo Admin – Report Scheduler), logically separating immediate actions from administrative schedule management.

If a report needs to be generated immediately, outside of the defined schedule (if one is active), this can be triggered manually. This is useful for obtaining up-to-date reports after significant changes, for testing configurations, or for ad-hoc analysis.
