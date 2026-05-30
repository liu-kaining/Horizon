---
layout: default
title: "Horizon Summary: 2026-05-30 (ZH)"
date: 2026-05-30
lang: zh
---

> From 199 items, 10 important content pieces were selected

---

1. [vLLM v0.22.0 发布，支持 DeepSeek V4、NVFP4 及实验性 Rust 前端。](#item-1) ⭐️ 9.0/10
2. [Claude Mythos AI 在开源项目中发现超 2.3 万个漏洞](#item-2) ⭐️ 9.0/10
3. [蓝色起源新格伦火箭静态点火测试爆炸，NASA 登月计划受重创。](#item-3) ⭐️ 9.0/10
4. [华为发布“韬定律”，以“时间缩微”替代摩尔定律](#item-4) ⭐️ 9.0/10
5. [“死亡经济”理论：人工智能取代消费者，有引发通缩螺旋的风险。](#item-5) ⭐️ 8.0/10
6. [OpenAI 升级 GPT-5.5 Instant 模型使回复更自然，并宣布淘汰旧模型](#item-6) ⭐️ 8.0/10
7. [中国载人登月计划进展顺利，将于 2028-2030 年执行任务](#item-7) ⭐️ 8.0/10
8. [OpenAI 推出 Rosalind Biodefense 计划，提供 GPT-Rosalind 访问权限](#item-8) ⭐️ 8.0/10
9. [研究发现，经典计算机能够完全模拟复杂化学反应](#item-9) ⭐️ 8.0/10
10. [Anthropic 估值超过 OpenAI，成为最高估值 AI 初创公司](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.22.0 发布，支持 DeepSeek V4、NVFP4 及实验性 Rust 前端。](https://github.com/vllm-project/vllm/releases/tag/v0.22.0) ⭐️ 9.0/10

vLLM v0.22.0 是一次重大更新，强化了对 DeepSeek V4 模型的支持，包括 NVFP4 融合 MoE，并新增了多令牌预测 (MTP) 推测解码以及实验性的 Rust 前端。此次发布还推进了 Model Runner V2 架构，包含来自 230 位贡献者的 459 个提交。 此次发布显著提升了 DeepSeek V4 等大型混合专家 (MoE) 模型的推理效率，并通过推测解码和高性能 Rust 前端扩展了 vLLM 的能力，有可能为大语言模型服务性能和开发工具设定新标准。 主要新增功能包括对 DeepSeek V4 的 NVFP4 融合 MoE 支持、超出 CPU 内存的多层 KV 缓存卸载，以及通过 Cutlass FP8 实现的批处理不变推理，延迟降低了 28.9%。Model Runner V2 现在成为 Qwen3 稠密模型的默认选项，并包含睡眠模式权重重载等功能。

github · khluu · May 29, 10:28

**背景**: vLLM 是一个高性能的开源库，专为快速高效地推理和部署大语言模型 (LLM) 而设计。推测解码是一种技术，它使用一个更小、更快的“草稿”模型一次提议多个令牌，然后由主模型并行验证以提高输出速度。混合专家 (MoE) 是一种模型架构，其中不同的参数子集（专家）会根据不同的输入被激活，从而提高大型模型的效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/moe_kernel_features/">Fused MoE Kernel Features - vLLM</a></li>
<li><a href="https://huggingface.co/kernels/Atlas-Inference/nvfp4-moe">Atlas-Inference/nvfp4-moe - Kernel - Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference-optimization`, `#deep-learning`, `#open-source`, `#performance`

---

<a id="item-2"></a>
## [Claude Mythos AI 在开源项目中发现超 2.3 万个漏洞](https://www.v2ex.com/t/1216615#reply5) ⭐️ 9.0/10

Anthropic 的 Claude Mythos Preview 模型已扫描超过 1000 个开源项目，发现了估计 23019 个漏洞，其中一家独立安全公司抽样验证了 1752 个高危或严重级别漏洞，确认 90.6%（1587 个）为有效漏洞。 这表明 AI 现在能够以前所未有的规模和速度发现漏洞，可能自动化大部分安全研究工作，并迫使网络安全行业改变其漏洞验证和补丁修复的流程。 该模型能力过于强大，Anthropic 在开发出更完善的防护系统之前暂不对外发布，仅通过其“玻璃翼计划”向可信赖的合作伙伴提供访问权限，该计划已承诺投入 1 亿美元模型使用额度用于研究。

rss · V2EX · May 30, 02:02

**背景**: Claude Mythos 是 Anthropic 公司推出的一款专门用于发现软件漏洞的 AI 模型。漏洞发现（或称“挖洞”）是指在软件中寻找可能被攻击者利用的安全缺陷的过程。开源项目是源代码公开的软件，它们是关键基础设施，通常由人工和自动化工具共同进行安全审计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/glasswing-initial-update">Project Glasswing: An initial update</a></li>
<li><a href="https://quantumzeitgeist.com/mythos-preview-vulnerabilities-partnership-identifies/">Mythos Preview Identifies 10,000+ Vulnerabilities With Partners</a></li>
<li><a href="https://www.elisity.com/blog/claude-mythos-ai-vulnerability-discovery-microsegmentation-unpatchable-devices">Claude Mythos Found 27-Year-Old Bugs. Your Unpatchable Devices...</a></li>

</ul>
</details>

**社区讨论**: V2EX 的讨论帖显示出极大的兴趣和猜测，用户们询问是否有人真正使用过该预览版，并辩论这是否意味着继编程之后，漏洞研究将是下一个被 AI 颠覆的工作。

**标签**: `#AI_security`, `#vulnerability_discovery`, `#Anthropic`, `#cybersecurity`, `#automation`

---

<a id="item-3"></a>
## [蓝色起源新格伦火箭静态点火测试爆炸，NASA 登月计划受重创。](https://arstechnica.com/space/2026/05/blue-origins-new-glenn-rocket-just-exploded-during-a-static-fire-test/) ⭐️ 9.0/10

2026 年 5 月 28 日晚，蓝色起源公司的新格伦火箭在卡纳维拉尔角 36 号发射台进行静态点火测试时发生剧烈爆炸，导致一级和二级火箭完全报废，发射台的闪电防护塔倒塌，地面基础设施严重损毁。 此次事故是蓝色起源旗舰火箭的重大挫折，预计将延迟该公司为 NASA 阿尔忒弥斯计划人类着陆系统以及亚马逊柯伊伯计划卫星提供的发射服务，进而影响整个商业航天发射能力和深空探索时间表。 爆炸发生在为 NG-4 任务做准备期间，该任务原计划发射 48 颗亚马逊柯伊伯宽带卫星；事故原因正在调查中，修复和复飞的时间表尚未公布。

telegram · zaihuapd · May 29, 11:08

**背景**: 新格伦是蓝色起源设计的大型可重复使用轨道火箭，旨在与 SpaceX 的猎鹰重型火箭等运载工具竞争，其第一级由七台 BE-4 甲烷发动机提供动力。蓝色起源被 NASA 选中，负责开发作为阿尔忒弥斯计划人类着陆系统一部分的蓝月亮着陆器，这是将宇航员送回月球表面的关键组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/New_Glenn">New Glenn - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BE-4">BE-4 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human_Landing_System">Human Landing System - Wikipedia</a></li>

</ul>
</details>

**标签**: `#space`, `#rocket launch`, `#NASA`, `#Blue Origin`, `#Artemis program`

---

<a id="item-4"></a>
## [华为发布“韬定律”，以“时间缩微”替代摩尔定律](https://t.me/zaihuapd/41648) ⭐️ 9.0/10

在 2026 年上海举行的 IEEE 国际电路与系统研讨会上，华为宣布了“韬定律”，这是一种以“时间缩微”替代“几何缩微”的半导体演进新原则。华为表示，过去六年已依据该定律设计并量产了 381 款芯片。 随着传统的几何缩放（摩尔定律）接近物理和经济极限，这一提议为半导体行业提供了一个潜在的范式转变，为继续提升芯片密度和性能提供了另一条路径。 韬定律通过“逻辑折叠”架构实现，该架构将逻辑电路物理折叠和堆叠，据报告可将晶体管密度提高 55%，能效提升 41%。华为目标在 2031 年前生产出晶体管密度等效于 1.4 纳米工艺水平的芯片，首个商业应用将是其即将推出的麒麟移动芯片。

telegram · zaihuapd · May 30, 02:18

**背景**: 摩尔定律，即观察到芯片上的晶体管数量大约每两年翻一番，几十年来一直是半导体发展的驱动力。然而，随着晶体管尺寸缩小到原子尺度，几何缩微变得越来越困难和昂贵。韬定律提出将重点从缩小物理尺寸（几何缩微）转向优化跨整个系统层级的时间相关参数，如信号延迟和时钟周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huawei.com/en/news/2026/5/ieee-iscas-tau-scaling">HUAWEI Presents the Tau (τ) Scaling Law, Enabling Breakthroughs in Transistor Density and System Performance - Huawei</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/huawei-claims-sanctions-busting-breakthrough-with-1-4nm-class-chips-by-2031-claims-55-percent-higher-transistor-density-firm-claims-new-logicfolding-chip-architecture-can-bypass-euv-restrictions-introduces-tau-scaling-law-to-replace-moores-law">Huawei claims sanctions-busting breakthrough with 1.4nm-class chips by 2031, claims 55% higher transistor density — firm claims new LogicFolding chip architecture can bypass EUV restrictions, introduces 'Tau Scaling Law' to replace Moore's Law | Tom's Hardware</a></li>
<li><a href="https://chinarxiv.org/items/chinaxiv-202605.00224">A Time Scaling Theory for Multi-Layer Electronic Systems</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#Huawei`, `#Moore's Law`, `#chip design`, `#paradigm shift`

---

<a id="item-5"></a>
## [“死亡经济”理论：人工智能取代消费者，有引发通缩螺旋的风险。](https://www.owenmcgrann.com/p/the-dead-economy-theory) ⭐️ 8.0/10

文章提出了“死亡经济”理论，认为广泛采用人工智能驱动的自动化可能通过取代既是工人的消费者，从而引发通缩性反馈循环，最终摧毁其试图服务的市场需求。 该理论挑战了关于技术进步的普遍叙事，指出了人工智能应用中的一个根本性矛盾：它可能会侵蚀自身的客户基础，这与当前关于自动化和就业替代的经济辩论高度相关。 该理论的核心观点是，当公司用人工智能取代人类员工以削减成本时，它们同时也削弱了总消费能力，导致商品和服务（包括人工智能生产的产品）的需求下降。

hackernews · WillDaSilva · May 29, 15:46 · [社区讨论](https://news.ycombinator.com/item?id=48324712)

**背景**: 该理论类比了经济学中的通缩螺旋，即价格下跌导致生产减少、工资下降和需求进一步萎缩。历史先例，如发达国家劳动力大规模从农业转出，表明经济可以适应，但该理论质疑人工智能驱动的转变是否会造成独特的破坏性。技术性失业，即创新可能导致失业的概念，是经济学家长期争论的话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deflation">Deflation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Technological_unemployment">Technological unemployment - Wikipedia</a></li>
<li><a href="https://news.lavx.hu/article/the-dead-economy-theory-why-ai-driven-automation-may-collapse-demand">The Dead Economy Theory – Why AI ‑Driven Automation May...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论非常活跃，评论将印度受到补贴、劳动密集型农业类比为一种“被扶持”但低效的体系。其他用户推测科技行业的产能过剩，质疑大型团队的生产力，并认为人工智能可能只是在自动化一个已经过剩的劳动力市场。一些评论探讨了极端逻辑终点，即一个完全自动化的经济将没有人类消费者。

**标签**: `#AI economics`, `#automation impact`, `#deflation`, `#labor markets`, `#technological unemployment`

---

<a id="item-6"></a>
## [OpenAI 升级 GPT-5.5 Instant 模型使回复更自然，并宣布淘汰旧模型](https://www.ithome.com/0/957/437.htm) ⭐️ 8.0/10

OpenAI 于 2026 年 5 月 28 日更新了 GPT-5.5 Instant 模型，使其生成的回复更自然、易读、结构更清晰，并减少了冗长的列表。该公司还宣布将逐步淘汰 OpenAI o3 和 GPT-4.5 模型，它们的移除日期分别定为 2026 年 8 月 26 日和 2026 年 6 月 27 日。 此次更新是提升数百万用户核心默认模型可用性和可靠性的重大一步，直接解决了人们对人工智能生成文本质量和幻觉的常见抱怨。淘汰旧模型标志着 OpenAI 生态系统的整合，引导用户和开发者转向更新、更强大的架构。 GPT-5.5 Instant 模型于 2026 年 5 月 5 日取代 GPT-5.3 Instant 成为免费用户的 ChatGPT 默认模型，其在医学、法律和金融等高风险主题上的幻觉减少了 52.5%。一个值得注意的变化是，GPT-5.5 Instant 和 GPT-5.5 Thinking 将不再提供 Canvas 功能，这是一个用于文本和代码的专用工作空间，但付费用户在旧模型退役前有一段宽限期可以继续使用。

rss · IT HOME · May 30, 02:14

**背景**: GPT-5.5 Instant 是 OpenAI 的 GPT-5.5 模型架构的一个版本，专为快速、低延迟的回复而调优，是许多 ChatGPT 用户的默认模型。OpenAI o3 模型是作为先进的“推理”模型推出的，是 o1 模型的继任者，旨在处理需要深度思考的复杂任务。ChatGPT 中的 Canvas 功能提供了一个独立的、结构化的面板，用于起草和编辑长文本或代码，提供了一个比标准聊天界面更专注的工作空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-5-5-instant-system-card/">GPT-5.5 Instant System Card | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-canvas/">Introducing canvas | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.5`, `#AI model updates`, `#ChatGPT`, `#model deprecation`

---

<a id="item-7"></a>
## [中国载人登月计划进展顺利，将于 2028-2030 年执行任务](https://www.ithome.com/0/957/384.htm) ⭐️ 8.0/10

中国首飞航天员、载人航天工程副总设计师杨利伟正式确认，载人登月计划推进正常。计划于 2028 年至 2030 年间，在文昌航天发射场密集执行 3 次无人绕月验证任务及 1 次载人登月任务。 这一带有具体时间表的确认，标志着中国航天战略从近地轨道正式迈向地月空间，使其成为新一轮月球探索竞赛的主要参与者。这是建立地球轨道以外可持续人类存在的关键一步，对未来深空探索和国际太空合作具有重要意义。 任务将使用长征十号火箭和新一代载人飞船，两者均已在去年和今年年初进行了测试。杨利伟在 2023 年曾表示，登月航天员的选拔将优先考虑有飞行经验的航天员。

rss · IT HOME · May 29, 14:55

**背景**: 位于海南的文昌航天发射场是中国最靠南、最新的发射场，靠近赤道，为向月球等高轨道发射提供了燃料效率优势。中国现行的载人航天计划“神舟”系列已在近地轨道运行了二十余年。此次规划的任务是生命保障、航天器再入和重型运载火箭技术数十年发展的结晶。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wenchang_Space_Launch_Site">Wenchang Space Launch Site - Wikipedia</a></li>
<li><a href="https://www.bbc.com/zhongwen/simp/china/2013/06/130611_china_shenzhou_timeline">资料：中国“ 神 舟 ” 载 人 航天历史 - BBC News 中文</a></li>
<li><a href="https://www.dutenews.com/n/article/10668438">飞 船 返回舱成功着陆， 神 二 十 一乘组到家了</a></li>

</ul>
</details>

**标签**: `#space exploration`, `#China`, `#manned spaceflight`, `#lunar mission`, `#engineering`

---

<a id="item-8"></a>
## [OpenAI 推出 Rosalind Biodefense 计划，提供 GPT-Rosalind 访问权限](https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense) ⭐️ 8.0/10

OpenAI 推出了 Rosalind Biodefense 计划，该计划向经过审核的开发者和美国政府合作伙伴提供其 GPT-Rosalind 模型的访问权限，以推进生物防御和大流行病防备工作。 这项举措意义重大，因为它将强大的前沿人工智能能力战略性地引向应对关键的公共卫生和国家安全挑战，可能加速开发生物威胁早期检测和应对的工具。 该计划建立在 OpenAI 现有的安全与韧性工作基础之上，被描述为支持‘防御性加速’，专注于诊断、防备和响应方面的应用，而非开放式研究。

rss · OpenAI Blog · May 29, 03:00

**背景**: GPT-Rosalind 是 OpenAI 为生命科学研究设计的一个专用人工智能模型，通过一个可信访问计划提供，而非广泛向公众开放。生物防御的概念涉及保护民众免受生物威胁，包括自然发生的大流行病和蓄意的生物恐怖主义，这一关切的重要性日益增长。前沿人工智能指的是处于能力尖端的最先进、最强大的人工智能系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-rosalind/">Introducing GPT - Rosalind for life sciences research | OpenAI</a></li>
<li><a href="https://blog.getbind.co/openai-launches-rosalind-biodefense-to-put-frontier-ai-in-the-hands-of-pandemic-defenders/">OpenAI Launches Rosalind Biodefense to Put Frontier AI in the...</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Biodefense`, `#Public Health`, `#AI Safety`, `#Government AI`

---

<a id="item-9"></a>
## [研究发现，经典计算机能够完全模拟复杂化学反应](https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/) ⭐️ 8.0/10

一项历经数十年的研究最终得出明确结果，证明经典计算机在算法层面拥有完全模拟复杂化学反应的能力，这挑战了此类任务本质上需要量子计算机的普遍假设。 这一发现意义重大，因为它重新定义了化学和计算机科学领域的计算边界，可能将研究重点和资金从单纯追求解决此特定问题的量子优势上转移开。 这一突破解决了模拟强关联电子体系这一长期存在的难题，在该领域，指数级的计算复杂度增长曾被认为只有量子计算机才能克服，而该经典算法的具体细节对未来应用至关重要。

rss · Quanta Magazine · May 29, 13:54

**背景**: 计算化学的一个根本目标是求解电子薛定谔方程以预测分子性质。对于具有强关联电子的体系，可能的电子构型数量呈指数级增长，这一挑战被称为‘指数壁垒’。这种复杂性导致了一种普遍观点，即天生处理量子态的量子计算机是精确模拟此类反应所必需的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://roibaer.huji.ac.il/galleries/expeditious-methods-electronic-structure-theory-and-many-body-techniques/">Expeditious Methods in Electronic Structure Theory and Many Body...</a></li>
<li><a href="https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.7.013191">Spin coupling is all you need: Encoding strong electron correlation in...</a></li>

</ul>
</details>

**标签**: `#computational chemistry`, `#quantum computing`, `#classical simulation`, `#scientific breakthrough`, `#algorithm design`

---

<a id="item-10"></a>
## [Anthropic 估值超过 OpenAI，成为最高估值 AI 初创公司](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html) ⭐️ 8.0/10

Anthropic 完成了一轮 650 亿美元的新融资，投后估值达到 9650 亿美元，超过了 OpenAI 最新约 8520 亿美元的估值。 这一估值里程碑标志着主要人工智能公司竞争格局的重大转变，表明投资者对 Anthropic 的战略和技术比对其主要竞争对手更具信心。 Anthropic 是 Claude 系列人工智能模型的开发公司，这笔巨额新资本将主要用于算力、模型训练和商业化扩张。

telegram · zaihuapd · May 29, 03:29

**背景**: Anthropic 和 OpenAI 是大规模生成式人工智能模型开发领域的两家领先公司。如此极高的估值反映了大量资本流入人工智能行业，该行业严重依赖昂贵的计算基础设施和密集的研发来训练强大的基础模型。

**标签**: `#AI Industry`, `#Venture Capital`, `#Anthropic`, `#OpenAI`, `#Startup Valuation`

---