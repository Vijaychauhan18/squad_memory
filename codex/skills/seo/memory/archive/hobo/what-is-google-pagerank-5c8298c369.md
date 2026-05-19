---
source: https://www.hobo-web.co.uk/google-pr-update/
title: What is Google Pagerank?
scraped: 2026-03-23
published_on: 2013-12-06
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

# What is Google Pagerank?

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/google-pr-update/
Published: 2013-12-06
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
Question: Does Google still use PageRank? Answer: Yes. Evidence: "A key quality signal is PageRank"

## Extracted Body
QUOTE : “ A key quality signal is PageR ank, which captures a web page’s quality and authoritativeness based on the frequency and importance of the links connecting to it . Id. at 2795:19–2797:21 (Allan); PXR0356 at -744 (“PageRank. . is a single signal relating to distance from a known good source, and it is used as an input to the Quality score.”). justice.gov, 2025 . PageRank was a key early innovation that separated Google from the competition and is now “widely known.”Rem. Tr. at 2795:19–2796:25(Allan). Concededly, some of Google’s quality sub-signals are scale dependent. Seeid. at 2802:5-8(Allan)(discussing RDXD-20.022);id.at2875:10-15 (Allan). But they are the exception, as Plaintiffs seemed to acknowledge when questioning Google’s expert in computer science and information retrieval, Dr. James Allan. See Rem. Tr. at 2875:10-11 (“Do you understand that most of Google’s quality signal is derived from the webpage itself?” ). UNITED STATES OF AMERICA et al v. GOOGLE LLC, No. 1:2020cv03010 – Document 1436 (D.D.C. 2025) Justia, 2025

Google’s original PageRank algorithm, developed by Larry Page and Sergey Brin at Stanford, assigns an importance score to each webpage based on the web’s link structure.

The basic idea is that a page is considered more important if many other important pages link to it .

As Google’s early patent (Lawrence Page, U.S. Patent 6,285,999) explains, “ a document should be important (regardless of its content) if it is highly cited by other documents . Not all citations, however, are necessarily of equal significance.

A citation from an important document is more important than a citation from a relatively unimportant document… [Thus] the rank of a document is a function of the ranks of the documents which cite it.” patents.google.com

In practice, the PageRank of a page A is defined recursively:

r(A)=1−dN + d∑i=1nr(Bi)L(Bi), r(A) = \frac{1 – d}{N} \;+\; d \sum_{i=1}^{n} \frac{r(B_i)}{L(B_i)} ,r(A)=N1−d​+d∑i=1n​L(Bi​)r(Bi​)​,

where B1…BnB_1 \ldots B_nB1​…Bn​ are pages linking to A , L(Bi)L(B_i)L(Bi​) is the number of outgoing links from page BiB_iBi​, N is the total number of pages, and d is a damping factor (usually set around 0.85): patentimages.storage.googleapis.com and snap.stanford.edu .

In other words, “the ranks form a probability distribution over web pages, so that the sum of all Web pages’ PageRanks will be one,” and the rank of a page can be interpreted as “the probability that a random web surfer ends up at the page after following a large number of forward inks.”: patentimages.storage.googleapis.com

Because a random surfer occasionally jumps to a random page with probability (1– d ), even pages with few links can get some baseline rank.

This elegant link analysis makes PageRank an objective measure of a page’s citation importance.

As Brin and Page noted in their 1998 research paper, “PageRank…corresponds well with people’s subjective idea of importance. Because of this correspondence, PageRank is an excellent way to prioritise the results of web keyword searches.”: snap.stanford.edu

How it was used: In Google’s early search engine, PageRank was a core ranking signal used to “prioritise” or weight search results. Google even had Google Toolbar Updates back in the day.

Pages with higher PageRank (i.e. more or better-quality backlinks) tended to rank higher in the “10 blue links” results, all else being equal.

PageRank was computed offline by iteratively propagating link weights, and Google updated these scores periodically.

By the early 2000s, Google even exposed a rough 0–10 PageRank score via the browser Toolbar, underscoring how central it was to ranking.

Importantly, even from the start, Google recognised that PageRank was one signal among many – it improves relevance when combined with content-based scoring.

Nonetheless, it became the foundation of Google’s ranking, embodying the principle that “links…are votes of support” and that pages “endorsed by many high-quality sites” should be ranked as more authoritative.

Google’s original ranking algorithm, PageRank , assigns each page a numerical importance score based on backlinks. In Larry Page’s original formulation , a page’s rank is calculated from the ranks of other pages linking to it. PageRank is query-independent — it condenses the entire web’s link graph into a “global ranking of all web pages, regardless of content, based solely on backlinks” as described in Google’s patent documentation .

Early Google engineers recognised that even low-quality pages contributed a minimum PageRank value, meaning that creating many interlinked dummy pages could artificially inflate a target page’s score ( source ).

To counter this, Google later refined its patents to apply weighting to links from domains containing many pages ( see patent updates ). Despite these adjustments, PageRank continued to serve as a core foundation of the modern ranking system, as outlined in Go Fish Digital’s analysis .

Several SEO analysts recognised PageRank’s central importance – and its weaknesses. As early as 2007, Jim Boykin discussed “old BackRub techniques with some TrustRank thrown in,” acknowledging that Google’s ranking model was still rooted in link votes.

The late Bill Slawski extensively analysed Google’s link algorithms and noted the vulnerability of PageRank to spam farms and reciprocal “endorsement” loops.

He highlighted that many low-value links could still elevate a page’s rank because “every linking page is guaranteed to have a minimum PageRank… links from many such low-quality pages can still inflate the PageRank score” ( Google patent reference ).

Slawski also drew attention to Google’s efforts to combat manipulation – such as the “reasonable surfer” model, which gives different weights to links depending on how likely users are to click them ( technical details here ). Around that time, we described PageRank as a measure of link-derived authority – “ the rank assigned to a document is calculated from the ranks of documents citing it” – a principle that Google itself defined in its own materials .

Bill often compared backlinks to votes or peer reviews , echoing Google’s own explanation that PageRank uses “information external to webpages — their backlinks — which provide a kind of peer review. Backlinks from ‘important’ pages are considered more significant… by recursive definition” ( Google patent reference ).

This idea of “link votes” mirrored Google’s internal philosophy. In my own practical guides, I stressed that “Google has long worked by displaying organic results based on keywords and links” – reinforcing that link authority, or PageRank, still underpins modern ranking outcomes.

Looking back, those early interpretations were remarkably accurate . PageRank truly became the foundational ranking factor within Google’s system, and the advice to acquire high-quality backlinks was prescient.

Bill Slawski’s early warnings about link spam predicted the very manipulative tactics Google would later fight internally ( documented in its patents ). Although many additional signals have since been integrated into Google’s algorithm, evidence presented during the 2023 DOJ trial confirmed that PageRank – or evolved derivatives of it – remains an active component of search ranking today.

As the web expanded, link spam – artificial link networks or “link farms” – began undermining the reliability of Google’s original PageRank system.

In response, researchers (including some who later joined Google) developed TrustRank , an evolution of PageRank that emphasizes trustworthiness over raw link popularity.

A Google patent on link-spam detection defines TrustRank as “a link analysis technique related to PageRank” and “a method for separating reputable, good pages on the Web from web spam.” It works on the principle that good websites seldom link to spam sites .

TrustRank operates in two steps: first, human experts identify a small seed set of highly trustworthy pages; second, a propagation algorithm spreads a trust score outward through the web graph. As the patent notes, “TrustRank involves two steps, one of seed selection and another of score propagation. [Thus] the TrustRank of a document is a measure of the likelihood that the document is a reputable (i.e., non-spam) document.”

Google implemented this concept internally to downweight webspam and elevate authoritative content. Rather than counting all backlinks equally, links from trusted seed pages carry greater value — effectively running a biased PageRank that starts from verified, reputable nodes.

A later Google patent describes “select[ing] a few ‘trusted’ pages (also referred to as seed pages) and [finding] other pages likely to be good by following the links from the trusted pages.” By crawling outward from this set of high-quality seed pages and measuring link distance (the number of hops or weighted path length), Google can calculate a trust score for each page based on its proximity to trusted sources.

Pages closely linked to the trusted seeds earn higher trust scores, while those further away — or connected mainly through untrusted links — are considered less reliable.

This distance ranking approach, patented by Google, reduces the influence of spam farms: “good documents on the Web seldom link to spam,” and therefore spam pages naturally end up many link-hops away from the reputable core .

In practice, Google can use TrustRank to demote or filter pages with high PageRank but low trust. One Google filing even notes that the system may compute a discrepancy between link-based popularity (PageRank) and trustworthiness (TrustRank) to identify artificially boosted pages.

In essence, a page with many backlinks may still rank poorly if those links come from low-trust sources .

By the late 2000s, Google’s ranking algorithms had begun to incorporate such link quality assessments alongside link quantity, reinforcing the enduring principle that not all links are equal .

Usage: TrustRank (and related “link distance” signals) are believed to operate internally as part of Google’s ranking and anti-spam frameworks. While Google has never publicly branded the system “TrustRank,” several Google patents and research papers describe the method of using a seed set of reputable documents whose trust values are propagated through the link graph to influence overall ranking.

In summary, TrustRank evolved PageRank by introducing a crucial layer of link reliability , ensuring that a page’s ranking reflects not only the number of its backlinks but also the trustworthiness and quality of those linking sources.

Bill Slawski closely followed Google’s developments around trust. He noted that “Google TrustRank is very different from Yahoo’s TrustRank… Yahoo’s TrustRank identifies spam, whereas Google developed a system for reordering rankings of web pages based on trust signals” ( source ).

Years before Google’s trial revelations, Slawski discussed patents describing how trusted seed sites could influence rank. In one such patent, “the system assigns lengths to links, computes the shortest distances from seed pages to each page, and determines a ranking score based on those computed shortest distances.” In simpler terms, Bill explained that pages closer – in link hops – to authoritative or trusted sites would rank higher, encapsulating the essence of TrustRank as a measure of “distance from authority sites.”

Slawski explicitly connected Google’s trust metrics to what he described as the “distance between documents.” He highlighted that Yahoo’s TrustRank “diminishes with increased distance between documents” and depends on carefully selected seed sets ( further reading ). Google appeared to mirror this approach, as evidenced by a 2019 analysis by Slawski showing a patent for ranking pages based on how “close or distant” they are to trusted seed sites.

This “seed set distance” metaphor became Slawski’s shorthand for translating Google’s internal ranking logic into SEO-friendly terms. I often discussed “authority” in similar language — echoing both Slawski and Jim Boykin – and recommended acquiring backlinks from .gov , .edu , or established community hubs to convey trust, a strategy fully aligned with Google’s evolving TrustRank principles.

Bill Slawski (RIP) effectively reverse-engineered Google’s thinking through meticulous patent analysis. He identified that Google aimed to compute a “trust score” to combat low-quality or spammy results. This intuition was confirmed when Pandu Nayak revealed that Google added an explicit quality/trust metric around 2011 to counter the surge of content farms.

My own emphasis on site credibility, authoritative backlinks, and user trust anticipated what Google would later formalise as its E-A-T principles (Expertise, Authoritativeness, Trustworthiness) . In hindsight, the guidance many of us shared — to “stay close to trusted authorities,” both literally within link graphs and figuratively in reputation — proved remarkably accurate .
