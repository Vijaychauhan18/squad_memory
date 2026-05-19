---
source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
title: Build and submit a sitemap
scraped: 2026-05-18
tags: google, official, sitemaps, discovery, canonical_urls
topic: sitemaps
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: sitemap strategy, discovery, and canonical URL signaling
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Build and submit a sitemap

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
Page updated label: 2025-12-10 UTC

## Why This Matters
sitemap strategy, discovery, and canonical URL signaling

## Extracted Passages
- This page describes how to build a sitemap and make it available to Google. If you're new to sitemaps, read our introduction first .
- Google supports the sitemap formats defined by the sitemaps protocol . Each format has its own benefits and shortcomings; choose the one that is the most appropriate for your site and setup (Google doesn't have a preference). The following table compares the different sitemap formats:
- XML sitemaps are the most versatile of the sitemaps formats. It's extensible and can be used to supply additional data about images , video , and news content, as well as the localized versions of your pages.
- RSS, mRSS, and Atom 1.0 sitemaps are similar in structure to XML sitemaps, however they are often the easiest to provide because CMSes automatically create them.
- The best practices for sitemaps are defined by the sitemaps protocol . The most overlooked best practices are related to the size limits, sitemap location, and the URLs included in the sitemaps.
- Sitemap size limits: All formats limit a single sitemap to 50MB (uncompressed) or 50,000 URLs. If you have a larger file or more URLs, you must break your sitemap into multiple sitemaps. You can optionally create a sitemap index file and submit that single index file to Google. You can submit multiple sitemaps and sitemap index files to Google. This may be useful if you want to track the search performance of each individual sitemap in Search Console.
- Sitemap file encoding and location: The sitemap file must be UTF-8 encoded. You can host your sitemaps anywhere on your site, but unless you submit your sitemap through Search Console , a sitemap affects only descendants of the parent directory. Therefore, a sitemap posted at the site root can affect all files on the site, which is where we recommend posting your sitemaps.
- Referenced URLs' properties: Use fully-qualified, absolute URLs in your sitemaps. Google will attempt to crawl your URLs exactly as listed. For example, if your site is at https://www.example.com/ , don't specify a URL such as /mypage.html (a relative URL), use the complete, absolute URL: https://www.example.com/mypage.html .
- Include the URLs in your sitemap that you want to see in Google's search results. Google generally shows the canonical URLs in its search results, which you can influence with sitemaps. If you have different URLs for mobile and desktop versions of a page, we recommend pointing to only one version in a sitemap. However, if you want to point to both URLs, annotate your URLs to indicate the desktop and mobile versions.
- The XML sitemap format is the most versatile of the supported formats. Using the Google supported sitemap extensions, you can also provide additional information about your images , video , and news content, as well as the localized versions of your pages.
- If your CMS generates an RSS or Atom feed, you can submit the feed's URL as a sitemap. Most CMSes create a feed for you, however keep in mind that this feed only provides information on recent URLs.
- If you only want to provide web page URLs, you can create a common text file that contains one URL per line and submit that to Google. For example, if you have two pages on your site, you could add them to your text sitemap located at https://www.example.com/sitemap.txt as follows:
- When creating a sitemap, you're telling search engines about which URLs you prefer to show in search results. These are the canonical URLs . If you have the same content accessible under different URLs, choose the URL you prefer and include that in the sitemap instead of all URLs that lead to the same content.
- Once you've decided which URLs to include in the sitemap, pick one of the following ways to create a sitemap, depending on your site architecture and size:
- If you're using a CMS such as WordPress, Wix, or Blogger, it's likely that your CMS has already made a sitemap available to search engines. Try searching for information about how your CMS generates sitemaps, or how to create a sitemap if your CMS doesn't generate a sitemap automatically. For example, in case of Wix, search for "wix sitemap", or in case of Blogger, search for "Blogger RSS".
- For sitemaps with less than a few dozen URLs, you may be able to manually create a sitemap. For this, open a text editor such as Windows Notepad or Nano (Linux, MacOS) , and follow a syntax described in the Sitemap Formats section. You can name the file anything you like as long as the characters are allowed in a URL .
- You can manually create larger sitemaps, but it's a tedious process and hard to maintain long term.
- For sitemaps with more than a few dozen URLs, you will need to generate the sitemap. There are various tools that can generate a sitemap . However, the best way is to have your website software generate it for you. For example, you can extract your site's URLs from your website's database and then export the URLs to either the screen or actual file on your web server. Talk to your developers or server manager about this solution. If you need inspiration for the code, check out our old, unmaintained collection of third-party sitemap generators .

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

