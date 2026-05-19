---
source: https://www.onely.com/blog/ultimate-guide-to-xml-sitemaps/
title: The Ultimate Guide to XML Sitemaps for SEO
scraped: 2026-03-23
published_on: 2021-11-29
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

# The Ultimate Guide to XML Sitemaps for SEO

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/ultimate-guide-to-xml-sitemaps/
Published: 2021-11-29
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Sitemaps can positively impact the crawling and indexing of your website. This guide will help you understand what sitemaps are and what to include in them.

## Extracted Body
A sitemap is not necessary for your site to function, but adding one can positively impact the crawling and indexing of your website by search engines.

On the other hand, a poorly optimized sitemap can negatively affect your crawl budget and put you at risk of search engines overlooking your valuable content.

This guide will help you understand what sitemaps are, what to include in them, and why you need one.

An XML sitemap is a text file that lists URLs on your website. It serves as a digital map for search engine bots and helps them find the valuable pages you want search engines to index.

Sitemaps have their own URLs, and they can be placed anywhere on your site’s server. However, they affect only descendants of the parent directory. So to affect all of the pages, you need to add the sitemap to your root directory:

The link to your sitemap should be included in your robots.txt file. To do it, use the following directive at the beginning or the end of your file:

You don’t necessarily have to put a sitemap in the robots.txt file, but it will help most bots find it, including search engines other than Google and Bing. For example, both Seznam and Yandex can read sitemap directives from robots.txt. source: Renata Gwizdak, Junior SEO at Onely

Having a sitemap comes with many benefits for your website. First and foremost, it helps search engines find content to index.

In the ideal world, well-designed site architecture should let users and search engines reach all your pages without a problem.

Unfortunately, a website structure can be complicated and doesn’t always make it easy for search engine bots to find all your pages.

A sitemap presents the URLs in a straightforward format bypassing the need for crawlers to follow links on your site, which makes it easier for search engines to discover all important pages on your site.

An XML sitemap can help any website, and every website should have one just to be safe. Still, it may be more beneficial for some than for others.

Not all of your pages should make it into your sitemap. If you put all of them in, you risk wasting your crawl budget on crawling low-quality pages. This can lead to high-quality pages on your site that remain unindexed because search engines didn’t have the resources to crawl them.

That’s why it’s so important to ensure you only include indexable pages with your most valuable content.

Additionally, here is a list of pages that should not end up in your sitemap:

Both <?xml> and <urlset> tags are basic XML components. They define the encoding standard and XML version.

Every <url> tag describes an individual URL. Inside, you can find the following tags:

<loc> tag stands for “ location, ” and it contains the URL of the page.

You need to remember to specify the site protocol (HTTP or HTTPS).

I will elaborate and cover the use of the hreflang tags below. And meanwhile, if you have an International SEO sitemap with hreflang tags and need expert assistance, explore our International SEO Services .

<lastmod> stands for “ last modified, ” and it includes information about the last modification.

For content sites, this tag helps Google establish that you are the original publisher – if someone scrapes your content and publishes it on their page, <lastmod> may help you remain the author of that content in Google’s eyes.

Note: You should only update this tag if you have made meaningful changes to a page. If you try to “trick” Google into thinking you update content regularly when you don’t, Google might potentially start ignoring this tag.

Make a judgment call whether the changes make a difference to a potential user. Ask yourself: would it make sense for someone to return to this page after the modifications were made? If all you did was change commas around, it’s probably not worth the risk.

<changefreq> tag stands for “ change frequency .” It informs search engines how often the page is likely to change.

Note: The <changefreq> tag is only a hint for search engines. Additionally, some of them, including Google, don’t take it into account at all.

The priority tag directly lets search engines know how vital a page is in relation to other URLs on your site. Assign priority on a scale between 0.0 and 1.0.

It’s worth noting that Google does not take this tag into account:

https://twitter.com/johnmu/status/1172491183593070594?lang=en

You can specify the language version of your pages with an hreflang tag.

To do so, you need to include the tag below each <url> tag to represent every language version of the page, including itself.

Here’s an example of a page that has English and German language versions.

Adding the hreflang tag to your sitemap can help search engines present the most appropriate language version to the users. However, the recommended practice is adding the tag to your HTML code and in your sitemap or only in the HTML code.

While putting hreflangs in sitemap works, it also makes them a pain to verify. First, many SEO tools are optimized for hreflang tags in HTML . Second, you can forget about any browser add-ons that will automatically check hreflangs for you while visiting the page. This only works with hreflangs in HTML. If you put the markup in the sitemap, all this convenience is lost. You will have to crawl your sitemaps every time you wish to see any change made to your hreflang tags. source: Artur Bowsza, SEO Specialist at Onely

If you want to learn more about hreflang tags or International SEO, check out our Ultimate Guide to International SEO.

You can add additional syntax to your sitemap to specify information about rich media content, including:

You can add your images to your existing sitemap or create a separate XML Image Sitemap.

An Image Sitemap helps create an organized index of images on your website, allowing search engine bots to crawl it more efficiently. It’s beneficial if:

You can add image metadata and specify additional information like an image caption, location, or license. You can find more about available image tags in Google’s documentation.

The images you include in an image sitemap don’t have to be on the same domain as your website. A CDN is fine if it is verified in Google Search Console.

Just like Image Sitemap, you can add your videos to your existing sitemap or create a separate XML Video Sitemap.

You can provide additional information for search engine bots about your videos to help the bots find and understand your video content better, especially if the content would be difficult to discover otherwise.

For example, you can add the duration of the video and specify if it’s family-friendly. You can find more about available video tags in Google’s documentation.

If you want to learn more about video indexing, check out our new article about Google’s Video indexing report and the consequences of its launch.

Google News Sitemap contains a list of articles published on your site and helps Google discover new articles faster.

You can list up to 1,000 URLs in the Google News Sitemap and update the articles in the sitemap as soon as they are published.

You can find the available news-specific tags in Google’s documentation.

Sitemaps can hold 50,000 URLs. Therefore, if you want to include more URLs, you should create more than one sitemap.
