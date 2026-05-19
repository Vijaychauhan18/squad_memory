---
source: https://www.onely.com/blog/webassembly-experiment/
title: WebAssembly: What It Is, and Can Google Deal With It?
scraped: 2026-03-23
published_on: 2020-04-07
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# WebAssembly: What It Is, and Can Google Deal With It?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/webassembly-experiment/
Published: 2020-04-07
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Read the newest posts on our blog to make sure you're not missing out on anything!

## Extracted Body
On December 5, 2019, the World Wide Web Consortium declared WebAssembly (abbreviated WASM) a web standard. It joined HTML, CSS, and JavaScript as the fourth language natively supported by web browsers.

JavaScript completely changed the way modern websites are built, giving webmasters tons of possibilities. But, it has its limitations.

Many websites have trouble with Google not indexing their content generated using JavaScript. As our research and indexing tool, ZipTie , shows, JavaScript is often indexed with significant delay when compared to content written in HTML. And, in some cases, JavaScript content is not read by search engines at all.

More importantly, though, JavaScript is slow in terms of its execution. Time is money. We want everything to work as quickly as possible, and for that, we need appropriate tools. That is why the technologies we are using to build the web are constantly reexamined.

JavaScript is a high-level language (easy to read and understand for humans), compiled Just-In-Time. It means that the code is transformed to be understood by a machine exactly at the moment of execution.

The more JavaScript code is used by a website, the more time and computing power is needed to run it.

The graph below presents a simplified JavaScript processing procedure that is implemented in Google Chrome.

Are you using JavaScript on your website? Check how we can help you with our JavaScript SEO services .

As you can see, JavaScript code execution is a lot of work for computers. This is where WebAssembly [WASM] comes into play.

The biggest difference between JavaScript and WASM is that the latter is served to users as a machine code that has been previously interpreted and optimized (these operations require the most computing power).

This results in a significant shortening of the previously presented chain of execution. The WASM code is combined with the JavaScript code (in the form of machine code) and then run. There are many experiments and tests that confirm the advantage of WASM over JavaScript in terms of performance (with certain types of calculations).

Many programming languages, like C, C++, C#, Rust, or Go, can be compiled into WASM format. In other words: you can create an advanced desktop application in your favorite language, and then transfer it to the web with just a little effort.

let current_datetime = new Date(); document.getElementById(‘datetime’).innerText=”Today is ” + current_datetime.toString();

And there’s more. WASM can use CPU power more efficiently than JavaScript (e.g., thanks to SIMD – Single Instruction, Multiple Data architecture support), and in the future, it may even gain access to the GPU.

Thanks to WASM, it was possible to create full browser versions of large applications like AutoCAD or Doom 3 (yes, WebAssembly is a huge opportunity for online browser games!). Here are two interesting examples of WASM put into practice.

WebAssembly is currently under intense development. Further performance improvement is only a matter of time. JavaScript is already 25 years old, but after the sudden boom in the early 2000s, it only took a few years for it to dominate web development.

Will history repeat itself with WASM? It is difficult to say. WASM is a great improvement for web applications that require high computing power. Will anyone decide to generate other types of content using WASM? Maybe, which is why it’s worth knowing if Google is able to process it.

Since May 2019, Googlebot has been using the latest version of the Chromium engine, and therefore the latest version of the V8 engine responsible for processing JavaScript. In the browser of a user, it’s the JavaScript engine that’s responsible for running WASM modules. Does this mean that Google is now also able to run the WASM environment? I decided to see for myself by creating a simple experiment .

I built test pages with content generated using modules written in C, compiled into WASM with the help of the Emscripten chain, and then imported onto the site using JavaScript.

The test results show that Google has no technical problems with running WASM modules and reading the content generated by them. The page text has been fully indexed, and Google found links to subpages with no effort.

However, you should keep in mind that WebAssembly isn’t equipped with the right tools to directly manipulate DOM elements yet. This means that you still need to use “glue code” written in JavaScript, which acts as a bridge between the structure of the site and the WASM application.

Therefore, WASM is burdened with JavaScript SEO issues . As our research has shown, the amount of JavaScript code and the computing power required to process it have an impact on the indexing process. That’s one of the reasons why performance is such an important aspect of SEO.

Does WASM have a big impact on SEO? The best answer is… it depends.

Webpages are, in essence, paragraphs of text with pictures. With WASM, generating text is not as simple as you may think. This is because strings are not natively supported. A WASM application can “communicate” with the rest of the website only by using blocks of memory.

For example, let’s say you generate a simple “Hello World!” inside your shiny, super-fast WASM module. Then you need to write that text into memory, character by character. The next step is to read those characters with JavaScript code. You need to know exactly where in the memory those characters are stored and what is the size of each character. After JavaScript reads everything, it needs to combine those separate characters back into a full string of text. Last but not least, your text needs to be placed somewhere inside the Document Object Model.

For now, JavaScript is a faster and more convenient tool than WASM when it comes to generating usual web content, such as paragraphs of text. But after all, JavaScript was initially used primarily to improve the visual layer (drop-down menus, animations…) of websites built primarily with HTML. Now it is often used for generating main content. There are tons of JavaScript frameworks. Soon, we might see some WebAssembly frameworks.

WebAssembly is a relatively new technology, even by IT standards. The process of building modules is not perfect yet. Modules are quite large, and loading them on a website is slow. Therefore, you should consider whether in the era of the increasing importance of web performance using WASM is the right approach. Will this new technology speed up the key operations on the website so much that it will offset the costs of using it? Every improvement we make on the website should be aimed to improve the user experience.

WebAssembly is a very interesting topic and it is worth following the development of this technology. As it’s being improved, it might happen that WASM will change the internet as we know it, just like JavaScript did.
