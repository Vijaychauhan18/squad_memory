---
source: https://www.oncrawl.com/data-driven-seo/seo-in-orbit-log-analysis-results/
title: [Webinar Digest] SEO in Orbit: A results-focused approach to log file analysis - Oncrawl
scraped: 2026-03-23
published_on: 2019-10-02
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

# [Webinar Digest] SEO in Orbit: A results-focused approach to log file analysis - Oncrawl

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/data-driven-seo/seo-in-orbit-log-analysis-results/
Published: 2019-10-02
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
The webinar "A results-focused approach to log file analysis" with Ian Lurie is a part of the SEO in Orbit series, and aired on May 7th, 2019.

## Extracted Body
The webinar A results-focused approach to log file analysis is a part of the SEO in Orbit series, and aired on May 7th, 2019. For this episode, we discussed some of the applications of log file analysis that can be applied directly to your SEO strategy for measurable results. Ian Lurie and Oncrawl’s Alice Roussel develop use cases of log file analysis applied to SEO.

SEO in Orbit is the first webinar series sending SEO into space. Throughout the series, we discussed the present and the future of technical SEO with some of the finest SEO specialists and sent their top tips into space on June 27th, 2019.

Ian Lurie is a digital marketing consultant with 25 years of experience. Earlier in his career, he founded Portent, a Clearlink Digital Agency. Portent provides paid and organic search and social media, content, and analytics services to B2B and B2C brands including Patagonia, Princess, Linode, and Tumi.

Ian’s professional specialties and favorite topics are marketing strategy, search, history, and all things nerdy. He spends far too much time poring over Amazon search patents, Google rankings and natural language processing theory. His random educational background includes a B.A. in History from UC San Diego and a degree in Law from UCLA. Ian recently wrote about log file analysis on the Portent blog. You can find Ian on Twitter at @ianlurie

This episode was hosted by Alice Roussel, SEO Operations Manager at Oncrawl. Alice puts her years of experience as a Technical SEO Manager on the agency side to good use; she provides daily support and hands-on training for clients so they can boost their ability to find actionable takeaways in crawl data. Passionate about data analysis and how it can be put to work for SEO, she uses technical skills to make a real difference. Her ideal day involves reading Google patents & running log analyses. You can also find her on twitter, or blogging at https://merci-larry.com

A log file is a text file stored on a server. Log files can log all sorts of different information.

Any time a client–whether a browser or a bot or any other type of client–request any type of file from a website, the server adds a line to the file.

Each line includes certain information, which will vary depending on the configuration of the site and the server. Usually, you’ll find:

Ian credits a co-worker at Portent for the phrase “single source of truth”: the one defined place where you know you’re going to get the most accurate measure.

When it comes to measuring web traffic, log files are the single source of truth. If something on a web server is accessed, it’s going to appear in a log file. Any file that is hit by any visiting client will be recorded, assuming the server is correctly configured.

Javascript, which is most often used to fire analytics pixels such as Google Analytics can be inaccurate for many reasons:

Regardless of what happens with the analytics pixel, the hit is still recorded in the log file.

@glenngabe Log files are so underrated, so much good information in them.

Ian has to spend a lot of time persuading clients to allow SEOs to have access to their log files. Based on how difficult it is for SEOs to get access to this data, we can say that log files are badly under-used. This is also reinforced by Ian’s experience discussing with clients what type of work other agencies have done; log file analysis is never cited. There are a lot of insights to be gained from log file analysis that are not being taken advantage of today.

Log files have been around for over 20 years, but SEO has never paid much attention to them.

Ensuring that Googlebots spend time on your key pages and adjusting the distribution of your crawl budget is one of the principal uses of log files.

A few years ago, Ian had a client with a big site on which every page had a “forward this to a friend” link and a “request more information” link. When the site was relaunched by the client, the rankings plunged and it was difficult to diagnose the problem since everything looked fine. On-page SEO and the Google site index indications were great.

In the log files, though, it was clear that Googlebot was hitting hundreds of thousands of pages that weren’t visible on the site. It turned out that the client thought they’d removed these links from the pages, but they’d just made them invisible. Google was spending 90% of its time crawling these invisible links, and only 10% of its time and energy on pages with meaningful content.

Because these links weren’t visible, without the log files, it would have taken weeks or months to diagnose and correct the ranking drop.

Ian usually looks for quality rather than quantity. It doesn’t matter whether search engine bots hit a site more or less often after an SEO analysis and changes. It’s more useful to look at the following points in order to tell whether we have the desired bot behavior:

Check how many types of each response are actually provided to bots:

Google Search Console doesn’t always provide the most accurate data for this, so log files can provide a much more accurate measure for this metric.

By using log files to monitor Googlebot behavior, we’ve seen changes in how Google supports certain directives. Rel=canonical and rel=next/prev are big examples. We can see how Google works its way through pages, which allows us to see whether these directive declarations are actually working on a site.

It’s also worthwhile to check whether Google’s actually obeying noindex and nofollow declarations. This can tell us whether these directives are working, whether they have previously worked, or if Google has started to ignore them.

[Note: Since this episode aired, Google has announced that nofollow would be considered a hint rather than a directive . Using log files to confirm whether or not the hint is followed on your website will become increasingly important as this begins to influence ranking and, later, indexing.]

When Google makes recommendations that SEOs use directives or strategies, Ian is often a sceptic, such as with rel=next/prev. While Ian’s advice is to follow Google’s recommendations, he also relies on log files to look at whether this makes a difference in Googlebot behavior or not on websites he’s working on. In the specific case of rel=next/prev, looking at Googlebot behavior on paginated pages is nothing new. We can keep an eye on this behavior to see if there are changes:

For online publishers, this is a very common use: measuring the time it takes from when the page is put online, to the time when Google starts crawling it, to the time when it starts showing up in the rankings.

Log files are a great way to know and understand whether a page has been “viewed” by Google. It can also be a way to reassure publishers, particularly one with large sites, who are worried when content is published but not yet receiving organic traffic. Log files can help by determining whether the lack of traffic is because Google has not looked at the page yet or not. Depending on the answer, the solution will be different.

Log files can also be useful because Google Search Console may not be completely up to date. We can find out within minutes, if we’re analyzing log files in real time, whether or not Googlebots have hit a particular resource.

There’s not a perfect correlation between when a page is hit by a bot and when the page will first appear in the index. However, Ian has consistently seen that if a page is hit by a bot, it will show up in the SERPs a “short time” later.

A “short time” can be anywhere from 30 minutes to 30 days. And in general, the more popular and acknowledge a site is a source of authority, the quicker it will show up in the Google index. (Don’t yell at @IanLurie on Twitter for saying this.)

If you’re a top-20 news site and a page hit by Googlebot doesn’t show up in the index within about an hour, it’s time to worry. On the other hand, if you’re a less well-known publication and Googlebot lands on the page, you should worry if it’s been a week and your page hasn’t shown up in the index.

In short, there’s not a fixed amount of time required to get a page indexed, but you can use log files to determine what is normal for your site and to adjust your expectations accordingly.

Ian will always lean towards technical SEO first in getting a page to be indexed and rank faster. Technical improvements that affect indexing speed might include, for example, site performance: the more quickly Google can crawl on your site, the more pages it will likely put into its index.

EAT (Expertise-Authority-Trustworthiness) has an impact today on how quickly you show up in the index.

Pages need to be linked as high up in the site hierarchy as possible. Looking at evidence in log files, it’s pretty clear–at least for the first few times a site is crawled–that Googlebot crawls a site starting at the top of the site hierarchy, usually at the home page, and working its way down.

The internal links inside your site should indicate the importance of a page. To get a page to rank more quickly, multiple pages on the site need to link to it, and it’s even better if they do so from primary or secondary navigation.

Log files aren’t standardized. There are a lot of different formats, of which W3C is likely the most common.

Regardless of the format, the most important thing is to make sure that your server is configured to store the right data in those log files. It’s possible that, when a server is first set up, that it isn’t automatically configured to store the referrer, the response code, or the user-agent.

Once you understand what to look for in a log file, it’s pretty easy to interpret, no matter what the format is. It’s much more important to make sure that the right data is present. You’ll want at least the following information:

SEOs should use log files because they are the single source of truth. If you are an SEO and you want an accurate look at how search engine bots are crawling your site, there’s no other way to do it.

This is also a way to remove levels of abstraction introduced by tools, no matter how useful, like Google Search Console. The Search Console is Google’s interpretation of what they saw when they visited your site. You want to see how they visited the site, without interpretation.

With this in mind, log files have so many use cases for which we often depend on interpretive tools:

There’s no predefined set of use cases that make log files useful. What makes them useful is the fact that they provide an unedited, unbiased, raw set of data on how bots are crawling your site.

Ian’s favorite technical trick is the Linux command line tool, GREP, because it allows you to sift through a large file really quickly. This can be useful because log files can quickly become enormous. On a large site, in just a day or two, you can end up with files of millions of lines. And most desktop tools can’t handle a file when it gets that large.

This is Ian’s least favorite question. It’s difficult to understand the opposition to providing SEOs with a log file.

There are no security issues unless your server is configured very badly.

Googlebot with a smartphone user-agent is one of the bots that Ian follows attentively at the moment. This is a big one right now.
