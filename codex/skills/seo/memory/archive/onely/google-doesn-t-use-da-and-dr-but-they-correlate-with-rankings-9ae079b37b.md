---
source: https://www.onely.com/blog/da-and-dr-correlate-with-rankings/
title: Google Doesn't Use DA And DR, But They Correlate With Rankings
scraped: 2026-03-23
published_on: 2022-09-28
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

# Google Doesn't Use DA And DR, But They Correlate With Rankings

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/da-and-dr-correlate-with-rankings/
Published: 2022-09-28
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Data shows that Domain Authority and Domain Rating correlate with rankings. So in many cases they may be useful in SEO.

## Extracted Body
Google doesn’t use Domain Authority or Domain Rating as ranking factors. But Google does use PageRank.

PageRank is an algorithm that measures the importance of a given web page. It considers the number and quality of internal and external links pointing to a page. Google admits to still using PageRank after over 20 years since it was invented .

https://twitter.com/JohnMu/status/1232014208180592641?s=20&t=j-WUaSvkMdiNF73GSmICCw

So as long as Google isn’t screwing with us, there is a causal relationship between a page’s rankings on Google and its PageRank score .

The problem for us is that we don’t know the PageRank score that Google is using.

And that’s exactly why metrics like Domain Authority or Domain Rating exist. Google may not use them, but we can use them to emulate PageRank.

We don’t know the exact formulas for DA and DR, just like with PageRank.

But the creators of these metrics, Moz and Ahrefs, mention the factors that they use to calculate them.

We calculate DR in a somewhat similar way to how PageRank is calculated . The main difference is that PageRank is calculated between pages, while DR is calculated between websites .

So the main difference between DR and PageRank is that DR is calculated for websites and not individual pages .

This makes sense from a technical standpoint. To calculate the Domain Rating score for individual pages, Ahrefs would need to spend way more resources . It would have to fully crawl each domain in its database.

And the same is true for the Domain Authority metric by Moz:

Domain Authority is based on data from our Link Explorer web index and uses dozens of factors in its calculations . The actual Domain Authority calculation itself uses a machine learning model to predictively find a “best fit” algorithm that most closely correlates our link data with rankings across thousands of actual search results that we use as standards to scale against .

(…) Domain Authority is calculated by evaluating multiple factors, including linking root domains and total number of links, into a single DA score .

Since we don’t know the PageRank scores of our pages, we need something else to evaluate the strength of their link profiles . We need metrics that we can work on and see an improvement in our rankings.

But if these metrics are any good, they would have to correlate with Google’s rankings. Meaning that as your page’s DR or DA score goes up, so should its rankings.

After all, there’s a causal relationship between PageRank and Google rankings. So proxy metrics for PageRank should correlate with Google rankings.

And they do – I checked. Both DA and DR are actually quite strongly correlated with rankings.

There’s a correlation between a given domain’s DA and DR and its position in the top 10 organic search results. But the whole picture is more complex.

For Domain Authority, the average correlation coefficient is 0.16.

When it comes to Domain Rating, the average correlation coefficient is 0.14 .

This indicates a slight correlation between these metrics and rankings. When you consider that PageRank (which DA and DR simulate) is one of hundreds or thousands of ranking factors, then it’s actually a significant correlation.

But when we look at the distribution of correlations for different keywords and SERPs, they vary greatly .

Starting with Domain Rating, it had a slight positive correlation with most SERPs, but there were many edge cases.

And with Domain Authority, the distribution of correlation coefficients looks very similar.

As you can see, the correlation is negative for many keywords, and for some, very strongly so. This means that there are SERPs where DA and DR do the opposite of what they should.

And keyword difficulty makes it even more interesting. Both DA and DR are most correlated with keywords of medium difficulty.

As keywords get more difficult, DA and DR become less predictive. Domain Authority is slightly less predictive for keywords of medium difficulty but performs a little better with the most difficult keywords.

The chart below shows how the correlation between Domain Rating , Domain Authority , and Google rankings can vary depending on keyword difficulty.

But this doesn’t mean that DA and DR aren’t important for difficult keywords. It might be that to rank for difficult keywords, you need to meet an importance threshold. And then other ranking factors are more decisive.

PageRank is one of many factors that influence a given page’s rankings on Google. So an average correlation coefficient of 0.14 and 0.16 is a good score.

If it were the only thing influencing rankings, I would expect a much stronger correlation, but… it’s not. So congrats to Moz and Ahrefs!

My general conclusion from this research is that DA and DR can be useful in SEO.

But don’t blindly improve them. Before you decide you need to get some external links to rank higher, look at your SERPs.

With difficult keywords, you might want to focus on other factors first.

And with some keywords, DA and DR may be completely irrelevant to rankings.

Looking to improve your Google rankings? Start with technical SEO!

And if you want to find out more about our offer first, here’s an intro to our technical SEO services.

I took 10 randomly selected domains from various countries and industries. I then used Ahrefs to select 200 keywords each of these domains was ranking for, giving me 2000 keywords of various lengths, types, and difficulty .

I exported the top 10 organic SERP results for each of the 2000 keywords using Ahrefs with the United States chosen as the location . Then I got the DA and DR scores for all domains I found.

With this data, I was able to calculate Pearson’s correlation coefficient between DA and DR for each of the 2000 SERPs I collected .

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
