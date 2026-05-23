---
layout: default
title: "Horizon Summary: 2026-05-23 (ZH)"
date: 2026-05-23
lang: zh
---

> From 199 items, 22 important content pieces were selected

---

1. [Megalodon：通过 CI 工作流大规模入侵 GitHub 代码仓库](#item-1) ⭐️ 9.0/10
2. [Secure Boot 证书颁发机构轮换要求 Linux 发行版紧急准备](#item-2) ⭐️ 9.0/10
3. [CISA 承包商在 GitHub 上泄露 AWS GovCloud 密钥](#item-3) ⭐️ 9.0/10
4. [Anthropic 启动 Project Glasswing 进行 AI 驱动的代码安全研究](#item-4) ⭐️ 8.0/10
5. [中国完成首次应急载人航天发射，替换受损飞船](#item-5) ⭐️ 8.0/10
6. [苹果开源 corecrypto 底层加密库，集成后量子安全算法](#item-6) ⭐️ 8.0/10
7. [我国完成 537 天万米深海腐蚀试验，刷新世界纪录](#item-7) ⭐️ 8.0/10
8. [英伟达 CEO 预测：AI 基建年度开支将达 4 万亿美元](#item-8) ⭐️ 8.0/10
9. [八部门联合整治非法跨境证券经营，已对老虎、富途、长桥立案调查](#item-9) ⭐️ 8.0/10
10. [企业“Token 焦虑”催生 AI 基础设施新战场](#item-10) ⭐️ 8.0/10
11. [谷歌发布 Gemini 3.5：速度提升 4 倍，每年节省超 10 亿美元](#item-11) ⭐️ 8.0/10
12. [TanStack 披露复杂 npm 供应链攻击，42 个软件包遭入侵](#item-12) ⭐️ 8.0/10
13. [Pip 26.1 发布，引入依赖冷却和锁文件机制以抵御供应链攻击](#item-13) ⭐️ 8.0/10
14. [苹果发布对其核心密码库 corecrypto 进行形式化验证的蓝图](#item-14) ⭐️ 8.0/10
15. [Galois 宣布为 SAW 添加 Isabelle 定理证明器支持](#item-15) ⭐️ 8.0/10
16. [Linux PDF 查看器发现存在十年之久的远程代码执行漏洞](#item-16) ⭐️ 8.0/10
17. [《Qud 洞穴》中村庄的端到端程序化生成：2019 年 GDC 技术演讲](#item-17) ⭐️ 8.0/10
18. [美国联邦贸易委员会与考克斯媒体集团就欺骗性 AI“主动聆听”广告达成和解](#item-18) ⭐️ 8.0/10
19. [Linux 探索使用 BPF 实现自定义页面缓存淘汰策略](#item-19) ⭐️ 8.0/10
20. [谷歌 Project Zero 发现 Pixel 10 手机零点击内核级漏洞](#item-20) ⭐️ 8.0/10
21. [字节跳动开源 3B 统一多模态模型 Lance](#item-21) ⭐️ 8.0/10
22. [Cloudflare 故障：25 分钟全球中断影响 28%的 HTTP 流量](#item-22) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Megalodon：通过 CI 工作流大规模入侵 GitHub 代码仓库](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows) ⭐️ 9.0/10

2026 年 5 月 18 日，一个代号为“Megalodon”的自动化攻击活动在六小时内向超过 5500 个 GitHub 代码仓库推送了 5700 多个恶意提交，将其中的 GitHub Actions 工作流替换为旨在窃取机密信息的 Base64 编码负载。 这代表了一种高度可扩展且激进的供应链攻击向量，通过污染 CI/CD 流水线破坏软件完整性，可能影响大量开源项目及其下游用户。 攻击者使用伪造身份（如“build-bot”和“ci-bot”）的临时账户推送了恶意的 GitHub Actions 工作流，其中包含用于将 CI 机密、云凭据、SSH 密钥和 OIDC 令牌窃取到命令与控制服务器（216.126.225.129:8443）的 bash 负载。

rss · Lobsters · May 22, 09:05

**背景**: GitHub Actions 是集成在 GitHub 中的 CI/CD 平台，用于自动化软件的构建、测试和部署工作流。供应链攻击针对软件开发和分发过程，旨在通过入侵受信任的工具或依赖项来最终感染终端用户。利用 CI 工作流是一个已知但威胁巨大的攻击向量，因为工作流通常拥有提升的权限来访问敏感机密信息和部署代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/megalodon-malware-github-repos/">Megalodon Malware Compromised 5,500+ GitHub Repos Within 6 Hours</a></li>
<li><a href="https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/">How to catch GitHub Actions workflow injections before attackers do</a></li>

</ul>
</details>

**社区讨论**: Lobsters 上的社区讨论（原文中有链接）可能聚焦于其对开源安全的严重影响以及保护自动化工作流的实际挑战，并可能就代码仓库维护者和平台提供商的责任进行辩论。

**标签**: `#supply-chain-security`, `#CI/CD`, `#github-actions`, `#cybersecurity`, `#open-source-security`

---

<a id="item-2"></a>
## [Secure Boot 证书颁发机构轮换要求 Linux 发行版紧急准备](https://blog.einval.com/2026/05/22#secure_boot_ca_rollover) ⭐️ 9.0/10

一篇博文向 Linux 发行版发出了关键提醒：2011 年版的 Microsoft Secure Boot 证书颁发机构（CA）将于 2026 年 6 月开始过期，需要协调准备以避免启动失败。 此次轮换至关重要，因为如果 Linux 发行版不协调更新，依赖 Secure Boot 的系统可能无法启动，或者丧失对 bootkit 级别攻击的防护，从而影响大量用户和服务器。 即将过期的证书是'Microsoft Corporation UEFI CA 2011'及相关密钥，时间线始于 2026 年 6 月并延续至 2026 年 10 月，该过程涉及将其替换为更新的 2023 系列证书。

rss · Lobsters · May 22, 09:48

**背景**: UEFI Secure Boot 是一项安全标准，确保设备仅使用原始设备制造商（OEM）信任的软件启动。它通过一个密钥层次结构运作，该结构包括平台密钥（PK）、密钥交换密钥（KEK）和签名数据库（db/dbx）。Microsoft 的第三方 CA 被 Linux 发行版使用，通常通过一个'shim'引导加载程序来签名其引导加载程序，从而使其在默认的 Secure Boot 固件配置中被信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://windowsforum.com/threads/secure-boot-certificate-rollover-what-to-check-before-june-2026.416378/">Secure Boot Certificate Rollover: What to Check Before June ...</a></li>
<li><a href="https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e">Windows Secure Boot certificate expiration and CA updates - Microsoft Support</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/windows-itpro-blog/updating-microsoft-secure-boot-keys/4055324">Updating Microsoft Secure Boot keys | Windows IT Pro blog</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 评论页面可能包含大量社区讨论，反映了该问题的技术严重性以及开源生态系统中协调行动的必要性。

**标签**: `#Secure Boot`, `#Linux distributions`, `#cryptography`, `#system security`, `#certificate management`

---

<a id="item-3"></a>
## [CISA 承包商在 GitHub 上泄露 AWS GovCloud 密钥](https://www.schneier.com/blog/archives/2026/05/cisa-security-leak.html) ⭐️ 9.0/10

直到上周末，美国网络安全和基础设施安全局（CISA）的一名承包商在一个公开的 GitHub 仓库中意外泄露了具有高度特权的 AWS GovCloud 密钥以及内部系统详情。 这是近年来最严重的政府数据泄露事件之一，因为泄露的凭证可能让人得以访问美国政府的关键云基础设施，这引发了国会的质询，并引起了严重的国家安全担忧。 泄露的仓库中包含了详细说明 CISA 内部如何构建、测试和部署软件的文件，而该机构仍在努力控制此次入侵并作废已被泄露的凭证。

rss · Schneier on Security · May 22, 13:58

**背景**: CISA 是美国网络安全和基础设施安全局，一个负责保护国家关键基础设施免受网络威胁的联邦机构。AWS GovCloud（美国）是亚马逊网络服务提供的一个专门的、隔离的云区域，旨在托管敏感的政府工作负载，并遵守严格的美国合规要求，如 ITAR 和 FedRAMP。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>

</ul>
</details>

**社区讨论**: 这则由安全专家布鲁斯·施奈尔讨论、并由 KrebsOnSecurity 等媒体报道的新闻，在网络安全界引起了广泛的震惊和担忧，突显了政府承包商在安全协议方面存在严重疏漏。

**标签**: `#cybersecurity`, `#government`, `#data-leak`, `#AWS`, `#CISA`

---

<a id="item-4"></a>
## [Anthropic 启动 Project Glasswing 进行 AI 驱动的代码安全研究](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 8.0/10

Anthropic 宣布启动 Project Glasswing 人工智能安全研究项目，称其系统在独立验证后，以 90.6%的真实阳性率发现了超过 1752 个高危漏洞。 该计划可能通过主动发现并修复关键漏洞，显著提升软件安全性，以应对人工智能时代传统方法难以处理复杂代码库的重大挑战。 所声称的 90.6%真实阳性率基于独立安全公司的评估，但该数字显著高于其他人工智能漏洞检测工具的基准，后者通常低于 40%。

hackernews · louiereederson · May 22, 19:31 · [社区讨论](https://news.ycombinator.com/item?id=48240419)

**背景**: 大语言模型（LLM）正成为软件漏洞检测的新工具，相较于可能产生高误报率的传统静态和动态分析方法具有优势。静态应用程序安全测试（SAST）工具已被用于发现缺陷，但 LLM 旨在检测更细微、更依赖上下文的漏洞。CVE 计划是用于唯一识别和编录此类软件漏洞的标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html">Anthropic's Claude Mythos Finds Thousands of Zero-Day Flaws ...</a></li>
<li><a href="https://fuzzinglabs.com/benchmarking-ai-agents-vulnerability-research/">Benchmarking LLM agents for vulnerability research</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户报告了类似工具（如 Codex Security）的高准确结果，这与 Anthropic 的说法一致；而其他人则表示怀疑，引用了 curl 等项目的反馈，质疑相对于现有工具的改进程度。一个关键争论在于，当许多组织尚未实施基本的静态分析和代码检查工具时，应用昂贵的 LLM 工具是否合理。

**标签**: `#AI-security`, `#vulnerability-detection`, `#code-analysis`, `#research`

---

<a id="item-5"></a>
## [中国完成首次应急载人航天发射，替换受损飞船](https://www.ithome.com/0/954/253.htm) ⭐️ 8.0/10

2025 年 11 月，中国成功实施了首次应急载人航天发射，神舟二十二号飞船在神舟二十号返回舱舷窗遭空间碎片撞击受损后被送往空间站。从发现问题到新飞船对接，整个应急处置流程在 20 天内完成。 此次事件为中国“打一备一”的应急备份策略提供了成功的实战验证，为国际航天界高效处理在轨突发事件、保障航天员安全提供了宝贵范例。 危机起因是神舟二十号航天员发现返回舱舷窗因疑似微流星体或空间碎片撞击出现裂纹；经分析评估，任务指挥部认为原船返回风险过大，决定航天员换乘备份的神舟二十一号安全返回，同时利用待命的长征二号 F 遥二十二火箭发射神舟二十二号。基于此经验，即将发射的神舟二十三号飞船舷窗已进行了防空间碎片能力的适应性改进。

rss · IT HOME · May 23, 01:30

**背景**: 中国载人航天工程自空间站时代开启以来，一直遵循“打一备一”策略，即始终有一艘载人飞船和一枚运载火箭在发射场待命，可迅速转入发射状态。空间碎片以极高速度运行，即使毫米级的碎片也能对航天器舷窗和太阳翼等关键部件造成损伤，构成严重威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.cctv.com/2026/05/23/ARTI6kbH95B6sY8GZiHipQ5Z260523.shtml">去年中国载人航天工程实施首次应急发射任务 为国际航天领域高效应对突...</a></li>
<li><a href="https://www.news.cn/tech/20251127/26d2f836ea564c178330e8f01e27c4a4/c.html">解密载人航天首次应急发射任务 - 新华网</a></li>
<li><a href="https://baike.baidu.com/item/打一备一、滚动备份模式/67166787">打一备一、滚动备份模式 - 百度百科</a></li>

</ul>
</details>

**标签**: `#Space Exploration`, `#Crewed Spaceflight`, `#Emergency Response`, `#Space Station`, `#China`

---

<a id="item-6"></a>
## [苹果开源 corecrypto 底层加密库，集成后量子安全算法](https://www.ithome.com/0/954/226.htm) ⭐️ 8.0/10

苹果在 GitHub 上发布了其核心加密库 corecrypto 的源代码，该库集成了后量子算法 ML-KEM 和 ML-DSA，并附带了形式化验证工具和相关文档。 此次发布是在 iPhone 和 Mac 等消费设备上大规模部署后量子密码学的重要一步，为抵御未来量子计算威胁提供了一个透明且经过验证的安全基础。 corecrypto 库是苹果 Security 框架和 CryptoKit 的底层加密引擎，此次发布的代码包含源码、测试工具、性能基准以及专门的形式化验证目录，以验证其符合 FIPS 203 和 FIPS 204 标准。

rss · IT HOME · May 22, 23:01

**背景**: 后量子密码学（PQC）是指能够抵御经典计算机和未来量子计算机攻击的密码算法，量子计算机可能会破解当前广泛使用的 RSA 和 ECC 等方案。2024 年，美国国家标准与技术研究院（NIST）将 ML-KEM（FIPS 203，用于密钥封装）和 ML-DSA（FIPS 204，用于数字签名）标准化为首要的后量子算法。此前，苹果已在 iOS 17.4 系统中通过 PQ3 协议将后量子保护集成到 iMessage。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM - Wikipedia</a></li>
<li><a href="https://www.digicert.com/insights/post-quantum-cryptography/mldsa">ML-DSA | Post-Quantum Cryptography | DigiCert Insights</a></li>
<li><a href="https://csrc.nist.gov/pubs/fips/203/final">Federal Information Processing Standard (FIPS) 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#cryptography`, `#open-source`, `#security`, `#Apple`

---

<a id="item-7"></a>
## [我国完成 537 天万米深海腐蚀试验，刷新世界纪录](https://www.ithome.com/0/954/225.htm) ⭐️ 8.0/10

中国完成了全球首次在海洋 11000 米深度进行的、为期 537 天的材料腐蚀试验，刷新了此类深海原位实验持续时长的全球纪录。 这一里程碑展示了深海测试能力的关键突破，能够在极端高压和腐蚀环境下对材料性能进行长期验证，这对于未来深海探测装备和基础设施的发展至关重要。 该试验由中国船舶集团七二五研究所主导，系统验证了 30 种特种防护涂层、4 类新型牺牲阳极以及 22 种结构金属材料在万米深渊的环境适应性。

rss · IT HOME · May 22, 22:45

**背景**: 深海原位试验是指在深海自然环境中直接开展科学试验，以保持原位物理化学条件，从而获取材料性能的最真实数据。牺牲阴极是保护水下金属结构的关键防腐方法，其原理是通过更活泼的金属优先腐蚀来保护主体结构。进行如此长时间的测试，对于理解材料在深海极端高压和腐蚀环境下的真实使用寿命至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Galvanic_anode">Galvanic anode - Wikipedia</a></li>
<li><a href="https://www.mdpi.com/2075-163X/13/2/184">Design and Application of a Deep-Sea Engineering Geology In Situ Test System</a></li>

</ul>
</details>

**标签**: `#deep-sea research`, `#materials science`, `#corrosion testing`, `#ocean engineering`, `#scientific records`

---

<a id="item-8"></a>
## [英伟达 CEO 预测：AI 基建年度开支将达 4 万亿美元](https://www.ithome.com/0/954/223.htm) ⭐️ 8.0/10

英伟达公布 2027 财年第一季度创纪录营收 816 亿美元，数据中心业务同比暴增 92%；同时 CEO 黄仁勋预测，超大规模云厂商的 AI 资本开支将在 2030 年前增长至每年 3 至 4 万亿美元，是当前华尔街共识的四倍。 这一预测预示着 AI 基础设施将迎来大规模、长期的投资周期，将推动芯片、云服务和能源需求，深刻影响科技行业、金融市场乃至消费者的电费支出。 预测的 2030 年前年度 3 至 4 万亿美元支出，与华尔街共识认为超大规模厂商资本开支要到 2028 年才能达到 1.03 万亿美元形成鲜明对比；此外，英伟达自身正在执行 800 亿美元的股票回购计划。

rss · IT HOME · May 22, 22:30

**背景**: 超大规模云厂商如亚马逊、谷歌、微软和 Meta 是运营全球大型数据中心网络的大型云服务提供商。其资本开支，主要受 GPU 和服务器等 AI 基础设施驱动，一直在快速增长，2026 年的预测支出约为 7000 亿美元。英伟达的数据中心业务销售构成 AI 基础设施骨干的高性能 GPU，一直呈爆发式增长，并持续超出预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techblog.comsoc.org/2025/12/22/hyperscaler-capex-600-bn-in-2026-a-36-increase-over-2025-while-global-spending-on-cloud-infrastructure-services-skyrockets/">Hyperscaler capex > $600 bn in 2026 a 36% increase over 2025...</a></li>
<li><a href="https://247wallst.com/investing/2026/05/01/hyperscalers-hit-700-billion-in-2026-ai-spending-plans/">Hyperscalers Hit $700 Billion in 2026 AI Spending Plans</a></li>
<li><a href="https://qz.com/can-nvidia-s-data-center-business-sustain-its-high-growth-momentum?trk=article-ssr-frontend-pulse_little-text-block">Can NVIDIA 's Data Center Business Sustain Its High Growth ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#NVIDIA`, `#cloud computing`, `#capital expenditure`, `#tech earnings`

---

<a id="item-9"></a>
## [八部门联合整治非法跨境证券经营，已对老虎、富途、长桥立案调查](https://mp.weixin.qq.com/s?__biz=MzA4NzAzMDgwMw==&amp;mid=2651090403&amp;idx=3&amp;sn=bca72a940ac72bef356f29b5b9576ac1&amp;chksm=8a1670281e2bc67d2df3608a313ba9fdaf0fcd2f43ce44475c6bf273b386af2e4f9d8e8e2e2b&amp;scene=0&amp;xtrack=1) ⭐️ 8.0/10

中国证监会等八部门联合印发整治方案，对非法跨境证券期货基金经营行为开展为期两年的集中整治，期间只允许存量投资者单向卖出并转出资金。证监会已对老虎证券、富途控股和长桥证券境内外相关主体正式立案调查，并作出行政处罚事先告知。 此次监管行动对服务于寻求海外投资渠道的中国内地投资者的金融科技平台产生了重大影响，实质上迫使其核心业务活动停止，并强化了严格的资本管制。这凸显了政府堵塞监管漏洞、将跨境投资引导至港股通和 QDII 等官方批准渠道的决心。 整治对象不仅包括非法跨境展业的境外机构，还包括其境内关联方、中介方，以及提供开户通道和营销引流的信息平台与自媒体。方案明确，两年整治期结束后，相关的境内网站、交易软件和配套服务器将被全面关停，证监会拟没收被调查主体的全部违法所得。

telegram · 新智元 · May 22, 08:26

**背景**: 在中国，跨境证券投资受到严格监管，以控制资本外流和管理金融风险。合法的投资渠道包括沪港通和深港通等股票互联互通机制、QDII（合格境内机构投资者）计划以及粤港澳大湾区跨境理财通。老虎证券、富途等平台吸引了大量内地客户进行海外交易，但其在未获得必要内地牌照的情况下运营，一直处于监管灰色地带。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/港股通/13611865">港股通（内地与香港股票市场交易互联互通机制）_百度百科 一文搞懂港股通开通条件及交易规则 - 知乎 港股通交易规则全解：从时间、机制到费用，一文看懂实操要点 港股通是什么?开通条件与流程全解析 (2025 最新版)|内地股市|融资融券... 港股上市公司加入港股通的条件及最近一次的调整记录（20250310） 基本... 一文讲清楚港股通：开通条件、佣金、交易规则（附港股通测评答案）_股...</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/合格境内机构投资者">合格境内机构投资者 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.swhyhk.com/tc/cross-boundary/">申萬宏源（香港）有限公司 - 粵港澳大灣區 跨 境 理 財 通</a></li>

</ul>
</details>

**标签**: `#financial regulation`, `#fintech`, `#cross-border investment`, `#securities law`, `#Chinese market`

---

<a id="item-10"></a>
## [企业“Token 焦虑”催生 AI 基础设施新战场](https://www.infoq.cn/article/TLRAmZy8pPICVFVWmu6p?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

企业正面临“Token 焦虑”——即难以将采购的 GPU 等 AI 硬件高效转化为生产力的困境，这推动了 AI 基础设施市场的激烈竞争与创新。 这一转变表明，企业 AI 应用的真正瓶颈正从硬件采购转向软件和基础设施的优化，直接影响企业 AI 投资的回报率。 挑战不仅在于 GPU 利用率低下，还涉及软件编排的集成、AI 副本优化等扩缩容系统，以及在云环境中管理成本以匹配实际工作负载需求。

rss · InfoQ 中文站 · May 22, 20:34

**背景**: “Token 焦虑”指的是开发者和企业为最大化利用 AI 令牌（如大语言模型的计算单位）以证明基础设施成本合理性而产生的压力，该概念近期由 Andrej Karpathy 等人普及。AI 基础设施是指高效运行、扩展和管理 AI 工作负载所需的软件、中间件和云系统，远不止于拥有硬件本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alex-ber.medium.com/the-rise-of-token-anxiety-why-ai-is-making-developers-miserable-462ff6d50cc1">The Rise of “Token Anxiety”: Why AI is Making Developers ...</a></li>
<li><a href="https://scaleops.com/product/ai-infra/">AI Infra - ScaleOps</a></li>
<li><a href="https://medium.com/@mcschnei/right-sizing-gpu-compute-infrastructure-for-ai-workloads-a-practical-guide-997caf455601">Right-Sizing GPU & Compute Infrastructure for AI Workloads ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#GPU optimization`, `#enterprise AI`, `#system architecture`, `#resource management`

---

<a id="item-11"></a>
## [谷歌发布 Gemini 3.5：速度提升 4 倍，每年节省超 10 亿美元](https://www.infoq.cn/article/COda3jCSAliReaA4YVJc?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

谷歌宣布推出其最新 AI 模型系列 Gemini 3.5，首发了 3.5 Flash 版本，该公司声称这代表了性能和运营效率的重大飞跃。 此次发布标志着谷歌内部一次重大的技术转向，其所声称的 4 倍速度提升和每年超过 10 亿美元的成本节省，可能极大地巩固其在 AI 行业的竞争地位。 据报道，Gemini 3.5 Flash 在现实世界的企业任务中，性能比其前代产品提升了 19.6%，但其运营成本被指出比某些同类模型（如 DeepSeek V4 Flash）高出约 60%。

rss · InfoQ 中文站 · May 22, 18:13

**背景**: Gemini 是谷歌的多模态 AI 模型系列，旨在处理文本、图像、音频和视频。“Flash”变体通常指为速度和成本效益优化的模型，适合高并发的实时应用。谷歌的这些进步得益于其定制的张量处理单元（TPU）硬件，它为训练和服务这些大型模型提供了计算基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3 . 5 : frontier intelligence with action</a></li>
<li><a href="https://blog.kilo.ai/p/the-age-of-the-flash-model-gemini">The Age of the Flash Model: Gemini 3 . 5 , StepFun, DeepSeek and the...</a></li>
<li><a href="https://docs.cloud.google.com/tpu/docs/v5p">TPU v5p | Google Cloud Documentation</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Google`, `#Performance Optimization`, `#Large Language Models`, `#Tech Industry News`

---

<a id="item-12"></a>
## [TanStack 披露复杂 npm 供应链攻击，42 个软件包遭入侵](https://www.infoq.cn/article/ePxUGQ7cZvWNWkOhE1vT?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

TanStack 公开披露了一起复杂的供应链攻击事件，导致其 42 个 npm 软件包被入侵，攻击手段包括劫持 GitHub Actions 工作流。 此事件凸显了开源生态系统中的关键安全风险，因为它影响了一个广泛使用的 Web 开发库，并暴露了软件包管理和贡献工作流的脆弱性。 此次攻击可能与更广泛的“Mini Shai-Hulud”活动有关，涉及利用缓存投毒和有效 SLSA Build Level 来源的自传播恶意软件来发布恶意版本。作为回应，TanStack 团队正在考虑将拉取请求改为仅限邀请制，这是对标准开放贡献模式的重大改变。

rss · InfoQ 中文站 · May 22, 16:00

**背景**: npm 供应链攻击是指恶意代码被注入到广泛使用的 JavaScript 软件包中，开发者和应用程序会自动下载这些软件包，可能导致数据被盗或系统被入侵。TanStack 是一个流行的开源项目，提供用于 Web 开发的无头、类型安全的 UI 库和工具。由威胁组织 TeamPCP 命名的更广泛的“Mini Shai-Hulud”活动是一种复杂的蠕虫病毒，它通过劫持合法的 GitHub Actions 工作流，已经入侵了数百个 npm 软件包。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/security/2026/05/18/tanstack-weighs-invitation-only-pull-requests-after-supply-chain-attack/5241899">TanStack weighs invitation-only pull requests after supply ...</a></li>
<li><a href="https://thecybersecguru.com/news/mini-shai-hulud-npm-worm-affected-packages-list/">Mini Shai-Hulud npm Attack: All Affected Packages | The ...</a></li>
<li><a href="https://www.kunalganglani.com/blog/npm-supply-chain-attack-defense">NPM Supply Chain Attacks : 5 Defenses Every JS Dev Needs [2026]</a></li>

</ul>
</details>

**社区讨论**: 提供的源材料中没有社区评论可供总结。

**标签**: `#supply-chain-attack`, `#npm`, `#open-source-security`, `#software-security`, `#dependency-management`

---

<a id="item-13"></a>
## [Pip 26.1 发布，引入依赖冷却和锁文件机制以抵御供应链攻击](https://www.infoq.cn/article/tO2s7Qc7DtKWpXMpMbC1?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Pip 26.1 正式引入了“依赖冷却”机制，在安装新发布的包之前强制实施等待期，并增加了基于 PEP 751 (pylock.toml) 的实验性锁文件支持。 这些功能通过提供检测恶意包的时间缓冲并确保确定性、可复现的安装，直接解决了 Python 包生态系统中的关键漏洞，是缓解供应链攻击的重要一步。 依赖冷却通过 `--uploaded-prior-to` 选项实现，允许用户指定包发布的截止日期。锁文件功能是实验性的，仅保证在当前 Python 版本和平台上的有效性。

rss · InfoQ 中文站 · May 22, 10:40

**背景**: 供应链攻击涉及入侵开源包以将恶意软件传播给下游用户，这是一个日益严重的威胁，近期数百个 npm 和 PyPI 包被入侵的事件凸显了这一点。依赖冷却是一种防御策略，包管理器拒绝安装某个包，直到其发布后经过了一定时间，这为社区提供了识别和报告恶意版本的窗口。锁文件（如 pylock.toml）记录了环境中使用的所有依赖项的确切版本，以防止意外更改并确保构建的一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sethmlarson.dev/pip-relative-dependency-cooling-with-crontab">Relative “ Dependency Cooling ” in pip v26.0 with crontab</a></li>
<li><a href="https://pip.pypa.io/en/stable/cli/pip_lock/">pip lock - pip documentation v26.1.1</a></li>
<li><a href="https://www.infoq.com/news/2026/05/pip-261-dependency-cooldowns/">Pip 26.1 Ships Dependency Cooldowns and Experimental Lockfile ...</a></li>

</ul>
</details>

**社区讨论**: 这些功能的引入可能会受到安全意识强的开发者和组织的欢迎，尽管锁文件的实验性可能导致谨慎采用。讨论可能集中在不同工作流中冷却期的实际实施，以及与现有锁文件解决方案（如 Pipfile.lock）的比较。

**标签**: `#Python`, `#Package Management`, `#Security`, `#Supply Chain`, `#Tools`

---

<a id="item-14"></a>
## [苹果发布对其核心密码库 corecrypto 进行形式化验证的蓝图](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 8.0/10

苹果发布了一份详细蓝图，阐述了如何对其 corecrypto 密码库应用形式化验证技术，其中包括了具备量子安全性的 ML-KEM 和 ML-DSA 算法实现及其数学证明，以及他们为此创建的自定义验证库和工具。 此举意义重大，因为它展示了一家主要科技公司公开投入资源，以数学方式证明一个基础安全组件的正确性，这可以提升行业软件保障标准，并激励形式化验证在安全关键软件中得到更广泛的应用。 发布的证明具体针对量子安全 ML-KEM（FIPS 203）和 ML-DSA（FIPS 204）算法的实现，配套的博文还提供了苹果为该项目内部开发的形式化验证库和工具的访问权限。

rss · Lobsters · May 22, 19:40

**背景**: 形式化验证是一套运用数理逻辑来证明系统设计或实现完全符合其规范的技术，它超越了传统测试，能穷尽所有可能的输入。苹果的 corecrypto 是为其 iOS 和 macOS 等操作系统提供基础安全原语的底层密码库。近期以后量子密码学标准（如 FIPS 203 和 204）为代表的发展趋势，因其算法的关键性和新颖性，正推动着对更强验证手段的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.apple.com/blog/formal-verification-corecrypto/">A blueprint for formal verification of Apple corecrypto</a></li>
<li><a href="https://9to5mac.com/2026/05/22/apple-shares-iphone-and-mac-post-quantum-cryptography-code-on-github/">Apple shares iPhone and Mac post-quantum ... - 9to5Mac</a></li>
<li><a href="https://www.nist.gov/document/formal-verification-cryptographic-software-aws-current-practices-and-future-trends">Formal Veriﬁcation of Cryptographic Software at AWS - Current ...</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 评论区很可能包含了来自安全和形式化方法社区的实质性技术讨论，内容可能聚焦于苹果方法的实际意义、验证的深度，以及与 AWS 等其他公司类似工作的比较。

**标签**: `#formal-verification`, `#cryptography`, `#apple`, `#security`, `#software-correctness`

---

<a id="item-15"></a>
## [Galois 宣布为 SAW 添加 Isabelle 定理证明器支持](https://www.galois.com/articles/announcing-isabelle-support-for-saw) ⭐️ 8.0/10

Galois 宣布其软件分析工作台（SAW）新增了对 Isabelle 定理证明器的集成支持，使用户能够更无缝地结合使用这两款形式化验证工具。 此次集成对形式化方法社区意义重大，因为它连接了两大主要工具，有望简化验证流程，让软件开发者和安全分析师能更容易地处理复杂的形式化证明。 此次集成特别将 SAW 与 Isabelle 连接起来。SAW 通过将程序翻译为逻辑表达式供外部求解器使用来自动化验证，而 Isabelle 则是一款以其可信的小内核架构闻名的高阶逻辑定理证明器。

rss · Lobsters · May 22, 21:59

**背景**: 软件分析工作台（SAW）是 Galois 公司开发的一款工具，用于通过将程序转换为逻辑形式并利用自动推理来形式化验证程序属性。Isabelle 是一款基于高阶逻辑（HOL）的强大通用交互式定理证明器，广泛应用于学术和工业研究中以验证复杂系统。集成此类工具是形式化方法领域的共同目标，旨在结合不同验证方法的优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tools.galois.com/saw">SAW : The Software Analysis Workbench | SAW | Galois Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_theorem_prover">Isabelle theorem prover</a></li>

</ul>
</details>

**社区讨论**: 内容中链接的 Lobsters 讨论表明，社区对这次集成很感兴趣，这显示了它对使用形式化验证工具的实践者具有实际价值。

**标签**: `#formal-verification`, `#theorem-proving`, `#software-analysis`, `#Isabelle`, `#SAW`

---

<a id="item-16"></a>
## [Linux PDF 查看器发现存在十年之久的远程代码执行漏洞](https://medeiros.zip/posts/CVE-2026-46529-evince) ⭐️ 8.0/10

在流行的 Linux PDF 查看器 XReader、Evince 和 Atril 中发现了一个严重的远程代码执行漏洞，编号为 CVE-2026-46529，该漏洞存在约十年之久且未被发现。 该漏洞影响重大，因为它波及众多 Linux 发行版上广泛使用的文档查看器，攻击者可能仅通过打开一个恶意 PDF 文件就能在用户系统上执行任意代码。 该漏洞是一个命令注入缺陷，与处理特定的 GTK 标志有关，该标志已在 GTK 4 中移除，这使得像 'Papers' 这样的新软件受到的影响比 Evince、Atril 和 XReader 要小。利用此漏洞需要攻击者预测恶意 PDF 文件将被保存的绝对路径。

rss · Lobsters · May 22, 22:14

**背景**: PDF 查看器是 Linux 系统上用于渲染便携式文档格式文件的常见软件。远程代码执行 (RCE) 是一类安全漏洞，允许攻击者在远程位置于目标机器上执行任意代码。CVE，即通用漏洞披露，是一个用于识别和编目已知公开网络安全漏洞的标准化系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seclists.org/oss-sec/2026/q2/643">oss-sec: Re: Evince / Atril / Xreader command injection CVE-2026-46529</a></li>
<li><a href="https://advisory.eventussecurity.com/advisory/critical-vulnerability-in-pdf-js-allows-remote-code-execution/">Critical Vulnerability in PDF.js Allows Remote Code Execution</a></li>

</ul>
</details>

**社区讨论**: Lobsters 社区讨论很可能深入探讨了该命令注入的技术细节、漏洞长期存在的影响，以及不同 PDF 查看器实现（特别是比较使用 GTK 3 与 GTK 4 的实现）的相对安全性。

**标签**: `#security`, `#CVE`, `#Linux`, `#software-vulnerability`, `#open-source`

---

<a id="item-17"></a>
## [《Qud 洞穴》中村庄的端到端程序化生成：2019 年 GDC 技术演讲](https://www.youtube.com/watch?v=jV-DZqdKlnE) ⭐️ 8.0/10

在 2019 年 GDC 的一场演讲中，Freehold Games 的开发者详细介绍了他们在《Qud 洞穴》中用于生成村庄的完整程序化生成系统，该系统通过算法创建历史、文化、建筑风格、非玩家角色和任务。 此演讲展示了一种超越简单关卡或地形创建的复杂程序化生成方法，用于模拟相互关联的社会和叙事系统，为游戏中的涌现式叙事设定了高标准。 该系统是“端到端”生成的，意味着高层的历史模拟会直接产出详细且连贯的村庄级内容，如具体的任务线和文化特征，从而确保了生成世界的一致性。

rss · Lobsters · May 22, 17:36

**背景**: 《Qud 洞穴》是一款以深度模拟和广泛程序化生成著称的科学幻想类 Roguelike 游戏。其世界生成系统会创建一段包含程序化生成的苏丹、地区和事件的历史，这构成了演讲中所讨论的村庄系统的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=jV-DZqdKlnE">End - to - End Procedural Generation in Caves of Qud - YouTube</a></li>
<li><a href="https://wiki.cavesofqud.com/wiki/World_generation">World generation - Official Caves of Qud Wiki End-to-End Procedural Generation in Caves of Qud Generating Anything and Everything in Caves of Qud Procedural World Generation : r/cavesofqud - Reddit Images Caves of Qud Procedural Generation Survive Your First Minutes! Subverting Historical Cause & Effect: Generation of Mythic ...</a></li>
<li><a href="https://media.gdcvault.com/gdc2019/presentations/Grinblat_Jason_End-to-End_Procedural_Generation.pdf">End-to-End Procedural Generation in Caves of Qud</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 讨论很可能包含了富有见解的技术辩论和社区对于生成复杂模拟历史和文化的新颖方法的兴趣，正如新闻条目评分理由中所强调的。

**标签**: `#procedural-generation`, `#game-development`, `#systems-design`, `#simulation`

---

<a id="item-18"></a>
## [美国联邦贸易委员会与考克斯媒体集团就欺骗性 AI“主动聆听”广告达成和解](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-require-cox-media-group-two-other-firms-pay-nearly-1-million-settle-charges-they-deceived) ⭐️ 8.0/10

美国联邦贸易委员会（FTC）要求考克斯媒体集团及另外两家公司支付总计 93 万美元，以和解他们通过虚假宣传一种名为“主动聆听”的 AI 驱动广告服务来欺骗客户的指控。 此次和解是一项重要的监管行动，追究了一家主要媒体公司在 AI 驱动广告中欺骗行为的责任，为未来在日益发展的 AI 营销技术领域的执法树立了重要先例。 这项名为“主动聆听”的技术被宣传为使用 AI 通过智能手机和智能扬声器监听现实世界对话以投放定向广告，但 FTC 发现其宣传具有欺骗性；和解要求财务处罚，但公司不承认有不当行为。

rss · Lobsters · May 22, 04:53

**背景**: “主动聆听”AI 技术声称使用人工智能分析对话中的实时语音数据，并将其与在线行为数据相结合，以定向向消费者投放广告。美国联邦贸易委员会（FTC）是负责消费者保护和防止欺骗性商业行为的美国机构。此次和解涉及考克斯媒体集团、MindSift LLC 和 1010 Digital Works LLC。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thecyberexpress.com/ftc-ai-powered-active-listening-case/">AI-Powered Marketing Service “Active Listening” Deceived ...</a></li>
<li><a href="https://cyberwarriorsmiddleeast.com/ftc-ai-powered-active-listening-case/">FTC Exposes Deception in AI-Powered Marketing Service “Active ...</a></li>

</ul>
</details>

**社区讨论**: 提供的内容链接到了 Lobsters 上的一个评论区，但输入中未包含具体的评论或讨论内容以供分析。

**标签**: `#AI ethics`, `#regulation`, `#marketing technology`, `#FTC`, `#consumer protection`

---

<a id="item-19"></a>
## [Linux 探索使用 BPF 实现自定义页面缓存淘汰策略](https://lwn.net/Articles/1073103/) ⭐️ 8.0/10

在 2026 年 Linux 存储、文件系统、内存管理和 BPF 峰会上，一场会议探讨了利用 BPF 为特定工作负载自定义内核页面缓存策略，以取代当前单一的淘汰策略。 页面缓存对系统整体性能影响巨大，基于 BPF 的可定制策略能够为不同应用进行精细化优化，有望提升默认策略表现不佳的工作负载的性能。 该方案建立在现有的研究基础之上，例如'cache_ext'框架，它利用内核的 struct_ops 机制通过 eBPF 程序实现可附加到特定 cgroup 的自定义淘汰策略。

rss · LWN.net · May 22, 14:37

**背景**: Linux 内核的页面缓存在内存中存储文件数据的副本（以'folio'为单位组织）以加速访问。内核使用淘汰策略来决定在需要内存时移除哪些页面。扩展伯克利数据包过滤器（eBPF）是一种允许在内核中运行沙盒程序的技术，无需修改内核源代码即可安全、动态地自定义内核功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cache-ext/cache_ext">cache_ext: Custom Page Cache Eviction Policies with eBPF</a></li>
<li><a href="https://deepwiki.com/cache-ext/cache_ext/3.2-ebpf-policy-system">eBPF Policy System | cache-ext/cache_ext | DeepWiki</a></li>
<li><a href="https://blogs.oracle.com/linux/intro-to-folios">An explanation of how folios improve memory management in Linux .</a></li>

</ul>
</details>

**标签**: `#Linux Kernel`, `#BPF`, `#Memory Management`, `#Page Cache`, `#Systems Optimization`

---

<a id="item-20"></a>
## [谷歌 Project Zero 发现 Pixel 10 手机零点击内核级漏洞](https://hackaday.com/2026/05/22/this-week-in-security-ai-generated-reports-more-ai-generated-reports-github-chaos-and-more-linux-vulnerabilities/) ⭐️ 8.0/10

谷歌的 Project Zero 团队展示了一个针对 Pixel 10 手机的新零点击漏洞利用，该漏洞允许攻击者无需任何用户交互，即可从远程访问实现对内核的完全控制。 此发现至关重要，因为一个能够提升至内核级别的零点击漏洞利用构成了严重的安全威胁，可能破坏设备的核心安全模型，并影响一款重要的新旗舰手机。 该漏洞利用是在 Project Zero 的一次调查过程中发现的，展示了从远程访问提升至内核级别的完整路径，揭示了该设备安全架构中的一个重大缺陷。

rss · Hackaday · May 22, 14:00

**背景**: Project Zero 是谷歌内部一个专门寻找零日漏洞（即先前未知的安全缺陷）的团队。零点击漏洞利用是一种无需用户交互（如点击链接）即可执行的攻击，因此尤为危险。Pixel 手机是谷歌的旗舰 Android 设备，而一个内核级别的漏洞利用意味着该漏洞针对的是操作系统的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Zero">Project Zero</a></li>
<li><a href="https://grokipedia.com/page/Zero-click_exploit">Zero-click exploit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero -day vulnerability - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#zero-day`, `#Android`, `#exploit`

---

<a id="item-21"></a>
## [字节跳动开源 3B 统一多模态模型 Lance](https://mp.weixin.qq.com/s/Xbfq72cr1796RZxJIs3L1A) ⭐️ 8.0/10

字节跳动开源了轻量级多模态模型 Lance，其激活参数量仅为 3B，却原生统一了图像理解、视频理解、图像生成和视频生成任务，并在 GenEval 和 VBench 等基准测试中取得了领先结果。 此次发布代表了在构建高效统一的多模态 AI 方面迈出的重要一步，允许单个模型处理多样化的视觉-语言任务，这可能简化开发流程并降低构建多模态应用的复杂性。 该模型采用了双流专家架构，分别使用 Qwen2.5-VL 和 Wan2.2 编码器处理理解与生成任务，并通过模态感知位置编码来解决序列边界混淆问题。它采用了宽松的 Apache 2.0 许可证发布。

telegram · zaihuapd · May 22, 06:40

**背景**: 统一多模态模型旨在单一架构内处理图像描述、视频理解和图像/视频生成等多种任务，这与针对每个任务的专用模型不同。双流专家架构通常为不同的模态或任务（如理解与生成）使用单独的处理路径或“专家”，以在统一能力的同时保持高性能。位置编码是 Transformer 模型中用于注入令牌顺序信息的技术，针对多模态调整它对于有效处理图像、视频和文本等混合输入至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41598-025-10930-1">Dual-stream interactive mechanism with multi-modal hierarchical ...</a></li>
<li><a href="https://arxiv.org/pdf/2510.23095">Revisiting Multimodal Positional Encoding in Vision-Language ...</a></li>
<li><a href="https://deepwiki.com/deepbeepmeep/Wan2GP/8.1-text-encoders">Text Encoders | deepbeepmeep/Wan2GP | DeepWiki</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#open-source`, `#computer-vision`, `#generative-ai`, `#bytedance`

---

<a id="item-22"></a>
## [Cloudflare 故障：25 分钟全球中断影响 28%的 HTTP 流量](https://t.me/zaihuapd/41527) ⭐️ 8.0/10

Cloudflare 发布了事件报告，详述了 2025 年 12 月 5 日发生的持续约 25 分钟的全球网络中断，此次故障影响了约 28%的 HTTP 流量，主要波及使用旧版 FL1 代理并启用了 Cloudflare 托管规则集的客户。 此事件凸显了向旧版基础设施大规模部署安全补丁的关键风险，因为单次配置更改导致一家主要互联网基础设施提供商的广泛网络中断，影响了很大一部分网络流量。 根本原因是针对 React Server Components 关键漏洞 CVE-2025-55182 的安全补丁，在禁用 WAF 规则测试工具时，无意中导致旧版 FL1 代理出现错误；而基于 Rust 的新系统未受影响。

telegram · zaihuapd · May 22, 16:15

**背景**: CVE-2025-55182 是一个影响 React Server Components 和 Next.js 框架的严重预认证远程代码执行漏洞，CVSS 评分为 10.0。Cloudflare 的 Web 应用程序防火墙 (WAF) 使用托管规则集，这些是预配置且定期更新的安全规则，用于防御常见的网络攻击。FL1 指的是 Cloudflare 较旧的、基于 Lua 的代理基础设施，目前正逐步被更现代的系统取代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=46162656">Cloudflare outage on December 5, 2025 | Hacker News</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2025/12/15/defending-against-the-cve-2025-55182-react2shell-vulnerability-in-react-server-components/">Defending against the CVE-2025-55182 (React2Shell ...</a></li>
<li><a href="https://developers.cloudflare.com/waf/managed-rules/">Managed Rules · Cloudflare Web Application Firewall (WAF) docs</a></li>

</ul>
</details>

**社区讨论**: 社区讨论，特别是在 Hacker News 和 LinkedIn 上，集中在汲取的运营教训上，强调了在全球范围而非逐步推出配置更改的危险性，以及在生产系统中维护旧版代码固有的风险。

**标签**: `#cloudflare`, `#incident-report`, `#web-infrastructure`, `#network-outage`, `#security-patch`

---