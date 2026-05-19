---
source: https://yoast.com/moving-your-website-to-https-ssl-tips-tricks/
title: Moving your website to HTTPS / SSL: tips and tricks
scraped: 2026-03-23
published_on: 2017-07-12
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

# Moving your website to HTTPS / SSL: tips and tricks

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/moving-your-website-to-https-ssl-tips-tricks/
Published: 2017-07-12
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Moving your website to https and SSL? Learn from our experiences with this process and read our tricks and tips!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

In 2014, we decided to switch over to the (now) commonly-used HTTPS protocol to encrypt sensitive data that’s being sent across our website. This post describes some useful tips based on our own experiences that might come in handy if you’re considering switching.

Moving your WordPress site to support HTTPS connections with SSL certificates became a lot easier as of WordPress 5.7. In that release, the WordPress team added a new feature to Site Health that checks if a site runs on a hosting package that supports HTTPS. If it does, the feature offers a one-click option to move your site to HTTPS . It even updates the links in the database for you and prevents mixed content warnings from happening. So, activate that SSL certificate for your site and get to it!

Back in 2014 HTTPS became a hot-topic after the Heartbleed bug became public. This bug allowed people with ill intent to listen in on traffic being transferred over SSL/TLS. It also gave them the ability to hijack and/or read the data. Luckily, this bug got patched quickly after its discovery. This incident was a wake-up call that properly encrypting user information over the internet is a necessity and shouldn’t be an optional thing.

To emphasize the importance of encrypting sensitive data, Google Chrome (since January 2017) displays a clear warning next to the address bar whenever you visit a website that doesn’t encrypt – potential – sensitive data, such as forms.

Because it’s important that your data is safe, we took steps in 2014 to ensure that we have SSL-certificates across our own websites. If you decide to switch (you really should!), there are a few things that you need to take into account to ensure your website fully works as intended once you’re done.

Google also published a handy guide on how to move to HTTPS without massively impacting your ranking, which can be found here .

Like stated in the previous section, moving from HTTP to HTTPS can influence your rankings slightly if you don’t plan accordingly. However, after you switch over to HTTPS, your rankings will actually improve over time. Google announced in 2014 that having an SSL certificate will be considered a positive ranking factor, so it’s worth the investment.

To make sure Googlebot can re-index your website more rapidly after the move, make sure you migrate to https:// during low-traffic hours. This way Googlebot can use more of your server’s resources. Just take into account that a medium-sized website might take a while to regain rankings. Have a sitemap? Then Googlebot might be able to recalculate and re-index your website even faster.

Generally speaking, hosting providers have a service to allow you to enable HTTPS/order a certificate. There are a few types of certificates you can choose from, which differ in a few ways. Every variant also has their own price tag, so before purchasing one, make sure that you go with a certificate that fits your needs and budget!

If you’re a bit strapped for cash and tech-savvy, go take a look at Let’s Encrypt to acquire a free(!) certificate.

If you run and manage your own web server, there are a few things that you’ll have to enable in your server configuration before being able to use SSL certificates. This tutorial explains what steps to take to get a certificate running on your server.

Having to check the validity of an SSL certificate can result in a small hit in loading speed. To overcome this, you can make use of OCSP stapling . OCSP stapling is a feature that enables the server to download a copy of the certificate vendor’s response when checking the SSL certificate. This means that once a browser connects to the server, it checks the validity of the certificate based on the copy on the server instead of having to query the certificate vendor itself, resulting in a significant performance improvement.

Before enabling OCSP stapling on your Apache server, please check that you’re running version 2.3.3+ of Apache by running the command apache2 -v (or httpd -v ) on your server. Lower versions of Apache do not support this feature .

If you went through the process of setting up HTTPS on your server as described in the ‘Setting up HTTPS & SSL on your server’ section, then you should have come into contact with a VirtualHost configuration specifically made for usage with HTTPS/SSL.

Nginx also supports OCSP stapling. Before editing the server configuration, please check that you’re running version 1.3.7+ of Nginx by running the command nginx -v on your server. Lower versions of Nginx do not support this feature .

If you went through the process of setting up HTTPS on your server as described in the ‘Setting up HTTPS & SSL on your server’ section, then you should have come into contact with an Nginx configuration specifically made for usage with HTTPS/SSL.

In that file, add the following lines in the server {} section:

The last line references a file that contains a list of trusted CA certificates. This file is used to verify client certificates when using OCSP.

After adding these lines to the file, check that the configuration is still valid by running service nginx configtest . If so, reload Nginx by running service nginx reload .

The Strict Transport Security Header (HSTS) is another handy feature that basically enforces browsers to use the HTTPS request instead of the HTTP equivalent. Enabling this feature is relatively painless.

If you’re running Apache, first enable the Apache Headers module by running a2enmod headers . After this, it’s only a matter of adding the following line to your VirtualHost configuration (in the <VirtualHost></VirtualHost> section) that you set up earlier for HTTPS:

Nginx requires you to add the following line in the server{} section of your server configuration file:

To see if your SSL certificate is working properly, head over to SSL Labs , fill in your domain name and see what kind of score you get.

To ensure requests are properly redirected to the HTTPS URL, you need to add an extra line to you configuration. This way, traffic that tries to visit your website over HTTP, will automatically be redirected to HTTPS.

In your default VirtualHost configuration (so the one that’s used for HTTP requests), add the following to ensure URLs get properly redirected:

As with the other changes we made before, don’t forget to reload Apache!

In Nginx, change the default configuration file that was used for HTTP requests and alter it as such:

“Should I switch over to HTTPS?” Short answer: Yes. Using HTTPS ensures that private (user) information is being sent across the web in a more secure manner. Especially if you’re dealing with monetary transactions, HTTPS is a must.

What type of certificate you end up going with, depends on your specific use case and budget. Make sure to properly research your options beforehand.

Jimmy Comack is Developer Relations Advocate at Yoast by day, gamer and film addict by night. He's a big proponent of open source software and tries to contribute to the OS community when possible.

Thanks for sharing amazing info because today am I transfer on https

Hmmm looks very hard to implement the ssl certificate but I think the hosting providers can do that for the site owners without any fee. Nice tips by the way.

hi after i install ssl my sitemap is have problem it dont have url in it just text https://www.cesardl.info/sitemap_index.xml

Good information. I am using cloudfare free CDN and really-simple-ssl wordpress plug in. All appears to be fine. But yoast is not generating site map with Https. In my google webmaster site map urls start from http only.

Mike Clegg pointed out here https://yoast.com/moving-your-website-to-https-ssl-tips-tricks/#comment-529224 that he needed to deactivate and reactivate the plugin to get the sitemaps to properly regenerate.

I allways thought that HTTPS was an issue of webshops. I didn’t realize that it’s a ranking signal for all kind of websites. I will take a look this week how to set it up.

Mid of last year I’ve done a switch from HTTP to HTTPS for my Blog “Happy Carb”. Overall it was running successful, I didn’t noticed any negative Ranking Drop.

But two things were pretty annoying: Google Search Console needs to be setup again for the HTTPS-Version. Please note: I didn’t keep the HTTP-Version, every link was redirected to HTTPS. I was wondering why I couldn’t just tell the Google Search Console my change Domain Protocoll correctly.

Facebook Likes for my pages where resetted to zero since the changed Protocoll results in a different URL. In my opionion Facebook should change this behavior, because of the nulled likes lot’s of positive Social Signals get lost. I didn’t find a way to change this behavior and for sure I don’t want to allow Facebook to access the HTTP versions of my pages…

Good thing to notice here: I used the following MySQL Database Search & Replace util for changing all internal links:

https://interconnectit.com/products/search-and-replace-for-wordpress-databases/

Also my advice: run a 404 and 301 checker tool on all pages after you’ve done the switch.

In regards to the Facebook likes not properly being fixed, there is a solution, but it requires altering code: https://developers.facebook.com/docs/plugins/faqs#faq_1149655968420144

thanks for your note about the Facebook Likes recovery solution. Within my HTTP => HTTPS change last year, I checked this notes from Facebook. Since I’m using 301 redirects to HTTPs versions and Yoast SEO for WordPress for generating the Open Graph metas, it still wasn’t easy to create an update the way Facebook wanted.

The og:url should keep the old URL (just the HTTP version in my case) and, the important thing, the corresponding page must being accessible by the Facebook crawler for the HTTP version without the redirect to HTTPS.

So two things to solve. Yoast SEO for WordPress unfortunately doesn’t provide a mechamism to overwrite the og:url meta generation (right?). Setting up the Facebook crawler identification could be done within the .htaccess file.

What I’m wondering about: why doesn’t Facebook just define an alternative og:url (“og:url:alternative”) that keeps the old URL? That would be the easiest way, Crawler access could grap this information from the given page and not cryptic handled ones. But ok, this is just a wish, maybe somebody from the Facebook Development Department ist reading this posts ;)
