---
source: https://moz.com/blog/state-of-web-and-core-web-vitals-part-three
title: Performance as a Ranking Factor: State of the Web and CWV
scraped: 2026-03-23
published_on: 2021-10-19
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

# Performance as a Ranking Factor: State of the Web and CWV

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/state-of-web-and-core-web-vitals-part-three
Published: 2021-10-19
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Are Core Web Vitals correlated with rankings? If so, is that any more true than it was before the Page Experience Update? In the third and final post of this series, we’ll see what the data tells us about the relationship between CWV metrics and organic ranking performance.

## Extracted Body
In part one of this series, we talked about how Google and the web in general were not really ready for the Page Experience Update — Google’s CrUX data covered too few websites, the vast majority of which were not hitting the required thresholds. That was why, I suggested, the update had been so delayed and watered down.

In part two , we talked about the metrics themselves — their flimsiness, their arbitrariness, their openness to manipulation. This, too, I suggested, might be holding Google back.

However, the proof is in the pudding. Are Core Web Vitals, taken individually or as a whole, correlated with rankings? If so, is that any more true than it was before the Page Experience Update? In this third and final post of this series, we’ll see what the data tells us about the relationship between Core Web Vitals metrics and organic ranking performance.

This is, at most, a correlation study. There are many mechanisms by which something can be correlated with rankings without having directly influenced rankings.

For example, perhaps websites that take SEO seriously rank well, and also tend to work on their loading performance. If so, loading performance and ranking would be correlated even without any direct causal link.

We’ll talk through potential implications as we go, but please, proceed with caution!

To start with, I decided to look only at the URLs that had CrUX data in the first place. You may remember from part two that, at the time of the update rolling out in August this year, that was some 38.3% of URLs. This is taken from the top 20 results for 10,000 MozCast keywords, across mobile and desktop device types.

Note that these URLs are all taken from the top 20, so it’s interesting that the averages are both well above the rank of 10.5 we’d expect. This is likely because higher traffic URLs are disproportionately likely to rank well, and also disproportionately likely to have CrUX data.

We see a solid 0.39 ranking position lead here for the URLs that pass all three CWV thresholds, above those that fail at least one.

On the face of it, the above data looks very promising for CWV as a ranking factor. However, it’s worth tempering our excitement a bit.

Let’s have a look at the same data but from May, before the Page Experience update rolled out:

The average rank of URLs with CrUX data was generally worse in August than in May. This is to be expected, as more URLs had CrUX data by August, so it had worked its way further down the rankings.

URLs which pass the CWV thresholds already had a ranking difference even before the update. This suggests that perhaps URLs which pass the test were already better in other ways that already counted towards rankings (for example, perhaps rankings were rewarding URLs with a good user experience).

The difference between URLs which passed the thresholds and those which did not has grown from 0.38 in May to 0.39 in August — although this is probably very easily within the margin of error.

It’s also interesting to contrast with a performance metric which was not part of the Page Experience update: Speed Index, as reported in Lighthouse lab results.

As “passing” the three thresholds for CWV represents being in the top 36.3% of URLs by that metric, we can compare what ranking difference is associated with being in the top 36.3% for Speed Index.

We can see in this chart that Speed Index, despite not being an explicit ranking factor, has a modest improvement in average rank associated with this percentile breakdown (0.17, vs. 0.39 for passing all three CWV thresholds). This doesn’t mean that Speed Index is a ranking factor, it just means that these things can be related in more complex ways.

(If you’re a mathematics nerd like me and you’ve just noticed the weighted average rank of the two groups is not the same, that’s because there are a tiny number of URLs for which I was able to obtain CrUX data, but not lab data, due to server errors, etc.)

The real impact was felt for URLs that failed all three tests. Although these URLs often started out ranking best of all (probably because they disproportionately represent some important, household name brands) they’ve taken a hit with the update. These URLs have had a 1.15 position ranking drop, compared to around 0.2 for URLs with CrUX data taken as a whole.

This, as I mentioned in part one, is different to what Google set out to do. Back in the original FAQs for the update in 2020, Google said:

For all the data reasons I covered in part one, likely they weren’t able to do this, and had to improvise a bit, instead only applying the relative penalty (or absence of a boost) for URLs that failed all metrics, rather than for URLs that failed one or more.

Well, no, that’s not quite the attitude. There are still lots of other reasons to want to pass all three, and more importantly, to have a generally good page experience. Google is only going to be looking for more ways to augment and ramp up these factors over time.

Also, the rest of SEO still counts. Check out the rather more pronounced difference associated with Page Authority, for example:

Ready to see if your site's pages are passing one CWV or none? Head over to Moz Pro and check out the Performance Metrics beta within our Site Crawl toolset.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
