---
source: https://yoast.com/how-to-test-wordpress/
title: How to test WordPress 5.0 -
scraped: 2026-03-23
published_on: 2018-12-07
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

# How to test WordPress 5.0 -

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/how-to-test-wordpress/
Published: 2018-12-07
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Want to test the latest version of WordPress without harming your site? Installing a local test server is super easy, here's how you do it!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

December 6, 2018, is the day we shall remember for the birth of WordPress 5.0 and its new block editor. While we loved the new editor, initially, we advised people to hold off updating to WordPress 5.0 until a more stable release. But now, we’re happy to tell people to move to WordPress 5.0 ! Nevertheless, you should still take the time to thoroughly test the new release and come to grips with the inner workings of the new block editor. Here, we’ll explain how you can easily set up a local testing environment to safely test WordPress 5.0.

We can’t say this enough: always, always, always back up your site! Set up automatic backups using plugins like UpdraftPlus , Blogvault , BackWPup or online tools like ManageWP. Most WordPress-friendly web hosting companies like WPEngine have tools to make and manage backups as well. So, options aplenty — use them!

To test WordPress and its new block editor Gutenberg locally, you need to install a local server. In the old days, you had to download and configure all pieces of this puzzle by hand, making it a tough job for the average site owner. Today, you can install a fine-tuned local server in a matter of minutes and with a minimum amount of clicks. During the installation, you’ll even set up a WordPress site so you can get going quickly.

There are several local server tools aimed at the WordPress user, but we find ServerPress and Local by FlyWheel to be the best and easiest to work with. In this article, we’ll focus on Local by FlyWheel as that has the nicest all-in-one interface, handy SSL support and a unique way to share your local site online.

Go to the Local by Flywheel site and click that big green Free Download button. Choose your operating system, fill in the fields and hit the Get it now button. The package will now download to your computer. Double click on the installer package to install Local by Flywheel on your computer.

After Local by Flywheel is installed on your system, doubleclick it to run the app. You’ll notice it’ll take a while to start all services. After it’s done, you’ll be greeted by a screen with a big green button to create a new site, but hold off clicking that button, though.

Of course, you’re going with the quick and easy option here. But first, you need to get your files, posts, plugins, settings and themes — everything. To do that, you need a full backup of your site. In this case, you’ll use the Duplicator plugin to make an exact copy of your site to your local server. Log into your real site, install the Duplicator plugin from the Plugins directory and follow the instructions.

After installing Duplicator, you can make a new so-called package. A package is a complete collection of every part of your site. You can move this package easily to another server, or a local site like you’re doing here. Duplicator can do a lot of other stuff and we’d encourage you to read up on that.Click Create New and set up the details for the package. Give it a name and browse through the options. For most sites, the default settings are fine. Do give the other options a look-see, though.Hit Next and Duplicator’ll start scanning your site. This can take a little while, depending on how big your site is.Once it’s done, you’ll get an overview of the status — it’s best if everything is green here. If it is, you’re good to go and you can start building your package by clicking the Build button. Building might take a while. After it’s done, you’ll get two files to download. Download the archive package and place it in an easy to find place.

Open the Local by Flywheel interface and simply drag your archive package anywhere in the interface. You’ll see an icon with the text Drop to import site appear. After that, you get a screen asking you to give your new test site a name. After hitting Continue, you get a screen asking you to select a server environment to base your site on. Please choose Perferred unless you want to test in a specific combination of technologies. Done? Click on the Import Site button. Local by Flywheel will now extract the files of your site and set up a new WordPress environment.This process might take a while if you have a big site. After it’s done, you’ll see the Local by Flywheel dashboard of your new site and you are ready log in by clicking on the Admin button. If all is well, you’ll find your real site in tact! Please check if everything is in order before you continu.

Once you’ve verified your old site is working great, it’s time to update WordPress to the latest version. Since WordPress 5.0 is now out, you can update your test environement via the regular update process. Alternatively, there’s a great plugin that can help you test upcoming releases. The WordPress Beta Tester plugin makes it incredibly easy to test the very latest development versions of WordPress, even if they are so-called bleeding edge nightlies.

Find WordPress Beta Tester in the plugin repository, install it and activate the plugin. To test get the latest version of WordPress 5.0, you need to go to Tools > Beta Testing and pick the Point release nightlies. After that, go to Dashboard > Updates and you’ll see that there’s an update available. Hit that blue Upgrade Now button to get started. Eventually, you’ll see that Welcome to WordPress 5.0 screen. That’s all! The WordPress Beta Tester will keep your test site updated to the latest WordPress version.

WordPress 5.0 is now active on your test site and you are welcome to explore it. There’s one thing we need to do, though — install the Classic Editor plugin . With this plug installed everything will become like it was before the release of WordPress 5.0 and you can continue to use the old editor instead of the block editor. At the moment, we’re advising people not to upgrade until WordPress 5.0 is a bit more stable, come January. Even then, we’d like people to install the Classic Editor plugin to minimize the risk of things breaking down. The Classic Editor plugin is available until December 31, 2021.

Of course, you can try this out on your test site as well. Find the Classic Editor plugin in the repository, install and activate it. Go to Settings > Writing and pick one of the two options: replace the new editor with the Classic Editor completely, or use the new editor by default and make the Classic Editor a fallback option.

In need of more insights into the inner workings of your WordPress install? If so, the Health Check plugin might give you what you need. It offers a great overview of everything that is going on on your site and it even has a Troubleshooting Mode that helps you find and fix issues. You can find the Health Check plugin in the WordPress plugin repository.

Now that you’ve set up a complete local copy of your real site, it is time to get testing! Click through your posts and pages, check your theme, find out if all your plugins are compatible, test your meta boxes, shortcodes etcetera, etcetera. Users of page builder plugins should take extra care to check that these plugins are fully compatible with WordPress 5.0 and the new editor.

In addition, the most important thing for you to do is to get acquainted with the new block editor. How does it interact with your content? Are there ways to improve your content with the new possibilities the new editor offers? Maybe there are blocks that help you build your content? Or you might just get a brilliant idea for a totally new block. Everything is possible. Now, go forth and test your site!

A local installation of your site will only get you so far. While you can test how your site looks and works in a local environment, there’s no way to test a WordPress site using a real-world set-up. For this, you need a staging environment. A staging environment is a restricted copy of your site on your server that you can use to test and develop your site. Depending on the setup, you can push changes you make on your staging environment to your live site. Many WordPress-friendly web hosters like Kinsta and Siteground offer an easy way to set up and manage a staging environment.

In addition to setting up a staging environment at a hosting company, or using Duplicator to fix this for you, there’s another option: the WP-Staging plugin . This plugin helps you set up a staging environment right from the WordPress backend.

In this article, you have seen how easy it is to get a local version of your site up and running. If you’ve followed along, you can now go out into the wild and start testing every inch of your site to get ready for WordPress 5.0 and the new block editor. Don’t forget, you should test every major version of WordPress, not just this one. If you want to make testing WordPress an even more integral part of your set up, you can choose to set up a staging environment on your server.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

Staging plugin is tested up to wp 4.9.9. Oh – and thnx for your great information, both this post and your whole blog!!

In trying to set up Flywheel I get an error message that VT-X/AMD-v is not enabled in the bios and is mandatory. I am leery of mucking around in bios and don’t know what to do.

Hmm, not sure what that is all about. There’s a help document on Flywheel’s site, though: https://local.getflywheel.com/community/t/windows-help-im-getting-a-bios-error-about-vt-x-amd-v-during-installation/426

its great wordpress 5.0 very easy to work and secure and move faster!

Thank you for sharing this amazing and informative post which I found really helpful for me. WordPress is an amazing platform to manage our site and content in a prominent manner and that’s why we must go for its efficient and effective version. I was also confused about what version should I choose or how to test the significant one and this post cleared all my doubts.

I just checked out the WP Staging plugin and it feels like the most useful WordPress plugin ever created – for a designer like me who constantly adds new features and redesign sites from time to time. It makes cloning a site pretty simple – I’m so glad I read this article. Thanks again

Yeah, that’s a pretty solid plugin alright. Thanks for reading Sunday!

Wow! looks much easier than I thought. To think I’m just getting to know about Local by Flywheel. – comes really handy. Thanks Edwin.

We care about the protection of your data. Read our privacy policy.
