---
layout: default
title: "Horizon Summary: 2026-05-25 (ZH)"
date: 2026-05-25
lang: zh
---

> From 167 items, 10 important content pieces were selected

---

1. [APKPure 上的 Telegram 官方 APK 被发现植入间谍后门](#item-1) ⭐️ 9.0/10
2. [Epic 公布虚幻引擎 6，以《火箭联盟》作为首个展示游戏](#item-2) ⭐️ 9.0/10
3. [华为提出“韬定律”与“逻辑折叠”技术，探索半导体演进新路径](#item-3) ⭐️ 8.0/10
4. [美国初创公司 Bexorg 利用 BrainEx 系统在离体人脑上测试药物](#item-4) ⭐️ 8.0/10
5. [新型全息 3D 打印技术实现 70 倍效率提升](#item-5) ⭐️ 8.0/10
6. [阿里达摩院玄铁 C9 处理器成为首款全面支持安卓 16 的 RVA23 RISC-V 芯片。](#item-6) ⭐️ 8.0/10
7. [我国将首次在太空连续培育两代水稻](#item-7) ⭐️ 8.0/10
8. [苹果 WWDC 将是库克作为 CEO 的最后一次主题演讲，特努斯即将接任](#item-8) ⭐️ 8.0/10
9. [长鑫科技董事长朱一明让渡近半持股激励员工，并承诺十年不减持](#item-9) ⭐️ 8.0/10
10. [谷歌文档推出 Docs Live 功能，支持语音对话生成文档](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [APKPure 上的 Telegram 官方 APK 被发现植入间谍后门](https://x.com/EricParker/status/2058411298195661221) ⭐️ 9.0/10

通过 APKPure 应用商店分发的 Telegram 官方版 12.6.5 被重新打包，其代码中被植入了一个名为 DataCollector 的恶意间谍框架。该后门可窃取大量数据，包括聊天记录、通讯录、照片、文档、GPS 定位和 SIM 卡信息。 此事件是一次重大的供应链攻击，破坏了用户对流行第三方应用商店的信任，直接威胁到从 APKPure 下载应用的数百万 Telegram 用户的隐私和安全。它凸显了在广泛使用的通信工具中植入恶意软件的持续风险。 恶意负载被嵌入一个附加文件（classes3.dex）中，包含超过 3000 行代码，窃取的数据在传输到特定命令与控制服务器（IP 地址 38.190.225.166）之前会使用 AES-GCM 进行加密。

telegram · zaihuapd · May 24, 11:38

**背景**: 供应链攻击通过入侵软件或其分发渠道，在软件到达最终用户之前植入恶意软件。APKPure 是一个托管 APK 文件的第三方安卓应用商店，APK 文件是安卓应用的安装包。重新打包 APK 涉及反编译应用、插入恶意代码，然后使用新的数字证书重新编译和签名，以分发木马化版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/academy/application-security/supply-chain-attacks">Supply Chain Attacks: Examples & Strategies - wiz.io</a></li>
<li><a href="https://seedsecuritylabs.org/Labs_16.04/Mobile/Android_Repackaging/Android_Repackaging.pdf">Android Repackaging Attack Lab</a></li>
<li><a href="https://medium.com/@anyrun/understand-encryption-in-malware-aes-lu0bot-example-1080a58736ab">Understand Encryption in Malware: AES (Lu0Bot Example) | by ANY.RUN | Medium</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain-attack`, `#malware`, `#telegram`, `#privacy`

---

<a id="item-2"></a>
## [Epic 公布虚幻引擎 6，以《火箭联盟》作为首个展示游戏](https://www.pcgamer.com/gaming-industry/epic-reveals-first-unreal-engine-6-game-and-its-not-fortnite/) ⭐️ 9.0/10

Epic Games 正式公布了虚幻引擎 6，并确认载具足球游戏《火箭联盟》是首款展示运行在该新引擎上的游戏，实现了从虚幻引擎 3 的直接跨代升级。 此次公布标志着游戏开发行业的一个重大里程碑，意味着 Epic 广泛使用的游戏引擎进入新世代，可能影响成千上万的开发者以及实时 3D 内容创作的未来。 展示的游戏画面被描述为“游戏内实时录制”，这与虚幻引擎 5 发布时较长的技术演示不同；值得注意的是，Epic 尚未详细说明 UE6 相比 UE5 的具体技术优势。

telegram · zaihuapd · May 25, 02:20

**背景**: 虚幻引擎是全球最受欢迎的游戏引擎之一，被用于开发无数电子游戏和其他实时 3D 应用。其前代版本虚幻引擎 5 于 2022 年发布，引入了用于虚拟化几何体的 Nanite 等技术。此次公告正值 UE5 因在 PC 端的优化问题而备受批评之际，而且 Epic 的首席执行官此前曾表示将在几年内从 UE5 过渡到 UE6，整合 Verse 等新编程工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unrealengine.com/unreal-engine-5">Unreal Engine 5</a></li>
<li><a href="https://www.reddit.com/r/pcgaming/comments/1kep0xt/epics_tim_sweeney_shares_first_details_about/">Epic's Tim Sweeney shares first details about Unreal Engine 6</a></li>

</ul>
</details>

**标签**: `#game development`, `#unreal engine`, `#epic games`, `#rocket league`, `#game engine`

---

<a id="item-3"></a>
## [华为提出“韬定律”与“逻辑折叠”技术，探索半导体演进新路径](https://www.ithome.com/0/954/720.htm) ⭐️ 8.0/10

在 IEEE ISCAS 2026 大会上，华为发表了“韬（τ）定律”，提出以“时间缩微”替代“几何缩微”作为半导体演进新原则，并通过“逻辑折叠”等创新技术压缩信号传播时延、提升晶体管密度。 此举为半导体行业提供了一条超越摩尔定律的潜在路径，强调从器件到系统的多层级协同优化，以在传统几何缩微逼近物理极限时继续实现性能和密度提升。 该多层级协同优化体系涵盖电路层的逻辑折叠技术以缩短关键路径走线、芯片层的全栈软硬芯协同设计，以及系统层的灵衢总线协议以降低通信时延；华为预计，到 2031 年基于该定律的高端芯片晶体管密度可达 1.4 纳米制程同等水平。

rss · IT HOME · May 25, 02:48

**背景**: 摩尔定律观察到芯片上的晶体管数量约每两年翻一番，驱动了半导体行业数十年的发展，但如今正面临物理和经济上的根本性极限。传统的“几何缩微”通过先进光刻技术缩小晶体管尺寸，但随着工艺节点逼近原子尺度，这一路径变得日益困难和昂贵。华为的方法将焦点转移到优化整个系统堆栈中信号传播的基本“时间常数”（τ）上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huawei.com/en/news/2025/9/hc-lingqu-ai-superpod">Huawei Unveils World's Most Powerful SuperPoDs and... - Huawei</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#chip-design`, `#Huawei`, `#architecture`, `#IEEE`

---

<a id="item-4"></a>
## [美国初创公司 Bexorg 利用 BrainEx 系统在离体人脑上测试药物](https://www.ithome.com/0/954/713.htm) ⭐️ 8.0/10

美国初创公司 Bexorg 研发了专有的 BrainEx 系统，该系统能将捐赠的离体人脑维持存活，用于测试针对帕金森病和阿尔茨海默病等神经退行性疾病的实验性药物。 这种方法相比动物模型或细胞培养提供了更真实的药物测试环境，有望加速神经系统疾病治疗方法的开发，并减少对早期人体试验的依赖。 大脑通过人工血液和氧气维持，其电活动被丙泊酚等麻醉剂抑制；Bexorg 已研究了 700 多颗大脑，正在准备首篇论文，同时美国 FDA 已批准一项基于其数据的药物临床试验。

rss · IT HOME · May 25, 02:25

**背景**: 离体器官维持技术涉及向体外器官灌注含氧溶液以保持细胞功能，Bexorg 将此技术应用于大脑。丙泊酚是一种常见的静脉麻醉剂，通过增强 GABA 受体活性来诱导镇静，有助于抑制这些实验中的神经活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neuwritesd.org/2019/06/13/brainex-restoring-brain-circulation-after-death/">BrainEx: Restoring Brain Circulation After Death | NeuWrite San Diego</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6552398/">Bioengineering approaches to organ preservation ex vivo - PMC - NIH</a></li>
<li><a href="https://go.drugbank.com/drugs/DB00818">Propofol : Uses, Interactions, Mechanism of Action | DrugBank</a></li>

</ul>
</details>

**标签**: `#biotechnology`, `#neuroscience`, `#pharmaceutical research`, `#ethics`, `#medical innovation`

---

<a id="item-5"></a>
## [新型全息 3D 打印技术实现 70 倍效率提升](https://www.ithome.com/0/954/679.htm) ⭐️ 8.0/10

瑞士洛桑联邦理工学院（EPFL）的研究团队开发了一种使用相位光调制器（PLM）MEMS 器件的新型全息体积 3D 打印系统，与传统的振幅调制相比，光能利用效率提升了 70 倍。这使得打印复杂、多尺度的结构（如人耳模型）仅需两分多钟，且只需使用 150 毫瓦的激光。 这一突破通过使用极低功率的激光实现高分辨率、大尺寸打印，显著降低了体积 3D 打印的成本和复杂度，有望使该技术在医疗器械、组织工程和快速原型制造等领域更易于应用。无需更换硬件即可进行多尺度打印的能力，可能加速需要精细定制部件的领域的研发周期。 关键创新在于将相位光调制器集成到体积打印系统中，该器件调制光的相位而非振幅，从而实现了 70 倍的效率提升。该系统可以使用 150 毫瓦的激光打印最大 3 x 3 x 4 cm³的物体，并允许从微米级支架到厘米级模型的数字缩放，无需更换硬件。

rss · IT HOME · May 25, 01:32

**背景**: 体积 3D 打印，也称为全息或断层摄影 3D 打印，通过从多个角度将光图案投射到光固化树脂中，以同时固化整个 3D 体积，而不是逐层打印。传统系统通常使用振幅调制，通过阻挡光线来形成图案，浪费大量能量。相比之下，相位调制通过重定向光线而非吸收光线来实现，使其在生成高质量体积打印所需的复杂光场方面效率远高于传统方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41377-026-02331-4">High-efficiency multi-scale holographic volumetric 3D printing with a phase light modulator | Light: Science & Applications</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56852-4">Holographic tomographic volumetric additive manufacturing | Nature Communications</a></li>
<li><a href="https://wp.optics.arizona.edu/pablanche/wp-content/uploads/sites/37/2017/12/1707_Blanche_ApplSci7040411.pdf">Diffraction-Based Optical Switching with MEMS</a></li>

</ul>
</details>

**标签**: `#3D printing`, `#holographic printing`, `#additive manufacturing`, `#materials science`, `#medical devices`

---

<a id="item-6"></a>
## [阿里达摩院玄铁 C9 处理器成为首款全面支持安卓 16 的 RVA23 RISC-V 芯片。](https://www.ithome.com/0/954/672.htm) ⭐️ 8.0/10

阿里巴巴达摩院宣布，其玄铁 C9 系列处理器已完成对安卓 16 操作系统的适配，该处理器符合 RISC-V RVA23 规范，目前正面向战略合作伙伴发布。 这一里程碑表明 RISC-V 架构能够与最新安卓主流版本实现完全兼容，使其从基础功能移植迈入规范兼容与产品化交付的新阶段，为在移动设备和物联网领域的大规模商业落地奠定了关键的技术基础。 该平台已通过安卓主线中超过 68,000 项与 CPU 相关的核心 CTS/VTS 测试用例，并提供集成 40 余个安全应用的完整可信执行环境，支持安全启动和数字版权管理等功能。

rss · IT HOME · May 25, 01:13

**背景**: RISC-V 是一种开放标准的指令集架构，允许任何实体设计和制造处理器。RVA23 配置文件是 RISC-V 的一项关键规范，它为 64 位应用处理器定义了通用的指令集特性集合，这对软件生态系统的兼容性至关重要。安卓验证启动 (AVB)、通用内核镜像 (GKI) 和供应商接口 (VINTF) 是安卓系统中用于系统安全、内核标准化和软硬件分离的核心框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.riscv.org/reference/profiles/rva23/_attachments/rva23-profile.pdf">RVA 23 Profiles</a></li>
<li><a href="https://fprox.substack.com/p/risc-v-vector-cryptography-extensions">RISC-V Vector Cryptography Extensions (1/2)</a></li>
<li><a href="https://source.android.com/docs/core/architecture/partitions">Partitions overview | Android Open Source Project</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#Android`, `#processor`, `#embedded systems`, `#Alibaba`

---

<a id="item-7"></a>
## [我国将首次在太空连续培育两代水稻](https://www.ithome.com/0/954/670.htm) ⭐️ 8.0/10

5 月 24 日发射的神舟二十三号飞船将水稻种子等实验材料运抵中国空间站，以开展人类首次在轨连续培育两代水稻的实验。 该实验对于理解微重力环境下的跨代遗传稳定性至关重要，是实现未来长期深空探测任务中粮食原位可持续生产的关键一步。 实验材料包括曾经历太空环境的“祖先”种子繁衍的后代和从未上天的普通种子，并将对比有性繁殖与再生稻模式（营养繁殖）在空间环境下的适应性差异。

rss · IT HOME · May 25, 01:08

**背景**: 2022 年，中国科学家已在天宫空间站成功完成了水稻从种子到种子的全生命周期培养实验，初步证明了太空水稻种植的可行性。太空的微重力环境会改变基本的生物过程，而研究跨代影响是必要的，因为遗传机制和代谢的改变可能需要更长时间和后续世代才能显现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://worldscience.cn/c/2024-10-28/664270.shtml">空间微重力条件下的植物生长发育</a></li>
<li><a href="https://www.pku-iaas.edu.cn/list_63/1414.html">育种MBA | 0011 环境组学与未来生物学、农业和作物育种</a></li>
<li><a href="https://html.rhhz.net/linyekexue/html/20090725.htm">大青杨航天诱变植株早期抗氧化酶生化指标测定</a></li>

</ul>
</details>

**标签**: `#space biology`, `#agriculture`, `#genetics`, `#space exploration`, `#microgravity`

---

<a id="item-8"></a>
## [苹果 WWDC 将是库克作为 CEO 的最后一次主题演讲，特努斯即将接任](https://www.ithome.com/0/954/666.htm) ⭐️ 8.0/10

彭博社的马克·古尔曼报道称，苹果 2026 年 6 月 8 日的 WWDC 主题演讲将是蒂姆·库克作为 CEO 的最后一次演讲，约翰·特努斯将于 9 月 1 日正式接任 CEO 一职。 这标志着苹果公司蒂姆·库克时代的结束，以及这家全球最有价值的公司之一领导层重大交接的开始，将塑造苹果未来的产品战略和方向。 蒂姆·库克将转任执行董事长，并且未来不会再发表主题演讲，而约翰·特努斯作为 CEO 的首次重要公开亮相将是 9 月的 iPhone 发布会，据报道，折叠屏 iPhone 届时将是优先事项。

rss · IT HOME · May 25, 00:55

**背景**: 蒂姆·库克自 2011 年起担任苹果公司 CEO，接替史蒂夫·乔布斯。约翰·特努斯是苹果公司硬件工程高级副总裁。WWDC 是苹果公司一年一度的开发者大会，会上通常会宣布主要的软件更新，有时也会发布新硬件。

**标签**: `#Apple`, `#Leadership Transition`, `#WWDC`, `#Tech Industry`, `#Tim Cook`

---

<a id="item-9"></a>
## [长鑫科技董事长朱一明让渡近半持股激励员工，并承诺十年不减持](https://www.ithome.com/0/954/653.htm) ⭐️ 8.0/10

国内 DRAM 芯片龙头长鑫科技的创始人兼董事长朱一明自愿承诺，在公司上市后，将其持有的 7.68 亿股股份在十年内全部分配给公司员工作为长期激励，并锁定其剩余股份十年不减持。 这一举措，加上公司计划 IPO 前惊人的财务增长数据，展现了领导层对长鑫科技长期价值的强大信心，并可能有助于在竞争激烈的中国半导体行业留住人才。 朱一明合计持股 15.98 亿股（占比 2.6561%），其中用于分配的 7.68 亿股接近其持股的一半；其股份锁定期总长达 20 年，即在上市后十年内不减持，之后每年减持不超过 20%。

rss · IT HOME · May 25, 00:43

**背景**: 长鑫科技是中国领先的动态随机存取存储器（DRAM）芯片制造商。DRAM 是一种易失性存储器，是个人电脑、服务器和智能手机等计算设备的核心组件。该公司已申请在上海科创板上市，计划募集资金 295 亿元用于产能和技术升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jiuyangongshe.com/a/3y18xw1sxeq">长鑫科 技 、长江 存 储 上市，真正利好的是哪条半导体产业链？ -韭研公社</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#corporate governance`, `#IPO`, `#employee incentives`, `#DRAM`

---

<a id="item-10"></a>
## [谷歌文档推出 Docs Live 功能，支持语音对话生成文档](https://www.wsj.com/tech/personal-tech/google-docs-live-test-e4473e07) ⭐️ 8.0/10

谷歌推出了名为 Docs Live 的新功能，它利用 Gemini AI 将用户的语音对话直接转换成结构化的文档草稿。该工具支持用户口述想法，并通过语音指令调整大纲或语气，还能调用 Google Drive 中的文件或搜索网页信息来补充内容。 该功能有望极大地简化文档创建流程，特别是在头脑风暴和初稿撰写阶段，帮助用户克服“白纸焦虑”。这标志着先进的生成式人工智能直接集成到广泛使用的生产力软件中，可能改变人们创作内容的方式。 Docs Live 将首先面向 iOS 和 Android 端的付费 AI 订阅用户开放，随后计划逐步扩展到网页端及更多普通用户。该功能遵循 Google Workspace 的隐私规则，确保用户输入的数据不会用于模型训练。

telegram · zaihuapd · May 24, 09:39

**背景**: 谷歌文档是谷歌 Workspace 办公套件中广泛使用的云端文字处理软件，支持实时协作。Docs Live 利用了谷歌先进的 Gemini 系列大语言模型来理解和生成类人文本，实现从语音到文字的转换。该功能是科技公司将生成式人工智能直接嵌入日常生产力工具以提升用户效率的广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/tech/services-and-software/turn-your-spoken-ramblings-into-coherent-articles-with-google-docs-live/">Turn Your Spoken Ramblings Into Coherent Articles With Google ...</a></li>
<li><a href="https://www.gadgets360.com/ai/news/google-i-o-2026-docs-live-gmail-keep-gemini-ai-voice-us-rollout-11520723">Google I/O 2026: Docs Live Brings Gemini Voice AI to Gmail, Docs ...</a></li>
<li><a href="https://one.google.com/about/google-ai-plans/">Google AI Plans with Cloud Storage - Google One</a></li>

</ul>
</details>

**标签**: `#Google Docs`, `#AI Productivity Tools`, `#Voice-to-Text`, `#Generative AI`, `#Workspace AI`

---