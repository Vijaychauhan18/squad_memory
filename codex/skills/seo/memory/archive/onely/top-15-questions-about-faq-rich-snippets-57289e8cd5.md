---
source: https://www.onely.com/blog/frequently-asked-questions-about-faq-rich-results/
title: Top 15 Questions About FAQ Rich Snippets
scraped: 2026-03-23
published_on: 2021-04-29
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

# Top 15 Questions About FAQ Rich Snippets

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/frequently-asked-questions-about-faq-rich-results/
Published: 2021-04-29
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Get the most out of FAQ schema! See our guide on how to properly implement FAQPage schema markup and get to the FAQ rich results!

## Extracted Body
A Frequently Asked Question (FAQ) rich result (also known as an FAQ rich snippet) consists of a list of questions and answers on a specific subject. Google pulls these answers from indexed pages that implemented the FAQ rich result schema for their content.

Once you implement the FAQ schema, parts of your page’s content become eligible to be shown in a dropdown menu of questions on the search result pages. After clicking on the questions, respective answers appear underneath.

Unlike with featured snippets , using schema is a prerequisite for displaying any type of rich results.

Schema.org provides a collection of shared vocabularies webmasters can use to mark up their pages in ways that can be understood by the major search engines: Google, Microsoft, Yandex, and Yahoo!

Add FAQ schema to help search engine robots better understand what your content is about, regardless of the language used. This lets search engines show your content in a more appropriate context, and the FAQ rich results are one example of that.

To get featured in a FAQ rich result section, you need to add the FAQPage schema markup to your website.

You can find out how to implement it in Schema.org’s documentation . It contains the properties that you can use to identify specific elements of your page.

The FAQPage type in the schema documentation is used to mark up a page that contains questions and their answers.

To be eligible for FAQ rich results, you need to include the following property from the documentation:

mainEntity – an array of Question elements containing the list of answered questions

Other types that are needed are Question and Answer schema types.

The Question type identifies a single answered question. Every Question needs to be located within the mainEntity property array of the FAQPage.

acceptedAnswer – the Answer to the question – there should be one per question

The Answer type defines the acceptedAnswer to each of the Question types on this page.

text – this contains the full text of the answer to the question

You can add the markup to your page using JSON-LD or Microdata, but JSON-LD is recommended whenever possible.

Google offers step-by-step guidelines on how to implement structured data , so be sure to check them out.

Google has a list of FAQ content guidelines that you need to follow:

They appear in both desktop and mobile search results and are available in all countries and all languages.

After choosing the page that will be a good fit and implementing the markup, you can validate it in Google Search Console. Enter the page’s URL and request that Google crawls the page again. There is no set waiting time – it could happen on the same day or take a few days or weeks.

Keep in mind that Google clearly states that structured data enables the possibility of showing up as one of the available rich results, but there is no guarantee.

The Google algorithm tailors search results to create what it thinks is the best search experience for a user, depending on many variables, including search history, location, and device type. In some cases, it may determine that one feature is more appropriate than another, or even that a plain blue link is best. source: Google

You do not need to have a specific FAQ page to have it appear as an FAQ rich result. You can use it on various types of pages, like articles, categories, or products.

By default, Google will show the first three FAQs in the search results. The maximum number of questions that Google shows is ten, followed by a link to view more on the page.

Only three pages with the FAQ markup will display as rich results on a single search results page. Also, it seems like FAQs only appear on the 1st page of Google results.

If you are using the markup but aren’t ranking on the first page of search results, it’s unlikely your page will show up as a FAQ rich result in SERPs.

Elfsight presents data on the CTR for mobile and desktop devices with and without FAQ snippets measured weekly:

FAQ snippets provide a 10% growth on desktop and an even more significant increase on mobile: 31% .

As with other SERP features, FAQ rich results may provide searchers with answers to their queries without visiting the page. It can result in more zero-click searches , which are searches that don’t end with an organic or paid click on a result.

In some cases, it can severely hurt the amount of search traffic you get.

Lily Ray shared her experience after implementing it back in 2019:

The unintended consequence of adding FAQ schema. It looks so pretty in the SERP… but where did all our traffic go? 🙄 #seo #structureddata #schema #google pic.twitter.com/yy93nGo6m8

Zero-click searches have been on the rise. According to some studies, they already reached over 50% of all searches in 2019 , and they skyrocketed in 2020, getting to nearly 65% . This is mainly due to the growing numbers of SERP features that show up in search results today.

Luckily, FAQ rich results offer a way to help you drive more traffic to your site . You can include internal linking in your answers to increase your click-through rate and encourage users to visit your site.

Apart from links, you can enhance your text in FAQs with HTML tags. Make your answers more visible by adding headings, bolding important parts, or compiling the text into lists.

This way, you can drive targeted traffic to multiple pages on your site from just this one search result.

All links that you add should be relevant and implemented carefully, as Google might penalize you if they appear like spam or advertising.

FAQ pages take up a lot of space in search results. This means they can give your site more visibility and recognition and push down other results, reducing room for your competitors on the first page of SERPs.

Using the FAQ markup can let you show up as an FAQ Action shown on Google Assistant. This way, users may access your content through voice search.

Despite the possibility of resulting in fewer organic clicks, you can still use zero-click searches to your site’s advantage. In this case, it’s harder to measure the benefits of rich results without traffic to analyze. But zero-click searches always expose your brand and information about it to an audience and make users familiar with it.

Overall, these benefits depend on your strategy and planning. Will your FAQs contain all the information in the answers? Or, will they spark the users’ curiosity and get them interested in learning more and exploring your page?

If you leverage internal links, follow Google’s policies and guidelines, and provide meaningful answers to your questions, you’ll maximize the advantages of FAQ rich results.

Q&A pages are more dynamic – they show a single question, and users can submit multiple answers. Readers can vote on which answer provides the best, most accurate information.

If this sounds more like something that fits your site’s profile, see Google’s Q&A documentation to learn more.

John Mueller was asked about this during one of the Google Webmaster Central hangouts .

A person observed that their FAQ rich results stopped appearing, despite the Rich Results Test in Search Console showing no issues with implementing structured data.

John explained that Google couldn’t show all of them and had to choose those best suited for FAQ results and for which it made sense.

It’s also likely that their number is limited because they take up so much space in SERPs – this could shrink the number of pages that fit in search results.
