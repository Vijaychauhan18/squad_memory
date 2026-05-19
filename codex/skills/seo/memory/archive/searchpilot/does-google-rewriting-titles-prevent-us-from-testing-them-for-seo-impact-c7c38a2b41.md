---
source: https://www.searchpilot.com/resources/blog/google-title-rewrites
title: Does Google rewriting titles prevent us from testing them for SEO impact?
scraped: 2026-03-22
published_on: 2023-08-07T09:55:57+01
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Does Google rewriting titles prevent us from testing them for SEO impact?

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/google-title-rewrites
Published: 2023-08-07T09:55:57+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Title tag testing still works even with Google rewriting many page titles for display in the search results. Since the majority of titles are not substantially rewritten, and title tag changes are among our most consistently detected and largest impact tests, it would be worth continuing to run title tag experiments even at much higher levels of rewriting than we see in the wild today.

## Extracted Body
If you came here for more than that, here’s our full current thinking:

At the time of writing, in late 2021, following a lot of back-and-forth over the summer, Google has confirmed that they are using HTML title elements in the search results over 80% of the time . Moz’s research has shown a high incidence of small tweaks vs. the HTML title alongside rarer rewrites . Lily Ray has a deep dive into the whole landscape if you want to geek out.

As all of the commentary has noted, it wasn’t entirely new for Google to rewrite titles (here’s Google spokesperson Matt Cutts on the subject in 2014 [video] ), but what did change this year was the frequency and the degree to which the rewrites happen. This is relevant to our situation because it does mean that all our title tag case studies to date that detected a statistically significant impact did so in an environment where we couldn’t perfectly control the title displayed to searchers.

And title tag tests are our most consistently statistically significant:

The first thing to note is that our testing is robust enough to detect changes that appear unevenly across the variant group - this is exactly what happens during the time that Google is recrawling and reindexing the targeted site section, when some pages will be seen to have the new treatment and some won’t. The way the neural network analysis works is that it can detect an uplift if it is large enough and spread out enough, but it doesn’t need to be uniform across the site section.

In the context of title rewriting, what that means is that any % of pages having their titles entirely rewritten such that our change is entirely invisible to users will reduce the power of our statistical tests by some related proportion. In the extreme case that all our titles were overwritten in a way that was totally independent of our test, then obviously we wouldn’t be able to detect an impact. Since the majority of titles are not substantially rewritten, and title tag changes are among our most consistently detected and largest impact tests, it would be worth continuing to run title tag experiments even at much higher levels of rewriting than we see in the wild today.

Secondly, in the case of minor changes (truncations for length or other similar basic modifications) it is quite likely that the effect of the change we are testing will survive the rewrite, and the impact will continue to be detectable. If these changes are detectable and positive, they will be worth rolling out to the whole site section with the presumed minor rewriting that will go with it.

Thirdly, we may even have hypotheses that are specific to the new world, such as testing the possibility that if we write better titles ourselves, then Google will either rewrite them less or rewrite them better and hence our change will be statistically significant in part because Google is rewriting more aggressively.

Finally, Google has confirmed that the original titles are what matter for ranking purposes, so it is of course possible that there could be a detectable effect coming from improved rankings even if Google was rewriting 100% of the site section’s titles in such a way that our change was not visible which is itself very unlikely.

While there are some changes that are focused entirely on modifying the title in situ (e.g. truncating for display length), most of the new and interesting rewrites take content from elsewhere on the page and use that to modify or rewrite the title. It’s quite possible, therefore, that other kinds of tests (most likely rewriting of headings, addition of HTML structure such as bullets etc, or changes to structured data) could impact the title as displayed in the search result . Since display snippet changes - and especially title changes - are so consistently dramatic and measurable, we may find that other on-page tests could have a significant impact on search performance because they end up influencing Google to write better display titles.

Recently Google announced that they’re rolling out “continuous scroll” for mobile search . With this addition to the search environment, we’re expecting results that were on the second and third page to start seeing a boost in impressions. It’s possible that lower-ranking results could conceivably benefit more from having more compelling titles - if someone hasn’t found what they wanted in the first ten results, then the display snippet (and especially title) may be more important in their decision of whether or not to click. There is also simply more room for improvement for lower-ranking content that is by its nature currently getting lower click through rates.

Putting all of this together, we might expect to see more dramatic impacts - both positive and negative - from title tests on mobile with continuous scroll in place.

So - it’s still very much worth testing title tag changes as changes to the display of your snippet in the search results are many of our most impactful tests as well as our most-often-statistically-significant tests, and so even if Google’s changes might dampen the effect, title tag changes are here to stay.
