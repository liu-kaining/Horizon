---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 216 items, 13 important content pieces were selected

---

1. [vLLM v0.21.0 发布，包含重大构建变更和高级功能](#item-1) ⭐️ 9.0/10
2. [首个公开的 macOS 内核内存破坏漏洞利用瞄准苹果 M5 硬件](#item-2) ⭐️ 9.0/10
3. [严重 Linux 页面缓存漏洞影响所有主流发行版](#item-3) ⭐️ 9.0/10
4. [PostgreSQL 发布多个版本安全更新，修复 11 个 CVE 漏洞](#item-4) ⭐️ 9.0/10
5. [关键 Linux 零日漏洞允许非特权用户读取根用户文件](#item-5) ⭐️ 9.0/10
6. [支付宝账户关闭支付功能后被扣 184 万元，官方称不排除违法犯罪](#item-6) ⭐️ 8.0/10
7. [研究人员利用 Anthropic Claude Mythos AI 模型发现并利用 macOS 提权漏洞](#item-7) ⭐️ 8.0/10
8. [TanStack 供应链攻击波及 OpenAI，官方敦促 Mac 用户更新 ChatGPT 应用](#item-8) ⭐️ 8.0/10
9. [谷歌 DORA 团队发布新报告：扎实的工程基础决定 AI 投资回报](#item-9) ⭐️ 8.0/10
10. [(分享发现) Deekseek 疑似爆出一个 bug！可能是 P0 级的顶级安全事故](#item-10) ⭐️ 8.0/10
11. [OpenAI Codex 移动版预览已登陆 ChatGPT 应用](#item-11) ⭐️ 8.0/10
12. [Abridge AI 处理量达 1 亿次就诊，每周为临床医生节省 10-20 小时](#item-12) ⭐️ 8.0/10
13. [Anthropic 限制 Mythos AI 模型因其超强漏洞检测能力](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 发布，包含重大构建变更和高级功能](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 9.0/10

vLLM v0.21.0 引入了强制性的 C++20 构建要求，并正式弃用了对 Transformers v4 的支持，要求用户迁移到 v5。本次发布增加了多项高级功能，包括与混合内存分配器（HMA）集成的 KV 缓存卸载、遵守思维/推理预算的推测解码，以及面向 NVIDIA Blackwell GPU 上特定模型的新 TOKENSPEED_MLA 注意力后端。 作为广泛使用的高性能大语言模型推理引擎，vLLM 采用 C++20 标准使其与 PyTorch 等现代工具链保持一致，这对于长期维护和兼容性至关重要。新增的集成 HMA 的 KV 缓存卸载和预算感知推测解码等功能，直接解决了扩展和加速大模型推理的核心挑战，有望降低服务大型模型时的延迟和内存占用。 C++20 要求是一项破坏性变更，从源代码构建的用户需要升级编译器。KV 缓存卸载子系统现在支持调度器侧的滑动窗口分组，并通过 MooncakeStoreConnector 等连接器启用了分布式 KV 缓存卸载。

github · khluu · May 14, 23:15

**背景**: vLLM 是一个用于大语言模型（LLM）的高吞吐量、高内存效率的推理和部署引擎。KV 缓存是 LLM 推理中的一项基本优化，它存储中间的键值状态以避免重复计算。推测解码是一种使用更小、更快的“草稿”模型生成候选 token，然后由主模型进行验证以加速生成的技术。混合内存分配器（HMA）是一种内存管理系统，旨在高效利用高带宽（GPU）内存和主（CPU）内存来执行诸如 KV 缓存卸载之类的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/issues/22605">[RFC]: Separated CPU KV Cache Offloading/Transfer Process · Issue #22605 · vllm-project/vllm</a></li>
<li><a href="https://arxiv.org/html/2504.14893v1">Hardware-based Heterogeneous Memory Management for Large Language Model Inference</a></li>
<li><a href="https://deepwiki.com/vllm-project/vllm/8-attention-backends">Attention Backends | vllm-project/vllm | DeepWiki</a></li>

</ul>
</details>

**标签**: `#LLM-inference`, `#model-serving`, `#GPU-optimization`, `#open-source`, `#AI-infra`

---

<a id="item-2"></a>
## [首个公开的 macOS 内核内存破坏漏洞利用瞄准苹果 M5 硬件](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Calif 团队在 AI 系统 Mythos Preview 的协助下，仅用五天时间就开发并公布了首个针对苹果 M5 芯片 macOS 的公开内核内存破坏漏洞利用，该利用绕过了 MIE 硬件保护，并实现了从非特权用户到 root shell 的本地提权。 该漏洞利用意义重大，因为它表明苹果耗时五年打造的 MIE 硬件防御可以被绕过，这凸显了一种潜在的范式转变：即人工智能辅助的协作能够快速突破顶级安全措施，并为网络安全生态系统提出了紧迫的问题。 该攻击链涉及两个不同的漏洞和多项技术，仅利用标准系统调用就在 macOS 26.4.1 中实现了数据型本地内核提权，其完整的技术报告（55 页）将在苹果发布补丁后公开。

hackernews · Lobsters · May 14, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48139219)

**背景**: 苹果的 MIE 是一项基于硬件的安全功能，在 M5 芯片上引入，它利用标记内存来防御缓冲区溢出和内存破坏攻击，这项技术基于 ARM 的内存标记扩展（MTE）。苹果 M5 芯片是苹果为 Mac、iPad 和 Vision Pro 定制的最新一代芯片，其统一内存架构旨在提升设备端的 AI 性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/">Apple unleashes M 5 , the next big leap in AI performance for... - Apple</a></li>
<li><a href="https://8ksec.io/mie-deep-dive-kernel/">Memory Integrity Enforcement (MIE) on iOS Deep Dive</a></li>

</ul>
</details>

**社区讨论**: 社区的反应参杂着不安情绪；一些用户对提供的技术细节表示怀疑，另一些用户则强调了潜在的漏洞赏金，根据提交方式的不同，赏金可能在 10 万到 150 万美元之间。一个反复出现的观点是世界尚未准备好应对 LLM 对安全的影响，还有一位用户幽默地评论说，自己当初特意为 MIE 保护购买 M5，现在感觉很愚蠢。

**标签**: `#macOS security`, `#kernel exploit`, `#M5 chip`, `#AI-assisted research`, `#vulnerability research`

---

<a id="item-3"></a>
## [严重 Linux 页面缓存漏洞影响所有主流发行版](https://www.infoq.cn/article/1HucCJrazwgF7QNT232r?utm_source=rss&utm_medium=article) ⭐️ 9.0/10

安全研究人员披露了两个严重的 Linux 内核漏洞，Copy Fail（CVE-2026-31431）和 DirtyFrag，这些漏洞利用页面缓存逻辑缺陷，允许无特权的本地用户在受影响系统上获得 root 权限。 这些漏洞影响所有主流 Linux 发行版，为攻击者提供了强大的提权原语，对服务器、工作站和云基础设施构成重大且即时的安全风险。 Copy Fail 是加密模板中的一个逻辑缺陷，它链接 AF_ALG 和 splice()来实现对页面缓存的受控 4 字节写入，而 DirtyFrag 则涉及用于 IPsec 操作的 xfrm-ESP 等模块中的漏洞。

rss · InfoQ 中文站 · May 15, 09:37

**背景**: Linux 页面缓存是一个关键的内存管理组件，它存储从磁盘频繁访问的数据副本以加速系统性能。对这个缓存的写入原语可以让攻击者修改可执行文件或敏感的系统数据。AF_ALG 接口是基于内核的加密 API，而 splice()是一个用于在文件描述符之间移动数据而不复制到用户空间的系统调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xint.io/blog/copy-fail-linux-distributions">Copy Fail : 732 Bytes to Root on Every Major Linux Distribution. - Xint</a></li>
<li><a href="https://www.elastic.co/security-labs/copy-fail-dirtyfrag-linux-page-bugs-in-the-wild">Copy Fail and DirtyFrag: Linux Page Cache ... — Elastic Security Labs</a></li>
<li><a href="https://arstechnica.com/security/2026/05/linux-bitten-by-second-severe-vulnerability-in-as-many-weeks/">Linux bitten by second severe vulnerability in as many... - Ars Technica</a></li>

</ul>
</details>

**标签**: `#Linux`, `#Security`, `#Kernel`, `#Vulnerability`, `#Systems`

---

<a id="item-4"></a>
## [PostgreSQL 发布多个版本安全更新，修复 11 个 CVE 漏洞](https://www.postgresql.org/about/news/postgresql-184-1710-1614-1518-and-1423-released-3297/) ⭐️ 9.0/10

PostgreSQL 全球开发小组发布了 18.4、17.10、16.14、15.18 和 14.23 版本的安全更新，以修复 11 个安全漏洞，即公共漏洞和暴露（CVE）。 此次发布对数据库管理员和安全团队至关重要，因为它修补了世界上最流行的开源关系型数据库系统之一的重大漏洞，有助于防止潜在的数据泄露或系统受损。 更新覆盖了五个主要的 PostgreSQL 发布分支（18、17、16、15 和 14），确保使用较旧但仍受支持版本的用户也能获得必要的安全修复。这 11 个 CVE 的具体技术性质和严重程度在初始摘要中未详细说明，但此类发布对于生产环境通常很紧急。

rss · Lobsters · May 14, 19:43

**背景**: PostgreSQL 是一个强大的、开源的对象关系型数据库系统，以其可靠性、功能健全性和性能而享有盛誉。CVE 是公开已知网络安全漏洞的标准化标识符，定期安全更新是软件维护中保护用户的标准做法。建议数据库管理员及时应用这些更新以降低风险。

**社区讨论**: 链接到的 Lobste.rs 讨论显示了很高的社区参与度，有 43 条评论和 96 个点赞，表明社区对这个广泛使用的数据库系统的安全非常关注。评论很可能涉及对具体漏洞、升级流程以及在生产环境中及时打补丁重要性的讨论。

**标签**: `#databases`, `#security`, `#postgresql`, `#CVEs`, `#releases`

---

<a id="item-5"></a>
## [关键 Linux 零日漏洞允许非特权用户读取根用户文件](https://github.com/0xdeadbeefnetwork/ssh-keysign-pwn/) ⭐️ 9.0/10

一个零日漏洞被披露，该漏洞允许非特权 Linux 用户访问根用户拥有的文件，很可能是由于 ssh-keysign 二进制文件中的缺陷所致。 这是一个严重的安全问题，因为它实现了本地权限提升，允许任何普通用户绕过文件权限并可能读取敏感系统文件，从而可能导致整个系统被入侵。 该漏洞涉及 ssh-keysign 二进制文件，它通常作为 SUID 程序安装，这意味着它以提升的权限运行，其中的任何缺陷都可能被利用来获得更高访问权限。

rss · Lobsters · May 15, 01:14

**背景**: SSH（安全外壳）是一种用于安全远程登录和其他网络服务的加密网络协议。ssh-keysign 是 SSH 客户端用于基于主机的身份验证的辅助程序；它通常作为 SUID 二进制文件安装，以允许其读取系统主机密钥，如果实现不当，这是常见的安全漏洞来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://steflan-security.com/linux-privilege-escalation-exploiting-misconfigured-ssh-keys/">Linux Privilege Escalation - Exploiting Misconfigured SSH Keys - Steflan's Security Blog</a></li>
<li><a href="https://www.halfdog.net/Security/2017/SshAgentGainGroupPrivileges/">Gain Access to SSH Group via ssh-agent and OpenSSL</a></li>

</ul>
</details>

**社区讨论**: Lobsters 上的相关讨论表明社区对该漏洞的严重性进行了大量参与和验证，确认这是一个真实且关键的零日问题。

**标签**: `#security`, `#linux`, `#zero-day`, `#vulnerability`, `#privilege-escalation`

---

<a id="item-6"></a>
## [支付宝账户关闭支付功能后被扣 184 万元，官方称不排除违法犯罪](https://www.ithome.com/0/950/711.htm) ⭐️ 8.0/10

一位用户在联系支付宝客服关闭支付功能后，其账户仍被用于向多家公益机构捐赠了近 184.7 万元。中国人民银行上海分行的调查发现，支付宝系统存在一个漏洞，即在支付功能关闭后，公益捐赠场景仍可进行付款。 这起事件揭示了中国最大数字支付平台之一存在严重的安全和设计缺陷，损害了用户信任，并暴露了数字金融服务在监管层面可能存在的漏洞。它凸显了平台特定的技术决策如何可能违背用户意愿，从而导致严重的财务后果。 中国人民银行确认该账户的支付功能一直处于关闭状态，但支付宝的设计允许公益捐赠通过电脑密码验证以及手机短信/生物识别验证绕过此限制。支付宝表示怀疑该账户存在共用情况，正在向警方寻求帮助；而接收捐赠的慈善基金会则表示，若能收到官方证明捐赠非自愿的材料，愿意核实是否符合退款条件。

rss · IT HOME · May 15, 02:00

**背景**: 支付宝是蚂蚁集团运营的主要移动和在线支付平台，在中国拥有超过十亿用户。在数字支付系统中，用户通常可以禁用转账和消费等核心支付功能以保障安全。慈善捐赠平台通常与支付宝等支付系统集成，以促进社会公益捐赠，这些捐赠一旦执行通常不可撤销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ifeng.com/c/8t7lhDoqRzV">女子称关闭 支 付 功 能 后，180多万元凌晨莫名通过 支 付 宝 捐 给慈善 机 构</a></li>
<li><a href="https://fgw.sh.gov.cn/ys-hqjrfw-1.3.3.2/index.html">责任披露、数据使用和争议机制_上海市发展和改革委员会</a></li>
<li><a href="https://www.workercn.cn/c/2025-12-10/8680864.shtml">中 国 乡 村 发 展 基 金 会 ：童伴妈妈 项 目 累计服务儿童近90...</a></li>

</ul>
</details>

**标签**: `#Alipay`, `#security`, `#financial-fraud`, `#regulation`, `#digital-payments`

---

<a id="item-7"></a>
## [研究人员利用 Anthropic Claude Mythos AI 模型发现并利用 macOS 提权漏洞](https://www.ithome.com/0/950/676.htm) ⭐️ 8.0/10

来自 Calif 的安全研究人员使用 Anthropic 最强的 AI 模型 Claude Mythos，发现了 macOS 26.4.1 中的两个漏洞，并将其链接利用，在 Apple M5 硬件上成功实现了本地提权，获得了 root shell。 这是首个在 Apple M5 芯片上公开记录的、绕过了苹果硬件强制执行的内存完整性强制保护 (MIE) 的内核内存损坏利用，展示了先进人工智能如何显著加速针对加固系统复杂网络攻击的发现和执行，开辟了新的范式。 攻击链从一个无特权的本地账户开始，结合了两个不同的漏洞和多种利用技术，由人类研究人员与 AI 模型协作大约五天开发完成；具体的漏洞细节因苹果公司仍在审查而未公开。

rss · IT HOME · May 15, 00:14

**背景**: Claude Mythos 是 Anthropic 公司最新、最强大的大语言模型，定位为与 GPT-4 和 Gemini 等模型竞争的产品。内存完整性强制保护 (MIE) 是苹果为其 Apple Silicon 芯片引入的一项重大安全功能，利用硬件能力来强制执行内存安全，使某些类型的利用变得更加困难。本地提权 (LPE) 漏洞允许攻击者在拥有设备基本用户访问权限的情况下，获得更高的、通常是 root 级别的权限，从而完全控制系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model ) - Wikipedia</a></li>
<li><a href="https://8ksec.io/mie-deep-dive-kernel/">iOS Memory Integrity Enforcement Deep Dive | 8kSec</a></li>
<li><a href="https://cybersnowden.com/local-privilege-escalation-lpe-exploits-detection-defense/">Local Privilege Escalation (LPE) Exploits — Detection & Defense - Cyber ...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#AI`, `#macOS`, `#privilege-escalation`

---

<a id="item-8"></a>
## [TanStack 供应链攻击波及 OpenAI，官方敦促 Mac 用户更新 ChatGPT 应用](https://www.ithome.com/0/950/666.htm) ⭐️ 8.0/10

OpenAI 要求所有 Mac 版 ChatGPT 桌面应用用户在 2025 年 6 月 12 日前完成强制更新，原因是针对开源库 TanStack 的供应链攻击导致其内部代码签名证书泄露。 此事件凸显了开源生态系统中供应链攻击的级联风险，一个流行库的漏洞可能直接影响大型 AI 公司，并迫使最终用户采取紧急安全措施。 此次与“Mini Shai-Hulud”活动相关的攻击仅波及两名 OpenAI 员工的设备，影响范围限于内部代码仓库和凭证材料；据报道，用户数据和 OpenAI 的核心系统未受影响。

rss · IT HOME · May 14, 23:30

**背景**: TanStack 是一个流行的开源 Web 开发库集合，其中包含用于数据获取的 TanStack Query。“Mini Shai-Hulud”是一种已知的供应链恶意软件，通过劫持 CI/CD 流水线和伪造数字签名来入侵软件包。代码签名证书由开发者用于对应用程序进行数字签名，以确保其真实性和完整性；其泄露可使攻击者使用受信任的密钥签署恶意软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberscoop.com/mini-shai-hulud-supply-chain-malware-attack/">‘Mini Shai-Hulud’ malware compromises hundreds of open-source packages in sprawling supply-chain attack | CyberScoop</a></li>
<li><a href="https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem">TeamPCP's Mini Shai-Hulud Is Back: A Self-Spreading Supply Chain Attack Compromises TanStack npm Packages - StepSecurity</a></li>

</ul>
</details>

**标签**: `#security`, `#supply chain attack`, `#OpenAI`, `#macOS`, `#vulnerability`

---

<a id="item-9"></a>
## [谷歌 DORA 团队发布新报告：扎实的工程基础决定 AI 投资回报](https://www.infoq.cn/article/IgGuKFh9qmKmFEIZeR4t?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

谷歌的 DevOps 研究与评估（DORA）团队发布了一份新报告，强调了扎实的工程基础对于实现 AI 投资回报至关重要。 该报告意义重大，因为它为投资 AI 的组织提供了实用见解，强调了基础工程实践直接影响 AI 计划的成功和投资回报。 该报告很可能借鉴了 DORA 团队已确立的软件交付绩效指标，这些指标能够预测组织成效，并将其与 AI 部署的有效性联系起来。

rss · InfoQ 中文站 · May 14, 09:23

**背景**: DORA 是谷歌云内部的一个研究 DevOps 实践的研究团队。它以识别部署频率、变更准备时间等衡量软件交付绩效的关键指标而闻名。DORA 每年发布的《DevOps 状态报告》在软件工程界具有重要影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DORA_Metrics">DORA Metrics</a></li>
<li><a href="https://dora.dev/guides/dora-metrics/">DORA | DORA's software delivery performance metrics</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#DORA metrics`, `#engineering practices`, `#ROI`

---

<a id="item-10"></a>
## [(分享发现) Deekseek 疑似爆出一个 bug！可能是 P0 级的顶级安全事故](https://www.v2ex.com/t/1212886#reply8) ⭐️ 8.0/10

A user reports a possible critical bug in DeepSeek's platform where typing a specific command could expose other users' historical conversation data.

rss · V2EX · May 15, 02:23

**标签**: `#security-vulnerability`, `#AI-safety`, `#data-leakage`, `#DeepSeek`, `#bug-report`

---

<a id="item-11"></a>
## [OpenAI Codex 移动版预览已登陆 ChatGPT 应用](https://www.v2ex.com/t/1212885#reply1) ⭐️ 8.0/10

OpenAI 已将 Codex 编程助手的移动预览版集成到 ChatGPT 的 iOS 和 Android 应用中，现面向所有用户开放，包括免费和 Go 档位套餐。这允许开发者通过手机远程连接到他们的笔记本电脑、Mac mini 或云端开发环境，从而监控代理状态、批准指令并查看代码差异和测试输出。 此举将编程助手从桌面工具转变为真正的移动协作者，使开发者能够随时随地审查和批准 AI 驱动的工作，这可能显著提高软件开发工作流程的生产力和灵活性。 该移动预览版允许实时监控代理线程和批准任务，专为长时间运行的代理编程工作设计，使开发者现在可以远程保持在线。此功能对所有 ChatGPT 用户开放，涵盖所有订阅档位，将 Codex 的可访问性扩展到了付费计划之外。

rss · V2EX · May 15, 02:23

**背景**: OpenAI Codex 是一个由 ChatGPT 驱动的云端 AI 编程代理，可以自主执行软件开发任务，如编写代码、调试和使用云环境并行运行测试。远程开发涉及从一台设备（如手机）连接到另一个环境（如笔记本电脑或云服务器）进行代码工作，这是 VS Code 和 JetBrains IDE 等工具支持的做法。所描述的代理工作流强调自主、长时间运行的任务，AI 代理独立工作，而人类开发者则远程监督和批准更改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/work-with-codex-from-anywhere/">Work with Codex from anywhere | OpenAI</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://developers.openai.com/codex">Codex | OpenAI Developers</a></li>

</ul>
</details>

**社区讨论**: 提供的内容不包含社区评论，因此没有讨论可以总结。

**标签**: `#OpenAI`, `#Codex`, `#Mobile Development`, `#Remote Development`, `#ChatGPT`

---

<a id="item-12"></a>
## [Abridge AI 处理量达 1 亿次就诊，每周为临床医生节省 10-20 小时](https://www.latent.space/p/abridge) ⭐️ 8.0/10

Abridge 正在扩展其人工智能平台，以处理 1 亿次医生就诊，通过自动化预先授权和临床文档记录，预计每周可为临床医生节省 10 至 20 小时。 这表明生成式人工智能在医疗保健领域进行了一次重大且实用的部署，通过大规模自动化高容量的行政任务，直接缓解临床医生的职业倦怠，并提升了运营效率。 该平台利用生成式人工智能将患者与临床医生的实时对话转换为临床笔记，并优化了预先授权流程，这是医疗保健领域众所周知的耗时行政障碍。

rss · Latent Space · May 14, 22:05

**背景**: 预先授权是健康保险公司要求临床医生在提供特定服务或药物前获得批准的程序，该流程以延误和行政负担著称。临床文档自动化使用人工智能，特别是大语言模型（LLMs），从对话中生成准确的医疗记录，旨在减少导致临床医生职业倦怠的文书工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.abridge.com/">Generative AI for Clinical Conversations | Abridge</a></li>
<li><a href="https://tossom.com/products/abridge-ai">Abridge AI - Generative AI for Clinical Documentation... | Tossom</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11105142/">Efficient healthcare with large language models: optimizing clinical ...</a></li>

</ul>
</details>

**标签**: `#AI in Healthcare`, `#Large Language Models`, `#Clinical Automation`, `#Startup Case Study`

---

<a id="item-13"></a>
## [Anthropic 限制 Mythos AI 模型因其超强漏洞检测能力](https://www.schneier.com/blog/archives/2026/05/how-dangerous-is-anthropics-mythos-ai.html) ⭐️ 8.0/10

Anthropic 宣布其新的 Claude Mythos Preview 模型在发现软件漏洞方面表现极其出色，因此公司不会将其向公众发布，而是限制为一个特定公司群体提供访问，用于扫描他们自己的软件。 这一决定凸显了在利用强大 AI 能力获得安全优势与负责任部署以防止滥用之间日益增长的紧张关系，为如何控制强大 AI 模型树立了先例。 该公告指出，虽然 Anthropic 的模型能力超群，但其他模型如 OpenAI 的 GPT-5.5，经英国 AI 安全研究所评估，在发现漏洞的能力上也表现出相当水平。

rss · Schneier on Security · May 14, 11:04

**背景**: AI 模型越来越多地被用于网络安全应用测试，例如在软件漏洞被利用前自动检测它们。公司和研究所正在评估这些模型以了解其潜在风险和收益，引发了关于安全受控访问的讨论。

**标签**: `#AI safety`, `#cybersecurity`, `#responsible AI`, `#software vulnerabilities`, `#anthropic`

---