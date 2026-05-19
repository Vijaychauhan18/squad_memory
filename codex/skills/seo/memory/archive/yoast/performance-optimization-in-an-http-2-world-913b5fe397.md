---
source: https://yoast.com/performance-optimization-http2/
title: Performance optimization in an HTTP/2 world
scraped: 2026-03-23
published_on: 2016-12-22
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

# Performance optimization in an HTTP/2 world

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/performance-optimization-http2/
Published: 2016-12-22
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
HTTP/2 will make the web faster and you can already get started with it. You'll find that some classic optimizations are no longer needed.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

A revolution is currently going on in the underpinnings of the web. HTTP, the protocol your browser uses to connect to your site, has a new version: HTTP/2 . This is not something that should concern the average user, but for web developers, it changes how we do performance optimization entirely. In this short article, I want to explain what performance optimization best practices you can do away with, and why.

The most important thing you should know about the new HTTP/2 is that it no longer requires a new request for each file. This is the modification that makes our performance optimization guidelines change so drastically. In the HTTP1 / HTTP/1.1 world, it’d be faster to combine JS & CSS files and even images, so there would be fewer requests between browser and server. In the HTTP/2 world, this type of optimization is no longer needed and can even become counterproductive.

The answer is, fairly simply: yes . If your site is running on HTTPS , then all major current browsers support HTTP/2. You or your hosting company might have to change your server configuration to make sure it supports HTTP/2, but that’s it. Some older browsers might not be able to use it, but your site would still work for them.

Yes, you should use HTTP/2! It’s a lot faster than old fashioned HTTP1, and when you set it up well, most of your visitors will benefit hugely.

Even with HTTP/2 you still need a CDN . A CDN delivers content a lot faster than your average server ever will, so your site would still benefit enormously from having one. Every proper CDN will already support HTTP/2.

The following performance best practices are no longer needed with HTTP/2 and should be done away with:

Unfortunately, Google’s PageSpeed tool and many other web performance testing tools are rather slow in their adoption of HTTP/2. They should be changing their guidelines. If a simple HTTP/2 test shows you that a site is capable of using HTTP/2, quite a few of the site speed suggestions are moot. Their documentation speaks of “networking round trips” that simply, in an HTTP/2 environment, don’t happen.

There are people at Google that understand this, of course. This presentation by Ilya Gregorik in 2015 already shows all of that.

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

Quite interesting. With what was said above, it more like saying that caching plugins are no more needed.

With HTTP/2 you can use Brotli compression as well! If Brotli isn’t available GZIP will automatically be used as a fallback. Test for Brotli compression support online at https://tools.keycdn.com/brotli-test

Unfortunately, it is not always easy to “change your server configuration to make sure it supports HTTP/2”. Windows Server 2012 (R2) for example, it is widely used and will never support HTTP/2.

Therefore, I think you should develop with HTTP 1.1 and HTTP 2 in mind.

Maybe plugin developers can catch the protocol used, to perform different actions based on that. For example, concatenating CSS and JS files in Autoptimize only if HTTP 1.1 is used.

I trust Google will heed your commentary. If it doesn’t, you should feel insulted.

Adding HTTP/2 is simple if you use Cloudflare. You can learn more about it at https://www.cloudflare.com/website-optimization/http2/

Sir, I didnt understand what is duplicate content and how to recognise this thing. any article belong to this. by the way yoast seo is awesome.

I wish I saw this a week ago. I just spent a lot of time optimizing my sites and trying to figure out which plugins successfully minify etc. I checked and discovered that, with Siteground and an SSL, my sites already are on http/2. So I turned off the minifier, and my sites loaded faster. :D

Well this was timely. I’m looking to do a full on performance upgrade to a couple of clients sites. We are doing a complete new web design and migrating over to https. The information brought forth in this article should definitely help the transition go smoother. Thanks a bunch!

Inlining CSS and JS “Inlining small bits of CSS and JS is a practice that was aggressively pushed by Google.” — Should it be punished rather than pushed?

It might be like PHP7 where those of us with cPanel had to wait several months before it was compatible. It was well worth the wait and since HTTP/2 is new and unknown to the average web site owner it will probably be well into 2017 before we can jump on it. Fingers crossed it’ll be sooner, but technology on servers (even dedicated ones) is much slower than in our minds.

Not such an easy thing for Liquid Web. I inquired with their tech support (which always goes above and beyond) about HTTP/2 and here’s what they had to say about it working with cPanel:

“HTTP2 requires the use of Application-Layer Protocol Negotiation (ALPN) which is a form of TLS and is not supported in OpenSSL version 1.0.1. It is supported in 1.0.2, but that is not included in the managed software on your server. So, you would need to maybe use an unmanaged Fedora server and install OpenSSL v 1.0.2 first, then try to get it working. This is beyond our level of support. The other is wait for Centos 8 or Unbuntu 16 to come out and hope that OpenSSL is updated in those version. “

Hello my friends. Need to check with the server if they have support for this.

You can also check here on this site ==> https://tools.keycdn.com/http2-test

To see if it already supports the second version of the HTTP / 2 protocol.

What isn’t particularly clear to me from this article is the how: how do we enable HTTP/2? Is this something we’re requesting at the host end? What action is required on our end? A small addition of a ‘Getting Started’ would enhance this article quite a bit, imho.

Totally agree with this. Really interesting to know about HTTP/2 but I’m left wondering – do I even have a choice to use HTTP/2 or is it entirely up to the host to implement???

Your host has to have implemented it before you can take advantage if it, Cathy. In addition, your site must be using https (an SSL certificate) for HTTP/2 to take effect.

I have plans to change a few sites to HTTP/2 in the next few months and wondering if you recommend any hosting and CDNs?

For CDN I recommend Cloudflare. It is a great CDN and it’s free.

It certainly mitigates any negative effects using SSL might have on your performance, as HTTP/2 more than compensates this. It also feels a bit like a reward after the punishing Google is doing to regular content sites by enforcing to go SSL with their browser.

if your hosts support HTTP/2 and your site is configured for SSL you should be good to go.

What good news. So that means a lot will change and we will have less work with performance practice.

Bad forces us to use Https on all websites and still check if the server supports to enable the correct http/2?

Does that means you should force use https or can you leave both (https and http) active?

Hi Kristof, I found your question interesting and did a bit of research… I don’t know if this will help you make your decision on whether to keep both HTTP & HTTPS or require HTTPS only but it is interesting to see no browser currently supports HTTP/2 without TLS even though HTTP/2 supports non-encrypted (HTTP) connections. Read more here: https://http2.github.io/faq/#does-http2-require-encryption

We care about the protection of your data. Read our privacy policy.
