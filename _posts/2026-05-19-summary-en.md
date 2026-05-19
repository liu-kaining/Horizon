---
layout: default
title: "Horizon Summary: 2026-05-19 (EN)"
date: 2026-05-19
lang: en
---

> From 202 items, 17 important content pieces were selected

---

1. [Japanese researchers achieve 112 Gbps wireless transmission at 560 GHz for 6G.](#item-1) ⭐️ 9.0/10
2. [1985 Essay Argues Programming is Theory Building](#item-2) ⭐️ 9.0/10
3. [CISA Contractor Accidentally Leaks AWS GovCloud Keys on GitHub](#item-3) ⭐️ 9.0/10
4. [China's startups advance AI brain implants from trials to real-world use](#item-4) ⭐️ 9.0/10
5. [Cursor releases Composer 2.5, its most powerful AI coding model based on Kimi K2.5.](#item-5) ⭐️ 8.0/10
6. [Google and Blackstone Launch $25B AI Cloud Company to Challenge CoreWeave](#item-6) ⭐️ 8.0/10
7. [NVIDIA Begins Shipping Custom Vera CPU for Agentic AI to Anthropic, OpenAI, SpaceXAI, and Oracle](#item-7) ⭐️ 8.0/10
8. [China launches its first supercritical CO2 geothermal heating project in Zhengzhou.](#item-8) ⭐️ 8.0/10
9. [Meta Plans Global Layoffs of 10%, About 7800 Affected by AI Strategy Shift](#item-9) ⭐️ 8.0/10
10. [Brazil Breaks Apple's App Store Wall, iOS 26.5 Adds Third-Party Store Default Option](#item-10) ⭐️ 8.0/10
11. [Xiaohongshu Presents Muse Platform Architecture for Vibe Coding](#item-11) ⭐️ 8.0/10
12. [OpenAI and Dell partner to deploy Codex in hybrid and on-premise enterprise environments.](#item-12) ⭐️ 8.0/10
13. [Guide for Fine-Tuning NVIDIA Cosmos 2.5 with LoRA/DoRA for Robotics Videos](#item-13) ⭐️ 8.0/10
14. [Deep Dive into Go's Runtime Select Statement Implementation](#item-14) ⭐️ 8.0/10
15. [Linux Kernel Swap Subsystem Receives Renewed Development Focus](#item-15) ⭐️ 8.0/10
16. [Zero-Day Exploit 'YellowKey' Bypasses Default BitLocker Encryption](#item-16) ⭐️ 8.0/10
17. [Apple Announces WWDC26 Will Open on June 8, Reveals Full Schedule](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Japanese researchers achieve 112 Gbps wireless transmission at 560 GHz for 6G.](https://www.ithome.com/0/952/053.htm) ⭐️ 9.0/10

A team from Tokushima University in Japan has demonstrated a novel photonic system using a soliton microcomb, enabling a record-breaking 112 Gbps single-channel wireless transmission in the 560 GHz terahertz band. This is the first demonstration of over 100 Gbps wireless communication above 420 GHz, overcoming a critical performance bottleneck for high-frequency electronics and establishing a key technological foundation for future 6G networks and ultra-high-speed mobile backhaul links. The system extracts two stable optical carriers from the microcomb, modulates them using QPSK and 16QAM formats, and converts them to a 560 GHz THz wave for transmission, achieving 84 Gbps and 112 Gbps respectively. The integration of a silicon nitride microring resonator with directly bonded fiber enhances robustness and miniaturization.

rss · IT HOME · May 18, 23:38

**Background**: Terahertz waves (300 GHz to 3 THz) are considered a core spectrum for 6G communications due to their ultra-high bandwidth. However, conventional electronic components suffer from severe performance degradation, such as drastically increased phase noise, above 350 GHz. A soliton microcomb is a chip-scale optical device that converts a single laser into a series of highly stable, evenly spaced optical frequency lines, which can serve as ultra-pure light sources for generating high-quality terahertz carriers.

<details><summary>References</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDdXBHTkVSR1dLYVpMYldfTHRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - Soliton microcombs for 6G transmission - Overview</a></li>
<li><a href="https://tf.nist.gov/general/pdf/2599.pdf">Phase-Noise Measurement System for the Terahertz-Band</a></li>
<li><a href="https://www.nature.com/articles/s41598-022-21590-w">Thermo-optic tuning of silicon nitride microring resonators ...</a></li>

</ul>
</details>

**Tags**: `#6G`, `#terahertz communications`, `#photonic systems`, `#wireless networks`, `#microcombs`

---

<a id="item-2"></a>
## [1985 Essay Argues Programming is Theory Building](https://gwern.net/doc/cs/algorithm/1985-naur.pdf) ⭐️ 9.0/10

提供的内容并未描述新事件或变化；它展示的是Peter Naur于1985年撰写的一篇开创性论文，该论文最近在一个专业社区中被提及和讨论。 This essay profoundly challenges the view of programming as mere coding, arguing that its core is the developer's internal mental model or theory about the program, which is crucial for effective maintenance and evolution. The essay was authored by computer scientist Peter Naur, who coined the term 'software engineering,' and it posits that the knowledge ('theory') of how a program works can only be fully transmitted through direct collaboration, not just documentation.

rss · Lobsters · May 18, 21:42

**Background**: In the 1980s, the software industry struggled with a 'software crisis,' characterized by projects failing due to poor quality and being hard to maintain. Naur's essay entered this debate by focusing on the human and cognitive aspects of programming, offering a philosophical perspective distinct from purely technical or process-oriented solutions.

**Discussion**: The essay is linked to a Lobsters community discussion where it continues to spark high-quality debate. Participants generally agree on its enduring relevance, often discussing its implications for modern practices like onboarding, knowledge transfer, and the limitations of comprehensive documentation.

**Tags**: `#software_engineering`, `#programming_philosophy`, `#computer_science_history`, `#theory_building`

---

<a id="item-3"></a>
## [CISA Contractor Accidentally Leaks AWS GovCloud Keys on GitHub](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) ⭐️ 9.0/10

A contractor for the U.S. Cybersecurity and Infrastructure Security Agency (CISA) maintained a public GitHub repository that exposed credentials for multiple highly privileged AWS GovCloud accounts and internal CISA systems until this past weekend. This breach is significant because it exposed access to AWS GovCloud, a specialized environment for U.S. government workloads, and internal CISA operational details, posing potential national security risks and representing a major operational security failure by the agency responsible for national cybersecurity. The leaked repository included files detailing how CISA internally builds, tests, and deploys software, which security experts have described as one of the most egregious government data leaks in recent history.

rss · Krebs on Security · May 18, 20:48

**Background**: AWS GovCloud (US) is an isolated Amazon Web Services region designed to host sensitive data and meet U.S. government compliance requirements, such as FedRAMP High, ITAR, and DoD SRG Level 5. GitHub's secret scanning is a free feature for public repositories that automatically detects exposed credentials and sensitive data to prevent such leaks.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>
<li><a href="https://docs.github.com/en/code-security/concepts/secret-security/about-secret-scanning">About secret scanning - GitHub Docs</a></li>
<li><a href="https://www.cisa.gov/resources-tools/resources/safe-software-deployment-how-software-manufacturers-can-ensure-reliability-customers">Safe Software Deployment: How Software Manufacturers ... - CISA</a></li>

</ul>
</details>

**Discussion**: The Lobste.rs discussion linked in the news likely features strong condemnation of the breach, with community members analyzing the operational security failures, debating the accountability of both the contractor and CISA, and discussing the broader implications for government cloud security and contractor management.

**Tags**: `#security`, `#aws`, `#data-leak`, `#government`, `#devops`

---

<a id="item-4"></a>
## [China's startups advance AI brain implants from trials to real-world use](https://www.nature.com/articles/d41586-026-01468-x) ⭐️ 9.0/10

Chinese start-up companies are intensifying their development of AI algorithms for brain-computer interfaces designed to help individuals regain mobility and communication abilities, actively moving the technology from clinical trials towards real-world deployment. This development signifies a major leap in neurotechnology, potentially offering transformative assistive solutions for people with severe motor impairments like stroke or spinal cord injury, and marking China's growing influence in a high-stakes global field. The focus is on using advanced AI algorithms to improve the efficiency of BCIs, which involve complex stages including neural data acquisition, feature extraction, and signal classification. The move towards real-world use involves creating implantable devices with ultra-low power consumption for sustained operation.

rss · Nature · May 19, 00:00

**Background**: A brain-computer interface (BCI) is a system that acquires brain signals, analyzes them, and translates them into commands for an external device, thereby creating a direct communication pathway between the brain and the outside world. AI and machine learning algorithms are critical for processing the noisy, high-dimensional neural data to accurately decode user intentions. The field has evolved from basic research to developing complex systems aimed at restoring function for individuals with neurological conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://onlinelibrary.wiley.com/doi/10.1155/2020/5762149">Deep Learning Algorithm for Brain-Computer Interface</a></li>
<li><a href="https://www.ttp.com/case-studies/ultra-low-power-machine-learning-for-implantable-medical-devices">Ultra-low power machine learning for implantable medical devices - TTP</a></li>
<li><a href="https://neuro.jmir.org/2024/1/e59556">JMIR Neurotechnology - Twenty-Five Years of AI in Neurology: The Journey of Predictive Medicine and Biological Breakthroughs</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#AI in healthcare`, `#neurotechnology`, `#medical devices`, `#China AI`

---

<a id="item-5"></a>
## [Cursor releases Composer 2.5, its most powerful AI coding model based on Kimi K2.5.](https://www.ithome.com/0/952/106.htm) ⭐️ 8.0/10

Cursor has launched Composer 2.5, its most advanced AI model for coding, which is built upon Moonshot AI's Kimi K2.5 model. The update introduces a key technical innovation: text-feedback reinforcement learning to improve stability on long-horizon tasks and better adherence to complex instructions. This release represents a significant step for AI-assisted development by tackling the persistent challenge of maintaining coherence and accuracy over long coding tasks. The use of a novel training methodology could set a new standard for how developer tools learn from complex interactions, directly benefiting programmers who rely on AI for large-scale code generation and editing. The model's key innovation is a text-feedback reinforcement learning approach that inserts corrective feedback at the specific point of error during a long roll-out, using distillation to correct mistakes in tool use or style. The training also expanded synthetic task scale by 25x and incorporates a method of deleting testable functions from real codebases and rewarding the model for successfully restoring them.

rss · IT HOME · May 19, 02:06

**Background**: Kimi K2.5 is a large open-source multimodal model from Moonshot AI (月之暗面) with 1 trillion total parameters and 32 billion active parameters, designed for complex real-world tasks. Text-feedback reinforcement learning is an advanced technique where a model is trained using corrective textual critiques rather than just a single scalar reward, allowing for more nuanced error correction in multi-step processes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k2-5">Kimi K 2 . 5 Tech Blog: Visual Agentic Intelligence</a></li>
<li><a href="https://www.kimi.com/ai-models/kimi-k2-5">Kimi K 2 . 5 | Open Visual Agentic Model for Real Work</a></li>

</ul>
</details>

**Tags**: `#AI-coding`, `#language-models`, `#reinforcement-learning`, `#developer-tools`, `#Kimi`

---

<a id="item-6"></a>
## [Google and Blackstone Launch $25B AI Cloud Company to Challenge CoreWeave](https://www.ithome.com/0/952/097.htm) ⭐️ 8.0/10

Google and Blackstone are forming a new AI cloud company, with Blackstone initially investing $5 billion in equity and the total compute investment expected to reach approximately $25 billion. The new entity aims to leverage Google's custom TPU chips and cloud capabilities to directly compete with AI infrastructure providers like CoreWeave, targeting a capacity of 500 megawatts by 2027. This partnership represents Google's largest-ever effort to commercialize its proprietary TPU chips externally, significantly intensifying competition in the high-stakes AI infrastructure and cloud computing market. It also underscores the massive capital flowing into AI infrastructure, with major players like Blackstone positioning themselves as key investors alongside tech giants. The company plans to secure data center sites, some of which are already under construction, to support its expansion to 500 MW by 2027. Blackstone is one of the most active investors in AI infrastructure, claiming over $150 billion in data center assets and having previously invested in CoreWeave, Anthropic, and OpenAI.

rss · IT HOME · May 19, 01:52

**Background**: Google's Tensor Processing Units (TPUs) are custom-designed AI accelerator chips, with the latest eighth-generation models (TPU 8t and 8i) recently announced, featuring separate designs optimized for training and inference. CoreWeave is a fast-growing cloud computing company that provides GPU-accelerated infrastructure specifically for AI and machine learning workloads, representing a new class of specialized 'AI cloud' providers. Blackstone is a global investment firm that has aggressively expanded into digital infrastructure, viewing data centers as its 'highest conviction theme' and acquiring major providers like QTS Realty Trust.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.blackstone.com/investing-in-ai/">Investing in AI - Blackstone</a></li>
<li><a href="https://decodingthefutureresearch.substack.com/p/coreweave-part-1-competitive-landscape">An overview of CoreWeave: Part 1 (Competitive Landscape ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#cloud computing`, `#investment`, `#Google TPU`, `#data centers`

---

<a id="item-7"></a>
## [NVIDIA Begins Shipping Custom Vera CPU for Agentic AI to Anthropic, OpenAI, SpaceXAI, and Oracle](https://www.ithome.com/0/952/080.htm) ⭐️ 8.0/10

NVIDIA has officially begun shipping its first custom Vera CPU, designed specifically for Agentic AI workloads, with initial deliveries made to Anthropic, OpenAI, SpaceXAI, and Oracle Cloud Infrastructure. The company's VP Ian Buck personally delivered the first systems to these companies, marking the processor's transition into mass production. This shipment marks NVIDIA's entry into the custom CPU market with a chip specifically architected for the emerging demands of agentic AI, positioning it as a critical component in next-generation AI factories alongside its GPUs. It signals a major shift where specialized CPUs become essential for orchestrating complex, autonomous AI agent workflows, moving beyond traditional GPU-centric processing. The Vera CPU features 88 custom-designed 'Olympus' cores based on Arm v9.2-A architecture, 1.5 TB of system memory, 1.2 TB/s memory bandwidth using LPDDR5X, and a 1.8 TB/s NVLink-C2C interconnect for coherent memory with GPUs. Oracle plans to deploy 'hundreds of thousands' of Vera CPUs starting in 2026, and NVIDIA expects it to create a multi-billion dollar new business line, both integrated in the Vera Rubin NVL72 platform and as a standalone product.

rss · IT HOME · May 19, 01:05

**Background**: Agentic AI refers to AI systems that can act autonomously to achieve goals, requiring them to write code, use tools, and manage complex multi-step workflows, which places heavy demands on the CPU for orchestration and data movement rather than just raw GPU compute. NVIDIA's Vera CPU is its second-generation data center CPU following Grace, but is its first to use a fully custom-designed CPU core (Olympus) instead of licensed Arm cores, aiming for extreme single-threaded performance needed to keep pace with fast GPUs in AI factories.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-cpu/">Next Gen Data Center CPU | NVIDIA Vera CPU</a></li>
<li><a href="https://www.servethehome.com/nvidias-vera-cpu-in-detail-high-perf-chip-takes-aim-at-broader-ai-server-market/">NVIDIA’s Vera CPU in Detail: High Perf Chip Takes... - ServeTheHome</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-vera-cpu-delivers-high-performance-bandwidth-and-efficiency-for-ai-factories/">NVIDIA Vera CPU Delivers High Performance, Bandwidth, and...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#CPU`, `#AI hardware`, `#Agentic AI`, `#industry announcement`

---

<a id="item-8"></a>
## [China launches its first supercritical CO2 geothermal heating project in Zhengzhou.](https://www.ithome.com/0/952/058.htm) ⭐️ 8.0/10

China has put into operation its first commercial geothermal heating project using supercritical carbon dioxide as the heat transfer fluid in Zhengzhou, replacing water. The project, built by China Huaneng Group, uses a closed-loop system reaching a depth of 2500 meters and achieves approximately 20% higher heat extraction efficiency compared to traditional water-based methods. This breakthrough demonstrates a viable commercial application of supercritical CO2 geothermal technology, significantly improving heating efficiency while eliminating water consumption and subsurface environmental disruption. It provides a scalable and clean model for developing deep geothermal resources in China and beyond, contributing to renewable heating goals. The technology reportedly increases heat extraction capacity by about 20% and reduces unit heating energy consumption by 10%, while the process avoids extracting groundwater or contaminating geological formations. The project can supply heating for over 18,000 square meters of residential space and is estimated to save 288 tons of standard coal and reduce CO2 emissions by 750 tons annually.

rss · IT HOME · May 18, 23:56

**Background**: Supercritical carbon dioxide (sCO2) is a state of CO2 above its critical temperature and pressure, where it exhibits gas-like viscosity and liquid-like density, making it an excellent heat transfer medium. Closed-loop geothermal systems, unlike traditional ones, circulate a working fluid through sealed wellbores without direct contact with subsurface rock or water, preventing resource depletion and environmental issues. While sCO2 has been studied for enhanced geothermal systems (EGS) for its potential to improve efficiency and enable carbon sequestration, this project marks a significant step from research to commercial heating application.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S1755008424001017">A literature review of using supercritical CO2 for geothermal energy extraction: Potential, methods, challenges, and perspectives - ScienceDirect</a></li>
<li><a href="https://en.wikipedia.org/wiki/Closed-loop_geothermal">Closed-loop geothermal - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1364032125008500">Closed-loop geothermal systems: Critical review of ...</a></li>

</ul>
</details>

**Tags**: `#renewable energy`, `#geothermal`, `#supercritical CO2`, `#energy efficiency`, `#clean technology`

---

<a id="item-9"></a>
## [Meta Plans Global Layoffs of 10%, About 7800 Affected by AI Strategy Shift](https://www.ithome.com/0/952/056.htm) ⭐️ 8.0/10

Meta announced a plan to lay off 10% of its global workforce, affecting approximately 7800 employees, starting on May 20, as part of a major restructuring to prioritize AI development and restructure operations. This significant workforce reduction and strategic pivot to AI reflect a broader industry trend where major tech companies are reallocating resources from traditional roles to focus on artificial intelligence, signaling a potential shift in employment patterns within the tech sector. Meta plans to transfer 7000 employees to new AI-related projects, cancel some management positions, and has also closed 6000 open roles; layoff notifications will be sent in three batches globally, and internal employee resistance has emerged through protests and a petition against AI surveillance tools.

rss · IT HOME · May 18, 23:48

**Background**: Meta is intensifying investments in AI agents, which are autonomous systems designed to execute complex tasks with minimal human intervention, as part of its 'AI for Work' initiative. This restructuring aligns with efforts to develop AI agents for product integration and internal workflows, exemplified by teams like Applied AI Engineering (AAI) and Agent Transformation Accelerator (ATA) XFN.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thenews.com.pk/latest/1403015-meta-outlines-sweeping-layoffs-amid-ai-driven-restructuring-in-internal-memo">Meta outlines sweeping layoffs amid AI-driven restructuring in internal memo</a></li>
<li><a href="https://www.thestar.com.my/tech/tech-news/2026/05/19/exclusive-meta-lays-out-plans-for-may-20-layoffs-restructuring-internal-document-says">Exclusive-Meta lays out details of May 20 restructuring in internal document | The Star</a></li>
<li><a href="https://www.okintdigital.com/en/insights/ai-agents-enterprise-automation">AI Agents in the Enterprise : Beyond Chatbots to... | OKINT Digital</a></li>

</ul>
</details>

**Discussion**: Internal employee resistance has surfaced, with over 1000 workers signing a petition against installing mouse-tracking software for AI training, and some using elephant emojis on Workplace to highlight the 'elephant in the room' regarding layoffs; in the UK, Meta employees are organizing unionization efforts with the United Tech and Allied Workers union, criticizing management for imposing costly AI strategies that lead to job losses.

**Tags**: `#Meta`, `#layoffs`, `#AI strategy`, `#corporate restructuring`, `#tech industry`

---

<a id="item-10"></a>
## [Brazil Breaks Apple's App Store Wall, iOS 26.5 Adds Third-Party Store Default Option](https://www.ithome.com/0/952/051.htm) ⭐️ 8.0/10

Apple is building a new 'App Installation' setting in iOS 26.5, discovered in the RC code, which allows users in Brazil to choose and set a third-party app store as their default marketplace instead of the App Store. This change, driven by a 2025 antitrust settlement with Brazil's CADE, marks a significant regulatory victory that forces Apple to open its closed ecosystem in a major market, potentially setting a precedent for similar actions worldwide. The new interface shows that setting a default store will affect recommendations in Spotlight, Siri, and Safari; Apple has a deadline of up to 105 days from the December 2025 settlement to implement these changes, facing substantial fines for non-compliance.

rss · IT HOME · May 18, 23:27

**Background**: Sideloading refers to installing applications on a device from sources outside the official app store, a practice Apple has historically restricted on iOS for security and control. The change in Brazil results from a settlement between Apple and Brazil's antitrust regulator CADE, ending a three-year investigation that began in 2022. This forces Apple to allow third-party payment systems and alternative app marketplaces, mirroring regulatory pressure seen in other regions like the European Union.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2025/12/24/new-app-store-fee-structure-in-brazil/">Apple to Introduce New App Store Fee Structure in Brazil Following Antitrust Settlement - MacRumors</a></li>
<li><a href="https://9to5mac.com/2025/12/23/apple-settles-brazilian-antitrust-case-with-app-store-policy-overhaul/">Apple settles Brazilian antitrust case with App Store policy overhaul - 9to5Mac</a></li>
<li><a href="https://www.reuters.com/legal/litigation/apple-allow-third-party-app-stores-brazil-settle-ios-case-with-regulator-2025-12-23/">Apple to allow third-party app stores in Brazil to settle iOS case with regulator | Reuters</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#app-store`, `#iOS`, `#platform-ecosystem`, `#Brazil`

---

<a id="item-11"></a>
## [Xiaohongshu Presents Muse Platform Architecture for Vibe Coding](https://www.infoq.cn/article/0cMu1bsEszkZDf09OP2M?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Xiaohongshu shared a technical case study at AICon Shanghai detailing the high-availability, human-AI collaborative agentic system architecture of their Muse vibe coding platform. This provides a rare production-level insight into engineering a complex, collaborative AI system at scale, offering valuable lessons for building robust, human-in-the-loop agentic platforms. The architecture focuses on high availability and designing for human-AI collaboration within a vibe coding context, where users build applications using natural language prompts.

rss · InfoQ 中文站 · May 19, 10:00

**Background**: Vibe coding platforms enable users to build software by describing their intent in natural language, with the system handling code generation, testing, and deployment. An agentic system typically involves autonomous or semi-autonomous AI agents that can plan, use tools, and execute multi-step tasks. High-availability design ensures the system remains operational and reliable, which is critical for production environments.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">AI Vibe Coding Platform · Cloudflare Reference Architecture docs</a></li>
<li><a href="https://cloud.google.com/discover/what-is-vibe-coding">Vibe Coding Explained: Tools and Guides | Google Cloud</a></li>
<li><a href="https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system">Choose a design pattern for your agentic AI system | Cloud ...</a></li>

</ul>
</details>

**Tags**: `#AI_system_architecture`, `#agentic_systems`, `#high_availability`, `#human_AI_collaboration`, `#production_engineering`

---

<a id="item-12"></a>
## [OpenAI and Dell partner to deploy Codex in hybrid and on-premise enterprise environments.](https://openai.com/index/dell-codex-enterprise-partnership) ⭐️ 8.0/10

OpenAI and Dell have formed a partnership to deploy OpenAI's Codex AI coding agents in hybrid and on-premise enterprise environments, aiming to securely integrate them into corporate data and workflows. This partnership is a major strategic move to bring advanced AI coding capabilities into secure, on-premise enterprise settings, which is crucial for adoption in sensitive industries like finance and healthcare that handle regulated data. OpenAI Codex is a suite of AI-driven coding agents designed to automate software engineering tasks, and this partnership leverages Dell's infrastructure to support deployment where data resides, potentially reducing latency and enhancing data sovereignty for enterprises.

rss · OpenAI Blog · May 18, 10:00

**Background**: OpenAI Codex refers to a suite of AI coding agents developed by OpenAI that can assist or automate software development tasks. Hybrid and on-premise deployments are critical for enterprises that need to keep sensitive data within their own infrastructure for security, compliance, or latency reasons, rather than relying solely on public cloud services.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>
<li><a href="https://infohub.delltechnologies.com/en-us/p/from-hybrid-data-to-ai-ready-workflows/">From Hybrid Data to AI-Ready Workflows | Dell Technologies ...</a></li>

</ul>
</details>

**Tags**: `#enterprise AI`, `#cloud computing`, `#software development`, `#partnerships`, `#on-premise`

---

<a id="item-13"></a>
## [Guide for Fine-Tuning NVIDIA Cosmos 2.5 with LoRA/DoRA for Robotics Videos](https://huggingface.co/blog/nvidia/cosmos-fine-tuning-for-robot-video-generation) ⭐️ 8.0/10

Hugging Face published a tutorial on efficiently fine-tuning NVIDIA's Cosmos Predict 2.5 world foundation model using parameter-efficient LoRA and DoRA techniques to specialize it for generating robotic manipulation videos. This provides a practical pathway for robotics researchers to adapt a state-of-the-art video generation model for their domain without the massive cost of full model retraining, accelerating the development of simulation and data generation for physical AI. The guide focuses on Cosmos Predict 2.5, a flow-based model unifying Text2World, Image2World, and Video2World generation, and demonstrates the use of DoRA, which decomposes weights into magnitude and direction for finer control, as an improved alternative to standard LoRA fine-tuning.

rss · Hugging Face Blog · May 18, 16:00

**Background**: NVIDIA Cosmos Predict 2.5 is a world foundation model designed to simulate and predict future states of the world as video, useful for training autonomous systems. LoRA (Low-Rank Adaptation) is a popular parameter-efficient fine-tuning method that injects trainable low-rank matrices into model layers. DoRA (Weight-Decomposed Low-Rank Adaptation) is an advanced variant from NVIDIA that decomposes pre-trained weights to achieve better performance than LoRA while remaining parameter-efficient.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/nvidia-cosmos/cosmos-predict2.5">nvidia-cosmos/cosmos-predict2.5 - GitHub</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-dora-a-high-performing-alternative-to-lora-for-fine-tuning/">Introducing DoRA, a High-Performing Alternative to LoRA for ...</a></li>
<li><a href="https://arxiv.org/abs/2402.09353">[2402.09353] DoRA: Weight-Decomposed Low-Rank Adaptation Fine-tuning Guide | NVlabs/DoRA | DeepWiki Implementing DoRA (an Improved LoRA) from Scratch Advanced LLM Fine-Tuning: LoRa, QLora, Dora & Lora+ ... Improving LoRA: Implementing Weight-Decomposed Low-Rank ...</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#video generation`, `#robotics`, `#fine-tuning`, `#LoRA`

---

<a id="item-14"></a>
## [Deep Dive into Go's Runtime Select Statement Implementation](https://internals-for-interns.com/posts/go-runtime-select/) ⭐️ 8.0/10

A detailed technical analysis has been published, explaining how Go's select statement is implemented within the runtime, specifically detailing its code path and internal data structures like scase and sudog. Understanding select's implementation provides critical insights for Go developers working on high-performance concurrent systems, helping them write more efficient code and debug complex channel interactions by knowing the underlying mechanics. The implementation involves the IR stage converting the select statement into runtime calls, handling cases with zero, one, or multiple channel operations differently, and utilizing key runtime structures like scase for case descriptors and sudog for waiting goroutines.

rss · Lobsters · May 18, 16:05

**Background**: The select statement in Go is a control structure that allows a goroutine to wait on multiple channel operations simultaneously, proceeding with whichever operation is ready first. It is a core concurrency primitive built on Go's channels, which are typed conduits for communication between goroutines following the CSP model. The Go runtime scheduler manages goroutine execution across OS threads, and select interacts closely with this scheduler to manage blocked goroutines waiting on channel events.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.kassiansun.com/posts/go-source-code-part-16/">Go Runtime Implementations: Select | Kassian Sun</a></li>
<li><a href="https://antonz.org/go-concurrency/internals/">Gist of Go: Concurrency internals</a></li>
<li><a href="https://go.googlesource.com/go/+/ba2835db6ce72dc941ee8a1492c49176ed3bf9f7/src/runtime/HACKING.md">Scheduler structures - go.googlesource.com</a></li>

</ul>
</details>

**Discussion**: The linked discussion on Lobste.rs likely contains technical commentary from systems programmers and Go runtime enthusiasts, focusing on the correctness, performance implications, and alternative approaches to the described implementation.

**Tags**: `#go`, `#runtime`, `#concurrency`, `#internals`, `#systems-programming`

---

<a id="item-15"></a>
## [Linux Kernel Swap Subsystem Receives Renewed Development Focus](https://lwn.net/Articles/1072657/) ⭐️ 8.0/10

The Linux kernel's swap subsystem was the topic of three dedicated sessions at the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit, focusing on performance improvements, maintainability, and making swapping friendlier to SSDs. This renewed development focus addresses a long-neglected core subsystem critical for memory management, which could lead to better system performance and longevity of solid-state storage devices in Linux environments. The sessions discussed swapping's impact on SSD wear, with one session specifically shared with the storage track to design more flash-friendly swap mechanisms, acknowledging the different write patterns and wear characteristics of solid-state drives.

rss · LWN.net · May 18, 13:16

**Background**: The swap subsystem manages anonymous memory pages by moving them to secondary storage (like disk or SSD) when physical RAM is under pressure. Swapping is crucial for allowing systems to run more applications than physical memory can hold, but it can cause performance issues and accelerate SSD wear due to frequent write operations.

<details><summary>References</summary>
<ul>
<li><a href="https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/linux-stable/+/v4.4.101/include/linux/swapops.h">include/ linux / swapops .h - pub/scm/ linux / kernel /git/stable/ linux -stable...</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#memory-management`, `#swap`, `#systems-programming`, `#storage`

---

<a id="item-16"></a>
## [Zero-Day Exploit 'YellowKey' Bypasses Default BitLocker Encryption](https://www.schneier.com/blog/archives/2026/05/zero-day-exploit-against-windows-bitlocker.html) ⭐️ 8.0/10

A researcher published a zero-day exploit named YellowKey that reliably bypasses the default Windows 11 BitLocker encryption, which is configured to use the Trusted Platform Module (TPM) for key storage. The exploit requires physical access to the target computer to function. This is significant because BitLocker is a mandatory full-disk encryption standard for many organizations, including those working with governments, and the exploit undermines its core security promise. It highlights that even robust encryption technologies relying on dedicated hardware can be defeated if the system's recovery environment contains flaws. The vulnerability resides within the Windows Recovery Environment (WinRE) and specifically impacts Windows 11, Windows Server 2022, and Windows Server 2025, but not older systems like Windows 10. The exploit leverages legacy code left in the WinRE to bypass the TPM-based protections and decrypt the disk in minutes.

rss · Schneier on Security · May 18, 11:08

**Background**: BitLocker is Microsoft's full-volume encryption feature designed to protect data on disk by requiring authentication before the operating system loads. In a default configuration, the encryption key is stored and protected by a Trusted Platform Module (TPM), a dedicated security chip that safeguards cryptographic keys. The Windows Recovery Environment (WinRE) is a separate, minimal operating system used for troubleshooting and repair, which must maintain access to encrypted drives during its operations.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html">Windows Zero-Days Expose BitLocker Bypasses And CTFMON ...</a></li>
<li><a href="https://www.notebookcheck.net/YellowKey-fully-bypasses-Microsoft-BitLocker-encryption-on-affected-Windows-PCs-Bitcoins-personal-data-at-risk.1296120.0.html">YellowKey fully bypasses Microsoft BitLocker encryption on ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview">Trusted Platform Module Technology Overview | Microsoft Learn</a></li>

</ul>
</details>

**Discussion**: The news has drawn attention from security professionals, with some noting the inherent tension between the need for a recovery environment and strong encryption. Discussions often emphasize that this is a local attack requiring physical access, which limits its scope compared to remote exploits, but it remains a serious concern for protecting lost or stolen devices.

**Tags**: `#security`, `#encryption`, `#vulnerability`, `#BitLocker`, `#Windows`

---

<a id="item-17"></a>
## [Apple Announces WWDC26 Will Open on June 8, Reveals Full Schedule](https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/) ⭐️ 8.0/10

Apple officially announced that its Worldwide Developers Conference (WWDC) 2026 will kick off on June 8 at 10:00 AM PDT with a keynote, and detailed the full week-long schedule including the Platforms State of the Union, over 100 technical sessions, and interactive Group Labs. As Apple's premier annual event, WWDC sets the strategic direction for its software platforms, where new versions of iOS, macOS, and other operating systems are unveiled, directly impacting millions of developers and billions of users worldwide. The Platforms State of the Union, a deep technical session, will stream immediately after the keynote on June 8, and the conference will feature the annual Apple Design Awards, with 36 finalists already announced, as well as the Swift Student Challenge, where 350 winners, including 50 distinguished attendees, have been selected.

telegram · zaihuapd · May 19, 01:07

**Background**: The Worldwide Developers Conference (WWDC) is Apple's annual multi-day event for software developers, typically featuring the unveiling of major updates to its operating systems. The 'Platforms State of the Union' is a follow-up session to the keynote that provides developers with in-depth technical details about new APIs, tools, and technologies. The Swift Student Challenge is a global coding competition organized by Apple to encourage students to build apps using the Swift programming language.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/05/18/apple-sends-invites-for-wwdc26-keynote-unveils-schedule/">Apple sends invites for WWDC26 keynote, iOS 27 and more ...</a></li>
<li><a href="https://developer.apple.com/design/awards/">Apple Design Awards - 2026 finalists - Apple Developer</a></li>
<li><a href="https://grokipedia.com/page/Swift_Student_Challenge">Swift Student Challenge</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#WWDC`, `#Software Development`, `#Industry News`

---