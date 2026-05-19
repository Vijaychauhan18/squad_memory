---
source: https://www.hobo-web.co.uk/qualitynsrpqdata/
title: Google's Leaked QualityNsrPQData: The Core of Page Quality Assessment
scraped: 2026-03-23
published_on: 2025-10-05
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

# Google's Leaked QualityNsrPQData: The Core of Page Quality Assessment

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/qualitynsrpqdata/
Published: 2025-10-05
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
It’s a rare chance to look under the bonnet and see the engineering that powers the modern web. We can’t see inside the engine with this leak, where things are calculated, but we can see all the inputs that go into the engine, so to speak. The Google Content Warehouse is not just a database; it’s ... Read more

## Extracted Body
It’s a rare chance to look under the bonnet and see the engineering that powers the modern web. We can’t see inside the engine with this leak, where things are calculated, but we can see all the inputs that go into the engine, so to speak.

The Google Content Warehouse is not just a database; it’s the engine’s digital memory, an API that lets Google index and analyse the web on a scale that’s still hard to fathom.

The primary storage unit for any given URL is a CompositeDoc, a complex file holding everything Google knows about a page. And nestled within that file is the module that’s the subject of this analysis, the key to understanding Google’s modern perception of quality: GoogleApi.ContentWarehouse.V1.Model.QualityNsrPQData.

For years, my work has involved reverse-engineering Google’s ranking systems through observation, testing, and analysis. The QualityNsrPQData model, however, isn’t a theory; it’s the data structure itself. It holds the page-level quality signals that feed directly into core ranking systems like Mustang—the system responsible for scoring and serving search results. This is the closest we’ve ever come to seeing the raw ingredients of Google’s quality recipe.

What this model confirms is something I’ve been telling clients for over a decade: there is no single “quality score.” It’s a myth. Instead, Google’s evaluation is a multi-faceted, multi-layered assessment. The QualityNsrPQData model is a collection of distinct, yet interconnected, signals that work together to build a holistic quality profile for a URL. It looks at everything from the effort invested in the content to the integrity of the site’s link neighbourhood. It’s not a simple pass/fail test; it’s a sophisticated, multi-vector analysis. For any SEO who wants to move beyond the basics, understanding the function and interplay of each signal within this model is no longer optional. It’s the new foundation of our craft.

At the heart of this data model is a concept that feels like the modern evolution of everything we’ve ever known about site authority: Normalised Site Rank, or NSR. Back in the day, PageRank was the metric that changed the game. NSR appears to be its spiritual successor, a far more sophisticated algorithm for assessing the reliability, trustworthiness, and authority of a website. It’s a metric used to normalise and compare content quality across the entire index, often on a transformed scale to keep comparisons consistent.

The predictedDefaultNsr attribute is what I would consider the baseline or default quality score for a URL. Crucially, it’s a VersionedFloatSignal, which means Google doesn’t just see the score today; it maintains a historical record. This has massive strategic implications that I’ll touch on later. This score is the foundation upon which other adjustments, or “delta” signals, are applied.

The calculation of this default score is derived from a combination of signals that have been the bedrock of my profession for years:

A high predictedDefaultNsr score is a clear sign that Google’s systems see a website as trustworthy and well-maintained, giving it a powerful head start in the search results.

For years, Google’s public guidelines have championed E-E-A-T (Experience, Expertise, Authoritativeness, and Trustworthiness). I’ve written countless articles on the topic, and the NSR framework appears to be the algorithmic manifestation of those principles. It’s how Google’s engineers have quantified the abstract concept of trust.

Think about it: every factor contributing to the NSR score is a proxy for trust. A site linking to spammy neighbours is untrustworthy. A page that users immediately bounce away from has broken their trust. Thin, inaccurate content is, by its nature, not trustworthy.

Therefore, I don’t see predictedDefaultNsr as just a “quality score.” I see it as a calculated “trust score.” A high value here means the algorithms have determined the URL is a reliable and authoritative source. This reframes the entire purpose of SEO. Our job isn’t just to chase rankings with clever tactics; it’s to build algorithmically trusted entities. It’s about demonstrating to Google, through every signal at our disposal, that our content is a safe, reliable, and valuable answer for its users.

While predictedDefaultNsr provides a foundational score, the QualityNsrPQData model contains a suite of more specialised signals that offer a granular, multi-dimensional view of a page’s quality. These signals allow Google to evaluate content based on the effort of its creation, its integrity, its initial trustworthiness, and its potential for being very low quality. The following table provides a strategic overview of these key signals before a detailed analysis of each.

Rate My Page Quality using the Hobo SEO Method : A prompt that uses a 12-criterion methodology to perform a deep audit of a single URL, algorithmically estimating its contentEffort and E-E-A-T signals.

Of all the signals revealed, contentEffort is the one that feels most like the future. It’s defined as a Large Language Model (LLM)-based estimation of the effort required to produce an article page. This is a paradigm shift. For my entire career, we’ve used indirect proxies for effort—word count, backlink profiles, and so on. This is a direct, algorithmic quantification of the human labour, originality, and resources invested in creating content.

This attribute is the technical engine of Google’s Helpful Content System (HCS). I’ve spent the last few years helping clients navigate the HCS, which rewards content “created for people” and demotes content made “for search engines.” The contentEffort signal is the scalable mechanism that makes this distinction possible. It assesses things that are hallmarks of people-first content: depth of knowledge, original research, and the difficulty of replication. A low contentEffort score is a powerful flag that content may not be “people-first,” potentially triggering the site-wide demotion that has become the signature of the HCS.

With the explosion of generative AI, the web is flooded with content that is grammatically perfect but utterly soulless and unoriginal. The contentEffort LLM is the direct countermeasure. It’s trained to spot the difference between high-effort content—unique data, complex analysis, original images—and the formulaic, generic text that characterises low-effort work.

Fundamentally, I see the contentEffort score as an anti-commoditisation metric. It’s not just measuring effort; it’s measuring replicability . If your content can be easily and cheaply reproduced by a competitor or an AI, it’s a commodity with little unique value. This means that investing in truly unique assets—original research, proprietary data, exclusive interviews, custom visuals—is no longer just a “best practice.” It’s a direct, measurable input into a core Google quality signal.

The tofu attribute stands for “Trust on First Use.” This is a concept I’ve grappled with for decades: how do you get a brand-new website or a new piece of content to rank when it has no history? This signal is Google’s answer. It’s a predictive quality score designed specifically for new URLs that lack the historical data and user interactions that power other systems.

TOFU functions as an initial quality predictor. It allows Google to make a preliminary judgment before the URL has had a chance to accumulate user engagement signals like clicks and dwell time. To do this, the TOFU model looks at intrinsic signals available from the moment a page is crawled: the consistency of quality across the site, the nature of its outbound links, the level of on-page “clutter” like excessive ads, and core technical factors like HTTPS.

Every new URL presents a “cold start” problem. A powerful system like NavBoost can’t work without user clicks, which a new URL doesn’t have. The tofu signal is the solution. It creates a predictive score based on the evidence it can see on day one. Is the site technically sound? Is the content free of spam signals? Does it link out to reputable sources? A high initial tofu score can give new content a fair shot in the SERPs, allowing it to earn the user interaction signals that will inform its ranking journey. A low score can leave it languishing in the “sandbox,” a concept we’ve debated for years, which now seems more real than ever.

The chard and chardScoreEncoded attributes represent a versatile, content-based metric used to evaluate quality and reliability. It’s not a single score but a multi-purpose classification system. It seems to have different variants for identifying specialised content, such as hoaxes, machine-translated pages, or, most critically, pages that fall into the “Your Money or Your Life” (YMYL) category.

The primary function of the chard system is to understand the fundamental nature and integrity of the content. A high chardScore indicates a well-maintained site with valuable content. I think of it as a “content-DNA test.” Its role is to classify the content and flag potential risks that require different evaluation criteria. You can’t apply the same quality standards to a recipe blog as you do to a financial advice article; the potential for real-world harm is vastly different.

The chard system appears to be the initial classifier that determines what kind of content is being processed. If chard classifies a page as YMYL, it would then trigger a more rigorous evaluation of E-E-A-T signals. If it identifies a page as machine-translated, it might trigger a different model to assess fluency. chard establishes the context for all subsequent evaluations. A mismatch—like a YMYL page with no author information or sources—would almost certainly lead to a poor overall quality assessment.

Google has always loved its quirky internal codenames, and within the QualityNsrPQData model, we find keto and rhubarb. These aren’t just random; they refer to specific internal models with distinct roles.

Both of these signals appear to function as “delta” or modulating factors. They aren’t the primary quality score but rather composite scores from specific models that adjust a baseline score like predictedDefaultNsr.

These specialised models allow for more nuanced adjustments. The rhubarb model, a “Site-URL delta signal,” likely calculates the difference between a site’s overall average quality and the quality of a specific URL on that site. This would allow Google to reward “hidden gems” on mediocre domains or penalise a “bad apple” on an otherwise high-quality site.

The keto score is mentioned in connection with AI predictive value. Given the metabolic association of the keto diet with efficiently burning fat for fuel, I’d wager this model’s codename is a metaphor for its function: identifying “lean,” efficient, and highly valuable content that directly and quickly satisfies a user’s need. It might do this by analysing user engagement, rewarding pages that are information-dense and resolve queries effectively. Together, these specialist models allow Google to layer nuance onto its scoring, leading to a more accurate and context-aware final evaluation.

While some signals reward high-quality content, others are designed to identify and penalise poor content. These act as a “quality floor,” below which a page is unlikely to perform well.

These are powerful demotion signals. The existence of page2vecLq is particularly revealing. I remember the days of fighting blatant keyword stuffing and hidden text. The Page2Vec methodology is far more sophisticated. It converts the semantic meaning of a page into a numerical vector.

By training a model on a vast dataset of pages identified as “low quality,” Google can map out a “low-quality region” in this semantic space. When a new page is crawled, its own vector is generated. If it falls within that low-quality region, it gets a poor page2vecLq score. This allows Google to detect new forms of spam that don’t conform to old patterns. It’s a proactive, meaning-based approach to content policing that makes it much harder for low-effort content to gain traction.

For all the talk of on-page analysis and AI, let me be clear: links still matter. I’ve been building links since before Google existed, and they remain a foundational pillar of its ranking algorithm. The QualityNsrPQData model confirms this by including several attributes dedicated to link-based signals.

The presence of these attributes directly within the page quality model underscores that link data is not a separate, secondary consideration; it is an integral component of a URL’s overall quality profile. Core systems like PageRank, which estimate a page’s importance by counting the number and quality of its links, are still fundamental to how Google works.

The numOffdomainAnchors metric is particularly insightful. It’s not just a link count; it’s a raw count of the unique ways other sites describe a page. I’ve always taught that anchor text is a powerful relevancy signal. A high number of diverse, relevant anchor texts from a wide array of external domains is a strong, cumulative signal of a page’s authority and topical relevance. It reflects a broad consensus across the web about what a page is about.

Within this holistic framework, link signals play a crucial role as the external, third-party validation for Google’s own content analysis. There’s a symbiotic relationship here between Google’s internal assessment and the web’s collective “peer review.”

Signals like contentEffort and chard are Google’s internal evaluation—the “self-assessment.” In contrast, signals like linkIncoming and numOffdomainAnchors represent the web’s collective judgement—the “peer review.”

The ideal scenario is an alignment between these two perspectives. A page that scores highly on contentEffort (high intrinsic quality) and also boasts a high numOffdomainAnchors from authoritative sites (strong external validation) presents an unambiguously powerful and trustworthy signal.

This reframes the purpose of link building. It’s not about accumulating “link juice.” It’s about earning genuine, external validation that corroborates Google’s own algorithmic assessment of your content’s quality. The most sustainable off-page strategies are those that focus on creating content so valuable that it naturally earns the external endorsements that validate its quality.

The QualityNsrPQData model also points towards more automated and granular systems for adjusting page quality scores, suggesting a level of sophistication that goes beyond evaluating a page as a single entity.

The term “Autopilot” in other Google products denotes automated management. In search quality, urlAutopilotScore likely refers to a system that applies automated adjustments to a URL’s quality score without a full re-evaluation by the more expensive models. The deltaAutopilotScore would then represent the specific adjustment applied during a given update cycle.

The concept of “subchunks,” revealed by these attributes, is critically important. It confirms that Google doesn’t treat a webpage as an indivisible block of text. Instead, it deconstructs pages into logical components. The subchunkData holds the raw information about these identified parts (header, main content, comments, footer, etc.). This data is then evaluated to calculate the deltaSubchunkAdjustment, an aggregated quality score from these individual parts that can apply a positive or negative adjustment to the overall page score.

The existence of the deltaSubchunkAdjustment signal has profound implications, giving rise to a concept I’m calling “template-level SEO.” This signal means that the very structure and boilerplate components of your website’s page templates are being algorithmically scored and are actively contributing to the quality assessment of every page that uses them.

This means boilerplate content, user-generated content (UGC), navigation, and footers are not neutral. They are active contributors to a page’s final quality score. For years, we’ve told clients to clean up their templates, but now we see a direct signal that scores it. This necessitates a shift in focus. Auditing and improving every repeatable element on a page template is now a direct way to influence this quality signal. The quality of the template is as important as the quality of the unique content within it.

A subtle but profoundly important detail in the QualityNsrPQData model is that critical signals like predictedDefaultNsr, contentEffort, keto, and rhubarb are stored as VersionedFloatSignal or VersionedIntSignal.

This reveals that Google isn’t just storing the current quality score. It’s maintaining a historical ledger of these scores over time. This technical detail provides a concrete explanation for a phenomenon I’ve observed for my entire career: the time lag before changes are fully reflected in rankings.

Whether it’s an improvement or a degradation, the effects are rarely immediate. The versioning of signals clarifies why. Google’s systems aren’t just seeing a new state; they are building a new historical record and evaluating the trend.

The versioning of core quality signals implies that Google can, and likely does, analyse the trajectory of a page or site’s quality over time. This concept of “algorithmic momentum” is likely a powerful meta-signal. A single data point is information, but a series of data points over time reveals a trend.

This “algorithmic memory” allows Google’s systems to differentiate between several scenarios:
