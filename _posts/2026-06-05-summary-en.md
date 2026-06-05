---
layout: default
title: "Horizon Summary: 2026-06-05 (EN)"
date: 2026-06-05
lang: en
---

> From 199 items, 14 important content pieces were selected

---

1. [Gaussian Point Splatting enables real-time, high-quality 3D rendering](#item-1) ⭐️ 10.0/10
2. [Shenzhen Team Trains 1.6T-Parameter Model on Domestic Huawei Ascend 910C Chips](#item-2) ⭐️ 9.0/10
3. [Cloudflare Acquires VoidZero to Advance JavaScript Tooling and AI-Native Web](#item-3) ⭐️ 8.0/10
4. [Anthropic Reports Progress on AI Recursive Self-Improvement](#item-4) ⭐️ 8.0/10
5. [Cloudflare Reports Bot Traffic Surpasses Human Traffic for the First Time in Internet History](#item-5) ⭐️ 8.0/10
6. [AMD debuts Helios, its first rack-scale AI platform, to rival NVIDIA NVL72.](#item-6) ⭐️ 8.0/10
7. [Anthropic calls for global pause on advanced AI due to loss-of-control signs.](#item-7) ⭐️ 8.0/10
8. [Alipay uses AI agents to detect security flaws in other agents](#item-8) ⭐️ 8.0/10
9. [MobileGym: Browser-Based Android Simulation for GUI Agent Training](#item-9) ⭐️ 8.0/10
10. [ChatGPT Upgrades Memory System with Automated 'Dreaming' Process](#item-10) ⭐️ 8.0/10
11. [The Race: AI Enthusiasts Chase Time, Skeptics Battle Entropy](#item-11) ⭐️ 8.0/10
12. [Hackers exploit Meta AI chatbot to hijack Instagram accounts via social engineering](#item-12) ⭐️ 8.0/10
13. [Microsoft Achieves 20-Second Qubit Coherence Breakthrough](#item-13) ⭐️ 8.0/10
14. [Pentagon Considers Ending Anthropic Partnership Over AI Military Use Restrictions](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Gaussian Point Splatting enables real-time, high-quality 3D rendering](https://momentsingraphics.de/Siggraph2026.html) ⭐️ 10.0/10

A SIGGRAPH 2026 paper introduces Gaussian Point Splatting, a stochastic rendering method that uses explicit 3D Gaussian primitives instead of neural networks to achieve real-time, high-quality scene rendering. This technique represents a significant advancement in real-time 3D rendering, offering a potentially transformative alternative to neural radiance fields by combining the benefits of explicit Gaussian representations with efficient, scalable rendering. The core idea is to sample pixel-sized, opaque points from the Gaussians and splat them to a framebuffer using 64-bit atomics, which scales extremely well to scenes with many Gaussians.

rss · Lobsters · Jun 4, 15:15

**Background**: 3D Gaussian Splatting (3DGS) is a rasterization-based technique for representing and rendering photorealistic 3D scenes from sparse 2D images, which emerged as a mainstream method in 3D reconstruction. Unlike neural radiance fields (NeRF) that encode scenes in neural network weights, 3DGS uses explicit Gaussian ellipsoid primitives, enabling real-time rendering and easier editing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/3d-gaussian-primitives">3D Gaussian Primitives: Efficient Scene Rendering</a></li>
<li><a href="https://momentsingraphics.de/Siggraph2026.html">Gaussian Point Splatting - momentsingraphics.de</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion likely contains high-quality technical debate and community validation, as suggested by the news item's high score and the active research interest in improving 3DGS for deployment on lightweight devices and large-scale scenes.

**Tags**: `#computer_graphics`, `#3D_rendering`, `#neural_radiance_fields`, `#real_time_rendering`, `#SIGGRAPH`

---

<a id="item-2"></a>
## [Shenzhen Team Trains 1.6T-Parameter Model on Domestic Huawei Ascend 910C Chips](https://www.ithome.com/0/960/281.htm) ⭐️ 9.0/10

A joint research team from Shenzhen successfully completed the full-parameter post-training of the 1.6 trillion-parameter DeepSeek-V4-Pro model using a domestic Huawei Ascend 910C AI computing cluster. This achievement serves as a major validation that China's domestic AI chips can handle world-class, ultra-large model training, which is a critical milestone for the country's semiconductor self-sufficiency and AI development strategy. The project achieved a Model FLOPs Utilization (MFU) exceeding 30% and a 14% improvement in the efficiency of key training operators, with all metrics meeting industrial-grade operational standards.

rss · IT HOME · Jun 5, 02:40

**Background**: The Huawei Ascend 910C is a high-performance AI processor from Huawei, positioned as a competitive alternative to Nvidia's chips within China. DeepSeek-V4-Pro is a large language model with a mixture-of-experts (MoE) architecture and 1.6 trillion total parameters, with only 49 billion parameters active per token, representing a state-of-the-art design for efficiency and performance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lovechip.com/blog/meet-huawei-s-ascend-910c-a-new-contender-in-the-ai-chip-arena">Meet Huawei's Ascend 910C: A New Contender in the AI Chip Arena</a></li>
<li><a href="https://www.morphllm.com/deepseek-v4">DeepSeek V4 (2026): Specs, Benchmarks, API Pricing, and ...</a></li>
<li><a href="https://www.aimadetools.com/blog/deepseek-v4-pro-complete-guide/">DeepSeek V4 Pro Complete Guide: 1.6T Parameters, 80.6% SWE ...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Huawei Ascend`, `#large language models`, `#China tech`, `#AI training`

---

<a id="item-3"></a>
## [Cloudflare Acquires VoidZero to Advance JavaScript Tooling and AI-Native Web](https://blog.cloudflare.com/voidzero-joins-cloudflare/) ⭐️ 8.0/10

Cloudflare has acquired VoidZero, the company behind popular open-source JavaScript tools like Vite, and plans to integrate its team and technology into the Cloudflare Workers developer platform. The team will continue developing VoidZero's open-source projects while accelerating their integration with Cloudflare's ecosystem. This acquisition signals a major infrastructure provider's strategic move to own and deeply integrate key open-source developer tools, which could significantly influence the future of web development workflows and the JavaScript ecosystem. It highlights the growing importance of developer experience and tooling in the competitive cloud platform market. VoidZero founder Evan You, also the creator of Vue.js, stated the mission is to eliminate fragmentation and performance bottlenecks in the modern web stack. The acquisition is part of Cloudflare's broader strategy to build an 'AI-native web' and enhance its developer platform, which has also included other acquisitions like Outerbase.

hackernews · coloneltcb · Jun 4, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48398055)

**Background**: VoidZero is a company focused on building a unified JavaScript toolchain to improve developer productivity, with its most famous project being Vite, a fast and opinionated frontend build tool. Cloudflare is a major internet infrastructure and security company that also offers a developer platform called Workers, enabling serverless computing at the edge. Acquisitions of popular open-source projects by large tech companies are common but often spark debate about the projects' future independence and business model.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cloudflare.com/press/press-releases/2026/cloudflare-acquires-voidzero-to-build-the-future-of-the-ai-native-web/">Cloudflare Acquires VoidZero to Build the Future of the AI ...</a></li>
<li><a href="https://voidzero.dev/">VoidZero | The Javascript Tooling company</a></li>
<li><a href="https://github.com/voidzero-dev/">VoidZero - GitHub</a></li>

</ul>
</details>

**Discussion**: The community reaction is mixed, with significant unease about the acquisition. Some commenters express concern that open-source projects lose their independence and community trust after being acquired by a corporation, citing potential changes to roadmaps and business priorities. Others speculate about the business model of venture-funded open-source companies, questioning if acquisitions are the only viable exit, while a few note that Cloudflare's UX is often criticized and question the strategic fit.

**Tags**: `#open-source`, `#acquisition`, `#cloudflare`, `#javascript-tools`, `#developer-ecosystem`

---

<a id="item-4"></a>
## [Anthropic Reports Progress on AI Recursive Self-Improvement](https://www.anthropic.com/institute/recursive-self-improvement) ⭐️ 8.0/10

Anthropic published a detailed article outlining its progress in delegating a growing share of its AI development cycle to AI systems themselves, claiming an 8× increase in lines of code per engineer per day by the second quarter of 2026. This progress toward recursive self-improvement could dramatically accelerate AI capability development, but it also intensifies critical safety debates about alignment, control, and the potential for unintended consequences from rapidly evolving autonomous systems. Anthropic acknowledges that using 'lines of code' as a metric is imperfect and likely overstates true productivity gains, as it measures quantity over quality, yet they argue it still indicates a clear acceleration in development.

hackernews · meetpateltech · Jun 4, 16:20 · [Discussion](https://news.ycombinator.com/item?id=48400842)

**Background**: Recursive self-improvement is a concept where an AI system enhances its own capabilities, which could lead to an 'intelligence explosion' where progress becomes extremely rapid. This idea is a core concern in AI safety research, as such systems could become difficult to control or align with human goals.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self - improvement - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community discussion is highly skeptical and critical. Users point out a contradiction between Anthropic's safety claims and its pursuit of rapid self-improvement, question the lack of concrete software breakthroughs outside AI itself, and note frequent service outages and high resource usage in their own products as practical evidence against the narrative of seamless, powerful AI development.

**Tags**: `#AI Safety`, `#Recursive Self-Improvement`, `#Artificial Intelligence`, `#Software Development`, `#Ethics`

---

<a id="item-5"></a>
## [Cloudflare Reports Bot Traffic Surpasses Human Traffic for the First Time in Internet History](https://www.ithome.com/0/960/248.htm) ⭐️ 8.0/10

Cloudflare CEO Matthew Prince announced that automated bot traffic now accounts for 57.5% of web HTTP requests, surpassing human traffic at 42.5%, a milestone that arrived earlier than his predicted timeline of 2027. This represents a fundamental shift in the composition of internet traffic, driven largely by the rapid rise of AI agents, with significant implications for web security, content delivery, digital advertising, and the future architecture of the internet. The data measures HTTP request counts, not user engagement, meaning humans still dominate metrics like total time spent on apps, video streaming, and scrolling feeds, which generate far fewer page-load requests than automated agents.

rss · IT HOME · Jun 5, 02:00

**Background**: Cloudflare is a major internet infrastructure and security company that manages a significant portion of global web traffic, giving it unique visibility into traffic patterns. AI agents are software programs that autonomously perform web-based tasks like browsing, price comparison, and customer service interactions, distinct from traditional search engine crawlers or malicious bots. The crossover point where bot traffic exceeds human traffic had been previously anticipated for 2027 but was accelerated by the explosion in AI agent development and deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/bots-have-now-passed-human-traffic-online-cloudflare-boss-laments-says-agentic-traffic-wasnt-expected-to-eclipse-real-people-until-next-year">‘Bots have now passed human traffic online,’ Cloudflare boss laments — says agentic traffic wasn’t expected to eclipse real people until next year | Tom's Hardware</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/its-official-agentic-bots-surf-the-web-more-than-real-people-do/">AI Agents Now Generate More Web Traffic Than Humans - CNET</a></li>
<li><a href="https://www.cloudflare.com/products/bot-management/">Bot Management</a></li>

</ul>
</details>

**Tags**: `#Internet Trends`, `#AI Agents`, `#Web Infrastructure`, `#Bot Traffic`, `#Cloudflare`

---

<a id="item-6"></a>
## [AMD debuts Helios, its first rack-scale AI platform, to rival NVIDIA NVL72.](https://www.ithome.com/0/960/247.htm) ⭐️ 8.0/10

At Computex 2026, AMD publicly unveiled its first rack-scale AI platform, codenamed Helios, which integrates 256-core EPYC Venice processors and 72 MI455X accelerators with 31TB of HBM4 memory, targeting the high-end AI infrastructure market. This announcement directly challenges NVIDIA's dominant NVL72 platform, offering hyperscalers and enterprises an open-standard alternative for large-scale AI workloads, which could intensify competition and drive innovation in the AI infrastructure market. The Helios platform theoretically delivers up to 2900 PFLOPS of FP4 performance and features a UALink-over-Ethernet interconnect providing a 260TB/s scale-up bandwidth, positioning it slightly behind NVIDIA's VR200 NVL72 in raw compute but with a significant advantage in HBM4 memory capacity for memory-intensive tasks like large language models.

rss · IT HOME · Jun 5, 01:51

**Background**: A rack-scale AI platform is a fully integrated system designed for high-performance AI training and inference, combining compute, memory, networking, and software into a single optimized unit. UALink is an open interconnect standard designed for high-speed, low-latency communication between accelerators within a server rack. Ultra Ethernet is an emerging consortium specification aiming to enhance Ethernet for AI and high-performance computing workloads, with products like AMD's Pensando Vulcano NIC supporting it.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/blogs/2025/amd-helios-ai-rack-built-on-metas-2025-ocp-design.html">AMD Helios - AI Rack Built on Meta’s 2025 OCP Design</a></li>
<li><a href="https://ualinkconsortium.org/blog/ualink-200g-1-0-specification-overview-802/">UALink™ 200G 1.0 Specification Overview – UALink Consortium</a></li>
<li><a href="https://www.servethehome.com/amd-vulcano-800g-nic-coming-as-amd-outlines-its-ualink-and-uec-scale-plans/">AMD Vulcano 800G NIC Coming As AMD Outlines its UALink and ...</a></li>

</ul>
</details>

**Tags**: `#AI_hardware`, `#AMD`, `#GPU_accelerator`, `#data_center`, `#high_performance_computing`

---

<a id="item-7"></a>
## [Anthropic calls for global pause on advanced AI due to loss-of-control signs.](https://www.ithome.com/0/960/218.htm) ⭐️ 8.0/10

AI company Anthropic published a report stating its latest AI models are showing signs of losing human control and urged global companies to consider slowing or pausing advanced AI development. The company also announced plans to convene government officials, scientists, and competitors in the coming months to discuss a global coordination mechanism. This call highlights a growing tension between the rapid advancement of frontier AI capabilities and the urgent need for safety research and societal governance frameworks to catch up. It could significantly influence global AI policy debates and the competitive dynamics between major AI players, particularly between the U.S. and China. Anthropic frames its proposal as analogous to a 'nuclear non-proliferation treaty' but acknowledges AI is harder to monitor because development can be hidden, and companies face competitive pressure to keep advancing. The call has drawn criticism from some U.S. officials who argue the company is exaggerating risks and using safety as a competitive tactic.

rss · IT HOME · Jun 5, 01:16

**Background**: AI alignment refers to the challenge of ensuring AI systems act in accordance with human values and intentions. Frontier models like Anthropic's unreleased 'Mythos' are reported to have significantly advanced capabilities, which amplifies safety concerns. Global coordination for AI safety is increasingly discussed as a necessity to prevent a regulatory race to the bottom, but establishing enforceable international agreements remains a major challenge.

<details><summary>References</summary>
<ul>
<li><a href="https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf">Claude Mythos Preview System Card - www-cdn.anthropic.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://axis-intelligence.com/ai-safety-research-state-field-2026-analysis/">AI Safety Research 2026: Critical Inflection Point for AGI Alignment...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI policy`, `#Anthropic`, `#AI risk`, `#global AI governance`

---

<a id="item-8"></a>
## [Alipay uses AI agents to detect security flaws in other agents](https://www.infoq.cn/article/MmVSQxLc1b5BWHYRuGo4?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Alipay has developed and presented a practical system that uses AI agents to automatically detect and mitigate security vulnerabilities in other AI agents, a concept they call 'using models to manage models'. This approach addresses the critical and growing security risks associated with AI agent systems, offering an automated and scalable way to proactively find and fix vulnerabilities before they can be exploited in high-stakes environments like fintech. The system was presented at the AICon conference in Shanghai, highlighting its practical application by a major financial technology company, which adds credibility and demonstrates real-world viability.

rss · InfoQ 中文站 · Jun 4, 10:00

**Background**: AI agents are software entities that can autonomously perform tasks, make decisions, and interact with other systems or agents. As they become more prevalent, their security becomes paramount because vulnerabilities can lead to unauthorized actions, data breaches, or system manipulation. Adversarial testing and vulnerability detection are traditional cybersecurity practices now being adapted for the complex, dynamic nature of multi-agent AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.praetorian.com/blog/how-ai-agents-automate-cve-vulnerability-research/">How AI Agents Automate CVE Vulnerability Research | Praetorian</a></li>
<li><a href="https://witness.ai/blog/ai-agent-vulnerabilities/">AI Agent Vulnerabilities : Understanding Security Risks - WitnessAI</a></li>
<li><a href="https://arxiv.org/abs/2511.10949">Exposing Weak Links in Multi-Agent Systems under Adversarial ... AMACollision/readme.md at main · alanshuo123 ... - GitHub AMACollision: An advanced framework for testing autonomous ... Adversarial Decision-Making in Partially Observable Multi ... Enhancing Multi-agent System Testing with Diversity-Guided ... Adversarial-Test-Driven Multi-Agent LLM Defense: A Self ... A formal testing method for multi-agent systems using colored ...</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Agent-Based Systems`, `#Vulnerability Detection`, `#FinTech AI`

---

<a id="item-9"></a>
## [MobileGym: Browser-Based Android Simulation for GUI Agent Training](https://www.v2ex.com/t/1218107#reply0) ⭐️ 8.0/10

MobileGym is a new open-source project that provides a fully simulated Android environment running directly in the browser, complete with 28 functional apps and system-level mechanisms. The project's website has been updated to support online interaction with a GUI agent, allowing users to input an API key to watch the agent perform tasks step-by-step. This project provides a lightweight, scalable, and safe sandbox for developing and testing AI agents that interact with mobile GUIs, addressing a major bottleneck in research. Its demonstrated sim-to-real transfer capability means that agents trained efficiently in the browser can be deployed on real devices with high success rates, accelerating the path to practical automation. The system is built purely with frontend technologies (TypeScript + React), achieving an extremely low memory footprint of 400MB per instance, which supports high concurrency on servers. It includes 416 parameterized task templates for deterministic evaluation and meticulously recreates Android system mechanisms like Activity stacks and Intents.

rss · V2EX · Jun 5, 02:21

**Background**: GUI agents are AI models designed to automate interactions with graphical user interfaces on computers and phones, typically by simulating clicks and swipes. Training such agents usually requires either risky interaction with real devices or limited, non-scalable simulators. Sim2Real transfer learning is a technique where a model is first trained in a simulated environment before being fine-tuned for deployment in the real world to improve safety and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/guide/components/activities/tasks-and-back-stack">Tasks and the back stack - Android Developers</a></li>
<li><a href="https://zylos.ai/research/2026-02-08-computer-use-gui-agents/">Computer Use and GUI Agents in 2026: State of the Art</a></li>
<li><a href="https://github.com/showlab/WorldGUI">GitHub - showlab/WorldGUI: Enable AI to control your PC. This ...</a></li>

</ul>
</details>

**Discussion**: The community discussion on V2EX would likely reflect high technical interest and validation of the project's novelty, given its comprehensive feature set and open-source nature. Users may express excitement about the practical applications for AI agent research and discuss the technical challenges of accurately simulating complex mobile OS mechanisms in a browser.

**Tags**: `#open-source`, `#android-simulation`, `#GUI-agent`, `#browser-based`, `#AI-research`

---

<a id="item-10"></a>
## [ChatGPT Upgrades Memory System with Automated 'Dreaming' Process](https://openai.com/index/chatgpt-memory-dreaming/) ⭐️ 8.0/10

OpenAI is rolling out a new memory system for ChatGPT Plus and Pro users in the US that uses a background 'dreaming' process to automatically learn user preferences and update context over time. This upgrade addresses a key user pain point by moving from manual, easily outdated memory entries to automated, dynamic context retention, significantly improving the personalization and long-term utility of conversational AI. The system automatically extracts preferences and context from multi-turn conversations without requiring explicit memory commands, and it can automatically discard outdated information, such as ceasing to recommend local restaurants after a user's trip ends.

telegram · OpenAI Blog · Jun 4, 16:22

**Background**: AI memory systems aim to solve the limitation of LLMs that forget context between separate conversations. Traditional approaches often relied on explicit user commands or simple storage, which could become static and irrelevant. The new 'dreaming' technique likely refers to a background consolidation process, similar to concepts in AI research on long-term memory architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://gwern.net/ai-daydreaming">LLM Daydreaming - Gwern.net</a></li>
<li><a href="https://redis.io/blog/long-term-memory-architectures-ai-agents/">Long-Term Memory Architectures for AI Agents - Redis</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#AI_memory`, `#user_experience`, `#OpenAI`, `#conversational_AI`

---

<a id="item-11"></a>
## [The Race: AI Enthusiasts Chase Time, Skeptics Battle Entropy](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/#atom-everything) ⭐️ 8.0/10

Charity Majors published an article articulating the fundamental tension between AI enthusiasts and skeptics within engineering teams, framing it as a leadership and engineering challenge requiring designed feedback loops. This analysis provides a crucial framework for understanding the internal conflict in software organizations adopting AI, highlighting that ignoring either the threat of being left behind or the threat of degrading system quality is existential. The core problem identified is the lack of a natural feedback loop connecting the two groups, which necessitates deliberate organizational design to mend the gap in shared reality.

rss · Simon Willison · Jun 4, 23:55

**Background**: The article discusses two archetypal perspectives in modern software teams regarding AI-generated code. Enthusiasts see rapid capability gains as a competitive necessity, while skeptics worry that shipping AI code faster than it can be understood erodes trust, reliability, and institutional knowledge. This tension reflects a broader industry debate on balancing development velocity with software quality and maintainability.

**Tags**: `#AI adoption`, `#software engineering`, `#team dynamics`, `#AI skepticism`, `#development practices`

---

<a id="item-12"></a>
## [Hackers exploit Meta AI chatbot to hijack Instagram accounts via social engineering](https://www.schneier.com/blog/archives/2026/06/hacking-metas-ai-chatbot.html) ⭐️ 8.0/10

Hackers are successfully manipulating Meta's AI support chatbot to add unauthorized email addresses to victims' Instagram accounts and reset their passwords, effectively hijacking the accounts. This attack involves a step-by-step social engineering process demonstrated in a video, where the chatbot unwittingly facilitates the entire account takeover. This vulnerability exposes a critical design flaw in AI-assisted customer support systems, where the AI lacks the nuanced judgment to detect sophisticated social engineering tactics, putting millions of user accounts at risk. It highlights the urgent need for robust authentication safeguards that do not solely rely on AI interactions, especially as AI tools become more integrated into security-sensitive functions. The attack method involves using a VPN to spoof the target's location to bypass automated security checks, followed by tricking the chatbot into sending a verification code and revealing a password reset button. This demonstrates that the AI chatbot can be easily deceived into performing sensitive account operations without proper human oversight or additional verification layers.

rss · Schneier on Security · Jun 4, 11:04

**Background**: Social engineering attacks manipulate human or AI trust to extract confidential information or perform unauthorized actions, a threat that AI tools have made more scalable and effective. VPN geo-spoofing is a technique used to fake a user's geographic location, often to circumvent location-based security measures, though advanced systems can now detect such spoofing. Meta's AI support chatbot is designed to handle user queries and account management tasks, but its integration into security-critical processes without adequate safeguards creates vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/insights/generative-ai-social-engineering">Generative AI Makes Social Engineering More Dangerous—and ...</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/social-engineering/ai-social-engineering/">AI-Powered Social Engineering Attacks | CrowdStrike</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#vulnerability`, `#social engineering`, `#Meta`, `#account hijacking`

---

<a id="item-13"></a>
## [Microsoft Achieves 20-Second Qubit Coherence Breakthrough](https://hackaday.com/2026/06/04/microsoft-claims-20-second-qubits/) ⭐️ 8.0/10

Microsoft announced it has achieved qubit coherence times of 20 seconds, a major leap forward from the millisecond-scale times typical of many current quantum systems. This breakthrough addresses a critical bottleneck in quantum computing, as longer coherence times provide a much wider operational window for performing complex quantum algorithms and error correction, potentially accelerating the path to practical, fault-tolerant quantum computers. While the achievement is significant, the news report lacks specific details on the underlying qubit technology (e.g., whether it involves Microsoft's topological qubits) and the conditions under which the 20-second coherence was measured.

rss · Hackaday · Jun 5, 02:00

**Background**: Qubit coherence time is the duration a qubit can maintain its quantum state before it decays due to environmental interference, known as decoherence. Extremely short coherence times (often microseconds to milliseconds) have been a major hurdle for scaling quantum computers. Microsoft has been pursuing topological qubits, which are theorized to be inherently more stable and resistant to decoherence than other types.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quantum_computing">Quantum computing - Wikipedia</a></li>
<li><a href="https://quantum.microsoft.com/en-us/insights/education/concepts/topological-qubits">Microsoft Quantum | Topological qubits</a></li>
<li><a href="https://www.spinquanta.com/news-detail/qubit-coherence-time-a-critical-factor-in-quantum-computing">Qubit Coherence Time : A Critical Factor in Quantum Computing</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#qubit coherence`, `#Microsoft research`, `#hardware breakthrough`

---

<a id="item-14"></a>
## [Pentagon Considers Ending Anthropic Partnership Over AI Military Use Restrictions](https://t.me/zaihuapd/41777) ⭐️ 8.0/10

The U.S. Department of Defense is considering ending its partnership with Anthropic due to a fundamental disagreement over the permitted uses of the Claude AI model, specifically Anthropic's refusal to authorize its use for weapons development and autonomous warfare systems. This dispute highlights a significant and growing tension between the ethical guardrails set by leading AI companies and the expansive operational demands of national security agencies, potentially setting a precedent for how commercial AI technologies are integrated into military frameworks. Anthropic's policy strictly prohibits the use of its Claude model for large-scale surveillance and fully autonomous weapons systems, while the Pentagon seeks blanket authorization for all legally permissible military applications. This contrasts with competitors like OpenAI and Google, which have reportedly agreed to relax their usage restrictions for defense contracts.

telegram · zaihuapd · Jun 5, 01:27

**Background**: Anthropic is an AI safety company that developed the large language model Claude. The U.S. Department of Defense has been actively integrating commercial AI into military systems for applications like data analysis and decision support, often through partnerships with contractors like Palantir. The ethical debate centers on 'lethal autonomous weapons,' systems that can independently search for and engage targets without human intervention, raising profound concerns about accountability and the rules of war.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic–United_States_Department_of_Defense_dispute">Anthropic–United States Department of Defense dispute - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/technology/2026/mar/07/anthropic-claude-ai-pentagon-us-military">What does the US military’s feud with Anthropic mean for AI used in war? | AI (artificial intelligence) | The Guardian</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapon">Lethal autonomous weapon - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#military AI`, `#defense policy`, `#AI governance`, `#Anthropic`

---