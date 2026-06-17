---
layout: default
title: "Horizon Summary: 2026-06-17 (EN)"
date: 2026-06-17
lang: en
---

> From 201 items, 12 important content pieces were selected

---

1. [New World Model Physis to Open-Source, Led by 22-Year-Old Peking University Student](#item-1) ⭐️ 9.0/10
2. [Chrome Update to Deprecate Ad-Blocking APIs, Ending Current Functionality](#item-2) ⭐️ 9.0/10
3. [Android 17 Released: Mandates Large-Screen Adaptation and Adds AI Integration](#item-3) ⭐️ 9.0/10
4. [Ransomware Group Steals 1TB+ Data from Novo Nordisk, Threatens to Sell After Failed $25M Extortion](#item-4) ⭐️ 8.0/10
5. [Zhipu Releases Open-Source GLM-5.2: Top Code Arena Model with 1M Context](#item-5) ⭐️ 8.0/10
6. [Instruction-level analysis reveals how Huawei Ascend 950DT enables DeepSeek's 75% price cut.](#item-6) ⭐️ 8.0/10
7. [DeepMind researcher reviews frontier LLM post-training recipe in interview](#item-7) ⭐️ 8.0/10
8. [Export Controls on Claude Fable 5 Harm US Cyber Defense](#item-8) ⭐️ 8.0/10
9. [Meta's Restructuring Engineering to Prioritize AI Strategy](#item-9) ⭐️ 8.0/10
10. [Firefox Integrates Rust-Based zlib-rs for Memory Safety](#item-10) ⭐️ 8.0/10
11. [Gzip compression explored as a surprisingly effective language model for text classification.](#item-11) ⭐️ 8.0/10
12. [SpaceX secures $60B option to acquire AI coding tool Cursor](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [New World Model Physis to Open-Source, Led by 22-Year-Old Peking University Student](https://www.infoq.cn/article/DSWOGK8XvrirsxTIITdY?utm_source=rss&utm_medium=article) ⭐️ 9.0/10

A new AI world model named Physis, developed under the leadership of a 22-year-old undergraduate from Peking University, was announced to be open-sourced at the Zhiyuan Conference. This development represents a significant advancement in physics-based AI world models and showcases exceptional talent emerging from China's top academic institutions, potentially accelerating research in simulation and embodied AI. The model's name 'Physis' (from the Greek word for nature/physics) and its announcement at the Zhiyuan Conference suggest it likely incorporates physics-informed training or simulation capabilities. Open-sourcing the model will allow the broader research community to build upon and validate the work.

rss · InfoQ 中文站 · Jun 17, 10:09

**Background**: World models in AI refer to internal representations that allow systems to predict and simulate environmental dynamics, crucial for applications like robotics and autonomous agents. The Zhiyuan Conference is organized by the Beijing Academy of Artificial Intelligence (BAAI), a major Chinese non-profit AI research institution. Integrating computational physics with machine learning is an emerging field aimed at creating more physically accurate and generalizable AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Beijing_Academy_of_Artificial_Intelligence">Beijing Academy of Artificial Intelligence - Wikipedia</a></li>
<li><a href="https://www.simonsfoundation.org/2025/12/09/these-new-ai-models-are-trained-on-physics-not-words-and-theyre-driving-discovery/">These New AI Models Are Trained on Physics, Not Words, and They're ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Machine_learning_in_physics">Machine learning in physics - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI research`, `#world models`, `#open source`, `#machine learning`, `#computational physics`

---

<a id="item-2"></a>
## [Chrome Update to Deprecate Ad-Blocking APIs, Ending Current Functionality](https://9to5google.com/2026/06/15/google-chromes-next-update-will-mark-the-end-of-popular-ad-blockers/) ⭐️ 9.0/10

Google Chrome's next update will reportedly deprecate the key `webRequest` blocking API used by popular ad blockers, forcing them to use the more restrictive `declarativeNetRequest` API instead. This change will fundamentally limit the capabilities of ad blockers like uBlock Origin, impacting billions of Chrome users' ability to control ads and trackers, and represents a significant shift in browser extension policy. The newer `declarativeNetRequest` API requires pre-defined static rules, which limits the dynamic filtering and custom rule sets that make modern ad blockers effective, though Google argues it is more secure and performant.

rss · Lobsters · Jun 16, 15:55

**Background**: Chrome extensions have historically used Manifest V2, which allowed extensions to intercept all network traffic via the blocking `webRequest` API. Google is pushing developers to Manifest V3, which replaces this with the `declarativeNetRequest` API. This shift has been contentious because the new API severely limits the ability of extensions to block and modify web requests dynamically.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V3 | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate">Migrate to Manifest V3 | Chrome for Developers</a></li>
<li><a href="https://www.ctrl.blog/entry/removing-webrequest-api.html">Chrome is right to remove the webRequest extension API | Ctrl blog</a></li>

</ul>
</details>

**Tags**: `#Chrome`, `#ad-blockers`, `#web-privacy`, `#browser-extensions`, `#manifest-v3`

---

<a id="item-3"></a>
## [Android 17 Released: Mandates Large-Screen Adaptation and Adds AI Integration](https://android-developers.googleblog.com/2026/06/Android-17.html) ⭐️ 9.0/10

Android 17 officially launches, making large-screen adaptation mandatory for apps by removing orientation and size lock options, and introducing the AppFunctions API to enable direct integration with AI assistants like Google Gemini. This is a major OS release that fundamentally shifts Android development by enforcing modern UI standards for diverse device form factors and deeply embedding AI capabilities, which will impact millions of developers and the entire app ecosystem. The update includes new privacy controls like temporary permissions and a contacts picker, enforces strict memory limits based on device RAM, and officially shifts primary UI development to Jetpack Compose while deprecating traditional View components to maintenance mode.

telegram · zaihuapd · Jun 17, 01:02

**Background**: Android's large-screen push aims to provide a consistent experience across phones, foldables, tablets, and desktops, moving beyond basic support to optimized quality tiers. Jetpack Compose is Google's modern declarative UI toolkit for Android, designed to replace the older, imperative XML-based View system with a simpler, more efficient development model. The AppFunctions API provides a structured, on-device method for AI models to perform actions within apps, serving as an alternative to screen-scraping automation.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/reference/android/app/appfunctions/package-summary">android. app . appfunctions | API reference | Android Developers</a></li>
<li><a href="https://developer.android.com/develop/ui/compose/migrate/compare-metrics">Compare Compose and View metrics | Jetpack Compose | Android Developers</a></li>
<li><a href="https://developer.android.com/docs/quality-guidelines/adaptive-app-quality">Adaptive app quality guidelines | App quality | Android Developers</a></li>

</ul>
</details>

**Tags**: `#Android`, `#mobile-development`, `#AI-integration`, `#Jetpack-Compose`, `#OS-release`

---

<a id="item-4"></a>
## [Ransomware Group Steals 1TB+ Data from Novo Nordisk, Threatens to Sell After Failed $25M Extortion](https://www.ithome.com/0/965/287.htm) ⭐️ 8.0/10

The ransomware group FulcrumSec claims to have stolen over 1TB of data from pharmaceutical giant Novo Nordisk, including drug R&D details and AI models, after infiltrating its network for over two months. The group is now planning to sell the stolen data privately after the company refused to pay a $25 million ransom. This breach is significant because it targets a leading global pharmaceutical company, putting highly sensitive intellectual property, patient data, and potentially critical AI models at risk, which could impact drug development and competitive dynamics. The incident highlights the escalating sophistication of ransomware attacks and the persistent vulnerability of the healthcare and pharmaceutical sector to cyber extortion. FulcrumSec claims it gained access in March 2025, stole 1.3TB of data including 700,000 files, and communicated with Novo Nordisk starting June 1, 2025, using a Proton Mail address for anonymity. The group stated it will withhold certain sensitive data, such as details on 11,500 anonymized clinical trial subjects and industrial control system data, to 'reduce harm.'

rss · IT HOME · Jun 17, 03:25

**Background**: FulcrumSec is a relatively new ransomware and cloud extortion group that emerged in late 2025, known for exploiting cloud misconfigurations and exposed credentials. Proton Mail is an encrypted email service often used for anonymous communication due to its strong privacy features. Novo Nordisk is a major Danish pharmaceutical company famous for its obesity and diabetes drugs like Wegovy and Ozempic.

<details><summary>References</summary>
<ul>
<li><a href="https://ransomware.live/group/fulcrumsec">Ransomware .live group profile for fulcrumsec ransomware group</a></li>
<li><a href="https://www.moxfive.com/blog/who-is-fulcrumsec-inside-the-cloud-extortion-group-behind-21-victims-and-counting">Who Is FulcrumSec ? Inside the Cloud Extortion Group Behind 21...</a></li>
<li><a href="https://proton.me/mail/security">How Safe is Proton Mail ? Security Features Explained | Proton</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#ransomware`, `#pharmaceutical industry`, `#corporate security`

---

<a id="item-5"></a>
## [Zhipu Releases Open-Source GLM-5.2: Top Code Arena Model with 1M Context](https://www.ithome.com/0/965/193.htm) ⭐️ 8.0/10

Zhipu AI has released and open-sourced its GLM-5.2 model, claiming the top position among globally available models on the Code Arena frontend development evaluation system. The model features solid 1M-token context support and strong coding capabilities, with performance compared to Claude Opus 4.7 and 4.8 on relevant benchmarks. This release represents a significant step for the open-source large language model ecosystem, providing a powerful new option for long-context and coding tasks that competes with top proprietary models. It strengthens China's domestic AI capabilities and offers developers a high-performance, accessible alternative for complex applications. The model demonstrates optimized infrastructure performance, reducing per-token FLOPs to 2.9 times under 1M context, and has completed Day 0 inference adaptation for multiple domestic computing platforms like Huawei Ascend and Cambricon. It will be released under the permissive MIT license next week.

rss · IT HOME · Jun 17, 01:25

**Background**: GLM (General Language Model) is a series of large language models developed by Zhipu AI, which is associated with Tsinghua University. It typically uses architectures like Mixture-of-Experts (MoE) to balance performance and efficiency. The '1M context' refers to the model's ability to process and remember information from up to one million tokens in a single prompt, crucial for long-document analysis or complex coding projects.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1933303439544255676">🌐 智谱 GLM‑4.5 全面解析：挑战全球前列的开源旗舰大模型 - 知乎</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/637382548">清华大学通用预训练模型：GLM - 知乎</a></li>

</ul>
</details>

**Discussion**: The announcement from Zhipu's channel highlights a strategic positioning, emphasizing that when some frontier models suddenly become unavailable, they choose to make their frontier intelligence open and accessible to all. This framing suggests a response to market volatility and a commitment to open-source principles.

**Tags**: `#开源模型`, `#大语言模型`, `#代码生成`, `#长上下文`, `#人工智能`

---

<a id="item-6"></a>
## [Instruction-level analysis reveals how Huawei Ascend 950DT enables DeepSeek's 75% price cut.](https://www.infoq.cn/article/y9letxDfTZ72Ls1JX27u?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

A rare, detailed instruction-level analysis of Huawei's Ascend 950DT AI chip has been published, directly linking its specific architectural innovations to DeepSeek's 75% inference cost reduction and its subsequent major contract with ByteDance. This analysis provides deep technical validation for Huawei's AI chip strategy under process constraints, showing how hardware-software co-design can directly translate into massive commercial advantages and challenge established players in the AI infrastructure market. The Ascend 950DT is noted for its revolutionary SuperNode architecture, which supports high-speed interconnection of up to 8,192 chips, with future plans for an Ascend 960 chip that will double key specifications. DeepSeek's cost reduction stems from multiple technical levers, including its MoE architecture and sparse attention systems.

rss · InfoQ 中文站 · Jun 17, 11:12

**Background**: Huawei's Ascend series represents its push for domestic AI compute independence, often using architectural innovation to compensate for limits in advanced semiconductor manufacturing processes. DeepSeek is a prominent Chinese AI research company known for developing highly efficient large language models that significantly reduce inference costs. Inference cost is a critical operational expense for deploying AI models, making efficiency gains highly valuable for providers and customers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.omniyq.com/en/sys-nd/501.html">Ascend 950 : A Milestone for Domestic AI Compute - Shenzhen Cloud...</a></li>
<li><a href="https://intuitionlabs.ai/articles/deepseek-inference-cost-explained">DeepSeek 's Low Inference Cost Explained: MoE... | IntuitionLabs</a></li>
<li><a href="https://www.bain.com/insights/deepseek-a-game-changer-in-ai-efficiency/">DeepSeek : A Game Changer in AI Efficiency? | Bain & Company</a></li>

</ul>
</details>

**Tags**: `#AI Chips`, `#Huawei Ascend`, `#Deep Learning`, `#Hardware Architecture`, `#AI Industry`

---

<a id="item-7"></a>
## [DeepMind researcher reviews frontier LLM post-training recipe in interview](https://www.interconnects.ai/p/frontier-post-training-recipe-review) ⭐️ 8.0/10

A detailed interview with DeepMind's Finbarr Timbers provides an in-depth look at the practical techniques, evolution, and key trade-offs involved in post-training recipes for frontier large language models. This interview offers rare, practical insights into a critical but often opaque stage of AI development, helping practitioners understand the real-world challenges and decision-making in creating helpful, aligned AI assistants. The discussion covers the full post-training pipeline, including data curation, supervised fine-tuning (SFT), and reinforcement learning techniques like RLHF, highlighting the practical compromises required between model capability, safety, and computational cost.

rss · Interconnects · Jun 16, 13:29

**Background**: Post-training is the suite of techniques applied after an initial large language model (LLM) is trained on vast amounts of text to predict the next word. Its goal is to transform this 'base' model into a useful, safe, and instruction-following assistant. Common methods include Supervised Fine-Tuning (SFT) on curated examples and Reinforcement Learning from Human Feedback (RLHF), where the model learns from human preferences to align its outputs with human values.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2025/01/31/the-allen-institute-for-ai-ai2-releases-tulu-3-405b-scaling-open-weight-post-training-with-reinforcement-learning-from-verifiable-rewards-rlvr-to-surpass-deepseek-v3-and-gpt-4o-in-key-benchmarks/">The Allen Institute for AI (AI2) Releases Tülu... - MarkTechPost</a></li>
<li><a href="https://www.emergentmind.com/topics/post-training-techniques">Post - Training Techniques</a></li>

</ul>
</details>

**Tags**: `#LLM Training`, `#Machine Learning`, `#Deep Learning`, `#AI Research`, `#Practical AI`

---

<a id="item-8"></a>
## [Export Controls on Claude Fable 5 Harm US Cyber Defense](https://simonwillison.net/2026/Jun/16/fable-5-export-controls/#atom-everything) ⭐️ 8.0/10

A critique, supported by cybersecurity expert Kate Moussouris, argues that the US export control banning Anthropic's Claude Fable 5 model, based on its ability to fix vulnerable code, is a policy misstep that undermines defensive security. This situation highlights a critical tension where broad AI export controls, intended to prevent offensive cyber capabilities, may inadvertently ban models essential for defensive security, weakening the ability of US defenders to find and fix software vulnerabilities. The ban was triggered because researchers could use Fable 5 to fix code with known vulnerabilities (CVEs) and generate test scripts, a process experts define as the core defensive 'find, fix, and test' loop, not a guardrail bypass.

rss · Simon Willison · Jun 16, 05:20

**Background**: The US government has been imposing export controls on advanced AI models, particularly those with dual-use potential for both beneficial and harmful applications. CVE (Common Vulnerabilities and Exposures) is a standardized identifier for known cybersecurity vulnerabilities. Large language models (LLMs) are increasingly being explored for automated vulnerability detection and patching in software code.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/15/cybersecurity-vets-protest-dangerous-us-government-ban-on-anthropics-most-powerful-models/">Cybersecurity vets protest 'dangerous' US government... | TechCrunch</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 - Anthropic</a></li>

</ul>
</details>

**Discussion**: The discussion among cybersecurity experts, as reflected in an open letter and media reports, strongly protests the ban, viewing it as a dangerous precedent that conflates defensive security research with offensive capability and demonstrates a misunderstanding of AI model functionality.

**Tags**: `#AI regulation`, `#cybersecurity`, `#export controls`, `#vulnerability management`, `#LLM safety`

---

<a id="item-9"></a>
## [Meta's Restructuring Engineering to Prioritize AI Strategy](https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering) ⭐️ 8.0/10

Meta's leadership is conducting a major reorganization of its engineering organization, heavily prioritizing artificial intelligence initiatives. This restructuring involves significant changes to team structures and resource allocation to focus on AI development. This strategic shift signals Meta's commitment to competing in the AI race and could reshape how the company allocates engineering talent and resources. The move reflects broader industry trends where major tech companies are pivoting heavily toward AI development to maintain competitive advantage. The restructuring appears to be AI-fueled, with leadership making aggressive changes to engineering organization structures and priorities. The analysis suggests this represents a significant cultural and operational shift within Meta's engineering division.

rss · The Pragmatic Engineer · Jun 16, 16:27

**Background**: Meta Platforms Inc. is the parent company of Facebook, Instagram, and WhatsApp, and has been investing heavily in artificial intelligence and the metaverse. In recent years, many major technology companies have restructured their engineering organizations to prioritize AI development as the technology becomes increasingly central to their business strategies and competitive positioning.

**Tags**: `#Meta`, `#organizational_restructuring`, `#AI_strategy`, `#software_engineering_culture`, `#tech_industry_trends`

---

<a id="item-10"></a>
## [Firefox Integrates Rust-Based zlib-rs for Memory Safety](https://trifectatech.org/blog/zlib-rs-in-firefox/) ⭐️ 8.0/10

Firefox has integrated zlib-rs, a Rust rewrite of the classic zlib compression library, into its codebase. This represents a concrete step in the browser's ongoing efforts to replace critical components with memory-safe alternatives. This integration demonstrates real-world adoption of Rust in mission-critical, performance-sensitive software infrastructure, potentially reducing vulnerabilities related to memory safety in a widely used application. It highlights the industry trend of leveraging Rust's compile-time safety guarantees to modernize legacy C/C++ codebases. zlib-rs is a drop-in replacement for the original C-based zlib, aiming to provide the same functionality with Rust's inherent memory safety. The performance and compatibility of this Rust implementation compared to the original C library are critical factors for its successful adoption in a high-performance environment like a web browser.

rss · Lobsters · Jun 16, 13:29

**Background**: zlib is a foundational, widely used library for data compression, originally written in C. Rust is a systems programming language designed for performance and safety, known for its ownership model that guarantees memory safety without a garbage collector. A core effort in software security is rewriting critical infrastructure components in memory-safe languages like Rust to prevent entire classes of bugs, such as buffer overflows and use-after-free errors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zlib">zlib - Wikipedia</a></li>
<li><a href="https://www.compilenrun.com/docs/language/rust/rust-memory-management/rust-memory-safety/">Rust Memory Safety | Compile N Run</a></li>

</ul>
</details>

**Discussion**: Community discussion, such as on Lobsters, likely centers on the technical merits of the Rust rewrite, including performance benchmarks, API compatibility, and the practical trade-offs between safety and potential overhead. Participants may debate the significance of this move for the broader ecosystem and the challenges of replacing mature, battle-tested C libraries.

**Tags**: `#Rust`, `#Firefox`, `#memory-safety`, `#compression`, `#systems-programming`

---

<a id="item-11"></a>
## [Gzip compression explored as a surprisingly effective language model for text classification.](https://nathan.rs/posts/gzip-lm/) ⭐️ 8.0/10

An investigation demonstrates that gzip compression, when used with a k-nearest neighbors algorithm and normalized compression distance, can achieve competitive performance on text classification tasks. This challenges the assumption that complex neural networks are always necessary for NLP tasks, suggesting that fundamental computer science concepts like compression can capture linguistic similarity and offer simpler, interpretable alternatives. The method uses normalized compression distance (NCD) as a similarity metric between text sequences, where gzip acts as the compressor, and applies a k-nearest neighbors classifier to the resulting distances.

rss · Lobsters · Jun 16, 22:17

**Background**: Gzip is a widely-used lossless data compression program based on the DEFLATE algorithm. The k-nearest neighbors (kNN) algorithm is a simple, non-parametric supervised learning method that classifies data points based on the majority class of their nearest neighbors. Normalized compression distance (NCD) is an information-theoretic measure of similarity between two sequences derived from their compressed lengths.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gzip">gzip - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Normalized_compression_distance">Normalized compression distance - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm">k - nearest neighbors algorithm - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion features high-quality technical debate on the implications and limitations of the approach, with participants discussing its performance relative to modern deep learning models, its interpretability advantages, and potential scaling issues.

**Tags**: `#language-models`, `#compression`, `#NLP`, `#machine-learning`, `#data-science`

---

<a id="item-12"></a>
## [SpaceX secures $60B option to acquire AI coding tool Cursor](https://t.me/zaihuapd/41988) ⭐️ 8.0/10

SpaceX has reportedly obtained a $60 billion option to acquire AI coding startup Cursor, doubling its valuation from $29.3 billion in November 2024. The deal includes a $10 billion partnership fee payable by SpaceX if the acquisition does not close. This move represents a major strategic shift for SpaceX into the AI developer tools market and signals its aggressive preparation for a large-scale IPO by integrating advanced AI capabilities. It could create a powerful synergy between Cursor's code editing software and xAI's Colossus supercomputer to challenge leading AI companies like OpenAI and Anthropic. The proposed $60 billion valuation represents a significant leap from Cursor's previous valuation, highlighting the perceived value of its AI-powered coding assistant in the current market. The deal's structure, with a substantial $10 billion partnership fee if the acquisition fails, underscores SpaceX's strong commitment to integrating Cursor's technology regardless of the final outcome.

telegram · zaihuapd · Jun 16, 11:50

**Background**: Cursor is an AI-powered code editor that enhances developer productivity through intelligent autocompletion, debugging support, and built-in AI chat, distinguishing itself as more than just a simple autocomplete tool. xAI, Elon Musk's AI venture, operates Colossus, described as the world's largest AI training supercomputer, designed to handle massive AI workloads and power models like Grok. SpaceX's IPO strategy reportedly involves significant AI integration, with its space-based data centers potentially providing high-speed cloud infrastructure, and the IPO itself has drawn enormous investor demand.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/">Cursor : AI coding agent</a></li>
<li><a href="https://x.ai/colossus">Colossus : The World's Largest AI Supercomputer | xAI</a></li>
<li><a href="https://www.ainvest.com/news/elon-musk-spacex-ipo-strategic-implications-tesla-ai-driven-growth-2512/">Elon Musk's SpaceX IPO and Its Strategic Implications for Tesla and...</a></li>

</ul>
</details>

**Discussion**: The source for this news is a Telegram channel, which may lack the verification of primary financial news outlets, tempering the confidence some readers might have in the report's accuracy. The sheer scale of the reported deal, involving a doubling of valuation and a massive partnership fee, is likely to generate significant skepticism and discussion regarding its plausibility and SpaceX's strategic intentions.

**Tags**: `#AI acquisition`, `#developer tools`, `#SpaceX`, `#startup valuation`, `#business strategy`

---