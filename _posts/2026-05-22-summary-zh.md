---
layout: default
title: "Horizon Summary: 2026-05-22 (ZH)"
date: 2026-05-22
lang: zh
---

> From 206 items, 18 important content pieces were selected

---

1. [新研究：GPT-4.5 通过图灵测试，73%情况下被判定为人类。](#item-1) ⭐️ 9.0/10
2. [FreeBSD 14.x 内核漏洞导致本地权限提升](#item-2) ⭐️ 9.0/10
3. [AI 模型发现并利用苹果 M5 芯片上的 macOS 内核漏洞](#item-3) ⭐️ 9.0/10
4. [礼来 Retatrutide 在关键三期肥胖试验中实现 28.3%减重](#item-4) ⭐️ 9.0/10
5. [新型铁电 NAND 闪存可承受 1 亿次 X 光辐射，抗辐射能力提升 30 倍](#item-5) ⭐️ 8.0/10
6. [Windows 11 内核漏洞让攻击者可突破浏览器沙箱，获取系统最高权限。](#item-6) ⭐️ 8.0/10
7. [加州签署美国首份应对 AI 经济冲击的行政命令。](#item-7) ⭐️ 8.0/10
8. [因白宫内讧与科技游说，美国 AI 行政令突然取消](#item-8) ⭐️ 8.0/10
9. [美国投资 20 亿美元入股九家量子计算公司，IBM 独获 10 亿美元成立新芯片公司](#item-9) ⭐️ 8.0/10
10. [SpaceX 凭借重大行业交易崛起为主要 AI 算力供应商](#item-10) ⭐️ 8.0/10
11. [阿里发布新一代千问旗舰模型 Qwen3.7-Max，宣称国内最佳。](#item-11) ⭐️ 8.0/10
12. [Qt Bridges 让 C# 开发者能使用 Qt 框架构建界面](#item-12) ⭐️ 8.0/10
13. [微软研究院推出 Vega：用于隐私保护的数字身份验证](#item-13) ⭐️ 8.0/10
14. [OpenAI 的 GPT-next 模型证伪了埃尔德什 80 年前提出的平面单位距离猜想。](#item-14) ⭐️ 8.0/10
15. [在 Evince 等基于 GTK 的 PDF 阅读器中发现命令注入漏洞。](#item-15) ⭐️ 8.0/10
16. [英伟达第四季度营收达 681 亿美元，受 AI 需求推动上调下季度指引至 780 亿美元](#item-16) ⭐️ 8.0/10
17. [黄仁勋：英伟达已基本放弃中国 AI 芯片市场](#item-17) ⭐️ 8.0/10
18. [OpenAI Codex 新增 Mac 锁屏后继续操控应用功能](#item-18) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [新研究：GPT-4.5 通过图灵测试，73%情况下被判定为人类。](https://www.ithome.com/0/953/705.htm) ⭐️ 9.0/10

加州大学圣地亚哥分校发表在《美国国家科学院院刊》上的研究首次提供了实证数据，证明人工智能模型 GPT-4.5 能够通过图灵测试，在 15 分钟的聊天中以 73%的概率被判定为人类，超过了真人参与者的判定率。 这一里程碑表明，先进的人工智能能在对话中令人信服地模仿人类的社会行为，这对网络信任、社会工程攻击风险具有重大影响，并迫使人们重新评估图灵测试究竟衡量的是什么。 模型的成功依赖于被赋予特定的“人格”提示，以采用类似人类的沟通风格；在没有此类指导的情况下，其被判定为人类的概率急剧下降至 36%。研究还测试了其他模型，LLaMa-3.1-405B 达到了 56%，而经典的 ELIZA 聊天机器人和 GPT-4o 的得分则低得多。

rss · IT HOME · May 22, 01:22

**背景**: 图灵测试由艾伦·图灵于 1950 年提出，旨在评估机器展现出与人类无法区分的智能行为的能力。像 GPT-4.5 和 LLaMa 这样的大型语言模型（LLM）是基于海量文本数据训练、以生成类人回应的人工智能系统。ELIZA 于 20 世纪 60 年代创建，是使用简单模式匹配来模拟对话的早期聊天机器人，常被引用于人工智能历史中作为基线参照。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Eliza_(chatbot)">Eliza (chatbot)</a></li>
<li><a href="https://huggingface.co/blog/llama31">Llama 3 . 1 - 405 B , 70B & 8B with multilinguality and long context</a></li>

</ul>
</details>

**标签**: `#Turing Test`, `#GPT-4.5`, `#LLM`, `#AI Research`, `#Human-AI Interaction`

---

<a id="item-2"></a>
## [FreeBSD 14.x 内核漏洞导致本地权限提升](https://fatgid.io/) ⭐️ 9.0/10

一个名为 FatGid 的本地权限提升漏洞已被披露，影响 FreeBSD 14.x 内核，该漏洞利用 setcred(2)系统调用中的栈缓冲区溢出来获得提升的权限。 该漏洞很重要，因为它影响一个主要开源操作系统的内核，可能允许任何本地用户获得 root 权限，从而导致整个系统被入侵。 该利用链仅在 FreeBSD 14.x 上有效，因为存在一个 sizeof(*groups)的拼写错误；虽然 FreeBSD 15.0 也包含此拼写错误，但其不同的代码结构阻止了同一利用方式生效。

rss · Lobsters · May 21, 13:42

**背景**: FreeBSD 是一个免费开源的类 Unix 操作系统，以其高级的网络、安全和存储功能而闻名。内核本地权限提升（LPE）漏洞允许已拥有系统有限访问权限的攻击者，通过利用操作系统核心软件中的缺陷来获取更高权限，通常是 root 或管理员权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fatgid.io/">FatGid - FreeBSD 14.x kernel local privilege escalation</a></li>
<li><a href="https://www.freebsd.org/security/">FreeBSD Security Information | The FreeBSD Project</a></li>

</ul>
</details>

**社区讨论**: 该漏洞在 Lobsters 上进行了讨论，社区可能就该漏洞的技术细节、其现实世界的影响以及 FreeBSD 管理员的潜在缓解步骤进行了辩论。

**标签**: `#security`, `#FreeBSD`, `#kernel`, `#vulnerability`, `#LPE`

---

<a id="item-3"></a>
## [AI 模型发现并利用苹果 M5 芯片上的 macOS 内核漏洞](https://www.schneier.com/blog/archives/2026/05/macos-kernel-memory-corruption-exploit.html) ⭐️ 9.0/10

Calif 的研究人员使用了 Anthropic 尚未发布的 Claude Mythos AI 模型，在短短五天内发现了一个针对苹果 M5 芯片组的内核内存损坏漏洞，并成功开发了可工作的漏洞利用代码。 这是一项突破性演示，表明 AI 模型的能力已达到可以显著加速发现和利用关键安全漏洞的水平，预示着安全研究与防御领域的范式转变。 该漏洞利用针对的是苹果的 M5 芯片，该芯片设计了先进的硬件和软件缓解措施以大幅增加内存损坏攻击的难度，然而这个 AI 辅助的团队在五天内就绕过了这些防护。

rss · Schneier on Security · May 21, 16:03

**背景**: 内核内存损坏是一类漏洞，它允许软件意外地写入或读取计算机核心操作系统内存的区域，可能使攻击者获得完全控制权。苹果的 M 系列芯片采用了定制的硅片和系统级保护措施，例如指针认证码（PAC），以大幅增加此类攻击的难度。Mythos 模型是 Anthropic 最新的前沿 AI，在内部评估中因其强大的网络安全能力而备受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Assessing Claude Mythos Preview's cybersecurity capabilities - Anthropic Red</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#vulnerability`, `#kernel`, `#exploit`

---

<a id="item-4"></a>
## [礼来 Retatrutide 在关键三期肥胖试验中实现 28.3%减重](https://www.prnewswire.com/news-releases/lillys-triple-agonist-retatrutide-delivered-powerful-weight-loss-in-pivotal-phase-3-obesity-trial-302778859.html) ⭐️ 9.0/10

礼来公司公布了三期 TRIUMPH-1 试验的积极初步结果，其在研三重激动剂药物 retatrutide 在最高 12 毫克剂量组中，80 周后实现了平均 28.3%的体重减轻。 这些结果标志着肥胖治疗的重大突破，因为 retatrutide 实现的减重效果已接近减重手术的通常水平，可能为患有肥胖及相关合并症的患者提供一种强效的非手术治疗选择。 该试验纳入了约 2500 名患有肥胖或超重且至少伴有一种相关合并症的成年人；12 毫克剂量组中有 45.3%的参与者体重减轻至少 30%，且因不良事件导致的停药率低于安慰剂组。

telegram · zaihuapd · May 22, 02:18

**背景**: Retatrutide 是一种首创的在研药物，能同时激活三种激素受体：葡萄糖依赖性促胰岛素多肽（GIP）、胰高血糖素样肽-1（GLP-1）和胰高血糖素。这种三重激动剂机制旨在通过比司美格鲁肽或替尔泊肽等单一或双重激动剂更强的代谢效应实现更显著的减重效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ajmc.com/view/retatrutide-achieves-up-to-30-3-average-weight-loss-in-phase-3-triumph-1-trial">Retatrutide Achieves Up to 30.3% Average Weight Loss in Phase 3 TRIUMPH-1 Trial | AJMC</a></li>
<li><a href="https://www.pharmacytimes.com/view/retatrutide-delivers-bariatric-level-weight-loss-pivotal-phase-3-triumph-1-trial">Retatrutide Delivers Bariatric-Level Weight Loss in Pivotal Phase 3 TRIUMPH-1 Trial | Pharmacy Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLP1_poly-agonist_peptides">GLP 1 poly- agonist peptides - Wikipedia</a></li>

</ul>
</details>

**标签**: `#pharmaceutical`, `#clinical_trials`, `#obesity_treatment`, `#weight_loss`, `#drug_development`

---

<a id="item-5"></a>
## [新型铁电 NAND 闪存可承受 1 亿次 X 光辐射，抗辐射能力提升 30 倍](https://www.ithome.com/0/953/713.htm) ⭐️ 8.0/10

乔治亚理工学院的研究人员利用氧化铪开发出一种铁电 NAND 闪存，其辐射耐受性高达 100 万拉德，是传统 NAND 闪存的 30 倍。 这一突破使得在太空等极端辐射环境中为机载人工智能系统等关键应用实现可靠的大容量数据存储成为可能，解决了传统闪存在此类环境下失效的问题。 其关键创新在于利用材料的铁电极化状态而非俘获电荷来存储数据，从而对辐射引起的电荷干扰具有固有的抵抗力。这些芯片经测试可承受相当于 1 亿次胸部 X 光检查的辐射量，覆盖了从近地轨道到深空任务的辐射范围。

rss · IT HOME · May 22, 01:47

**背景**: 传统的 NAND 闪存通过将电子俘获在浮栅或电荷俘获层中来存储数据，这种机制容易受到太空中高能粒子的干扰而损坏。而像这种新型铁电 NAND（FeNAND）等铁电存储器，则采用不同的原理，通过铁电材料（如掺杂氧化铪 HfO2）的可逆极化方向来存储数据，因此对抗辐射干扰更为稳健。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ferroelectric_flash_memory">Ferroelectric flash memory - Wikipedia</a></li>
<li><a href="https://pubs.aip.org/aip/apl/article/121/24/240502/2834676/A-Perspective-on-ferroelectricity-in-hafnium-oxide">A Perspective on ferroelectricity in hafnium oxide: Mechanisms and considerations regarding its stability and performance | Applied Physics Letters | AIP Publishing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Radiation_hardening">Radiation hardening - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#radiation-hardened`, `#space technology`, `#materials science`, `#NAND flash`

---

<a id="item-6"></a>
## [Windows 11 内核漏洞让攻击者可突破浏览器沙箱，获取系统最高权限。](https://www.ithome.com/0/953/712.htm) ⭐️ 8.0/10

在 Windows 11 内核的 ntoskrnl.exe 文件中发现了一个关键漏洞（CVE-2026-40369），具体位于 ExpGetProcessInformation 函数内，允许攻击者绕过 Chrome 等主流浏览器的安全沙箱，并获取系统最高权限。 这一漏洞意义重大，因为它允许在浏览器中打开的恶意网站或载荷完全接管底层的 Windows 系统，破坏了现代网络浏览的基本安全模型，并且影响最新版本的 Windows 11。 该漏洞通过调用 NtQuerySystemInformation 函数并传入特定的信息类（253）和精心构造的缓冲区参数触发，由于长度为零时检查存在缺陷，从而绕过了内核的 ProbeForWrite 验证，并且利用链已被证明对沙箱逃逸的成功率为 100%。

rss · IT HOME · May 22, 01:46

**背景**: Windows 内核由 ntoskrnl.exe 文件管理，是操作系统的核心，而像 ExpGetProcessInformation 这样的函数用于系统管理任务。Chrome 等浏览器使用“沙箱”来隔离网络内容，防止恶意代码影响宿主系统。ProbeForWrite 是一种内核机制，旨在验证对用户空间缓冲区的写入访问权限，以防止安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ntoskrnl.exe">ntoskrnl.exe - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite">ProbeForWrite function (wdm.h) - Windows drivers | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#security`, `#Windows`, `#vulnerability`, `#kernel`, `#CVE`

---

<a id="item-7"></a>
## [加州签署美国首份应对 AI 经济冲击的行政命令。](https://www.ithome.com/0/953/710.htm) ⭐️ 8.0/10

美国加州州长加文·纽森于 5 月 21 日签署一项行政命令，指示州政府机构为人工智能（AI）带来的经济冲击做好准备并帮助缓解其对劳动力市场的干扰，这是美国首个此类行政命令。 这是美国一个主要州份针对 AI 对劳动力市场干扰采取的主动政策举措，可能为其他地区树立先例，并标志着政府对先进技术社会影响的具体回应。 该命令指示加州政府机构帮助工人获得分享 AI 收益的技能，追踪 AI 对劳动力市场的影响，并制定更强有力的公共政策来支持那些可能受到就业中断影响的人群。

rss · IT HOME · May 22, 01:45

**背景**: 生成式 AI 和先进自动化技术正在迅速改变许多行业的工作性质，引发了对工作岗位流失和经济不平等的担忧。行政命令是政府首脑发布的指令，在其行政管辖范围内具有法律效力，常用于设定政策优先事项和指导政府机构工作。

**标签**: `#AI policy`, `#labor market impact`, `#government regulation`, `#California`, `#workforce transition`

---

<a id="item-8"></a>
## [因白宫内讧与科技游说，美国 AI 行政令突然取消](https://www.ithome.com/0/953/708.htm) ⭐️ 8.0/10

北京时间 5 月 22 日，原定于周四签署的一项旨在加强 AI 监管的美国行政令被特朗普总统突然取消，此前该命令遭到了其顾问大卫·萨克斯以及科技公司 CEO 埃隆·马斯克和马克·扎克伯格的强烈反对，他们认为这会阻碍美国的竞争力。 此次政策反转凸显了特朗普政府内部反监管、支持技术“加速主义”的立场占据了上风，也表明科技行业游说对美国 AI 政策具有重大影响力，预示着美国在短期内可能对 AI 治理采取放任态度。 被取消的行政令草案要求企业在发布 AI 模型前最多提前 90 天向政府提交审查，但引发了为何由财政部而非网络安全机构主导此事的疑问。尽管该行政令被搁置，但据报道白宫国家网络主任办公室仍在制定其他 AI 安全举措。

rss · IT HOME · May 22, 01:37

**背景**: 这场辩论的核心是“AI 加速主义”——一种倡导在最小约束下快速推动技术进步的哲学——与呼吁进行预防性安全测试和监管以降低潜在风险之间的对立。在美国，这种政治张力体现了维持全球领导地位和产业增长的愿望与对 AI 社会影响和安全性的担忧之间的博弈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Accelerationism">Accelerationism</a></li>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">XAI (company)</a></li>

</ul>
</details>

**标签**: `#AI Regulation`, `#U.S. Policy`, `#Tech Lobbying`, `#AI Governance`, `#Geopolitics`

---

<a id="item-9"></a>
## [美国投资 20 亿美元入股九家量子计算公司，IBM 独获 10 亿美元成立新芯片公司](https://www.ithome.com/0/953/673.htm) ⭐️ 8.0/10

美国政府将以入股方式向九家量子计算公司投资 20 亿美元，其中 IBM 获得 10 亿美元，用于成立一家名为 Anderon 的量子芯片制造公司。这项由《芯片与科学法案》资助的计划，还向 GlobalFoundries 拨款 3.75 亿美元用于在美国建厂，并向 D-Wave 和 Rigetti Computing 等公司各提供约 1 亿美元。 这次大规模的政府投资凸显了量子计算对美国国家安全和经济竞争力的战略重要性，旨在增强国内能力并创造高科技就业岗位。这是美国政府在关键行业采取入股模式的又一最新案例，类似于此前对英特尔的做法，以强化供应链并提升技术领导力。 IBM 的新子公司 Anderon 总部将设在纽约州新奥尔巴尼，并计划向外部客户提供其量子芯片制造技术。值得注意的是，获得投资的两家公司 D-Wave 和 PsiQuantum 与特朗普政府有历史渊源，而本次资金最终来源于前总统拜登签署的法案激励措施。

rss · IT HOME · May 21, 23:02

**背景**: 量子计算利用量子力学原理执行复杂计算，速度远超传统计算机，在药物研发、金融建模和密码学等领域有巨大应用潜力。《芯片与科学法案》是美国为通过大量补贴和激励措施提振国内半导体制造与研究而颁布的一项重要法律。美国政府近期采取了一项策略，即直接入股被视为对国家安全至关重要的公司，此前对芯片制造商英特尔的投资便是一例。

**标签**: `#quantum computing`, `#government investment`, `#IBM`, `#semiconductor manufacturing`, `#technology policy`

---

<a id="item-10"></a>
## [SpaceX 凭借重大行业交易崛起为主要 AI 算力供应商](https://www.infoq.cn/article/fS0QHZiYGmZJZZNwk5V3?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

报告显示，Anthropic 承诺每年向 SpaceX 支付 150 亿美元用于计算资源，而 SpaceX 对 AI 编程初创公司 Cursor 的潜在收购包含一笔高达 100 亿美元的分手费，这使 SpaceX 成为 AI 基础设施领域的核心参与者。 这一转变可能将 SpaceX 打造成类似于英伟达在 GPU 领域地位的'算力庄家'，从根本上改变 AI 行业内的商业模式和力量格局。 Cursor 交易中的 100 亿美元分手费异常高昂，据报道占 600 亿美元收购价值的 17%，这远高于并购交易中通常 3-5%的分手费比例。

rss · InfoQ 中文站 · May 21, 15:23

**背景**: Anthropic 等 AI 公司需要巨大的计算能力来训练和运行其大型语言模型，这引发了对数据中心和超级计算机访问权的激烈竞争。以可复用火箭和星链网络闻名的 SpaceX，一直在向轨道数据中心和高性能计算领域扩张，可能利用其卫星基础设施提供全球分布的 AI 算力资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/cnbc_spacex-says-it-can-buy-cursor-later-this-activity-7452491823928868864-G6cT">SpaceX acquires AI startup Cursor for $60B | CNBC posted on the topic | LinkedIn</a></li>
<li><a href="https://www.reddit.com/r/cursor/comments/1ss7z42/spacexs_60b_agreement_to_acquire_cursor_is_wild/">SpaceX's $60B agreement to acquire Cursor is wild, but the $10B fallback is crazier. - Reddit</a></li>
<li><a href="https://thenextweb.com/news/spacex-cursor-60-billion-acquisition">SpaceX secures option to buy AI coding startup Cursor for $60B - TNW</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#SpaceX`, `#Anthropic`, `#tech industry`, `#business models`

---

<a id="item-11"></a>
## [阿里发布新一代千问旗舰模型 Qwen3.7-Max，宣称国内最佳。](https://www.infoq.cn/article/jAICqmzYVqQ8sHdGSzEH?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

阿里巴巴发布了其最新的旗舰级大语言模型 Qwen3.7-Max，并将其定位为中国国内表现最佳的模型。 此次发布加剧了中国人工智能领域的竞争，展示了国内大语言模型的快速进步，并可能影响该地区更广泛的技术和商业人工智能格局。 该模型被描述为旗舰级发布，但提供的内容缺乏具体的基准测试、参数数量或与其他模型的详细比较，无法进行独立验证。

rss · InfoQ 中文站 · May 21, 09:47

**背景**: Qwen（千问）是阿里云的大语言模型系列，一直作为中国提升国内人工智能能力战略的一部分进行积极开发和迭代。此处的“国产模型”主要指在中国境内开发和训练的 AI 模型，通常是国家实现技术自立自强努力的一部分。

**标签**: `#large language models`, `#AI research`, `#Chinese tech`, `#Qwen`, `#model release`

---

<a id="item-12"></a>
## [Qt Bridges 让 C# 开发者能使用 Qt 框架构建界面](https://www.v2ex.com/t/1214627#reply0) ⭐️ 8.0/10

Qt 已发布面向 C# 的 Qt Bridges 公测版，允许开发者创建作为 QML 组件在 Qt Quick 界面中运行的 C# 对象，下一个计划集成的语言是 Rust。 这一扩展显著降低了庞大的 C# 开发者社区利用 Qt 强大的跨平台 UI 框架的门槛，有望扩大 Qt 的生态系统并支持新的混合应用架构。 该测试版允许读写 C# 属性、调用 C# 方法、处理事件以及将 QML 属性绑定到 C# 集合，旨在让开发者以熟悉的 C# 风格编写后端代码，尽量减少 Qt 特定模式的使用。

rss · V2EX · May 22, 02:36

**背景**: Qt 是一个广泛使用的跨平台应用开发框架，用于创建图形用户界面，传统上需要 C++ 或 QML。QML 是一种用于设计 UI 的声明式语言，可以与用 C++ 等语言编写的后端逻辑集成。Qt Bridges 代表了一种新的方法，旨在无需创建完整、复杂的绑定即可将 Qt 的能力暴露给其他语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ics.com/blog/integrating-c-qml">Integrating C++ with QML | ICS</a></li>
<li><a href="https://ftp.nmr.mgh.harvard.edu/pub/dist/freesurfer/tutorial_packages_centos6/centos6/freesurfer-fsl-matlab-Linux-centos6_x86_64-dev/freesurfer/lib/qt/qt_doc/html/qtbinding.html">Qt 4.7: Using QML in C++ Applications</a></li>

</ul>
</details>

**标签**: `#Qt`, `#C#`, `#UI Framework`, `#Cross-Language`, `#Software Development`

---

<a id="item-13"></a>
## [微软研究院推出 Vega：用于隐私保护的数字身份验证](https://www.microsoft.com/en-us/research/blog/vega-zero-knowledge-proofs-for-digital-identity-in-the-age-of-ai/) ⭐️ 8.0/10

微软研究院推出了 Vega，这是一个零知识证明系统，允许用户从数字凭证中证明特定属性（如年龄或职业身份），而无需透露完整的凭证信息。 该系统解决了 AI 时代对隐私保护身份验证的迫切需求，在这个时代数字凭证的使用日益增多，但直接共享凭证可能面临暴露过多个人数据的风险。 Vega 能高效地将完整凭证转换为单一的选择性证明，并针对实际应用性能进行了设计，允许验证如人格证明或政府签发信息等属性，同时最大限度地减少数据暴露。

rss · Microsoft Research · May 21, 13:48

**背景**: 零知识证明是一种密码学方法，允许一方向另一方证明其知道特定信息，而无需透露信息本身。数字凭证（如政府颁发的身份证或专业证书）越来越多地以电子方式存储和验证，这便在便利性与隐私之间产生了权衡，而 Vega 等系统旨在解决这一矛盾。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/vega-zero-knowledge-proofs-for-digital-identity-in-the-age-of-ai/">Vega: Zero-knowledge proofs for digital identity in the age of AI - Microsoft Research</a></li>
<li><a href="https://eprint.iacr.org/2025/2094">Vega: Low-Latency Zero-Knowledge Proofs over Existing Credentials</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#digital identity`, `#privacy`, `#cryptography`, `#AI`

---

<a id="item-14"></a>
## [OpenAI 的 GPT-next 模型证伪了埃尔德什 80 年前提出的平面单位距离猜想。](https://www.latent.space/p/ainews-openai-gpt-next-disproves) ⭐️ 8.0/10

据称，OpenAI 的内部模型 GPT-next 生成了一个反例，证伪了埃尔德什平面单位距离猜想，这是一个在离散几何中悬而未决超过 80 年的问题。 这一突破展示了人工智能在形式数学推理能力上的重大进步，并可能深刻影响人工智能解决长期科学难题的方式。 该猜想认为，对于平面上的一组 n 个点，它们之间的单位距离数量最多为 O(n^{1+δ})（其中δ>0）；据报道，该模型的反例表明这一界限可以被超越。

rss · Latent Space · May 21, 07:28

**背景**: 埃尔德什平面单位距离猜想是数学家保罗·埃尔德什在离散几何中提出的一个著名问题，它涉及平面上 n 个点之间可能的最大单位长度线段数量。离散几何研究几何对象的组合性质，这类问题已被研究了数十年，旨在理解基本的空间排列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry</a></li>
<li><a href="https://www.reddit.com/r/mathematics/comments/1tixy6x/openai_model_produces_a_counterexample_to_erdőss/">OpenAI model produces a counterexample to Erdős's conjectured unit-distance bound : r/mathematics - Reddit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Erdős_distinct_distances_problem">Erdős distinct distances problem - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 网上的讨论，例如在 Reddit 的 r/mathematics 和 r/math 子版块，显示出极大的兴趣和怀疑态度，许多评论者寻求更多关于模型方法论、具体产生的反例以及验证过程的细节。

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research breakthrough`, `#formal reasoning`

---

<a id="item-15"></a>
## [在 Evince 等基于 GTK 的 PDF 阅读器中发现命令注入漏洞。](https://lwn.net/Articles/1073944/) ⭐️ 8.0/10

Michael Catanzaro 披露了一个影响多个基于 GTK 的 PDF 阅读器（包括 Evince、Atril 和 Xreader）的命令注入漏洞，该漏洞允许恶意 PDF 文件（同时也是有效的 ELF 二进制文件）在用户点击链接时执行任意代码。 该漏洞构成重大的现实世界安全风险，因为它仅需打开恶意 PDF 并点击链接即可在用户系统上执行任意代码，影响常见的 Linux 桌面应用程序。 该漏洞利用技术创建一个同时是有效 PDF 和有效 ELF 二进制文件的多语言文件，滥用 GTK 3 中的`--gtk-module`命令行标志将自身加载为模块，并通过其构造函数运行恶意代码；对于基于 GTK 4 的应用程序（如 Papers），该漏洞的严重性较低，因为该标志已被移除。

rss · LWN.net · May 21, 21:05

**背景**: Evince 等 PDF 阅读器在 Linux 桌面上被广泛使用。命令注入漏洞允许攻击者通过应用程序执行任意操作系统命令。ELF（可执行与可链接格式）是 Linux 及其他类 Unix 系统上可执行文件的标准文件格式。GTK（GIMP 工具包）是一个用于创建图形用户界面的流行工具包，可以通过加载模块来扩展其功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seclists.org/oss-sec/2026/q2/643">oss-sec: Re: Evince/Atril/Xreader command injection CVE-2026-46529</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#PDF`, `#GTK`, `#Linux`

---

<a id="item-16"></a>
## [英伟达第四季度营收达 681 亿美元，受 AI 需求推动上调下季度指引至 780 亿美元](https://t.me/zaihuapd/41498) ⭐️ 8.0/10

英伟达公布 2026 财年第四季度营收为 681 亿美元，超出市场预期，其中数据中心业务贡献了 623 亿美元。公司同时给出了 2027 财年第一季度 780 亿美元的强劲营收指引，显著超过分析师普遍预期的 726 亿美元。 这一业绩凸显了英伟达在 AI 硬件市场的主导地位，并反映了其 GPU 在驱动整个数据中心行业 AI 训练和推理工作负载方面需求的持续激增。上调的指引表明 AI 计算基础设施投资将继续呈指数级增长，影响着云服务提供商、企业及更广泛的半导体供应链。 关键细节包括每股收益（EPS）为 1.62 美元，同样超出预期，以及财报发布后盘后股价飙升超过 3%。然而，报告指出其游戏和汽车业务的营收未达预期。

telegram · zaihuapd · May 21, 05:10

**背景**: 英伟达设计和销售图形处理单元（GPU），这些 GPU 已成为训练和运行大型人工智能模型的基础硬件。公司的数据中心业务部门销售用于 AI 服务器的这些 GPU 和网络解决方案，在云超大规模厂商和企业大举投资建设 AI 基础设施的推动下，该部门已成长为公司最大的收入来源。

**标签**: `#AI hardware`, `#semiconductor industry`, `#financial results`, `#data center`

---

<a id="item-17"></a>
## [黄仁勋：英伟达已基本放弃中国 AI 芯片市场](https://www.cnbc.com/2026/05/21/nvidia-jensen-huang-china-ai-chip-market-huawei.html) ⭐️ 8.0/10

Nvidia CEO Jensen Huang stated the company has 'basically given up' on China's AI chip market due to U.S. export controls, ceding ground to Huawei and local competitors.

telegram · zaihuapd · May 21, 05:52

**标签**: `#AI hardware`, `#semiconductors`, `#geopolitics`, `#NVIDIA`, `#export controls`

---

<a id="item-18"></a>
## [OpenAI Codex 新增 Mac 锁屏后继续操控应用功能](https://x.com/OpenAIDevs/status/2057536706778378692) ⭐️ 8.0/10

OpenAI 为 Codex 的“计算机使用”能力新增了“锁屏使用”功能，允许该人工智能在 Mac 屏幕锁定或关闭时，继续操作已获批准的应用程序。用户可以从已连接的手机等设备进行控制。 此功能通过允许后台自动化和远程任务管理，无需 Mac 屏幕保持活动状态，显著增强了人工智能代理对开发者的实用性，可能简化长时间运行的编码或操作任务。这代表了直接集成到操作系统中的实用、持久型人工智能助手向前迈出了一步。 该功能目前仅适用于 macOS 系统，并且首发时存在地域限制，不包括欧洲经济区、英国和瑞士。使用前必须安装插件，并授予屏幕录制和辅助功能权限；用于控制的临时解锁仅在当前任务期间有效，一旦检测到本地输入操作，屏幕将重新锁定。

telegram · zaihuapd · May 22, 00:58

**背景**: Codex 是 OpenAI 推出的一款由人工智能驱动的编码代理，旨在通过理解并在集成开发环境及操作系统中执行命令来辅助开发者。“计算机使用”能力允许人工智能模型在视觉上感知并与计算机的图形用户界面进行交互，这是构建自主人工智能代理的一个基本方面。在 macOS 上授予屏幕录制和辅助功能权限是任何软件（包括远程控制和人工智能代理工具）合法与桌面环境交互和控制的标准要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Ylianst/MeshCentral/issues/4824">Screen Recording access permission does not work with MacOS Agent · Issue #4824 · Ylianst/MeshCentral - GitHub</a></li>
<li><a href="https://jumpcloud.com/support/grant-screen-recording-and-accessibility-permissions-for-remote-assist-agent-on-macos-devices">Grant Required Permissions for the Remote Assist Agent on macOS Devices - JumpCloud</a></li>

</ul>
</details>

**标签**: `#AI_agents`, `#OpenAI_Codex`, `#productivity`, `#macOS`, `#remote_control`

---