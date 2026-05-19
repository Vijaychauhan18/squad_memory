---
source: https://www.onely.com/blog/ultimate-guide-to-noindex-tag-for-seo/
title: Noindex Tag: Ultimate Guide & Actionable Tips
scraped: 2026-03-23
published_on: 2022-02-14
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Noindex Tag: Ultimate Guide & Actionable Tips

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/ultimate-guide-to-noindex-tag-for-seo/
Published: 2022-02-14
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Indexing your low-quality content may be harmful to the entire website's visibility. Luckily, it's easy to prevent with the noindex tag!

## Extracted Body
Summary in a nutshell What is Noindex Tag? The HTML “noindex” tag is an SEO directive used to prevent search engine bots from indexing certain web pages, ensuring that only beneficial content is visible in search results.

You may think that all pages on your website should be indexed, but that’s not the case. In fact, preventing certain pages from appearing in search results is integral to your indexing strategy.

You can apply the “noindex” directive by: 1. Inserting the meta tag “<meta name=’robots’ content=’noindex’>” in the page’s HTML <head> section. 2. Adding the “X-Robots-Tag: noindex” directive in the HTTP response headers for broader applications. How to check if the page uses Noindex Tag?

Check for a HTML “noindex” tag by viewing the page’s source code and looking for the “noindex” meta tag in the <head> section or by using SEO analysis tools (Ryte, Screaming Frog) or browser extensions (like aHrefs) that detect such directives.

Use “noindex” carefully to avoid hiding important pages. If “noindexed” pages appear in search results, prompt a search engine to recrawl using tools like Google’s URL Inspection. Also, distinguish “noindex” from similar tags like “nofollow” for precise SEO control.

The noindex tag is an HTML tag used to control the way bots treat a given page or file on your site and stop them from indexing that page or file.

You can tell search engines not to index a page by adding a noindex directive in a robots meta tag – simply add the following code to the <head> section of the HTML:

Alternatively, the noindex tag can be added as an x-robots-tag in an HTTP header :

When a search engine bot like Googlebot crawls a page with the noindex tag, it won’t index it. If the page was previously indexed and the tag was added later, Google will drop it from search results, even if other sites link to it.

Generally, search engine crawlers are not required to follow meta directives as they serve as suggestions rather than rules they must respect. Some search engine crawlers may interpret the robots meta values differently.

However, most search engine crawlers – like Googlebot – obey the noindex directive.

There are other meta robots directives that Google supports – the most popular ones include nofollow and follow. However, the follow tag is the default setting if no robots meta tags are added, so Google considers it unnecessary .

The nofollow tag prevents search engines from crawling the links on a page. As a result, ranking signals of that page will not be passed to the pages it links to.

It’s possible to use the noindex directive on its own, but it can also be combined with other directives. For instance, you can add both a noindex and nofollow tag if you don’t want search engine bots to index a page and follow the links on it.

If you have implemented a noindex tag, but your page is still appearing in search results, it’s likely that Google simply hasn’t crawled the page since the tag was added. To request Google to recrawl a page, you can use the URL Inspection tool.

You should use the noindex tag to prevent pages from being indexed by Google.

Making less important pages non-indexable is crucial because Google doesn’t have sufficient resources to crawl and index every page it finds on the web. At the same time, you need to identify your valuable pages that should be indexed and prioritize their optimization.

Let’s see what types of pages you should implement the noindex tag on to make them non-indexable.

Google Search Console notified you about indexing problems due to duplicate content? Read our guides and fix:

Making pages non-indexable should be done as part of a well-established indexing strategy.

Generally, never place noindex on pages that you expect to generate significant organic traffic.

Is your page “ Excluded by noindex tag ” in Google Search Console?

Read our article on how to fix this issue to unlock your indexing potential.

The noindex tag can be placed in a site’s HTML code or HTTP response headers.

Some CMS plugins like Yoast let you automatically noindex the pages you publish.

Let’s go through the two primary implementation methods step by step and analyze their pros and cons.

The noindex tag can be implemented as a robots meta tag in the <head> of a page’s HTML.

Robots meta tags are codes used to control a website’s crawling and indexing. Users cannot see them, but bots find them while crawling a page.

Inside a meta tag, there are pairs of attributes and values:

Both attributes require different values based on what you want the bots to do. Also, both name and content attributes are non-case sensitive.

The name attribute will typically take the value of “robots,” indicating that a directive targets all bots.

It’s also possible to use a specific bot’s name instead, such as “googlebot,” though you will encounter this much less often. If you want to address different bots, you will need to create separate meta tags for each of them.

Keep in mind that search engines have different crawlers for different purposes – check out Google’s list of crawlers.

Meanwhile, the content attribute contains the directive for the bots to follow. In our case, it is “noindex.” You can put more than one value there and separate the attributes by commas.

The HTML method is easier to implement and modify than the HTTP header method. It also does not require you to have access to your server.

However, implementing the noindex tag in your HTML can be time-consuming – you will need to add it manually to every page you want to noindex.

Another solution is to specify the noindex directive in an x-robots-tag.

This is an element of an HTTP header response. HTTP headers are used for communication between a server and a client (a browser or search engine bot).

You can configure it on your HTTP web server. The code will look slightly different depending on what server you’re using – like Apache, Nginx, or others.

Here is an example of what an HTTP response with an x-robots-tag can look like:

If you have an Apache-based server and want to noindex all the files that end with “.pdf,” you should add the directive to the .htaccess file .

If you have an Nginx-based server , implement the directive in the .conf file :

One significant advantage of using noindex in HTTP headers is you can use it on web documents that are not HTML pages , such as PDF files, videos, or images. Moreover, this method lets you target a particular part of the page.

Additionally, x-robots-tag supports the use of regular expressions ( RegEx ). In other words, you can target the pages that should be noindexed by specifying what they have in common. For example, you can target pages with URLs that contain specific parameters or symbols.

On the other hand, you need access to your server to implement an x-robots tag.

Adding the tag also requires technical skills and is more complicated than adding the robots meta tags to a website’s HTML.

If you want to check whether noindex or other robots meta directives are implemented, you can do it based on how they were added to a page.

So, if the noindex tag was added to a page’s HTML, you can check its source code, while for HTTP headers, you can use the Inspect option in Chrome . These tools will show you which directives were recognized on a given page.
