---
layout: default
title: "Horizon Summary: 2026-06-09 (ZH)"
date: 2026-06-09
lang: zh
---

> From 197 items, 12 important content pieces were selected

---

1. [苹果推出 Core AI，全新框架支持设备端模型运行](#item-1) ⭐️ 9.0/10
2. [苹果发布以谷歌 Gemini 模型为核心、注重隐私的全新 AI 架构。](#item-2) ⭐️ 8.0/10
3. [Cadence 与 NVIDIA 发布业界首款全自主 AI 芯片设计虚拟工程师](#item-3) ⭐️ 8.0/10
4. [OpenAI 秘密提交 IPO 申请，奥尔特曼的 Worldcoin 眼球扫描公司因营收困难裁员。](#item-4) ⭐️ 8.0/10
5. [芬兰初创公司 Donut Lab 的“革命性”钠离子固态电池被证实造假，实为普通锂离子电池。](#item-5) ⭐️ 8.0/10
6. [Meta 智能眼镜应用中隐藏人脸识别代码曝光后被紧急移除](#item-6) ⭐️ 8.0/10
7. [苹果 WWDC26：发布新系统、Siri AI 升级，库克完成最后一场主题演讲](#item-7) ⭐️ 8.0/10
8. [Alist 登录界面疑被劫持，指向被投毒的 Polyfill.io 脚本](#item-8) ⭐️ 8.0/10
9. [OpenAI 向美国证券交易委员会秘密提交 S-1 草案，筹备潜在首次公开募股](#item-9) ⭐️ 8.0/10
10. [苹果公司宣布 2026 年全球开发者大会活动](#item-10) ⭐️ 8.0/10
11. [人工智能发现 Zcash 关键隐私漏洞，可伪造代币](#item-11) ⭐️ 8.0/10
12. [Anthropic 秘密提交 S-1 招股书，为潜在 IPO 做准备，此前估值达 9650 亿美元](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [苹果推出 Core AI，全新框架支持设备端模型运行](https://developer.apple.com/documentation/coreai/) ⭐️ 9.0/10

苹果推出了 Core AI，这是一个全新的开发者框架，旨在转换并运行 AI 模型，使其能在苹果设备的 CPU、GPU 和神经引擎上协同工作。该框架在 WWDC 2026 上宣布，标志着从之前的 CoreML 框架的一次重大演进。 这标志着行业向设备端 AI 处理的重大转变，能够减少对云服务的依赖，增强用户隐私，并降低开发者的运营成本。此举可能会颠覆依赖云 API 服务的 AI 公司的商业模式。 Core AI 允许开发者将 PyTorch 等框架的模型转换为优化格式，并自动利用设备上最佳的可用硬件。该框架是苹果将其机器学习工作重新品牌化为更广泛的‘AI’的一部分，这从 CoreML 名称的转变中可以看出。

hackernews · hmokiguess · Jun 8, 18:47 · [社区讨论](https://news.ycombinator.com/item?id=48449665)

**背景**: 苹果的神经引擎是 Apple Silicon 芯片（A 系列和 M 系列）内的专用硬件加速器，旨在高效处理机器学习任务。Core ML 一直是苹果现有用于将训练好的模型集成到应用中的框架，主要针对苹果硬件上的推理进行了优化。向 Core AI 的转变表明，苹果正在推动现代化，以支持更广泛的 AI 工作负载和更无缝的跨设备硬件利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://letsdatascience.com/news/apple-replaces-core-ml-with-core-ai-3eaa8e92">Apple Replaces Core ML With Core AI | Let's Data Science</a></li>
<li><a href="https://dev.to/arshtechpro/core-ml-vs-foundation-models-which-should-you-use-3jo0">Core ML vs Foundation Models: Which Should You Use? - DEV Community</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Neural_Engine">Apple Neural Engine</a></li>

</ul>
</details>

**社区讨论**: 社区讨论参与度很高，开发者们分享了 Core AI 的 WWDC 会议链接，并争论它是否完全取代了 CoreML。许多评论对设备端 AI 实现‘无限 tokens’且无需月费表示兴奋，而一些人则认为这是一项战略举措，可能会削弱云端 AI 公司的护城河。

**标签**: `#apple`, `#on-device-ai`, `#coreml`, `#machine-learning`, `#developer-frameworks`

---

<a id="item-2"></a>
## [苹果发布以谷歌 Gemini 模型为核心、注重隐私的全新 AI 架构。](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/) ⭐️ 8.0/10

苹果宣布了一项新的 AI 架构，该架构将谷歌的 Gemini 模型集成到其注重隐私的苹果智能系统中，采用了设备端处理与新的私有云计算（PCC）框架相结合的方式处理云端任务。 此次合作是一项重大战略举措，使苹果能够迅速部署来自领先模型提供商的先进 AI 功能，同时尝试坚守其坚定的隐私承诺，这有可能重塑主要科技生态系统之间的竞争格局。 核心的技术挑战在于确保通过苹果私有云计算路由到谷歌模型的请求不会将用户上下文或可识别数据泄露给谷歌，这一点受到观察人士的质疑，也是苹果所宣称隐私保证的关键区分点。

hackernews · unclefuzzy · Jun 8, 19:14 · [社区讨论](https://news.ycombinator.com/item?id=48450142)

**背景**: 苹果智能是苹果对其设备端及云端 AI 功能的统称。私有云计算（PCC）是苹果设计的一种云架构，旨在以可验证的安全和隐私保障远程处理敏感的 AI 任务。谷歌 Gemini 是由谷歌 DeepMind 开发的一系列大型语言模型，与 OpenAI、Anthropic 等公司的模型竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.apple.com/blog/private-cloud-compute/">Private Cloud Compute: A new frontier for AI privacy in the cloud - Apple Security Research</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>
<li><a href="https://security.apple.com/documentation/private-cloud-compute">Private Cloud Compute Security Guide | Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区讨论凸显了人们对苹果在使用谷歌模型时能否真正防止用户数据泄露给谷歌的质疑，用户对隐私声明的技术可行性提出疑问。关于欧盟监管也有大量讨论，部分人希望欧盟能迫使苹果允许用户选择第三方 AI 模型，而另一些人则指出该服务未在欧盟发布可能是一个危险信号。

**标签**: `#Apple`, `#Google`, `#AI architecture`, `#privacy`, `#on-device AI`

---

<a id="item-3"></a>
## [Cadence 与 NVIDIA 发布业界首款全自主 AI 芯片设计虚拟工程师](https://www.ithome.com/0/961/795.htm) ⭐️ 8.0/10

在 COMPUTEX 2026 台北国际电脑展上，Cadence 宣布其在 NVIDIA 支持下打造的 ChipStack AI Super Agent 已达到 Level-5 级别的自主水平，成为业界首款具备全自主芯片设计能力的 AI 虚拟工程师。该智能体无需逐步提示即可独立执行复杂的芯片设计与验证工作流程。 这标志着 EDA 自动化领域的一次重大飞跃，将 AI 从辅助工程师的角色推向了可以充当自主工程师的层面，有望大幅加速芯片设计周期，让资深工程师专注于更具挑战性的高层级问题。这预示着半导体行业正朝着全自主工程智能体的方向发生重大转变。 该智能体基于 Cadence 的 AI 驱动 EDA 产品组合和 NVIDIA 的 Nemotron 模型构建，并在 NVIDIA OpenShell 沙箱环境中运行以确保安全。它能够评估中间结果，并在 RTL 生成、验证规划、仿真、调试等任务间不断迭代，直至目标完成，同时工程师仍可按需对其进行检查与指导。

rss · IT HOME · Jun 9, 02:28

**背景**: 在 AI 智能体的语境中，Level-5 自主级别指的是一个系统能够完全自我管理并在无需人类干预的情况下做出独立决策，这是许多自主系统的终极目标。NVIDIA Nemotron 模型系列采用了混合专家（MoE）架构，专为高吞吐量而设计；而 OpenShell 则提供了基于策略控制的沙箱执行环境，以确保 AI 智能体在安全运行的同时，不会发生数据泄露或未授权操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@angadi.saa/ai-the-5-levels-of-agentic-ai-systems-29cf46e75982">AI : The 5 Levels of Agentic AI Systems | by Shankar Angadi | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nemotron">Nemotron - Wikipedia</a></li>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#chip-design`, `#EDA`, `#automation`, `#NVIDIA`

---

<a id="item-4"></a>
## [OpenAI 秘密提交 IPO 申请，奥尔特曼的 Worldcoin 眼球扫描公司因营收困难裁员。](https://www.ithome.com/0/961/792.htm) ⭐️ 8.0/10

OpenAI 已秘密提交首次公开募股（IPO）申请，这可能是人工智能行业一个里程碑式的事件。与此同时，山姆·奥尔特曼的另一家公司，以 Worldcoin 虹膜扫描项目闻名的 Tools for Humanity，正因严重的营收困难进行裁员。 IPO 申请标志着 OpenAI 正在向大型上市公司转型，这可能巩固其市场领导地位并为进一步的 AI 发展提供资金。Tools for Humanity 的裁员则凸显了雄心勃勃但未经验证的生物识别加密货币项目所面临的财务压力和执行挑战，反映了外界对其商业模式的更广泛质疑。 Tools for Humanity 的投后估值达 25 亿美元，由 Andreessen Horowitz 和 Bain Capital 等知名区块链投资机构支持。该公司在国际上面临重大的监管和伦理阻力，包括因虹膜扫描数据收集引发的隐私问题，在肯尼亚被全面叫停运营，并在韩国被处以罚款。

rss · IT HOME · Jun 9, 02:19

**背景**: Worldcoin（现为 World Network 的一部分）是一个项目，使用专门的 Orb 硬件扫描人的虹膜，以在区块链上创建独特的数字身份。这种生物识别验证旨在证明“人性”，区分真人和机器人，并支持其关联的 Worldcoin（WLD）加密货币。该项目因其数据收集实践，既吸引了大量风险投资，也受到了公众和监管机构的密切关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_(blockchain)">World (blockchain) - Wikipedia</a></li>
<li><a href="https://arstechnica.com/tech-policy/2023/05/openai-ceo-raises-115m-for-crypto-company-that-scans-peoples-eyeballs/">OpenAI CEO raises $115M for crypto company that scans ...</a></li>
<li><a href="https://financefeeds.com/worldcoin-sells-135m-in-tokens-to-andreessen-horowitz-bain-capital-crypto/">Worldcoin Sells $135M In Tokens To Andreessen Horowitz , Bain ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#IPO`, `#AI`, `#Worldcoin`, `#Tech Industry`

---

<a id="item-5"></a>
## [芬兰初创公司 Donut Lab 的“革命性”钠离子固态电池被证实造假，实为普通锂离子电池。](https://www.ithome.com/0/961/748.htm) ⭐️ 8.0/10

由 20 多位独立电池专家进行的全面调查最终证实，芬兰初创公司 Donut Lab 宣传为革命性钠离子固态电池的产品，实际上是普通的锂离子电池。 此案揭露了清洁能源领域一起重大的技术骗局，影响了超过 1300 名投资约 2500 万美元的小投资者，并可能损害公众对正当固态电池研发努力的信任。 关键证据包括电池的电压曲线与高镍锂离子电池匹配，以及其膨胀曲线显示出石墨负极特有的明显拐点，这是锂离子电池而非钠离子电池的特征。

rss · IT HOME · Jun 9, 01:12

**背景**: 钠离子电池因钠资源丰富而被视为锂离子电池的有前途的替代品，但其电化学特性不同，如工作电压较低。固态电池使用固态电解质替代液态电解质，因其在安全性和能量密度方面的潜在改进，已成为主要研发领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sodium-ion_battery">Sodium-ion battery - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s42154-019-00080-2">A Comparative Study of Charging Voltage Curve Analysis and ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6854841/">Methods and Protocols for Reliable Electrochemical Testing in Post-Li Batteries (Na, K, Mg, and Ca) - PMC</a></li>

</ul>
</details>

**标签**: `#battery technology`, `#fraud`, `#startup scandal`, `#sodium-ion battery`, `#lithium-ion battery`

---

<a id="item-6"></a>
## [Meta 智能眼镜应用中隐藏人脸识别代码曝光后被紧急移除](https://www.ithome.com/0/961/724.htm) ⭐️ 8.0/10

Meta 被发现在其雷朋智能眼镜的配套应用程序中嵌入了一个名为‘NameTag’的休眠人脸识别功能。在《连线》杂志公开报道此事仅一天后，Meta 便通过更新移除了这段代码。 此事件引发了重大的隐私和伦理担忧，因为该代码旨在未经同意的情况下扫描和识别他人，可能使环境中的生物特征监控常态化。这凸显了在消费电子产品开发中有用的 AI 功能与保护个人隐私权之间的紧张关系。 ‘NameTag’功能可以自动采集沿途遇到的人的面部图像，并将其转换为存储在手机本地的生物特征标识，同时对新的扫描信息进行交叉比对。Meta 通讯副总裁称这只是试点项目，但该代码已被编写、审核并搭载到了正式上线的应用程序中。

rss · IT HOME · Jun 8, 22:57

**背景**: Meta 的雷朋智能眼镜是与依视路陆逊梯卡集团合作开发的 AI 驱动可穿戴设备，内置摄像头，此前曾因未经授权的录制等隐私问题引发争议。在此类设备上实现常开型人脸识别功能是 AI 伦理领域的重大关切，因为它可能在公共场所实现对个人的无感识别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/meta-smart-glasses-face-recognition-nametag-connections/">Meta Silently Added Face-Recognition Code for Its Smart ...</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/06/victory-meta-strips-facial-recognition-code-smart-glasses-app-after-public-outcry">VICTORY: Meta Strips Facial Recognition Code From Smart Glasses App ...</a></li>
<li><a href="https://www.biometricupdate.com/202606/smart-glasses-mobile-frt-normalize-ambient-biometric-surveillance">Smart glasses, mobile FRT normalize ambient biometric surveillance</a></li>

</ul>
</details>

**标签**: `#privacy`, `#facial-recognition`, `#AI ethics`, `#Meta`, `#smart glasses`

---

<a id="item-7"></a>
## [苹果 WWDC26：发布新系统、Siri AI 升级，库克完成最后一场主题演讲](https://www.ithome.com/0/961/722.htm) ⭐️ 8.0/10

苹果发布了包括 iOS 27 和 macOS Golden Gate 在内的所有操作系统新一代版本，重点在于性能提升，并对 Siri 进行了重大 AI 升级。此次发布会也是蒂姆·库克在转任执行董事长前的最后一场主题演讲。 Siri 的深度 AI 升级代表了苹果生态系统的重大飞跃，有望重塑用户在其所有平台上的交互方式。领导层的交接标志着一个时代的结束和公司新战略阶段的开始。 性能优化包括应用启动速度最高提升 30%、隔空投送速度最高提升 80%，并且 CPU 调度器的改进已向后兼容至 iPhone 11。新版 macOS 对其“液态玻璃”设计进行了大量 UI 精修，并彻底重建了系统的搜索基础架构。

rss · IT HOME · Jun 8, 22:50

**背景**: WWDC 是苹果公司每年举行的全球开发者大会，传统上会在该大会上预览其所有平台即将推出的软件更新。蒂姆·库克自 2011 年起担任苹果公司首席执行官，带领公司在服务以及 iPhone 和 Apple Watch 等产品上实现了巨大增长。

**标签**: `#Apple`, `#WWDC`, `#iOS`, `#AI`, `#Leadership`

---

<a id="item-8"></a>
## [Alist 登录界面疑被劫持，指向被投毒的 Polyfill.io 脚本](https://www.v2ex.com/t/1218951#reply7) ⭐️ 8.0/10

一名用户发现其自建的 alist 实例登录界面被一个来自 polyfill.io 的弹出窗口替换，且该窗口无法接受其登录凭证，这暗示了一次可能的供应链攻击。 Alist 是一款广泛使用的自托管文件管理工具，此类攻击可能危及用户凭证和服务器安全，凸显了开源软件依赖项中供应链漏洞的持续风险。 该事件与已被记录的 polyfill.io 供应链攻击有关，在该攻击中，一个被入侵的 JavaScript CDN 服务被用来向超过 10 万个网站注入恶意代码，可能将用户重定向到钓鱼门户。

rss · V2EX · Jun 9, 01:51

**背景**: Polyfill.io 是一项提供 JavaScript polyfill 以确保浏览器兼容性的流行服务，但其域名被一家中国公司收购后，在一次重大的供应链攻击中遭到入侵。Alist 是一个支持多种存储提供商的开源文件列表程序，常部署在个人服务器上，这使其成为攻击者拦截用户数据的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.qualys.com/vulnerabilities-threat-research/2024/06/28/polyfill-io-supply-chain-attack">Polyfill.io Supply Chain Attack: What You Need to Know - Qualys Blog</a></li>
<li><a href="https://alistgo.com/">Home | AList Docs</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain-attack`, `#alist`, `#self-hosted`, `#javascript`

---

<a id="item-9"></a>
## [OpenAI 向美国证券交易委员会秘密提交 S-1 草案，筹备潜在首次公开募股](https://openai.com/index/openai-submits-confidential-s-1) ⭐️ 8.0/10

OpenAI 已向美国证券交易委员会（SEC）秘密提交了一份注册声明草案，即 S-1 表格。这是迈向潜在首次公开募股（IPO）的一个正式初步步骤，但该公司尚未确定任何进一步行动的时间或条款。 这份文件的提交标志着全球领先人工智能组织的一个重要财务和公司治理里程碑，预示着它正从私人实体转型，并可能重塑人工智能行业的投资格局。一次成功的首次公开募股将为 OpenAI 提供大量资金，并可能为其他主要人工智能公司树立先例。 该提交是在保密审查程序下进行的，这允许美国证券交易委员会在不公开披露的情况下提供反馈，从而保护敏感的商业信息。公司明确表示尚未确定任何进一步行动的时间表，这意味着首次公开募股并非迫在眉睫，可能会被推迟或取消。

rss · OpenAI Blog · Jun 8, 14:00

**背景**: S-1 表格是公司在美国向公众发售股票之前必须向美国证券交易委员会提交的正式注册声明。美国证券交易委员会的保密审查程序，特别是针对'新兴成长型公司'的，允许企业提交注册声明草案进行非公开的内部审查，以帮助他们在正式公开提交之前，在公众视线之外完善文件。这是许多公司探索首次公开募股时采用的常见策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sec.gov/about/divisions-offices/division-corporation-finance/draft-registration-statement-processing-procedures-expanded">Enhanced Accommodations for Issuers Submitting Draft Registration Statements - SEC.gov</a></li>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Understanding Confidential IPO Filings - DFIN</a></li>
<li><a href="https://www.gtlaw.com/en/insights/2025/3/sec-expands-confidential-review-process-for-draft-registration-statements">SEC Expands Confidential Review Process for Draft Registration Statements | Insights</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#IPO`, `#SEC filing`, `#corporate news`, `#AI industry`

---

<a id="item-10"></a>
## [苹果公司宣布 2026 年全球开发者大会活动](https://www.apple.com/apple-events/event-stream/) ⭐️ 8.0/10

苹果公司已正式宣布其 2026 年全球开发者大会（WWDC）活动，活动页面现已上线。此次公告包含一个专门的 Lobsters 社区讨论链接，以便开发者参与交流。 WWDC 是苹果公司的旗舰年度活动，用于发布重大软件更新、新的开发者工具和框架，这些内容常常引领行业趋势。该会议直接影响数百万为苹果生态系统开发的开发者，并波及更广泛的科技领域。 活动页面托管在苹果官方网站上，社区讨论通过 Lobsters 平台进行，该平台在开发者中颇受欢迎。公告中使用了“WWDC26”作为简称，这符合苹果公司一贯的活动命名惯例。

rss · Lobsters · Jun 8, 16:52

**背景**: 苹果全球开发者大会（WWDC）是一个专注于苹果平台（包括 iOS、macOS、watchOS 等）软件和工具的年度活动。它通常包括主题演讲、技术讲座和面向开发者的实验室环节。该活动是苹果传达其战略方向并提前提供新技术的关键平台。

**社区讨论**: 链接的 Lobsters 讨论帖为开发者提供了一个社区中心，用于分享对 WWDC 2026 公告的看法、分析和反应。此类论坛通常会围绕新 API 设计、框架变更以及苹果平台演进的深层影响展开辩论。

**标签**: `#apple`, `#developer-conference`, `#software-development`, `#ios`, `#tech-event`

---

<a id="item-11"></a>
## [人工智能发现 Zcash 关键隐私漏洞，可伪造代币](https://www.schneier.com/blog/archives/2026/06/critical-zcash-vulnerability-found-and-fixed.html) ⭐️ 8.0/10

5 月 29 日，安全研究员泰勒·霍恩比使用 Claude Opus 4.8 人工智能模型，发现了 Zcash 的 Orchard 隐私池中一个存在四年之久的关键漏洞。该漏洞可能让攻击者通过利用零知识证明系统中的一个错误输入验证检查，凭空创造 ZEC。 此次发现既凸显了先进加密隐私系统中漏洞的严重性，也展示了人工智能作为主动安全研究强大工具的新兴作用。修复此漏洞需要 Zcash 进行有史以来最大规模的网络升级，以修补一个若被利用将严重损害货币价值和完整性的缺陷。 该漏洞存在于 Orchard 池的零知识证明电路中，其未能正确执行一项关键的输入验证规则，理论上允许无限量伪造。Zcash 团队已完成一次重大的网络升级来修复该电路，目前尚无证据表明该漏洞已在实际中被利用。

rss · Schneier on Security · Jun 8, 17:06

**背景**: Zcash 是一种注重隐私的加密货币，它使用零知识证明（ZKPs）让用户可以在公共区块链上交易而不泄露发送方、接收方或金额详情。Orchard 池于 2022 年推出，是其最先进的屏蔽交易系统，代表了 Zcash 隐私架构的核心部分。零知识证明是一种密码学方法，可以在不透露任何底层数据的情况下证明一个陈述是真实的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/zcash-completes-largest-network-upgrade-to-fix-orchard-privacy-pool-vulnerability">Zcash Completes Its Largest Network Upgrade to Address the Orchard Privacy Pool Vulnerability | KuCoin</a></li>
<li><a href="https://decrypt.co/369896/zcash-completes-most-ambitious-network-upgrade-zec-resumes-recent-surge">Zcash Completes 'Most Ambitious' Network Upgrade as ZEC Resumes Recent Surge - Decrypt</a></li>
<li><a href="https://cryptoadventure.com/what-is-the-orchard-pool-zcash-shielded-transactions-zk-proofs-and-inflation-risk/">What Is the Orchard Pool? Zcash Shielded Transactions, ZK Proofs, and Inflation Risk</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#security`, `#zero-knowledge-proofs`, `#AI-assisted-research`, `#vulnerability-disclosure`

---

<a id="item-12"></a>
## [Anthropic 秘密提交 S-1 招股书，为潜在 IPO 做准备，此前估值达 9650 亿美元](https://t.me/zaihuapd/41843) ⭐️ 8.0/10

Anthropic 已向美国证券交易委员会秘密提交了一份注册声明草案（S-1 表格），为潜在的首次公开募股奠定基础。此举紧随其近期破纪录的 650 亿美元 H 轮融资，该轮融资使这家人工智能公司的估值达到 9650 亿美元。 此次提交文件表明，领先的人工智能公司之一正准备登陆公开市场，这将是其投资者的重大套现事件，也是对公开市场对高估值人工智能公司兴趣的一次重要检验。它反映了人工智能行业的快速扩张和投资者的信心，尤其是在构建大型语言模型的公司中。 此次秘密提交是标准的初步步骤，允许公司与监管机构和机构投资者进行私下沟通；最终是否推进 IPO、发行股数及定价均未确定，取决于市场状况。Anthropic 近期发布了 Claude Opus 4.8 模型，这是其 Opus 系列中最强大的模型，支持 100 万 token 的上下文窗口。

telegram · zaihuapd · Jun 9, 01:10

**背景**: 秘密提交 S-1 文件是美国 2012 年《乔布斯法案》允许的一个流程，公司可以向 SEC 提交 IPO 注册文件而无需立即公开披露，从而在准备阶段提供更大的灵活性并减少压力。Anthropic 是一家成立于 2021 年的美国人工智能安全与研究公司，以开发 Claude 系列大型语言模型而闻名，其估值在巨额融资的推动下呈爆炸式增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Form_S-1">Form S-1 - Wikipedia</a></li>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Understanding Confidential IPO Filings</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4 . 8 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#IPO`, `#Anthropic`, `#business`, `#investment`

---