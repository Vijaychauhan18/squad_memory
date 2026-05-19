---
source: https://yoast.com/google-search-console-emails/
title: Did Google Search Console send an email with an error message?
scraped: 2026-03-23
published_on: 2021-06-18
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

# Did Google Search Console send an email with an error message?

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/google-search-console-emails/
Published: 2021-06-18
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Google Search Console loves to send emails. But what can you about the structured data errors it mentions? Here's an example for products.

## Extracted Body
Make your products stand out in the search results. Use AI to save time doing SEO tasks . Get extra SEO features for your WooCommerce store.

We are big fans of Google Search Console — and you should be too! It’s an essential tool to keep your site working properly and find opportunities to get better results from the SERPs. But, one thing Google Search Console also does, is send you emails when they encounter an issue. And those error messages can get somewhat cryptic.

Structured data has been a big deal for a while now. With structured data , you can describe your content so that search engines understand it instantly. Of course, there’s a big if — your code has to be correct and valid for search engines to grasp it fully.

There are three things at play here. For one, you need to provide the required structured data to get a chance for Google understanding the content. Doing this gives you a good shot at getting a rich result for that piece of content.

Second, you might need to provide as many of the recommended properties to get the full rich result. For instance, if you have reviews on your site, it’s a good idea to mark these up with everything that makes sense for your page. Required is stuff like the author’s name and the item reviewed, while the publishing date is recommended. Leaving that last one out might not make your review rich results as full-formed as others.

Third, this goes without saying, but you have to fix any error that pops up or else you want receive those shiny rich results!

Search Console is an essential tool to monitor the technical implementation of your structured data. If you’ve signed up, Google can send you emails when something is wrong.

Add your site to Search Console , and you’ll automatically let Google keep an eye on it. Google will send you an email to let you know of the problem it encountered. This might be anything, from URLs that became unavailable to advise on migrating to HTTPS or from mobile usability issues to recommendations to improve your structured data.

Generally, it’s awesome that Google notifies site owners and managers of issues that might have a big effect on a site’s performance. Unfortunately, the messaging is not always that clear. The solutions they ask for are sometimes cryptic and unintelligible for the ‘regular’ user. Case in point, even we were startled by an email about something called SharedArrayBuffers ! Nobody has ever heard of something called SharedArrayBuffers .

Of course, this is an extreme example, but most of the time, the emails hardly give you a clue on the importance and where to fix what. Most of the time, it’s a ‘We found an issue, please fix it’ type of deal. That’s not helpful, and it might even scare people with a bit less knowledge about (technical) SEO. In addition, it might take away the people’s focus! Often, it’s better to simply improve your site than obsess over messages from Search Console — these are usually peanuts compared to the other work you can do.

This post will go over an example of a recent structured data email that Search Console sent. In this case, we’ve provided solutions to the problems Google found in the structured data of this particular site. For this, we are using the WooCommerce SEO plugin .

Online stores should do everything they can to get their product and offers structured data in order. If not, this might hurt your performance — not only in the regular search results but also in Google Shopping.

So, whenever you see an email like the one below appear in your mailbox, you know it’s time to get to work. The email below shows which product properties Google missed on your page(s). In this case, priceValidUntil , availability , sku , and brand . The posting also misses a global identifier for the product, like an article number.

Rich results for products come with many properties, and one of the most interesting ones is availability . This tells Google if your product is in stock, out of stock, or even on backorder from the factory. Adding this makes your product listing more attractive in the SERPs and helps customers see immediately if you have your product in store.

Does your online store run on WooCommerce? Then you’re in luck because these errors are a quick fix with the WooCommerce SEO add-on for Yoast SEO . WooCommerce SEO, by default, adds loads of product structured data. To fix your availability, open a product and go to the inventory section. From there, make sure that you’ve selected the proper availability of the article.

The priceValidUntil message has something to do with sales or temporary price drops. With this field, you can add a date to your sale that signals Google when the sale ends and the regular price will show up again.

This is an easy fix with our WooCommerce SEO add-on. You only have to configure the sale price and the duration of your products’ sale in the General tab of the WooCommerce meta box. Then, the WooCommerce SEO plugin will automatically add the correct structured data to your product and fix the missing field priceValidUntil issue!

Every product should have a stock-keeping unit attached to it. A what? An SKU is a number that identifies a product, making it easier to discover amongst all those other products. If you get a message from Google Search Console asking you to fix the missing field ‘sku’, then you are happy to hear that this is an easy fix with WooCommerce SEO. Open a product, click on Inventory and enter an SKU in the field at the top. All done!

We have an article explaining how to fix the missing fields ‘sku’ message .

Again, WooCommerce SEO helps you set this up. In the regular Yoast SEO settings, go to WooCommerce SEO and find the Schema.org and OpenGraph settings. Here, you can set up the types for the manufacturer, brand, and colors. Don’t forget to save the changes once you are done!

This one is not in the email mentioned early, but another one that pops up often is the message Either ‘offers’ , ‘review’ or ‘aggregateRating’ should be specified. A message like this is all about the basics of product structured data on your site. Without these properties, Google has trouble finding your products and using the data to produce rich results for your product.

While WooCommerce should output these by default, our WooCommerce SEO offers much better integration of all the different product structured data properties. Also, it makes sure that your product structured data ties in neatly with the structured data Yoast SEO generates for your site. By doing this, Google has a much bigger chance of understanding your content, site, and products.

After you’ve fixed the errors or enhanced your structured data implementation with recommended properties, you can validate these as fixed in Google Search Console. This way, Google will know that you did the work and check if that is really the case. If so, the error will stay away and you might get an email like the one below:

Google Search Console sends out many emails, and it might be a bit scary to see one with an error message appear in your mailbox. Whatever you do, don’t panic. You are often alerted to a possible improvement to make — instead of an error on your site. Read the email carefully and try to find out if the message makes sense — and what you can do about it.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

A much needed post for me. Most of my blogs were not ranking. Now I know the reason

Hi Prashant, it’s good to hear you found the post helpful! If you’re interested, we have another article here about reasons your pages might not be ranking . Good luck!

Thanks for sharing this information it’s really helpful to me as you know google console its really pathetic sometimes when they send emails and say there are some issues in your accounts.

Google has gone nuts. They even send emails for blogger hosted blogs. I have one blogger hosted blog and it shows tons of errors. Last time, they were showing error for insufficient https coverage for that blog, even when I have already enabled https for my blog.

Hi Hemendra. Wouldn’t say they’ve gone nuts, but the messaging system is not flawless. I would simply keep an eye on the messages and see of there’s something in need of fixing right away. If not, you probably have bigger fish to fry.

Thank you for this article. Sometimes the search console is very annoying. Especially when it says that there are problems with the mobile version.

Hi! I’m glad a tool like Google Search Console exists, as it provides so many great insights. Sending emails to keep you informed is also a good idea, but the execution can still improve.

i got a few times “Coverage issue, Server error (5xx)” message for one of my blog that using free blogspot. that sound funny, as if you are reviewing your own product badly

We care about the protection of your data. Read our privacy policy.
