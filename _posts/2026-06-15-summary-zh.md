---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> From 178 items, 9 important content pieces were selected

---

1. [Linux 内核 7.1 发布，包含重大架构变更和新特性](#item-1) ⭐️ 10.0/10
2. [清华团队发现记忆重激活双向调节睡眠状态，成果登上《科学》](#item-2) ⭐️ 8.0/10
3. [OpenAI GPT-5.5 与 Codex 模型在亚马逊 Bedrock 平台上线](#item-3) ⭐️ 8.0/10
4. [RustWeek 演讲探讨用 Miri 进行高速 FFI 测试](#item-4) ⭐️ 8.0/10
5. [对苹果 Siri AI 隐私模型的批评性审视，指出其隐私缺陷。](#item-5) ⭐️ 8.0/10
6. [指南：通过更换显存芯片将 RTX 3070 显存翻倍至 16GB](#item-6) ⭐️ 8.0/10
7. [华为发布开源盘古 2.0 大模型，含 505B 与 92B 参数版本](#item-7) ⭐️ 8.0/10
8. [Anthropic 响应美国出口管制指令，暂停 Mythos 5 和 Fable 5 模型全球访问](#item-8) ⭐️ 8.0/10
9. [全球地下真菌网络总图首次绘出，规模巨大且碳封存作用关键](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Linux 内核 7.1 发布，包含重大架构变更和新特性](https://lwn.net/Articles/1077758/) ⭐️ 10.0/10

Linux 内核 7.1 版本已正式发布，带来了重大变更，包括移除了对一些旧款 486 架构的支持、新增了进程管理的 `clone()` 标志位、为异步 I/O 接口 io_uring 提供了 BPF 支持，以及完全重写了 NTFS 文件系统实现。 作为支撑全球服务器、台式机和嵌入式设备的基础技术，一次重要的稳定版内核发布直接影响着无数系统的稳定性、性能和硬件支持，而增强的调度器和 I/O 功能等新特性则为开发者和管理员提供了强大的新工具。 关键新增功能包括在可扩展调度类 (sched_ext) 中初步支持分层调度的子调度器、用户空间块设备驱动 ublk 的零拷贝 I/O，以及多项交换改进。此次发布也延续了清理工作，移除了对传统 CPU 架构的支持。

rss · LWN.net · Jun 14, 18:47

**背景**: Linux 内核是 Linux 操作系统的核心组件，负责管理硬件资源并为所有软件提供基础服务。io_uring 是一个高性能的异步 I/O 接口，旨在降低存储操作的系统调用开销。sched_ext 框架允许开发者通过 BPF 程序实现和加载自定义 CPU 调度器，为工作负载管理提供了前所未有的灵活性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">Io uring</a></li>
<li><a href="https://docs.kernel.org/block/ublk.html">Userspace block device driver (ublk driver) — The Linux Kernel documentation</a></li>
<li><a href="https://www.phoronix.com/news/cgroup-sub-scheduler-sched-ext">Sub-Scheduler Support Could Be One Of The Most Exciting Features To Come For Linux 7.1 - Phoronix</a></li>

</ul>
</details>

**标签**: `#linux`, `#kernel`, `#open-source`, `#operating-systems`, `#software-release`

---

<a id="item-2"></a>
## [清华团队发现记忆重激活双向调节睡眠状态，成果登上《科学》](https://www.ithome.com/0/964/240.htm) ⭐️ 8.0/10

清华大学与北京智源人工智能研究院的联合团队在《科学》杂志上首次发表研究，证实睡眠中的记忆重激活可以主动调控睡眠状态，同时记忆也会反过来影响睡眠。 这一发现建立了记忆与睡眠之间的双向调控机制，挑战了“睡眠仅单向促进记忆巩固”的传统观点，并指出记忆印迹细胞可能是治疗与抑郁症和慢性压力相关的睡眠障碍的潜在靶点。 负向记忆（如恐惧经历）在非快速眼动睡眠期间会重新激活，促使向觉醒状态转换，导致睡眠碎片化；而正向记忆的重激活则能促进并维持非快速眼动睡眠，这两种截然相反的效应由不同的下游神经通路介导。

rss · IT HOME · Jun 15, 01:49

**背景**: 传统的睡眠研究主要集中于睡眠如何加工和巩固记忆，但记忆可以主动塑造睡眠结构这一反向影响则鲜有深入探索。睡眠大致可分为非快速眼动睡眠（NREM）和快速眼动睡眠（REM）阶段，其中 NREM 睡眠对恢复性功能和记忆巩固尤为重要。记忆印迹细胞是在经历某事件时被激活的特定神经元群体，被认为储存了该事件的记忆痕迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tsinghua.edu.cn/info/1175/126722.htm">生命学院钟毅团队合作揭示记忆重激活调节睡眠的神经机制</a></li>
<li><a href="https://www.ithome.com/0/964/240.htm">为什么压力大会睡不好，清华团队新发现登上 Science - IT之家</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#sleep research`, `#memory`, `#brain science`, `#scientific breakthrough`

---

<a id="item-3"></a>
## [OpenAI GPT-5.5 与 Codex 模型在亚马逊 Bedrock 平台上线](https://www.infoq.cn/article/FuhAEYbk8T0b0GQZyq4c?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

OpenAI 最新的 GPT-5.5 语言模型及其 Codex 编程模型现已作为集成选项，在亚马逊的 Bedrock AI 服务中正式上线。 此集成为 AWS 上的企业客户提供了直接、受管理的途径来访问 OpenAI 的尖端模型，极大地简化了构建生成式 AI 应用程序的过程，无需管理底层基础设施。 亚马逊 Bedrock 是一项全托管的 AWS 服务，提供统一的 API 来访问来自不同 AI 供应商的基础模型，现在包括 OpenAI 的 GPT-5.5 和 Codex。

rss · InfoQ 中文站 · Jun 14, 10:00

**背景**: 亚马逊 Bedrock 是一项于 2023 年推出的云服务，允许开发者通过单一 API 访问多家公司的模型来构建生成式 AI 应用程序。OpenAI 的 Codex 是一个专为编程任务设计的 AI 模型，源自其 GPT 系列，为 GitHub Copilot 等工具提供支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Bedrock">Amazon Bedrock - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production scale – AWS</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cloud Computing`, `#OpenAI`, `#Amazon Web Services`, `#GPT`

---

<a id="item-4"></a>
## [RustWeek 演讲探讨用 Miri 进行高速 FFI 测试](https://youtu.be/9X-ngiKo_Y0) ⭐️ 8.0/10

在 RustWeek 上，Nia Deckers 做了一场演讲，展示了如何使用 Miri 以极高的速度运行和测试外部函数接口（FFI）代码，达到每秒 8000 次段错误。 测试 FFI 代码的内存安全性是 Rust 开发中的一个主要挑战，这种方法提供了一种高速检测不安全行为的方式，可能提高与 C/C++ 库交互的 Rust 项目的安全性和可靠性。 Miri 是一个检测未定义行为的 Rust 解释器，但将其应用于 FFI 代码具有挑战性，因为 FFI 调用涉及原始指针，并且超出了 Rust 的安全内存模型。

rss · Lobsters · Jun 14, 17:12

**背景**: Miri 是 Rust 中级中间表示（MIR）的实验性解释器，可以在测试期间检测各种形式的未定义行为。外部函数接口（FFI）允许 Rust 调用其他语言（如 C）编写的代码，但这需要使用 unsafe Rust 并处理原始指针，这可能导致内存安全问题，如段错误。段错误发生在程序尝试访问受限内存时，通常表示存在悬垂指针或缓冲区溢出等错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rust-lang/miri/">GitHub - rust-lang/miri: An interpreter for Rust's mid-level intermediate representation · GitHub</a></li>
<li><a href="https://doc.rust-lang.org/nomicon/ffi.html">Foreign Function Interface - Learn Rust</a></li>
<li><a href="https://en.wikipedia.org/wiki/Segmentation_fault">Segmentation fault - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 讨论可能提供了关于使用 Miri 进行 FFI 测试的实际挑战和潜力的宝贵社区见解，但此处未提供具体评论。

**标签**: `#Rust`, `#FFI`, `#Miri`, `#Testing`, `#Memory Safety`

---

<a id="item-5"></a>
## [对苹果 Siri AI 隐私模型的批评性审视，指出其隐私缺陷。](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/) ⭐️ 8.0/10

一项最新分析认为，苹果为其 Siri AI 助手实施的私有推理不足以保证真正的用户隐私，凸显了公司营销宣传与技术现实之间的差距。 这一批评意义重大，因为它挑战了一个主要科技平台 AI 产品的基本隐私承诺，引发了行业对当前隐私保护计算技术能否为消费级应用实现其宣称目标的更广泛担忧。 该分析具体批评了如差分隐私、安全多方计算和同态加密等技术在 AI 模型推理中的应用，认为它们可能遗留残余隐私漏洞或性能权衡，而这些并未向用户充分传达。

rss · Lobsters · Jun 14, 03:50

**背景**: 私有推理指的是允许 AI 模型处理用户数据，而服务提供商既看不到原始数据也看不到模型细节的技术。苹果曾将 Siri 的设备端处理和“私有云计算”宣传为隐私保障措施。涉及的关键技术包括差分隐私（向数据添加统计噪声）、安全多方计算（MPC，允许多方共同计算一个函数而不暴露各自的输入）以及同态加密（HE，能够直接在加密数据上进行计算）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://subscription.packtpub.com/book/data/9781800564671/7/ch07lvl1sec30/protecting-against-membership-inference-attacks">Chapter 5: Developing Applications with Differential Privacy Using...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>
<li><a href="https://ai.meta.com/research/publications/crypten-secure-multi-party-computation-meets-machine-learning/">CrypTen: Secure Multi-Party Computation Meets Machine Learning | Research - AI at Meta</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 讨论可能包含开发者和隐私研究人员之间实质性的技术辩论，焦点在于所提及隐私保护技术的具体技术限制以及在商业 AI 系统中实现强隐私保证的可行性。

**标签**: `#AI privacy`, `#Apple Siri`, `#cryptography`, `#machine learning`, `#privacy-preserving computation`

---

<a id="item-6"></a>
## [指南：通过更换显存芯片将 RTX 3070 显存翻倍至 16GB](https://hackaday.com/2026/06/14/double-the-vram-of-an-rtx-3070/) ⭐️ 8.0/10

一份详细的硬件改装指南已经发布，逐步介绍了如何通过物理更换 NVIDIA RTX 3070 显卡上的 GDDR6 显存芯片，将其显存容量从 8GB 翻倍至 16GB。 这种改装让用户能够克服一款流行中端 GPU 的显存限制，有可能延长其对于现代游戏以及对显存需求日益增长的 AI/机器学习工作负载的使用寿命。 该改装技术难度很高，需要先进的焊接技能来移除现有显存芯片并更换为更大容量的模块，成功与否取决于拥有正确的 PCB 原理图并确保固件兼容性。

rss · Hackaday · Jun 14, 08:00

**背景**: NVIDIA GeForce RTX 3070 是一款广泛使用的 Ampere 架构显卡，原厂配备 8GB GDDR6 显存。显存对于存储纹理、帧缓冲区以及其他 GPU 数据至关重要；显存不足会严重限制高分辨率游戏和复杂计算任务的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GDDR6_SDRAM">GDDR6 SDRAM - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/pcmasterrace/comments/12a2iz0/can_we_buy_micron_gddr6x_memory_chips_and/">r/pcmasterrace on Reddit: Can we buy micron GDDR6X memory chips and soldered them in to Graphics cards? Asking for a friend. He wants his 3070 Ti to 16GB</a></li>
<li><a href="https://forums.tomshardware.com/threads/upgrading-memory-modules-on-a-gpu.3714591/">[SOLVED] - Upgrading memory modules on a GPU | Tom's Hardware Forum</a></li>

</ul>
</details>

**社区讨论**: 虽然该指南提出了一种新颖的方法，但 Reddit 和 Tom's Hardware 等论坛上的社区讨论表明，这种改装风险极高，通常被普通用户认为不切实际，并且可能由于硬件锁定或难以找到完全匹配的显存芯片而无法实现。

**标签**: `#GPU`, `#hardware modding`, `#VRAM`, `#PC gaming`, `#hardware engineering`

---

<a id="item-7"></a>
## [华为发布开源盘古 2.0 大模型，含 505B 与 92B 参数版本](https://t.me/zaihuapd/41948) ⭐️ 8.0/10

在 2026 年华为开发者大会上，华为宣布开源其盘古 2.0 大语言模型系列，包括 5050 亿参数的 Pro 版本和 920 亿参数的 Flash 版本，这两个版本均针对其自研的昇腾 NPU 和鸿蒙生态系统进行了优化。 此次发布极大地推动了中国本土人工智能生态系统的发展，通过提供一个高性能的开源替代方案来挑战西方公司的模型，直接争夺全球领先地位，并有望加速基于华为硬件和软件栈的产业人工智能应用。 该模型支持长达 51.2 万 token 的上下文窗口，其中 Pro 版本使用 180 亿激活参数，Flash 版本使用 60 亿激活参数，并且华为计划从 6 月 30 日起陆续开源包括预训练代码在内的七大组件。

telegram · zaihuapd · Jun 14, 08:05

**背景**: 昇腾 NPU 是华为自主研发的 AI 加速器，是其构建独立于 NVIDIA GPU 的自研 AI 技术栈战略的关键部分。鸿蒙是华为面向多种设备的分布式操作系统，新版鸿蒙 6 引入了 AI 智能体框架以深度融合 AI 能力。盘古这类大语言模型（LLM）是基于海量文本数据训练的深度学习模型，旨在理解和生成人类语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/openpangu-2-complete-guide/">openPangu 2.0 Complete Guide: Huawei's 505B Model Trained ...</a></li>
<li><a href="https://www.panewslab.com/en/articles/019ebb7d-77a4-75e9-a5bc-e11af8f55293">Huawei releases open-source large-scale model Pangu 2.0: up ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarmonyOS">HarmonyOS - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Large Language Models`, `#Huawei`, `#Natural Language Processing`

---

<a id="item-8"></a>
## [Anthropic 响应美国出口管制指令，暂停 Mythos 5 和 Fable 5 模型全球访问](https://t.me/zaihuapd/41949) ⭐️ 8.0/10

在收到美国政府以国家安全为由发布的出口管制指令后，Anthropic 已暂时关闭其最先进的人工智能模型 Claude Fable 5 和 Claude Mythos 5 对所有客户的访问，包括居住在美国境内的外国公民。 此举代表了政府对人工智能行业一次重大的、开创性的干预，凸显了先进 AI 能力与国家安全政策日益交汇的趋势，可能会影响尖端 AI 技术的国际可访问性，并树立新的监管先例。 美国商务部的指令专门要求暂停所有外国公民的访问权限，但并未向 Anthropic 提供国家安全风险的具体细节，据报道这与模型可能被“越狱”用于潜在滥用的担忧有关；其他层级的 Claude 模型不受影响。

telegram · zaihuapd · Jun 14, 09:06

**背景**: Claude Fable 5 和 Claude Mythos 5 是 Anthropic 最新、最强大的人工智能模型，于数日前作为旨在处理复杂、长期项目的“Mythos 级”能力的一部分发布。“越狱”是指绕过人工智能模型安全训练、迫使其生成受限或有害输出的技术，随着模型能力不断增强，这已成为日益严重的关切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/technology/us-blocks-foreign-access-anthropics-most-advanced-ai-models-axios-reports-2026-06-13/">Anthropic disables top-tier AI models after US order limiting ...</a></li>
<li><a href="https://samsearch.co/government-contracting-news/us-export-controls-force-anthropic-to-suspend-global-access-to-ai-models-114075">U.S. Export Controls Force Anthropic to Suspend Global Access ...</a></li>
<li><a href="https://aisecurityandsafety.org/en/guides/jailbreaking-attacks/">Jailbreaking AI Models: Attack Patterns, Examples & Defenses ...</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#export controls`, `#Anthropic`, `#model access restrictions`, `#national security`

---

<a id="item-9"></a>
## [全球地下真菌网络总图首次绘出，规模巨大且碳封存作用关键](https://insideclimatenews.org/news/11062026/earths-massive-underground-fungal-networks/) ⭐️ 8.0/10

由地下网络保护协会（SPUN）领导的研究团队首次绘制出全球丛枝菌根真菌网络地图。该地图显示，地下菌丝总长度超过 1.1 亿亿公里，是地球与太阳之间距离的近十亿倍，总质量约为全人类体重的五倍。 这项绘图工作揭示了菌根网络至关重要的生态意义，它们与全球约 80%的植物共生，每年能将约 10 亿吨碳封存在地下。这些发现对理解气候变化减缓、农业可持续性和生态保护策略具有重大影响。 地图显示，农田中的真菌密度仅为野生生态系统的一半，而拥有全球约 40%该类真菌生物量的野生草原，正以森林四倍的速度被转为农田。这表明，农业扩张对这些至关重要的地下网络构成了具体而重大的威胁。

telegram · zaihuapd · Jun 14, 14:58

**背景**: 丛枝菌根真菌（AMF）是一种共生真菌，它们在地下形成复杂的网络，被称为'森林万维网'，连接着植物的根系。这些网络促进了植物与土壤之间的养分交换，例如真菌从土壤中获取磷和氮等养分，以换取植物提供的碳（糖分）。这种共生关系对植物健康和生态系统生产力至关重要，而真菌以稳定形式将碳封存在土壤中的作用，也是气候科学研究的关键领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.livescience.com/planet-earth/plants/earths-underground-fungal-network-is-so-massive-it-would-span-10-percent-of-the-milky-way-map-reveals">Earth's underground fungal network is so massive, it would span 10% of ...</a></li>
<li><a href="https://www.theguardian.com/science/2026/jun/11/arbuscular-mycorrhizal-fungi-plant-life-climate-global-mapping-study">Subterranean fungi networks more than 100 quadrillion km in length ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s44447-025-00023-w">Arbuscular mycorrhizal fungi (AMF): a pathway to sustainable soil...</a></li>

</ul>
</details>

**标签**: `#mycorrhizal_fungi`, `#ecology`, `#climate_science`, `#carbon_sequestration`, `#environmental_mapping`

---