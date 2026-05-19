---
source: https://moz.com/blog/shopify-seo
title: Shopify SEO 2023: The Guide to Optimizing Shopify
scraped: 2026-03-23
published_on: 2022-01-25
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Shopify SEO 2023: The Guide to Optimizing Shopify

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/shopify-seo
Published: 2022-01-25
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Shopify is an increasingly popular platform for e-commerce sites, but it's not fully SEO-friendly out of the box. What's the best way to optimize your Shopify experience for SEO?

## Extracted Body
A trend we’ve been noticing at Go Fish Digital is that more and more of our clients have been using the Shopify platform. While we initially thought this was just a coincidence, we can see that the data tells a different story:

The Shopify platform has been steadily rising in popularity throughout the years. Looking at BuiltWith usage statistics, we can see that usage of the CMS has more than doubled since October 2017. Currently, 4.24 of the top 10,000 sites and 3.02% of the top 100,000 are using Shopify.

Since we’ve worked with a good amount of Shopify stores, we wanted to share our process for common SEO improvements we help our clients with. The guide below should outline some common adjustments we make on Shopify stores.

Shopify SEO is a set of SEO adjustments that are specific to the Shopify platform. While Shopify stores come with some useful things for SEO, such as a blog and the ability to redirect, it can also create SEO issues such as duplicate content.

We’ll go into how we handle each of these recommendations below:

In terms of SEO, duplicate content is the highest priority issue we’ve seen created by Shopify. Duplicate content occurs when either duplicate or similar content exists on two separate URLs. This creates issues for search engines as they might not be able to determine which of the two pages should be the canonical version. On top of this, oftentimes link signals are split between the pages.

We’ve seen Shopify create duplicate content in several different ways:

Shopify creates this issue within their product pages. By default, Shopify stores allow their /products/ pages to render at two different URL paths:

Shopify accounts for this by ensuring that all /collections/.*/products/ pages include a canonical tag to the associated /products/ page. Notice how the URL in the address differs from the “canonical” field:

While this certainly helps Google consolidate the duplicate content, a more alarming issue occurs when you look at the internal linking structure. By default, Shopify will link to the non-canonical version of all of your product pages.

As well, we’ve also seen Shopify link to the non-canonical versions of URLs when websites utilize “swatch” internal links that point to other color variants.

Thus, Shopify creates your entire site architecture around non-canonical links by default. This creates a high-priority SEO issue because the website is sending Google conflicting signals:

“However, the pages we link to the most often are not the URLs we actually want to be ranking in Google. Please index these other URLs with few internal links”

While canonical tags are usually respected, remember Google does treat these as hints instead of directives. This means that you’re relying on Google to make a judgment about whether or not the content is duplicate each time that it crawls these pages. We prefer not to leave this up to chance, especially when dealing with content at scale.

Fortunately, there is a relatively easy fix for this. We’ve been able to work with our dev team to adjust the code in the product.grid-item.liquid file . Following those instructions will allow your Shopify site’s collections pages to point to the canonical /product/ URLs.

As well, we’ve seen many Shopify sites that create duplicate content through the site’s pagination. More specifically, a duplicate is created of the first collections page in a particular series. This is because once you're on a paginated URL in a series, the link to the first page will contain “?page=1”:

However, this will almost always be a duplicate page. A URL with “?page=1” will almost always contain the same content as the original non-parameterized URL. Once again, we recommend having a developer adjust the internal linking structure so that the first paginated result points to the canonical page.

While this is technically an extension of Shopify’s duplicate content from above, we thought this warranted its own section because this isn’t necessarily always an SEO issue.

It’s not uncommon to see Shopify stores where multiple product URLs are created for the same product with slight variations. In this case, this can create duplicate content issues as often the core product is the same, but only a slight attribute (color for instance) changes. This means that multiple pages can exist with duplicate/similar product descriptions and images. Here is an example of duplicate pages created by a variant: https://recordit.co/x6YRPkCDqG

If left alone, this once again creates an instance of duplicate content. However, variant URLs do not have to be an SEO issue. In fact, some sites could benefit from these URLs as they allow you to have indexable pages that could be optimized for very specific terms. Whether or not these are beneficial is going to differ on every site. Some key questions to ask yourself are:

Do you have the resources to create unique content for all of your product variants?

For a more in-depth guide, Jenny Halasz wrote a great article on determining the best course of action for product variations . If your Shopify store contains product variants, than it’s worth determining early on whether or not these pages should exist at a separate URL. If they should, then you should create unique content for every one and optimize each for that variant’s target keywords.

After analyzing quite a few Shopify stores, we’ve found some SEO items that are unique to Shopify when it comes to crawling and indexing. Since this is very often an important component of e-commerce SEO, we thought it would be good to share the ones that apply to Shopify.

By default, Shopify creates a robots.txt file for your store with quite a few prewritten “Disallow” commands. We find that in most cases, Shopify’s default robots.txt rules are good enough for most store owners. You can see an example of Shopify’s default robots.txt rules here:

Here are some sections of the site that Shopify will disallow crawling in:

However, as Shopify stores get bigger and more customized, there’s a greater chance that you might need to adjust the robots.txt file. Fortunately, as of June 2021, Shopify now lets you update the robots.txt file .

In order to edit the Shopify robots.txt file, store owners must create a robots.txt.liquid file and then create custom rules to specify any changes.

In order to create a robots.txt.liquid file, store owners can perform the following steps:

This should create your Shopify robots.txt.liquid file. You can then add rules to your robots.txt.liquid file by adding liquid code. Fortunately, this code isn’t too difficult to add, and Shopify does a good job of highlighting how to do it in their official documentation . Following these steps should allow you to have much more control over which URLs are crawled in your Shopify site.

By default, Shopify will generate a sitemap.xml index file at the URL path “domain.com/sitemap.xml”. Shopify’s sitemap.xml index file will automatically create links to child sitemaps that contain URLs of the following page types:

This sitemap.xml file will dynamically update as new pages are added/removed from to the site. Generally, the Shopify sitemap.xml is good to go out of the box and doesn’t need to be adjusted.

One thing to be aware of is that Shopify will include any published pages in the sitemap.xml file. The most common issue we see is that legacy pages that are published but no longer linked to on the site get included in the sitemap.xml file. It’s worth crawling your sitemap.xml to find any instances of published pages that are included in the sitemap but are not important for search engines to crawl.

While you cannot adjust the robots.txt, Shopify does allow you to add the “noindex” tag . You can exclude a specific page from the index by adding the following code to your theme.liquid file.

As well, if you want to exclude an entire template, you can use this code:

Shopify does allow you to implement redirects out-of-the-box, which is great. You can use this for consolidating old/expired pages or any other content that no longer exists. You can do this by going to:

The big thing to keep in mind is that you will need to delete a page before you can implement a redirect on Shopify . This means that you’ll want to be really sure you’re not going to use the page in the future. To make this process a little less stressful, we recommend implementing the “Rewind Backups” app .

As of now, Shopify does not allow you to access log files directly through the platform. This has been confirmed by Shopify support .

Fast Simon is an enterprise solution that adds robust personalization features to your Shopify store, and is becoming increasingly popular. If your Shopify site is utilizing the Fast Simon technology, you’ll want to be sure that you’re taking steps to adjust any potential indexing issues from an improper implementation.

Confirm that Fast Simon is pre-rendering your website’s content so that Google doesn’t run into crawling and indexing issues. This will give Googlebot a server-side, rendered version of your site that will make it easier for it to interpret the content. For more details, you can read our case study here .

Before doing anything with regards to structured data, you’ll want to first audit how schema is being deployed across your site. By doing this, you’ll gain a much better understanding of what changes you need to make to your schema implementation.

When working with Shopify sites, we’ll often find that — upon first investigation — there are multiple instances of structured data. This is because Shopify sites will many times insert structured data from elements such as the theme and third-party apps. The result is that the pages present multiple structured elements as opposed to a single consolidated one.

In the example below, you can see a site that presents two instances of “Product” structured data.

Before starting your review, audit each different page template and note the types of structured data on that template. Are there correct elements there, are there multiple elements or is schema missing entirely? From there you’ll start to better understand what you’ll need to do in order to improve your site’s schema moving forwards.

Overall, Shopify does a pretty good job with structured data. Many Shopify themes should contain “ Product ” markup out-of-the-box that provides Google with key information such as your product’s name, description, price etc. This is probably the highest-priority structured data to have on any e-commerce site, so it’s great that many themes do this for you.

Shopify sites might also benefit from expanding the Product structured data to collections pages as well. You can actually use “CollectionPage” or “OfferCatalog” schema to tell search engines that your category page contains multiple products. This involves marking up category page elements such as individual product names, URLs, prices and more.

As well, if you use Shopify’s blog functionality, you should use “ Article ” structured data. This is a fantastic schema type that lets Google know that your blog content is more editorial in nature. Of all of the informational content schema, “Article” seems to be the one that Google may prefer since that’s what’s referenced in their official documentation. However, “BlogPosting” schema is also another type of structured data you could add to your Shopify blog

One addition that we routinely add to Shopify sites are breadcrumb internal links with BreadcrumbList structured data. We believe breadcrumbs are crucial to any e-commerce site, as they provide users with easy-to-use internal links that indicate where they’re at within the hierarchy of a website. As well, these breadcrumbs can help Google better understand the website’s structure. We typically suggest adding site breadcrumbs to Shopify sites and marking those up with BreadcrumbList structured data to help Google better understand those internal links.

If you want to implement structured data and have a developer on hand, it can be good to have them add the above structured data types. This ensures that these schema elements will always be present on your site.
