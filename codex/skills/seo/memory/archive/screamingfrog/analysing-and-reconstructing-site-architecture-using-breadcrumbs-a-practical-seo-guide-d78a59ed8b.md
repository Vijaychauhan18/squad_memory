---
source: https://www.screamingfrog.co.uk/blog/reconstructing-site-architecture-using-breadcrumbs/
title: Analysing and Reconstructing Site Architecture Using Breadcrumbs: A Practical SEO Guide
scraped: 2026-03-25
published_on: 2026-02-20
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

# Analysing and Reconstructing Site Architecture Using Breadcrumbs: A Practical SEO Guide

Source: Screaming Frog Blog
Homepage: https://www.screamingfrog.co.uk/blog/
Original URL: https://www.screamingfrog.co.uk/blog/reconstructing-site-architecture-using-breadcrumbs/
Published: 2026-02-20
Strength: technical SEO, crawling, site architecture, large-site workflows

## Summary
Analysing site architecture is one of the most important — and often most challenging — aspects of technical SEO, particularly for large websites. In many projects, SEO professionals rely on signals such as URL folder structures, crawl depth, or internal linking graphs to understand how a site is organised. However,...

## Extracted Body
Posted 20 February, 2026 by Arash Seyfi in Screaming Frog , SEO

Analysing site architecture is one of the most important — and often most challenging — aspects of technical SEO, particularly for large websites.

In many projects, SEO professionals rely on signals such as URL folder structures, crawl depth, or internal linking graphs to understand how a site is organised. However, these signals do not always reflect the actual logic behind content categorisation or the architectural decisions made at a business level.

As a result, it is common to see site architecture analyses that appear technically sound, yet provide limited value when it comes to improving user experience or making informed structural decisions.

In this article, we take a different approach by focusing on a data source that is typically rooted directly in a site’s information architecture and commercial logic: page breadcrumbs .

We begin by exploring the limitations of common site architecture analysis methods and explain why breadcrumbs often provide a more accurate representation of a site’s true structure. We then walk through a practical, step-by-step workflow showing how breadcrumb data can be extracted using the Screaming Frog SEO Spider, processed with Python, and ultimately used to reconstruct the site architecture as a clear, analysable, and visual tree model.

This article is a guest contribution from Arash Seyfi , Technical SEO Specialist at Jangal Publishing.

When we talk about site architecture, we are not simply referring to how pages link to one another. Site architecture reflects the underlying logic used to organise content across a website — defining how pages are grouped, how sections relate to each other, and how those relationships are presented to users and search engines.

More precisely, site architecture refers to the structural design of a website that determines how pages are organised, connected, and internally linked in a way that supports user experience, crawlability, and ultimately the site’s commercial objectives.

On smaller websites, understanding this structure is usually straightforward and can often be assessed by reviewing a limited number of page paths. However, on larger sites — particularly ecommerce websites with thousands of products, categories, and landing pages — site architecture quickly becomes more complex and multi-layered.

In these scenarios, accurately extracting and reconstructing the true site architecture becomes a significant challenge for SEO and digital marketing professionals. When this challenge is overlooked, decisions around content expansion, internal linking optimisation, or even full architecture redesigns risk being based on incomplete data or incorrect assumptions.

When analysing or attempting to reconstruct site architecture, there are several commonly used approaches, each offering a partial view of how a website is structured. Many of these methods can be implemented using crawl data and tools such as the Screaming Frog SEO Spider. However, an important limitation remains: none of these approaches, on their own, reliably reflect the logical structure intended by the business .

Directory Tree Visualisations are particularly useful because they provide a hierarchical, visual representation of the site’s URL structure. They allow you to quickly see the arrangement of directories and subdirectories, making it easier to spot structural patterns and potential issues. These visualisations can also highlight sections of the site that are heavily nested or potentially under-optimised. While they don’t fully reflect the business-defined parent-child relationships between pages, they are a powerful tool for understanding URL-level organisation and supporting technical SEO analysis.

While each of these methods can be useful, they tend to emphasise technical or implementation-level signals, rather than the formal and logical hierarchy defined by a site’s information architecture .

For example, URL structures may reflect historical or technical constraints rather than current category logic. Crawl visualisations are built around depth and shortest discovery paths, which can bias the resulting view towards incidental linking patterns. Similarly, internal linking graphs are effective at illustrating linking behaviour and accessibility, but they do not necessarily represent the official hierarchy of categories and sub-sections.

As a result, particularly on large websites — and especially on ecommerce platforms — relying solely on these conventional approaches can lead to an incomplete or even misleading understanding of the site’s true architecture.

For this reason, instead of focusing on URLs, crawl depth, or internal link graphs, this article turns to a data source that often provides a more direct reflection of business-defined structure: page breadcrumbs .

Breadcrumbs are one of the few website elements that are typically designed directly based on a site’s information architecture and business logic, rather than purely technical considerations or implementation constraints. As a result, they often provide a representation that aligns more closely with the structure intended by site owners , rather than the accidental hierarchy that might arise from URL patterns or link distribution.

Unlike URL structures or internal linking graphs, breadcrumbs usually display a clear hierarchical path that the site wants both users and search engines to understand. Each breadcrumb path explicitly shows:

From a site architecture analysis standpoint, breadcrumbs can be considered a type of official representation of site structure . This representation is both visible to users and typically designed to enhance navigation, user experience, and the overall understanding of the site’s hierarchy.

These characteristics make breadcrumb data a more reliable source for reconstructing the actual site architecture in many cases — particularly on large ecommerce websites — compared to methods that rely solely on technical signals.

When it comes to understanding a website’s structure, site architecture isn’t just about URLs or internal links. It represents how a business organises its content — how pages and categories are grouped, how they relate to each other, and how these relationships are presented to both users and search engines.

On many websites, especially large e-commerce platforms, the true hierarchical structure — the parent-child relationships between categories and pages — is not always visible in the URLs . However, it is often clearly reflected in page breadcrumbs, which are designed based on the site’s information architecture and business logic.

Screaming Frog SEO Spider’s Directory Tree Visualisations show a website based on URL paths and directory structures. While this approach is useful for analysing URL organisation and technical structure, it doesn’t necessarily represent the actual parent-child relationships that the business defines. Essentially, what you see is a hierarchy of URLs, not the logical grouping of content.

Our breadcrumb-based method takes a different approach. By extracting breadcrumb data from pages, we can reconstruct the website’s architecture as it is intended by the business. The resulting structure shows the real parent-child relationships between categories and pages, rather than just following URL patterns. This approach provides a clearer picture of the site’s content hierarchy and is especially valuable for competitor analysis, SEO audits, and digital marketing strategies. It allows you to see how a site is truly organised, from a business perspective.

Here’s a summary of the key differences between the two approaches:

Feature Screaming Frog Directory Tree Breadcrumb-Based Method Data Source URL paths and directory structure Page breadcrumbs (business logic & information architecture) Node Relationships Based on URL structure, not true parent-child hierarchy Actual parent-child relationships between categories and pages Focus Technical URL analysis and directory grouping Logical content hierarchy and site architecture Strength Quick overview of URL organisation Accurate representation of business-defined site structure, ideal for optimisation and analysis Limitation May not reflect real business logic or category hierarchy Requires consistent breadcrumbs across pages

By comparing these two approaches side by side, it becomes clear why a breadcrumb-based analysis often gives more actionable insights for improving navigation, understanding content depth, and making strategic SEO or structural decisions.

The core idea behind this approach is to convert page-level breadcrumb paths into a structured, analysable model of site architecture. Instead of relying on URLs, crawl depth, or internal linking patterns, this method focuses on the hierarchical paths that the site itself defines to represent content relationships to users.

By extracting breadcrumb data across all relevant pages and analysing these paths collectively, it becomes possible to reconstruct site architecture as a hierarchical tree that more closely reflects information architecture decisions and business-driven structure, rather than purely technical implementations.

In the following sections, we walk through this process step by step — from extracting breadcrumb data using the appropriate tooling, to preparing the dataset, and finally reconstructing and visualising site architecture. The goal is to present a practical and scalable workflow that can be applied to large websites with minimal manual intervention.

To extract breadcrumb data across an entire website, we need a tool that can crawl pages at scale and return the required information in a structured format. In this workflow, the selected tool must support full-site crawling while also allowing targeted extraction of specific HTML elements.

The Screaming Frog SEO Spider is particularly well suited to this task. In addition to its crawling capabilities, it provides flexible options for extracting custom data directly from page markup. Rather than relying on the tool’s standard reports, this approach focuses specifically on using Custom Extraction to collect breadcrumb information from all relevant pages.

To improve both efficiency and accuracy, the crawl is configured to avoid collecting unnecessary data. Instead of extracting every available signal, Screaming Frog is set up so that the primary focus remains on breadcrumb paths. For this reason, the tool is deliberately configured in two key areas — Spider and Custom Extraction — which are covered step by step in the following sections.

In this workflow, the primary objective is to extract breadcrumb data only. Other crawl data is not required. For this reason, the Spider settings are intentionally kept as minimal as possible to improve crawl speed and reduce unnecessary data collection.

By limiting the crawl to only what is needed, the process runs more efficiently and ensures that the tool remains focused on pages that are relevant for breadcrumb extraction.

To apply these settings, navigate to Configuration within the SEO Spider and review the Spider options according to the paths outlined below. In each section, only the essential settings are enabled, while all non-critical options are left disabled to avoid collecting extraneous data.

The core of this methodology lies in correctly configuring Custom Extraction to capture breadcrumb elements from site pages. This feature allows specific data to be extracted directly from page HTML — in this case, the breadcrumb paths that represent the site’s hierarchical structure.

To achieve this, the exact location of breadcrumb elements must be defined within the Screaming Frog SEO Spider. These selectors can be specified using CSS selectors, XPath , or in some cases regex , depending on how the breadcrumb markup is implemented. The extraction type should also be chosen to match the underlying HTML structure of the page.

A critical consideration at this stage is ensuring consistency across different page types. Because the goal is to extract breadcrumb data for all relevant pages using a single, fixed configuration, the breadcrumb structure must be consistent across page templates (such as category pages, product pages, and other key page types).

To validate this, the HTML structure of breadcrumbs should first be reviewed across multiple page types. Once consistency is confirmed, the appropriate CSS selector or XPath can be identified and entered into Screaming Frog via the following path:

Tip: Every website will be different. You can use Visual Custom Extraction to help formulate the syntax.

After applying these settings and before running a full site crawl, it is essential to perform a validation step. While this may appear straightforward, it plays a critical role in ensuring the accuracy of the final output. To validate the extraction, select a small number of URLs representing different page types across the site, run Custom Extraction on these pages only, and manually compare the extracted values against the breadcrumbs displayed on each page.

If the extracted output does not match the visible breadcrumb on even a single page type, the CSS selector or XPath should be adjusted. Only once breadcrumb data is being extracted accurately and consistently across all tested page types should the full site crawl be executed and the data prepared for subsequent analysis.

Once the site crawl has completed, the Screaming Frog SEO Spider provides all extracted breadcrumb data within the Custom Extraction section. However, in its raw form, this data is not yet suitable for analysing or reconstructing site architecture and requires additional preparation.

At this stage, the objective is to transform the raw output into a clean, structured dataset that can be used directly as input for the Python script. This process includes exporting the data in the appropriate format, removing unnecessary columns, and standardising breadcrumb information. These steps ensure the dataset is ready for analysis and visualisation without the need for further manual adjustments.

After the crawl process has completed, the extracted breadcrumb data becomes available within the Custom Extraction section of Screaming Frog. At this point, the data needs to be exported so it can be processed and analysed in subsequent steps.

For this workflow, the data is exported as an Excel file from the Custom Extraction report. In addition to columns such as Address, Status Code, and Status, the file also includes columns representing breadcrumb paths. These columns typically appear as LVL 1, LVL 2, and subsequent levels, with each column corresponding to a specific level within the breadcrumb hierarchy.
