---
source: https://yoast.com/search-console-report-checks-site-speed/
title: Core Web Vitals report Search Console checks site speed
scraped: 2026-03-23
published_on: 2020-07-13
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

# Core Web Vitals report Search Console checks site speed

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/search-console-report-checks-site-speed/
Published: 2020-07-13
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
The latest addition to Google Search Console is the Core Web Vitals report. This report helps you track the page speed of your site.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Google is rapidly expanding the capabilities of Search Console — its must-have tool for site owners/managers. We’ve seen a lot of cool structured data reports appear. In this post, we’re examining an enhancement report dedicated to site speed. It’s important to have a fast site with a good user experience and Google’s new tool helps you monitor it and improve it. Here’s is a quick guide to its capabilities.

The Core Web Vitals report gives you an idea of how fast or slow your pages load over any given time. It gives you insights that were almost impossible to get up until now. Running page speed analysis on your complete site is not something the average user can do. Testing a couple of pages in PageSpeed Insights, fine, but 1,000 pages? The new Core Web Vitals report in Google Search Console gives you an idea of how your site loads. It puts all pages in buckets conveniently labeled poor, in need of improvement and good.

As you know, site speed and user experience have been a hot topic for quite a while. Google even declared page speed a ranking factor as well as new ranking factor called page experience . The search engine is rolling out all sorts of initiatives to help visualize site speed and prioritize improvements, like PageSpeed Insights and Lighthouse . Sometimes, Google also tries some outside the box changes like Chromes “speed badge of shame” . It is one of the indicators in the Chrome browser that helps users understand why a site may be loading slower. In reality, this is more a not so subtle jab at site owners to do something about their slow sites.

This focus on site speed is understandable. Site speed is user experience and users expect fast. But in regards to all those pretty numbers and colors, it’s hard to know what to look for. But as our own SEO expert Jono Alderson loves to say: “Don’t optimize for scores — just make it faster.” Scores say a lot, but all that matters is the perception of speed by users. How quickly can you make your page feel ready?

The Core Web Vitals report looks at the pages on your site, checks their scores in the Web Vitals data and puts these into buckets. There are mobile and desktop specific checks and these might differ. Due to hardware and network differences, it is harder to get a good score on mobile than it is on desktop. You’ll notice, though, that the same URLs are often troublesome both on mobile as well as desktop. They might load slightly faster due to changes in test setting, but they are a point of interest nonetheless.

While not the end-all tool for measuring site speed, the Core Web Vitals report is a valuable addition. It helps you find problematic URLs which you can check in PageSpeed Insights to get a deeper understanding — plus ways of fixing it. This way, you can keep an eye on all speed-related things, spot trends, make improvements and keep track of the results of those changes.

The cool thing about the Core Web Vitals report is that it uses data from the Chrome UX Report . The Chrome UX Report is a public data set of real user experience data collected from millions of opted-in users and websites. This way, Google collects loads of data — like connection type, type of device and much more — from real situations and used to give a better understanding of performance in the real world. Google uses this data in several speed-oriented Google tools, like PageSpeed Insights and Lighthouse.

When looking at site speed tools it is easy to focus on the wrong stuff. Many tools check site speed in particular circumstances, like a set location at one point in time, accessed from a specific device. There’s not enough context to make a decision based on this data. That’s why our advice in this has always been for you to look at a multitude of site speed tools. Combined these will give you a better handle on the problem.

Google built the Search Console Core Web Vitals report around three metrics: FCP, FID and CLS. These three metrics form the Core Web Vitals. Here’s what these metrics mean:

The results lead to an overview of pages that have good or poor scores, or are in need of improvement. The score of a URL is the lowest status assigned to it by a specific device. According to Google, the three metrics work together to come to a conclusion about the loading of the URL:

These insights give you a good idea of how your pages are performing. As said before, you probably need to run a couple of more tests to get the full picture.

Instead of showing a gazillion URLs and the corresponding results, Google uses aggregate scores and URL groups to make the results slightly less intimidating. For any issue, you’ll see a number of URLs getting the same score or issue. So it might be that from a specific URL, 70 other URLs suffer from the same performance issues. That makes it easier to uncover issues on a grander scale because all these pages probably have the same problems. Of course, you can do a deep-dive and check individual pages by clicking on the URL list and picking a URL to analyze using PageSpeed Insights .

The same goes for scoring. Grouping makes it easier to digest the results. The Core Web Vitals report in Search Console focuses mainly on FCP and FID, as mentioned above. It’s a good idea to keep an eye on PageSpeed Insights as well, as this has a multitude of other metrics, graphics of the loading process and suggestions to improve the results.

In the Core Web Vitals report, Google calculates the FCP and FID from all the visits to those particular pages.

The calculation of these scores continues to fluctuate due to outside influences. That’s why you might see the trend line go up and down.

The Core Web Vitals report allows you to monitor your site for speed-related issues. It helps you find problems and prioritize their resolution. Once you or your developer have run through all the suggestions and improvements you can validate the fix. Google will then monitor the pages for 28 days to see if the issue is fixed for these URLs.

This post is not about telling you how to fix your site speed issues, but rather guiding you through the new Core Web Vitals report that might give you the insights you need. To get practical, you can start here:

Last but not least, an incredible source of information: Jono’s slide deck on site speed from a talk at SMXL Milan .

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

What does it mean when you run your core vital report and it returns the message “not enough data for this device type”?

Hi Simone! This help article from Google might be able to help you with your question: https://support.google.com/webmasters/answer/9205520?hl=en

Thank for describing Google search console few feature (core web vital) but I have observed few sites with bad load time ranking higher in Google SERP. This’s little bit confusing, when Google say they want good user experience from websites but still they rank slower website top in result page.

Yes, I have seen this core web vitals in my search console report, it shows both desktop and mobile versions.

Thank you for the post, very helpful. A question for me is that the overall post number is way higher than the number of posts in the core web vitals section, for example, i have 10 posts in the coverage section, but only see 4 URLs under the core web vitals section. After a recent site migration, the number of URLs even got less, like 3 now. Can you help what does that mean? and how to fix if possible? Thank you!

I’v tried testing my own website both for the desktop and mobile version. The results are quite encouraging

Hi Mark. You can find the Core Web Vitals report in the Enhancements section of Google Search Console. I’ve added a screenshot to the article pointing it out.

When I click on “Core Web Vitals” is gives me this: “Not enough data for this device type. Learn more Try PageSpeed Insights”

Hi Kenneth. Is your site new? Or have you only just added it to Google Search Console? It might take some time for Google to fill it with data. You can find more information in their help docs: https://support.google.com/webmasters/answer/9205520?hl=en

Your blog will help me to use search console more effectively.

web vital report is really helpful to check the analytics regarding the speed of any page of the website, I always lacked in tracking my website speed with different tools available in the market. Now the google itself has provided a great tool to monitor this. Overall this is good news for the blogger.

Hi John, we agree! This tool can definitely help you monitor and improve your site speed. Lots of luck with your site!

We care about the protection of your data. Read our privacy policy.
