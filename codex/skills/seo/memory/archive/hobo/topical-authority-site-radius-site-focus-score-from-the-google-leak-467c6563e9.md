---
source: https://www.hobo-web.co.uk/topical-authority/
title: Topical Authority: Site Radius & Site Focus Score from the Google Leak
scraped: 2026-03-23
published_on: 2025-10-12
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

# Topical Authority: Site Radius & Site Focus Score from the Google Leak

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/topical-authority/
Published: 2025-10-12
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
Unlock "Topical Authority" in SEO! This report reveals Google's shift to quantitative "relevance" (T* score) & a blueprint for dominance. Master E-E-A-T, content architecture & AI for long-term success.

## Extracted Body
QUOTE: “Back in 2018, I was reading the official Hobo Web site while commuting, on the metro, bus, at work, or the gym. The clarity and depth of information there kept me going, especially after losing over 3,000 websites due to the August 1st, 2018 Google update… One day, while browsing Hobo Web, I came across a link to SEO by the Sea. I clicked on it and that moment changed my life. Today, I lead a community of over 50,000 members and run a private course with 2,500 students. All of this was made possible thanks to two foundational resources: Hobo Web and SEO by the Sea. That’s why Shaun Anderson and Bill Slawski have always been the lighthouses of my SEO journey.” Koray Tuğberk GÜBÜR @KorayGubur 2025

Shaun Anderson; I also suggest you to follow him. He doesn’t share so much things on Twitter but hobo webco uk is one of the greatest places that you can actually learn real seo and i am not talking about like five quick hacks that you can do or i’m not talking about six shortcuts tips blah blah not these type of idiotic titles they won’t appear there and you won’t have popular seo names here you will have real world research. Boring things but real things and here i have written without I wouldn’t have found my own company. ” – Koray Tuğberk GÜBÜR, 2022

During Lockdown, by the way, dear reader, it was a younger Koray (amongst few others) who even kept me half interested in SEO. I always knew (the basics) of what he legitimately made his name synonymous with, I’m sure: Topical Authority . It has been nice to revisit the topic.

Read on if you want to learn SEO the same way I did, starting back in 2000. It’s the path that experts like Koray Tuğberk GÜBÜR and so many others followed, all of us learning from the late Bill Slawski and other SEO legends. For nearly 20 years, I’ve had the pleasure of documenting this approach on the Hobo SEO blog.

For those 20 years, SEO has been an art and science (I use that term loosely) of inference, a practice of observing the shadows on the cave wall to deduce the shape of the object casting them.

SEOs like myself pored over every cryptic clue from Googlers who would throw a bone to those who could listen and think critically – I mean, no wonder !

But the landmark combination of sworn testimony from the U.S. Department of Justice v. Google trial and the accidental publication of Google’s internal Content Warehouse API documentation has transformed the black box into a blueprint .

For practitioners like myself who have spent 25 years working from the evidence available, this moment is nothing short of a Rosetta Stone; it provides the canonical, engineered reality behind the theories we have carefully constructed.

These revelations have given us the foundational data object for every URL in the index: the CompositeDoc .

This “master record” is the top-level protocol container that aggregates all known information about a single document.

Nestled within it is the most critical component for strategic analysis, the PerDocData model – what I’ve come to call the comprehensive “digital dossier” or “rap sheet” that Google maintains on every URL it indexes .

Understanding this architecture is no longer an academic exercise; it allows us to align our strategy directly with the core logic of the index itself.

This article deconstructs this newly visible architecture, revealing a fundamental, engineered split between two core evaluation systems.

By dissecting the specific, measurable attributes that feed these systems, this report provides a definitive, evidence-based framework for mastering Topical Authority by systematically building a perfect CompositeDoc that excels at every level of Google’s evaluation.

Google’s ranking is not a single, monolithic algorithm but a sophisticated, multi-stage pipeline that interrogates the CompositeDoc and its nested PerDocData module for every URL.

This process is engineered to answer two fundamental questions that form the bedrock of search quality: “Is this document trustworthy?” and “Is this document relevant?”. The answers are calculated by two distinct, yet interconnected, macro-systems: the Authority System (Q*) and the Relevance System (T*) .

This system assesses the inherent, query-independent authority of a website. It is the modern, continuously updated evolution of the site-level quality assessments pioneered by the Google Panda update .

Q* is a slow-moving, persistent reputation metric that acts as a foundational quality score for a domain and its pages.

The public-facing name for the enforcement of these principles is the Helpful Content System (HCS) , but the underlying machinery is the Q* system. E-E-A-T is not a single score but an emergent property of the dozens of granular signals that make up a site’s Q* profile, which are now, for the first time, visible to us.

At the very heart of the Q* system is a baseline quality and trust score known as predictedDefaultNsr , or Normalised Site Rank .

This attribute functions as the default quality assessment for a URL, a head start (or handicap) granted before it has even had a chance to accumulate extensive user engagement data. Crucially, the documentation defines this attribute as a VersionedFloatSignal, a technical detail with profound strategic implications.

The term VersionedFloatSignal explicitly confirms that Google does not just store a page’s current quality score; it maintains a historical record of that score over time.

This transforms a static quality snapshot into a time-series dataset.

Consequently, a site’s quality trajectory – whether it is consistently improving, remaining stable, or declining over months and years – becomes a powerful meta-signal in its own right.

This creates what can be described as “ algorithmic momentum “.

A website with a long and consistent history of high-quality signals, as recorded in its versioned predictedDefaultNsr, builds positive momentum.

This acts as a tailwind, making the site more resilient to minor quality fluctuations and algorithm updates, and significantly harder for newer competitors to dislodge.

Conversely, a site with a history of low-quality signals carries a negative momentum that must be overcome through sustained, long-term investment in quality .

This technical reality confirms that SEO is a long game; short-term tactics are strategically flawed because they fail to build the positive historical trajectory that underpins algorithmic trust.

The Q* system contains a suite of specialised signals designed to provide a multi-dimensional view of a page’s content, evaluating it based on the effort of its creation, its originality, and its fundamental integrity.

For years, E-E-A-T has been discussed as an abstract concept for human raters. These leaked attributes reveal the engineered components Google uses to translate that framework into a scalable, machine-readable system.

Optimising for E-E-A-T is therefore no longer a conceptual exercise; it is about creating content that demonstrably scores well on these specific, measurable attributes.

Google’s assessment of freshness is far more sophisticated than simply reading a publication date. The leak confirms a nuanced system designed to reward genuine content improvement while resisting manipulation.

These signals feed into re-ranking systems called “ Twiddlers .”

Specifically, the FreshnessTwiddler is a re-ranking function that boosts timely content for queries that deserve it.

First, an update must be “significant” enough to trigger the lastSignificantUpdate signal .

Second, that signal only provides a ranking benefit when the query is one that Google has identified as deserving fresh results (a concept known as QDF, or “Query Deserves Freshness”).

The strategic imperative is not to update everything constantly, but to identify QDF-sensitive topics and focus significant update efforts there.

Google’s understanding of topics has evolved far beyond keywords to a mathematically precise model of concepts and their relationships. This is the technical foundation of Topical Authority.

These attributes confirm that “Topical Authority” is not an abstract concept but the measurable outcome of a mathematical calculation.

A site demonstrates topical authority by achieving a high siteFocusScore and ensuring that all of its important content has a low siteRadius .

This makes actions like pruning or improving off-topic content a direct and measurable way to strengthen a domain’s calculated authority.

The leaked Google documentation has confirmed that “Topical Authority” is not an abstract concept but the result of a precise mathematical model.

This system evaluates a website’s content to determine its thematic focus, but it’s crucial to understand that this calculation is distinct from the assessment of its overall quality and trustworthiness.

The foundation of this topical analysis rests on a few key attributes, primarily siteRadius , siteFocusScore , and the underlying site2vecEmbeddingEncoded technology.

The easiest way to understand these concepts is through an analogy: think of your website as a solar system.

We can visualise different states of topical health using this framework using marbles. The green areas represent content with a low siteRadius (close to the core topic), while orange and red represent content with a high siteRadius (topical outliers).

Perfect Topicality : The ideal for a niche authority site. It would have a very high siteFocusScore because every single page has a low siteRadius . All the pages are related. Google will be sure what your next article is going to be about.

High Focus with Topical Drift : A common state for a strong site that has a few off-topic posts. These outlier pages have a high siteRadius and, if numerous enough, can begin to lower the overall siteFocusScore . Trim off-topic pages from the site unless they are picking up high-quality links.

Generalist Site with a Niche Core : This site has a core of expertise, but it’s diluted by a large amount of tangentially related content with a high siteRadius . This wide radius of content significantly lowers the overall siteFocusScore . These sites do not look like the niche sites Google wants for a lot of keywords. A site whose pages perform poorly for everything ranks for nothing.

Fragmented Authority : Represents a site trying to be an expert in two distinct topics. This creates a confusing mathematical identity ( site2vec ) and a low siteFocusScore , as there is no single “sun” for the system to orbit. This could be a hack, or someone in your office linking your site to their gambling sites (I jest), or you suddenly publishing completely off-topic content.

The visual metaphor can also be extended to page quality or link building.

If you don’t have the authority, you would do well to focus on your own topic of expertise in future.

And go deep! There is an infinite content data layer crammed with information with your name on it. Really.

I call it the Infinite Synthetic Content Data Layer , and I call the art of mining it “ Inference Optimisation “.

A common mistake is to equate a high siteFocusScore with a high-quality site. These are two separate assessments.

The New York Times is a perfect example. It’s a pinnacle of site quality in Google’s eyes, with immense authority and trust. However, it is a generalist site, not a topically focused one. It covers hundreds of subjects. Its site2vec pattern is that of a “trusted major news portal,” which is a known, high-quality pattern, but it would not have a high siteFocusScore in the way a niche site would.

Conversely, you could create a website entirely focused on a single, obscure topic. Every page could have a very low siteRadius , resulting in a nearly perfect siteFocusScore . However, if the content is thin, untrustworthy, and has no backlinks, Google will still see it as a very low-quality site.

While focus and quality are measured separately, a severely confused topical structure can indirectly harm your site’s perceived authority. Google’s systems are built on pattern recognition.

They have learned the mathematical patterns of what trustworthy sites in various categories look like.

A site with a strange topical mix – like a blog that is 50% about vegan baking and 50% about heavy metal repair – becomes a mathematical outlier .

It doesn’t fit the known pattern of a trusted food blog or a trusted industrial repair site. Because it’s hard to classify, it may be harder for Google to trust, indirectly impacting its ability to rank even for its core topics.

You can extrapolate that particular example to your own niche.

This video was a response to the article you are reading. Its core argument – aiming to “tweak my verbage” – is that “Topical Cohesion” is a practical, designable SEO strategy that is more effective and controllable than the vague, often misunderstood concept of “Topical Authority.”

The host, Carolyn Holzman , argues that “Topical Cohesion” (which she relates to the terms siteFocus and siteRadius I shared from the Google leak. is the key to signalling relevance to Google’s systems, whereas “authority” is something that is “conferred” by others and cannot be directly built.

I agree with this verbage tweaking so much, I am using it myself in some recent docs . I think it does well to help visualise the difference between topical authority and topical cohesion from a strategic point of view.

A robust suite of attributes forms the “Trust” pillar of E-E-A-T , functioning primarily as a liability model where negative signals can suppress the performance of an entire domain.

Building trust is therefore as much about diligently auditing for and removing these negatives as it is about adding positives.

A comprehensive trust strategy must include regular audits for outbound link quality, on-page ad experience, and other potential trust liabilities across the entire domain.

PageRank is the foundational algorithm that started it all, but its modern implementation is far more sophisticated than the simple idea of “link juice.”

While the core principle of using links as votes remains, the system now deeply integrates concepts of internal site structure, trust, and neighbourhood quality. The leaked documentation gives us specific insight into attributes that are crucial to understanding modern PageRank: onsiteProminence and spamrank .

For years, SEOs have focused on how external links pass authority.

However, the onsiteProminence attribute confirms that Google meticulously maps how authority flows within your own website . To understand this, my metaphor of “Links as Lasers.”

Think of your powerful pages (like the homepage) as power sources .

Your internal links are not pipes that spill water everywhere; they are lasers ⚡ that direct that energy with precision. You cannot point the laser everywhere at once; you must choose your targets.

This confirms that a “flat” site architecture is strategically weak.

It leaves every page lukewarm rather than creating pillars of authority.

The goal is to practice thermal management: identify your most critical pages and systematically heat them up with focused internal links from your most prominent content. And remember. None of this works unless users are clicking on your links. So choose wisely .

When it comes to external links, the focus has shifted from pure volume to trust and relevance . The spamrank attribute is a clear indicator of this, functioning as a “guilt by association” signal. It specifically measures the likelihood that your page links out to known spammy or low-quality domains.

Linking to a disreputable “bad neighborhood” on the web can directly harm your page’s perceived trustworthiness.

Modern PageRank isn’t just a vote; it’s an endorsement. By linking to another site, you are vouching for its quality . If you consistently vouch for untrustworthy sites, Google will start to question your own site’s integrity.

Therefore, a modern PageRank strategy must be defensive as well as offensive

It involves not only acquiring high-quality backlinks but also diligently auditing your outbound links. Curation is key; you must ensure you are a responsible citizen of the web, linking only to other high-quality, relevant resources. This protects your own site’s spamrank score and reinforces its position within a trusted part of the web graph.

In the past, SEOs practised what was known as “PageRank sculpting.” This was the tactic of using the rel="nofollow" attribute on internal links (e.g., links to a privacy policy or contact page) with the goal of preventing PageRank from flowing to those “unimportant” pages, thereby preserving more of it to be funneled to “important” money pages.

However, Google changed how this works years ago. The PageRank intended for a nofollowed link simply vanishes from the calculation for that page. It is not re-assigned to the other links.

Using the “Links as Lasers” metaphor, applying nofollow to an internal link doesn’t make your other lasers stronger; it just shuts one of them off . You’re actively deleting a portion of that page’s expected outbound heat. The modern and correct approach is not to block PageRank flow with nofollow , but to guide it intelligently through your site architecture and manage your onsiteProminence by linking strategically to the pages you want to heat up.

While Q* measures a site’s inherent, slow-moving authority, T* calculates a document’s dynamic, query-dependent relevance.

Sworn testimony in the DOJ trial revealed this system is formally designated as T * and is built upon the foundational “ABC” (Anchors, Body, Clicks) signals .

The Content Warehouse leak provided the codename for the engine that operationalises this process ( which I was credited by Barry Swartz at SERoundtable – the most credible newsman in SEO for many decades) for finding via original research: “ Goldmine “ .

Goldmine begins by gathering a pool of potential SERP titles and relevance signals from various sources.

This directly corresponds to the “Anchors” and “Body” signals described by Google executives in court. The system scores these using internal factors like goldmineBodyFactor and goldmineAnchorFactor. Key sources include:

This process traces its roots directly to the Penguin update , which was designed to target manipulative link-building schemes.

The existence of a specific penalty attribute, anchorMismatchDemotion, confirms this legacy.

This signal actively demotes pages where inbound link anchor text is not topically relevant to the target page’s content, punishing attempts to use irrelevant links to manipulate rankings. Avoid this practice.

Once candidates are sourced, they are passed through an AI quality filter.

The goldmineBlockbertFactor scores each candidate on its semantic coherence and contextual relevance to the page’s content.
