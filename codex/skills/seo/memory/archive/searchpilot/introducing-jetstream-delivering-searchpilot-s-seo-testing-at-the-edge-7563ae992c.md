---
source: https://www.searchpilot.com/resources/blog/introducing-jetstream-delivering-searchpilots-seo-testing-at-the-edge
title: Introducing JetStream: Delivering SearchPilot’s SEO testing at the edge
scraped: 2026-03-25
published_on: 2024-03-21
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

# Introducing JetStream: Delivering SearchPilot’s SEO testing at the edge

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/introducing-jetstream-delivering-searchpilots-seo-testing-at-the-edge
Published: 2024-03-21
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Discover JetStream from SearchPilot: the innovative server-side SEO A/B testing tool that uses edge worker tech to deploy within Cloudflare, with no additions to your web stack.

## Extracted Body
We’ve often heard the question: can we do true SEO A/B testing without introducing any new infrastructure into our web stack?

Thanks to JetStream, our innovative new deployment approach, the answer is YES.

Built using edge worker technology, JetStream means Cloudflare CDN customers can get the green light they need from engineering to start rolling out rapid, revenue-boosting SEO testing programs.

For the techies out there, our edge technology is deployed as a WASM (WebAssembly) binary designed to work with a range of CDNs and built using Go (using a custom compiler). This interfaces with several CDN-specific features as well as our bespoke backend technologies. All of this combines to perform blisteringly fast and efficient SEO testing (quite the coding feat for those who know).

So, let’s delve into what JetStream means for our Cloudflare customers. (And why we’re so excited about it!)

JetStream is part of our continuous work to make our approach engineer-friendly.

For many of our customers, the most challenging part about getting SearchPilot implemented is getting engineering and security teams on board.

The main difference between JetStream and our traditional deployment is that with JetStream, there is no new infrastructure needed. Instead, JetStream sits on the edge without adding new layers to your web stack . It deploys changes at the last entry point between your CDN and your user.

Deploying on the edge means making the most of your existing Cloudflare infrastructure while getting the same SearchPilot platform features you would get from our traditional deployment.

Before JetStream, Cloudflare users with strict data transport policies could not deploy true SEO split testing . With JetStream, they can now run robust SEO split testing on large, mission-critical websites confidently and with ease.

We first built the SearchPilot platform because we saw an opportunity to do SEO better. And as a bunch of innovators and ambitious SEO experts, that mentality remains. We’re always looking for opportunities to make our platform better. That means keeping our customers’ needs - be it SEO teams , engineering and security , or data analysts - front and center.

When we heard that security and engineering teams were telling SEOs they couldn’t do server-side SEO split testing - not if it meant inserting new tech into the web stack, we saw this as an opportunity to do better.

So, we took the ‘can’t do’ hypothesis and put it to the test. My team and I tested, tweaked, tested, optimized, and tested again using edge worker tech. And now, with JetStream making use of tech already in a site’s web stack, we’ve made the impossible possible .

JetStream is an alternative deployment method for what is already a robust and powerful platform. No matter how you deploy SearchPilot, it helps you run large-scale SEO experimentation programs that deliver statistically significant results and attributable ROI.

By delivering server-side testing on the edge for Cloudflare CDN users, JetStream makes it easier to satisfy security teams, makes deployment a dream, supercharges site speed, and enables indefinite scalability.

As we’ve said, one of the biggest obstacles we’ve seen for SEO teams is the big, red ‘no’ from engineering or compliance. No new layers in the web stack. Period.

Traditional SearchPilot deployment already has incredibly robust failover and resilience in place. But it’s often not about the detail - some teams may have a blanket policy that prevents our standard deployment approach.

With JetStream, there are no new layers to integrate . When a website user makes a request, it goes through the typical chain via your CDN directly to the origin server. Then, just before HTML is returned to browsers, the edge worker code executes and implements the SEO experiment. And if anything goes wrong, the CDN still serves the page normally, without changes.

Deployment can be another sticking point for SEO teams trying to get their testing program running. While SearchPilot is robust and easy to use, initial deployment is subject to engineering sign-off.

With JetStream, you simply authorize our platform to automatically set up and install the worker into your Cloudflare account. Then, when you are ready to go, you activate it. You can get your program up and running quickly with virtually no effort from engineering. (Good for you and good for them too!)

Plus, the deployment remains completely under your control in your existing Cloudflare admin console, which will be music to both engineering and compliance teams' ears.

Here at SearchPilot, we pride ourselves on our minimal impact on your site speed. We’ve done some very clever coding to make our platform super fast. It’s so good that it’s survived the scrutiny of many a diligent enterprise engineering team .

JetStream can do even better. With native integration into the Cloudflare CDN, we are not only able to match the speeds we get with our regular deployments - we’ve improved on them .

One of the benefits of powerful CDNs like Cloudflare is their ability to cache HTML in their edge network and deliver it lightning-fast to users.

By integrating using edge workers, JetStream can be “cache aware” and run server-side CRO tests while still caching HTML.

For SEO teams, high traffic is, of course, a blessing. But it can also be a curse. The greater the volume, the more server resources you need to scale your SEO experimentation program.

JetStream uses your CDN’s scalability to manage traffic. This means ambition becomes the only limit to your high-traffic, large-scale testing programs.

JetStream is available for Cloudflare users now. We’re excited to work with all of you out there who have been waiting for a way to do SEO A/B testing that gets the green light from strict security and engineering policies.

Want to dive into the future of SEO testing? Speak to a member of our team today and join the innovation revolution in SEO.

P.S. For those of you excited to be part of the edge worker world, but who aren’t on Cloudflare, we say: good things come to those who wait . We are working with other CDNs to enable our CDN-agnostic edge worker code to work effectively for you, too.

Get in touch and tell us which CDN you want to see JetStream available for next.
