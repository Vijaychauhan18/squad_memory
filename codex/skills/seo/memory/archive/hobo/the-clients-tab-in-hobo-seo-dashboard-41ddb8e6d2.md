---
source: https://www.hobo-web.co.uk/hobo-seo-dashboard-clients-tab/
title: The Clients Tab in Hobo SEO Dashboard
scraped: 2026-03-22
published_on: 2025-04-30
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

# The Clients Tab in Hobo SEO Dashboard

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/hobo-seo-dashboard-clients-tab/
Published: 2025-04-30
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
The 'Clients' tab in Hobo SEO Dashboard functions as the central control panel for tailoring the dashboard's powerful features to each specific SEO project.

## Extracted Body
Disclosure : Hobo Web uses generative AI when specifically writing about our own experiences, ideas, stories, concepts, tools, tool documentation or research. Our tool of choice is in this process is Google Gemini Pro 2.5 Deep Research. This assistance helps ensure our customers have clarity on everything we are involved with and what we stand for. It also ensures that when customers use Google Search to ask a question about Hobo Web software, the answer is always available to them, and it is as accurate and up-to-date as possible. All content was verified as correct. Edited and checked by Shaun Anderson, creator of the Hobo SEO Dashboard and founder of Hobo Web. See our AI policy .

The Clients tab in Hobo SEO Dashboard is your client control centre.

Each website from Search Console is a “client”, and each client’s details are stored in one column in your Clients tab. The Dashboard will automatically cycle through each column (each client) in your sheet to produce individual reports for them in Google Sheets.

Despite its incredible complexity, Hobo SEO Dashboard is entirely controlled by a Google Sheet, remember. It can be configured in any way you need, before and after report generation.

While we recommend beginners use the Set Admin menu to add new clients to the client tab, you can do so manually, too.

At any time, you can go in and tweak the settings in the Client Tab and modify the details in the column for that particular client. You can add things like email addresses and keywords to track.

The Clients tab in Hobo SEO Dashboard will not change in future iterations. The software is built on top of it. So feel free to add details. Simply delete columns (clients) you don’t want from the sheet, although do note the Client Archive function ( Row 111 ).

We recommend you use it and populate it with all relevant details for any client you wish to (optionally) email published reports to.

NOTE: When you sync your clients, most of this stuff on this page is done automatically, apart from adding sensitive client info, naturally. The system uses the Clients tab as the central data source, but the Clients tab is 100% editable by you.

TIP : If you have problems loading any specific client in Hobo SEO Dashboard, go to Row 42 for that client in your Clients tab and select “ Override “. The next time that particular client loads (you can also move the client to column C on your Clients tab to ensure the Dashboard will run a report for this client next in the queue. Column C in your Clients tab is the next client to be loaded – the next in the queue. When a client report is published, the Override status is removed automatically.

This report provides an in-depth analysis of the configuration settings found within the ‘Clients’ tab of the Hobo SEO Dashboard. The Hobo SEO Dashboard is an automated SEO reporting and auditing system operating within the Google Sheets environment, designed primarily for SEO professionals, agencies, and multi-site managers.

Its core functions involve integrating data from Google Search Console (GSC) – known as Hobo SC – and technical site crawls (facilitated by Screaming Frog data analysis, known as Hobo SF) to generate comprehensive SEO reports.

This analysis details the purpose and function of each specified setting, elucidating how they collectively enable site configuration, data integration, audit customisation, report generation, client communication, and system automation.

The focus is on understanding how these parameters control the dashboard’s operations for individual client projects.

The entire aim of Hobo SEO Dashboard is autonomy and automation. All default settings are preset to allow you to instantly initialise your Dashboard, IE, they run automatically, when you initialise from the main menu.

See Tip 1: Turn ON Automated Reporting in Hobo SEO Dashboard .

This group of settings establishes the fundamental identity and technical parameters of the client website being analysed.

Correct configuration here is crucial for accurate data retrieval and analysis – note that by DEFAULT, Hobo SEO Dashboard is set at the optimal configuration. These will auto-configure when you select Hobo Admin > Report Scheduler > Activate Automated Reporting .

Specifies the definitive, preferred version of the client’s domain, including the protocol (https) and any subdomain (www). This is essential for ensuring consistency in reporting and for checks related to canonicalisation issues during site audits. Importantly, ensure the slash – “/” – is included at the end.

USED BY SYSTEM. EDIT ROW 2. Defines the first common variant of the domain that should permanently redirect (301) to the Canonical Domain. This is typically the non-www version if the canonical includes www, or vice versa, using the same protocol.

USED BY SYSTEM. EDIT ROW 2. Defines a second common variant, usually the HTTP version of the canonical domain (with www if applicable), which should also redirect to the primary Canonical Domain. Tracking these ensures proper domain consolidation for SEO.

USED BY SYSTEM. EDIT ROW 2. Defines a third common variant, typically the http, non-www version, which should redirect to the Canonical Domain. Ensuring all major variants redirect correctly prevents duplicate content issues and consolidates link equity.

USED BY SYSTEM. EDIT ROW 2. Specifies the root domain name without protocol or subdomains. This is used for filtering data, internal linking analysis, or potentially connecting with domain-level GSC properties.

USER INPUT – ADD A SAMPLE URL – Designates the URL pattern or specific URL of the website’s internal search results page. This can be used to identify and potentially exclude search result pages from certain analyses or indexing checks, as they often provide limited SEO value. N/A indicates it’s not defined or applicable for this client.

USED BY SYSTEM. EDIT ROW 2. Provides a specific URL on the client’s site that is known to return a 404 (Not Found) status code. This allows the system to periodically test and confirm that the server correctly handles requests for non-existent pages, which is important for user experience and crawl efficiency.

USER INPUT – ADD A SAMPLE URL – Similar to the 404 test URL, this field is for a URL known to return a 410 (Gone) status code, indicating a resource has been permanently removed. Testing this confirms the correct server configuration for intentionally removed content. N/A signifies that no specific 410 test URL is set.

USER INPUT – ADD A SAMPLE URL – Specifies the direct URL to the client’s primary XML sitemap file. This allows the dashboard to potentially fetch the sitemap for analysis, compare it against crawled pages, or check its validity. N/A indicates it’s not provided, or perhaps auto-discovery is used.

USED BY SYSTEM. EDIT ROW 2. Provides the direct URL to the client’s robots.txt file. This file instructs search engine crawlers which parts of the site should not be crawled or indexed. The dashboard uses this URL to fetch and analyse the file for potential issues or misconfigurations.

USER INPUT – ADD A SAMPLE URL – Allows for the specification of a secondary XML sitemap URL. This might be used for sites with multiple sitemaps (e.g., for images, videos, or different site sections). N/A indicates no secondary sitemap is specified.

These initial settings form the bedrock of the dashboard’s understanding of the target website.

Correctly defining the canonical domain and its variants ensures that data analysis focuses on the intended entity, while specifying critical files like robots.txt (Row 11) and sitemaps (Row 10, Row 13) enables direct checks of fundamental SEO configurations.

The inclusion of test URLS for 404/410 errors (Row 8, Row 9) facilitates automated verification of server response codes, a basic but crucial aspect of technical health.

Note that ALL checks in the Clients tab for the reporter to function are automatically handled by the system via regular scheduled imports and synchronisations of your Google Search Console account and Google Drive.

This section details the settings required to connect the Hobo SEO Dashboard to external data sources via APIs, primarily Google services. These integrations are fundamental for populating reports with performance data.

Connecting to external APIS, particularly Google Search Console (Row 12, Row 47, Row 87) and PageSpeed Insights (Row 18), is central to the dashboard’s functionality.

These integrations automate the collection of critical performance data, saving significant manual effort and enabling features like performance trend analysis and algorithm impact assessment.

The configuration details, such as the specific GSC property type (Row 87), ensure data accuracy relative to the client’s setup.

The potential for Google Analytics integration (Row 49) further suggests a design aimed at consolidating key website performance data streams.

These settings control the depth, frequency, and specific elements of the automated technical SEO audits performed by the dashboard, leveraging data primarily from sampling tests carried out directly in the Domain Stats tab of Hobo SEO Dashboard and full or partial site crawls (via Hobo SF integration).

This extensive suite of technical checks (Row 57 – Row 84) demonstrates the dashboard’s focus on in-depth site auditing.

By leveraging crawl data, users can automate the detection of a wide array of common and complex SEO issues, from basic broken links and missing tags to more nuanced problems like redirect chains (Row 79), mixed content (Row 68), and non-indexable canonicals (Row 70).

The ability to toggle these checks individually allows users to tailor the audit scope, while scheduling settings (Row 40) automate the ongoing monitoring process.

The limits on row processing (Row 37, Row 39) reflect the practical constraints of operating within the Google Sheets environment.

These settings manage the output and delivery of the generated SEO reports to clients or stakeholders, including report access, templating, and automated email communication.

These settings highlight the dashboard’s role in streamlining agency workflows beyond just data analysis.

The system facilitates consistent report generation using templates (Row 46) and automates client communication through scheduled emails (Row 112, Row 114, Row 258, Row 259).

The customisation options for email content (Row 52, Row 303-Row 307), including branding elements like logos (Row 301) and footers (Row 302), as well as promotional messages (Row 304), allow agencies to maintain a professional and personalised communication style while benefiting from automation.

The emphasis on data privacy within the email disclaimer (Row 302) reinforces a core aspect of the Hobo tool suite’s value proposition.
