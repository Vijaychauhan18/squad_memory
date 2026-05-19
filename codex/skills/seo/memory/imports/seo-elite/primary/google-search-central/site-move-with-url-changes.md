---
source: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
title: How to move a site
scraped: 2026-05-18
tags: google, official, site_migrations, redirects, sitemaps
topic: site_migrations
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: site migration planning, redirect validation, and post-move SEO checks
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# How to move a site

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
Page updated label: 2026-03-27 UTC

## Why This Matters
site migration planning, redirect validation, and post-move SEO checks

## Extracted Passages
- This document describes how to change the URLs of existing pages on your site while minimizing negative impact on your Google Search results. Examples of this kind of site move include:
- The details of site preparation vary for each site move, but typically you'll do one or more of the following:
- Set up a robots.txt for your new site and make sure the rules in the new site's robots.txt file correctly reflect the parts you want blocked from crawling.
- Note that some site owners block all crawling while in development. If you follow this strategy, make sure you prepare what the robots.txt file should look like once the site move starts. Likewise, if you use noindex rules during development, prepare a list of URLs from which you'll remove the noindex rules when you start the site move.
- Provide errors for deleted or merged content if you're not moving to the new site all your old content, make sure those URLs correctly return an HTTP 404 or 410 error response code on the new site.
- If you haven't already, verify both the old and new sites in Search Console. Be sure to verify all variants of both the old and new sites. For example, verify www.example.com and example.com , and include both the HTTPS and HTTP site variants if you use HTTPS URLs. Do this for both old and new sites.
- Make sure your Search Console verification will continue to work after the site move. If you're using a different method of verification, keep in mind that verification tokens may be different when the URL changes.
- If you're using the HTML file method to verify ownership of your site in Search Console, make sure you don't forget to include your current verification file in your new copy of the site.
- Likewise, if you verify ownership with an include file that references the meta tag or Google Analytics to verify ownership, ensure the new CMS copy includes these as well.
- Review any configured settings in Search Console that you may have made for the old site, and make sure the new site's settings are updated to reflect those changes as well. For example:
- Clean up your recently purchased domain ; you'll want to make sure it's clean of any outstanding issues from the previous owner. Check the following settings:
- Use web analytics to analyze usage on both the old and new sites. Web analytics software can help with this. Typically, web analytics configuration consists of a piece of JavaScript embedded in your pages. The details for tracking different sites varies depending on your analytics software and its logging, processing, or filtering settings. Check with your analytics software provider for help. Additionally, if you have been planning to make any configuration changes to your analytics software, now is a good time. If you use Google Analytics, consider creating a new profile for your new site if you want clean separation in your content reports.
- It's important to map your old site's URLs to the URLs for the new site. This section describes a number of general approaches you can take to correctly assess the URLs on your two sites and facilitate mapping. The exact details of how you generate this mapping will vary depending on your current website infrastructure and the details of the site move.
- In the simplest of site moves, you may not need to generate a list of your old URLs. For example, you could use a wildcard server-side redirect if you're changing your site's domain (for example, moving from example.com to example.net ).
- In more complex site moves, you will need to generate a list of old URLs and map them to their new destinations. How you get a listing of old URLs depends on your current website's configuration, but here are some handy tips:
- Once you have the listing of old URLs, decide where each one should redirect to. How you store this mapping depends on your servers and the site move. You might use a database, or configure some URL rewriting rules on your system for common redirect patterns.
- Once you have your URL mapping defined, you'll want to do three things to get the pages ready for receiving traffic.
- Once you have a mapping and your new site is ready, the next step is to plan your redirect strategy. We recommend server side permanent redirects from the old URLs to the new URLs as you indicated in your mapping. Check with your server administrator (or hosting company) about what kind of server side redirects you can technically do. It might be redirect rules in your .htaccess files if your server is using Apache HTTP server or redirect functions in your CMS.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

