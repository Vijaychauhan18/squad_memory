---
source: https://www.onely.com/blog/how-to-fix-page-indexed-without-content-in-google-search-console/
title: How To Fix “Page indexed without content” in GSC
scraped: 2026-03-23
published_on: 2023-01-19
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

# How To Fix “Page indexed without content” in GSC

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/how-to-fix-page-indexed-without-content-in-google-search-console/
Published: 2023-01-19
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
“Page indexed without content”- how is this possible? See our 4 tips on how to fix this status in Google Search Console

## Extracted Body
“Page indexed without content” is a Google Search Console status that means your page is indexed even though Google couldn’t find or read its content.

Do you see this status in your Page indexing (Index Coverage) report, but you’re unsure how to approach it?

You need to know that although the “Page indexed without content” issues may be relatively rare to encounter in Google Search Console, when they keep arising, it’s a sign that you should take a closer look. That’s because if there’s content on the page that should be indexed but isn’t, the page won’t perform well on Google.

Unfortunately, the information you may find about this status is often limited or conflicting. But don’t worry – I got you fully covered, so read on to learn about the possible causes and solutions.

If you see the “Page indexed without content” status in your Page indexing (Index Coverage) report , it indicates that Googlebot couldn’t find or access your content but indexed your page because of extensive internal and external linking pointing to the URL.

And if you’re wondering how a page can be indexed without content, let’s analyze how Google approaches pages in the indexing pipeline.

When Google discovers a page on your website, it goes through the robots.txt file to ensure it can visit a URL.

The general idea of using robots.txt is that it indicates what pages bots shouldn’t visit. In other words, if your URL is blocked within robots.txt, Googlebot shouldn’t crawl it and see your content.

Of course, it still may happen that the URL you blocked in robots.txt gets indexed. Ania Siano described that case in her article on the “Indexed, though blocked by robots.txt” status.

On the other hand, if your URL is crawlable and indexable (meaning you don’t block it with robots.txt or the noindex tag ):

However, an important thing to remember is that, according to John Mueller, “A page’s content doesn’t need to be indexed for a page to be indexed (…).”

That’s why one of the cases when you can see this status is when you publish a page without content by mistake or remove the content leaving a blank page for users within the indexed URL.

However, if bots have valid reasons to index a URL but, for some reason, they can’t access or process your content, such a page may also be considered “Page indexed without content.”

There are actually a few reasons why Google may think your page has no content, even if it actually contains some. Let’s dive in!

One of the reasons is that your page is published in a non-accessible format for Google, so it can’t read it.

According to Google’s official documentation, to see your textual content on Google, it needs to be published in one of the indexable file types .

Another case is when Google thinks that your indexed page has no content due to server-related issues on your side.

This is essentially an issue on your site’s serving side, it’s not something we have control over, or which we can debug from our side. Sometimes it’s an over-zealous bot-protection or a misbehaving CDN / gateway / server. source: John Mueller

Here’s when Google can’t process the content because, for some reason, your server blocks bots from seeing it.

In other words, it’s like Google doesn’t have any additional information about your page, e.g., it may not recognize either the content type or the HTTP response.

Here’s how you may see such a page when inspecting the URL in Google Search Console:

In this case, contact your developers to track down the possible cause of the issue.

Another reason why Google might assign your page to the “Page indexed without content” status is when you show different content to users and bots. With some exceptions, this is considered cloaking and goes against Google’s guidelines.

Why is cloaking problematic for Google? In this case, Google can see the content on your page, but it finds out that there are actually two versions of it – one for users and another for bots.

As a result, Google gets suspicious, as it considers such behavior a form of spam “(…) with the intent to manipulate search rankings and mislead users” and may not want to index a given page’s content.

According to John Mueller, cloaking can poorly impact user experience as users see different content than they were promised on SERPs:

If we recommend a page to people for a specific query and they go there, and they can’t find that content, then they’re frustrated, and they think we did a bad job, and that’s something where our cloaking problem comes from.

On the other side, some webmasters may use cloaking to show keyword-rich content only to bots in hopes of better rankings. However, fooling Google may have severe consequences.

In both these cases, such an approach may result in a manual penalty.

We covered that topic before on our blog. Read Ania Siano’s article about manual actions and how to deal with them.

To fully understand the context of your page and serve it to users on SERPs, bots need to render your content.

However, it may not be possible if you’re blocking some important files in your robots.txt.

And, although official Google documentation on the Page indexing (Index Coverage) report says that “Page indexed without content” “(…) is not a case of robots.txt blocking,” I feel it needs some clarification.

The statement above is true when it refers to blocking URLs. But blocking, e.g., JavaScript or CSS resources in your robots.txt may actually contribute to the “Page indexed without content” issues.

In other words, if the URL is crawlable and indexable, but you blocked important files in robots.txt:

It means that Googlebot won’t fully render your page as you didn’t give it access to your essential resources.

Moreover, remember that even if you’re not blocking any crucial files in your robots.txt, your pages may still struggle with rendering issues, making it impossible for Google to see your content.

It’s especially the case when you don’t optimize the way you serve your JavaScript-based content to search engines.

Why? Because, sometimes, Googlebot may not be able to handle the cost of processing your JavaScript content on its own and see only a blank page instead of your valuable content.

And when you get rendering messed up on your website, it may bring severe consequences for your organic visibility as Google can’t fully understand what your page is about.

You can find the “Page indexed without content” status at the bottom of the Page indexing (Index Coverage) report in Google Search Console in the ‘Improve page appearance’ section.

Enter the status page to dive into the list of the “Page indexed without content” URLs. It will also show you the chart on how the number of affected pages has changed over time.

Another way to navigate this issue is to use the URL Inspection tool .

Here you can enter a specific URL on your domain and examine its current status. For “Page indexed without content,” you should see the following information: ‘URL is on Google’ and “Page indexed without content.”

Also, by clicking on ‘View crawled page,’ you may check how Googlebot sees the affected page. However, in the case of “Page indexed without content,” additional information like the page HTML, screenshot, or more info on page resources may not be available.

The initial analysis of the “Page indexed without content” URLs in Google Search Console may help you decide on the next steps.

Looking at the lists of the affected pages for our clients, the “Page indexed without content” issues were primarily empty pages.

If it’s also the case for you, it may be a good moment to rethink your indexing strategy and consider whether these pages should still be indexed.
