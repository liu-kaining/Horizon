---
layout: default
title: "Horizon Summary: 2026-05-27 (EN)"
date: 2026-05-27
lang: en
---

> From 183 items, 10 important content pieces were selected

---

1. [China's Supreme Court to Draft Judicial Rules for AI and Data Rights](#item-1) ⭐️ 8.0/10
2. [China Claims World's First AI System That Autonomously Develops Other AIs](#item-2) ⭐️ 8.0/10
3. [Google Cloud adds cross-engine Apache Iceberg support to BigQuery](#item-3) ⭐️ 8.0/10
4. [curl project faces unsustainable pressure from AI-generated security reports](#item-4) ⭐️ 8.0/10
5. [Microsoft Copilot Cowork Vulnerability Enables File Exfiltration via Prompt Injection](#item-5) ⭐️ 8.0/10
6. [Theseus: A Project to Translate Win32 Applications to WebAssembly](#item-6) ⭐️ 8.0/10
7. [Chromium Intends to Prototype a New Embedding API](#item-7) ⭐️ 8.0/10
8. [Linux developers work on better automatic management for transparent huge pages](#item-8) ⭐️ 8.0/10
9. [China Restricts Manus Co-founders During Review of Meta Acquisition](#item-9) ⭐️ 8.0/10
10. [Qualcomm and ByteDance forge major AI chip partnership for custom ASICs](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [China's Supreme Court to Draft Judicial Rules for AI and Data Rights](https://www.ithome.com/0/955/719.htm) ⭐️ 8.0/10

China's Supreme People's Court announced plans to develop normative judicial documents specifically addressing cases involving artificial intelligence and the protection of data property rights, as part of its ongoing legal reform efforts for the digital economy. This initiative is significant because it will create unified judicial standards for novel issues like AI-generated content ownership and data rights, directly impacting tech companies, data markets, and the broader digital economy in China. The court also aims to refine adjudication rules for data ownership, data transactions, and AI-generated content to promote the deep integration of digital technology with the real economy and support the construction of an open and secure data market.

rss · IT HOME · May 27, 02:34

**Background**: China's Supreme People's Court has been actively working to build a coherent legal framework for the digital economy, having already released its first set of guiding cases concerning data rights protection to unify judicial standards. The global legal landscape is also grappling with how to define ownership for AI-generated works and establish clear data property rights, with different jurisdictions taking varied approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lexology.com/library/detail.aspx?g=51b25197-c798-4aea-9837-296434d4fa44">The Supreme People's Court Issues Its First Guiding Cases on Data ...</a></li>
<li><a href="https://english.court.gov.cn/2025-09/04/c_1122273.htm">SPC releases landmark data-related cases to guide adjudication</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#data rights`, `#China law`, `#digital economy`, `#judicial policy`

---

<a id="item-2"></a>
## [China Claims World's First AI System That Autonomously Develops Other AIs](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247893123&idx=1&sn=5d7d73a6ba59384a99ee4e5abc254e05) ⭐️ 8.0/10

A Chinese-developed AI system has reportedly achieved autonomous development of other AI models, claiming a 10% faster training speed than NVIDIA's Megatron-LM framework. This represents a potential step towards AI-driven AI development, which could accelerate model iteration and reduce human effort, though the claims require independent verification. The news snippet lacks detailed technical specifications, such as the system's architecture, the specific tasks it automates, or the benchmark conditions used for the speed comparison.

rss · 量子位 · May 26, 05:30

**Background**: NVIDIA's Megatron-LM is a prominent open-source framework optimized for training massive transformer-based language models using model parallelism across multiple GPUs. Autonomous AI development systems, often involving AI agents that can plan, code, and test, are an active research area aiming to create meta-learning or self-improving AI. Claiming a significant speed advantage over an established industry benchmark like Megatron is a bold technical assertion.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVIDIA/Megatron-LM">GitHub - NVIDIA/Megatron-LM: Ongoing research training transformer models at scale · GitHub</a></li>
<li><a href="https://developer.nvidia.com/megatron-core">Megatron-Core | NVIDIA Developer</a></li>
<li><a href="https://groupify.ai/blog/self-evolving-ai-development-systems">Automated AI Development in Columbia: AI for AI and the Rise of...</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so there is no discussion to summarize.

**Tags**: `#AI development`, `#automation`, `#training efficiency`, `#national technology`, `#deep learning`

---

<a id="item-3"></a>
## [Google Cloud adds cross-engine Apache Iceberg support to BigQuery](https://www.infoq.cn/article/kadDStA9JWuOGHujwdoz?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Google Cloud has introduced native Apache Iceberg support in BigQuery, enabling cross-engine interoperability for open table format data across different cloud platforms and analytics engines like Databricks and Snowflake. This move significantly enhances data portability and reduces vendor lock-in, allowing enterprises to leverage BigQuery's performance on data stored in other clouds or accessed via competing analytics platforms, which is crucial for the modern data lakehouse ecosystem. The integration allows querying Iceberg data across AWS and Azure, and supports features like table mutations using GoogleSQL DML and unified batch/streaming via the BigQuery Storage Write API.

rss · InfoQ 中文站 · May 27, 09:07

**Background**: Apache Iceberg is a high-performance open-source table format for large analytic tables in data lakes, addressing challenges of older formats like Hive. A data lakehouse combines the low-cost storage of data lakes with the transactional guarantees and performance of data warehouses, and open table formats like Iceberg, Hudi, and Delta Lake are key to enabling cross-engine interoperability in this architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg - Wikipedia</a></li>
<li><a href="https://www.infoq.com/news/2026/05/google-cross-engine-iceberg/">Google Cloud Introduces Cross-Engine Iceberg Support in BigQuery</a></li>
<li><a href="https://cloud.google.com/blog/products/data-analytics/announcing-bigquery-tables-for-apache-iceberg">Announcing BigQuery tables for Apache Iceberg | Google Cloud Blog</a></li>

</ul>
</details>

**Tags**: `#bigquery`, `#apache-iceberg`, `#cloud-data`, `#data-engineering`, `#lakehouse`

---

<a id="item-4"></a>
## [curl project faces unsustainable pressure from AI-generated security reports](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 8.0/10

The curl security team is experiencing an unprecedented flood of high-quality, AI-assisted vulnerability reports, with the rate now more than double that of 2025 and averaging over one report per day, placing immense strain on maintainers. This situation reveals a critical sustainability crisis for foundational open-source infrastructure, where AI's power to find vulnerabilities is outpacing the human capacity to triage and fix them, potentially threatening the stability and security of software used globally. Despite the high volume, the reports are detailed and the vulnerabilities found tend to be of low or medium severity, with no high-severity CVEs since October 2023, but the sheer workload has forced the lead maintainer to work excessive hours, affecting his personal life.

rss · Simon Willison · May 26, 23:48

**Background**: curl is a ubiquitous open-source software library for transferring data with URLs, making it a critical component in countless applications and devices. Security vulnerabilities are tracked as CVEs (Common Vulnerabilities and Exposures), and AI-powered fuzzing uses artificial intelligence to automatically generate and test software inputs to find flaws more efficiently than traditional methods.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/curl/curl/blob/master/docs/SECURITY-ADVISORY.md">curl /docs/ SECURITY - ADVISORY .md at master · curl / curl · GitHub</a></li>
<li><a href="https://medium.com/@stawils/software-fuzzing-the-cornerstone-of-automated-vulnerability-discovery-95aef284cd84">Software Fuzzing: The Cornerstone of Automated Vulnerability Discovery | by Suleiman Tawil | Medium</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#security`, `#ai-impact`, `#software-sustainability`, `#curl`

---

<a id="item-5"></a>
## [Microsoft Copilot Cowork Vulnerability Enables File Exfiltration via Prompt Injection](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

Security researchers discovered a prompt injection vulnerability in Microsoft's Copilot Cowork agentic system, allowing attackers to exfiltrate files by leveraging the system's ability to send emails with embedded images and OneDrive links without user approval. This vulnerability highlights a critical and growing security challenge for agentic AI systems, where the autonomous actions intended to boost productivity can be exploited for data theft, posing significant risks for enterprise environments using Microsoft 365. The attack exploited Copilot Cowork's capability to send emails to a user's own inbox that contained external images triggering network requests, and also leveraged OneDrive's pre-authenticated download links, which could be leaked through a successful prompt injection.

rss · Simon Willison · May 26, 15:36

**Background**: Microsoft Copilot Cowork is an agentic AI feature within Microsoft 365 designed to automate multi-step tasks like sending emails and managing calendars. Prompt injection is a cybersecurity attack where malicious inputs trick an AI model into performing unintended actions. Agentic systems, which can autonomously use tools and take actions, present unique security risks because they blur the line between data and instructions, making them vulnerable to such exploits.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/what-is-agentic-ai-security">Agentic AI Security: What It Is and How to Do It - Palo Alto Networks</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#data exfiltration`, `#Microsoft Copilot`, `#agentic systems`

---

<a id="item-6"></a>
## [Theseus: A Project to Translate Win32 Applications to WebAssembly](https://neugierig.org/software/blog/2026/05/theseus-wasm.html) ⭐️ 8.0/10

The Theseus project has been created to translate Win32 applications into WebAssembly modules, allowing legacy Windows programs to run within web browser environments. This project is significant because it bridges the gap between classic desktop Windows software and modern web platforms, potentially preserving and modernizing a vast ecosystem of legacy applications without requiring source code rewrites. The project focuses on translating Win32 APIs and system calls to their WebAssembly and JavaScript equivalents, which is a complex task given the deep system integration of typical Win32 programs.

rss · Lobsters · May 27, 01:45

**Background**: WebAssembly (often abbreviated as Wasm) is a binary instruction format designed as a portable compilation target for programming languages, enabling high-performance applications on web pages. The Win32 API is the core set of application programming interfaces provided by Microsoft Windows for desktop application development, and translating it to a web environment is a non-trivial compatibility challenge.

<details><summary>References</summary>
<ul>
<li><a href="https://surma.dev/things/c-to-webassembly/">Compiling C to WebAssembly without Emscripten — surma.dev</a></li>
<li><a href="https://developer-mozilla-org.nproxy.org/en-US/docs/WebAssembly">WebAssembly | MDN</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion indicates substantial community interest, with comments likely focusing on the technical feasibility, the novelty of the approach, and comparisons to existing solutions like Wine or Emscripten.

**Tags**: `#WebAssembly`, `#Win32`, `#compatibility-layer`, `#emulation`, `#software-porting`

---

<a id="item-7"></a>
## [Chromium Intends to Prototype a New Embedding API](https://groups.google.com/a/chromium.org/g/blink-dev/c/EjL1gAy3k3Q/m/31Cnh22MBgAJ) ⭐️ 8.0/10

The Blink rendering engine, used in Chromium-based browsers, has announced its intention to prototype a new Embedding API that could fundamentally change how web content is integrated. This API represents a significant shift for web capabilities, potentially offering a modern alternative to existing embedding techniques like iframes, which could lead to more powerful, secure, and seamless content integration across the web. The announcement is in the 'intent to prototype' stage, meaning active development and specification work are beginning but the final shape of the API is not yet determined.

rss · Lobsters · May 26, 21:41

**Background**: Blink is the browser engine that powers Google Chrome, Microsoft Edge, Opera, and many other browsers, making it the most widely used engine on the web. Currently, embedding external content into a web page is most commonly done using the iframe element, which has limitations regarding security, performance, and deep integration with the host page.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blink_(browser_engine)">Blink (browser engine ) - Wikipedia</a></li>
<li><a href="https://www.chromium.org/blink/">Blink ( Rendering Engine )</a></li>
<li><a href="https://blog.logrocket.com/ultimate-guide-iframes/">The ultimate guide to iframes - LogRocket Blog</a></li>

</ul>
</details>

**Discussion**: The linked Lobste.rs discussion likely contains technical debates about the API's design, its potential to replace iframes, and security/privacy implications. Without access to the specific comments, the overall sentiment cannot be summarized.

**Tags**: `#web-apis`, `#browser-engine`, `#embedding`, `#chromium`, `#web-development`

---

<a id="item-8"></a>
## [Linux developers work on better automatic management for transparent huge pages](https://lwn.net/Articles/1073407/) ⭐️ 8.0/10

Nico Pache presented work at the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit on improving the transparency and usability of THPs for applications. A subsequent session led by David Hildenbrand focused on mechanisms to reclaim THPs from processes that are not fully utilizing them. These improvements aim to make THPs work more seamlessly for a wider range of applications, potentially boosting performance through better TLB utilization and reducing manual tuning overhead. Optimizing THP management is critical for systems running memory-intensive workloads like databases and virtual machines. The sessions highlighted the long-standing challenge that THP transparency has not worked as ideally as intended, requiring ongoing kernel development. One key focus is on more intelligent allocation and deallocation strategies to prevent THPs from being held by processes that do not benefit from them, which can waste memory.

rss · LWN.net · May 26, 13:23

**Background**: Transparent Huge Pages (THPs) are a Linux kernel feature that automatically uses larger memory pages (typically 2MB instead of 4KB) to reduce Translation Lookaside Buffer (TLB) misses and lower memory management overhead. TLB is a small, fast cache in the CPU that stores recent virtual-to-physical address translations to speed up memory access. While THPs aim to simplify huge page usage for applications, their behavior can sometimes lead to performance issues, such as latency spikes during defragmentation or reclaim, which is why manual tuning or disabling is common for some workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.kernel.org/admin-guide/mm/transhuge.html">Transparent Hugepage Support — The Linux Kernel documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Translation_lookaside_buffer">Translation lookaside buffer - Wikipedia</a></li>
<li><a href="https://www.alibabacloud.com/help/en/alinux/support/performance-tuning-method-related-to-transparent-large-page-thp-in">Tune THP for system performance - Alibaba Cloud Linux - Alibaba Cloud</a></li>

</ul>
</details>

**Discussion**: Based on the provided LWN article summary, community discussion is not included. However, LWN articles on this topic typically feature expert commentary on the trade-offs between performance gains and potential overhead or complexity introduced by such kernel changes.

**Tags**: `#linux-kernel`, `#memory-management`, `#performance-optimization`, `#operating-systems`

---

<a id="item-9"></a>
## [China Restricts Manus Co-founders During Review of Meta Acquisition](https://t.me/zaihuapd/41577) ⭐️ 8.0/10

Chinese regulators are scrutinizing Meta's acquisition of AI startup Manus for potential violations of investment rules, and have restricted its CEO and Chief Scientist from leaving the country during the investigation. This regulatory action underscores the intensifying geopolitical tensions surrounding cross-border AI investments and technology transfers, particularly involving major US tech firms and Chinese-founded startups. The two co-founders, CEO Xiao Hong and Chief Scientist Ji Yichao, met with China's National Development and Reform Commission in Beijing before being informed they could not leave the country but are allowed to travel domestically.

telegram · zaihuapd · May 26, 09:56

**Background**: Manus is an AI agent developer founded in China and based in Singapore, and Meta announced its acquisition of the company in late December 2025 in a deal reportedly valued at around $2 billion. China's Ministry of Commerce is reviewing the deal for potential export control violations, which adds a layer of regulatory scrutiny to this major tech acquisition.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus ( AI agent) - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2025/12/30/meta-acquires-singapore-ai-agent-firm-manus-china-butterfly-effect-monicai.html">Meta acquires intelligent agent firm Manus, capping year of aggressive AI moves</a></li>
<li><a href="https://www.reuters.com/world/china/meta-acquire-chinese-startup-manus-boost-advanced-ai-features-2025-12-29/">Meta to buy Chinese founded startup Manus to boost advanced AI | Reuters</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#geopolitics`, `#tech M&A`, `#Meta`, `#China tech policy`

---

<a id="item-10"></a>
## [Qualcomm and ByteDance forge major AI chip partnership for custom ASICs](https://www.bloomberg.com/news/videos/2026-05-26/qualcomm-to-supply-chips-to-tiktok-owner-bytedance-video) ⭐️ 8.0/10

Qualcomm has reached a partnership agreement with ByteDance to supply millions of custom Application-Specific Integrated Circuit (ASIC) chips to support ByteDance's AI computing needs. This deal signifies a major expansion of Qualcomm's role in the cloud AI infrastructure market and provides ByteDance with a dedicated, high-volume supply of tailored chips to power its massive AI operations, reflecting a broader industry trend of tech giants designing custom silicon. The partnership will also assist ByteDance in converting its internal chip designs into mass-producible semiconductor products, and follows Qualcomm's recent announcement about delivering its first ASIC to a hyperscale cloud provider.

telegram · zaihuapd · May 27, 02:29

**Background**: An Application-Specific Integrated Circuit (ASIC) is a chip custom-designed for a particular use case, offering higher efficiency than general-purpose processors like GPUs for specific tasks. Major cloud and AI companies, often called hyperscalers, are increasingly developing their own custom ASICs to optimize performance and cost for their unique AI workloads, a trend exemplified by Google's TPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Application-specific_integrated_circuit">Application-specific integrated circuit - Wikipedia</a></li>
<li><a href="https://briefingtech.com/choosing-the-right-hardware-gpu-vs-tpu-for-ai-workloads/">Choosing the Right Hardware: GPU vs TPU for AI ... - Briefing Tech</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#semiconductors`, `#partnership`, `#cloud computing`, `#ByteDance`

---