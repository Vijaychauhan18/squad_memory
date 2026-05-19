---
source: https://moz.com/blog/seo-and-core-algorithms
title: SEO & Core Algorithms: How to Address, Analyze, and Affect
scraped: 2026-03-23
published_on: 2022-03-15
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# SEO & Core Algorithms: How to Address, Analyze, and Affect

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/seo-and-core-algorithms
Published: 2022-03-15
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Given how cryptic Google typically is about core updates, it can often seem like we’re at the mercy of the algorithm, with no legitimate measures of our own to employ. However, there are in fact ample tactics at our disposal to address, analyze, and affect the outcomes of core algorithm updates.

## Extracted Body
Core algorithm updates can be the bane of an SEO’s existence. The number of unknowns coming out of an update keeps people on their feet, as Google seemingly sits back and watches them scramble to address the changes.

Given how cryptic Google typically is about core updates — and even regular updates, for that matter — it can often seem like we’re at the mercy of the algorithm, with no legitimate measures of our own to employ. Google itself has even stated repeatedly that website owners shouldn’t view updates as something they are fighting against.

With all that said, do we just throw our hands up in defeat? The answer is no — there are ample tactics at our disposal, but as with anything in SEO, it’s a more nuanced, longer-term play. Throughout this article, we’ll explore how to address, analyze, and affect the outcomes of core algorithm updates.

First and foremost, it’s important that we properly calibrate how we think about core algorithm updates. As previously mentioned, Google has confirmed that there is no “fix” that website owners should enact in response, tweeting the following after a previous core update:

The reason for this lack of an easy “fix” is because websites are evaluated over a period of time. Essentially, this can be viewed as a single, aggregated report card that is then used to inform decisions to reward, punish, or maintain a site’s current status.

Continuing with this metaphor, in order to earn good marks at the end of the school year, we should ensure that we are doing our very best throughout the semester rather than constantly skipping class and cramming right ahead of the final. In the same vein, it’s important to mention that many SEOs have identified a trend where website changes in the weeks leading up to a core update are largely disregarded . This finding does make sense in the context of websites being evaluated on changes made over a longer period of time rather than within just a couple of weeks. In the rare event where Google is kind enough to give us advanced notice of an update, that should not be the signal for us to implement a barrage of changes sitewide.

In an attempt to provide some semblance of concrete data that we can actually use to better understand timing, below are some takeaways using the launch dates of past core updates. The “Brackets” Core Update seems to mark the beginning of when the concept of “core algorithm updates” became more popularized. So, with that in mind, we can glean the following insights from past core updates since “Brackets” in March of 2018.

We’ve only seen 2 updates in Q4 (Google is probably enjoying the holidays).

Most common time of month: Nine out of twelve updates have taken place in the first half of the month (prior to the 15th). More than half of the updates have taken place within the first four days of a month (maybe Google runs on monthly sprints).

To some extent, we can leverage this data. The average time in between Google Core Algorithm updates is 120 days, which falls in line with our finding that core algorithms updates typically happen three times a year. This can generally be used as a gauge to understand the amount of time we have in between core updates to prompt recovery or algorithmic gains.

Now that we understand the possible timing of core updates, we now need to properly analyze website performance after an update has been rolled out. Within recent years, Google has been slightly more transparent about changes to their algorithm. One piece of information they’ve shared is how long the roll-out period lasts: one to two weeks.

Although everyone will be eager to check trend lines as the rollout is occurring, a deeper analysis should really only be conducted two weeks after the initial launch date, or after Google has indicated that the update has finished rolling out. This will help to mitigate multiple rounds of post-update analysis.

I’ve found that STAT’s Competitive Landscape tab is one of the best methods to get an initial gauge of website performance fluctuations. The reason for this is because STAT is capable of providing possibly the most accurate depiction of website visibility around keywords you care about most, because you yourself are able to determine the keywords that are being tracked. Alternatively, however, if you are tracking a small subset of keywords or if you’ve just recently added keywords, STAT may not be the most insightful, as you’ll likely want a set of keywords large enough to mitigate outliers, and STAT is unable to provide historical data retroactively.

Assuming that you have a large enough keyword set, you’ll want to navigate to the “Competitive Landscape” tab of STAT, as shown below.

You will then see a chart which shows trend lines of the top 10 sites by share of voice. In STAT, share of voice measures the visibility of a given keyword set on Google:

Share of voice = Total click-throughs (520) / Total search volume (10,100) = 5.15%

By leveraging this tool, we’re able to understand SERP volatility to the top 10 competitors. Every seven days, STAT does a simple tally of the sites that appeared the most frequently in the top 10 search results for your selected keyword set. This is how those top 10 competitors are selected.

Some of the many insights we can glean in the context of a Core Algorithm Update are the following:

Changes in visibility within the general space of your keyword set : Gains or losses to an industry as a whole may indicate a number of things, such as a general increase in demand or reduction of Google SERP features.

Changes in visibility to your website: Gains in visibility to your site after an update indicate that your site was positively impacted, and losses indicate that your site was negatively impacted. Inverse relationships in visibility between your site and competitors can indicate who the winners and losers are after a major update.

Changes in visibility to Google: Typically, if Google shows a higher level of visibility after a Core Algorithm Update, it is likely the case that they’ve introduced additional SERP features that effectively shifts visibility from your website or competitors.

Based on your visibility around a given keyword set, your own website may or may not be automatically included within the view. Below is how to add your website into the Competitive Landscape tab, if not automatically included.

Select a site in your Data Views pane, in the Site Tools pane, click Settings.

Domains are matched exactly, so “www.example.com” does not include “example.com” or “shop.example.com.”

Do not include schemes (“http://” or “https://”) or directory paths (“www.example.com/blog/”).

Your pinned site will now appear in your share of voice charts and tables (as shown in the bottom left of the above screenshot) . It may take up to 24 hours for this data to be calculated. Pinned sites are identified with an asterisk.

Whether you find that your website was impacted or not, as a next step, I like to use Search Analytics for Sheets , which is a Google Sheets add-on that allows you to request and backup data from Webmaster Tools. This tool is basically an enhanced Google Search Console. It allows you to segment multiple data points (date, query, page, etc.) to get a much higher level of granularity than can be achieved on Search Console’s standard web frontend.

Let’s take a look at a website that was positively impacted by the June 2021 core update and use this tool to understand possible algorithmic changes.

Our date range should be relatively small, but ensuring that it incorporates the entirety of the roll out period, a few days before, and as many days after as available. Including days prior will help you understand standard pre-update performance and can be a point of comparison. The days after will, of course, help you to understand post-update changes.

Given the rollout period was from June 2 – June 12, I’ve elected to use a 22-day date range 5/30 – 6/20. Next, using the “Group By:” field, add the date. Ensure that all branded keywords are excluded by using the “Filter” fields. Lastly, click “Request Data” in blue at the very bottom of the side panel.

Once the data has been generated, there is quite a bit of data manipulation that can be applied in order to glean insight. Generally speaking, absolute changes ([current period] – [prior period]) and relative percent changes ( ([current period] / [prior period]) – 1) are great formulas to understand movement. Below is an example of what this might ultimately look like:

Based on this data, we now have a general understanding of the following trends:

My website appears to have been positively impacted by the core update:

As mentioned, while there may be other factors at play to consider, such as other Google updates, day of the week, website migrations, technical website changes, etc., the above will be directionally helpful for website owners to be able to answer the question, “was my website affected?”

Last but not least, we want to explore the types of website changes that may be slightly more valuable in the context of core algorithm updates. While there is no limit to the types of tactics that we can leverage to try to prompt favorable algorithmic responses, we can make some educated guesses based on Google’s historical primary focus areas.

Since the Medic Update of August 2018, Google has cracked down on sites that are categorized as “Y-M-Y-L” (Your Money Your Life). YMYL sites are ones that fall within the medical, health, financial, and news fields, and can be considered sites that have the ability to impact someone’s livelihood. Google introduced this concept and a higher degree of scrutiny as a means of combating the spread of false information at that time.

Since August 2018, YMYL websites have notoriously been a consistent target of Google updates . From 2018 – 2020, trendlines of websites likely categorized as YMYL would frequently experience steep hills and plummeting valleys in the aftermath of a core update.

Even if your website does not fall within these areas, it is likely that Google is still evaluating the same type of criteria on all sites, although to a slightly lesser extent. So, with this in mind, a general strategy is to preemptively make sweeping updates to your website’s signals of expertise, authority, and trustworthiness (E-A-T). The concept of E-A-T was born out of the necessity to meet Google’s increasingly rigorous standards.

Given all that background, and using recurring themes from Google’s Search Quality Evaluator Guidelines (what human quality raters use to evaluate websites and SERPs), below are 10 specific website updates that can elevate your website’s E-A-T signals. This list is typically where I would start when trying to prompt recovery after declines coming out of a core update:

Include author bylines, bios, and author pages by listing specific credentials and awards

Maintain off-page reputation by updating your Wikipedia page and other informational sources

Showcase business reputation through testimonials and reviews on-site

E-A-T aside, though, general technical issues are a high contender for priority website fixes. Using Google Search Console’s indexation report and Deep Crawl, there are no shortage of technical fixes to rectify for any type of website.

In summary, you, the website owner, are in fact armed with a number of tools to fend off harmful algorithmic declines – as the saying goes, the best defense is a good offense. By better understanding how to address, analyze, and affect the outcomes of core algorithm updates, you can be better prepared for the inevitable turbulence on a triannual basis! Are you ready for the next core algorithm update?

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
