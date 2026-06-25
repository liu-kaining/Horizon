---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> From 199 items, 13 important content pieces were selected

---

1. [OpenAI 推出首款定制人工智能推理芯片“Jalapeno”，由博通打造。](#item-1) ⭐️ 9.0/10
2. [Anthropic 指控阿里巴巴通过大规模蒸馏攻击窃取 Claude 能力。](#item-2) ⭐️ 9.0/10
3. [高通发布 Dragonfly 数据中心产品组合，包含 HBC 架构、C1000 CPU 和 AI300 加速器](#item-3) ⭐️ 8.0/10
4. [报告：OpenHarmony 登顶全球，中国开发者贡献度 7 年后有望超越美国](#item-4) ⭐️ 8.0/10
5. [全球最大产能高丰度硼-10 同位素装置在山东投产，实现战略材料自主可控。](#item-5) ⭐️ 8.0/10
6. [TRM 思考奖励模型量化大模型推理过程，以 ICML 2026 口头报告形式发表。](#item-6) ⭐️ 8.0/10
7. [Databricks 领导者呼吁为 AI 代理云构建开放生态系统](#item-7) ⭐️ 8.0/10
8. [提案中的 HTTP QUERY 方法，用于安全的带请求体查询](#item-8) ⭐️ 8.0/10
9. [中国“LineShine”成为全球最快超级计算机，算力突破 2 百亿亿次](#item-9) ⭐️ 8.0/10
10. [台积电将全线上调先进制程代工价格，涨幅 5%-10%](#item-10) ⭐️ 8.0/10
11. [Cloudflare 与浏览器厂商提议用 PACT 协议和加密令牌取代验证码](#item-11) ⭐️ 8.0/10
12. [美光 2026 财年第三财季营收同比暴增 346%，AI 驱动存储需求爆发](#item-12) ⭐️ 8.0/10
13. [谷歌 Play 商店 6 月 30 日起在美国、英国和欧洲经济区启用外部计费](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 推出首款定制人工智能推理芯片“Jalapeno”，由博通打造。](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 发布了其首款定制人工智能芯片 Jalapeno，这是一款与博通合作开发、由台积电制造的推理加速器。据报道，该芯片从设计到生产仅用时九个月，OpenAI 声称其自身的 AI 模型被用于加速设计和优化流程。 此举标志着 OpenAI 在人工智能硬件领域向垂直整合迈出的重大战略转变，使其能够减少对通用 GPU 处理关键推理工作负载的依赖。随着推理成为人工智能服务的主要成本和利润中心，拥有底层芯片可以提供显著的效率提升和持久的竞争优势。 Jalapeno 专为推理设计，即运行已训练好的人工智能模型以生成输出的过程，这一阶段在规模化时通常需要数万颗芯片。OpenAI 声称其自身模型在九个月内加速了该芯片的开发，但这一说法在社区中受到一些质疑，关于这一具体贡献的细节仍然很少。

hackernews · jamdesk · Jun 24, 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: 人工智能工作负载大致分为训练和推理。训练是教导模型的计算密集型过程，而推理是使用模型的持续过程。随着服务规模扩大，推理正迅速成为人工智能公司的主要成本，这使得专用推理芯片成为战略要地。垂直整合，即公司设计自己的硬件以紧密优化其软件栈，是谷歌（通过其 TPU）等主要人工智能参与者中正在兴起的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.granitefirm.com/blog/us/2025/08/24/ai-inference-chips/">AI inference chips vs. training chips - Andy Lin's Long-term Stock Investment Blog</a></li>
<li><a href="https://www.datacenterknowledge.com/data-center-chips/inference-becomes-the-next-ai-chip-battleground">Inference Becomes the Next AI Chip Battleground</a></li>
<li><a href="https://fourweekmba.com/google-the-most-complete-vertical-integrator-in-ai/">Google: The Most Complete Vertical Integrator in AI - FourWeekMBA</a></li>

</ul>
</details>

**社区讨论**: 社区讨论参与度很高，但情绪褒贬不一，一些人对定制硬件可能带来的效率提升感到兴奋，但对营销声明持怀疑态度，特别是关于使用 AI 模型加速设计的说法。评论者还指出台积电作为制造商的重要性，并将 OpenAI 的举措与谷歌长期运行的 TPU 项目进行了比较，一些人则提出了更激进的概念，比如将模型权重直接烧录到硅片中。

**标签**: `#AI_hardware`, `#custom_chips`, `#OpenAI`, `#Broadcom`, `#inference`

---

<a id="item-2"></a>
## [Anthropic 指控阿里巴巴通过大规模蒸馏攻击窃取 Claude 能力。](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html) ⭐️ 9.0/10

Anthropic 正式指控阿里巴巴及其 Qwen 实验室在 2026 年 4 月 22 日至 6 月 5 日期间，使用近 2.5 万个欺诈账户与 Claude 模型进行了超过 2880 万次交互，并称这是该公司迄今已知的最大规模蒸馏攻击。 此项指控揭示了一种严重且新颖的 AI 知识产权盗窃形式，可能加速中国追赶美国先进 AI 模型（如 Anthropic 的 Mythos Preview）的能力，加剧了两国间的技术竞争。 此次指控的攻击涉及大量、集中且重复的查询，符合蒸馏攻击的特征；指控是以致美国参议院银行委员会信函的形式提出的，时间恰逢 AI 听证会前夕，且紧随美国对 Anthropic 最强模型实施出口限制之后。

telegram · zaihuapd · Jun 25, 01:36

**背景**: 模型蒸馏是一种技术，指较弱的 AI 模型通过研究更强模型的输出来学习复制其能力。在此背景下，它指的是竞争对手通过反复查询专有模型的 API 来非法提取知识的攻击。此指控发生在美国就 AI 领导权和安全问题与中国紧张关系加剧的背景下，包括美国政府近期限制先进 AI 技术出口的行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Medium</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#intellectual property`, `#US-China relations`, `#model distillation`, `#AI security`

---

<a id="item-3"></a>
## [高通发布 Dragonfly 数据中心产品组合，包含 HBC 架构、C1000 CPU 和 AI300 加速器](https://www.ithome.com/0/968/257.htm) ⭐️ 8.0/10

高通宣布了其 Dragonfly 数据中心产品套件，其中包括新颖的高带宽计算（HBC）架构、面向数据中心工作负载的 C1000 CPU 以及 AI300 推理加速器。HBC 架构采用 3D 堆叠设计，将计算单元置于 LPDDR DRAM 下方实现近内存计算，与传统的 HBM 系统相比，可实现显著更高的带宽和每瓦能效。 此次发布标志着高通大举进军数据中心市场，以一种旨在突破人工智能工作负载“内存墙”瓶颈的架构直接挑战行业巨头。如果成功，HBC 所声称的每瓦带宽和更低总拥有成本方面的优势，可能会重塑人工智能加速器的内存架构，并影响与英伟达和超威半导体的竞争格局。 HBC 架构声称其每瓦带宽是 HBM 的 6 倍，每瓦容量是 SRAM 的 200 倍；基于第一代 HBC 的 AI250 加速器计划于 2027 年中启动商业化样品测试。预计于 2028 年上市的 Dragonfly C1000 CPU 可扩展至 250 个以上 Oryon 内核，并支持 PCIe Gen 7 和 CXL 规范。

rss · IT HOME · Jun 25, 01:12

**背景**: HBM（高带宽内存）是一种广泛应用于高性能 GPU 和加速器的堆叠内存技术，但其不断增长的功耗导致数据中心总拥有成本（TCO）升高。近内存计算是一种将处理单元放置在靠近内存位置以减少数据移动、从而提高性能和效率的架构方法。高通的 HBC 架构是这一概念的具体实现，它利用硅通孔（TSV）技术将 LPDDR DRAM 芯片直接堆叠在计算单元之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://partofstyle.com/qualcomms-hbc-puts-compute-under-dram-to-break-ais-memory-bottleneck-with-6x-hbm-efficiency/">Qualcomm’s HBC Puts Compute Under DRAM to Break AI’s Memory ...</a></li>
<li><a href="https://wccftech.com/qualcomm-hbc-stacks-compute-beneath-dram-to-smash-the-ai-memory-wall/">Qualcomm's HBC Stacks Compute Beneath DRAM To Smash The AI Memory Wall, Claiming 6x The Bandwidth Per Watt Of HBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#data center`, `#AI accelerator`, `#Qualcomm`, `#hardware architecture`, `#near-memory computing`

---

<a id="item-4"></a>
## [报告：OpenHarmony 登顶全球，中国开发者贡献度 7 年后有望超越美国](https://www.ithome.com/0/968/251.htm) ⭐️ 8.0/10

开源社发布的《2025 中国开源年度报告》指出，中国在 GitHub 平台的活跃开发者已超 210 万，OpenHarmony 等项目以 OpenRank 值登顶全球榜首。 该报告凸显了中国在全球开源生态系统中加速提升的影响力，预示了开发者贡献领先地位的潜在转变，并反映了国家技术战略和国际协作的更广泛趋势。 尽管中国在 GitHub 上的活跃开发者数量约为美国的三分之一，但其贡献影响力（OpenRank）已达到美国总贡献度的近 50%，且增速差超过 10%，有望在七年内超越美国成为全球第一。

rss · IT HOME · Jun 25, 01:02

**背景**: OpenHarmony 是开放原子开源基金会旗下的开源项目，于 2020 年启动，旨在为智能设备提供分布式操作系统基础。OpenRank 是一种衡量开源项目活跃度和影响力的指标，通过分析开发者协作数据来提供比星标数或贡献者数更全面的评估。开源社是 2014 年成立的中国重要非营利组织，致力于推广开源文化与协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://open-digger.cn/en/docs/user-docs/metrics/openrank">OpenRank Algorithm - OpenDigger</a></li>
<li><a href="https://cn.linkedin.com/company/kaiyuanshe">KAIYUANSHE 开 源 社 | 领英</a></li>

</ul>
</details>

**标签**: `#open-source`, `#developer-ecosystem`, `#China-tech`, `#global-trends`, `#OpenHarmony`

---

<a id="item-5"></a>
## [全球最大产能高丰度硼-10 同位素装置在山东投产，实现战略材料自主可控。](https://www.ithome.com/0/968/247.htm) ⭐️ 8.0/10

中国在山东东营成功投产全球最大产能的高丰度硼-10 同位素生产装置。该装置仅用一年半时间完成从设计到投产的全流程，目前已稳定产出 25 吨合格产品，硼-10 丰度最高达 99.7%。 这一突破打破了海外企业对高丰度硼-10 同位素核心技术和高端市场的垄断，使中国在核电和高端医疗等领域能够实现关键材料的自主可控。此举使中国跻身于少数掌握该同位素规模化制备技术的国家之列。 该项目由上海化工研究院有限公司牵头，仅用一年半时间就完成了百吨级装置从设计、建设到投产的全流程，并实现一次性开车成功。目前达到的 99.7%硼-10 丰度仍有进一步提升空间。

rss · IT HOME · Jun 25, 00:50

**背景**: 硼-10 是硼的一种稳定同位素，拥有极高的中子俘获截面，是控制核反应和屏蔽辐射的关键材料。它主要用作核反应堆控制棒和安全系统中的中子吸收材料，同时也应用于硼中子俘获疗法（BNCT）等先进癌症治疗领域。其工业规模提纯通常涉及三氟化硼（BF₃）化学交换蒸馏等复杂工艺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Control_rod">Control rod - Wikipedia</a></li>
<li><a href="https://pdf.benchchem.com/1234/A_Comparative_Analysis_of_Boron_10_Enrichment_Techniques_for_Researchers_and_Drug_Development_Professionals.pdf">A Comparative Analysis of Boron-10 Enrichment Techniques for ...</a></li>
<li><a href="https://www.nuclear-power.com/glossary/boron-10/applications-of-boron-nuclear-power/">Applications of Boron - Nuclear Power</a></li>

</ul>
</details>

**标签**: `#strategic materials`, `#nuclear technology`, `#isotope production`, `#advanced manufacturing`, `#technology sovereignty`

---

<a id="item-6"></a>
## [TRM 思考奖励模型量化大模型推理过程，以 ICML 2026 口头报告形式发表。](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247899199&idx=3&sn=b0d6764e50d881295fd85b75f8f9434a) ⭐️ 8.0/10

一种新的思考奖励模型（TRM）被提出，用于定量评估大语言模型的中间推理过程，而不仅仅是最终答案的正确性。该模型在 ICML 2026 会议上以口头报告形式发表。 这项研究意义重大，因为它为 AI 推理提供了一个更细粒度的评估框架，能够通过奖励合理的思考过程来改进大模型的训练和对齐。它直接解决了当前 AI 评估中的一个关键限制，即正确答案可能掩盖了有缺陷的推理过程。 该项目包含一个开源实现，并获得了社区的广泛关注，其 GitHub 仓库已积累 4.2k 星。研究团队还构建了专门的 TRM-偏好数据集用于训练和评估。

rss · 量子位 · Jun 24, 04:00

**背景**: 在人工智能领域，奖励模型通常用于通过对输出进行评分来使语言模型与人类偏好对齐。传统模型往往只评估最终答案，但过程奖励模型（PRMs）旨在评估中间的推理步骤。思考奖励模型（TRM）是一种具体的方法，它基于这些中间过程来建模奖励，以提供更清晰的训练信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/thinking-supervised-reward-model-trm">Thinking -supervised Reward Model ( TRM )</a></li>
<li><a href="https://eu.36kr.com/en/p/3866659734279170">TRM Thinking Reward Model Launched: Large Models ' Reasoning...</a></li>
<li><a href="https://icml.cc/virtual/2026/events/oral">ICML 2026 Orals</a></li>

</ul>
</details>

**社区讨论**: 该项目的开源实现获得了社区的极大关注，其高 GitHub 星数就是明证。这表明社区对能够评估和改进 AI 推理质量（而不仅仅是结果）的工具有强烈需求。

**标签**: `#Large Language Models`, `#AI Evaluation`, `#Reward Modeling`, `#Reasoning`, `#Open Source`

---

<a id="item-7"></a>
## [Databricks 领导者呼吁为 AI 代理云构建开放生态系统](https://www.latent.space/p/databricks) ⭐️ 8.0/10

Databricks 联合创始人马泰·扎哈里亚和雷诺·辛进行了一次罕见的联合采访，主张开放生态系统对于每家公司构建自己的'代理云'至关重要。 这一来自 Apache Spark 创造者的倡导，凸显了 AI 代理平台向开放、可互操作方向发展的潜在行业趋势，这有助于防止供应商锁定，并在云人工智能的下一波浪潮中促进更广泛的创新。 '代理云'的概念指的是自主 AI 代理交互和运作的平台，而 Databricks 一直有开源 Unity Catalog 等核心组件的历史，以支持其开放生态系统战略。

rss · Latent Space · Jun 24, 18:53

**背景**: '代理云'是一个新兴概念，描述了一个多个 AI 代理可以自主协作和执行任务的云环境。Databricks 以创建统一数据平台湖仓一体而闻名，一贯倡导开源和开放标准以避免供应商锁定，其开源用于数据和 AI 治理的 Unity Catalog 就是明证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open">Databricks Open Sources Unity Catalog, Creating the... - Databricks</a></li>
<li><a href="https://www.linkedin.com/pulse/why-databricks-open-source-strategy-matters-more-than-stratulat-uarhe">Why Databricks ’ Open Source Strategy Matters More to the Business...</a></li>
<li><a href="https://medium.com/@philippeandrepage/ai-agent-clouds-c8cf588f7392">Autonomous Agent Clouds . A Conceptual Framework for... | Medium</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#cloud computing`, `#open ecosystem`, `#Databricks`, `#industry trends`

---

<a id="item-8"></a>
## [提案中的 HTTP QUERY 方法，用于安全的带请求体查询](https://httpwg.org/http-extensions/draft-ietf-httpbis-safe-method-w-body.html#section-1-5.2) ⭐️ 8.0/10

一项名为 QUERY 的新 HTTP 方法正作为协议扩展被提出。该方法被设计为安全且幂等的，同时允许在请求体中发送复杂的查询参数。 这解决了 HTTP 协议中一个长期存在的限制，即像 GET 这样的安全操作不鼓励使用请求体，迫使开发者将大型查询编码到 URL 中。它能够为复杂查询实现更具表现力和更高效的 API 设计。 QUERY 方法必须保持安全性和幂等性，这是实现缓存和可靠重试所必需的特性，这使其与 POST 等方法区别开来。它的采用将取决于客户端、服务器以及代理等中间件的广泛生态系统支持。

rss · Lobsters · Jun 24, 20:04

**背景**: 在 HTTP 协议中，'安全'的方法不会改变服务器状态，而'幂等'的方法可以多次调用且效果相同。广泛使用的 GET 方法是安全且幂等的，但其规范不鼓励包含请求体，这使得复杂查询变得繁琐。QUERY 提案旨在正式引入一种新的、安全的、幂等的方法，并明确支持请求体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Safe/HTTP">Safe ( HTTP Methods ) - Glossary | MDN</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET">GET request method - HTTP | MDN</a></li>
<li><a href="https://lists.w3.org/Archives/Public/ietf-http-wg/2024JulSep/0102.html">Method Mania from Josh Cohen on 2024-07-25 (ietf- http -wg@w3.org...)</a></li>

</ul>
</details>

**社区讨论**: 相关链接的 Lobsters 社区讨论显示出高度参与的技术辩论。主要观点包括评估其在复杂查询中相对于 GraphQL 的使用场景，讨论其对现有缓存机制可能产生的影响，以及将其与替代方案（如使用特殊头的 POST 或 SEARCH 方法）进行比较。

**标签**: `#HTTP`, `#web-standards`, `#API-design`, `#protocol`, `#specification`

---

<a id="item-9"></a>
## [中国“LineShine”成为全球最快超级计算机，算力突破 2 百亿亿次](https://hackaday.com/2026/06/24/lineshine-is-fastest-supercomputer-at-over-2-exaflops/) ⭐️ 8.0/10

中国的“LineShine”超级计算机在 TOP500 榜单中首次登顶，成为全球首台持续性能超过 2 百亿亿次浮点运算（exaflops）的系统。 这一成就标志着高性能计算领域的一个重要里程碑，展示了计算能力的巨大飞跃，将对全球范围内的前沿科学研究、人工智能和工业模拟产生深远影响。 该系统采用全 CPU 架构，搭载了国产的基于 Armv9 指令集的 LX2 处理器，每颗处理器拥有 304 个核心，部署于深圳国家超算中心。

rss · Hackaday · Jun 25, 02:00

**背景**: 百亿亿次（Exascale）计算指的是能够执行至少每秒 10^18 次浮点运算（FLOPS）的计算系统，此前只有极少数机器达到这一里程碑。TOP500 项目根据高性能 Linpack（HPL）基准测试对全球最强大的超级计算机进行排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.top500.org/news/lineshine-debuts-no-1-top500-enters-new-global-exascale-era/">LineShine Debuts at No. 1 as the TOP500 Enters a New Global ...</a></li>
<li><a href="https://www.hpcwire.com/2026/04/28/china-unveils-2-exaflop-all-cpu-lineshine-supercomputer/">China Unveils 2 Exaflop, All-CPU ‘LineShine’ Supercomputer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Exascale_computing">Exascale computing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#supercomputing`, `#high-performance-computing`, `#exaflops`, `#computer-science`, `#benchmark`

---

<a id="item-10"></a>
## [台积电将全线上调先进制程代工价格，涨幅 5%-10%](https://36kr.com/newsflashes/3866472254411779) ⭐️ 8.0/10

台积电已通知客户，将对所有先进制程节点（包括 7nm 及以下）的晶圆代工价格进行上调，整体涨幅约为 5%至 10%。 此次涨价影响了台积电约 75%的晶圆营收，并可能推高众多下游科技产品的生产成本，波及全球半导体供应链。 此次涨价不仅涵盖市场传闻的 3nm 制程，更扩展到 7nm 及以下所有先进节点，表明台积电对其技术最尖端产品线进行了全面调整。

telegram · zaihuapd · Jun 24, 05:45

**背景**: 台湾积体电路制造公司（台积电）是全球最大的芯片代工厂商，为苹果、英伟达、AMD 等主要客户生产先进集成电路。7nm 和 3nm 等制程节点指的是制造技术的特征尺寸，数字越小通常代表芯片越先进、性能越强、能效越高。晶圆代工定价是整个电子行业的关键因素，直接影响智能手机、计算机和数据中心的成本。

**标签**: `#semiconductors`, `#supply chain`, `#TSMC`, `#foundry`, `#pricing`

---

<a id="item-11"></a>
## [Cloudflare 与浏览器厂商提议用 PACT 协议和加密令牌取代验证码](https://www.techtimes.com/articles/318891/20260623/cloudflare-chrome-firefox-plan-replace-captchas-cryptographic-tokens.htm) ⭐️ 8.0/10

Cloudflare 联合 Chrome、Firefox、Edge 和 Shopify 提出了 PACT 协议，该协议旨在用基于 IETF Privacy Pass 技术的匿名加密令牌取代传统的验证码。 该提案有望通过消除侵入性验证码任务，同时仍能验证人类用户，从而显著提升用户隐私和浏览体验，影响数十亿用户和主要平台的网络安标准。 该协议使用盲签名密码学从可信站点颁发令牌，允许用户访问其他网站而不泄露身份或浏览历史，并且它也解决了区分合法 AI 代理与恶意机器人的问题。

telegram · zaihuapd · Jun 24, 06:30

**背景**: 验证码（CAPTCHA，全自动区分计算机和人类的图灵测试）被广泛用于阻止机器人，但常因烦人且存在可访问性问题而受到批评。Privacy Pass 是一个现有的 IETF 协议，使用盲签名实现匿名认证。盲签名密码学是一种技术，允许签名者对消息进行签名而不了解消息内容，从而保护用户匿名性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://privacypass.github.io/">Privacy Pass</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blind_signature">Blind signature - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/draft-ietf-privacypass-protocol-01">Privacy Pass Protocol Specification (Internet-Draft, 2021)</a></li>

</ul>
</details>

**标签**: `#web-security`, `#privacy`, `#protocols`, `#CAPTCHA-alternatives`, `#cryptography`

---

<a id="item-12"></a>
## [美光 2026 财年第三财季营收同比暴增 346%，AI 驱动存储需求爆发](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) ⭐️ 8.0/10

美光科技公布了创纪录的 2026 财年第三财季业绩，营收同比暴增 346%至 414.6 亿美元，这主要受 AI 基础设施对高性能内存的爆发式需求驱动，并给出了强劲的下季度指引，预计营收将达 500 亿美元。 这一前所未有的财务表现凸显了高带宽内存在推动 AI 革命中关键且日益增长的作用，表明内存已成为 AI 基础设施的主要瓶颈和成本驱动因素。 公司的盈利能力达到了非凡水平，季度净利润高达 282.4 亿美元，非 GAAP 毛利率飙升至 84.9%。美光已签署 16 份长期战略协议以锁定未来 3 至 5 年的订单，并预计内存短缺将持续至 2027 年以后。

telegram · zaihuapd · Jun 24, 22:22

**背景**: 高带宽内存是一种专为 AI 加速器设计的高性能 DRAM，采用 3D 堆叠架构，可提供巨大的数据带宽。AI 模型的爆炸式增长已导致全球内存市场出现结构性短缺，使其从周期性波动转变为持续性的供应危机。这种需求正在将内存从大宗商品组件转变为整个计算栈中关键的、限制性能的核心要素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://assets.micron.com/adobe/assets/urn:aaid:aem:8a68fc66-7658-4d0a-98ef-3d70f93181a2/renditions/original/as/import_of_mem_in_hi_perf_compute_and_ai_white_paper.pdf">The Importance of Memory in High-Performance Computing and AI</a></li>
<li><a href="https://enkiai.com/ai-market-intelligence/ai-memory-crisis-2026-unpacking-the-global-shortage/">AI Memory Crisis 2026: Unpacking the Global Shortage</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#financial-results`, `#AI-infrastructure`, `#memory-chips`, `#market-trends`

---

<a id="item-13"></a>
## [谷歌 Play 商店 6 月 30 日起在美国、英国和欧洲经济区启用外部计费](https://android-developers.googleblog.com/2026/06/play-expanded-billing.html) ⭐️ 8.0/10

自 2026 年 6 月 30 日起，谷歌将允许美国、英国和欧洲经济区的符合条件的开发者提供第三方或基于网页的支付系统，并与谷歌 Play 计费系统并行，同时实施新的费率结构，将首年 100 万美元收入的基准服务费降至 10%。 这一重大政策转变显著提高了开发者的计费灵活性，可能降低他们的成本并赋予其更多货币化控制权，从而重塑全球关键市场的应用商业模式。 新的费率结构将 Play 服务费与单独的结算费分开；在这些地区，使用谷歌 Play 计费的交易需额外支付 5%的结算费，而使用替代计费或外部链接的交易则无需支付。参与谷歌“Level Up”或“Apps Experience”计划的开发者从 9 月起还将享受更低费率。

telegram · zaihuapd · Jun 25, 02:33

**背景**: 谷歌 Play 历来要求应用内销售的大部分数字商品和服务使用其自有计费系统，并收取高达 30%的佣金。此举是在监管压力和法律和解之后做出的，特别是在欧盟，这些因素推动了应用商店运营商允许替代支付选项。欧洲经济区（EEA）包括欧盟成员国以及冰岛、列支敦士登和挪威，形成一个具有共同经济规则的统一市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://android-developers.googleblog.com/2026/06/play-expanded-billing.html">Android Developers Blog: Expanded billing choice and lower fees on...</a></li>
<li><a href="https://9to5google.com/2026/06/24/google-play-store-external-billing-june-30/">Google Play Store opens external billing starting June 30</a></li>
<li><a href="https://www.3u.com/news/details/15063/google-lowering-play-store-fees-and-allowing-alternative-payments-worldwide">Google Lowering Play Store Fees and Allowing Alternative... - 3uTools</a></li>

</ul>
</details>

**标签**: `#Google Play Store`, `#App Billing`, `#Developer Policy`, `#Mobile Ecosystem`, `#Monetization`

---