---
source: https://www.oncrawl.com/data-driven-seo/fix-mistakes-parsing-log-files/
title: How to fix typical mistakes when parsing log files - Oncrawl
scraped: 2026-03-25
published_on: 2019-02-21
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

# How to fix typical mistakes when parsing log files - Oncrawl

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/data-driven-seo/fix-mistakes-parsing-log-files/
Published: 2019-02-21
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
In this article, we will detail some of the typical mistakes due to a standard configuration and often incomplete of your log files.

## Extracted Body
Log files are a wealth of information to help you improve your SEO strategy. In order to use them properly, you need to make sure that their data is accurate and complete. And this is not always as obvious as you might think!

In this article, I will detail some of the typical mistakes that occur when using a standard — and often incomplete — configuration for writing your logs.

Google has made many announcements about HTTPS in the past few years, and migration from HTTP to HTTPS has become a common task for many SEO experts. For this type of project, log files are an efficient tool to make sure that the migration goes smoothly.

First of all, I would advise that you set up a strong log files analysis, combined with an appropriate segmentation in an SEO crawler as Oncrawl. This will allow you to monitor the inclusion of your redirections and the progressive transfer of your site from one crawl budget to another.

In most cases, the original, standard log format does not allow you to differentiate between the HTTP and the HTTPS protocols. Why? Because of the lack of an element which can explicitly identify the targeted protocol.

Concretely speaking, this element could be the port (80 for HTTP, 443 for HTTPS), the scheme (HTTP or HTTPS) or even the SSL/TLS protocol (ex. TLSV1.2).

One significant impact of the inability to differentiate between HTTP and HTTPS is that you would see two different status codes for a single URL. An organic or a Googlebot visit on an HTTP page (http://www.site.com/a.html) that is properly redirected in 301 toward its HTTPS equivalent (https://www.site.com/a.html), would produce two entries for /a.html: the first one in 301 and the second one with the final status code.

Before an HTTPS migration, make sure that your log files contain all the required information to ensure you can monitor the elements you need.

In some cases, the port is already present in your logs. However, you can’t be sure that it is the right one.

For example, in the log formats options for Apache servers, the port can be declined in 3 ways — Canonical, Local or Remote — which can sometimes lead to different results.

In other cases, it is not impossible that the only available logs come from an internal layer of your infrastructure which has unsecured exchanges with the other layers. It would be preferable to check that the returned port matches the one used by visitors.

Using the same logic we did for the port, we can known the IP address written in your logs may be wrong — or at least different than the one expected.

According to the principle of layered infrastructure as previously seen, the returned IP address in your logs could be, for example, the one from your cache server which calls the pages/ressource instead of the one of the user who is making the request.

However, the IP address is sometimes the only element which allows you to differentiate between crawl by the “real” Googlebots and crawls by your competitors or other tools which browse your site by falsifying their User-Agent. It is relevant for your SEO strategy to ensure that you are working with the right information.

Some servers host several websites at the same time. In many configurations, every site/host/vhost handles its own log files.

These files are generally recognizable thanks to their name (which includes the vhost) or the name of the repertory in which they are stored.

However, it sometimes happens that the server configuration leads to logs from different sites being written in a shared file.

In that case, it is important, perhaps even mandatory, to add a field that makes it possible to identify the website concerned in every log line. Without this, it is impossible to assign the activity recorded in the logs to a specific website. An alternative would be, for example, to fill in the absolute URL as a Path (this is the field indicating the URL requested) as opposed to the relative URL that is usually found in this field.

This would also offer a good alternative to requiring a field for the port or any other field which makes it possible to identify the protocol.

Make sure that the timestamp of your server is correct and respects the local timezone.

In short: every log line includes the date and time, which makes it easy to identify the time of a given event.

But sometimes the time in the logs does not exactly match the actual time of the event.

This may seem like splitting hairs, but when you are trying to identify the precise time and cause of peak in number of errors, for example, it is better to be able to quickly and easily spot the lines involved.

Don’t forget to validate this configuration point with your hosting service.

Keep in mind that log files are rarely perfectly set up without some action on your part.

And remember: any modifications you make to the rules for writing your logs will not be retroactive. Therefore, the sooner you optimize their format, the sooner your log analysis will be an efficient and useful tool to pilot your SEO strategy.
