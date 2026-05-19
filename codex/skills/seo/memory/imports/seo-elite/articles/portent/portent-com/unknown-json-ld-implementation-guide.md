---
source: https://portent.com/blog/seo/json-ld-implementation-guide.htm
title: A JSON-LD Implementation Guide
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

# A JSON-LD Implementation Guide

Source expert/publication: portent
Source homepage: https://www.portent.com/blog/seo
Original URL: https://portent.com/blog/seo/json-ld-implementation-guide.htm
Published: unknown

## Why This Matters
Discovered via XML sitemap during elite bulk backfill.

## Extracted Article Passages
- SearchFest 2016 (aka the last “SearchFest” ) had a load of great talks, but only a few were as immediately relevant to my work as the deep dive discussion of structured and unstructured data from AJ Kohn and Mike Arnesen . They lent great insight to my approach to these two different types of information, and deepened my appreciation for structured data at large. This was also my first exposure to JSON-LD, the hot new thing in the space.
- Fast forward a month or two and I’ve got a client with a problem that is best solved by better structuring their data, and for whom switching to JSON-LD made practical sense.
- While in-depth discussion about JSON-LD was easy to come by, no single resource gave me enough footing to properly start to run with it.
- This is my attempt to create the resource I wish I’d found when I went to apply the technology.
- JSON-LD (JavaScript Object Notation for Linked Data) is a method of implementing structured data markup on a website. It’s been in use for a few years, and is used and supported by Google, Bing, Yandex, and many smaller search engines.
- JSON-LD utilizes the widely known JSON notation. This syntax is considerably simpler and more widely known than either microdata or RDFa, which also means that it is easier to implement and less prone to human errors.
- Like Microdata and RDFa, JSON-LD can exist in the body of the page, but can also be used in the head. It also allows for multiple blocks of script, which can be useful for breaking it into more manageable chunks.
- In this post we’ll break down the basics of the code and its implementation, touch on some general tips for utilizing and validating the code, and wrap with a pair of examples for further study.
- The following code is an example of JSON-LD as it would appear on the page. We’ll walk through the various elements of the code and cover the essentials of each:
- This code is the script that contains the JSON-LD within the HTML of the rendered page. If your JSON-LD isn’t in those curly brackets, it isn’t being parsed by the search engines or applied to the page.
- @context defines the vocabulary that the data is being linked to. In this example our @context references all of schema.org. This allows us to use any of the Types or Properties it defines and is more than enough to cover most structured data use cases.
- A more advanced execution of @context can use specific URLs to define terms manually like Properties. These terms can then be defined as @types later in the script, allowing a greater degree of specificity or allowing us to call alternative vocabularies:
- This kind of granularity isn’t generally needed. If you aren’t sure how specifically it would be useful to you, you’re likely better off sticking with schema.org.
- We use @type to call the Type of entity you are describing. For those with prior experience using microdata, this is our “itemtype.” In the example, we first use @type to describe the webpage itself, and then call it again to define the “mainEntity” of the page.
- There is no equivalent to itemprop in JSON-LD. Once we reference a Type, any Property that can apply to that Type can be called and defined. In this case, we first reference the webpage Type so that we can define a breadcrumb for search engines to use in their results.
- Pro Tip: After every property but the last, you must include a comma. This tells the engines parsing your code that there is more to come. If the last property has a comma however, this will return an error.

## Retrieval Use
- Use when the task maps to `portent` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

