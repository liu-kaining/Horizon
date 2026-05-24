---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 175 items, 7 important content pieces were selected

---

1. [Anthropic 的 Project Glasswing 项目利用 AI 发现逾万高危软件漏洞](#item-1) ⭐️ 9.0/10
2. [苹果开源 corecrypto 库，提供后量子算法的形式化验证证明](#item-2) ⭐️ 9.0/10
3. [微软财报披露 OpenAI 单季度净亏损 115 亿美元](#item-3) ⭐️ 9.0/10
4. [Anthropic 正完成逾 300 亿美元融资，估值有望超越 OpenAI](#item-4) ⭐️ 8.0/10
5. [OpenAI 详解用于可扩展低延迟语音 AI 的 WebRTC 架构](#item-5) ⭐️ 8.0/10
6. [z386：一个基于原始 Intel 微码的开源 80386 CPU](#item-6) ⭐️ 8.0/10
7. [微软内部推广 Anthropic 的 Claude Code，覆盖核心工程团队](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 的 Project Glasswing 项目利用 AI 发现逾万高危软件漏洞](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic 宣布其 Project Glasswing 计划，利用 Claude Mythos Preview 人工智能模型，在一个月内与约 50 个合作伙伴组织共同发现了超过一万个关键软件漏洞。 这代表了软件安全领域的一次范式转变，如此大规模、高速度的人工智能漏洞发现能力远超当前人类在验证、披露和修补方面的承受能力，迫使整个行业必须调整其修复流程。 在对上千个开源项目的扫描中，发现了 6,202 个高危漏洞，在已审查的子集（1,752 个）中，90.6% 为真阳性；Cloudflare 等合作伙伴报告称，漏洞发现速率提高了十倍以上。

telegram · zaihuapd · May 23, 03:16

**背景**: Project Glasswing 是 Anthropic 发起的一项协作安全倡议，旨在利用先进人工智能保护关键软件。Claude Mythos Preview 是 Anthropic 迄今为止能力最强的前沿模型，在多项基准测试中代表了重大飞跃。这一发现凸显了一个日益严峻的行业挑战：尽管人工智能发现漏洞的速度远超人类，但用于验证、披露和修补这些漏洞的人工流程却严重滞后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf">Claude Mythos Preview System Card - www-cdn.anthropic.com</a></li>
<li><a href="https://claude.com/product/claude-security">Claude Security | Claude by Anthropic</a></li>

</ul>
</details>

**社区讨论**: 讨论可能围绕其对软件安全和开源生态系统的重大影响展开。一个关键担忧是这给维护者带来了巨大压力，有报告显示，由于无法跟上修补进度，一些开源开发者已请求放缓漏洞报告的速度。

**标签**: `#AI Security`, `#Vulnerability Discovery`, `#Large Language Models`, `#Open Source`, `#Anthropic`

---

<a id="item-2"></a>
## [苹果开源 corecrypto 库，提供后量子算法的形式化验证证明](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

苹果发布了其 corecrypto 密码库的源代码，其中包含了 NIST 标准化的 ML-KEM 和 ML-DSA 后量子算法的实现，并附带了形式化验证的数学证明以确保其正确性。 此举为覆盖数十亿台苹果设备的基础密码库提供了关键的透明度和可验证的安全保障，为实施和验证抗量子密码学设立了新的行业标准。 形式化证明使用 Isabelle 证明助手创建，验证了 C 代码和手工优化的 ARM64 汇编代码与 NIST 规范严格一致。苹果还发布了定制的验证工具和 Isabelle 理论库，以供独立专家进行评估。

telegram · zaihuapd · May 23, 04:49

**背景**: 后量子密码学（PQC）是指设计为能够抵御未来量子计算机攻击的密码算法。ML-KEM（Kyber）和 ML-DSA（Dilithium）分别是 NIST 在 2024 年最终确定的用于密钥封装和数字签名的首个标准。形式化验证是一种使用数学证明来保证系统实现与其规范完全一致的技术，可以消除某些类别的错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kyber">ML - KEM - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_(proof_assistant)">Isabelle ( proof assistant ) - Wikipedia</a></li>
<li><a href="https://www.macrumors.com/2015/10/30/apple-opens-cryptographic-libraries/">Apple Opens Cryptographic Libraries to Third-Party Developers to Encourage Security - MacRumors</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#open-source`, `#formal-verification`, `#security`

---

<a id="item-3"></a>
## [微软财报披露 OpenAI 单季度净亏损 115 亿美元](https://t.me/zaihuapd/41537) ⭐️ 9.0/10

微软最新季度财务报告（采用权益法核算投资）披露，其按比例分担的 OpenAI 净亏损使微软自身的净利润减少了 31 亿美元。根据微软约 27% 的持股比例计算，这意味着 OpenAI 在该季度净亏损约 115 亿美元。 这一披露揭示了一家领先 AI 公司前所未有的、不可持续的资金消耗速度，凸显了当前人工智能产业巨大的资本密集度和显著的财务风险。它表明，在短期内将前沿 AI 开发转化为收入是一项严峻挑战。 计算得出的亏损是基于微软报告的权益法投资损益及其声明的持股比例（约 27%）；若使用税前亏损和稍高的报告持股比例（32.5%）计算，实际亏损可能超过 120 亿美元。该季度亏损额几乎是 OpenAI 报告的 2024 年上半年 43 亿美元营收的三倍。

telegram · zaihuapd · May 23, 07:40

**背景**: 权益法是一种会计处理方法，投资者在其利润表中确认其在被投资公司利润或亏损中所占的份额，通常适用于投资者具有重大影响（通常持股 20%-50%）的情况。OpenAI 是一家领先的人工智能研究机构，负责开发 GPT 系列大语言模型。微软是 OpenAI 的主要战略和财务投资者，已承诺投入数十亿美元资本，并将 OpenAI 的技术集成到其产品中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/权益法/9289851">权益法_百度百科 采用权益法核算的长期股权投资账务处理流程（附案例详解） 一文搞懂长期股权投资的核算方法：成本法、权益法和合并法 在阅读||#20998;... 权益法核算的长期股权投资收益_东奥会计在线 【老丁解税】权益法下投资收益的所得税处理解析 长期股权投资权益法 (长期股权投资核算方法) - 会计百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/496165358">长期股权投资——权益法（干货总结） - 知乎</a></li>

</ul>
</details>

**标签**: `#AI`, `#Finance`, `#OpenAI`, `#Microsoft`, `#Business`

---

<a id="item-4"></a>
## [Anthropic 正完成逾 300 亿美元融资，估值有望超越 OpenAI](https://www.ithome.com/0/954/452.htm) ⭐️ 8.0/10

据报道，Anthropic 正在敲定一轮超过 3000 亿美元的巨额融资，最快可能下周完成，这可能将其估值推高至 9000 亿美元以上。 这笔交易将使 Anthropic 成为全球估值最高的 AI 初创企业，超越 OpenAI，并表明投资者在竞争激烈的人工智能领域对 Anthropic 的技术和发展轨迹充满信心。 这轮融资需求旺盛，规模已超过 Anthropic 最初设定的 3000 亿美元目标，并在数周内迅速敲定；该公司还报告了收入的快速增长，预计年化营收将在下月底前突破 5000 亿美元。

rss · IT HOME · May 23, 15:12

**背景**: Anthropic 和 OpenAI 是领先的人工智能研究公司，致力于开发大语言模型，这是一种能够理解和生成类人文本的生成式人工智能。估值指的是在融资轮次中由投资者确定的私营公司的估计价值，而年化营收则是根据公司近期表现推算出的全年总营收。

**标签**: `#AI funding`, `#Anthropic`, `#valuation`, `#industry news`, `#OpenAI`

---

<a id="item-5"></a>
## [OpenAI 详解用于可扩展低延迟语音 AI 的 WebRTC 架构](https://www.infoq.cn/article/HzTpYj4SIqzFOHybIO2q?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

OpenAI 详细阐述了一种新颖的 WebRTC 架构，该架构用中继-收发器设计取代了传统的媒体终止模型，以支持全球规模的低延迟语音 AI。 这种架构转变意义重大，因为它使一个主要 AI 平台能够以低延迟和大规模支持语音 AI 应用（如 ChatGPT 语音），为实时对话系统设立了新标准。 该架构采用了无 SFU（选择性转发单元）设计，通过允许推理服务无需像 WebRTC 对等方那样运作来简化扩展，并为客户保留了标准的 WebRTC 行为。

rss · InfoQ 中文站 · May 23, 14:00

**背景**: WebRTC 是一个开源框架，支持浏览器和应用程序之间直接进行实时语音、视频和数据通信。低延迟语音 AI 指的是能够近实时地理解和回应人类语音的系统，这对于自然的对话界面至关重要。在全球范围内扩展此类系统，在为数百万用户保持一致、快速的性能方面面临着巨大挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.infoq.com/news/2026/05/openai-voice-ai-scale/">OpenAI Outlines WebRTC Architecture for Low-Latency Voice AI ...</a></li>
<li><a href="https://openai.com/index/delivering-low-latency-voice-ai-at-scale/">How OpenAI delivers low-latency voice AI at scale | OpenAI</a></li>
<li><a href="https://quantumzeitgeist.com/low-latency-voice-ai-openais-steps/">OpenAI’s 4 Steps to Low-Latency Voice AI at Global Scale</a></li>

</ul>
</details>

**标签**: `#AI`, `#WebRTC`, `#System Architecture`, `#Voice AI`, `#Real-Time Systems`

---

<a id="item-6"></a>
## [z386：一个基于原始 Intel 微码的开源 80386 CPU](https://nand2mario.github.io/posts/2026/z386/) ⭐️ 8.0/10

z386 项目成功创建了一个完全开源的、基于 FPGA 的 Intel 80386 CPU 实现，其构建核心是恢复的该处理器原始微码。 这项工作为 x86 架构的历史微码提供了一个独特的、可保存的硬件参考，使得爱好者和工程师能够进行更深入的研究、教育并忠实地保存复古计算硬件。 该实现建立在 z8086 项目的基础上，并融合了多位研究人员广泛的逆向工程工作，能够成功运行 DOS 和保护模式应用程序，包括经典游戏《毁灭战士》。

rss · Lobsters · May 23, 15:24

**背景**: 微码是 CPU 内部的一个低层指令层，它实现了软件所见的高层机器码指令。Intel 80386 是一款定义了现代 x86 架构的关键 32 位处理器。从历史芯片中逆向工程此类微码是一项极其复杂的任务，它使得研究人员能够理解处理器指令集在硬件层面的确切实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nand2mario.github.io/posts/2026/z386/">z386: An Open-Source 80386 Built Around Original Microcode - Small Things Retro</a></li>
<li><a href="https://bestcadpapers.com/comparisons-differences/z386-an-open-source-80386-built-around-original-microcode/">z386: An Open-Source 80386 Built Around Original Microcode - Best CAD papers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microcode">Microcode - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 该项目在 Lobsters 等技术社区引起了极大兴趣，讨论主要集中在逆向工程的非凡技术成就，以及此类项目对保存计算历史的价值。

**标签**: `#retro-computing`, `#CPU-design`, `#open-source-hardware`, `#reverse-engineering`, `#x86`

---

<a id="item-7"></a>
## [微软内部推广 Anthropic 的 Claude Code，覆盖核心工程团队](https://t.me/zaihuapd/41535) ⭐️ 8.0/10

微软正要求其核心工程团队（包括负责 Windows 和 Microsoft 365 的团队）在安装和使用 GitHub Copilot 的同时，也必须安装和使用 Anthropic 的 Claude Code，并鼓励非技术员工使用该工具进行原型设计。 此举标志着一个重大战略转变：一家科技巨头在其内部公开采用并推广直接竞争对手的人工智能工具，凸显了人工智能驱动的开发者工具市场竞争的加剧，并表明了一种务实的多供应商人工智能采用策略。 此次内部推广要求工程师并行使用 Claude Code 和 GitHub Copilot 并提供对比反馈，这表明微软正在积极地将竞争对手的产品与其自身的投资进行基准测试。

telegram · zaihuapd · May 23, 06:05

**背景**: Claude Code 是 Anthropic 推出的一款人工智能编程助手，可直接在开发者的终端或集成开发环境中运行，提供对代码库的上下文感知帮助和自动化功能。GitHub Copilot 是微软（通过 GitHub）广泛采用的人工智能结对编程工具。Anthropic 的模型近期在企业市场获得了显著发展势头，在企业使用的大语言模型市场份额上已超越 OpenAI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://techcrunch.com/2025/07/31/enterprises-prefer-anthropics-ai-models-over-anyone-elses-including-openais/">Enterprises prefer Anthropic's AI models over anyone else's ...</a></li>
<li><a href="https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/">Introducing Anthropic's Claude models in Microsoft Foundry ...</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#enterprise adoption`, `#Microsoft`, `#developer tools`, `#AI competition`

---