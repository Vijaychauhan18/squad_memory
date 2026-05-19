---
source: https://www.onely.com/blog/top-5-insights-rendering-seo-explained/
title: Top 5 Insights from "Practical Rendering SEO Explained" with Martin Splitt and Bartosz Góralewicz
scraped: 2026-03-23
published_on: 2021-10-06
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

# Top 5 Insights from "Practical Rendering SEO Explained" with Martin Splitt and Bartosz Góralewicz

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/top-5-insights-rendering-seo-explained/
Published: 2021-10-06
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
These are the top insights from a webinar with Martin Splitt and Bartosz Góralewicz on the topic of Rendering SEO from October 6th, 2021.

## Extracted Body
On October 6th, 2021, Bartosz Góralewicz spoke to Martin Splitt from Google about Rendering SEO – a topic they’ve been covering and exposing to the SEO community for a while now.

The webinar was hosted by Jason Barnard and organized by Duda.co .

You can read the full transcript here and watch the recording here , but in this short article, I want to talk about some of the things I found most notable in that conversation.

Bartosz opened the discussion up with a fundamental question to many SEOs, and Martin’s reply was pretty straightforward: Yes, if something goes wrong when Google is trying to render your page, it can hurt you.

Rendering is an essential step in Google’s indexing pipeline. It primarily consists of fetching resources and executing JavaScript to create a layout tree for a given page. That layout tree is a crucial source of information about that page for Google – it helps understand where the main content is located, what the page is about, and it’s used in the further steps that lead to your page showing up in the search results.

Even the most minor bug in your code can lead to a portion or even a whole page rendering improperly, both in your users’ browsers and for Google’s Web Rendering Service. The consequences of that may vary from the page not getting indexed because Google can’t see the content to some parts of that content not getting indexed, which may, in turn, damage your rankings.

And unfortunately, even looking at some very popular websites, you’d find plenty of bugs and JavaScript that’s simply too heavy to render – our research suggests that heavy scripts are often responsible for the problem of partial indexing .

This point is critical because it implies that you should look into how Google might render your website regardless of whether or not you’re using JavaScript.

Rendering is often conflated with JavaScript execution, but it’s more than that – it involves all visual elements of your website, such as menus, link carousels, images, videos, and even text paragraphs.

While debugging JavaScript is the trickiest part of Rendering SEO , you should aim to understand how Google processes non-JS elements too.

For instance, you can make Google’s job easier and thus speed up the indexing process by using image dimensions for all your images. This allows Google to skip rendering images and use the provided dimensions for generating the layout tree. It also helps with your crawl budget, because the image files won’t have to be fetched!

Do you need some help with JavaScript SEO on your website? Feel free to contact us for JavaScrict SEO services .

Bartosz asked Martin how SEOs can make the rendering process easier for Google when optimizing resources. His reply was interesting, and I think it’s something that’s not mentioned very often:

“Google Rendering Service does not care about pixels, so we are not painting, so if you see something that is very paint-expensive, you don’t have to worry about that. We are not using any GPUs to paint any pictures, and we don’t care about anything paint-related.

Expensive layouts are tricky, especially layout work that happens on the main thread – layout work that causes CPU time which is precious to Google.”

So what you can do is minimize the amount of the main thread work needed to render your pages. While this may not play a role for a small website, if you have millions of pages, the CPU cost adds up, and it may potentially slow the indexing process down for your website.

Martin had a fascinating thing to say about how CMS platforms might influence the rendering of your page:

“The nice thing about platforms is whenever they optimize the actual platform you get this optimization for free. You don’t have to actually do anything about that, so that’s nice. If you build your own thing, then you have to do the optimization work, and never ever is some optimization magically falling into your lap.”

But this comes at a cost. Using a CMS platform means your website has to ship some redundant code that you might never use. The platform may provide an out-of-the-box feature that you’ll never even use, but it may be impossible to get rid of the code that makes the feature possible.

When you optimize rendering, you often simply make your pages lighter. For Google, it means less CPU consumption and less resource fetching, which is excellent because these are the things Google spends very conservatively.

But it’s equally as great for regular users, primarily if they use lower-end devices with a poor connection.

“The more expensive you make it, the worse it is for us as an experience. Google Search doesn’t really care, we just need to invest in resources that we need and we do a lot of optimizations to make sure we are wasting as little time and energy as possible. But obviously, if you’re optimizing that, a nice side effect is that your users will probably also be happier because they need less battery, their old phone will still work fine with what you put out there, and they will be able to consume your web content and maybe not your competitors’ because your competitors just don’t care and actually produce something that is less convenient to use on their phones. So this is not something where you pit Google vs UX, this is kinda like the same problem or the same challenge, and we’re all facing it, including Google Search, so that’s a nice one.”

If you’re still struggling with rendering, we can help you with website performance optimization .

Still unsure of dropping us a line? Read how Rendering SEO services can help you improve your website.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
