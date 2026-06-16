---
layout: default
title: "Horizon Summary: 2026-06-16 (ZH)"
date: 2026-06-16
lang: zh
---

> From 210 items, 12 important content pieces were selected

---

1. [vLLM v0.23.0 发布：深度优化 DeepSeek-V4 并扩展 Model Runner V2](#item-1) ⭐️ 9.0/10
2. [LinkedIn 求职面试任务通过恶意 npm 包植入后门](#item-2) ⭐️ 8.0/10
3. [开发者用本地模型替代云端 AI 编程助手](#item-3) ⭐️ 8.0/10
4. [Tensordyne Napier AI 推理芯片宣称吞吐量达 NVIDIA Blackwell 的 13 倍](#item-4) ⭐️ 8.0/10
5. [SpaceX 转向自有渠道发布财报，创 IPO 募资纪录](#item-5) ⭐️ 8.0/10
6. [Gemma 4 12B 通过无编码器设计实现设备端多模态主动工作流](#item-6) ⭐️ 8.0/10
7. [编码智能体技术全景：上下文工程、子智能体与脚手架架构](#item-7) ⭐️ 8.0/10
8. [快手在复杂业务场景下对 RCA Agent 的探索实践](#item-8) ⭐️ 8.0/10
9. [苹果拟将 1.2 万亿参数 Gemini 模型整合进 Siri，以克服移动设备限制](#item-9) ⭐️ 8.0/10
10. [提议使用 HTTPS DNS 记录跳过 TLS 握手往返时间](#item-10) ⭐️ 8.0/10
11. [DROP TABLE 是 PostgreSQL 中唯一可扩展的数据删除方法](#item-11) ⭐️ 8.0/10
12. [美国政府出口管制指令迫使 Anthropic 关闭 Fable 5 和 Mythos 5 模型访问。](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.23.0 发布：深度优化 DeepSeek-V4 并扩展 Model Runner V2](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 9.0/10

vLLM v0.23.0 版本发布，该版本对 DeepSeek-V4 模型进行了全面的强化和优化，默认将 Model Runner V2 架构扩展至 Llama 和 Mistral 稠密模型，并推出了成熟的 Rust 前端，增加了新的端点和解析器。 这是 vLLM 推理引擎的一次重大更新，巩固了其对 DeepSeek-V4 等前沿模型的支持，并提升了核心架构的模块化和性能，这有利于整个专注于高效、可扩展大语言模型服务的 AI/ML 基础设施社区。 本次发布包含 200 位贡献者提交的 408 个代码，显著特性包括为 DeepSeek-V4 集成的 TRTLLM-gen 注意力内核、统一的解析器接口、带有对象存储层的多级 KV 缓存卸载，以及对 Transformers v5 的初步支持，但 Minimax M3 模型仍不受支持。

github · khluu · Jun 15, 05:27

**背景**: vLLM 是一个用于大语言模型推理与服务的高性能开源库，以其高效管理内存的 PagedAttention 技术而闻名。Model Runner V2 (MRv2) 是 vLLM 核心执行引擎的模块化、GPU 原生重写版本，旨在提升可维护性和速度。DeepSeek-V4 是 DeepSeek 推出的最新大语言模型，其稀疏 MLA（多头潜在注意力）架构需要专门的优化才能实现高效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/features/sparse-attention.html">Sparse Attention — TensorRT LLM</a></li>

</ul>
</details>

**标签**: `#llm-inference`, `#mlops`, `#model-serving`, `#performance-optimization`, `#open-source`

---

<a id="item-2"></a>
## [LinkedIn 求职面试任务通过恶意 npm 包植入后门](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 8.0/10

一名开发者在 LinkedIn 上收到一个虚假加密初创公司招聘人员的欺诈性工作邀请，其中包含一个 GitHub 仓库，内含一个恶意 Node.js 包，旨在受害者运行`npm install`时在其机器上执行任意代码。 此事件揭示了一种复杂的社会工程攻击向量，它利用了招聘过程中固有的信任以及开发者日常安装依赖包的惯例，对个人开发者及更广泛的软件供应链构成重大威胁。 恶意载荷隐藏在注释代码中，并被配置为在 npm `prepare`生命周期脚本期间自动运行，该脚本在标准的`npm install`之后执行，这意味着仅通过安装项目的依赖项就会激活后门。

hackernews · lwhsiao · Jun 15, 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48546294)

**背景**: npm 是 Node.js 的包管理器，允许包定义在不同阶段运行的生命周期脚本，例如`npm install`之后的`postinstall`或`prepare`。供应链攻击通过损害受信任的组件（如开源库）来攻击软件开发和分发过程，从而向其用户分发恶意代码。社会工程涉及心理操纵，诱骗人们执行操作或泄露机密信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/?v=true">scripts - npm Docs</a></li>
<li><a href="https://www.nodejs-security.com/blog/npm-ignore-scripts-best-practices-as-security-mitigation-for-malicious-packages">NPM Ignore Scripts Best Practices - nodejs-security.com</a></li>
<li><a href="https://cycode.com/blog/malicious-code-hidden-in-npm-packages/">One Threat to Unite Them All: Malicious Code Hidden in NPM Packages - Cycode</a></li>

</ul>
</details>

**社区讨论**: 社区强烈谴责了这次攻击，许多人分享了收到欺诈性面试任务的类似经历，凸显了这种攻击的可信度和普遍性。评论者对缺乏有效的举报渠道以及平台在删除恶意内容方面反应缓慢表示沮丧，同时也讨论了 GitHub 和 LinkedIn 等平台在防止此类滥用方面的责任。

**标签**: `#security`, `#social-engineering`, `#npm`, `#cybercrime`, `#software-development`

---

<a id="item-3"></a>
## [开发者用本地模型替代云端 AI 编程助手](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.0/10

一个拥有高参与度（748 分，358 条评论）的 Hacker News 帖子显示，开发者们正在分享他们完全用本地模型替代 Claude 和 GPT 等云端大语言模型，并将其作为主要日常编程工具的详细设置和真实体验。 这一转变凸显了一个日益增长的趋势：开发者通过将 AI 驱动的编程辅助从专有云服务转移到本地运行的开源模型，从而优先考虑数据隐私、降低成本并实现操作自主。 用户报告使用了特定硬件，如配备 128GB RAM 的 Mac Studio 或搭载双路 NVIDIA RTX 3090/RTX 6000 GPU 的设备来本地运行 Qwen3.6 和 Gemma 等模型，实现了约每秒 150 个 token 的推理速度，但他们也指出本地模型的能力尚不及 Claude Code 等前沿云端模型。

hackernews · cloudking · Jun 15, 14:46

**背景**: 基于云的编程助手，如 GitHub Copilot（由 GPT-4 等模型驱动）和 Anthropic 的 Claude，提供强大的 AI 辅助，但需要将代码发送到外部服务器。本地 LLM 推理是指在用户自己的硬件上运行开放权重模型，这提供了隐私保护且无需订阅费，但需要强大的计算资源。评估本地性能的关键指标包括每秒 token 数（tok/s），用于衡量生成速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Tokens_per_second">Tokens per second — Grokipedia</a></li>
<li><a href="https://benchlm.ai/llm-speed">LLM Speed & Latency Comparison — Tokens/sec, TTFT by Provider (2026) | BenchLM.ai</a></li>
<li><a href="https://vasilkoff.com/blog/vscodium-and-ollama">VSCodium + Ollama: Local LLM Coding Setup Guide</a></li>

</ul>
</details>

**社区讨论**: 讨论呈现出一种分裂但务实的观点：许多用户成功地将本地模型用于大部分个人编程工作，并重视隐私和成本节约；而另一些人则认为，鉴于当前的能力差距，不使用最新云端模型的机会成本太高，使得完全替代在专业工作流程中仍具挑战性。

**标签**: `#local-llm`, `#coding-assistants`, `#llm-inference`, `#privacy`, `#open-source-models`

---

<a id="item-4"></a>
## [Tensordyne Napier AI 推理芯片宣称吞吐量达 NVIDIA Blackwell 的 13 倍](https://www.ithome.com/0/964/688.htm) ⭐️ 8.0/10

初创公司 Tensordyne 发布了其 Napier AI 推理处理器，该芯片已成功流片并正采用台积电 3 纳米工艺制造，宣称其吞吐量比 NVIDIA 的 Blackwell 系统高 13 倍，且每词元能效提升 17 倍。 这一宣称若得到验证，将代表 AI 推理效率因采用对数数学方法而可能发生范式转变，可能挑战 NVIDIA 的主导地位，并大幅降低大规模 AI 部署的巨大能耗。 Napier 处理器采用对数数字系统（LNS），将复杂的乘法运算转换为更简单的加法运算，拥有 1380 亿个晶体管、256MB 片上 SRAM 缓存和 144GB HBM3E 内存，所有这些都被集成到一个包含 72 颗芯片的“推理舱”系统中。

rss · IT HOME · Jun 16, 02:33

**背景**: 对数数字系统（LNS）是浮点算术的一种替代方案，它通过将数字表示为对数值来简化乘法和除法运算，从而在特定操作中提供更高的速度和精度。当前 AI 硬件市场由 NVIDIA 等公司的 GPU 主导，初创公司正在探索 LNS 和小芯片等新颖架构，以克服推理和训练中的性能瓶颈与功耗限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/tensordyne-napier-ai-processor-announced-with-logarithmic-math/">Tensordyne Napier AI Processor Announced with Logarithmic Math - ServeTheHome</a></li>
<li><a href="https://www.forbes.com/sites/karlfreund/2026/06/15/tensordyne-revives-logarithmic-math-in-a-bid-to-cut-ai-power-use/">Tensordyne Revives Logarithmic Math In A Bid To Cut AI Power Use</a></li>
<li><a href="https://en.wikipedia.org/wiki/Logarithmic_number_system">Logarithmic number system - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Inference Accelerator`, `#Semiconductor`, `#Startup`, `#NVIDIA Competitor`

---

<a id="item-5"></a>
## [SpaceX 转向自有渠道发布财报，创 IPO 募资纪录](https://www.ithome.com/0/964/650.htm) ⭐️ 8.0/10

SpaceX 宣布，其季度及年度财务业绩和其他重大公告将仅通过公司官网及 X 平台的官方账号发布，不再使用传统的商业新闻专线服务。这一变化伴随着该公司创纪录的首次公开募股（IPO），承销商行使超额配售选择权（绿鞋机制）后，总募资额达到 857 亿美元。 此举标志着对标准企业通讯实践的重大背离，可能重塑大型公司发布关键财务信息和管理投资者关系的方式。这凸显了 SpaceX 独特的地位和影响力，使其能够利用其首席执行官埃隆·马斯克旗下 X 平台（前身为 Twitter）上的庞大直接受众，绕过传统的信息中间商。 财务业绩将仅发布在 SpaceX 网站的“投资者关系”板块及其 X 平台官方账号上，公司欢迎相关方关注这些渠道。在宣布当日，公司股价上涨约 19%，盘后交易中又上涨约 2%，反映出市场强烈的信心。

rss · IT HOME · Jun 16, 01:02

**背景**: 商业新闻专线服务（如 Business Wire 或 PR Newswire）长期以来一直是上市公司向媒体、金融机构和公众同步发布官方公告和财务数据的标准化、受监管渠道，以确保信息的广泛、公平和及时获取。“绿鞋机制”（超额配售选择权）是一种 IPO 稳定工具，它赋予承销商在需求旺盛时额外发售股份（通常为发行规模的 15%）的权利，以在上市后支撑股价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cj.sina.com.cn/articles/view/7879922977/1d5ae152101901akqi?froms=ggmp&vt=4">cj.sina.com.cn/articles/view/7879922977/1d5ae152101901akqi?froms...</a></li>
<li><a href="https://xueqiu.com/9741403476/316446573">xueqiu.com/9741403476/316446573</a></li>

</ul>
</details>

**标签**: `#corporate communications`, `#financial disclosure`, `#SpaceX`, `#IPO`, `#media strategy`

---

<a id="item-6"></a>
## [Gemma 4 12B 通过无编码器设计实现设备端多模态主动工作流](https://www.infoq.cn/article/7djN3gq1MaqGitDAPkhe?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

谷歌的新 Gemma 4 12B 模型移除了传统的独立视觉和音频编码器，使多模态输入能够直接流入大型语言模型主干。这使得复杂的、多步骤的代理工作流能够在配备约 16GB 显存的设备上本地运行。 这种无编码器架构代表了高效多模态 AI 部署的重大飞跃，显著降低了模型复杂性和资源需求。它将先进的代理 AI 能力带到了边缘设备和移动应用附近，可能加速其在现实世界中的采用。 该模型在本地运行时，其代理任务的性能接近谷歌更大的 260 亿参数模型。传统的多模态模型通常依赖独立的、冻结的视觉（1.5 亿至 5.5 亿参数）和音频（高达 3 亿参数）编码器，新设计消除了这些。

rss · InfoQ 中文站 · Jun 16, 09:44

**背景**: 多模态 AI 模型能够同时处理和理解多种类型的输入数据，例如文本、图像和声音。“代理工作流”指的是一个 AI 系统，它可以自主规划并执行一系列任务以实现目标，而不仅仅是对单个提示做出反应。Gemma 是谷歌为研究与开发设计的轻量级开放模型家族。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digg.com/ai/9ycprcp3">Google releases Gemma 4 12B, an encoder -free multimodal model ...</a></li>
<li><a href="https://www.labellerr.com/blog/gemma-4-12b-run-locally-and-fine-tune/">Gemma 4 12B : Run Locally, Fine-Tune, Benchmark Performance</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview | Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#multimodal-AI`, `#on-device-AI`, `#edge-computing`, `#efficient-ML`, `#Google-Gemma`

---

<a id="item-7"></a>
## [编码智能体技术全景：上下文工程、子智能体与脚手架架构](https://www.infoq.cn/article/UFLm5D5VDPmu9Ykc9CdJ?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

一篇综合性分析文章深入剖析了过去一年编码智能体设计的主要范式转移，具体探讨了上下文工程的兴起、子智能体架构的演进，以及作为核心组件的脚手架框架的出现。 该综合梳理帮助开发者和架构师系统性地理解快速演变的 AI 辅助软件工程格局，从而更好地把握当前趋势，并为工具采用和系统设计做出明智决策。 分析指出，上下文工程现已成为管理 AI 智能体上下文窗口信息输入、压缩和检索的关键实践；子智能体架构通过将任务委托给专门模型来管理复杂性和上下文限制；而脚手架工程则专注于构建外围代码、配置和逻辑，以引导和信任智能体行动。

rss · InfoQ 中文站 · Jun 15, 10:31

**背景**: 编码智能体是旨在辅助或自动化软件开发任务的 AI 系统。上下文工程是一种精心策划 AI 模型可“查看”信息以优化其性能的刻意实践，因为更大的上下文窗口并不自动意味着更好的结果。子智能体是由主编排智能体分配任务的次级、专业化 AI 进程，用于管理负载和上下文。脚手架（Harness）指的是包裹和引导 AI 智能体的所有非模型代码、配置和执行逻辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html">Context Engineering for Coding Agents</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>
<li><a href="https://spring.io/blog/2026/01/27/spring-ai-agentic-patterns-4-task-subagents/">Spring AI Agentic Patterns (Part 4): Subagent Orchestration</a></li>
<li><a href="https://martinfowler.com/articles/harness-engineering.html">Harness engineering for coding agent users</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#AI-engineering`, `#context-engineering`, `#software-development`, `#paradigm-shift`

---

<a id="item-8"></a>
## [快手在复杂业务场景下对 RCA Agent 的探索实践](https://www.infoq.cn/article/dSexstkokyRe1TIkcBLW?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

快手的一位高级服务器架构师分享了在大型复杂业务系统中，部署 AI 驱动的根因分析(RCA) Agent 的实践经验和新颖方法。 这项工作展示了 AI 智能体在大规模技术运维中提升系统可靠性的实际应用，为解决真实世界的 AIOps 挑战和推进故障诊断自动化提供了宝贵见解。 重点在于将 AI 智能体应用于快手这类大型互联网公司的业务特定场景，以处理其复杂性和规模，旨在超越通用的根因分析工具，实现定制化解决方案。

rss · InfoQ 中文站 · Jun 15, 10:20

**背景**: 根因分析(RCA)是识别系统故障或问题的根本原因的过程。AIOps 利用人工智能和机器学习来自动化和增强 IT 运维任务，包括监控、事件关联和根因分析。在此背景下，AI 智能体指能够感知环境、做出决策并采取行动（例如分析日志和指标）以实现诊断故障等目标的自主系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://logz.io/platform/features/ai-powered-root-cause-analysis/">Logz.io AI Agent for RCA - AI -Powered Root Cause Analysis</a></li>
<li><a href="https://sciencelogic.com/articles/automated-root-cause-analysis">Automated Root Cause Analysis | ScienceLogic</a></li>
<li><a href="https://www.reddit.com/r/sre/comments/1exsd2j/automated_root_cause_analysis/">r/sre on Reddit: Automated Root Cause Analysis</a></li>

</ul>
</details>

**社区讨论**: 提供的搜索结果包含关于 AIOps 和自动化 RCA 的通用行业讨论，其中有人对新工具如何与现有工具区分表示怀疑。然而，没有包含与快手文章相关的具体评论，因此无法获知社区反应。

**标签**: `#AI agents`, `#root cause analysis`, `#system reliability`, `#AIOps`, `#large-scale systems`

---

<a id="item-9"></a>
## [苹果拟将 1.2 万亿参数 Gemini 模型整合进 Siri，以克服移动设备限制](https://www.infoq.cn/article/LSwQ3hQpZ1INX40icTSE?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

据报道，苹果计划在 2026 年全球开发者大会上宣布将谷歌 1.2 万亿参数的 Gemini AI 模型整合到其 Siri 语音助手，这标志着因计算限制而发生的重大战略转变。 此举标志着苹果在 AI 竞赛中向谷歌做出重大让步，凸显了行业当前无法在消费移动设备上完全运行最先进大型语言模型的现状，并将竞争格局推向以云为基础的解决方案。 据报道，该庞大的 1.2 万亿参数模型将在苹果自有的 Private Cloud Compute 服务器上运行，以在苹果生态系统内处理用户数据，谷歌将因此获得 10 亿美元的年度合同。

rss · InfoQ 中文站 · Jun 15, 10:00

**背景**: 大型语言模型是基于海量数据集训练以理解和生成人类语言的人工智能系统，参数数量通常越多表示能力越强。运行如此庞大的模型需要巨大的计算能力，因此常在“设备端”推理（注重隐私和速度）与“云端”推理（注重算力）之间做出权衡。谷歌的 Gemini 是一系列先进的多模态大型语言模型，以其巨大的上下文窗口和强劲性能而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://themauritiustimes.com/business/apples-1-2-trillion-parameter-problem-why-it-needs-googles-1b-ai/">Apple's 1 . 2 Trillion Parameter Problem... - THE MAURITIUS TIMES</a></li>
<li><a href="https://dwtvnews.com/business/googles-1-2-trillion-parameter-ai-model-wins-1b-apple-contract/">Google's 1 . 2 Trillion Parameter AI Model Wins... - DW TV NEWS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#Apple`, `#Google Gemini`, `#Large Language Models`, `#Mobile Computing`

---

<a id="item-10"></a>
## [提议使用 HTTPS DNS 记录跳过 TLS 握手往返时间](https://savearoundtrip.com/) ⭐️ 8.0/10

一项名为“savearoundtrip”的提议建议发布 HTTPS DNS 记录（特别是 SVCB 记录），以消除 HTTPS 连接建立 TLS 握手过程中的一个往返时间。 此优化能显著降低 HTTPS 连接的延迟，提升用户网络性能，并通过提高初始连接建立效率来减轻服务器负载。 该方法利用了 RFC 8484 中定义的 HTTPS DNS 记录类型，该类型可传输服务绑定（SVCB）信息，包括端点的 IP 地址和端口，从而允许客户端将 DNS 查询和 TLS ClientHello 消息合并到一个往返时间中。

rss · Lobsters · Jun 15, 18:36

**背景**: 标准的 TLS 1.2 握手通常需要客户端和服务器之间两个往返时间（四条消息）才能开始安全数据传输。较新的 TLS 1.3 将其减少到一个往返时间，而像 TLS False Start 这样的技术可以进一步优化。SVCB（服务绑定）及其特定的'HTTPS'类型等 DNS 记录允许一个域宣告替代连接端点和参数，超越了仅提供 IP 地址的简单 A/AAAA 记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hosting.nl/en/support/wat-is-een-https-dns-record-en-hoe-voeg-je-een-http-dns-record-toe/">Add an HTTPS DNS record (and what is it really) | Hosting.NL</a></li>
<li><a href="https://hpbn.co/transport-layer-security-tls/">Networking 101: Transport Layer Security ( TLS ) - High Performance...</a></li>
<li><a href="https://kb.isc.org/docs/svcb-and-https-resource-records-what-are-they">SVCB and HTTPS resource records - what are they?</a></li>

</ul>
</details>

**社区讨论**: Lobsters 上的相关讨论可能包含关于此方法的可行性、安全影响以及与现有优化（如 TLS 1.3 和连接复用）相比的实际性能提升的技术辩论。

**标签**: `#networking`, `#DNS`, `#performance-optimization`, `#HTTPS`

---

<a id="item-11"></a>
## [DROP TABLE 是 PostgreSQL 中唯一可扩展的数据删除方法](https://planetscale.com/blog/the-only-scalable-delete) ⭐️ 8.0/10

PlanetScale 的一篇博文指出，在 PostgreSQL 中删除大量数据时，唯一能够真正实现扩展且不会导致性能显著下降的操作是 DROP TABLE。 这一观点挑战了使用 DELETE 或 TRUNCATE 进行大规模数据清理的常见做法，迫使数据库工程师重新考虑模式设计，特别是通过表分区等技术，以实现高性能和可扩展的数据生命周期管理。 核心的技术问题是 DELETE 不会立即释放磁盘空间，需要后续的 VACUUM 操作来回收空间，这可能会很慢且资源密集。TRUNCATE 速度更快，但会锁定表，并且仅适用于整个表或分区，而 DROP TABLE 几乎是一个瞬时的元数据操作。

rss · Lobsters · Jun 15, 05:55

**背景**: PostgreSQL 使用多版本并发控制（MVCC），DELETE 操作只是将行标记为已删除，而不是立即将其移除。之后自动清理（autovacuum）进程会清理这些死元组以回收空间，但在高删除量的情况下，这可能成为一个瓶颈。表分区将一个大表拆分为更小、更易管理的部分（例如按日期），从而允许 DROP TABLE 或 TRUNCATE 等操作针对特定分区进行高效的批量删除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/PostgreSQL/comments/1d705i7/vacuum_vs_vacuum_full_simple_explanation/">Vacuum vs Vacuum full - Simple explanation ? : r/PostgreSQL - Reddit</a></li>
<li><a href="https://practicaldev-herokuapp-com.global.ssl.fastly.net/stringintech/optimizing-postgresql-mass-deletions-with-table-partitioning-4ai4">Optimizing PostgreSQL Mass Deletions with Table Partitioning</a></li>
<li><a href="https://www.cybertec-postgresql.com/en/postgresql-delete-vs-truncate/">PostgreSQL: DELETE vs. TRUNCATE</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 评论区可能讨论了这种方法的实际权衡，例如管理分区的操作开销、DROP TABLE 对复制和逻辑解码的影响，以及是否可以通过替代的 PostgreSQL 配置（例如使用 fillfactor、频繁清理）来缓解所述的局限性。

**标签**: `#postgresql`, `#database-performance`, `#data-deletion`, `#scalability`, `#system-design`

---

<a id="item-12"></a>
## [美国政府出口管制指令迫使 Anthropic 关闭 Fable 5 和 Mythos 5 模型访问。](https://t.me/zaihuapd/41962) ⭐️ 8.0/10

美国政府向 Anthropic 发出国家安全指令，迫使该公司暂停所有客户对 Fable 5 和 Mythos 5 AI 模型的访问，包括外国员工，原因是担忧模型被越狱带来的风险。 此次行动代表了对人工智能开发的重大监管干预，直接影响了对顶级性能模型的访问，并为国家安全关切如何凌驾于商业人工智能部署之上树立了先例。 该指令来自美国商务部，Anthropic 已确认其他 Claude 模型不受影响，并正努力尽快恢复对暂停模型的访问。

telegram · zaihuapd · Jun 15, 10:09

**背景**: Anthropic 最近发布了 Claude Fable 5 和 Mythos 5 作为其最新的前沿模型，其中 Fable 5 是高性能模型，而 Mythos 5 则是共享同一基础但更注重安全性的变体。AI 越狱是指用于绕过人工智能模型内置安全防护栏的技术，各国政府越来越将其视为国家安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 - Anthropic</a></li>
<li><a href="https://www.reddit.com/r/OutOfTheLoop/comments/1u4g6i4/whats_up_with_anthropics_fable_5_and_mythos_5_llm/">What's up with Anthropic's Fable 5 and Mythos 5 LLM models and them now being suspended? : r/OutOfTheLoop - Reddit</a></li>

</ul>
</details>

**社区讨论**: Reddit 等平台上的在线讨论显示，许多用户认为 Fable 5 是用于编码和智能体工作等任务的最佳可用模型，并且对这些模型是否会恢复公共访问存在重大不确定性与担忧。

**标签**: `#AI governance`, `#export controls`, `#national security`, `#Anthropic`, `#model access`

---