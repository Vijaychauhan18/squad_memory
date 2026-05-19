---
source: https://www.searchenginejournal.com/interview-with-gary-flake-of-yahoo-labs/622/
title: Interview with Gary Flake of Yahoo Labs
scraped: 2026-03-23
published_on: 2004-06-07
tags: live_feed, phase1_ingest, search-engine-journal, searchenginejournal, publication, industry-news, archive_backfill, historical_source
topic: industry_news
intent: monitoring, research, source_selection
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Search Engine Journal
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Interview with Gary Flake of Yahoo Labs

Source: Search Engine Journal
Homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/interview-with-gary-flake-of-yahoo-labs/622/
Published: 2004-06-07
Strength: broad SEO coverage, platform updates, practitioner commentary

## Summary
20 Questions with Gary Flake, Head of Yahoo Research Labs An interview in the ROTW space this time around. Dr. Gary Flake, Principal Scientist & Head of

## Extracted Body
An interview in the ROTW space this time around. Dr. Gary Flake, Principal Scientist & Head of Yahoo! Research Labs, was kind enough to answer 20 questions for this email interview. This is a “must read” for those of you interested in web search and online information retrieval.

The interview is posted in two parts. Part I begins below. Part II of the interview is NOW AVAILABLE on ResourceShelfPLUS.

ResourceShelf: Dr. Flake, can you tell ResourceShelf about your background in IR and web search?

Gary Flake: Like a lot of people in this industry, my background is in machine learning. In the late 80s, I was working on what can now be best termed as “toy” problems relative to today’s scales. In the early 90s, I started working on larger data mining problems (at first from the biomedical domain, and then later on in industrial processes). Things seemed to get much more interesting with more data, so it was natural for me to switch to the Web and IR because that was where some of the most interesting data could be found.

RS: How many people do you have on your team at Yahoo Research? How do you decide on what new products or services to work on? What’s a typical day like?

GF: We have a couple dozen full-time members of Yahoo! Research Labs (YRL), and a significantly larger number when you consider the extended R&D family within Yahoo! that includes folks from the individual business units (BUs). While those two sets of researchers collaborate as often as possible, the focus of the full-time members of YRL is on areas that can impact the whole of the company, while the BU scientists focus more on problems specific to a BU.

How we pick what activities to pursue is a long story (and partially a function of my own history within industrial R&D), so please tolerate the longish answer to this question.

In general, YRL’s mission is to produce reusable R&D results, explore areas that fall between the cracks (i.e., between BUs), and look for — or perhaps produce — R&D results that could disrupt the industry. Steering the activities of a group with this sort of mission requires that one take a very holistic view of R&D and see the value of diversity. By this, I mean we explicitly choose to do a lot of things in vastly different ways. We work on short, medium, and long term projects. We have activities initiated by a scientist or engineer, but we also have some efforts which are done in response to an executive goal. We work on fundamental algorithms (occasionally producing deep theoretical results), but also ground our efforts to business problems. We also work on individual products, infrastructure improvements, or even business strategy.

The point of all this is that we mix it up. Done incorrectly, prioritizing all of these seemingly conflicting objectives could produce mediocrity. However, with the right blend, one often finds that there is a subtle interplay among these objectives that often yields something wonderful. My job is to keep the mix as interesting as possible, which requires that I look for what’s missing. If activities within YRL are chaotic, I’ll wear my dictator hat until things become less chaotic. If activities seem too focused or top-down, I’ll encourage some short-term anarchy.

That’s the philosophical answer that ignores the content of R&D. If we consider the content of the work, then my own preference is to look for activities that are eminently reusable (i.e., applicable to multiple BUs, so that we get more bang for the buck). I also believe that all of our efforts have to be interesting on either a scientific, mathematical, engineering, product, or strategic yardstick. The very best activities will be significant along all of those dimensions. For example, machine learning and data mining are both off the chart because both have high value no matter how they are evaluated, and a single result may be applicable to multiple BUs.

Typical day? I haven’t had one of those in a long time. In a typical week, I’ll make a trip or two, dissect code, brainstorm with product and business teams, indulge in some discussions with YRL members (which is like oxygen to me), read as much as possible, receive hundreds of emails (and write a few too), all while trying to balance and prioritize the team’s efforts in a rational way. The balancing part is perhaps the most subtle and important.

GF: It’s easier for me to point to what web search should be and then highlight the differences. If web search were perfect, then it would produce an answer to every query that would be as good — or better — than if the smartest people in the world had as much time, data, and contextual information (about the user) required to fulfill the query; and it would do all of this in a split second. In other words, the search engine would be an artificial intelligence (AI) so smart that if a correct answer could be found in theory with close to infinite resources, then it would find it. If a correct answer did not exist, then the search engine would give you the next best thing: an approximation, or perhaps even an explanation as to why your query has no perfect result. (And by the way, if we realized all of the above within my lifetime, I would consider myself lucky. That should give you an idea of what sort of time frame I am talking about.)

Alternative interfaces, like cell phones, voice, and snazzy graphical results are all nice, but in the end they represent relatively easy technology problems when compared to the challenges involved in realizing our hypothetical search engine. What really matters is what is under the hood.

Today, search engines have almost no understanding of words or language in any significant way. They exploit the statistical properties of words and links, but in no way is there anything going on akin to understanding. Search engines don’t recognize user intent, can’t distinguish goal-oriented search from browsing search, and are completely ignorant of the subtleties of how different concepts relate to one another. Moreover, they completely lack wisdom — i.e., they are very poor at distinguishing between trivia and something profound.

RS: Do you still see a need for targeted crawlers and focused databases?

GF: Certainly. Different types of data have different notions of timeliness. Moreover, besides structured and unstructured data, there is a whole universe of data best characterized as semi-structured. As long as those two observations hold, niche tools will always fill a niche, to coin a tautology. I don’t think a huge monolithic database will ever subsume all other databases. Instead, what we think of as a search engine will gradually evolve into a more subtle meta-search engine, blending its own data with other sources.

GF: Getting at the heart of user intent is very important to us and to the overall search team, with whom we work on a daily basis. I think this is how we will make the most impact in the short to medium term. I also think that current search engines have only scratched the surface on what can be done with link data. The commoditization of 64-bit hardware will also change the search engine landscape, and we intend to push on this front as well. Our long-term goal is to get as close as possible to what I described earlier as a perfect search engine. We are far, far from that goal. But that’s okay, too, because we know some of the next key steps towards realizing the larger goal.

RS: What’s your feeling about trying to place structured data like a library catalog/bibliographic record or an indexed article into an unstructured database? Asked another way, what’s the role of structured data in an unstructured web world? How can we bring both types of resources together and still allow users to take advantage of all of the additional access points that a structured database and its retrieval mechanism make available?

GF: The beautiful thing about a relational database is that its structure tells you a lot about what is important. Database designers have been brilliant at optimizing databases (both the organization of the information as well as the algorithms) to best exploit this regularity. When you flatten out a database, those paths towards optimization often aren’t available.

A middle ground — which is not perfect, but adds a lot of utility — is to convert structured into a semi-structured form. Today, we treat documents as a big bag of words and index those words. In this semi-structured approach, we take structured information (say, the value of specific fields) and synthesize fake words that represent the fact that “document X has field Y with value Z.? Now, clearly I can’t run a SQL query on this representation; but at least I can search for documents with specific field:value pairs.

I’d like to tell you that we will be able to make an unstructured database as powerful as a structured database; but that simply is not the case. Nonetheless, the fusion of structured and unstructured data and approaches will add a lot of utility to the lives of most users.

In parallel to the above, we have started on a different approach through the launch of our Content Acquisition Program, working with such partners as NPR and the Library of Congress, as well as with universities such as Northwestern, UCLA and University of Michigan — all so we can bring their structured data to a larger audience.

Gary Flake ANSWERS 14 more questions in Part II of the the interview on ResourceShelf.
