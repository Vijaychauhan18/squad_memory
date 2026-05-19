---
source: https://yoast.com/how-to-remove-www-from-your-url/
title: How to remove www from your URL
scraped: 2026-03-23
published_on: 2017-02-03
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

# How to remove www from your URL

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/how-to-remove-www-from-your-url/
Published: 2017-02-03
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Getting rid of the www in your URL, or instead adding it, is quite easy, this is a simple explanation of how to do it.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

At Yoast, we sometimes receive the question how to remove www from your website’s URL – or add it. In this post, I’ll show you how you can enforce either a www or non-www URL by tweaking your .htaccess file (or nginx.conf if you’re running on an Nginx server).

You might be wondering if using one or the other will have an impact on your SEO. The answer is: no. It’s really just a matter of preference/esthetics. Just make sure you properly add the www and non-www domains in Google Search Console, as described here , to ensure Google can properly index your website.

If you prefer to market your website without the www prefix, you can add the following lines to your .htaccess file (Apache only):

[code]RewriteEngine On RewriteCond %{HTTP_HOST} ^www.example.com$ [NC] RewriteRule ^(.*)$ http://example.com/$1 [R=301,L][/code]

Edit: As Thomas pointed out in the comments, it is not necessary to restart Apache after modifying the .htaccess file.

Note that Apache’s mod_rewrite module needs to be enabled. Otherwise, the above snippet won’t work.

Now, in Nginx this snippet is a bit different, but yields the exact same result when placed in the proper configuration file (which depends on your setup):

[code]server { server_name www.example.com; return 301 http://example.com$request_uri; }[/code]

To do the opposite of the previous section, add the following code to your .htaccess file:

[code]RewriteEngine On RewriteCond %{HTTP_HOST} ^example.com$ RewriteRule (.*) http://www.example.com$1 [R=301] [/code]

[code]server { server_name example.com; return 301 http://www.example.com$request_uri; }[/code]

As some of you pointed out in the comments (thank you for that!), there are some security concerns when you decide to use a non-www type URL.

If you run a variety of different services on subdomains, you run the risk of sharing cookies between your main, non-www homepage and said service. This could potentially be bad if certain sensitive data is being stored in cookies that you don’t want to be shared with third-parties.

There are a few other concerns with cookies and non-www style URLs, which you can read more about here .

Jimmy Comack is Developer Relations Advocate at Yoast by day, gamer and film addict by night. He's a big proponent of open source software and tries to contribute to the OS community when possible.

Why should you add both the www and non-www domains (as well as http/https in Google Search Console? If you use the .htaccess redirect to redirect all traffic to let’s say https://www.mydomain.nl then that’s all that Google will and need to visit. Or not?

By adding both to Google Search Console, you are able to tell Google what domain has your preference. If you decide you want the www version to be the ‘main’ domain name, Google will attempt to only list that version of your URL in the search results.

By -not- adding the non-www version to GSC, you might run into issues where Google decides that the non-www version should be indexed because there are links pointing to the non-www version. This will then lead to search results where you’ll see a mixture of http://www.example.com and example.com.

Adding both http and https to GSC should be done for an entirely different reason. By adding both version, you ensure that you can monitor all traffic coming to your website, no matter if visitors initially visited the http version instead of the https version. Obviously having a redirect in place in a necessity for (preferably) pointing visitors to https.

Thank you very much. All the other links are working fine but when tested in google structured data testing tool my website text logo link is still pointed to the none www version. I preferred all my link to be in https://www.domain.com

We are sorry to hear this happened to your site. The logo URL may be listed incorrectly in a setting (theme or plugin) or may not have updated to the correct URL. Please review this knowledge base article: How can I get support?

We need to make sure that we are doing proper 301 redirect while redirecting the domain from www to non www or vice versa.

Hi Jimmy! Very interesting the article. I think you are a very good teacher. Interesting and simple article. Sorry my english …I must to improve. All the best from Spain!!

When you’re modifying .htaccess files you don’t need to restart apache to see the change. You only have to do that if you edit the apache configuration file for the virtual host. Might want to correct that in the post.

Also, I agree with the other commenters that in my experience it is preferable to use www for the reasons stated in that Johansen post even if there is no SEO reason to do so.

Hi Thomas! Thank you for pointing this out. I edited the article accordingly.

Johansen published an article recently about it that I found illuminating.

It appears there is no problem from a SEO perspective, but it appears there is a possible security one, in case you use subdomains.

Thank you for this. I added a small section to the post to highlight these concerns.

Not sure it is a good idea to set your website to non-www. So far, I have seen little benefit, and some problems because of it.

It’s not just “a matter of preference/esthetics”. Cookies on the “non-www” Domains will appear on all subdomains you might have.

We care about the protection of your data. Read our privacy policy.
