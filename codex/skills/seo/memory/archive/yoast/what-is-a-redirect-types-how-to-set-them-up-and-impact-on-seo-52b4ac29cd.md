---
source: https://yoast.com/what-is-a-redirect/
title: What is a redirect? Types, how to set them up, and impact on SEO
scraped: 2026-03-23
published_on: 2025-12-19
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

# What is a redirect? Types, how to set them up, and impact on SEO

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/what-is-a-redirect/
Published: 2025-12-19
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Have you ever wondered: "What is a redirect?" Well, redirects make a browser go from one URL to another URL. Read on to find out more!

## Extracted Body
Ever clicked a link and landed on a “Page Not Found” error? Redirects prevent that. They automatically send visitors and search engines to the right page. Redirects are crucial for both SEO and user experience. For SEO, they preserve link equity and maintain your rankings. Additionally, it enhances the user experience, as no one likes dead ends. Here, you’ll find the easiest way to do a redirect in WordPress.

Key takeaways A redirect automatically sends users and search engines from one URL to another, preventing errors like ‘Page Not Found.’ Redirects are crucial for SEO and user experience, preserving link equity and maintaining rankings. Different types of redirects exist: 301 for permanent moves and 302 for temporary ones. Avoid client-side redirects, such as meta refresh or JavaScript, as they can harm SEO. Use Yoast SEO Premium to easily set up and manage redirects on your site. What is a redirect? A redirect is a method that automatically sends users and search engines from one URL to another. For example, if you delete a page, a redirect can send visitors to a new or related page instead of a 404 error.

Redirects keep your website running smoothly. Without them, visitors hit dead ends, links break, and search engines get lost. They’re not just technical fixes, because they protect your traffic, preserve rankings, and make sure users land where they’re supposed to. Whether you’re moving a page, fixing a typo in a URL, or removing old content , redirects make sure that nothing gets left behind.

There are various types of redirects , each serving a distinct purpose. Some are permanent, some are temporary, and some you should avoid altogether. Here’s what you need to know to pick the right one.

Not all redirects work the same way. A 301 redirect tells search engines a page has moved permanently, while a 302 redirect signals a temporary change. Client-side redirects, like meta refresh or JavaScript, exist because they’re sometimes the only option on restrictive hosting platforms or static sites, but they often create more problems than they solve. Below, we break down each type, explain when to use it, and discuss its implications for your SEO.

A 301 redirect tells browsers and search engines that a page has moved permanently. Use it when:

SEO impact: 301 redirects pass virtually all link equity to the new URL. But be sure to never redirect to irrelevant pages, as this can confuse users and hurt SEO. For example, redirecting a deleted blog post about “best running shoes” to your homepage, instead of a similar post about running gear. This wastes link equity and frustrates visitors.

A 302 redirect tells browsers and search engines that a move is temporary. Use it for:

SEO impact: 302 redirects typically don’t pass ranking power like 301s. Google treats them as temporary, so they may not preserve SEO value. For permanent moves, always use a 301 to ensure link equity transfers smoothly.

Example 1: Temporary out-of-stock product (302): An online store redirects example.com/red-sneakers to example.com/blue-sneakers while red sneakers are restocked. A 302 redirect keeps the original URL alive for future use.

Example 2: A permanent domain change (301): A company moves from old-site.com to new-site.com. A 301 redirect makes sure visitors and search engines land on the new domain while preserving SEO rankings.

These redirects follow HTTP rules more strictly than 301 or 302:

For most sites : Stick with 301 (permanent) or 302 (temporary) . These are for specific technical cases only.

Client-side redirects, such as meta refresh or JavaScript, execute within the browser instead of on the server. They’re rarely the right choice, but here’s why you might encounter them:

Stick with server-side redirects (301/302) whenever possible. If you must use a client-side redirect, test it thoroughly and monitor for SEO issues.

Redirects do more than just send users to a new URL. They shape how search engines crawl, index, and rank your site. A well-planned redirect preserves traffic and rankings. A sloppy one can break both. Here’s what you need to know about their impact.

301 redirects pass most of the link equity from the old URL to the new one. This helps maintain your rankings. 302 redirects may not pass ranking power, especially if used long-term.

Too many redirects can slow down how quickly search engines crawl your site. Avoid redirect chains ( A→B→C ) to save crawl budget .

Redirects prevent 404 errors and keep users engaged. A smooth redirect experience can reduce bounce rates.

Redirects seem simple, but small errors can cause big problems. Here are the most common mistakes and how to avoid them.

A redirect chain happens when one URL redirects to another, which redirects to another, and so on. For example:

A redirect loop sends users and search engines in circles. For example:

A 302 redirect is meant for temporary changes, but many sites use it for permanent moves. For example:

Redirecting a page to unrelated content confuses users and search engines. For example:

After setting up a redirect, many sites forget to update internal links . For example:

Assuming redirects work without testing can lead to surprises. For example:

When a page is deleted, some sites redirect all traffic to the homepage. For example:

After setting up redirects, many sites forget to update their XML sitemaps. For example:

Some sites use redirects to hide thin or duplicate content. For example, redirecting multiple low-quality pages to a single high-quality page to “clean up” the site.

Setting up redirects isn’t complicated, but the steps vary depending on your platform. Below, you’ll find straightforward instructions for the most common setups, whether you’re using WordPress, Apache, Nginx, or Cloudflare.

Pick the method that matches your setup and follow along. If you’re unsure which to use, start with the platform you’re most comfortable with.

Yoast SEO Premium makes it easy to set up redirects, especially when you delete or move content. Here’s how to do it:

Yoast SEO can create redirects automatically when you delete a post or page. Here’s how:

This feature saves time and ensures visitors land on the right page. No manual setup required.

No code, no hassle. Just smarter redirects and many other invaluable tools.

Apache uses the .htaccess file to manage redirects. If your site runs on Apache, this is the simplest way to set them up. Add the rules below to your .htaccess file, ensuring it is located in the root directory of your site.

Nginx handles redirects in the server configuration file. If your site runs on Nginx, add these rules to your server block and then reload the service to apply the changes.

Cloudflare allows you to set up redirects without modifying server files. Create a page rule to forward traffic from one URL to another, without requiring any coding. Simply enter the old and new URLs, select the redirect type, and click Save.

Redirects don’t always work as expected. A typo, a cached page, or a conflicting rule can break them, or worse, create loops that frustrate users and search engines. Below are the most common issues and how to fix them.

If something’s not working, start with the basics: check for errors, test thoroughly, and clear your cache. The solutions are usually simpler than they seem.

A proxy redirect keeps the URL the same in the browser but fetches content from a different location. Used for load balancing or A/B testing. Avoid for SEO, as search engines may not follow them.

Redirects are a simple but powerful tool. A redirect automatically sends users and search engines from one URL to another. As a result, they keep your site running smoothly and preserve SEO value and ranking power. Remember:

Need help? Yoast SEO Premium’s redirect manager is the easiest way to do a redirect in WordPress.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

We care about the protection of your data. Read our privacy policy.
