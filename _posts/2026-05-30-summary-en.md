---
layout: default
title: "Horizon Summary: 2026-05-30 (EN)"
date: 2026-05-30
lang: en
---

> From 199 items, 10 important content pieces were selected

---

1. [vLLM v0.22.0 released with DeepSeek V4, NVFP4, and experimental Rust frontend.](#item-1) ⭐️ 9.0/10
2. [Claude Mythos AI Discovers Over 23,000 Open-Source Vulnerabilities](#item-2) ⭐️ 9.0/10
3. [Blue Origin's New Glenn rocket explodes during static fire test, delaying NASA's Artemis moon missions.](#item-3) ⭐️ 9.0/10
4. [Huawei Unveils 'Tao Law' to Replace Moore's Law with Time Scaling](#item-4) ⭐️ 9.0/10
5. [Dead Economy Theory: AI risks a deflationary spiral by replacing consumers.](#item-5) ⭐️ 8.0/10
6. [OpenAI Upgrades GPT-5.5 Instant for More Natural Responses, Retires Older Models](#item-6) ⭐️ 8.0/10
7. [China's Manned Lunar Landing Program on Track for 2028-2030 Missions](#item-7) ⭐️ 8.0/10
8. [OpenAI launches Rosalind Biodefense for GPT-Rosalind access](#item-8) ⭐️ 8.0/10
9. [Classical Computers Can Fully Simulate Complex Chemistry, Study Finds](#item-9) ⭐️ 8.0/10
10. [Anthropic Surpasses OpenAI as Highest-Valued AI Startup](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.22.0 released with DeepSeek V4, NVFP4, and experimental Rust frontend.](https://github.com/vllm-project/vllm/releases/tag/v0.22.0) ⭐️ 9.0/10

vLLM v0.22.0 is a major update that hardens DeepSeek V4 model support with NVFP4 fused MoE, adds multi-token prediction (MTP) speculative decoding, and introduces an experimental Rust-based frontend. The release also advances the Model Runner V2 architecture and includes 459 commits from 230 contributors. This release significantly boosts inference efficiency for large mixture-of-experts (MoE) models like DeepSeek V4 and expands vLLM's capabilities with speculative decoding and a high-performance Rust frontend, potentially setting new standards for LLM serving performance and developer tooling. Key additions include NVFP4 fused MoE support for DeepSeek V4, multi-tier KV cache offloading beyond CPU memory, and a 28.9% latency improvement for batch-invariant inference with Cutlass FP8. The Model Runner V2 is now the default for Qwen3 dense models and includes features like sleep-mode weight reloading.

github · khluu · May 29, 10:28

**Background**: vLLM is a high-performance, open-source library designed for fast and efficient inference and serving of large language models (LLMs). Speculative decoding is a technique that uses a smaller, faster 'draft' model to propose multiple tokens at once, which are then verified in parallel by the main model to increase output speed. Mixture-of-Experts (MoE) is a model architecture where different subsets of parameters (experts) are activated for different inputs, improving efficiency for large models.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/moe_kernel_features/">Fused MoE Kernel Features - vLLM</a></li>
<li><a href="https://huggingface.co/kernels/Atlas-Inference/nvfp4-moe">Atlas-Inference/nvfp4-moe - Kernel - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference-optimization`, `#deep-learning`, `#open-source`, `#performance`

---

<a id="item-2"></a>
## [Claude Mythos AI Discovers Over 23,000 Open-Source Vulnerabilities](https://www.v2ex.com/t/1216615#reply5) ⭐️ 9.0/10

Anthropic's Claude Mythos Preview model has scanned over 1,000 open-source projects and discovered an estimated 23,019 vulnerabilities, with an independent security firm confirming 90.6% of the high-severity bugs they sampled were valid. This demonstrates that AI can now discover vulnerabilities at a scale and speed previously unattainable by human researchers, potentially automating a significant portion of security work and forcing the cybersecurity industry to adapt its processes for verification and patching. The model was so powerful that Anthropic withheld its public release until it could develop better safeguards, providing access only to trusted partners under its Project Glasswing, which has committed $100M in model credits for research.

rss · V2EX · May 30, 02:02

**Background**: Claude Mythos is a specialized AI model from Anthropic designed for vulnerability discovery in software. Vulnerability discovery, or 'bug hunting,' is the process of finding security flaws in software that could be exploited by attackers. Open-source projects, whose source code is publicly available, are critical infrastructure often audited by both humans and automated tools for security issues.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/glasswing-initial-update">Project Glasswing: An initial update</a></li>
<li><a href="https://quantumzeitgeist.com/mythos-preview-vulnerabilities-partnership-identifies/">Mythos Preview Identifies 10,000+ Vulnerabilities With Partners</a></li>
<li><a href="https://www.elisity.com/blog/claude-mythos-ai-vulnerability-discovery-microsegmentation-unpatchable-devices">Claude Mythos Found 27-Year-Old Bugs. Your Unpatchable Devices...</a></li>

</ul>
</details>

**Discussion**: The V2EX discussion thread shows significant interest and speculation, with users asking if anyone has actually used the preview and debating whether this signals that vulnerability research is the next job to be disrupted by AI, following programming.

**Tags**: `#AI_security`, `#vulnerability_discovery`, `#Anthropic`, `#cybersecurity`, `#automation`

---

<a id="item-3"></a>
## [Blue Origin's New Glenn rocket explodes during static fire test, delaying NASA's Artemis moon missions.](https://arstechnica.com/space/2026/05/blue-origins-new-glenn-rocket-just-exploded-during-a-static-fire-test/) ⭐️ 9.0/10

On May 28, 2026, Blue Origin's New Glenn rocket suffered a catastrophic explosion during a static fire test at Cape Canaveral's Launch Complex 36, destroying the vehicle's first and second stages and causing severe damage to the launch pad's lightning protection tower and ground infrastructure. This is a major setback for Blue Origin's flagship vehicle, likely delaying the company's launch manifest for NASA's Artemis Human Landing System and Amazon's Project Kuiper satellites, and impacting the broader commercial space industry's launch capacity and deep-space exploration timelines. The explosion occurred during the NG-4 mission preparation, which was intended to launch 48 Amazon Kuiper broadband satellites; the cause is under investigation, and no timeline for repairs or return to flight has been announced.

telegram · zaihuapd · May 29, 11:08

**Background**: New Glenn is Blue Origin's large, reusable orbital rocket designed to compete with vehicles like SpaceX's Falcon Heavy. The vehicle is powered by seven BE-4 methane-fueled engines on its first stage. Blue Origin was selected by NASA to develop the Blue Moon lander as part of the Artemis program's Human Landing System, a critical component for returning astronauts to the lunar surface.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/New_Glenn">New Glenn - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BE-4">BE-4 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human_Landing_System">Human Landing System - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space`, `#rocket launch`, `#NASA`, `#Blue Origin`, `#Artemis program`

---

<a id="item-4"></a>
## [Huawei Unveils 'Tao Law' to Replace Moore's Law with Time Scaling](https://t.me/zaihuapd/41648) ⭐️ 9.0/10

At the 2026 IEEE International Symposium on Circuits and Systems in Shanghai, Huawei announced the 'Tao Law', a new semiconductor scaling principle that replaces geometric scaling with 'time scaling'. Huawei claims it has used this principle to design and mass-produce 381 chips over the past six years. This proposal offers a potential paradigm shift for the semiconductor industry as traditional geometric scaling (Moore's Law) approaches physical and economic limits, providing an alternative path to continue improving chip density and performance. The Tao Law is implemented through a 'LogicFolding' architecture that physically folds and stacks logic circuits, reportedly achieving a 55% increase in transistor density and a 41% boost in power efficiency. Huawei targets producing chips with transistor density equivalent to 1.4nm process levels by 2031, with the first commercial application being its upcoming Kirin mobile chips.

telegram · zaihuapd · May 30, 02:18

**Background**: Moore's Law, the observation that the number of transistors on a chip doubles roughly every two years, has been the driving principle of semiconductor advancement for decades. However, as transistor sizes shrink to atomic scales, geometric scaling becomes increasingly difficult and expensive. The Tao Law proposes a shift in focus from shrinking physical dimensions (geometric scaling) to optimizing time-related parameters like signal delay and clock cycles across the entire system hierarchy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.huawei.com/en/news/2026/5/ieee-iscas-tau-scaling">HUAWEI Presents the Tau (τ) Scaling Law, Enabling Breakthroughs in Transistor Density and System Performance - Huawei</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/huawei-claims-sanctions-busting-breakthrough-with-1-4nm-class-chips-by-2031-claims-55-percent-higher-transistor-density-firm-claims-new-logicfolding-chip-architecture-can-bypass-euv-restrictions-introduces-tau-scaling-law-to-replace-moores-law">Huawei claims sanctions-busting breakthrough with 1.4nm-class chips by 2031, claims 55% higher transistor density — firm claims new LogicFolding chip architecture can bypass EUV restrictions, introduces 'Tau Scaling Law' to replace Moore's Law | Tom's Hardware</a></li>
<li><a href="https://chinarxiv.org/items/chinaxiv-202605.00224">A Time Scaling Theory for Multi-Layer Electronic Systems</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#Huawei`, `#Moore's Law`, `#chip design`, `#paradigm shift`

---

<a id="item-5"></a>
## [Dead Economy Theory: AI risks a deflationary spiral by replacing consumers.](https://www.owenmcgrann.com/p/the-dead-economy-theory) ⭐️ 8.0/10

The article introduces the 'dead economy theory,' arguing that widespread AI-driven automation could create a deflationary feedback loop by displacing workers who are also consumers, ultimately collapsing the demand that AI aims to serve. This theory challenges the common narrative of technological progress by highlighting a potential fundamental contradiction in AI adoption: it might erode its own customer base, which is highly relevant to current economic debates about automation and job displacement. The theory is based on the idea that when companies replace human workers with AI to cut costs, they simultaneously reduce aggregate consumer spending power, leading to lower demand for goods and services, including those produced by AI.

hackernews · WillDaSilva · May 29, 15:46 · [Discussion](https://news.ycombinator.com/item?id=48324712)

**Background**: The theory draws an analogy to deflationary spirals in economics, where falling prices lead to reduced production, lower wages, and further decreases in demand. Historical precedents, like the massive shift of labor out of agriculture in developed nations, show economies can adapt, but the theory questions whether an AI-driven shift could be uniquely disruptive. Technological unemployment, the concept that innovation can cause job losses, is a long-standing debate among economists.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deflation">Deflation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Technological_unemployment">Technological unemployment - Wikipedia</a></li>
<li><a href="https://news.lavx.hu/article/the-dead-economy-theory-why-ai-driven-automation-may-collapse-demand">The Dead Economy Theory – Why AI ‑Driven Automation May...</a></li>

</ul>
</details>

**Discussion**: The community discussion is robust, with comments drawing analogies to India's subsidized, labor-intensive agriculture as a model of a 'supported' but inefficient system. Other users speculate about tech industry overcapacity, questioning the productivity of large teams and suggesting AI may simply be automating an already surplus workforce. A few comments explore the extreme logical endpoint where a fully automated economy would have no human consumers.

**Tags**: `#AI economics`, `#automation impact`, `#deflation`, `#labor markets`, `#technological unemployment`

---

<a id="item-6"></a>
## [OpenAI Upgrades GPT-5.5 Instant for More Natural Responses, Retires Older Models](https://www.ithome.com/0/957/437.htm) ⭐️ 8.0/10

OpenAI updated its GPT-5.5 Instant model on May 28, 2026, to produce more natural, readable, and structured responses while reducing verbose lists. The company also announced the phased retirement of the OpenAI o3 and GPT-4.5 models, with removal dates set for August 26, 2026, and June 27, 2026, respectively. This update represents a significant step in improving the usability and reliability of a core default model for millions of users, directly addressing common complaints about AI-generated text quality and hallucinations. The retirement of older models signals a consolidation in OpenAI's ecosystem, guiding users and developers toward newer, more capable architectures. The GPT-5.5 Instant model, which replaced GPT-5.3 Instant as ChatGPT's default for free-tier users on May 5, 2026, has seen a 52.5% reduction in hallucinations on high-stakes topics like medicine, law, and finance. A notable change is that the Canvas feature, a dedicated workspace for text and code, will no longer be available in GPT-5.5 Instant or GPT-5.5 Thinking, though paid users have a grace period to use it before the old models are retired.

rss · IT HOME · May 30, 02:14

**Background**: GPT-5.5 Instant is a version of OpenAI's GPT-5.5 model architecture tuned for fast, low-latency responses, serving as the default model for many ChatGPT users. The OpenAI o3 model was introduced as an advanced 'reasoning' or 'inference' model, succeeding the o1 model, and is designed for complex tasks requiring deep thought. The Canvas feature in ChatGPT provides a separate, structured panel for drafting and editing long-form text or code, offering a more focused workspace than the standard chat interface.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-5-5-instant-system-card/">GPT-5.5 Instant System Card | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-canvas/">Introducing canvas | OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.5`, `#AI model updates`, `#ChatGPT`, `#model deprecation`

---

<a id="item-7"></a>
## [China's Manned Lunar Landing Program on Track for 2028-2030 Missions](https://www.ithome.com/0/957/384.htm) ⭐️ 8.0/10

China's first astronaut and current Deputy Chief Designer of the Manned Space Engineering Program, Yang Liwei, officially confirmed that the manned lunar landing program is progressing normally. The plan involves executing three unmanned circumlunar verification missions and one crewed mission between 2028 and 2030 at the Wenchang Space Launch Site. This confirmation with a specific timeline marks a major strategic shift for China's space program from near-Earth orbit operations to cislunar space, positioning it as a leading contender in the new era of lunar exploration. It signals a significant step towards establishing a sustained human presence beyond Earth orbit, with implications for future deep-space exploration and international space cooperation. The missions will utilize the Long March-10 rocket and a new-generation crewed spacecraft, both of which underwent tests last year and earlier this year. Astronaut selection for the lunar missions will prioritize those with prior flight experience, as stated by Yang Liwei in 2023.

rss · IT HOME · May 29, 14:55

**Background**: The Wenchang Space Launch Site in Hainan is China's newest and southernmost launch facility, chosen for its proximity to the equator, which provides a fuel efficiency advantage for launches to higher orbits like the Moon. China's current human spaceflight program, Shenzhou, has been operating in low-Earth orbit for over two decades. The planned missions represent the culmination of decades of development in life support, spacecraft re-entry, and heavy-lift launch vehicle technology.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wenchang_Space_Launch_Site">Wenchang Space Launch Site - Wikipedia</a></li>
<li><a href="https://www.bbc.com/zhongwen/simp/china/2013/06/130611_china_shenzhou_timeline">资料：中国“ 神 舟 ” 载 人 航天历史 - BBC News 中文</a></li>
<li><a href="https://www.dutenews.com/n/article/10668438">飞 船 返回舱成功着陆， 神 二 十 一乘组到家了</a></li>

</ul>
</details>

**Tags**: `#space exploration`, `#China`, `#manned spaceflight`, `#lunar mission`, `#engineering`

---

<a id="item-8"></a>
## [OpenAI launches Rosalind Biodefense for GPT-Rosalind access](https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense) ⭐️ 8.0/10

OpenAI has launched the Rosalind Biodefense program, which provides vetted developers and U.S. government partners with access to its GPT-Rosalind model to advance biodefense and pandemic preparedness efforts. This initiative is significant because it strategically directs powerful frontier AI capabilities towards critical public health and national security challenges, potentially accelerating the development of tools for early detection and response to biological threats. The program builds on OpenAI's existing safety and resilience work and is described as supporting 'defensive acceleration,' focusing on applications for diagnostics, preparedness, and response rather than open-ended research.

rss · OpenAI Blog · May 29, 03:00

**Background**: GPT-Rosalind is a specialized AI model from OpenAI designed for life sciences research, available through a trusted access program rather than broadly to the public. The concept of biodefense involves protecting populations from biological threats, including naturally occurring pandemics and deliberate bioterrorism, a concern that has grown in prominence. Frontier AI refers to the most advanced, powerful AI systems that are at the cutting edge of capability.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-rosalind/">Introducing GPT - Rosalind for life sciences research | OpenAI</a></li>
<li><a href="https://blog.getbind.co/openai-launches-rosalind-biodefense-to-put-frontier-ai-in-the-hands-of-pandemic-defenders/">OpenAI Launches Rosalind Biodefense to Put Frontier AI in the...</a></li>

</ul>
</details>

**Tags**: `#AI for Science`, `#Biodefense`, `#Public Health`, `#AI Safety`, `#Government AI`

---

<a id="item-9"></a>
## [Classical Computers Can Fully Simulate Complex Chemistry, Study Finds](https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/) ⭐️ 8.0/10

A decades-long research effort has produced a definitive result demonstrating that classical computers possess the algorithmic capability to fully simulate complex chemical reactions, challenging the prevailing assumption that such tasks inherently require quantum computers. This finding is significant because it redefines the computational boundaries for chemistry and computer science, potentially redirecting research priorities and funding away from the sole pursuit of quantum advantage for this specific problem. The breakthrough addresses the long-standing question of simulating strongly correlated electron systems, where the exponential scaling of complexity was thought to be a barrier only quantum computers could overcome, and the classical algorithm's exact details will be critical for future applications.

rss · Quanta Magazine · May 29, 13:54

**Background**: A fundamental goal of computational chemistry is to solve the electronic Schrödinger equation to predict molecular properties. For systems with strongly correlated electrons, the number of possible electronic configurations grows exponentially, a challenge known as the 'exponential wall.' This complexity led to the widespread belief that quantum computers, which natively handle quantum states, were necessary for exact simulations of such reactions.

<details><summary>References</summary>
<ul>
<li><a href="https://roibaer.huji.ac.il/galleries/expeditious-methods-electronic-structure-theory-and-many-body-techniques/">Expeditious Methods in Electronic Structure Theory and Many Body...</a></li>
<li><a href="https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.7.013191">Spin coupling is all you need: Encoding strong electron correlation in...</a></li>

</ul>
</details>

**Tags**: `#computational chemistry`, `#quantum computing`, `#classical simulation`, `#scientific breakthrough`, `#algorithm design`

---

<a id="item-10"></a>
## [Anthropic Surpasses OpenAI as Highest-Valued AI Startup](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html) ⭐️ 8.0/10

Anthropic has completed a new $65 billion funding round, resulting in a post-money valuation of $965 billion, which surpasses OpenAI's latest valuation of approximately $852 billion. This valuation milestone marks a significant shift in the competitive landscape of major AI companies, indicating strong investor confidence in Anthropic's strategy and technology over its primary rival. Anthropic is the company behind the Claude series of AI models, and the substantial new capital will primarily be used for computational resources, model training, and commercial expansion.

telegram · zaihuapd · May 29, 03:29

**Background**: Anthropic and OpenAI are two of the leading companies in the development of large-scale generative AI models. Such extremely high valuations reflect the massive capital flowing into the AI sector, which is highly dependent on expensive computing infrastructure and intensive research and development to train powerful foundation models.

**Tags**: `#AI Industry`, `#Venture Capital`, `#Anthropic`, `#OpenAI`, `#Startup Valuation`

---