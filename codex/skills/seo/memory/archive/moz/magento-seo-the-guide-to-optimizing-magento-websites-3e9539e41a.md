---
source: https://moz.com/blog/guide-to-magento-seo
title: Magento SEO: The Guide to Optimizing Magento Websites
scraped: 2026-03-23
published_on: 2021-08-17
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

# Magento SEO: The Guide to Optimizing Magento Websites

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/guide-to-magento-seo
Published: 2021-08-17
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
If you’re an SEO in the e-commerce space, it’s important to learn how to work with Magento. Today, Chris walks you through seven areas for SEO adjustments that are unique to the Magento platform.

## Extracted Body
When it comes to e-commerce platforms, there are few that are more robust than Magento. Due to its power and customizability, Magento is still the go-to e-commerce platform for retailers. This is especially true for enterprise stores. Magento is utilized by many enterprise sites such as American Express, Ford, Puma, Xerox, and more.

In 2019, it was estimated that Magento accounted for 30% of the e-commerce market share . Using BuiltWith data , we can see that 1.04% of the top 1 million sites utilize the platform, and Magento’s share of the market grows to 1.77% in the top 10,000 sites.

If you’re an SEO working in the e-commerce space, it’s going to be important to learn how to work with Magento. Fortunately, there are a lot of really good things that Magento does out of the box from an SEO perspective. However, there are definitely some considerations you’ll need to take into account with any Magento site.

Magento SEO is a set of SEO adjustments that are unique to the Magento platform. Magento has great features for SEO such as a robots.txt file, sitemap.xml and multiple ways to redirect pages. Magento SEO issues include duplicate content from the faceted navigation, improper canonical tags, and a lack of blogging functionality.

Below you can see our recommendations for improving SEO on the Magento platform:

One of the biggest SEO issues with any Magento site is likely going to be the faceted navigation. Faceted navigations create huge crawling and indexing issues since their existence exponentially increases the number of pages that can be crawled. As pages in the faceted navigation will only either sort or narrow existing products, these pages create duplicate and similar content. Alsol, if you think about the fact that every single combination of parameters could be considered a unique page, the number of pages a faceted navigation creates can be enormous. In this example , Google showsa video from Google, they indicate how a store with 158 SKUs actually created 380,000 unique URLs that Googlebot could crawl. Not ideal!

If your Magento store utilizes faceted navigation, you’re likely going to need to take steps to control the crawl. While a how-to on controlling the crawl of a faceted navigation could warrant multiple blog posts, I’ll try to summarize steps that should be taken.

Audit to find low-quality, indexed pages from the faceted navigation. Identify steps to remove them from the index (noindex, canonical tag)

Review the site’s log files to find any low-quality pages that are getting crawled

Block the crawl of any low value parameters through the robots.txt

Consider only allowing pages with high search potential to be indexed

Of course, the steps taken here are going to vary a lot depending on the site. The overall point is that if you utilize a faceted navigation on your Magento site, one of the most important things you’ll need to do is review how Google is crawling and indexing the pages that are being generated and take steps to remove the indexation and then block the crawl of low quality or duplicate pages.

By default, a Magento site’s canonical tags won’t be set for both product and category pages. This isn’t ideal, as it’s best practice to ensure that product and category pages have self-referential canonical tags. This indicates to the search engines that these pages are the pages that should be ranking well.

Ensure that “Use Canonical Link Meta Tag For Categories” and “Use Canonical Link Meta Tag For Products” are set to “Yes”

By adjusting these settings, this should ensure that all of the site’s product and category pages will have self-referential canonical tags applied to them.

When looking at paginated URLs of Magento sites, we can see that, by default, proper canonical tags are not set. In Magento, all of the paginated URLs in a given series have a canonical tag that points back to the root category page. For example, here is how the canonical tag of “Page 2” of a particular category would look:

Technically, this is not best practice from an SEO standpoint. Canonical tags should only be used to consolidate duplicate content. Since paginated content are not duplicates of the root versions (as they contain different products), they should not have canonical tags that point to this version. Instead, every page within the pagination series should have it’s own self-referential canonical tag . This will tell Google that the paginated URL contains unique content and should be crawled accordingly.

You might need to have a developer create a custom solution that allows the site’s pagination to utilize self-referential canonical tags instead of pointing to the root category page.

Another Magento SEO issue is that internal search pages are indexable out of the box. This means that Google can crawl and index these low-quality pages. These pages will generally be in the /catalogsearch/ URL path.

For example, here’s a Magento site where over 4,000 internal search pages have gotten caught in Google’s index:

In order to ensure that these pages don’t get indexed by Google, you’ll want to be sure the “noindex” tag is applied to them. We recommend having a developer implement this for you and providing this article as a reference point for them .

After you’ve implemented the “noindex” tag, you’ll want to be sure that none of your internal search URLs are actually getting indexed. Perform a search for “ site:example.com inurl:/catalogsearch /”. If you see URLs appearing in the index, we recommend waiting until Google removes the majority of them. If you don’t see the URLs in the index, you might consider blocking them by using a robots.txt command.

Within Magento, you can also configure the robots.txt file. You’ll want to utilize the robots.txt file in order to limit how many pages of your Magento site that Google is eligible to crawl. This is especially important to configure if your site utilizes a faceted navigation that allows users to select from a variety of attributes.

Fortunately, Magento does allow you to control the robots.txt of your site. To do this, you can perform the following steps:

In the Admin sidebar, navigate to Content > Design > Configuration

Add your robots.txt commands in the “Edit custom instruction of robots.txt File” field

How you adjust the robots.txt is going to depend on your particular store. Unfortunately, there is no one-size-fits-all option here. The main objective will be to block the crawling of any low value pages (that aren’t indexed) while allowing the crawl of high priority ones.

Below are some general things you might consider blocking in the robots.txt:

Low value pages created by the faceted navigation and sorting options

Sitemap.xml files ensure that Google has a pathway of discovering all of your site’s key URLs. This means that regardless of the site’s architecture, the sitemap.xml gives Google a way of finding important URLs on the site.

Fortunately, Magento has the capability of creating a sitemap.xml file and does a good job of this in it’s default settings. You can technically configure the XML sitemap settings in Magento’s “Catalog” menu . However, most of these should be okay.

While these settings are configured, you might need to generate your sitemap.xml file so it will actually be published on the site. Fortunately, that process is very straightforward. You can do this by:

For “Path”, choose the URL path you want to be associated with your sitemap.xml file. This is generally at the “/pub/” URL path

This should correctly set up your sitemap.xml on Magento. You’ll then want to be sure to submit your sitemap.xml file to Google Search Console so Google can discover your sitemap.xml file.

Something else that you’ll want to be mindful of on Magento sites is any content that is loaded through JavaScript. Magento frequently utilizes JavaScript to load key content on the store. While this isn’t inherently a negative thing for SEO, it is something you’ll want to be sure you’re reviewing.

If JavaScript is required to load key content on a page, this means that Google must perform a two-step indexing process where it processes the initial HTML, and then must return to the site to render any content loaded via JavaScript. Where SEOs need to check is in the second stage of the indexing process, to ensure that Google was able to “see” all of the content that is on the page. If any elements are loaded via JavaScript, it’s worth checking whether they’re indexed.

For instance, here’s an example of a product page in Magento where JavaScript is enabled in the browser. We can see thumbnail images, text in tabs, and a related products section at the bottom:

However, most of that content is reliant on JavaScript to load. When turning JavaScript off using the Web Developer extension for Chrome , most of those elements do not render. Notice how we can only see the initial three tabs on the page:

Since JavaScript is required to load a lot of the content on the page, we’ll want to ensure that it’s getting indexed properly. Fortunately, we can use tools such as The Mobile Friendly Testing Tool and The Rich Results Test to determine what Googlebot is able to render on the page.

We also like to manually check the index by identifying content that’s loaded via JavaScript, and then using a “site:” search operator to verify that Google is able to read that text on the page. JavaScript SEO is a very expansive subject and I suggest reading this guide by Pierce Brelinsky for more information. Just understand that if you use Magento, some of your content is likely loaded through JavaScript.

Out of the box, Magento will add the URL extension “.html” to the end of the site’s product and category URLs. While this isn’t necessarily “bad” for SEO, it does create lengthier URLs that are harder to read from a user perspective. URLs without the “.html” extension will have a much cleaner format for users.

To remove the .html extension from the end of URLs, you can take the following steps:

The result will be cleaner and easier to read URLs for your store.

Please note that this is best done for a brand new Magento site . This change will automatically adjust all of the URLs on your Magento store. If your store has already existed for some time, without proper migration planning, changing this field could actually result in ranking drops. Therefore, tores that have been established a while may want to consider keeping the “.html” extension.

In addition, the old URL paths won’t automatically redirect back to the new URLs without the “.html” extension. This means that you might need to implement global redirect rules to ensure that the old pages will redirect both users and search engines.

Magento does implement global redirects on your site. This means that if your store utilizes a “www” subdomain or “https”, if a user doesn’t enter those attributes, Magento will still redirect the user to the correct destination URL. This is great for the user experience of the site, as users should land on the correct content even if they don’t type in the exact destination URL in those instances.

However, Magento does this through 302 redirects instead of 301 redirects:

Back in 2016, there was a famous study by Wayfair that showed that 302 redirects could significantly dilute link equity. While Google has claimed that 302 redirects pass link equity , this argument is still a never-ending debate in SEO. While we believe that 302 redirects do distribute much more link equity then they once did, we take the stance that you should never utilize 302 redirects unless you absolutely need to.
