---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 216 items, 13 important content pieces were selected

---

1. [vLLM v0.21.0 Released with Major Build Change and Advanced Features](#item-1) ⭐️ 9.0/10
2. [First Public macOS Kernel Memory Corruption Exploit Targets Apple M5 Hardware](#item-2) ⭐️ 9.0/10
3. [Critical Linux Page Cache Flaws Threaten All Major Distributions](#item-3) ⭐️ 9.0/10
4. [PostgreSQL Releases Security Updates for Multiple Versions Addressing 11 CVEs](#item-4) ⭐️ 9.0/10
5. [Critical Linux zero-day vulnerability allows unprivileged users to read root files](#item-5) ⭐️ 9.0/10
6. [Alipay Account Drain of 1.84 Million Yuan After Payment Function Disabled](#item-6) ⭐️ 8.0/10
7. [Researchers Use Anthropic's Claude Mythos AI to Exploit macOS Privilege Escalation Flaw](#item-7) ⭐️ 8.0/10
8. [OpenAI Mandates ChatGPT Mac App Update After TanStack Supply Chain Attack](#item-8) ⭐️ 8.0/10
9. [Google DORA Report: Engineering Foundations Key to AI Investment Returns](#item-9) ⭐️ 8.0/10
10. [(分享发现) Deekseek 疑似爆出一个 bug！可能是 P0 级的顶级安全事故](#item-10) ⭐️ 8.0/10
11. [OpenAI Codex Mobile Preview Now Available in ChatGPT App](#item-11) ⭐️ 8.0/10
12. [Abridge AI Scales to 100M Visits, Saving Clinicians 10-20 Hours Weekly](#item-12) ⭐️ 8.0/10
13. [Anthropic Restricts Mythos AI Due to Superior Vulnerability Detection](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 Released with Major Build Change and Advanced Features](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 9.0/10

vLLM v0.21.0 introduces a mandatory C++20 build requirement and formally deprecates support for Transformers v4, requiring users to migrate to v5. The release adds several advanced features, including KV offloading integrated with the Hybrid Memory Allocator (HMA), speculative decoding that respects thinking/reasoning budgets, and a new TOKENSPEED_MLA attention backend for specific models on NVIDIA Blackwell GPUs. As a widely-used high-performance LLM inference engine, vLLM's adoption of C++20 aligns it with modern toolchains like PyTorch, which is crucial for long-term maintainability and compatibility. The new features like HMA-integrated KV offloading and budget-aware speculative decoding directly address core challenges in scaling and accelerating LLM inference, potentially reducing latency and memory footprint for serving large models. The C++20 requirement is a breaking change that necessitates compiler upgrades for users building from source. The KV offloading subsystem now includes scheduler-side sliding window group support and enables distributed KV offloading via connectors like MooncakeStoreConnector.

github · khluu · May 14, 23:15

**Background**: vLLM is a high-throughput and memory-efficient inference and serving engine for Large Language Models (LLMs). KV caching is a fundamental optimization in LLM inference that stores intermediate key-value states to avoid redundant computation. Speculative decoding is a technique that uses a smaller, faster 'draft' model to generate candidate tokens, which are then verified by the main model to accelerate generation. The Hybrid Memory Allocator (HMA) is a memory management system designed to efficiently utilize both high-bandwidth (GPU) and main (CPU) memory for tasks like KV cache offloading.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/issues/22605">[RFC]: Separated CPU KV Cache Offloading/Transfer Process · Issue #22605 · vllm-project/vllm</a></li>
<li><a href="https://arxiv.org/html/2504.14893v1">Hardware-based Heterogeneous Memory Management for Large Language Model Inference</a></li>
<li><a href="https://deepwiki.com/vllm-project/vllm/8-attention-backends">Attention Backends | vllm-project/vllm | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#LLM-inference`, `#model-serving`, `#GPU-optimization`, `#open-source`, `#AI-infra`

---

<a id="item-2"></a>
## [First Public macOS Kernel Memory Corruption Exploit Targets Apple M5 Hardware](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

The Calif team, assisted by the AI system Mythos Preview, developed and published the first public kernel memory corruption exploit for Apple's M5 chip in macOS, which bypasses the MIE hardware protection and achieves local privilege escalation from a non-privileged user to a root shell within five days. This exploit is significant because it demonstrates that Apple's five-year effort to build the Memory Integrity Enforcement (MIE) hardware defense can be bypassed, highlighting a potential paradigm shift where AI-assisted collaboration can rapidly defeat top-tier security measures and raising urgent questions for the cybersecurity ecosystem. The attack chain involves two distinct vulnerabilities and multiple techniques, exploiting data-type local kernel privilege escalation in macOS 26.4.1 using only standard system calls, and the full 55-page technical report will be released after Apple issues a fix.

hackernews · Lobsters · May 14, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48139219)

**Background**: Apple's Memory Integrity Enforcement (MIE) is a hardware-based security feature introduced on the M5 chip that uses tagged memory to protect against buffer overflow and memory corruption attacks, building upon ARM's Memory Tagging Extension (MTE). The Apple M5 chip is the latest generation of Apple's custom silicon for Macs, iPads, and Vision Pro, featuring a unified memory architecture designed for on-device AI performance.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/">Apple unleashes M 5 , the next big leap in AI performance for... - Apple</a></li>
<li><a href="https://8ksec.io/mie-deep-dive-kernel/">Memory Integrity Enforcement (MIE) on iOS Deep Dive</a></li>

</ul>
</details>

**Discussion**: The community reaction is mixed with a sense of unease; some users express skepticism about the technical details provided, while others highlight the potential bug bounty payout, which could range from $100,000 to $1.5 million depending on how the exploit is framed. A recurring sentiment is that the world is not prepared for the impact of LLMs on security, and one user humorously comments on feeling foolish for purchasing the M5 specifically for its MIE protection.

**Tags**: `#macOS security`, `#kernel exploit`, `#M5 chip`, `#AI-assisted research`, `#vulnerability research`

---

<a id="item-3"></a>
## [Critical Linux Page Cache Flaws Threaten All Major Distributions](https://www.infoq.cn/article/1HucCJrazwgF7QNT232r?utm_source=rss&utm_medium=article) ⭐️ 9.0/10

Security researchers have disclosed two critical Linux kernel vulnerabilities, Copy Fail (CVE-2026-31431) and DirtyFrag, which exploit page cache logic bugs to allow unprivileged local users to gain root access on affected systems. These vulnerabilities affect all major Linux distributions and provide attackers with powerful primitives to escalate privileges, posing a significant and immediate security risk to servers, workstations, and cloud infrastructure. Copy Fail is a logic bug in the cryptographic template that chains AF_ALG and splice() to enable a controlled 4-byte write into the page cache, while DirtyFrag involves vulnerabilities in modules like xfrm-ESP for IPsec operations.

rss · InfoQ 中文站 · May 15, 09:37

**Background**: The Linux page cache is a critical memory management component that stores copies of frequently accessed data from disk to speed up system performance. A write primitive to this cache can allow an attacker to modify executable files or sensitive system data. The AF_ALG interface is a kernel-based cryptographic API, and splice() is a system call for moving data between file descriptors without copying to user space.

<details><summary>References</summary>
<ul>
<li><a href="https://xint.io/blog/copy-fail-linux-distributions">Copy Fail : 732 Bytes to Root on Every Major Linux Distribution. - Xint</a></li>
<li><a href="https://www.elastic.co/security-labs/copy-fail-dirtyfrag-linux-page-bugs-in-the-wild">Copy Fail and DirtyFrag: Linux Page Cache ... — Elastic Security Labs</a></li>
<li><a href="https://arstechnica.com/security/2026/05/linux-bitten-by-second-severe-vulnerability-in-as-many-weeks/">Linux bitten by second severe vulnerability in as many... - Ars Technica</a></li>

</ul>
</details>

**Tags**: `#Linux`, `#Security`, `#Kernel`, `#Vulnerability`, `#Systems`

---

<a id="item-4"></a>
## [PostgreSQL Releases Security Updates for Multiple Versions Addressing 11 CVEs](https://www.postgresql.org/about/news/postgresql-184-1710-1614-1518-and-1423-released-3297/) ⭐️ 9.0/10

The PostgreSQL Global Development Group has released security updates for versions 18.4, 17.10, 16.14, 15.18, and 14.23 to address 11 security vulnerabilities, known as Common Vulnerabilities and Exposures (CVEs). This release is critical for database administrators and security teams as it patches significant vulnerabilities in one of the world's most popular open-source relational database systems, helping to prevent potential data breaches or system compromises. The updates cover five major PostgreSQL release branches (18, 17, 16, 15, and 14), ensuring that users on older but still supported versions also receive necessary security fixes. The specific technical nature and severity of the 11 CVEs were not detailed in the initial summary, but such releases are typically urgent for production environments.

rss · Lobsters · May 14, 19:43

**Background**: PostgreSQL is a powerful, open-source object-relational database system with a strong reputation for reliability, feature robustness, and performance. CVEs are standardized identifiers for publicly known cybersecurity vulnerabilities, and regular security updates are a standard practice in software maintenance to protect users. Database administrators are advised to apply these updates promptly to mitigate risks.

**Discussion**: The linked Lobste.rs discussion indicates high community engagement with 43 comments and 96 upvotes, showing strong interest in the security of this widely-used database system. The comments likely involve discussions on the specific vulnerabilities, upgrade procedures, and the importance of timely patching in production environments.

**Tags**: `#databases`, `#security`, `#postgresql`, `#CVEs`, `#releases`

---

<a id="item-5"></a>
## [Critical Linux zero-day vulnerability allows unprivileged users to read root files](https://github.com/0xdeadbeefnetwork/ssh-keysign-pwn/) ⭐️ 9.0/10

A zero-day vulnerability has been disclosed that allows unprivileged Linux users to access files owned by root, likely due to a flaw in the ssh-keysign binary. This is a critical security issue because it enables local privilege escalation, allowing any regular user to bypass file permissions and potentially read sensitive system files, which could lead to full system compromise. The vulnerability involves the ssh-keysign binary, which is typically installed as a SUID program, meaning it runs with elevated privileges and any flaw in it can be exploited to gain higher access.

rss · Lobsters · May 15, 01:14

**Background**: SSH (Secure Shell) is a cryptographic network protocol used for secure remote login and other network services. ssh-keysign is a helper program used by the SSH client for host-based authentication; it is typically installed as a SUID binary to allow it to read system host keys, which is a common source of security vulnerabilities if not implemented correctly.

<details><summary>References</summary>
<ul>
<li><a href="https://steflan-security.com/linux-privilege-escalation-exploiting-misconfigured-ssh-keys/">Linux Privilege Escalation - Exploiting Misconfigured SSH Keys - Steflan's Security Blog</a></li>
<li><a href="https://www.halfdog.net/Security/2017/SshAgentGainGroupPrivileges/">Gain Access to SSH Group via ssh-agent and OpenSSL</a></li>

</ul>
</details>

**Discussion**: The linked discussion on Lobsters indicates significant community engagement and verification of the vulnerability's severity, confirming it is a real and critical zero-day issue.

**Tags**: `#security`, `#linux`, `#zero-day`, `#vulnerability`, `#privilege-escalation`

---

<a id="item-6"></a>
## [Alipay Account Drain of 1.84 Million Yuan After Payment Function Disabled](https://www.ithome.com/0/950/711.htm) ⭐️ 8.0/10

A user's Alipay account was used to make unauthorized donations totaling 1.847 million yuan even after she had contacted customer service to disable payment functions. An investigation by the People's Bank of China Shanghai Branch found that Alipay's system retained a loophole allowing charitable donations to proceed despite the payment function being closed. This incident reveals a critical security and design flaw in one of China's largest digital payment platforms, undermining user trust and exposing potential gaps in financial regulatory oversight for digital services. It highlights how platform-specific technical decisions can override user intent with severe financial consequences. The People's Bank of China confirmed the account's payment function was closed throughout, but Alipay's design allowed charitable donations to bypass this restriction via computer password verification and mobile phone SMS/biometric authentication. Alipay stated it suspects the account was shared and is seeking police assistance, while the recipient charity foundation indicated willingness to verify refund eligibility upon receiving official proof of involuntary donation.

rss · IT HOME · May 15, 02:00

**Background**: Alipay is a dominant mobile and online payment platform operated by Ant Group, serving over a billion users in China. In digital payment systems, users can typically disable core payment functions like transfers and consumption for security. Charitable donation platforms often integrate with payment systems like Alipay to facilitate social welfare contributions, which are usually irreversible once executed.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ifeng.com/c/8t7lhDoqRzV">女子称关闭 支 付 功 能 后，180多万元凌晨莫名通过 支 付 宝 捐 给慈善 机 构</a></li>
<li><a href="https://fgw.sh.gov.cn/ys-hqjrfw-1.3.3.2/index.html">责任披露、数据使用和争议机制_上海市发展和改革委员会</a></li>
<li><a href="https://www.workercn.cn/c/2025-12-10/8680864.shtml">中 国 乡 村 发 展 基 金 会 ：童伴妈妈 项 目 累计服务儿童近90...</a></li>

</ul>
</details>

**Tags**: `#Alipay`, `#security`, `#financial-fraud`, `#regulation`, `#digital-payments`

---

<a id="item-7"></a>
## [Researchers Use Anthropic's Claude Mythos AI to Exploit macOS Privilege Escalation Flaw](https://www.ithome.com/0/950/676.htm) ⭐️ 8.0/10

Security researchers from Calif used Anthropic's most powerful AI model, Claude Mythos, to discover and chain two vulnerabilities in macOS 26.4.1, achieving a local privilege escalation to a root shell on Apple M5 hardware. This is the first publicly documented kernel memory corruption exploit on Apple M5 silicon that bypasses Apple's hardware-enforced Memory Integrity Enforcement (MIE) security, demonstrating a new paradigm where advanced AI significantly accelerates the discovery and execution of complex cyberattacks against hardened systems. The attack chain started from an unprivileged local account, combined two distinct vulnerabilities and multiple exploitation techniques, and was developed by human researchers collaborating with the AI model over approximately five days; the specific vulnerability details remain undisclosed as Apple is still reviewing them.

rss · IT HOME · May 15, 00:14

**Background**: Claude Mythos is Anthropic's latest and most capable large language model, positioned as a rival to models like GPT-4 and Gemini. Memory Integrity Enforcement (MIE) is a major security feature Apple introduced for its Apple Silicon chips, using hardware capabilities to enforce memory safety and make certain types of exploits more difficult. A local privilege escalation (LPE) vulnerability allows an attacker with basic user access on a device to gain higher, often root, privileges, giving them full control over the system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model ) - Wikipedia</a></li>
<li><a href="https://8ksec.io/mie-deep-dive-kernel/">iOS Memory Integrity Enforcement Deep Dive | 8kSec</a></li>
<li><a href="https://cybersnowden.com/local-privilege-escalation-lpe-exploits-detection-defense/">Local Privilege Escalation (LPE) Exploits — Detection & Defense - Cyber ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#AI`, `#macOS`, `#privilege-escalation`

---

<a id="item-8"></a>
## [OpenAI Mandates ChatGPT Mac App Update After TanStack Supply Chain Attack](https://www.ithome.com/0/950/666.htm) ⭐️ 8.0/10

OpenAI is requiring all Mac ChatGPT desktop application users to update their app by June 12, 2025, due to a supply chain attack that compromised its internal code signing certificates. This incident highlights the cascading risk of supply chain attacks in the open-source ecosystem, as a compromise in a popular library can directly impact major AI companies and force emergency security actions from end-users. The attack, linked to the 'Mini Shai-Hulud' campaign, only compromised two OpenAI employees' devices, limiting the breach to internal code repositories and credential materials; user data and OpenAI's core systems were reportedly unaffected.

rss · IT HOME · May 14, 23:30

**Background**: TanStack is a popular collection of open-source web development libraries, including TanStack Query for data fetching. The 'Mini Shai-Hulud' is a known supply chain malware that hijacks CI/CD pipelines and spoofs digital signatures to compromise software packages. Code signing certificates are used by developers to digitally sign applications, ensuring they are authentic and have not been tampered with; their compromise allows attackers to sign malicious software with a trusted key.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberscoop.com/mini-shai-hulud-supply-chain-malware-attack/">‘Mini Shai-Hulud’ malware compromises hundreds of open-source packages in sprawling supply-chain attack | CyberScoop</a></li>
<li><a href="https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem">TeamPCP's Mini Shai-Hulud Is Back: A Self-Spreading Supply Chain Attack Compromises TanStack npm Packages - StepSecurity</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply chain attack`, `#OpenAI`, `#macOS`, `#vulnerability`

---

<a id="item-9"></a>
## [Google DORA Report: Engineering Foundations Key to AI Investment Returns](https://www.infoq.cn/article/IgGuKFh9qmKmFEIZeR4t?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Google's DevOps Research and Assessment (DORA) team released a new report emphasizing that solid engineering foundations are crucial for achieving returns on AI investments. This report is significant because it provides practical insights for organizations investing in AI, highlighting that foundational engineering practices directly impact the success and return on investment of AI initiatives. The report likely draws on DORA's established metrics for software delivery performance, which predict organizational outcomes, and connects them to the effectiveness of AI deployments.

rss · InfoQ 中文站 · May 14, 09:23

**Background**: DORA is a research team within Google Cloud that studies DevOps practices. It is known for identifying key metrics like deployment frequency and lead time for changes that measure software delivery performance. The annual State of DevOps Reports, which DORA produces, are influential in the software engineering community.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DORA_Metrics">DORA Metrics</a></li>
<li><a href="https://dora.dev/guides/dora-metrics/">DORA | DORA's software delivery performance metrics</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#DORA metrics`, `#engineering practices`, `#ROI`

---

<a id="item-10"></a>
## [(分享发现) Deekseek 疑似爆出一个 bug！可能是 P0 级的顶级安全事故](https://www.v2ex.com/t/1212886#reply8) ⭐️ 8.0/10

A user reports a possible critical bug in DeepSeek's platform where typing a specific command could expose other users' historical conversation data.

rss · V2EX · May 15, 02:23

**Tags**: `#security-vulnerability`, `#AI-safety`, `#data-leakage`, `#DeepSeek`, `#bug-report`

---

<a id="item-11"></a>
## [OpenAI Codex Mobile Preview Now Available in ChatGPT App](https://www.v2ex.com/t/1212885#reply1) ⭐️ 8.0/10

OpenAI has integrated a mobile preview of its Codex coding agent into the ChatGPT iOS and Android apps, now available to all users including free and Go tier plans. This allows developers to remotely connect to their laptops, Mac minis, or cloud development environments from their phones to monitor agent status, approve commands, and review code diffs and test outputs. This move transforms coding assistants from desktop-bound tools into truly mobile collaborators, enabling developers to review and approve AI-driven work from anywhere, which could significantly increase productivity and flexibility in software development workflows. The mobile preview allows real-time monitoring of agent threads and approval of tasks, specifically designed for longer-running agentic coding work where developers can now stay in the loop remotely. The feature is accessible to all ChatGPT users across all subscription tiers, expanding Codex's accessibility beyond just paid plans.

rss · V2EX · May 15, 02:23

**Background**: OpenAI Codex is a cloud-based AI coding agent powered by ChatGPT that can autonomously perform software development tasks like writing code, debugging, and running tests in parallel using cloud environments. Remote development involves connecting from one machine (like a phone) to another environment (like a laptop or cloud server) to work on code, a practice supported by tools like VS Code and JetBrains IDEs. The agentic workflow described emphasizes autonomous, long-running tasks where the AI agent works independently while the human developer oversees and approves changes remotely.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/work-with-codex-from-anywhere/">Work with Codex from anywhere | OpenAI</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://developers.openai.com/codex">Codex | OpenAI Developers</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so there is no discussion to summarize.

**Tags**: `#OpenAI`, `#Codex`, `#Mobile Development`, `#Remote Development`, `#ChatGPT`

---

<a id="item-12"></a>
## [Abridge AI Scales to 100M Visits, Saving Clinicians 10-20 Hours Weekly](https://www.latent.space/p/abridge) ⭐️ 8.0/10

Abridge is scaling its AI platform to process 100 million doctor visits, automating prior authorization and clinical documentation to save clinicians an estimated 10 to 20 hours per week. This demonstrates a major, practical deployment of generative AI in healthcare, directly addressing clinician burnout by automating high-volume administrative tasks and improving operational efficiency on a massive scale. The platform leverages generative AI to convert live patient-clinician conversations into clinical notes and streamlines the prior authorization process, which is a notoriously time-consuming administrative hurdle in healthcare.

rss · Latent Space · May 14, 22:05

**Background**: Prior authorization is a requirement by health insurers for clinicians to obtain approval before providing a specific service or medication, a process known for delays and administrative burden. Clinical documentation automation uses AI, particularly large language models (LLMs), to generate accurate medical notes from conversations, aiming to reduce the paperwork that contributes significantly to clinician burnout.

<details><summary>References</summary>
<ul>
<li><a href="https://www.abridge.com/">Generative AI for Clinical Conversations | Abridge</a></li>
<li><a href="https://tossom.com/products/abridge-ai">Abridge AI - Generative AI for Clinical Documentation... | Tossom</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11105142/">Efficient healthcare with large language models: optimizing clinical ...</a></li>

</ul>
</details>

**Tags**: `#AI in Healthcare`, `#Large Language Models`, `#Clinical Automation`, `#Startup Case Study`

---

<a id="item-13"></a>
## [Anthropic Restricts Mythos AI Due to Superior Vulnerability Detection](https://www.schneier.com/blog/archives/2026/05/how-dangerous-is-anthropics-mythos-ai.html) ⭐️ 8.0/10

Anthropic announced that its new Claude Mythos Preview model is so proficient at finding software vulnerabilities that the company will not release it to the general public, instead limiting access to a select group of companies for scanning their own software. This decision highlights the growing tension between advancing powerful AI capabilities for security benefits and the need for responsible deployment to prevent misuse, setting a precedent for how powerful AI models might be controlled. The announcement notes that while Anthropic's model is exceptionally capable, other models like OpenAI's GPT-5.5, as evaluated by the UK's AI Security Institute, show comparable vulnerability-finding abilities.

rss · Schneier on Security · May 14, 11:04

**Background**: AI models are increasingly being tested for cybersecurity applications, such as automatically detecting software flaws before they can be exploited. Companies and institutes are evaluating these models to understand their potential risks and benefits, leading to debates on safe and controlled access.

**Tags**: `#AI safety`, `#cybersecurity`, `#responsible AI`, `#software vulnerabilities`, `#anthropic`

---