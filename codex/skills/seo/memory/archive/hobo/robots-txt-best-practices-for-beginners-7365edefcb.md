---
source: https://www.hobo-web.co.uk/robots-txt-tutorial-for-beginners/
title: Robots.txt Best Practices For Beginners
scraped: 2026-03-23
published_on: 2008-01-10
tags: live_feed, phase1_ingest, hobo, publication, quality, leak-systems, archive_backfill, historical_source
topic: quality_systems
intent: research, monitoring, source_selection, leak_systems
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Archive backfill - Hobo Web
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Robots.txt Best Practices For Beginners

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/robots-txt-tutorial-for-beginners/
Published: 2008-01-10
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
A robots.txt file is a file on your webserver used to control bots like Googlebot, Google's web crawler. You can use it to block Google and Bing from crawling parts of your site.

## Extracted Body
After more than two decades immersed in the world of SEO and website development , I know that files like robots.txt can seem intimidating. They feel like the domain of developers, full of strange syntax and the potential to break your entire website with a single misplaced character.

Back in 2008, I published an interview on this blog with my friend (then well-known SEO) Sebastian’s Pamphlets, breaking down the basics of robots.txt. It was a fun piece that even received a comment from a then-lesser-known Googler named John Mueller, who said, “That was a fun and interesting interview! Thanks for putting that together, guys.”

A lot has changed since 2008, and Sebastian’s Pamphlets is no longer with us, but the core principles of robots.txt we discussed have remained remarkably stable.

My mission with this updated replacement guide is to revisit those fundamentals, incorporating some of Sebastian’s timeless advice with the strategic lessons I’ve learned from over 20 years of hands-on experience. We’re not just going to cover the “what” – the syntax and the rules. We’re going to focus on the far more important “why.” Why does this simple text file matter so much for your site’s health? How does it relate to your business goals?

Think of your robots.txt file as the very first conversation you have with search engine crawlers like Googlebot. It’s the fundamental dialogue that sets the rules of engagement. It’s how you ensure your digital storefront has clear signage and open doors for your most important customer: Google. Let’s make sure you’re giving them the right instructions.

At its core, a robots.txt file is a plain text file that lives at the root of your domain. You can see ours by typing https://www.hobo-web.co.uk/robots.txt into your browser. Its primary, officially stated purpose is to manage crawler traffic to your site, typically to prevent your server from being overwhelmed with requests. 1

However, the most important lesson I can teach you is about what robots.txt is NOT . Understanding this will save you from some of the most common and costly SEO mistakes. As Sebastian wisely pointed out all those years ago, “all robots.txt directives are crawler directives that don’t affect indexing.”

This is a critical distinction. The Disallow directive in a robots.txt file is a polite request, not an enforceable command. While reputable crawlers like Googlebot will honour it, many others will not. 1

More importantly, as Google’s own documentation warns, if a page you’ve disallowed is linked to from another website, Google can still find and index that URL. 1 It won’t crawl the page, so the search result will appear without a description, but the URL itself can still show up. If you truly want to keep a page out of Google’s search results, the correct method is to allow crawling and use a

noindex meta tag on the page itself. 1 For securing sensitive information, you must always use proper server-side security, like password protection.

This leads to a crucial point that many beginners miss: your robots.txt file is a public document. Anyone—including your competitors or malicious actors—can view it to understand the structure of your website. 2 If you include a line like

Disallow: /admin-portal/, you are not hiding that directory; you are putting up a public signpost that points directly to it. Never use robots.txt as a security measure.

So, if robots.txt isn’t for blocking indexing, what is its main strategic purpose for SEO? The answer is crawl budget optimisation .

Google allocates a finite amount of resources—time and computing power—to exploring any given website. We call this the “ crawl budget “. For small websites, this is rarely an issue. But for larger sites, especially e-commerce stores with thousands of pages and complex filtering options, it’s a critical factor.

A poorly configured (or non-existent) robots.txt file can lead to catastrophic “Crawl Budget Wastage” on larger sites. This happens when Googlebot spends the majority of its time crawling thousands of low-value, duplicate, or unimportant URLs. Think of pages generated by faceted navigation (sorting by price, colour, size), internal search results, or endless tag and archive pages.

When Googlebot is busy with this digital clutter, it may never get around to crawling your most important, revenue-generating pages. Those pages then languish, uncrawled and unranked.

Your robots.txt file is your primary tool for actively managing this budget. By using it correctly, you can guide Googlebot away from the unimportant sections and direct its full attention to the content that truly matters to your business.

If you have a small site (fewer than hundreds of thousands of sites), this is much less of an issue.

A robots.txt file is made up of one or more “groups.” Each group applies to a specific crawler (a User-agent) and contains a set of rules (Allow or Disallow) that tell that crawler what it can and cannot access.

Here is a simple, scannable breakdown of the most common directives you will use.

Ready to create your own? Some of the best advice on this is timeless.

Over my career, I’ve seen a few simple robots.txt errors cause devastating damage to a site’s visibility. Here are the most common ones to watch out for.

Congratulations. By understanding the robots.txt file, you’ve mastered a foundational piece of technical SEO. You’re no longer just creating content; you’re actively managing the conversation between your website and the search engines that determine its success.

The perfect next step on your journey is to download my free Beginner SEO guide . It’s a comprehensive guide that builds on these technical fundamentals, covering everything from content strategy and link earning to keyword research, all grounded in a modern, “people-first” approach that works today.

robots.txt tells Google “don’t even look at this page.” A noindex tag tells Google “you can look at this page, but don’t show it in search results.” If you block a page in robots.txt, Google might still index its URL if it finds links to it from other sites. If you want to guarantee a page is removed from the index, you must allow Google to crawl it so it can see the noindex tag.

Simply add a new line anywhere in the file (though typically at the top or bottom for clarity) with the following format: Sitemap: https://www.yourdomain.com/sitemap.xml. Be sure to replace the example URL with the actual, full URL of your sitemap.

Yes, absolutely. A single line, Disallow: /, will instruct all compliant search engine crawlers not to crawl any pages on your site. This is one of the most common and devastating technical SEO mistakes, often happening when a development site’s settings are accidentally moved to a live site.

Mastering the fundamentals is the key to building a resilient, long-term SEO strategy that stands the test of time. The robots.txt file is one of those fundamentals. By taking control of this simple file, you are taking a professional approach to managing your site’s health and aligning your goals with Google’s guidelines . You are telling the world’s most powerful search engine exactly how you want it to interact with your property, ensuring its resources are focused on the content you’ve worked so hard to create.

My friend Sebastian, a technically-minded peer who helped shape the original 2008 interview, had a knack for cutting through the noise. His advice then is just as critical now for anyone wanting to keep a page out of Google: “ Robots.txt blocks with Disallow: don’t prevent from indexing. Don’t block crawling of pages that you want to have deindexed. “

Author Bio: Shaun Anderson is the founder of Hobo Web and has been a professional website designer, developer and SEO since 2001. With over two decades of experience, his work focuses on ethical, ‘white hat’ strategies that align with Google’s guidelines to deliver sustainable results. You can read more about his journey on his full bio page .

Disclosure : Hobo Web uses generative AI when specifically writing about our own experiences, ideas, stories, concepts, tools, tool documentation or research. Our tools of choice for this process is Google Gemini Pro 2.5 Deep Research. This assistance helps ensure our customers have clarity on everything we are involved with and what we stand for. It also ensures that when customers use Google Search to ask a question about Hobo Web software, the answer is always available to them, and it is as accurate and up-to-date as possible. All content was verified as correct by Shaun Anderson. See our AI policy .
