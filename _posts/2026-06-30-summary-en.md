---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 202 items, 14 important content pieces were selected

---

1. [ChatGPT Reportedly Overturns Core Computational Geometry Problem](#item-1) ⭐️ 9.0/10
2. [Single Vulnerability (CVE-2026-6307) Bypasses Both Chrome Renderer and V8 Sandboxes](#item-2) ⭐️ 9.0/10
3. [Critical Linux kernel flaw CVE-2026-46215 grants unprivileged root access.](#item-3) ⭐️ 9.0/10
4. [vLLM v0.24.0 Released with Major Optimizations for MiniMax-M3 and DeepSeek-V4](#item-4) ⭐️ 8.0/10
5. [Rocket Lab Acquires Iridium in Major Satellite Industry Consolidation](#item-5) ⭐️ 8.0/10
6. [Study Finds Half of Social Media Child Safety Features Ineffective](#item-6) ⭐️ 8.0/10
7. [US Supreme Court Limits Geofence Warrants, Requiring Probable Cause for Cellphone Location Data](#item-7) ⭐️ 8.0/10
8. [AI Observability Expands to Monitor Model Reliability and Hallucinations](#item-8) ⭐️ 8.0/10
9. [AWS Launches Graviton5 with 192 Cores and Formally Verified VM Isolation](#item-9) ⭐️ 8.0/10
10. [Microsoft Introduces Memora, a Scalable Memory System for AI Agents](#item-10) ⭐️ 8.0/10
11. [JIT Compiler for Game Boy Translates to WebAssembly, Outperforms Native Interpreter](#item-11) ⭐️ 8.0/10
12. [New Linux Exploit Escapes Containers via IPv6 Fragment Bug](#item-12) ⭐️ 8.0/10
13. [New Research Reveals Vulnerable RSA Keys with Many Zeros in Wild](#item-13) ⭐️ 8.0/10
14. [Tesla's FSD v14 Lite brings HW4-level driving and parking to HW3 cars](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ChatGPT Reportedly Overturns Core Computational Geometry Problem](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652709773&idx=2&sn=68bde762eb0070f5bd61518728971232) ⭐️ 9.0/10

Building on OpenAI's recent solution to the Erdős conjecture, ChatGPT has reportedly overturned a long-standing core problem in computational geometry that researcher Chen Lijie from the Yao Class spent seven years studying, with the finding supported by over 30 institutions. This signifies a major paradigm shift in AI's capability for autonomous mathematical discovery, demonstrating that AI systems can not only assist but actively solve long-standing open problems in advanced mathematics, potentially accelerating progress across the field. The breakthrough builds directly on OpenAI's recent work disproving the Erdős unit distance conjecture, a problem in discrete geometry that had been open for about 78 years, which required the AI to produce a novel geometric construction not present in its training data.

rss · 新智元 · Jun 29, 05:01

**Background**: The Erdős conjectures refer to a large collection of unsolved mathematical problems proposed by prolific mathematician Paul Erdős. The specific one recently solved by OpenAI concerns the unit distance problem in discrete geometry. Computational geometry is a branch of computer science devoted to the study of algorithms which can be stated in terms of geometry. Chen Lijie is a renowned researcher affiliated with the Yao Class, a prestigious computer science program in China.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/openai-erdos-math-breakthrough-ai-reasoning">OpenAI Solved a 78-Year-Old Math Problem: What It Means for AI Reasoning | MindStudio</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_conjectures_by_Paul_Erdős">List of conjectures by Paul Erdős - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community discussion appears to highlight the credibility of the finding through the support of over 30 institutions and frames it as part of a broader trend where AI, like ChatGPT, is finding security vulnerabilities and making scientific discoveries, moving beyond being just a tool.

**Tags**: `#AI breakthrough`, `#computational geometry`, `#mathematical discovery`, `#OpenAI`, `#ChatGPT`

---

<a id="item-2"></a>
## [Single Vulnerability (CVE-2026-6307) Bypasses Both Chrome Renderer and V8 Sandboxes](https://nebusec.ai/research/v8-cve-2026-6307-writeup/) ⭐️ 9.0/10

Security researchers have demonstrated that CVE-2026-6307, a type confusion flaw in Chrome's Turbofan compiler, can be exploited with a single bug to escape both the renderer process sandbox and the V8 JavaScript engine's internal sandbox. This is significant because it represents a powerful 'two-in-one' exploit that defeats Chrome's primary layered defenses, potentially granting an attacker full system compromise from a simple web page, undermining the core security model of modern browsers. The vulnerability, tracked as CVE-2026-6307, is a high-severity (CVSS 8.8) type confusion issue in Turbofan that was patched in Chrome version 147.0.7727.101; the research highlights that a single memory corruption bug can bridge two separate security boundaries that were thought to be isolated.

rss · Lobsters · Jun 29, 15:00

**Background**: Chrome uses a multi-layered sandbox architecture where the renderer process (which handles web content) runs in a highly restricted OS sandbox, and the V8 JavaScript engine runs inside its own internal sandbox to contain memory corruption within its heap. The V8 sandbox is designed to prevent a bug in JavaScript code from being escalated to execute arbitrary code on the system. A type confusion vulnerability in the Turbofan optimizing compiler can cause memory to be treated as the wrong type, leading to memory corruption.

<details><summary>References</summary>
<ul>
<li><a href="https://v8.dev/blog/sandbox">The V8 Sandbox · V8</a></li>
<li><a href="https://chromium.googlesource.com/chromium/src/+/HEAD/docs/design/sandbox.md">Chromium Docs - Sandbox</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-6307">NVD - CVE - 2026 - 6307</a></li>

</ul>
</details>

**Discussion**: The discovery, featured on Lobsters, sparked significant community interest due to its groundbreaking nature, with discussions likely focusing on the sophistication of the exploit and its implications for browser security design.

**Tags**: `#security`, `#vulnerability`, `#browser`, `#v8`, `#chrome`

---

<a id="item-3"></a>
## [Critical Linux kernel flaw CVE-2026-46215 grants unprivileged root access.](https://cyberstan.co.uk/drm-lpe-linux/) ⭐️ 9.0/10

A critical use-after-free vulnerability (CVE-2026-46215) was discovered in the Linux kernel's DRM GEM subsystem's `drm_gem_change_handle_ioctl()` function, which allows any local user with access to a GPU render node to escalate their privileges to root. This vulnerability enables complete local privilege escalation on affected Linux systems, posing a severe risk to servers, workstations, and any device where untrusted users have shell access, as it bypasses all standard security controls to grant the highest system privileges. The flaw exists because the `drm_gem_change_handle_ioctl()` function moves a GEM object between handles but fails to adjust the object's internal `handle_count` reference, creating a use-after-free condition when the object is subsequently accessed or freed.

rss · Lobsters · Jun 29, 18:05

**Background**: DRM (Direct Rendering Manager) is a Linux kernel subsystem for managing GPU hardware and graphics memory. GEM (Graphics Execution Manager) is a memory manager within DRM used to handle graphics buffers. A use-after-free (UAF) vulnerability occurs when a program continues to use a pointer to memory after it has been freed, which can lead to arbitrary code execution.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberstan.co.uk/drm-lpe-linux/">Unprivileged root via a use-after-free in DRM GEM change_handle (CVE-2026-46215) – cyberstan</a></li>
<li><a href="https://www.phoronix.com/news/Linux-7.1-DRM-Change-Handle">Linux DRM Ioctl Developed By AMD Being Disabled Following Ongoing Security Issue - Phoronix</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion likely contains substantive technical analysis and debate regarding the root cause, exploitability, and patch status of this vulnerability, indicating significant community interest in kernel security.

**Tags**: `#linux-kernel`, `#security`, `#vulnerability`, `#cve`, `#exploit`

---

<a id="item-4"></a>
## [vLLM v0.24.0 Released with Major Optimizations for MiniMax-M3 and DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 is a major release with 571 commits, introducing support for the MiniMax-M3 model and extensive optimizations for DeepSeek-V4, including FP8/ROCm tuning and significant latency improvements through techniques like sparse index caching. This release significantly boosts the performance and hardware compatibility of a leading open-source LLM inference engine, enabling faster and more cost-effective deployment of large models on both NVIDIA and AMD GPUs. Key optimizations include MXFP4 support for MiniMax-M3 and a FlashInfer sparse index cache that provides a 2-4% improvement in Time to First Token (TTFT) for DeepSeek-V4; the release also marks the beginning of the deprecation window for using `CUDA_VISIBLE_DEVICES` internally on ROCm.

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-performance library for LLM inference and serving that implements efficient memory management and scheduling. FP8 (8-bit floating point) and ROCm (AMD's GPU computing platform) are technologies used to accelerate deep learning workloads on different hardware. MiniMax-M3 and DeepSeek-V4 are recent, large-scale mixture-of-experts (MoE) models that demand optimized inference kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitado.com.br/minimax-sparse-attention-msa-a-two-branch-block-sparse-attention-trained-on-a-109b-parameter-moe-with-a-3t-token-budget/">MiniMax Sparse Attention ( MSA ): a Two-Branch Block-Sparse...</a></li>
<li><a href="https://www.emergentmind.com/topics/mxfp4-data-format">MXFP4: Efficient 4-bit Data Format - Emergent Mind</a></li>
<li><a href="https://docs.flashinfer.ai/api/sparse.html">flashinfer . sparse - FlashInfer 0.6.13 documentation</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference-engine`, `#performance-optimization`, `#deep-learning`

---

<a id="item-5"></a>
## [Rocket Lab Acquires Iridium in Major Satellite Industry Consolidation](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

Rocket Lab has announced a historic agreement to acquire Iridium, a move that will provide the launch company with valuable spectrum assets and guaranteed launch volume. This acquisition represents significant consolidation in the satellite launch industry, giving Rocket Lab critical assets like spectrum and a baseline of regular launches to hedge against market volatility, directly mirroring a strategy previously seen with SpaceX and its Starlink constellation. The deal grants Rocket Lab control over Iridium's valuable L-band spectrum and orbit slots, and includes Iridium's profitable satellite operations and its order book for future constellation replacements.

hackernews · everfrustrated · Jun 29, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48719485)

**Background**: Iridium operates a constellation of 66 active satellites providing global voice and data coverage, originally launched in the late 1990s. The Iridium NEXT modernization saw its satellites launched by SpaceX. Spectrum refers to licensed radio frequencies crucial for satellite communications, and holding such assets is a core component of a satellite operator's value.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation - Wikipedia</a></li>
<li><a href="https://www.satellitetoday.com/technology/2019/10/15/satellite-operators-can-improve-return-on-assets-with-iot/">Satellite Operators Can Improve Return on Assets With IoT</a></li>

</ul>
</details>

**Discussion**: Commenters largely view this as a smart strategic move, noting it secures launch volume for Rocket Lab similar to how SpaceX uses Starlink. Discussion also raised concerns about increasing space debris and light pollution as launch costs drop. One commenter noted the irony of the acquisition making Rocket Lab, which started as a New Zealand source of pride, now an American company.

**Tags**: `#space-industry`, `#acquisitions`, `#satellite-launch`, `#business-strategy`, `#consolidation`

---

<a id="item-6"></a>
## [Study Finds Half of Social Media Child Safety Features Ineffective](https://www.ithome.com/0/970/253.htm) ⭐️ 8.0/10

A new study by New York University and Northeastern University tested 86 child safety features across Instagram, Snapchat, TikTok, and YouTube, finding that at least half on each platform failed to work as advertised, leaving children exposed to harmful content and unwanted contact. This research exposes critical gaps in the protective measures major social media platforms claim to have, directly impacting the online safety of millions of children and raising serious questions about platform accountability and regulatory effectiveness. The study used simulated child and adult accounts to test three scenarios: normal use by minors, teens bypassing safety features, and malicious adults circumventing protections. Specific failures included Snapchat allowing adult accounts to freely search for and message children, and TikTok recommending anorexia-related content to teen accounts.

rss · IT HOME · Jun 29, 23:46

**Background**: Major social media platforms like Instagram, Snapchat, TikTok, and YouTube have publicly promoted various parental controls, content filters, and contact restrictions designed to protect underage users. These features are often a key part of their compliance with children's online privacy and safety regulations, such as COPPA in the United States. The effectiveness of these measures has been a growing concern for parents, educators, and regulators worldwide.

**Discussion**: The article notes that platform companies like Meta disputed the study's conclusions, with Meta arguing that their teen accounts lead to less exposure to sensitive content and unwanted contact. The study authors were criticized for allegedly being vague and not providing specific evidence in their claims of feature failures.

**Tags**: `#online safety`, `#social media`, `#child protection`, `#research study`, `#platform accountability`

---

<a id="item-7"></a>
## [US Supreme Court Limits Geofence Warrants, Requiring Probable Cause for Cellphone Location Data](https://www.ithome.com/0/970/252.htm) ⭐️ 8.0/10

The US Supreme Court ruled 6-3 that law enforcement obtaining detailed cellphone location history via geofence warrants constitutes a Fourth Amendment search, even for short time periods, requiring probable cause and a warrant. This ruling significantly curtails the broad, suspicionless collection of location data from tech companies, setting major constitutional limits on surveillance practices and strengthening digital privacy protections for millions of users. The court specified that individuals cannot be swept into an investigation merely for being present in an area, but location data remains accessible if police have probable cause to target a specific individual or known suspect.

rss · IT HOME · Jun 29, 23:39

**Background**: A geofence warrant is a legal tool where law enforcement requests cellphone location data for all devices within a specific geographic area and time frame from companies like Google or Apple, in order to identify suspects. This practice was challenged under the Fourth Amendment, which protects against unreasonable searches and seizures, with the key legal question being whether such data collection constitutes a 'search' requiring a warrant based on probable cause.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/06/29/us/politics/supreme-court-geofence-warrant-cell-phones.html">Supreme Court Puts Limits on Cellphone Location Data Searches</a></li>
<li><a href="https://techcrunch.com/2026/06/29/in-major-privacy-win-supreme-court-rules-geofence-warrants-are-protected-by-privacy-rights/">In major privacy win, Supreme Court rules geofence... | TechCrunch</a></li>
<li><a href="https://versustexas.com/blog/carpenter-v-united-states/">Supreme Court: Warrant Required to Access Cell Site</a></li>

</ul>
</details>

**Tags**: `#digital privacy`, `#Supreme Court`, `#legal ruling`, `#law enforcement`, `#Fourth Amendment`

---

<a id="item-8"></a>
## [AI Observability Expands to Monitor Model Reliability and Hallucinations](https://www.infoq.cn/article/HUri8txfhl93vIb9kHIJ?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

The article argues that AI system observability must evolve beyond traditional infrastructure stability metrics to also include monitoring for model-specific issues like hallucination and reliability. This shift is critical because unreliable or hallucinating AI models can produce incorrect or harmful outputs, impacting user trust and safety, which traditional system monitoring would miss. The focus is on monitoring model performance and output quality in real-time, which requires new tools and metrics tailored for AI applications, distinct from logs, traces, and metrics used in traditional software.

rss · InfoQ 中文站 · Jun 29, 18:06

**Background**: Traditional observability in software engineering relies on logs, traces, and metrics to understand system health. AI systems, especially those using large language models (LLMs), introduce a new layer of complexity because their outputs are probabilistic and can 'hallucinate'—generating plausible but factually incorrect information. This has given rise to the field of MLOps and AI observability, which aims to ensure these models are reliable, transparent, and accountable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dynatrace.com/knowledge-base/ai-observability/">What is AI observability?</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-observability">What is AI Observability? | IBM</a></li>
<li><a href="https://galileo.ai/blog/llm-performance-metrics">7 Key LLM Metrics to Enhance AI Reliability | Galileo</a></li>

</ul>
</details>

**Tags**: `#AI observability`, `#LLM reliability`, `#MLOps`, `#model monitoring`

---

<a id="item-9"></a>
## [AWS Launches Graviton5 with 192 Cores and Formally Verified VM Isolation](https://www.infoq.cn/article/ONqpdtmlUXgF32G1vqT2?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

AWS announced the Graviton5 processor, which features 192 cores and introduces formally verified virtual machine isolation for enhanced security. This release sets a new benchmark for cloud infrastructure by combining high core density with mathematically proven security, impacting how developers build and secure high-performance applications in the cloud. The formally verified isolation is powered by the Nitro Isolation Engine, which provides mathematical assurance for VM isolation, moving beyond traditional security approaches.

rss · InfoQ 中文站 · Jun 29, 11:50

**Background**: AWS Graviton processors are a family of ARM-based CPUs designed by Amazon's Annapurna Labs, known for their energy efficiency and strong performance-per-watt ratio for cloud workloads. Formal verification is a mathematical method used to prove the correctness of a system's design against a specification, offering a much higher degree of assurance than traditional testing. The Nitro platform provides the underlying hardware and software for AWS EC2, offloading virtualization functions to dedicated hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AWS_Graviton">AWS Graviton - Wikipedia</a></li>
<li><a href="https://oracore.dev/en/news/nitro-split-kernel-isolation-math-en">Nitro’s split kernel turns isolation into math | OraCore.dev</a></li>
<li><a href="https://www.nops.io/blog/aws-graviton-processors/">AWS Graviton : Basics, benefits, and processing | nOps</a></li>

</ul>
</details>

**Tags**: `#cloud-computing`, `#AWS`, `#hardware`, `#security`, `#virtualization`

---

<a id="item-10"></a>
## [Microsoft Introduces Memora, a Scalable Memory System for AI Agents](https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity/) ⭐️ 8.0/10

Microsoft Research has introduced Memora, a novel memory representation system for AI agents that separates storage from retrieval to improve efficiency in long and complex tasks. The system is designed to be scalable and addresses the fundamental problem of AI agents having to constantly reload or retrieve context. This memory system could significantly improve the performance and efficiency of AI agents engaged in long-duration, complex tasks by reducing the computational overhead of constant context reloading. It represents a meaningful architectural contribution that may influence the design of future agent systems, especially as they are scaled for more sophisticated applications. The core innovation of Memora is its separation of what is stored from how it is retrieved, which is intended to make memory management more efficient and scalable. While the concept is promising, the provided blog post from Microsoft Research does not include detailed implementation specifics or extensive performance benchmarks.

rss · Microsoft Research · Jun 29, 21:14

**Background**: AI agents, especially those based on large language models, typically suffer from limited context windows, meaning they can only 'remember' a fixed amount of recent information. Systems like Retrieval-Augmented Generation (RAG) address this by retrieving relevant documents from an external database, but they can still struggle with efficiency over very long tasks. Memory systems for agents aim to maintain a structured, persistent record of past interactions and knowledge to enable more coherent and stateful behavior over time.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG? - Retrieval-Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://redis.io/blog/ai-agent-memory-stateful-systems/">AI agent memory: types, architecture & implementation</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#memory systems`, `#retrieval-augmented generation`, `#scalable architecture`, `#Microsoft Research`

---

<a id="item-11"></a>
## [JIT Compiler for Game Boy Translates to WebAssembly, Outperforms Native Interpreter](https://humphri.es/blog/WATaBoy/) ⭐️ 8.0/10

A project named WATaBoy developed a JIT compiler that translates Game Boy CPU instructions into WebAssembly bytecode at runtime, achieving faster execution than a traditional native interpreter. This demonstrates that WebAssembly can serve as a high-performance compilation target for emulation, potentially enabling complex emulators to run efficiently in web browsers without relying on native code. The JIT compiler dynamically converts Game Boy opcodes into WebAssembly instructions, leveraging Wasm's near-native execution speed within a sandboxed environment.

rss · Lobsters · Jun 29, 15:07

**Background**: WebAssembly (Wasm) is a binary instruction format designed as a portable compilation target for programming languages, enabling deployment on the web and other environments. The Game Boy's CPU uses a specific instruction set architecture (ISA), and emulators typically interpret these instructions in software. JIT compilation improves performance by translating code into native machine code at runtime, reducing the overhead of repeated interpretation.

<details><summary>References</summary>
<ul>
<li><a href="https://wingolog.org/archives/2022/08/18/just-in-time-code-generation-within-webassembly">just-in-time code generation within webassembly — wingolog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Just-in-time_compilation">Just -in- time compilation - Wikipedia</a></li>
<li><a href="https://meganesulli.com/blog/game-boy-opcodes/">Meet the Game Boy Instruction Set | Megan Sullivan</a></li>

</ul>
</details>

**Discussion**: The linked comments on Lobsters indicate significant interest in this technical achievement, with discussions likely focusing on the novelty of using JIT compilation for WebAssembly-based emulation and the practical performance implications.

**Tags**: `#WebAssembly`, `#JIT compilation`, `#emulation`, `#performance`, `#Game Boy`

---

<a id="item-12"></a>
## [New Linux Exploit Escapes Containers via IPv6 Fragment Bug](https://github.com/sgkdev/ipv6_frag_escape) ⭐️ 8.0/10

A proof-of-concept exploit called ipv6_frag_escape has been published, leveraging a use-after-free vulnerability in the Linux kernel's IPv6 fragment handling to reliably escape from jails and containers for local privilege escalation. This exploit directly threatens the security isolation fundamental to containers and jails, potentially allowing a compromised application within a container to gain full control of the host system, which is a critical risk for cloud and multi-tenant environments. The vulnerability, tracked as CVE-2022-48956, is a use-after-free issue that occurs when the ip6_fragment function is invoked without proper locking, and the published exploit is described as reliable for escaping various container runtimes.

rss · Lobsters · Jun 29, 17:01

**Background**: Local privilege escalation (LPE) refers to an attack where a user with limited access on a system gains higher-level privileges, such as root. Container and jail escapes are a severe type of LPE where an attacker breaks out of an isolated environment to access the underlying host operating system. IPv6 fragment reassembly is a complex part of the network stack where previous vulnerabilities like SegmentSmack have also been found.

<details><summary>References</summary>
<ul>
<li><a href="https://vulert.com/vuln-db/debian-11-linux-173152">Use-After-Free Vulnerability in Linux Kernel's IPv6 Fragmentation - CVE-2022-48956</a></li>
<li><a href="https://www.kyberturvallisuuskeskus.fi/en/vulnerability-handling-ip-fragments">Vulnerability in the handling of IP fragments | NCSC-FI</a></li>
<li><a href="https://hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html">Linux Privilege Escalation - HackTricks</a></li>

</ul>
</details>

**Discussion**: The community discussion on Lobste.rs likely focuses on the severity of the container escape, potential mitigation strategies such as applying kernel patches or disabling IPv6, and the implications for container security models.

**Tags**: `#security`, `#vulnerability`, `#linux`, `#container-escape`, `#exploit`

---

<a id="item-13"></a>
## [New Research Reveals Vulnerable RSA Keys with Many Zeros in Wild](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html) ⭐️ 8.0/10

Researchers have identified a new class of weak RSA keys characterized by having many zeros in their modulus, and the open-source badkeys project has found these vulnerable keys in real-world systems like TLS and SSH. This discovery poses significant security risks because these weak keys can be factored more easily, potentially allowing attackers to decrypt communications or impersonate servers in widely deployed cryptographic systems. The research leveraged the badkeys project, which scans massive datasets from public sources like Certificate Transparency logs and internet-wide scans to identify keys with unexpectedly sparse patterns, indicating cryptographic weakness.

rss · Schneier on Security · Jun 29, 16:05

**Background**: RSA is a foundational public-key cryptosystem widely used for secure data transmission. Its security relies on the difficulty of factoring large numbers into their prime components, and keys with unusual patterns, like many zeros, can create mathematical shortcuts that make this factoring easier than intended.

<details><summary>References</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html">Factoring RSA Keys with Many Zeros - Schneier on Security</a></li>
<li><a href="https://www.scworld.com/brief/researchers-discover-new-class-of-weak-rsa-keys-in-the-wild">Researchers discover new class of weak RSA keys in the wild | brief | SC Media</a></li>
<li><a href="https://securityboulevard.com/2026/06/factoring-rsa-keys-with-many-zeros/">Factoring RSA Keys with Many Zeros - Security Boulevard</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#RSA`, `#security`, `#vulnerabilities`, `#key-management`

---

<a id="item-14"></a>
## [Tesla's FSD v14 Lite brings HW4-level driving and parking to HW3 cars](https://x.com/Tesla_AI/status/2071592820889260101) ⭐️ 8.0/10

Tesla released FSD v14 Lite on June 29, 2026, a software update that distills the advanced neural network from Hardware 4 (HW4) vehicles to run on older Hardware 3 (HW3) cars, enabling them to access capabilities previously exclusive to HW4, such as reinforcement learning and offline models. This update is significant because it backports advanced Full Self-Driving (FSD) capabilities to a large installed base of older vehicles, extending their lifespan and value, and demonstrates Tesla's strategy of using software refinement to overcome hardware limitations. The distilled model for HW3 is approximately 15% the size of the original HW4 network to fit within HW3's memory constraints, and the update improves performance in scenarios like navigation, lane changes, and pedestrian interaction while introducing new parking features for the first time.

telegram · zaihuapd · Jun 30, 02:26

**Background**: Tesla's Hardware 3 (HW3) and Hardware 4 (HW4) refer to different generations of the onboard computer for its Autopilot and Full Self-Driving (FSD) systems, with HW4 offering more processing power and memory for running larger AI models. Full Self-Driving (FSD) is Tesla's advanced driver-assistance system that aims to eventually enable autonomous driving. Over-the-air (OTA) updates allow Tesla to deploy new software features directly to vehicles remotely.

<details><summary>References</summary>
<ul>
<li><a href="https://www.notateslaapp.com/news/4369/tesla-launches-fsd-v14-lite-first-impressions">Tesla Launches FSD V 14 - Lite : First Impressions - Not a Tesla App</a></li>
<li><a href="https://electrek.co/2026/06/29/tesla-fsd-v14-lite-hw3-rollout/">Tesla starts FSD v 14 ' Lite ' rollout to HW 3 cars | Electrek</a></li>
<li><a href="https://arxiv.org/html/2512.18662v1">Offline Reinforcement Learning for End-to-End Autonomous Driving</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#autonomous driving`, `#FSD`, `#over-the-air updates`, `#AI`

---