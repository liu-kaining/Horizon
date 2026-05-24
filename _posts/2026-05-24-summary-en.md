---
layout: default
title: "Horizon Summary: 2026-05-24 (EN)"
date: 2026-05-24
lang: en
---

> From 175 items, 7 important content pieces were selected

---

1. [Anthropic's Project Glasswing Finds 10,000+ Critical Software Vulnerabilities with AI](#item-1) ⭐️ 9.0/10
2. [Apple open-sources corecrypto with formal proofs for post-quantum algorithms](#item-2) ⭐️ 9.0/10
3. [Microsoft's Q2 report reveals OpenAI's $11.5 billion quarterly net loss](#item-3) ⭐️ 9.0/10
4. [Anthropic Finalizing Over $30B Funding, Potentially Surpassing OpenAI's Valuation](#item-4) ⭐️ 8.0/10
5. [OpenAI Details WebRTC Architecture for Scalable Low-Latency Voice AI](#item-5) ⭐️ 8.0/10
6. [z386: An Open-Source 80386 CPU Using Original Intel Microcode](#item-6) ⭐️ 8.0/10
7. [Microsoft Internally Promotes Anthropic's Claude Code Across Core Teams](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic's Project Glasswing Finds 10,000+ Critical Software Vulnerabilities with AI](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic announced that its Project Glasswing initiative, using the Claude Mythos Preview AI model, discovered over 10,000 critical vulnerabilities in software across approximately 50 partner organizations within a single month. This represents a paradigm shift in software security, as AI-powered vulnerability discovery at this scale and speed overwhelms current human capacity for verification, disclosure, and patching, forcing the entire industry to adapt its remediation processes. In a scan of over a thousand open-source projects, 6,202 high-severity vulnerabilities were found, with 90.6% of a reviewed subset (1,752) being true positives; partners like Cloudflare reported vulnerability discovery rates increased by more than tenfold.

telegram · zaihuapd · May 23, 03:16

**Background**: Project Glasswing is a collaborative security initiative by Anthropic designed to secure critical software using advanced AI. Claude Mythos Preview is Anthropic's most capable frontier model to date, representing a significant leap in performance benchmarks. The discovery highlights a growing industry challenge: while AI can find vulnerabilities faster than humans, the manual processes for verifying, disclosing, and patching them lag severely behind.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf">Claude Mythos Preview System Card - www-cdn.anthropic.com</a></li>
<li><a href="https://claude.com/product/claude-security">Claude Security | Claude by Anthropic</a></li>

</ul>
</details>

**Discussion**: The discussion likely centers on the significant implications for software security and the open-source ecosystem. A key concern is the overwhelming pressure this places on maintainers, with reports indicating that some open-source developers have already requested a slowdown in vulnerability reporting due to the inability to keep up with patching.

**Tags**: `#AI Security`, `#Vulnerability Discovery`, `#Large Language Models`, `#Open Source`, `#Anthropic`

---

<a id="item-2"></a>
## [Apple open-sources corecrypto with formal proofs for post-quantum algorithms](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

Apple has released the source code for its corecrypto cryptographic library, which includes implementations of the NIST-standardized ML-KEM and ML-DSA post-quantum algorithms, accompanied by formal verification mathematical proofs to ensure their correctness. This move provides critical transparency and verifiable security for the foundational cryptographic library used across billions of Apple devices, setting a new industry standard for implementing and verifying quantum-resistant cryptography. The formal proofs, created using the Isabelle proof assistant, verify that the C code and hand-optimized ARM64 assembly precisely match the NIST specifications. Apple also released the custom verification tools and Isabelle theory libraries to enable independent expert evaluation.

telegram · zaihuapd · May 23, 04:49

**Background**: Post-quantum cryptography (PQC) refers to cryptographic algorithms designed to be secure against attacks from future quantum computers. ML-KEM (Kyber) and ML-DSA (Dilithium) are the first standards finalized by NIST in 2024 for key encapsulation and digital signatures, respectively. Formal verification is a technique that uses mathematical proofs to guarantee that a system's implementation matches its specification exactly, eliminating certain classes of bugs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kyber">ML - KEM - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_(proof_assistant)">Isabelle ( proof assistant ) - Wikipedia</a></li>
<li><a href="https://www.macrumors.com/2015/10/30/apple-opens-cryptographic-libraries/">Apple Opens Cryptographic Libraries to Third-Party Developers to Encourage Security - MacRumors</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#post-quantum`, `#open-source`, `#formal-verification`, `#security`

---

<a id="item-3"></a>
## [Microsoft's Q2 report reveals OpenAI's $11.5 billion quarterly net loss](https://t.me/zaihuapd/41537) ⭐️ 9.0/10

Microsoft's latest quarterly financial report, using the equity method for its investment, disclosed that its share of OpenAI's net loss reduced Microsoft's own net income by $3.1 billion. Based on Microsoft's approximate 27% stake, this implies OpenAI incurred a net loss of roughly $11.5 billion for that quarter. This disclosure reveals an unprecedented and unsustainable financial burn rate for a leading AI company, highlighting the massive capital intensity and significant financial risks currently present in the artificial intelligence industry. It underscores the challenge of monetizing cutting-edge AI development in the short term. The calculated loss is based on Microsoft's reported equity pick-up and its stated ownership percentage (approx. 27%); calculations using a pre-tax loss and a slightly higher reported stake (32.5%) suggest the actual loss could exceed $12 billion. This quarterly loss is nearly three times OpenAI's reported first-half 2024 revenue of $4.3 billion.

telegram · zaihuapd · May 23, 07:40

**Background**: The equity method is an accounting treatment where an investor recognizes its share of the profits or losses of an investee company in its own income statement, typically used when the investor has significant influence (usually 20-50% ownership). OpenAI is a leading artificial intelligence research lab responsible for developing the GPT series of large language models. Microsoft is a major strategic and financial investor in OpenAI, having committed billions in capital and integrated OpenAI's technology into its products.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/权益法/9289851">权益法_百度百科 采用权益法核算的长期股权投资账务处理流程（附案例详解） 一文搞懂长期股权投资的核算方法：成本法、权益法和合并法 在阅读||#20998;... 权益法核算的长期股权投资收益_东奥会计在线 【老丁解税】权益法下投资收益的所得税处理解析 长期股权投资权益法 (长期股权投资核算方法) - 会计百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/496165358">长期股权投资——权益法（干货总结） - 知乎</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Finance`, `#OpenAI`, `#Microsoft`, `#Business`

---

<a id="item-4"></a>
## [Anthropic Finalizing Over $30B Funding, Potentially Surpassing OpenAI's Valuation](https://www.ithome.com/0/954/452.htm) ⭐️ 8.0/10

Anthropic is reportedly finalizing a massive new funding round exceeding $300 billion, which could be completed as early as next week, potentially raising its valuation to over $900 billion. This deal would make Anthropic the world's most valuable AI startup, surpassing OpenAI, and signals intense investor confidence in Anthropic's technology and growth trajectory within the competitive AI sector. The funding round, which saw strong demand, exceeded Anthropic's initial $300 billion target and was finalized in a matter of weeks; the company also reports rapid revenue growth, with annualized revenue projected to surpass $500 billion by next month.

rss · IT HOME · May 23, 15:12

**Background**: Anthropic and OpenAI are leading artificial intelligence research companies developing large language models, a type of generative AI that can understand and produce human-like text. Valuation refers to the estimated worth of a private company determined by investors during a funding round, while annualized revenue projects a company's total revenue for a year based on its recent performance.

**Tags**: `#AI funding`, `#Anthropic`, `#valuation`, `#industry news`, `#OpenAI`

---

<a id="item-5"></a>
## [OpenAI Details WebRTC Architecture for Scalable Low-Latency Voice AI](https://www.infoq.cn/article/HzTpYj4SIqzFOHybIO2q?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

OpenAI has detailed a novel WebRTC architecture that replaces a conventional media termination model with a relay-transceiver design to support low-latency voice AI at a global scale. This architectural shift is significant because it enables a major AI platform to handle voice AI applications with the low latency and massive scale required for services like ChatGPT voice, setting a new standard for real-time conversational systems. The architecture employs an SFU-less (Selective Forwarding Unit-less) design, which simplifies scaling by allowing inference services to avoid behaving as WebRTC peers, and it preserves standard WebRTC behavior for clients.

rss · InfoQ 中文站 · May 23, 14:00

**Background**: WebRTC is an open-source framework enabling real-time voice, video, and data communication directly between browsers and applications. Low-latency voice AI refers to systems that can understand and respond to human speech in near real-time, which is crucial for natural conversational interfaces. Scaling such systems globally presents significant challenges in maintaining consistent, fast performance for millions of users.

<details><summary>References</summary>
<ul>
<li><a href="https://www.infoq.com/news/2026/05/openai-voice-ai-scale/">OpenAI Outlines WebRTC Architecture for Low-Latency Voice AI ...</a></li>
<li><a href="https://openai.com/index/delivering-low-latency-voice-ai-at-scale/">How OpenAI delivers low-latency voice AI at scale | OpenAI</a></li>
<li><a href="https://quantumzeitgeist.com/low-latency-voice-ai-openais-steps/">OpenAI’s 4 Steps to Low-Latency Voice AI at Global Scale</a></li>

</ul>
</details>

**Tags**: `#AI`, `#WebRTC`, `#System Architecture`, `#Voice AI`, `#Real-Time Systems`

---

<a id="item-6"></a>
## [z386: An Open-Source 80386 CPU Using Original Intel Microcode](https://nand2mario.github.io/posts/2026/z386/) ⭐️ 8.0/10

The z386 project has successfully created a fully open-source, FPGA-based implementation of the Intel 80386 CPU by reconstructing it around the processor's recovered original microcode. This work provides a unique and preserved hardware reference for the x86 architecture's historical microcode, enabling deeper study, education, and faithful hardware preservation for retro-computing enthusiasts and engineers. The implementation is built on the z8086 project's foundation and incorporates extensive reverse-engineering work by multiple researchers, successfully running DOS and protected-mode applications including the classic game Doom.

rss · Lobsters · May 23, 15:24

**Background**: Microcode is a low-level layer of instructions within a CPU that implements the higher-level machine code instructions seen by software. The Intel 80386 was a pivotal 32-bit processor that defined the modern x86 architecture. Reverse-engineering such microcode from historical chips is an extremely complex task that allows researchers to understand the exact hardware-level implementation of the processor's instruction set.

<details><summary>References</summary>
<ul>
<li><a href="https://nand2mario.github.io/posts/2026/z386/">z386: An Open-Source 80386 Built Around Original Microcode - Small Things Retro</a></li>
<li><a href="https://bestcadpapers.com/comparisons-differences/z386-an-open-source-80386-built-around-original-microcode/">z386: An Open-Source 80386 Built Around Original Microcode - Best CAD papers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microcode">Microcode - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The project has generated significant interest in technical communities like Lobsters, with discussions focusing on the remarkable technical achievement of the reverse engineering and the value of such projects for preserving computing history.

**Tags**: `#retro-computing`, `#CPU-design`, `#open-source-hardware`, `#reverse-engineering`, `#x86`

---

<a id="item-7"></a>
## [Microsoft Internally Promotes Anthropic's Claude Code Across Core Teams](https://t.me/zaihuapd/41535) ⭐️ 8.0/10

Microsoft is requiring its core engineering teams, including those working on Windows and Microsoft 365, to install and use Anthropic's Claude Code alongside GitHub Copilot, and is encouraging non-technical employees to use it for prototyping. This move signals a significant strategic shift where a tech giant is openly adopting and promoting a direct competitor's AI tool internally, highlighting the intensifying competition in the AI-powered developer tools market and suggesting a pragmatic, multi-vendor approach to AI adoption. The internal promotion requires engineers to use Claude Code and GitHub Copilot side-by-side and provide comparative feedback, indicating Microsoft is actively benchmarking a competitor's offering against its own investment.

telegram · zaihuapd · May 23, 06:05

**Background**: Claude Code is an AI-powered coding assistant from Anthropic that operates directly in a developer's terminal or IDE, offering context-aware help with codebases and automation. GitHub Copilot is Microsoft's (via GitHub) widely-adopted AI pair programmer. Anthropic's models have recently gained significant enterprise traction, surpassing OpenAI in market share for large language models used by businesses.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://techcrunch.com/2025/07/31/enterprises-prefer-anthropics-ai-models-over-anyone-elses-including-openais/">Enterprises prefer Anthropic's AI models over anyone else's ...</a></li>
<li><a href="https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/">Introducing Anthropic's Claude models in Microsoft Foundry ...</a></li>

</ul>
</details>

**Tags**: `#AI coding`, `#enterprise adoption`, `#Microsoft`, `#developer tools`, `#AI competition`

---