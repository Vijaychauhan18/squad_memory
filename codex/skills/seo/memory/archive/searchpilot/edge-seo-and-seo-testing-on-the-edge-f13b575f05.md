---
source: https://www.searchpilot.com/resources/blog/edge-seo
title: Edge SEO and SEO testing on the edge
scraped: 2026-03-23
published_on: 2023-08-07T09:56:12+01
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Edge SEO and SEO testing on the edge

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/edge-seo
Published: 2023-08-07T09:56:12+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
SEO at the edge means any SEO changes that are made after the HTML is created by your CMS or origin server before it is served to the user. These changes are made closer to the user by modifying the HTML on the way “through” a CDN-like layer. The biggest benefit is that you aren’t constrained in the changes you can make. Between engineering resource constraints, and technical limitations of some web platforms, there are certain kinds of changes that can be difficult, prohibitively expensive, or 

## Extracted Body
The edge refers to the outer layers of a networking diagram that has the origin server “inside” proxy layers like Content Delivery Networks (CDNs) or services like SearchPilot:

Edge computing refers to the ability to run code on servers in the layers “outside” the origin server and make changes to a page’s content, or HTTP response. This is how SearchPilot works .

Serverless in this context essentially just means “at the edge”, and so in this case they are essentially synonyms. There are also other technologies (e.g. job queues) that can be referred to as “serverless” in other contexts. In reality serverless really just means “someone else’s server” and any edge technology of course does use servers. The reason it is commonly called serverless is that you, as the end user, do not have to administer the servers - their existence is abstracted away from you.

Coming from an SEO perspective, the key point about all these technologies is that they make server side changes that, as far as googlebot and users are concerned, are indistinguishable from code changes on your server or updates via the CMS.

Definition : SEO at the edge means any SEO changes that are made after the HTML is created by your CMS or origin server before it is served to the user. These changes are made closer to the user by modifying the HTML on the way “through” a CDN-like layer.

SearchPilot works in a very similar way to the edge technologies described above

Compared to CDN edge workers, SearchPilot brings two key benefits:

The biggest benefit is that you aren’t constrained in the changes you can make. Between engineering resource constraints, and technical limitations of some web platforms, there are certain kinds of changes that can be difficult, prohibitively expensive, or even impossible to make via a CMS or origin code change. Many of these changes are quick and easy to make by modifying the HTML output at the edge.

Precisely because it is easy to make any change you want to any group of pages you want, another key benefit comes from testing changes. This is the key insight upon which the whole SearchPilot business is built. The nature of SEO means that it is typically impossible to predict which changes will have a substantial impact, or even whether a particular change will be positive or negative, and so testing through an edge platform enables the answer to be determined in an agile fashion, and can form the business case for implementing positive changes at the origin.

For an SEO team, the benefit of an edge platform like SearchPilot, that comes with a meta CMS , is that you can make these enhancements, and run these tests easily, quickly, and without relying on your engineering team for every single one.

Changes made on the edge appear (to googlebot and users) exactly as if you had made the change by deploying code or making a change in the CMS. That combination - of visibility to googlebot, and flicker-free user enhancements without performance impact - also enables what we call full funnel testing which combines user experience / CRO testing with SEO testing. This is very aligned with Google’s priorities: all Google’s talk of Core Web Vitals, the page experience update etc, are proxies that they are using as they attempt to align their search results with the best user experience that also satisfies the searcher’s intent.

In many cases, the technology is quite new, and so it’s often not super user-friendly and involves writing worker code directly. This is one of the areas where we’re innovating at SearchPilot by building a CMS-like layer (that we call the meta CMS ) to make these changes easy.

For obvious reasons, engineering and operations teams need to get very comfortable with any technology that is going to be deployed into their stack. Our approach is:

It can also be a form of technical debt to have your SEO performance reliant on not only your CMS / origin functionality, but also enhancements done at the edge, and if you’re not careful, can make certain kinds of future changes slower to make. Our focus is on testing to build the business case to roll most enhancements into the origin where possible. The functionality that then remains on the edge is only those beneficial changes that are not possible or economical to make anywhere else in the stack.

Finally, it is critical to build good quality assurance and testing processes because many edge changes involve modifying HTML rather than creating it from scratch.

It can be hard to test your changes if they apply to a large number of pages because without checking every page, it’s hard to be sure that whatever element you are modifying is present / is the same on every page in the site section. For example, a common kind of change we make is to modify page titles to include additional information found elsewhere on the page, such as price, and that relies on the price being correctly available and marked up in the same way on every page in the site section.

Changes made at the edge can be brittle - meaning that if changes are made by deploying a new version at the origin, or even updating information in the CMS in some cases, your edge changes can become invalid. We work hard to make sure that this degrades nicely and doesn’t cause errors, but it means you need to coordinate even more closely with other teams making changes to the site (NOTE: SEOs should be doing this anyway, but this raises the importance of it).

Ultimately what this means is that we have to think more like developers than normal. Normally, when we specify a change for SEO benefit that is implemented by developers, it’s their job to make sure that no site functionality is broken in the process. If we are making edge changes, we have to do the quality control and testing to make sure that, for example, our changes to HTML structure haven’t broken site search.

The similarity is that either approach can change any aspect of the DOM. The difference is that JavaScript is modifying the DOM only in the browser, whereas edge changes mean that the enhancements and changes are served in the HTML source. By making changes at the edge, we can also modify HTTP headers, add or modify redirects, or even create entirely new pages.

In addition to drawbacks that also apply to edge SEO, JavaScript changes have other downsides including:

Although you can change anything about the HTML page source, or HTTP response of any page on the site at the edge, there are certain kinds of changes that we see more often than others either because they are very well-suited to SEO testing, or because they are often easy to make at the edge and harder to make at the origin, and so it makes sense to test them on the edge first.

The speed and ease of making changes at the edge enabled us, for one large fashion ecommerce retailer, to make fixes, stay on top of fast-moving trends, and enhance the sites in ways that were difficult to do at the origin. Changes included:

For a large travel site customer, we measured a +14% uplift in organic traffic from the implementation of schema on crucial pages, a change that was hard or impossible to make at the origin.

We gained rich review snippets in the search results by implementing schema for a major ecommerce customer and drove a +20% uplift in organic traffic . (You can read the full test result here - it’s an interesting one, because review schema alone was more effective than price + review schema).

The same customer drove a +21% increase in organic traffic through the addition of a small amount of copy to key gallery pages that were previously very “thin”. By testing this at the edge, using content stored in a database at the edge, the value of the change was easy to prove and quantify, and therefore justify engineering team involvement to implement at the origin.

We performed a full HTTPS migration under time pressure including rewriting paths to assets to be secure. The rollout of the Chrome version that would have flagged the customer’s site as insecure was imminent, and the only way they could make the change by the deadline was to rely on edge changes to rewrite paths etc. You can read the full details of the emergency HTTPS migration here .

For a large offline retailer, whose website combines multiple different sections powered by different content management systems (and some without content management), we have found huge value in:

Watch this video with our Head of Customer Success Emily Potter taking part in the Majestic SEO webinar “SEO on the edge” :
