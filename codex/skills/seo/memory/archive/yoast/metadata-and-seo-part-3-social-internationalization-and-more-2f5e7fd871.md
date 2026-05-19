---
source: https://yoast.com/metadata-and-seo-part-3-social-internationalization-and-more/
title: Metadata and SEO part 3: social, internationalization and more
scraped: 2026-03-23
published_on: 2017-03-15
tags: live_feed, phase1_ingest, yoast, publication, seo-education, wordpress-seo, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Yoast SEO Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Metadata and SEO part 3: social, internationalization and more

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/metadata-and-seo-part-3-social-internationalization-and-more/
Published: 2017-03-15
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
In this last post on metadata and SEO, we'll dive into social metadata and metadata that you need for internationalization

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Literally, metadata is data that says something about other data. You can use particular metadata to send information about a webpage to a search engine or a social media channel, and thereby improve your SEO. In the first two posts of this metadata series, we discussed meta tags in <head> of your site and link rel metadata. In this last episode, we’ll scrutinize on metadata that can improve the sharing experience on social media. And last, but definitely not least, we’ll describe why metadata like hreflang declarations are a necessity if your business serves multiple languages and/or countries.

Social metadata We have written about Open Graph and Twitter Cards before. These tags, or this information, is definitely metadata. It will help you tell social networks like Facebook and Twitter what the page at hand is about in an orderly, summarized way. It will allow you to control the way your articles or pages are shared.

OpenGraph is a standard used by a number of social networks like Facebook and Pinterest. If you’re using our Yoast SEO plugin, these tags are added to your page automatically, and of course, you can control the contents of these OpenGraph tags (in the social section in our meta box below on edit pages).

The same goes for Twitter Cards. They add metadata to your pages that are convenient for Twitter to read and understand. Our plugin adds Twitter Card metadata as well. If there is no Twitter Card data, Twitter will fallback to OpenGraph data, but you obviously want to make things as simple as possible for that Twitter.

If you’d like a preview of how your page, shared on either Twitter or Facebook would look like, please check our Yoast SEO premium plugin , as that one adds these social previews right in your WordPress backend .

If you thought that all the things previously mentioned are all the SEO related metadata for your website, think again.

For those of you that have multilingual sites, this one is really, really important. If you have a site or page that is served in more than one language, be sure to add hreflang tags to your page.

With hreflang tags, you can indicate the language variations of the page at hand. That looks like this:

As you can see, these can be used for variations of the ‘same’ language as well, like the British English in the second line. Note that hreflang isn’t a substitute for the rel=canonical we discussed. Be safe, implement both. More information on how to implement hreflang can be found here .

If you think about it, any extra attribute you assign to an image, like the alt or title tag, is metadata. Google uses it to scan the page and see what’s on there, so be sure to add these alt and title tags and optimize ’em .

For a better understanding of your site’s structure, you should add some kind of microdata to your breadcrumbs . That can be done by adding schema.org data for breadcrumbs, for instance by JSON-LD . RDFa is another option to add this type of metadata to your website. Again, install Yoast SEO for WordPress and this is taken care of.

Let’s wrap this long list of metadata up with another language related metadata element. At the very top of your HTML, we find the, indeed, html tag. This one wraps all the code of your <head> and <body> and can contain the language of the page at hand. That is done like this:

Makes sense, right. Some might say that adding a meta tag for Content-Language is also an option, but following the W3C guidelines, that meta tag should not be used anymore . Use the lang declaration in the html tag instead.

That concludes this series with a lengthy list of metadata you can use to tweak your SEO. I am confident you can come up with even more metadata, as there is plenty. Feel free to leave your additions in the comments!

Michiel was one of our very first employees and used to be a partner at Yoast. Kick start your site optimization with his articles!

We care about the protection of your data. Read our privacy policy.
