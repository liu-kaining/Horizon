---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> From 202 items, 14 important content pieces were selected

---

1. [据报道，ChatGPT 推翻了计算几何的核心难题](#item-1) ⭐️ 9.0/10
2. [单个漏洞（CVE-2026-6307）可同时突破 Chrome 渲染器和 V8 沙箱](#item-2) ⭐️ 9.0/10
3. [Linux 内核关键漏洞 CVE-2026-46215 允许非特权用户获取 root 权限。](#item-3) ⭐️ 9.0/10
4. [vLLM v0.24.0 发布，针对 MiniMax-M3 和 DeepSeek-V4 进行重大优化](#item-4) ⭐️ 8.0/10
5. [火箭实验室收购铱星公司，卫星行业迎来重大整合](#item-5) ⭐️ 8.0/10
6. [研究发现半数社交媒体儿童安全功能失效](#item-6) ⭐️ 8.0/10
7. [美国最高法院限制地理围栏搜查令，要求对手机位置数据适用合理依据标准](#item-7) ⭐️ 8.0/10
8. [人工智能时代的可观测性扩展，聚焦监测模型可靠性与幻觉](#item-8) ⭐️ 8.0/10
9. [AWS 发布 Graviton5 处理器，具备 192 核与经形式验证的虚拟机隔离功能](#item-9) ⭐️ 8.0/10
10. [微软推出 Memora：面向 AI 智能体的可扩展记忆系统](#item-10) ⭐️ 8.0/10
11. [Game Boy 即时编译器将指令翻译为 WebAssembly，性能超越本地解释器](#item-11) ⭐️ 8.0/10
12. [新 Linux 漏洞利用 IPv6 分片错误实现容器逃逸](#item-12) ⭐️ 8.0/10
13. [新研究发现野外存在含大量零的易受攻击 RSA 密钥](#item-13) ⭐️ 8.0/10
14. [特斯拉推送 FSD v14 Lite，HW3 车型获得 HW4 级智驾与自动泊车能力](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [据报道，ChatGPT 推翻了计算几何的核心难题](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 9.0/10

在 OpenAI 近期解决 Erdős 猜想的基础上，ChatGPT 据称推翻了计算几何领域一个长期存在的核心难题，该难题由姚班的传奇研究员陈立杰苦思了七年之久，这一发现获得了 30 多家机构的支持。 这标志着人工智能在自主数学发现能力上的重大范式转变，表明 AI 系统不仅能辅助，还能主动解决高等数学中长期悬而未决的开放性问题，可能加速整个领域的进步。 这一突破直接建立在 OpenAI 近期推翻 Erdős 单位距离猜想的工作基础上，该离散几何问题已悬而未决约 78 年，其解决需要 AI 生成一个在其训练数据中不存在的全新几何构造。

rss · 新智元 · Jun 29, 05:01

**背景**: Erdős 猜想是指由多产数学家保罗·Erdős 提出的大量未解决数学问题的集合。OpenAI 最近解决的那个具体问题涉及离散几何中的单位距离问题。计算几何是计算机科学的一个分支，致力于研究可以用几何术语描述的算法。陈立杰是著名的姚班（中国一个顶尖的计算机科学项目）的研究员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/openai-erdos-math-breakthrough-ai-reasoning">OpenAI Solved a 78-Year-Old Math Problem: What It Means for AI Reasoning | MindStudio</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_conjectures_by_Paul_Erdős">List of conjectures by Paul Erdős - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论似乎强调了超过 30 家机构的支持证明了该发现的可信度，并将其视为更广泛趋势的一部分，即像 ChatGPT 这样的 AI 正在发现安全漏洞和进行科学发现，而不仅仅是一个工具。

**标签**: `#AI breakthrough`, `#computational geometry`, `#mathematical discovery`, `#OpenAI`, `#ChatGPT`

---

<a id="item-2"></a>
## [单个漏洞（CVE-2026-6307）可同时突破 Chrome 渲染器和 V8 沙箱](https://nebusec.ai/research/v8-cve-2026-6307-writeup/) ⭐️ 9.0/10

安全研究人员证明，CVE-2026-6307——一个存在于 Chrome 浏览器 Turbofan 编译器中的类型混淆漏洞——可以仅利用这一个缺陷，同时突破渲染器进程沙箱和 V8 JavaScript 引擎的内部沙箱。 这一发现意义重大，因为它代表了一种强大的“二合一”利用方式，可以绕过 Chrome 的主要分层防御机制，攻击者可能仅通过一个简单的网页就获得完整的系统控制权，从而破坏现代浏览器的核心安全模型。 该漏洞编号为 CVE-2026-6307，是 Turbofan 中一个高危（CVSS 8.8）的类型混淆问题，已在 Chrome 147.0.7727.101 版本中修复；该研究强调，单个内存损坏缺陷就能连通两个原本被认为是隔离的安全边界。

rss · Lobsters · Jun 29, 15:00

**背景**: Chrome 采用多层沙箱架构：渲染器进程（负责处理网页内容）在一个受严格限制的操作系统沙箱中运行，而 V8 JavaScript 引擎则运行在其自身的内部沙箱中，以将内存损坏限制在其堆内存范围内。V8 沙箱的设计目的是防止 JavaScript 代码中的缺陷被升级为在系统上执行任意代码。Turbofan 优化编译器中的类型混淆漏洞会导致内存被错误地当作另一种类型来处理，从而引发内存损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://v8.dev/blog/sandbox">The V8 Sandbox · V8</a></li>
<li><a href="https://chromium.googlesource.com/chromium/src/+/HEAD/docs/design/sandbox.md">Chromium Docs - Sandbox</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-6307">NVD - CVE - 2026 - 6307</a></li>

</ul>
</details>

**社区讨论**: 这一发现在 Lobsters 上引发了社区的极大兴趣，由于其开创性，讨论很可能集中在漏洞利用的复杂性及其对浏览器安全设计的影响。

**标签**: `#security`, `#vulnerability`, `#browser`, `#v8`, `#chrome`

---

<a id="item-3"></a>
## [Linux 内核关键漏洞 CVE-2026-46215 允许非特权用户获取 root 权限。](https://cyberstan.co.uk/drm-lpe-linux/) ⭐️ 9.0/10

Linux 内核的 DRM GEM 子系统中`drm_gem_change_handle_ioctl()`函数被发现存在一个严重的释放后重用（UAF）漏洞（CVE-2026-46215），任何能够访问 GPU 渲染节点的本地用户都可以利用此漏洞将权限提升至 root。 该漏洞使受影响的 Linux 系统能够实现完整的本地权限提升，对服务器、工作站以及任何有不可信用户具有 shell 访问权限的设备构成严重风险，因为它能绕过所有标准安全控制并授予最高系统权限。 该漏洞存在的原因是`drm_gem_change_handle_ioctl()`函数在句柄之间移动 GEM 对象时，未能调整对象内部的`handle_count`引用计数，从而在后续访问或释放对象时导致释放后重用条件。

rss · Lobsters · Jun 29, 18:05

**背景**: DRM（直接渲染管理器）是用于管理 GPU 硬件和图形内存的 Linux 内核子系统。GEM（图形执行管理器）是 DRM 中用于处理图形缓冲区的内存管理器。释放后重用（UAF）漏洞发生在程序在内存被释放后仍继续使用指向该内存的指针时，这可能导致任意代码执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberstan.co.uk/drm-lpe-linux/">Unprivileged root via a use-after-free in DRM GEM change_handle (CVE-2026-46215) – cyberstan</a></li>
<li><a href="https://www.phoronix.com/news/Linux-7.1-DRM-Change-Handle">Linux DRM Ioctl Developed By AMD Being Disabled Following Ongoing Security Issue - Phoronix</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 讨论可能包含关于该漏洞根本原因、可利用性及补丁状态的实质性技术分析和辩论，表明社区对内核安全有显著关注。

**标签**: `#linux-kernel`, `#security`, `#vulnerability`, `#cve`, `#exploit`

---

<a id="item-4"></a>
## [vLLM v0.24.0 发布，针对 MiniMax-M3 和 DeepSeek-V4 进行重大优化](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 是一个重大版本更新，包含 571 次提交。该版本新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了大量优化，包括 FP8/ROCm 调优以及通过稀疏索引缓存等技术显著降低延迟。 此次发布显著提升了领先开源 LLM 推理引擎的性能和硬件兼容性，使得在 NVIDIA 和 AMD GPU 上部署大型模型更快速、更具成本效益。 关键优化包括为 MiniMax-M3 增加了 MXFP4 格式支持，以及为 DeepSeek-V4 提供了 FlashInfer 稀疏索引缓存，将首个 token 生成时间（TTFT）提升了 2-4%；此次发布还标志着在 ROCm 上内部使用 `CUDA_VISIBLE_DEVICES` 的废弃窗口期正式开始。

github · khluu · Jun 29, 19:41

**背景**: vLLM 是一个用于 LLM 推理和部署的高性能库，实现了高效的内存管理和调度。FP8（8 位浮点数）和 ROCm（AMD 的 GPU 计算平台）是用于在不同硬件上加速深度学习负载的技术。MiniMax-M3 和 DeepSeek-V4 是近期发布的大规模专家混合（MoE）模型，需要优化的推理内核。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitado.com.br/minimax-sparse-attention-msa-a-two-branch-block-sparse-attention-trained-on-a-109b-parameter-moe-with-a-3t-token-budget/">MiniMax Sparse Attention ( MSA ): a Two-Branch Block-Sparse...</a></li>
<li><a href="https://www.emergentmind.com/topics/mxfp4-data-format">MXFP4: Efficient 4-bit Data Format - Emergent Mind</a></li>
<li><a href="https://docs.flashinfer.ai/api/sparse.html">flashinfer . sparse - FlashInfer 0.6.13 documentation</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference-engine`, `#performance-optimization`, `#deep-learning`

---

<a id="item-5"></a>
## [火箭实验室收购铱星公司，卫星行业迎来重大整合](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

火箭实验室宣布了一项历史性的收购协议，将收购铱星公司，此举将为这家发射公司提供宝贵的频谱资产和有保障的发射量。 此次收购代表了卫星发射行业的重大整合，为火箭实验室提供了频谱等关键资产和定期发射的基本业务量，以对冲市场波动，这直接模仿了 SpaceX 及其星链星座之前采用的策略。 该交易使火箭实验室控制铱星公司宝贵的 L 波段频谱和轨道位置，并包括铱星盈利的卫星运营业务及其未来星座替换的订单。

hackernews · everfrustrated · Jun 29, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48719485)

**背景**: 铱星公司运营着一个由 66 颗活跃卫星组成的星座，提供全球语音和数据覆盖，最初于 1990 年代末发射。铱星 NEXT 现代化计划由 SpaceX 发射了其卫星。频谱是指用于卫星通信的关键授权无线电频率，拥有此类资产是卫星运营商价值的核心组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation - Wikipedia</a></li>
<li><a href="https://www.satellitetoday.com/technology/2019/10/15/satellite-operators-can-improve-return-on-assets-with-iot/">Satellite Operators Can Improve Return on Assets With IoT</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这是一项明智的战略举措，指出它为火箭实验室保障了发射量，类似于 SpaceX 利用星链的方式。讨论还引发了随着发射成本下降，太空碎片和光污染日益严重的担忧。一位评论者指出了其中的讽刺意味，即这次收购使起源于新西兰、曾是其骄傲的火箭实验室现在成了一家美国公司。

**标签**: `#space-industry`, `#acquisitions`, `#satellite-launch`, `#business-strategy`, `#consolidation`

---

<a id="item-6"></a>
## [研究发现半数社交媒体儿童安全功能失效](https://www.ithome.com/0/970/253.htm) ⭐️ 8.0/10

纽约大学和美国东北大学的一项新研究测试了 Instagram、Snapchat、TikTok 和 YouTube 上的 86 项儿童安全功能，发现每个平台至少一半的功能未能如宣传般有效，使儿童暴露于有害内容和不必要的联系中。 这项研究揭示了主要社交媒体平台所声称的保护措施存在重大缺陷，直接影响数百万儿童的网络安全，并对平台责任和监管效力提出了严重质疑。 研究使用模拟的儿童和成人账户测试了三种场景：未成年人的正常使用、青少年绕过安全功能，以及恶意成年人规避保护措施。具体失效案例包括 Snapchat 允许成人账户无限制地搜索和联系儿童账户，以及 TikTok 向青少年账户推荐与厌食症相关的内容。

rss · IT HOME · Jun 29, 23:46

**背景**: Instagram、Snapchat、TikTok 和 YouTube 等主要社交媒体平台公开推广了各种家长控制、内容过滤和联系人限制功能，旨在保护未成年用户。这些功能通常是其遵守美国《儿童在线隐私保护法》（COPPA）等儿童在线隐私和安全法规的关键部分。这些措施的有效性一直是全球家长、教育工作者和监管机构日益关注的问题。

**社区讨论**: 文章提到，Meta 等平台公司对研究结论提出异议，Meta 辩称其青少年账户能减少敏感内容和不受欢迎联系的曝光。研究作者则被批评在声称功能失效时含糊其辞，没有提供具体证据。

**标签**: `#online safety`, `#social media`, `#child protection`, `#research study`, `#platform accountability`

---

<a id="item-7"></a>
## [美国最高法院限制地理围栏搜查令，要求对手机位置数据适用合理依据标准](https://www.ithome.com/0/970/252.htm) ⭐️ 8.0/10

美国最高法院以 6 比 3 裁定，执法部门通过地理围栏搜查令获取个人详细手机位置历史，即便数据仅覆盖短时间段，也构成《第四修正案》意义上的搜查，需要合理依据和搜查令。 这项裁决极大地限制了无特定嫌疑人、大范围收集科技公司用户位置数据的做法，为数字监控实践设定了重要的宪法界限，并加强了对数百万用户的数字隐私保护。 法院明确指出，个人不能仅因出现在某一区域就被卷入调查，但如果警方已有合理依据锁定特定个人或已知嫌疑人，仍可合法调取位置数据。

rss · IT HOME · Jun 29, 23:39

**背景**: 地理围栏搜查令是一种法律工具，执法部门借此向谷歌或苹果等公司请求调取特定地理区域和时间段内所有设备的手机位置数据，以识别嫌疑人。这种做法依据《第四修正案》受到挑战，该修正案保护公民免受不合理的搜查和扣押，核心法律问题在于此类数据收集是否构成需要基于合理依据的“搜查”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/06/29/us/politics/supreme-court-geofence-warrant-cell-phones.html">Supreme Court Puts Limits on Cellphone Location Data Searches</a></li>
<li><a href="https://techcrunch.com/2026/06/29/in-major-privacy-win-supreme-court-rules-geofence-warrants-are-protected-by-privacy-rights/">In major privacy win, Supreme Court rules geofence... | TechCrunch</a></li>
<li><a href="https://versustexas.com/blog/carpenter-v-united-states/">Supreme Court: Warrant Required to Access Cell Site</a></li>

</ul>
</details>

**标签**: `#digital privacy`, `#Supreme Court`, `#legal ruling`, `#law enforcement`, `#Fourth Amendment`

---

<a id="item-8"></a>
## [人工智能时代的可观测性扩展，聚焦监测模型可靠性与幻觉](https://www.infoq.cn/article/HUri8txfhl93vIb9kHIJ?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

该文章主张，AI 系统的可观测性必须超越传统的基础设施稳定性指标，扩展为同时监测模型特定的问题，例如幻觉和可靠性。 这一转变至关重要，因为不可靠或产生幻觉的 AI 模型可能会输出错误或有害的结果，影响用户信任和安全，而传统的系统监测无法发现这些问题。 其重点是实时监测模型的性能和输出质量，这需要专为 AI 应用设计的新工具和指标，不同于传统软件使用的日志、跟踪和指标。

rss · InfoQ 中文站 · Jun 29, 18:06

**背景**: 传统的软件工程可观测性依赖于日志、跟踪和指标来了解系统健康状况。AI 系统，特别是使用大语言模型（LLMs）的系统，引入了新的复杂性层，因为它们的输出是概率性的，并可能产生“幻觉”——即生成看似合理但实际不正确的信息。这催生了 MLOps 和 AI 可观测性这一领域，旨在确保这些模型是可靠、透明和可问责的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dynatrace.com/knowledge-base/ai-observability/">What is AI observability?</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-observability">What is AI Observability? | IBM</a></li>
<li><a href="https://galileo.ai/blog/llm-performance-metrics">7 Key LLM Metrics to Enhance AI Reliability | Galileo</a></li>

</ul>
</details>

**标签**: `#AI observability`, `#LLM reliability`, `#MLOps`, `#model monitoring`

---

<a id="item-9"></a>
## [AWS 发布 Graviton5 处理器，具备 192 核与经形式验证的虚拟机隔离功能](https://www.infoq.cn/article/ONqpdtmlUXgF32G1vqT2?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

AWS 宣布推出 Graviton5 处理器，该处理器具备 192 个核心，并引入了经形式验证的虚拟机隔离功能以增强安全性。 此次发布为云基础设施树立了新标杆，它将高核心密度与数学上可证明的安全性相结合，将影响开发者在云中构建和保护高性能应用程序的方式。 经形式验证的隔离功能由 Nitro 隔离引擎驱动，它为虚拟机隔离提供了数学上的保证，超越了传统的安全方法。

rss · InfoQ 中文站 · Jun 29, 11:50

**背景**: AWS Graviton 处理器是亚马逊旗下 Annapurna Labs 设计的 ARM 架构 CPU 系列，以其能效和在云工作负载上出色的每瓦性能而闻名。形式验证是一种数学方法，用于根据规范证明系统设计的正确性，其提供的保证程度远高于传统测试。Nitro 平台为 AWS EC2 提供底层硬件和软件，将虚拟化功能卸载到专用硬件上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AWS_Graviton">AWS Graviton - Wikipedia</a></li>
<li><a href="https://oracore.dev/en/news/nitro-split-kernel-isolation-math-en">Nitro’s split kernel turns isolation into math | OraCore.dev</a></li>
<li><a href="https://www.nops.io/blog/aws-graviton-processors/">AWS Graviton : Basics, benefits, and processing | nOps</a></li>

</ul>
</details>

**标签**: `#cloud-computing`, `#AWS`, `#hardware`, `#security`, `#virtualization`

---

<a id="item-10"></a>
## [微软推出 Memora：面向 AI 智能体的可扩展记忆系统](https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity/) ⭐️ 8.0/10

微软研究院推出了 Memora，这是一种为 AI 智能体设计的新型记忆表示系统，它将存储与检索分离，以提高处理长而复杂任务时的效率。该系统旨在实现可扩展性，并解决了 AI 智能体需要不断重新加载或检索上下文这一根本性问题。 该记忆系统可以通过减少不断重新加载上下文带来的计算开销，显著提升执行长期、复杂任务的 AI 智能体的性能和效率。这是一项有意义的架构贡献，可能会影响未来智能体系统的设计，特别是在为更复杂的应用场景进行扩展时。 Memora 的核心创新在于将“存储内容”与“检索方式”分离，旨在使记忆管理更高效、更具可扩展性。尽管这个概念前景广阔，但微软研究院提供的博文中并未包含详细的实现细节或广泛的性能基准测试。

rss · Microsoft Research · Jun 29, 21:14

**背景**: AI 智能体，特别是基于大型语言模型的智能体，通常受到有限上下文窗口的限制，这意味着它们只能“记住”固定数量的最新信息。像检索增强生成（RAG）这样的系统通过从外部数据库检索相关文档来解决这个问题，但在处理非常长的任务时效率可能仍然不佳。智能体的记忆系统旨在维护关于过去交互和知识的结构化、持久性记录，以实现更连贯和有状态的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG? - Retrieval-Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://redis.io/blog/ai-agent-memory-stateful-systems/">AI agent memory: types, architecture & implementation</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#memory systems`, `#retrieval-augmented generation`, `#scalable architecture`, `#Microsoft Research`

---

<a id="item-11"></a>
## [Game Boy 即时编译器将指令翻译为 WebAssembly，性能超越本地解释器](https://humphri.es/blog/WATaBoy/) ⭐️ 8.0/10

一个名为 WATaBoy 的项目开发了一个即时编译器，该编译器在运行时将 Game Boy 的 CPU 指令翻译成 WebAssembly 字节码，实现了比传统本地解释器更快的执行速度。 这证明了 WebAssembly 可以作为模拟器的高性能编译目标，有望使复杂的模拟器无需依赖原生代码即可在网页浏览器中高效运行。 该即时编译器动态地将 Game Boy 的操作码转换为 WebAssembly 指令，利用了 WebAssembly 在沙箱环境中接近原生代码的执行速度。

rss · Lobsters · Jun 29, 15:07

**背景**: WebAssembly 是一种二进制指令格式，旨在作为编程语言的可移植编译目标，使其能够部署在 Web 和其他环境中。Game Boy 的 CPU 使用特定的指令集架构（ISA），模拟器通常通过软件解释这些指令。即时编译通过在运行时将代码翻译成原生机器码来提升性能，从而减少重复解释的开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wingolog.org/archives/2022/08/18/just-in-time-code-generation-within-webassembly">just-in-time code generation within webassembly — wingolog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Just-in-time_compilation">Just -in- time compilation - Wikipedia</a></li>
<li><a href="https://meganesulli.com/blog/game-boy-opcodes/">Meet the Game Boy Instruction Set | Megan Sullivan</a></li>

</ul>
</details>

**社区讨论**: 链接至 Lobsters 的评论显示出对这项技术成就的浓厚兴趣，讨论可能集中在使用即时编译进行基于 WebAssembly 的模拟的新颖性以及其实际的性能影响。

**标签**: `#WebAssembly`, `#JIT compilation`, `#emulation`, `#performance`, `#Game Boy`

---

<a id="item-12"></a>
## [新 Linux 漏洞利用 IPv6 分片错误实现容器逃逸](https://github.com/sgkdev/ipv6_frag_escape) ⭐️ 8.0/10

一个名为 ipv6_frag_escape 的概念验证漏洞利用代码已发布，它利用了 Linux 内核 IPv6 分片处理中的一个释放后重用漏洞，能够可靠地从监狱和容器环境中逃逸，实现本地权限提升。 此漏洞利用直接威胁到容器和监狱系统赖以存在的安全隔离基础，可能导致容器内被攻陷的应用程序获得对主机系统的完全控制权，这对云环境和多租户系统构成严重风险。 该漏洞编号为 CVE-2022-48956，是一个释放后重用问题，发生在调用 ip6_fragment 函数时未正确持有锁的情况下，并且已发布的利用程序被描述为能够可靠地逃逸多种容器运行时。

rss · Lobsters · Jun 29, 17:01

**背景**: 本地权限提升（LPE）指系统上权限有限的用户获得更高级别权限（如 root）的攻击方式。容器和监狱逃逸是一种严重的 LPE，攻击者从隔离环境中突破以访问底层主机操作系统。IPv6 分片重组是网络协议栈中的复杂部分，此前也曾发现过类似 SegmentSmack 的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vulert.com/vuln-db/debian-11-linux-173152">Use-After-Free Vulnerability in Linux Kernel's IPv6 Fragmentation - CVE-2022-48956</a></li>
<li><a href="https://www.kyberturvallisuuskeskus.fi/en/vulnerability-handling-ip-fragments">Vulnerability in the handling of IP fragments | NCSC-FI</a></li>
<li><a href="https://hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html">Linux Privilege Escalation - HackTricks</a></li>

</ul>
</details>

**社区讨论**: Lobste.rs 上的社区讨论可能集中在容器逃逸的严重性、缓解策略（如应用内核补丁或禁用 IPv6）以及对容器安全模型的影响等方面。

**标签**: `#security`, `#vulnerability`, `#linux`, `#container-escape`, `#exploit`

---

<a id="item-13"></a>
## [新研究发现野外存在含大量零的易受攻击 RSA 密钥](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html) ⭐️ 8.0/10

研究人员发现了一类新的弱 RSA 密钥，其特征是模数中包含大量零，并且开源项目 badkeys 已经在 TLS 和 SSH 等实际系统中发现了这些易受攻击的密钥。 这一发现带来了重大的安全风险，因为这些弱密钥更容易被分解，可能允许攻击者在广泛部署的加密系统中解密通信或冒充服务器。 该研究利用了 badkeys 项目，该项目扫描来自证书透明日志和全网扫描等公共来源的海量数据集，以识别模式异常稀疏的密钥，这表明了加密弱点。

rss · Schneier on Security · Jun 29, 16:05

**背景**: RSA 是一种基础的公钥密码系统，广泛用于安全数据传输。其安全性依赖于将大数分解为质因数的难度，而具有许多零等异常模式的密钥会产生数学捷径，使得这种分解比预期更容易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html">Factoring RSA Keys with Many Zeros - Schneier on Security</a></li>
<li><a href="https://www.scworld.com/brief/researchers-discover-new-class-of-weak-rsa-keys-in-the-wild">Researchers discover new class of weak RSA keys in the wild | brief | SC Media</a></li>
<li><a href="https://securityboulevard.com/2026/06/factoring-rsa-keys-with-many-zeros/">Factoring RSA Keys with Many Zeros - Security Boulevard</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#RSA`, `#security`, `#vulnerabilities`, `#key-management`

---

<a id="item-14"></a>
## [特斯拉推送 FSD v14 Lite，HW3 车型获得 HW4 级智驾与自动泊车能力](https://x.com/Tesla_AI/status/2071592820889260101) ⭐️ 8.0/10

特斯拉于 2026 年 6 月 29 日发布 FSD v14 Lite 软件更新，该更新将 HW4 车辆的先进神经网络提炼后运行在老旧的 HW3 硬件上，使 HW3 车型能够访问此前 HW4 独占的功能，例如强化学习和离线模型。 此次更新意义重大，因为它将先进的完全自动驾驶能力反向移植到大量老款车型上，延长了这些车辆的使用寿命和价值，并展示了特斯拉利用软件优化来克服硬件限制的策略。 针对 HW3 的提炼模型大小仅为原始 HW4 网络的约 15%，以适应 HW3 的内存限制；该更新在导航、并线和行人交互等场景中提升了性能，并首次引入了自动泊车等停车功能。

telegram · zaihuapd · Jun 30, 02:26

**背景**: 特斯拉的 Hardware 3 (HW3) 和 Hardware 4 (HW4) 指的是其 Autopilot 和完全自动驾驶(FSD)系统车载计算机的不同代次，HW4 拥有更强的处理能力和内存以运行更大的 AI 模型。完全自动驾驶(FSD)是特斯拉的高级驾驶辅助系统，旨在最终实现自动驾驶。空中下载(OTA)更新允许特斯拉远程向车辆部署新的软件功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notateslaapp.com/news/4369/tesla-launches-fsd-v14-lite-first-impressions">Tesla Launches FSD V 14 - Lite : First Impressions - Not a Tesla App</a></li>
<li><a href="https://electrek.co/2026/06/29/tesla-fsd-v14-lite-hw3-rollout/">Tesla starts FSD v 14 ' Lite ' rollout to HW 3 cars | Electrek</a></li>
<li><a href="https://arxiv.org/html/2512.18662v1">Offline Reinforcement Learning for End-to-End Autonomous Driving</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#autonomous driving`, `#FSD`, `#over-the-air updates`, `#AI`

---