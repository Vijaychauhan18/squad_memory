---
source: https://portent.com/blog/seo/field-guide-to-spider-traps-an-seo-companion.htm
title: Field Guide to Spider Traps: An SEO’s Companion
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

# Field Guide to Spider Traps: An SEO’s Companion

Source expert/publication: portent
Source homepage: https://www.portent.com/blog/seo
Original URL: https://portent.com/blog/seo/field-guide-to-spider-traps-an-seo-companion.htm
Published: unknown

## Why This Matters
Discovered via XML sitemap during elite bulk backfill.

## Extracted Article Passages
- If search engines can’t crawl your site, SEO efforts do not amount to much. One of the problems I see most often are ‘spider traps’. Traps kill crawls and hurt indexation. Here’s how you find and fix them:
- A spider trap is a structural issue that causes a web crawler to get stuck in a loop, loading meaningless ‘junk’ pages forever. The junk pages might be any combination of the following:
- E-commerce sites are particularly good at creating spider traps. They often have product category pages you can sort and filter using multiple criteria such as price, color, style and product type. These pages often have URLs like “www.site.com/category?pricerange=1020&color=blue,red&style=long&type=pencils.”
- If you have, say, ten product types, seven brands, six colors and ten price ranges, and four ways to sort it all, then you’ll have (I had to take my socks off for this one) 34,359,738,368 possible permutations. This number will vary depending on the number of options. The point is, it’s a big number.
- This can make it impossible for a search engine to index all of the content on the site, and can prevent the pages that do get indexed from ranking well. There are a few reasons why this is bad for SEO:
- The result is the same: Lousy rankings. Lost revenue. Fewer leads. Unhappy bosses.
- The best way to determine if a site has a spider trap is to use a crawler-based tool like Xenu’s Link Sleuth or Screaming Frog :
- There are a lot of ways to create spider traps. Every time I think I have seen them all, our crawler finds another. These are the most common:
- An expanding URL trap can be especially difficult to see in a browser, because it is usually caused by one or more malformed links buried deeply in the site. As with any spider trap, the easiest way to spot it is to crawl the site with a crawler-based tool. If the site has this issue, the crawl will reveal the following things:
- In most expanding URL spider traps, the file path is the part of the URL that gets longer. There are three ingredients that must all be present in order for this to happen:
- Ingredient #1: The site uses URL rewrite rules to convert path components into query parameters. For example, if the public URL is: http://example.com/products/12345/xl/extra-large-blue-widget then, on the server side, the rewrite rules might convert this to: http://example.com/store/products.php?prod_id=12345&size=xl In this example the “/extra-large-blue-widget” part is discarded, because it is ‘decorative’ text, added solely to get keywords into the URL.
- Ingredient #2: The rewrite rules are configured to ignore anything beyond the part of the URL they care about. For example, in: http://example.com/products/12345/xl/extra-large-blue-widget the rewrite rules would silently discard everything after “/products/12345/xl/”. You could change the URL to: http://example.com/products/12345/xl/ or even: http://example.com/products/12345/xl/here/is/junk/text/that/has/no/effect/on/the/output and the server would return exactly the same page.
- Ingredient #3: The final ingredient is a malformed relative link that accidentally adds new directory levels to the current URL. There are many different ways this can happen. For example:
- This issue happens when a site has a finite number of items that can be sorted and filtered in a virtually unlimited number of different ways. This is most common on large online stores that offer multiple ways to filter and sort lists of products.
- This type of filter creates a trap because each option multiples the number of possibilities by two or more. If there are many filters, the number of combinations can get extremely large very quickly. For example, if there are 40 different on/off filtering options, then there will be 2 40 , or over a trillion different ways to sort the same list of products.
- That’s 36 quadrillion different ways to view the same list of a few thousand products. For all practical purposes, this can be considered infinite. To make matters worse, the vast majority of these will contain zero or one items.

## Retrieval Use
- Use when the task maps to `portent` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

