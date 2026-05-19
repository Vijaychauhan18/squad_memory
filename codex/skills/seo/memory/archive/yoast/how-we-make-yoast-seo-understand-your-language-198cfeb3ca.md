---
source: https://yoast.com/how-we-make-yoast-seo-understand-your-language/
title: How we make Yoast SEO understand your language
scraped: 2026-03-23
published_on: 2019-10-03
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

# How we make Yoast SEO understand your language

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/how-we-make-yoast-seo-understand-your-language/
Published: 2019-10-03
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Find out all about the research and development process for the expansion of Yoast SEO checks for different languages!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

One of the key features of Yoast SEO is the content analysis. The analysis consists of multiple checks that give you SEO and readability feedback on the texts you write on your website. Some of these checks are language-independent. For these, we don’t need to create specific versions for, say, French and English. For others, it is necessary to adapt them for each language. In this article, I’ll explain our research and development process for the expansion of Yoast SEO checks for different languages. You’ll also learn how you can contribute to help Yoast SEO understand your language!

In principle, all of our checks are rule-driven. They consist of analyses that run in the browser. This has the advantage that all user data stays in your local environment and is processed there. There’s no need to upload anything to an external server.

The challenging part of this approach is that we can only operate based on predefined rules. Since we don’t know exactly what texts these rules operate on, we need to make sure to define the rules in advance in such a way to cover all necessary cases.

When adapting an analysis to a new language, we not only need to review linguistic and stylistic rules for that language but also translate them into new text processing rules. This might sound very abstract at the moment, but I’ll provide a concrete example below!

Let’s start with an outline of the kind of research that is needed to create a check in the first place. When reading the following example, don’t worry if you don’t get all the linguistic lingo right away! This is just an example to illustrate the formation of rules. I’ll explain all the terms you need to know.

Let’s take passive voice as an example. In our analysis, we check whether you have too many sentences that contain passive voice . It’s not necessary to know exactly what passive voice is at this point – I explain the necessary points below. However, if you want to know all the ins and outs you can read this article on how to recognize passive voice and why we advise you to avoid it .

Imagine that we’re tasked with creating this check from scratch. We want to give a clear recommendation on a text that someone just wrote. To give such a recommendation, the most important point is to figure out which sentences contain passive voice, and which don’t. As a little sneak peek, here’s an example of a passive sentence.

No idea yet what makes this sentence a passive sentence? Or maybe you do know what makes this particular sentence passive, but can you give a full definition of passive sentences in English? Let’s dive into the issue to discover all the rules and exceptions!

How do we know that the sentence above is passive? And how can we teach our analysis to recognize this, too? To answer the first question, language research comes into play. Going through some dusty old grammar books (or the digital equivalent of it), we can establish the following rule: a passive sentence in English is formed by an auxiliary verb and a past participle. In addition, we learn that the auxiliary always comes before the participle. Well, that’s great for a start! But now you might ask yourself: what’s an auxiliary verb? And what the heck is a past participle? Good questions! Since it’s not really obvious for a human, you can be sure that software doesn’t know, either. But that’s okay since we’ll teach it how to recognize them.

Now that we’ve discovered some grammatical rules, we want to know how we can translate them into logic that our text analysis can operate on. So we do some more research and figure out that an auxiliary verb used for passive voice is basically any form of the verb to be ( was , is , been , etc.). Fortunately for us, that’s a pretty short list. For participles, that looks a bit different. A past participle is a verb form such as loved in has been loved and created in has been created. Basically, any verb can be made into a participle. In this case, a word list isn’t really feasible. It’s better to formulate a more general rule. In its most simple form, the rule could be “find a word that ends in -ed”. Such a rule can be translated into a pattern that we can match with a regex for example. Done! Right? Well, almost…

The general rule we’ve established for discovering participles will cover lots of cases, such as cooked , talked , or invented . It won’t be quite sufficient, however. With only this rule in place, you’d get both false positives and false negatives.

False positives arise when your rule matches things it’s not supposed to match. Our word ending in -ed rule would also result in words such as bed being matched. This isn’t actually a past participle. In fact, it’s not even a verb. So we need to filter out exceptions to the rule. We can do this by creating a list of words ending in -ed that aren’t past participles.

False negatives, on the other hand, emerge when our rule fails to match things that we want to match. Consider irregular past participles such as written , seen , or heard . These don’t end in -ed , so they wouldn’t be found with our rule. Again, we need a word list to make sure to also pick up those participles.

So now we already have one general rule, plus two exceptions. And this example is still an oversimplification. In our actual implementation of this check, there are even more factors that we take into account when determining whether a sentence contains passive voice.

You see that for one check in the analysis, there’s a lot of preceding research that needs to happen before we can start implementing the check in our software. And then that’s only for one language. There’s still all other languages for which we also want to be able to carry out this analysis.

Our plugin already supports quite a few languages to help you write great content in your own language . When adapting a check for a new language, we might be faced with one of two situations:

In the first scenario, expanding a check to a new language might be done after a day or two of research. In the second scenario, it can require just as much time as implementing the check in the first place. The problem is that languages can differ not only in the words they use to express a certain concept – such as passive voice – but also the grammatical constructions they use for it. I’ll provide examples for both scenarios below.

Fortunately, not all assessments need completely new logic when adapting them to a new language. Whenever possible, we set them up to make them as much “plug and play” as possible. An example of an assessment that is relatively easy to adapt to a new language is the transition word assessment. This assessment checks whether a transition word or group of words (e.g., words such as however, to summarize ) from a specific list are present in that sentence. This mechanism is basically the same across languages. To make it work, we just need to supply a list of transition words for a given language, and voilà, it works.

Going back to the passive voice analysis, we see that adapting this check to a new language gets a bit more complicated. Here, we’d need to change quite a bit of logic depending on the language analyzed. In Dutch, for example, you still use auxiliary verbs and participles to express passive voice, but, unlike English, the auxiliary can also come after the participle. In Russian, you can spot passive voice relatively accurately by virtue of the form of the verb alone. So it’s not necessary to look at auxiliaries. So for all these languages, not only do you need different data, but you need different logic to carry out the analyses. This means that you need both, additional research and technical implementation. Just supplying new language data won’t suffice here. You also need to adapt the string processing rules that operate on this data.

We strive to make our readability and SEO analysis available in as many languages as possible. Make sure to check out which features are available in your language .

There are a number of ways to help us expand Yoast SEO functionality for your language! As you saw in the explanation above, some checks can be expanded relatively easily by adding the necessary language data. If you speak a language other than English, you can send in language data using one of our forms . We’ll then review this data and, if possible, implement it. This means that with your help, we can add language-specific Yoast features for your language!

If you’re a developer, you can also directly contribute to our codebase. You can find more detailed instructions in our article on making features available for your language . We’re looking forward to your contribution!

I’m the Product Owner of the Yoast WordPress plugins, where I help shape the strategy and roadmap for tools used by millions of websites around the world. I work closely with UX, engineering, marketing, and other teams to turn ideas into features that help people improve their online presence and reach their audience. Before becoming Product Owner, I was the development lead for Yoast’s content analysis. With a background in linguistics, I was fascinated by the challenge of translating language insights into tools that help people write better content. After more than eight years at Yoast, I’m still inspired by the company’s mission to make SEO accessible to everyone and its strong open-source ethos. I care deeply about product thinking: understanding user needs and building tools that truly help people succeed online.

Yoast is the best tool for SEO optimization on WordPress. I really love this plugin. And thanks for sharing this piece of content as well. It’s really helpful. More power to you the team behind Yoast. Cheers!

I use Yoast SEO for my websites. This is really helpful and really good for SEO. Thank you.

I used yoast seo for my website and it is really good for SEO. Thank for great job !

Maybe I misunderstood, but you told Yoast SEO that all words finished w “ed” are past participles, and then u talk about “bed”, for example, as an exception. But what happens with all the regular verbs in past simple form? (e: yesterday, I finished my homework).

We care about the protection of your data. Read our privacy policy.
