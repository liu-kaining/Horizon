---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 199 items, 13 important content pieces were selected

---

1. [OpenAI announces first custom AI inference chip, Jalapeno, built with Broadcom.](#item-1) ⭐️ 9.0/10
2. [Anthropic accuses Alibaba of massive distillation attack to steal Claude capabilities.](#item-2) ⭐️ 9.0/10
3. [Qualcomm Unveils Dragonfly Data Center Portfolio with HBC, C1000 CPU, AI300](#item-3) ⭐️ 8.0/10
4. [Report: OpenHarmony Tops Global, Chinese Dev Contributions May Surpass US in 7 Years](#item-4) ⭐️ 8.0/10
5. [China launches world's largest Boron-10 isotope production facility, achieving strategic material self-sufficiency.](#item-5) ⭐️ 8.0/10
6. [TRM Thinking Reward Model quantifies LLM reasoning, presented at ICML 2026 Oral.](#item-6) ⭐️ 8.0/10
7. [Databricks Leaders Argue for Open Ecosystems for AI Agent Clouds](#item-7) ⭐️ 8.0/10
8. [Proposed HTTP QUERY Method for Safe Requests with a Body](#item-8) ⭐️ 8.0/10
9. [China's LineShine Becomes World's Fastest Supercomputer, Exceeding 2 Exaflops](#item-9) ⭐️ 8.0/10
10. [TSMC to raise foundry prices for all advanced processes by 5-10%](#item-10) ⭐️ 8.0/10
11. [Cloudflare & Browsers Propose PACT to Replace CAPTCHAs with Crypto Tokens](#item-11) ⭐️ 8.0/10
12. [Micron's Q3 FY2026 Revenue Surges 346% on AI Memory Demand](#item-12) ⭐️ 8.0/10
13. [Google Play Store Enables External Billing in US, UK, and EEA on June 30](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI announces first custom AI inference chip, Jalapeno, built with Broadcom.](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI has unveiled its first custom AI chip, the Jalapeno, an inference accelerator developed in partnership with Broadcom and manufactured by TSMC. The chip was reportedly designed and brought to production in just nine months, with OpenAI claiming its own AI models were used to accelerate the design and optimization process. This move represents a significant strategic shift toward vertical integration in AI hardware, allowing OpenAI to reduce its dependence on generic GPUs for the critical inference workload. As inference becomes a major cost and profit center for AI services, owning the underlying silicon could provide substantial efficiency gains and a durable competitive advantage. The Jalapeno is specifically designed for inference, which is the process of running a trained AI model to generate outputs, a phase that often requires tens of thousands of chips at scale. OpenAI's claim that its own models accelerated the chip's development in nine months has been met with some skepticism in the community, with details about this specific contribution remaining scarce.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI workloads are broadly split into training, which is the computationally intensive process of teaching a model, and inference, which is the continuous process of using the model. Inference is rapidly becoming the dominant cost for AI companies as their services scale, making specialized inference chips a strategic battleground. Vertical integration, where a company designs its own hardware to tightly optimize it for its software stack, is an emerging trend among major AI players like Google with its TPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.granitefirm.com/blog/us/2025/08/24/ai-inference-chips/">AI inference chips vs. training chips - Andy Lin's Long-term Stock Investment Blog</a></li>
<li><a href="https://www.datacenterknowledge.com/data-center-chips/inference-becomes-the-next-ai-chip-battleground">Inference Becomes the Next AI Chip Battleground</a></li>
<li><a href="https://fourweekmba.com/google-the-most-complete-vertical-integrator-in-ai/">Google: The Most Complete Vertical Integrator in AI - FourWeekMBA</a></li>

</ul>
</details>

**Discussion**: The community discussion shows high engagement but mixed sentiment, with some excitement about the potential efficiency gains from custom hardware but skepticism about marketing claims, particularly around the use of AI models to accelerate design. Commenters also noted the significance of TSMC as the manufacturer and compared OpenAI's move to Google's long-standing TPU program, with some highlighting more radical concepts like burning model weights directly into silicon.

**Tags**: `#AI_hardware`, `#custom_chips`, `#OpenAI`, `#Broadcom`, `#inference`

---

<a id="item-2"></a>
## [Anthropic accuses Alibaba of massive distillation attack to steal Claude capabilities.](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html) ⭐️ 9.0/10

Anthropic has formally accused Alibaba and its Qwen lab of using nearly 25,000 fraudulent accounts to conduct over 28.8 million interactions with its Claude model between April 22 and June 5, 2026, calling it the largest known distillation attack against the company. This accusation highlights a severe and novel form of AI intellectual property theft that could accelerate China's ability to match advanced U.S. AI models like Anthropic's Mythos Preview, intensifying the technological competition between the two nations. The alleged attack involved massive, concentrated, and repetitive queries characteristic of distillation attacks, and the accusation was made in a letter to the U.S. Senate Banking Committee ahead of AI hearings, amidst recent U.S. export restrictions on Anthropic's most powerful models.

telegram · zaihuapd · Jun 25, 01:36

**Background**: Model distillation is a technique where a weaker AI model learns to replicate the capabilities of a stronger one by studying its outputs. In this context, it refers to an attack where a competitor illicitly extracts knowledge from a proprietary model by repeatedly querying its API. The accusation occurs against a backdrop of heightened U.S.-China tensions over AI leadership and security, including recent U.S. government actions to restrict advanced AI technology exports.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Medium</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#intellectual property`, `#US-China relations`, `#model distillation`, `#AI security`

---

<a id="item-3"></a>
## [Qualcomm Unveils Dragonfly Data Center Portfolio with HBC, C1000 CPU, AI300](https://www.ithome.com/0/968/257.htm) ⭐️ 8.0/10

Qualcomm announced its Dragonfly data center product suite featuring the novel High Bandwidth Compute (HBC) architecture, the C1000 CPU for data center workloads, and the AI300 inference accelerator. The HBC architecture uses a 3D stacked design with near-memory compute units beneath LPDDR DRAM to achieve significantly higher bandwidth and efficiency per watt compared to traditional HBM systems. This announcement marks Qualcomm's major push into the data center market, directly challenging incumbents with an architecture designed to break the 'memory wall' bottleneck in AI workloads. If successful, HBC's claimed advantages in bandwidth-per-watt and lower total cost of ownership could reshape memory architectures for AI accelerators and impact the competitive landscape against NVIDIA and AMD. The HBC architecture claims 6x the bandwidth-per-watt of HBM and 200x the capacity-per-watt of SRAM; the first-generation HBC-based AI250 accelerator targets commercial sampling in mid-2027. The Dragonfly C1000 CPU, expected in 2028, scales to over 250 Oryon cores and supports PCIe Gen 7 and CXL.

rss · IT HOME · Jun 25, 01:12

**Background**: HBM (High Bandwidth Memory) is a widely used stacked memory technology in high-performance GPUs and accelerators, but its increasing power consumption contributes to higher total cost of ownership (TCO) for data centers. Near-memory computing is an architectural approach that places processing closer to memory to reduce data movement, thereby improving performance and efficiency. Qualcomm's HBC architecture represents a specific implementation of this concept, using TSV technology to stack LPDDR DRAM dies directly on top of a compute unit.

<details><summary>References</summary>
<ul>
<li><a href="https://partofstyle.com/qualcomms-hbc-puts-compute-under-dram-to-break-ais-memory-bottleneck-with-6x-hbm-efficiency/">Qualcomm’s HBC Puts Compute Under DRAM to Break AI’s Memory ...</a></li>
<li><a href="https://wccftech.com/qualcomm-hbc-stacks-compute-beneath-dram-to-smash-the-ai-memory-wall/">Qualcomm's HBC Stacks Compute Beneath DRAM To Smash The AI Memory Wall, Claiming 6x The Bandwidth Per Watt Of HBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#data center`, `#AI accelerator`, `#Qualcomm`, `#hardware architecture`, `#near-memory computing`

---

<a id="item-4"></a>
## [Report: OpenHarmony Tops Global, Chinese Dev Contributions May Surpass US in 7 Years](https://www.ithome.com/0/968/251.htm) ⭐️ 8.0/10

The 2025 China Open Source Annual Report, released by KaiYuanShe, states that China's active GitHub developers have surpassed 2.1 million and projects like OpenHarmony have reached the top global ranking by OpenRank value. This report highlights China's accelerating influence in the global open-source ecosystem, signaling a potential shift in developer contribution leadership and reflecting broader trends in national tech strategy and international collaboration. Despite having roughly one-third the number of active developers as the US on GitHub, Chinese contributors have achieved nearly 50% of the US's total contribution impact (OpenRank), with their growth rate differential exceeding 10%, suggesting they could lead within seven years.

rss · IT HOME · Jun 25, 01:02

**Background**: OpenHarmony is an open-source project under the OpenAtom Foundation, initiated in 2020 to provide a distributed operating system foundation for smart devices. OpenRank is a metric developed to measure an open-source project's activity and influence by analyzing developer collaboration data, aiming to provide a more holistic view than simple counts like stars or contributors. KaiYuanShe (开源社) is a key Chinese non-profit organization founded in 2014 that promotes open-source culture and collaboration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://open-digger.cn/en/docs/user-docs/metrics/openrank">OpenRank Algorithm - OpenDigger</a></li>
<li><a href="https://cn.linkedin.com/company/kaiyuanshe">KAIYUANSHE 开 源 社 | 领英</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#developer-ecosystem`, `#China-tech`, `#global-trends`, `#OpenHarmony`

---

<a id="item-5"></a>
## [China launches world's largest Boron-10 isotope production facility, achieving strategic material self-sufficiency.](https://www.ithome.com/0/968/247.htm) ⭐️ 8.0/10

China has successfully launched the world's largest-capacity production facility for high-enrichment Boron-10 isotopes in Dongying, Shandong Province. The facility, which reached full production in just 1.5 years, has already produced 25 metric tons of product with a Boron-10 enrichment of up to 99.7%. This breakthrough breaks the foreign monopoly on the core technology and high-end market for high-enrichment Boron-10 isotopes, enabling China to achieve self-sufficiency in this critical material for its nuclear power and advanced medical industries. It positions China among the few nations capable of large-scale production of this strategically important isotope. The project was led by the Shanghai Research Institute of Chemical Industry (SRICI), which completed the hundred-ton-scale facility design, construction, and production in only 1.5 years, achieving success on the first commissioning attempt. The achieved enrichment of 99.7% for Boron-10 is noted to have further room for improvement.

rss · IT HOME · Jun 25, 00:50

**Background**: Boron-10 is a stable isotope of boron with a very high neutron capture cross-section, making it essential for controlling nuclear reactions and shielding against radiation. It is primarily used as a neutron-absorbing material in nuclear reactor control rods and safety systems, as well as in advanced medical therapies like Boron Neutron Capture Therapy (BNCT) for cancer. Industrial-scale enrichment typically involves complex processes such as the chemical exchange distillation of boron trifluoride (BF₃).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Control_rod">Control rod - Wikipedia</a></li>
<li><a href="https://pdf.benchchem.com/1234/A_Comparative_Analysis_of_Boron_10_Enrichment_Techniques_for_Researchers_and_Drug_Development_Professionals.pdf">A Comparative Analysis of Boron-10 Enrichment Techniques for ...</a></li>
<li><a href="https://www.nuclear-power.com/glossary/boron-10/applications-of-boron-nuclear-power/">Applications of Boron - Nuclear Power</a></li>

</ul>
</details>

**Tags**: `#strategic materials`, `#nuclear technology`, `#isotope production`, `#advanced manufacturing`, `#technology sovereignty`

---

<a id="item-6"></a>
## [TRM Thinking Reward Model quantifies LLM reasoning, presented at ICML 2026 Oral.](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247899199&idx=3&sn=b0d6764e50d881295fd85b75f8f9434a) ⭐️ 8.0/10

A new Thinking Reward Model (TRM) has been introduced to quantitatively assess the intermediate reasoning processes of large language models, moving beyond just evaluating final answer correctness. The model was presented as an Oral paper at the ICML 2026 conference. This is significant because it provides a more granular evaluation framework for AI reasoning, which can lead to better training and alignment of LLMs by rewarding sound thinking processes. It directly addresses a key limitation in current AI evaluation where correct answers can mask flawed reasoning. The project includes an open-source implementation that has gained substantial community traction, with the GitHub repository accumulating 4.2k stars. The research team also constructed a dedicated TRM-Preference dataset for training and evaluation.

rss · 量子位 · Jun 24, 04:00

**Background**: In AI, reward models are typically used to align language models with human preferences by scoring outputs. Traditional models often only assess the final answer, but process reward models (PRMs) aim to evaluate intermediate reasoning steps. The Thinking Reward Model (TRM) is a specific approach that models rewards based on these intermediate processes to provide clearer training signals.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/thinking-supervised-reward-model-trm">Thinking -supervised Reward Model ( TRM )</a></li>
<li><a href="https://eu.36kr.com/en/p/3866659734279170">TRM Thinking Reward Model Launched: Large Models ' Reasoning...</a></li>
<li><a href="https://icml.cc/virtual/2026/events/oral">ICML 2026 Orals</a></li>

</ul>
</details>

**Discussion**: The open-source project has received significant community interest, evidenced by its high GitHub star count. This suggests strong demand for tools that can evaluate and improve the quality of AI reasoning, not just its outcome.

**Tags**: `#Large Language Models`, `#AI Evaluation`, `#Reward Modeling`, `#Reasoning`, `#Open Source`

---

<a id="item-7"></a>
## [Databricks Leaders Argue for Open Ecosystems for AI Agent Clouds](https://www.latent.space/p/databricks) ⭐️ 8.0/10

Databricks co-founders Matei Zaharia and Reynold Xin gave a rare double interview arguing that an open ecosystem is essential for every company to build its own 'Agent Cloud'. This advocacy from the creators of Apache Spark highlights a potential industry shift towards open, interoperable platforms for AI agents, which could prevent vendor lock-in and foster broader innovation in the next wave of cloud AI. The concept of 'Agent Clouds' refers to platforms where autonomous AI agents interact and operate, and Databricks has a history of open-sourcing core components like Unity Catalog to support its open ecosystem strategy.

rss · Latent Space · Jun 24, 18:53

**Background**: An 'Agent Cloud' is an emerging concept describing a cloud environment where multiple AI agents can autonomously collaborate and perform tasks. Databricks, known for creating the unified data platform Lakehouse, has consistently championed open-source and open standards to avoid vendor lock-in, as seen with its open-sourcing of Unity Catalog for data and AI governance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open">Databricks Open Sources Unity Catalog, Creating the... - Databricks</a></li>
<li><a href="https://www.linkedin.com/pulse/why-databricks-open-source-strategy-matters-more-than-stratulat-uarhe">Why Databricks ’ Open Source Strategy Matters More to the Business...</a></li>
<li><a href="https://medium.com/@philippeandrepage/ai-agent-clouds-c8cf588f7392">Autonomous Agent Clouds . A Conceptual Framework for... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#cloud computing`, `#open ecosystem`, `#Databricks`, `#industry trends`

---

<a id="item-8"></a>
## [Proposed HTTP QUERY Method for Safe Requests with a Body](https://httpwg.org/http-extensions/draft-ietf-httpbis-safe-method-w-body.html#section-1-5.2) ⭐️ 8.0/10

A new HTTP method called QUERY is being proposed as a protocol extension. This method is designed to be safe and idempotent while allowing complex query parameters to be sent in the request body. This addresses a long-standing limitation in HTTP where safe operations like GET are discouraged from using a request body, forcing developers to use workarounds like encoding large queries into URLs. It could enable more expressive and efficient API designs for complex queries. The QUERY method must maintain the safety and idempotency properties required for caching and reliable retries, which distinguishes it from methods like POST. Its adoption will depend on broad ecosystem support from clients, servers, and intermediaries like proxies.

rss · Lobsters · Jun 24, 20:04

**Background**: In HTTP, a 'safe' method does not alter server state, and an 'idempotent' method can be called multiple times with the same effect. The widely used GET method is safe and idempotent but its specification discourages including a request body, making complex queries cumbersome. The QUERY proposal aims to formally introduce a new safe, idempotent method that explicitly supports a body.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Safe/HTTP">Safe ( HTTP Methods ) - Glossary | MDN</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET">GET request method - HTTP | MDN</a></li>
<li><a href="https://lists.w3.org/Archives/Public/ietf-http-wg/2024JulSep/0102.html">Method Mania from Josh Cohen on 2024-07-25 (ietf- http -wg@w3.org...)</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion shows high engagement with technical debates. Key viewpoints include evaluating its use cases for complex queries versus GraphQL, discussing its potential impact on existing caching mechanisms, and comparing it to alternative approaches like POST with a special header or the SEARCH method.

**Tags**: `#HTTP`, `#web-standards`, `#API-design`, `#protocol`, `#specification`

---

<a id="item-9"></a>
## [China's LineShine Becomes World's Fastest Supercomputer, Exceeding 2 Exaflops](https://hackaday.com/2026/06/24/lineshine-is-fastest-supercomputer-at-over-2-exaflops/) ⭐️ 8.0/10

China's LineShine supercomputer has debuted at number one on the TOP500 list, becoming the world's first system to achieve sustained performance exceeding 2 exaflops. This achievement marks a significant milestone in high-performance computing, demonstrating a major leap in computational power that will impact advanced scientific research, artificial intelligence, and industrial simulations worldwide. The system is notable for its all-CPU architecture, powered by domestically designed Armv9-based LX2 processors with 304 cores each, and is deployed at the National Supercomputing Center in Shenzhen.

rss · Hackaday · Jun 25, 02:00

**Background**: Exascale computing refers to systems capable of performing at least 10^18 (one quintillion) floating-point operations per second (FLOPS), a milestone previously achieved by only a few machines. The TOP500 project ranks the world's most powerful supercomputers based on the High Performance Linpack (HPL) benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://www.top500.org/news/lineshine-debuts-no-1-top500-enters-new-global-exascale-era/">LineShine Debuts at No. 1 as the TOP500 Enters a New Global ...</a></li>
<li><a href="https://www.hpcwire.com/2026/04/28/china-unveils-2-exaflop-all-cpu-lineshine-supercomputer/">China Unveils 2 Exaflop, All-CPU ‘LineShine’ Supercomputer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Exascale_computing">Exascale computing - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#supercomputing`, `#high-performance-computing`, `#exaflops`, `#computer-science`, `#benchmark`

---

<a id="item-10"></a>
## [TSMC to raise foundry prices for all advanced processes by 5-10%](https://36kr.com/newsflashes/3866472254411779) ⭐️ 8.0/10

TSMC has notified customers that wafer foundry prices will increase for all advanced process nodes, including 7nm and below, with an overall hike of about 5% to 10%. This price increase affects approximately 75% of TSMC's wafer revenue and is likely to raise production costs for a wide range of downstream technology products, impacting the global semiconductor supply chain. The price hike covers not only the rumored 3nm process but extends to all advanced nodes at 7nm and below, indicating a broad-based adjustment across TSMC's most technologically sophisticated offerings.

telegram · zaihuapd · Jun 24, 05:45

**Background**: Taiwan Semiconductor Manufacturing Company (TSMC) is the world's largest contract chipmaker, producing advanced integrated circuits for major clients like Apple, Nvidia, and AMD. Process nodes such as 7nm and 3nm refer to the manufacturing technology's feature size, where smaller numbers typically indicate more advanced, powerful, and efficient chips. Wafer foundry pricing is a critical factor for the entire electronics industry, influencing the cost of smartphones, computers, and data centers.

**Tags**: `#semiconductors`, `#supply chain`, `#TSMC`, `#foundry`, `#pricing`

---

<a id="item-11"></a>
## [Cloudflare & Browsers Propose PACT to Replace CAPTCHAs with Crypto Tokens](https://www.techtimes.com/articles/318891/20260623/cloudflare-chrome-firefox-plan-replace-captchas-cryptographic-tokens.htm) ⭐️ 8.0/10

Cloudflare, in collaboration with Chrome, Firefox, Edge, and Shopify, has proposed the PACT protocol, which aims to replace traditional CAPTCHAs with anonymous cryptographic tokens based on IETF's Privacy Pass technology. This proposal could significantly enhance user privacy and browsing experience by eliminating intrusive CAPTCHA tasks while still verifying human users, impacting web security standards for billions of users and major platforms. The protocol uses blind signature cryptography to issue tokens from trusted sites, allowing users to access other sites without revealing their identity or browsing history, and it also addresses distinguishing legitimate AI agents from malicious bots.

telegram · zaihuapd · Jun 24, 06:30

**Background**: CAPTCHAs (Completely Automated Public Turing test to tell Computers and Humans Apart) are widely used tests to block bots but are often criticized for being annoying and raising accessibility concerns. Privacy Pass is an existing IETF protocol that uses blind signatures to allow anonymous authentication, and blind signature cryptography is a technique where a message can be signed by a signer without the signer learning the message's content, preserving user anonymity.

<details><summary>References</summary>
<ul>
<li><a href="https://privacypass.github.io/">Privacy Pass</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blind_signature">Blind signature - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/draft-ietf-privacypass-protocol-01">Privacy Pass Protocol Specification (Internet-Draft, 2021)</a></li>

</ul>
</details>

**Tags**: `#web-security`, `#privacy`, `#protocols`, `#CAPTCHA-alternatives`, `#cryptography`

---

<a id="item-12"></a>
## [Micron's Q3 FY2026 Revenue Surges 346% on AI Memory Demand](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) ⭐️ 8.0/10

Micron Technology reported record Q3 FY2026 results with revenue surging 346% year-over-year to $41.46 billion, driven by explosive AI infrastructure demand, and provided a strong forward guidance projecting $50 billion in revenue for the next quarter. This unprecedented financial performance highlights the critical and growing role of high-bandwidth memory (like HBM) in enabling the AI revolution, signaling that memory has become a primary bottleneck and cost driver in AI infrastructure. The company's profitability reached extraordinary levels, with a net profit of $28.24 billion for the quarter and a Non-GAAP gross margin soaring to 84.9%. Micron has secured 16 long-term strategic agreements to lock in orders for the next 3-5 years and expects the memory shortage to persist through 2027.

telegram · zaihuapd · Jun 24, 22:22

**Background**: High Bandwidth Memory (HBM) is a specialized type of high-performance DRAM crucial for AI accelerators, featuring a 3D-stacked design that provides massive data bandwidth. The explosive growth of AI models has created a structural shortage in the global memory market, shifting it from cyclical fluctuations to a persistent supply crisis. This demand is transforming memory from a commodity component into a critical, performance-limiting element of the entire computing stack.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://assets.micron.com/adobe/assets/urn:aaid:aem:8a68fc66-7658-4d0a-98ef-3d70f93181a2/renditions/original/as/import_of_mem_in_hi_perf_compute_and_ai_white_paper.pdf">The Importance of Memory in High-Performance Computing and AI</a></li>
<li><a href="https://enkiai.com/ai-market-intelligence/ai-memory-crisis-2026-unpacking-the-global-shortage/">AI Memory Crisis 2026: Unpacking the Global Shortage</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#financial-results`, `#AI-infrastructure`, `#memory-chips`, `#market-trends`

---

<a id="item-13"></a>
## [Google Play Store Enables External Billing in US, UK, and EEA on June 30](https://android-developers.googleblog.com/2026/06/play-expanded-billing.html) ⭐️ 8.0/10

Starting June 30, 2026, Google will allow eligible developers in the US, UK, and European Economic Area to offer third-party or web-based payment systems alongside Google Play Billing, with a new fee structure that lowers the base service fee to 10% on the first $1M in annual revenue. This major policy shift significantly increases billing flexibility for developers, potentially reducing their costs and giving them more control over monetization, which could reshape app business models across key global markets. The new fee structure splits the Play service fee from a separate settlement fee; transactions using Google Play Billing incur an additional 5% settlement fee in these regions, while those using alternative billing or external links do not. Developers enrolled in Google's 'Level Up' or 'Apps Experience' programs will access even lower fees starting in September.

telegram · zaihuapd · Jun 25, 02:33

**Background**: Google Play has historically required most digital goods and services sold within apps to use its own billing system, taking a commission of up to 30%. This move follows regulatory pressure and legal settlements, particularly in the European Union, that have pushed app store operators to allow alternative payment options. The European Economic Area (EEA) includes EU member states plus Iceland, Liechtenstein, and Norway, forming a unified market with common economic rules.

<details><summary>References</summary>
<ul>
<li><a href="https://android-developers.googleblog.com/2026/06/play-expanded-billing.html">Android Developers Blog: Expanded billing choice and lower fees on...</a></li>
<li><a href="https://9to5google.com/2026/06/24/google-play-store-external-billing-june-30/">Google Play Store opens external billing starting June 30</a></li>
<li><a href="https://www.3u.com/news/details/15063/google-lowering-play-store-fees-and-allowing-alternative-payments-worldwide">Google Lowering Play Store Fees and Allowing Alternative... - 3uTools</a></li>

</ul>
</details>

**Tags**: `#Google Play Store`, `#App Billing`, `#Developer Policy`, `#Mobile Ecosystem`, `#Monetization`

---