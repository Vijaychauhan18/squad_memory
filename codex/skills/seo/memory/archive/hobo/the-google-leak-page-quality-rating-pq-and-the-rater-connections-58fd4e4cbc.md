---
source: https://www.hobo-web.co.uk/google-pq-page-quality-rating/
title: The Google Leak, Page Quality Rating (PQ) and the Rater Connections
scraped: 2026-03-23
published_on: 2026-01-11
tags: live_feed, phase1_ingest, hobo, publication, quality, leak-systems, archive_backfill, historical_source
topic: quality_systems
intent: research, monitoring, source_selection, leak_systems
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Archive backfill - Hobo Web
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# The Google Leak, Page Quality Rating (PQ) and the Rater Connections

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/google-pq-page-quality-rating/
Published: 2026-01-11
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
The connection between the specific 'PQ' acronym in the Google Leak and the 'Page Quality' system, revealing the digital twin of the human scoring system used in search rankings.

## Extracted Body
Disclosure : I use generative AI when specifically writing about my own experiences, ideas, stories, concepts, tools, tool documentation or research. My tool of choice for this process is Google Gemini Pro 3 Deep Research (and ChatGPT 5 for image generation). This assistance helps ensure our customers have clarity on everything we are involved with and what we stand for. It also ensures that when customers use Google Search to ask a question about Hobo Web software, the answer is always available to them, and it is as accurate and up-to-date as possible. All content was conceived, edited, and verified as correct by me (and is under constant development). See my AI policy .

Disclaimer : This is not official . It is theory based on a primary investigation of official and unnoficial sources. Any article (like this) dealing with the Google Content Data Warehouse leak requires a little bit of logical inference when putting together the framework for SEOs, as I have done with this article. I urge you to double-check my work and use critical thinking when applying anything for the leaks to your site. My aim with these articles is essentially to confirm that Google does, as it claims, try to identify trusted sites to rank in its index. The aim is to irrefutably confirm white hat SEO has purpose in 2026 – and that purpose is to build high-quality websites. Feedback and corrections welcome .

This article is for anyone who is wondering if Google Search Quality Evaluator guidelines have anything to do with modern SEO, and if the guidelines can be used to self assess ranking problems.

I have already demonstrated that E-E-A-T is Google’s doctrine codified . It is the rulebook that matters most in YMYL (Your Money, Your Life) topic areas, and we see this doctrine in action every time a Google Update or Spam Update rolls out. I have also highlighted through antitrust testimony that Quality raters don’t direclty impact your site rating .

I’ve also clarified that techncially you cannot add E-E-A-T anywhere. E-E-A-T is a doctrine . E-E-A-T is not mentionend anywhere in the leaked attributes although I’ve shown in previous articles how scores in a system of competing philoshopies feed into what Google calls E-E-A-T .

“ Experience, Expertise, Authoritativeness and Trust (E-E-A-T) are all important considerations in PQ rating. The most important member at the center of the E-E-A-T family is Trust .” Google, 2025

But for years, the industry has asked: Are these just concepts for humans, or are they hard-coded into the machine? Folk like myself, Cyrus Shephard, Lily Ray, Glenn Gabe and Marie Haynes have long recommended we take these rater concepts seriously.

Do the leaked “blueprints” in Google’s engineering actually reflect the Quality Rater Guidelines (QRG)?

Is the “Page Quality” (PQ) rating system actually used by Google systems? Is it the same system we are urged to “self-assess” our own content with?

The answer, found deep within the leaked Google Content Warehouse API, is yes .

And where it sites in the code gives you an idea of its importance.

The leak provides the technical confirmation that the concepts in the PDF are not just theoretical goals – they are hard-coded variables in the ranking pipeline.

And Google’s own John Mueller has given us the plain-English confirmation that matches the code perfectly.

Here is the breakdown of the specific variables that link “Page Quality” to “ranking math.”

PQ rating isn’t sexy. I can understand why the importance of this PQ rating in the leak has gone unannounced, overshadowed by sexier attributes like siteAuthority or siteFocus, and even E-E-A-T.

Buried in the thousands of lines of leaked API documentation is a variable that fundamentally changes how we should look at one aspect of site authority.

siteQualityStddev (type: number) “ Estimate of site’s PQ rating stddev–spread of the page-level PQ ratings of a site . Note this is different from nsr_variance which predicts error of NSR itself from the aggregated site-level rating.”

In the official Quality Rater Guidelines, the core metric is explicitly named the Page Quality (PQ) Rating .

It is statistically improbable that Google would use the specific acronym “PQ” in their internal engineering documentation to refer to something other than the “Page Quality” system they have spent millions of dollars refining.

They measure the spread (Standard Deviation) of that rating.

I really only found one person, Eduard Blacquière putting most of this together before.

The leak also reveals the companion variable that feeds this calculation.

The Analysis: This variable is defined as an integer . In the Quality Rater Guidelines, humans rate pages on a sliding scale (Lowest, Low, Medium, High, Highest).

The existence of pqData confirms that the algorithm converts these complex, human-centric signals into a hard number – a single integer for every URL in the index. This acts as the “Digital Twin” of the rater’s score.

For those who doubt the code, we now have the public confirmation. The variable siteQualityStddev (Standard Deviation) is the mathematical representation of Consistency .

Google has explicitly flagged this as the primary technical factor.

“Consistency is the biggest technical SEO factor.” — John Mueller, 2025

This is not a throwaway comment. It is a description of how this part of the system functions. If your siteQualityStddev is high (meaning you are inconsistent), you are failing the “biggest factor.”

Google has further explained why consistency matters, describing exactly how the siteQualityStddev variable likely functions to penalise a domain. This is not a metaphor; it is a description of the attributes described in the leak.

“One other specific piece of guidance we’ve offered is that low-quality content on some parts of a website can impact the whole site’s rankings , and thus removing low quality pages, merging or improving the content of individual shallow pages into more useful pages, or moving low quality pages to a different domain could eventually help the rankings of your higher-quality content.” Google 2011

Now that guideance was specficially for Google Panda way back in 2011.

But Panda and BabyPanda are also still in the exact same important module as PQdata.

It is always important to remember as my research on the Google leak made evident, Google is a system of competing philosopies in a ranking pipeline where after identifying relevant content T* ( Topicality ) Google aims to prioritise helpful content and deprioritise content that is harmful or potentially harmful using core systems like Q* (Q-Star) – which still includes Pagerank – and P* (Popularity signal) – and other signals – to determine rankings.

The Fix: “Removing,” “Merging,” or “Moving” are literally the only statistical ways to lower a standard deviation. If been giving that advice to my clients… since 2011. Again, we have an example of Google sharing how it works at a systems level.

This answers the question of “feedback.” If raters don’t directly change your rankings, what do they do?

We are looking at a classic Supervised Machine Learning loop. The raters teach the machine what “Quality” looks like, and the machine attempts to replicate that judgment at scale. Google essentially tells us this.

Human Input (QRG): A rater follows the guidelines and gives a page a “High” score.

Machine Training: The model analyzes the page to find patterns (signals) that correlate with that score.

Algorithmic Output ( pqData ): The model assigns an integer (e.g., 4) to millions of other pages, predicting what a human would say.

Site Assessment ( siteQualityStddev ): The system checks how consistent those scores are across your entire domain.

It doesn’t end there, though. While there is no evidence to contradict Google’s statements around Quality Raters not impacting individual sites, scores generated by human raters are evidently stored at an entity level

Google has long recommended site owners to “self-assess” their content using the questions in the SQEG. Before the leak, this sounded like general advice. Now, we know it is technical instruction.

When you self-assess, you are essentially trying to predict your own pqData score.

The presence of siteQualityStddev proves that consistency is a ranking factor. The variable measures “stddev” (Standard Deviation). In statistics, a high standard deviation means high volatility.

Low Variance: All pages are consistently good. (High Trust).

High Variance: Some great pages, many poor pages. (Low Trust).

If you have a “High Variance” site, you are mathematically unpredictable to the search engine. This supports the strategy of Pruning : removing or improving low-quality content is just as important as publishing new content.

The blueprints match. The Quality Rater Guidelines are the “Training Manual” for the human, and the variables pqData and siteQualityStddev are the “Scoring System” for the machine.

You aren’t just ranked on your best work; you are judged by your deviation from excellence. The “Self-Assessment” isn’t a suggestion – it’s the answer key to the test the algorithm is running on your site every day.

Yes . “ Search quality raters are people who give us insights on if our algorithms seem to be providing good results, a way to help confirm our changes are working well. In particular, raters are trained to understand if content has strong E-E-A-T. The criteria they use to do this is outlined in our search quality rater guidelines . Search raters have no control over how pages rank. Rater data is not used directly in our ranking algorithms. Rather, we use them as a restaurant might get feedback cards from diners. The feedback helps us know if our systems seem to be working. Reading the guidelines may help you self-assess how your content is doing from an E-E-A-T perspective , improvements to consider, and help align it conceptually with the different signals that our automated systems use to rank content.” Helpful Content Guidelines . PQ rating is mentioned 77 times in the september 2025 general guidelines . The most critical mentions of PQ rating are below:

“A Page Quality (PQ) rating task consists of a URL and a grid to record your observations as you explore the landing page and the website associated with the URL. The goal of PQ rating is to evaluate how well the page achieves its purpose.”

“Why is it important to determine the purpose of the page for PQ rating? The goal of PQ rating is to determine how well a page achieves its purpose. In order to assign a rating, you mustunderstand the purpose of the page and sometimes the website. By understanding the purpose of the page, you’ll better understand what criteria are important to consider when evaluating that particular page. Websites and pages should be created to help people. If that is not the case, a rating of Lowest may be warranted. As long as the page is created to help people, we will not consider any particular page purpose or type to be higher quality than another. For example, encyclopedia pages are not necessarily higher quality than humor pages.”

“Important: There are highest quality and lowest quality webpages of all different types and purposes: shopping pages, news pages, forum pages, video pages, pages with error messages, PDFs, images, gossip pages, humor pages, homepages, and all other types of pages. The type of page does not determine the PQ rating – you have to understand the purpose of the page to determine the rating.”

“All of the content on a webpage can be classified as one of the following: Main Content (MC), Supplementary Content (SC), or Advertisements/Monetization (Ads). In order to understand the purpose of a webpage and do PQ rating, you will need to be able to distinguish among these different parts of the page”

“Examine the landing page of the URL in your PQ rating task. Find and click on the link labeled with the name or logo of the website (occasionally labeled as “home” or “main”), which usually appears at the top of the page. In PQ rating tasks, you will need to identify who created the MC on the page.”

“The PQ rating is based on how well the page achieves its purpose”.

“The topic of the page helps determine the standards for your overall PQ assessment. Pages on YMYL topics have higher standards than pages on non-YMYL topics.”

“Different types of websites and webpages have different expectations for PQ rating. For example, PQ expectations may differ for: Small hobbyist websites vs. large corporate websites. Websites involving financial transactions vs. websites that do not require payment or collect personal information. Websites with content created by ordinary people on a volunteer basis vs. websites with content created by professionals”

“Remember: Many websites need monetization to share content with users. The presence or absence of Ads alone is not a consideration for PQ rating.”

“Important: These considerations overlap. For example, while examining the quality of the MC, you may notice factual inaccuracies that lower your assessment of Trust. While conducting reputation research, you may find information about the expertise of the content creator which increases your level of Trust. This is how PQ rating is designed to work!”

“The quality of the Main Content (MC) is one of the most important considerations for PQ rating. The MC plays a major role in determining how well a page achieves its purpose.”

“An important part of PQ rating is understanding the reputation of the website. If the website is not the primary creator of the MC, it’s important to research the reputation of the content creator as well. Reputation research should be performed according to the topic of the page. For example, if the page contains medical information, research the reputation of the website and content creator for providing medical information. Reputation research is especially important for detecting untrustworthy websites and content creators. Content may look great on the surface, but reputation research can expose scams, fraud, or other signs of harm. You never know what you will find unless you look! Therefore, reputation research is required for all PQ rating tasks.” “Reputation is important, but if reputation information is not available for a website or content creator, pay extra attention to other PQ considerations, especially when assessing pages on YMYL topics.”

“Experience, Expertise, Authoritativeness and Trust (E-E-A-T) are all important considerations in PQ rating . The most important member at the center of the E-E-A-T family is Trust.”

“Medium pages have a beneficial purpose and achieve their purpose. There is nothing wrong with Medium quality pages. Expect to encounter many Medium quality pages in PQ rating tasks. A PQ rating in the Medium range is often appropriate for pages with less extensive MC and external references. Naturally, Wikipedia articles with very little MC should get lower PQ ratings. Factual inaccuracy is a sufficient reason for a Low or Lowest rating.

“In PQ rating tasks, you may encounter pages with error messages or other types of “broken” pages. Please think about whether the page offers help for users—did the website owner make an effort to ensure that users visiting the page have a good experience and get help finding what they are looking for Pages with an explicit error (or custom 404) message are often Medium quality, since they tend to clearly communicate that there’s a problem and help users navigate to other/better pages on the website. A rating of High (or occasionally even Highest) may be used for the rare error message page that involves a high level of effort and original content and provides a truly satisfying experience for users.”

“Do not consider the country or location of the page or website for PQ rating. For example, English (US) raters should use the same PQ standards when rating pages from other English language websites (UK websites, Canadian websites, etc.) as they use when rating pages from U.S. websites. In other words, English (US) raters should not lower the PQ rating because the page location (UK, Canada) does not match the task location.”

“The PQ grid is designed to be your “note pad.” It allows you to record your observations about the landing page and the website it belongs to.”

“The steps are important and are designed to help you assess many different aspects of PQ. You may be surprised by what you find. Pages that initially look Low quality may turn out to be Medium or High quality with careful inspection. The reverse may happen as well. We want your most informed, thoughtful opinion.”

“For PQ rating, it’s not important to distinguish between expertise and experience. Instead, focus on what kind of content is trustworthy and satisfying for the purpose of the page. You may find that both expertise and experience can be trustworthy and satisfying for the same topic. For example, a medical website may be a trustworthy source for treatment options, and the experiences of other people who have gone through treatment may provide emotional support and prepare you for what to expect.” See Contextual SEO .

“Sometimes clicking on the task URL will bring up an interstitial page. You can ignore this page in your rating criteria if you can easily get to the MC. However, if the interstitial makes it extremely hard (or impossible) to get to the MC and evaluate how well the page achieves its purpose, that should factor into your PQ rating.”

“Finding information about a website is a reasonable interpretation and intent for URL queries, as some users issue URL queries to find information about a website, such as reviews or recent news. We recommended this to you as one method of reputation research in the PQ guidelines. Real users do this too. Results that give reviews and reputation information can be very helpful for a URL query.”

“The rating concepts in these guidelines apply to all types of content.”

I took the attributes in the Google leak and mapped them to the abstraction that is E-E-A-T.
