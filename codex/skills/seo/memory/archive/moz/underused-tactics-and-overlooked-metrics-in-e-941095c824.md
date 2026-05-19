---
source: https://moz.com/blog/underused-tactics-and-metrics-for-ecommerce
title: Underused Tactics and Overlooked Metrics in E
scraped: 2026-03-23
published_on: 2022-08-15
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

# Underused Tactics and Overlooked Metrics in E

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/underused-tactics-and-metrics-for-ecommerce
Published: 2022-08-15
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
There are plenty of impressive tactics or metrics that aren't often discussed, not necessarily because they aren't important, but because it's easy to get locked into the rhythm of reporting on traffic and sales. With that in mind, let's look into some areas we can optimize and exploit to improve…

## Extracted Body
There are plenty of impressive tactics or metrics that aren’t often discussed, not necessarily because they aren't important, but because it's easy to get locked into the rhythm of simply reporting on traffic and sales.

To change things up, let's look into some other areas we can optimize to improve the organic performance of e-commerce websites, and some underrated but useful metrics that can help you report on that performance.

Data scraping is very useful when you want to retrieve, or scrape, elements from a page for further analysis or optimization.

Most people know that you can scrape common webpage elements such as publication date, author name, or price, but what about more specific aspects of e-commerce websites, and what can we use them for? Product pages have unique attributes that you can scrape, such as “add to basket” type buttons or even product schema; below, I’ll talk about how you can scrape breadcrumb data.

In short, breadcrumbs are a trail that shows users where they are in the structure of a website, and they are especially useful for navigation and internal linking.

By using crawling tools to scrape data from the breadcrumbs, you can have a more complete view of the site as a whole, and it allows you to identify any trends.

Below, you can see that it's possible to extract breadcrumb data as a series of values by using XPath, and setting this up as a custom field. This allows you to see the data as a separate field once a crawl is finished.

The typical page templates that you'd expect to see on an e-commerce site include:

Information pages (e.g. about us, delivery information, terms and conditions)

A large e-commerce website may have a significant number of product and category pages. These are the pages that generate the most conversions and transactions, so it is tremendously helpful to know how you can break these down into more manageable chunks.

For a website with millions of pages, it is practically impossible to crawl the whole site; your crawler will run out of memory and space, or it could take weeks to finish, and that’s just not feasible for most of us. This is where segmentation comes in. Segmenting your website also allows you to focus on one area of the site before moving on to another.

A common tactic for websites the size of Target or Tesco is to focus on one category per quarter, and then move on to another area of the site. It's through segmentation that they're able to do this.

There are many different ways you can segment a website, and focusing on your products can help you start seeing improvements in revenue sooner than if you were to focus on other areas of the site.

With product pages, a good tactic is to look for URL patterns, such as those that end in .html or contain /product/.

It's also possible to get additional dimensions from your product pages by segmenting your products by their stock status. Separating pages by whether or not a product item is in stock or not can help you determine:

Whether availability and out-of-stock products are affecting product conversion rates.

Get a granular view of what page engagement metrics are affected by stock availability.

When scraping this data, you can look for specific on-page elements such as missing prices or an Unavailable / Out of Stock message on your pages.

One method of doing this would be to extract the product availability property from a site’s schema markup. If you’re using Screaming Frog, you can access the Custom Extraction feature in the Configuration dropdown under Custom > Extraction,and then set up your extraction rules.

Segmenting category pages allows you to find any categories that have hundreds of products and could benefit from being split into subcategories.

Category pages don't always have specific URL patterns, and they differ from one CMS to another, but you can look out for those that contain /category/ or /shop/. Another good option is to look for unique attributes, such as those with text showing X of Y results or pages with options for sorting product results.

We saw earlier that you could scrape pages for instances of product data to identify product pages. But before we move on, we need to ensure we understand what structured data or schema markup is and how it can benefit e-commerce websites.

Product markup provides more information about your products directly in the SERPs when your audience searches for them. Product markup can also mean your products are more eligible for rich results, such as carousels, images, and other non-textual elements.

Once added, product schema allows your audience to see valuable information about your products before they even land on your page, improving your CTR! We can see Walmart has added product schema to their products in the two examples below:

The more positive reviews your products have, the more likely customers will be to visit your website and buy your products, especially when compared to your competitors.

Star ratings can be pulled in from your product markup through third-party tools such as Trustpilot or Reevoo, or from on-page customer reviews.

We see this when looking at these searches for Dell laptops. Realistically, which links are you more likely to click on as a customer: those with high star ratings or those with seemingly no rating at all?

There will likely be pages on your website that are useful to existing customers, such as thank you pages after placing an order, logged-in account pages, etc. However, these pages won’t be the most important for new users looking to find you or your products on search.

It costs Google time and money to crawl our sites, so they need to budget accordingly. By managing this crawl budget , we guide search engines toward our most valuable and essential pages.

It’s entirely acceptable to meta-noindex or disallow certain pages in the robots.txt file — in fact, it’s expected. This is because indexing everything could mean that Google might not crawl all of our pages, so they might not index all of our content. This would be a problem, as it could mean some of our high-value, top-converting pages might not rank organically.

That said, we shouldn’t be noindexing vast chunks of an e-commerce website without proper research. By noindexing huge chunks, we're missing out on the ranking potential for key search behavior, e.g. locations, product sizing, etc.

As users or owners of e-commerce websites, we’re likely familiar with URL parameters. Common areas that we see these parameters include:

Faceted navigation pages and product sorting options are typically blocked in robots.txt files, but it’s a good idea to find out how many of those pages Google is still serving to searchers. We can do this in our chosen crawling tool by selecting the option to ignore robots.txt rules. Alternatively, you can segment landing page session data in Google Analytics by URLs with parameters to see how many of those parameter pages are being served to users. Then, the session data will be used to show how many visits those pages are getting.

It may seem counterintuitive to do this, but these pages tend not to have unique on-page content, as they will have duplicated titles, headings, or body content, which means you could be missing out on other, more essential pages ranking for relevant keywords.

With large e-commerce websites, it doesn't make sense to simply test one or two pages and take that as a site speed reading across the entire website. Each page template is built differently. One type of page can load faster than another — even if all other test parameters are the same.

As discussed earlier, there are many different template types that can make up a successful website. Testing a selection of pages from each of these templates is recommended to get the best picture of the load time performance of your site.

An excellent way to do this is through using the PageSpeed Insights API and connecting it to Screaming Frog or using cloud tools such as OnCrawl or Site Bulb, which will test the speed of each page on your website as it crawls.

To do this in Screaming Frog, go to “Configuration”. In “API Access”, select “PageSpeed Insights”, and there you will see fields to include the API key.

Once done, in the “Metrics” section, you can select both the device that you want to track and the reports, metrics, etc., that you are interested in extracting page speed information. In the example below, we have selected Crux Data and TTFB (Time to First Byte) and LCP and FCP data. Although the crawl may take longer to complete, this information should now appear alongside the URLs in the final crawl.

There are various tools you can use to test your site speed, such as PageSpeed Insights, WebPageTest, and GTmetrix, and most of these do allow you to set your testing location.

It's important to test your e-commerce site from a location close to where your data centre is located (where your website is hosted), as well as one that is further away. Doing this lets you get an idea of how your real customers are experiencing your store.

If you have a CDN installed, such as Cloudflare, this is also useful, as it allows you to see how much of an impact the CDN is having on your website and how it helps your site load more quickly.

Wherever you decide to test from, remember to keep these locations the same each time you test so you can get accurate results.

If your e-commerce website has caching installed, it’s even more important to test your pages more than once. This is because, on the first test, your page may not have loaded over the cache yet. Once it does, your results will likely be much faster than what you saw on your first test.

With or without caching installed, I would recommend testing each page template around three times for both mobile and desktop devices to get a good measurement and then calculate the average..

Understanding the common problems that e-commerce websites make is valuable for learning how to avoid them on your own website, as the reasons some tactics remain underused come down to these errors.

Whatever your e-commerce site sells, it should be easy to navigate, with sensible menus and navigation options that clearly tell visitors what they will see when they click.

You can see this on the Boohoo website, a prominent fashion retailer in the UK. This image shows the women's dresses navigation, but you can see how it is broken down by type of dresses, dresses by occasion, colour, how they fit, and even by current fashion trends. Users are able to navigate directly to the subcategories they need.
