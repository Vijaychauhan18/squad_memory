---
source: https://www.oncrawl.com/technical-seo/seo-in-orbit-js-in-2019/
title: [Webinar Digest] SEO in Orbit: JS in 2019: modern SEO for modern users
scraped: 2026-03-23
published_on: 2019-09-24
tags: live_feed, phase1_ingest, oncrawl, publication, technical-seo, ai-visibility, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Oncrawl
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# [Webinar Digest] SEO in Orbit: JS in 2019: modern SEO for modern users

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/technical-seo/seo-in-orbit-js-in-2019/
Published: 2019-09-24
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
The webinar SEO in Orbit: JS in 2019: modern SEO for modern users is a part of the SEO in Orbit series, and aired on May 2nd, 2019.

## Extracted Body
The webinar SEO in Orbit: JS in 2019: modern SEO for modern users is a part of the SEO in Orbit series, and aired on May 2nd, 2019. For this episode, we discussed how JavaScript, its use on websites, and its support by search engines have undergone major improvements since we first realized that JS could be problematic for Google. We explore with Mike King the new possibilities to reconcile interactive, professional websites and search engine crawl technologies in 2019.

SEO in Orbit is the first webinar series sending SEO into space. Throughout the series, we discussed the present and the future of technical SEO with some of the finest SEO specialists and sent their top tips into space on June 27th, 2019.

An artist and a technologist, all rolled into one, Michael King recently founded boutique digital marketing agency, iPullRank. Mike consults with companies all over the world, including brands ranging from SAP, American Express, HSBC, SanDisk, General Mills, and FTD, to a laundry list of promising startups and small businesses.

Mike has held previous roles as Marketing Director, Developer, and tactical SEO at multi-national agencies such as Publicis Modem and Razorfish. Effortlessly leaning on his background as an independent hiphop musician, Mike King is a dynamic speaker who is called upon to contribute to conferences and blogs all over the world. Mike recently purchased UndergroundHipHop.com a 20 year old indie rap mainstay and is working on combining his loves of music, marketing and technology to revitalize the brand.

This episode was hosted by François Goube, co-Founder and CEO at Oncrawl.

Most interactive functionality on websites today are currently powered by JavaScript.

JavaScript isn’t the only option for interactivity: CSS has a lot of native interactivity built in.

Back in the day, the thinking was that for SEO, you needed a completely different static version of the page in order to work with search engines, but that’s no longer realistic. Because much of the web has adopted this type of interactivity, search engines have needed to keep up.

Consequently, SEOs have also needed to modify their approach on how we optimized pages driven by JavaScript.

Rendering addresses how a webpage is seen by different user agents.

Historically, we’ve always thought of how search engine crawlers see pages as being the HTML version of the page. This means that the interactive options powered by JavaScript weren’t, in this traditional thinking, seen by search engines.

This contrasts with a fully-rendered version of the page, which corresponds to how a user sees it in the browser.

Search engines can now crawl in a headless format, which allows them to see what users see in a browser. However, they don’t always do this. Rendering is still a different process from crawling. Rendering may or may not be carried out, or it may be carried out at a later time.

One of the major advantages of JavaScript in 2019 is facilitating increased speed on interactive pages. Using JavaScript means that you don’t have to load an entire page in order to get new information on it.

Essentially, you use AJAX to repopulate parts of the page using JSON objects. This is a lot faster than having to download every resource on the page.

This makes for a better web, and allows applications, from Oncrawl to Gmail, to exist.

The compatibility between JavaScript and UX depends on the capabilities of the developers and UX experts working on a given website.

There are instances of sites that use frameworks when they could have just been flat HTML. There are also examples of sites that use JQuery to update a single object, where there’s no need to download and use the whole JQuery library.

This comes down to the same issue we’ve always had to deal with in SEO: are people using the right tools in the right ways to create optimal experiences?

Even when JavaScript makes the user experience much faster, it can make initial pages much slower to load. If you check the developer tools when you open a web page, almost every page has slow times in the JavaScript load times.

JavaScript used to be a major SEO issue because search engines had a hard time crawling it, but that has changed.

The biggest issue today is computation expense. Having a JavaScript renderer makes your costs way higher. A page that might take a few milliseconds to download as plain HTML might take 30 seconds with JavaScript in a headless browser.

Because of the current cost, Google has to determine whether or not it’s worthwhile to render pages. Some pages have little to no material differences in content. It isn’t necessarily worthwhile for Google to render pages like this; they need to make sure that when they do render pages, it really is necessary to do it.

Mike predicts that as the computational resources become faster and cheaper, Google will have less of an issue with JavaScript. Though rendering is something of an “optional” or “secondary” step for Google today, it will likely become less of a question of WRS rendering later, and might eventually be done in parallel with the crawl itself.

François reveals that when crawling, JavaScript rendering is approximately ten times more expensive in infrastructure costs than a standard crawl. Even if Google seems to have infinite resources, a discrepancy of this magnitude means that even Google will look at the cost.

For SEOs looking at how to optimize a page for search engines, therefore, looking at how you use JavaScript can be a good point to cover.

One of the main technical issues for SEO is the disparity between rendered and non-rendered versions of content.

Mike also often sees issues concerning the implementation of SSR architecture. Many solutions require a cache refresh, which can take a long time. If the page is visited by Google during the cache refresh, Google may see it as a 5xx error, and that URL may fall out of the index.

Despite the fact that Google keeps encouraging people to do dynamic serving, progressive enhancement is still the better way to do it in order to ensure that the bulk of your content is available to any user-agent that come to your page.

Almost all modern frameworks have solutions for SSR. Some use add-ons; others, like React, have native options like render to HTML string.

If your framework doesn’t have support for SSR, you can use solutions like Rendertron or Prerender.io in order to effectively create HTML snapshots.

Mike recommends using SSR. When you add another server for third-party rendering, you’re adding latency. We want the site to be as fast as possible. This also creates another point of failure in the process.

[Case Study] Improving rankings, organic visits and sales with log files analysis In the beginning of 2017, the team of TutorFair.com asked for Omi Sido’ SEO services to help them. Their website was struggling with rankings and organic visits. Read the case study

First and foremost, consider what you’re trying to solve with a JavaScript framework. Each framework has different strengths and weaknesses.

Consider whether you’re using a new framework just because it’s new. Angular and React, for example, are pretty entrenched at this point. There’s code and experience out there that can be leveraged.

Pick something that is both tried and true and that will be around in five years.

For Mike, React seems to be the way to go at the moment. He prefers native SSR. However, you can create snapshots with a variety of different tools, so you do have a choice depending on your technical requirements. He doesn’t believe any of the major known frameworks have any specific issue that means you might want to avoid them entirely.

Up until the latest versions, Angular was not as good as React for a number of reasons. This is curious, because Angular comes out of Google itself. However, recent versions have helped bridge this gap.

Bing has recently stated that they now accept websites that push their content to the search engine through the API, removing the need to render that content. In some ways, this makes a lot more sense.

This is essentially going backwards: we used to notify search engines to come take a look at a given URL. But this actually has the advantage of speaking to an architecture for web applications that make them more portable. It makes sense for everything (app, mobile app…) to be built from a central source in the form of micro-services in which you’re able to push everything out from a single API.

For Mike, if the web goes that way, it increases portability to new modes of consuming content, and makes a lot of sense.

It would also cut down on the computational expense of crawling from the search engine’s side.

Mike expects developers to understand how the choice of framework and implementation affect SEO. Furthermore, he sees more and more that developers are aware of SEO concerns associated with site technology choices.

For a long time, developers took the position of “Google will figure it out”, but there’s a growing awareness that possibly stems from client-side rendering being so problematic for so long.

For example, libraries that support SSR, like NextJS, are things that come out of the developer community, rather than from an SEO initiative.

Mike doesn’t have a specific method to evangelize technical SEO for developers, but usually takes an approach that can be applied to anyone.

To get someone to do something for you, you appeal to their self-interest. What are developers measured on? What do they care about? Mike then tries to align SEO with these things and to demonstrate how this impacts developers’ abilities to meet their own goals. You need to show what the value is going to be to a developer’s career, to short-term OKRs… This makes implementing SEO as valuable to developers as it is to SEOs.

Mike is known for his position on the “ technical SEO renaissance “.
