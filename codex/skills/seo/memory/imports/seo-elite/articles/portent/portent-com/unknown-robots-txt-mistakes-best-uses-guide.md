---
source: https://portent.com/blog/seo/robots-txt-mistakes-best-uses-guide.htm
title: The Complete Guide to Robots.txt
scraped: 2026-04-27
tags: elite_article, seo, portent, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# The Complete Guide to Robots.txt

Source expert/publication: portent
Source homepage: https://www.portent.com/blog/seo
Original URL: https://portent.com/blog/seo/robots-txt-mistakes-best-uses-guide.htm
Published: unknown

## Why This Matters
Discovered via XML sitemap during elite bulk backfill.

## Extracted Article Passages
- Robots.txt is a small text file that lives in the root directory of a website. It tells well-behaved crawlers whether to crawl certain parts of the site or not. The file uses simple syntax to be easy for crawlers to put in place (which makes it easy for webmasters to put in place, too). Write it well, and you’ll be in indexed heaven. Write it poorly, and you might end up hiding your entire site from search engines.
- There is no official standard for the file. Robotstxt.org is often treated as such a resource, but this site only describes the original standard from 1994. It’s a place to start, but you can do more with robots.txt than the site outlines, such as using wildcards, sitemap links, and the “Allow” directive. All major search engines support these extensions.
- In a perfect world, no one would need robots.txt. If all pages on a site are intended for public consumption, then, ideally, search engines should be allowed to crawl all of them. But we don’t live in a perfect world. Many sites have spider traps, canonical URL issues, and non-public pages that need to be kept out of search engines. Robots.txt is used to move your site closer to perfect.
- If you’re already familiar with the directives of robots.txt but worried you’re doing it wrong, skip on down to the Common Mistakes section. If you’re new to the whole thing, read on.
- Make a robots.txt file using any plain text editor. It must live in the root directory of the site and must be named “robots.txt” (yes, this is obvious). You cannot use the file in a subdirectory.
- The HTTP specification defines ‘user-agent’ as the thing that is sending the request (as opposed to the ‘server’ which is the thing that is receiving the request). Strictly speaking, a user-agent can be anything that requests web pages, including search engine crawlers, web browsers, or obscure command line utilities.
- In a robots.txt file, the user-agent directive is used to specify which crawler should obey a given set of rules. This directive can be either a wildcard to specify that rules apply to all crawlers:
- Learn more about giving directives to multiple user-agents in Other user-agent pitfalls .
- http://example.com/junk-page http://example.com/junk-page?usefulness=0 http://example.com/junk-page/whatever http://example.com/junk-pages-and-how-to-keep-them-out-of-search-results
- It will not block any URL whose path does not start with “/junk-page”. The following URL will not be blocked:
- The key thing here is that disallow is a simple text match. Whatever comes after the “Disallow:” is treated as a simple string of characters (with the notable exceptions of * and $, which I’ll get to below). This string is compared to the beginning of the path part of the URL (everything from the first slash after the domain to the end of the URL) which is also treated as a simple string. If they match, the URL is blocked. If they don’t, it isn’t.
- The Allow directive is not part of the original standard, but it is now supported by all major search engines.
- You can use this directive to specify exceptions to a disallow rule, if, for example, you have a subdirectory you want to block but you want one page within that subdirectory crawled:
- User-agent: * Allow: /nothing-good-in-here/except-this-one-page Disallow: /nothing-good-in-here/
- http://example.com/nothing-good-in-here/ http://example.com/nothing-good-in-here/somepage http://example.com/nothing-good-in-here/otherpage http://example.com/nothing-good-in-here/?x=y
- http://example.com/nothing-good-in-here/except-this-one-page http://example.com/nothing-good-in-here/except-this-one-page-because-i-said-so http://example.com/nothing-good-in-here/except-this-one-page/that-is-really-a-directory http://example.com/nothing-good-in-here/except-this-one-page?a=b&c=d

## Retrieval Use
- Use when the task maps to `portent` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

