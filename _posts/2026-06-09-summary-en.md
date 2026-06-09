---
layout: default
title: "Horizon Summary: 2026-06-09 (EN)"
date: 2026-06-09
lang: en
---

> From 197 items, 12 important content pieces were selected

---

1. [Apple Introduces Core AI, a New Framework for On-Device Model Execution](#item-1) ⭐️ 9.0/10
2. [Apple reveals new AI architecture integrating Google Gemini models with a privacy-first framework.](#item-2) ⭐️ 8.0/10
3. [Cadence and NVIDIA launch industry's first fully autonomous AI chip design engineer](#item-3) ⭐️ 8.0/10
4. [OpenAI files for IPO as Altman's Worldcoin eye-scan firm cuts jobs over revenue issues.](#item-4) ⭐️ 8.0/10
5. [Finnish startup Donut Lab's 'revolutionary' sodium-ion solid-state battery proven to be a fraud, actually a lithium-ion battery.](#item-5) ⭐️ 8.0/10
6. [Meta removes hidden face recognition code from smart glasses app after discovery](#item-6) ⭐️ 8.0/10
7. [Apple WWDC26: New OSes, Siri AI, and Tim Cook's Final Keynote](#item-7) ⭐️ 8.0/10
8. [Alist UI suspected of hijack by compromised Polyfill.io script](#item-8) ⭐️ 8.0/10
9. [OpenAI confidentially submits draft S-1 filing to SEC for potential IPO](#item-9) ⭐️ 8.0/10
10. [Apple Announces WWDC 2026 Event](#item-10) ⭐️ 8.0/10
11. [Critical Zcash Privacy Bug Found by AI, Enabling Counterfeit Coins](#item-11) ⭐️ 8.0/10
12. [Anthropic confidentially files S-1 for potential IPO after $965B valuation](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Apple Introduces Core AI, a New Framework for On-Device Model Execution](https://developer.apple.com/documentation/coreai/) ⭐️ 9.0/10

Apple has introduced Core AI, a new developer framework designed to convert and run AI models across the CPU, GPU, and Neural Engine on Apple devices. This framework, announced at WWDC 2026, represents a significant evolution from the previous CoreML framework. This signals a major industry shift toward on-device AI processing, which can reduce reliance on cloud services, enhance user privacy, and lower operational costs for developers. The move may disrupt the business models of AI companies that depend on cloud-based API services. Core AI allows developers to convert models from frameworks like PyTorch into an optimized format that automatically utilizes the best available hardware on the device. The framework is part of Apple's broader push to rebrand its machine learning efforts as broader 'AI,' as indicated by the transition from the CoreML name.

hackernews · hmokiguess · Jun 8, 18:47 · [Discussion](https://news.ycombinator.com/item?id=48449665)

**Background**: Apple's Neural Engine is a dedicated hardware accelerator within Apple Silicon chips (A-series and M-series) designed to efficiently handle machine learning tasks. Core ML has been Apple's existing framework for integrating trained models into apps, primarily optimized for inference on Apple hardware. The shift to Core AI suggests a modernization to support a wider array of AI workloads and more seamless cross-device hardware utilization.

<details><summary>References</summary>
<ul>
<li><a href="https://letsdatascience.com/news/apple-replaces-core-ml-with-core-ai-3eaa8e92">Apple Replaces Core ML With Core AI | Let's Data Science</a></li>
<li><a href="https://dev.to/arshtechpro/core-ml-vs-foundation-models-which-should-you-use-3jo0">Core ML vs Foundation Models: Which Should You Use? - DEV Community</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Neural_Engine">Apple Neural Engine</a></li>

</ul>
</details>

**Discussion**: The community discussion shows high engagement, with developers sharing WWDC session links for Core AI and debating whether it fully replaces CoreML. Many comments express excitement about on-device AI enabling 'infinite tokens' without monthly fees, while some view this as a strategic move that could undermine the moats of cloud-based AI companies.

**Tags**: `#apple`, `#on-device-ai`, `#coreml`, `#machine-learning`, `#developer-frameworks`

---

<a id="item-2"></a>
## [Apple reveals new AI architecture integrating Google Gemini models with a privacy-first framework.](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/) ⭐️ 8.0/10

Apple has announced a new AI architecture that integrates Google's Gemini models within its privacy-focused Apple Intelligence system, using a combination of on-device processing and a new Private Cloud Compute (PCC) framework for cloud-based tasks. This partnership represents a significant strategic move, allowing Apple to rapidly deploy advanced AI capabilities from a leading model provider while attempting to uphold its strong privacy promises, potentially reshaping the competitive dynamics between major tech ecosystems. The core technical challenge lies in ensuring that requests routed to Google's models via Apple's Private Cloud Compute do not leak user context or identifiable data to Google, a point of skepticism among observers and a key differentiator for Apple's claimed privacy guarantees.

hackernews · unclefuzzy · Jun 8, 19:14 · [Discussion](https://news.ycombinator.com/item?id=48450142)

**Background**: Apple Intelligence is Apple's umbrella term for its on-device and cloud-based AI features. Private Cloud Compute (PCC) is a cloud architecture designed by Apple to process sensitive AI tasks remotely with security and privacy claims that are intended to be verifiable. Google Gemini is a family of large language models developed by Google DeepMind, competing with models from OpenAI, Anthropic, and others.

<details><summary>References</summary>
<ul>
<li><a href="https://security.apple.com/blog/private-cloud-compute/">Private Cloud Compute: A new frontier for AI privacy in the cloud - Apple Security Research</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>
<li><a href="https://security.apple.com/documentation/private-cloud-compute">Private Cloud Compute Security Guide | Documentation</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights skepticism about whether Apple can truly prevent user data leakage to Google when using its models, with users questioning the technical feasibility of the privacy claims. There is also a significant discussion about EU regulation, with some hoping it will force Apple to allow user choice of third-party AI models, while others note the service's non-launch in the EU as a potential red flag.

**Tags**: `#Apple`, `#Google`, `#AI architecture`, `#privacy`, `#on-device AI`

---

<a id="item-3"></a>
## [Cadence and NVIDIA launch industry's first fully autonomous AI chip design engineer](https://www.ithome.com/0/961/795.htm) ⭐️ 8.0/10

At COMPUTEX 2026, Cadence announced that its ChipStack AI Super Agent, built with NVIDIA's support, has achieved Level-5 autonomy, making it the industry's first fully autonomous AI virtual engineer for chip design. The agent can independently execute complex design and verification workflows without step-by-step prompts. This represents a significant leap in EDA automation, moving AI from assisting engineers to potentially acting as an autonomous engineer, which could drastically accelerate chip design cycles and allow senior engineers to focus on more challenging, high-level problems. It signals a major shift toward fully autonomous engineering agents in the semiconductor industry. The agent is built on Cadence's AI-driven EDA portfolio and NVIDIA's Nemotron models, running within the NVIDIA OpenShell sandbox for security. It can evaluate intermediate results and iterate across tasks like RTL generation, verification, simulation, and debugging until the design goal is met, though engineers retain the ability to inspect and guide the process.

rss · IT HOME · Jun 9, 02:28

**Background**: In the context of AI agents, Level-5 autonomy refers to a system that can fully manage itself and make independent decisions without human intervention, which is a pinnacle goal for many autonomous systems. The NVIDIA Nemotron model family uses a hybrid Mixture-of-Experts (MoE) architecture designed for high throughput, and OpenShell provides sandboxed, policy-controlled execution environments to ensure AI agents operate safely without risking data leakage or unauthorized actions.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@angadi.saa/ai-the-5-levels-of-agentic-ai-systems-29cf46e75982">AI : The 5 Levels of Agentic AI Systems | by Shankar Angadi | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nemotron">Nemotron - Wikipedia</a></li>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#chip-design`, `#EDA`, `#automation`, `#NVIDIA`

---

<a id="item-4"></a>
## [OpenAI files for IPO as Altman's Worldcoin eye-scan firm cuts jobs over revenue issues.](https://www.ithome.com/0/961/792.htm) ⭐️ 8.0/10

OpenAI has confidentially filed for an initial public offering (IPO), marking a potentially landmark event for the AI industry. Simultaneously, Sam Altman's other venture, Tools for Humanity, known for the Worldcoin iris-scanning project, is undergoing layoffs due to significant revenue challenges. The IPO filing signals OpenAI's transition into a major publicly traded entity, which could solidify its market leadership and provide capital for further AI development. The layoffs at Tools for Humanity highlight the financial pressures and execution challenges facing ambitious but unproven biometric-crypto ventures, reflecting broader skepticism about their business models. Tools for Humanity had a post-money valuation of $2.5 billion, backed by prominent blockchain investors like Andreessen Horowitz and Bain Capital. The company faces significant regulatory and ethical pushback internationally, including operational bans in Kenya and fines in South Korea, over privacy concerns related to its iris-scan data collection.

rss · IT HOME · Jun 9, 02:19

**Background**: Worldcoin, now part of the World Network, is a project that uses specialized Orb hardware to scan a person's iris to create a unique digital identity on the blockchain. This biometric verification is intended to prove personhood and distinguish humans from bots, supporting its associated Worldcoin (WLD) cryptocurrency. The project has attracted both significant venture capital investment and substantial public and regulatory scrutiny due to its data collection practices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_(blockchain)">World (blockchain) - Wikipedia</a></li>
<li><a href="https://arstechnica.com/tech-policy/2023/05/openai-ceo-raises-115m-for-crypto-company-that-scans-peoples-eyeballs/">OpenAI CEO raises $115M for crypto company that scans ...</a></li>
<li><a href="https://financefeeds.com/worldcoin-sells-135m-in-tokens-to-andreessen-horowitz-bain-capital-crypto/">Worldcoin Sells $135M In Tokens To Andreessen Horowitz , Bain ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#IPO`, `#AI`, `#Worldcoin`, `#Tech Industry`

---

<a id="item-5"></a>
## [Finnish startup Donut Lab's 'revolutionary' sodium-ion solid-state battery proven to be a fraud, actually a lithium-ion battery.](https://www.ithome.com/0/961/748.htm) ⭐️ 8.0/10

A comprehensive investigation by over 20 independent battery experts conclusively proved that the battery marketed by Finnish startup Donut Lab as a revolutionary sodium-ion solid-state battery is a conventional lithium-ion battery. This case exposes a significant technology fraud in the clean energy sector, affecting over 1,300 small investors who contributed approximately $25 million, and risks undermining public trust in legitimate solid-state battery development efforts. Key evidence included the battery's voltage curve matching that of a high-nickel lithium-ion battery and its expansion profile showing a distinct inflection point characteristic of graphite anodes used in lithium-ion batteries, not sodium-ion ones.

rss · IT HOME · Jun 9, 01:12

**Background**: Sodium-ion batteries are a promising alternative to lithium-ion batteries due to sodium's abundance, but they have different electrochemical characteristics, such as lower operating voltages. Solid-state batteries, which use a solid electrolyte instead of a liquid one, are a major area of research for their potential safety and energy density improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sodium-ion_battery">Sodium-ion battery - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s42154-019-00080-2">A Comparative Study of Charging Voltage Curve Analysis and ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6854841/">Methods and Protocols for Reliable Electrochemical Testing in Post-Li Batteries (Na, K, Mg, and Ca) - PMC</a></li>

</ul>
</details>

**Tags**: `#battery technology`, `#fraud`, `#startup scandal`, `#sodium-ion battery`, `#lithium-ion battery`

---

<a id="item-6"></a>
## [Meta removes hidden face recognition code from smart glasses app after discovery](https://www.ithome.com/0/961/724.htm) ⭐️ 8.0/10

Meta was found to have embedded a dormant facial recognition feature, internally called 'NameTag', in its Ray-Ban smart glasses companion app. The company removed this code in an update just one day after it was publicly reported by Wired. This incident raises significant privacy and ethical concerns, as the code was designed to scan and identify people without their consent, potentially normalizing ambient biometric surveillance. It highlights the tension between developing helpful AI features and protecting individual privacy rights in consumer electronics. The 'NameTag' feature could automatically capture images of people encountered and convert them into biometric identifiers stored locally on the phone, cross-referencing new scans. Meta's Vice President of Communications stated it was only a pilot project, but the code had been written, reviewed, and shipped in a production app.

rss · IT HOME · Jun 8, 22:57

**Background**: Meta's Ray-Ban smart glasses, developed in partnership with EssilorLuxottica, are AI-powered wearable devices with a built-in camera that have previously faced controversy over privacy issues like unauthorized recording. The concept of an always-on facial recognition feature on such devices is a major concern in the field of AI ethics, as it could enable the identification of individuals in public spaces without their knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/meta-smart-glasses-face-recognition-nametag-connections/">Meta Silently Added Face-Recognition Code for Its Smart ...</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/06/victory-meta-strips-facial-recognition-code-smart-glasses-app-after-public-outcry">VICTORY: Meta Strips Facial Recognition Code From Smart Glasses App ...</a></li>
<li><a href="https://www.biometricupdate.com/202606/smart-glasses-mobile-frt-normalize-ambient-biometric-surveillance">Smart glasses, mobile FRT normalize ambient biometric surveillance</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#facial-recognition`, `#AI ethics`, `#Meta`, `#smart glasses`

---

<a id="item-7"></a>
## [Apple WWDC26: New OSes, Siri AI, and Tim Cook's Final Keynote](https://www.ithome.com/0/961/722.htm) ⭐️ 8.0/10

Apple unveiled the next generation of all its operating systems, including iOS 27 and macOS Golden Gate, with a focus on performance and a major Siri AI overhaul. The event also marked Tim Cook's final keynote before transitioning to executive chairman. The integration of advanced AI into Siri represents a significant leap for Apple's ecosystem, potentially reshaping user interactions across all its platforms. The leadership transition marks the end of an era and the beginning of a new strategic phase for the company. Performance optimizations include up to 30% faster app launches, 80% faster AirDrop, and the CPU scheduler improvements are being backported to the iPhone 11. The new macOS introduces extensive UI refinements to its 'liquid glass' design and a complete rebuild of the system's search infrastructure.

rss · IT HOME · Jun 8, 22:50

**Background**: WWDC is Apple's annual developer conference, where the company traditionally previews its upcoming software updates for all its platforms. Tim Cook has served as Apple's CEO since 2011, guiding the company through its massive growth in services and products like the iPhone and Apple Watch.

**Tags**: `#Apple`, `#WWDC`, `#iOS`, `#AI`, `#Leadership`

---

<a id="item-8"></a>
## [Alist UI suspected of hijack by compromised Polyfill.io script](https://www.v2ex.com/t/1218951#reply7) ⭐️ 8.0/10

A user observed that the login interface of their self-hosted alist instance was replaced by a popup from polyfill.io, which did not accept their credentials, suggesting a possible supply chain attack. Alist is a widely used self-hosted file management tool, and such an attack could compromise user credentials and server integrity, highlighting the persistent risk of supply chain vulnerabilities in open-source software dependencies. The incident is linked to the well-documented polyfill.io supply chain attack, where a compromised JavaScript CDN service was used to inject malicious code into over 100,000 websites, potentially redirecting users to phishing portals.

rss · V2EX · Jun 9, 01:51

**Background**: Polyfill.io is a popular service that provides JavaScript polyfills to ensure browser compatibility, but its domain was acquired by a Chinese company and subsequently compromised in a major supply chain attack. Alist is an open-source file listing program that supports multiple storage providers and is often deployed on personal servers, making it a target for attackers seeking to intercept user data.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.qualys.com/vulnerabilities-threat-research/2024/06/28/polyfill-io-supply-chain-attack">Polyfill.io Supply Chain Attack: What You Need to Know - Qualys Blog</a></li>
<li><a href="https://alistgo.com/">Home | AList Docs</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain-attack`, `#alist`, `#self-hosted`, `#javascript`

---

<a id="item-9"></a>
## [OpenAI confidentially submits draft S-1 filing to SEC for potential IPO](https://openai.com/index/openai-submits-confidential-s-1) ⭐️ 8.0/10

OpenAI has confidentially submitted a draft registration statement, known as an S-1, to the U.S. Securities and Exchange Commission (SEC). This is a formal preliminary step in the process toward a potential Initial Public Offering (IPO), though the company has not determined the timing or terms for any further action. This filing marks a significant financial and corporate milestone for one of the world's leading artificial intelligence organizations, signaling its transition from a private entity and potentially reshaping the AI industry's investment landscape. A successful IPO would provide OpenAI with substantial capital and could set a precedent for other major AI companies. The submission was made under a confidential review process, which allows the SEC to provide feedback without public disclosure, protecting sensitive business information. The company has explicitly stated that it has not yet determined the timing for any further action, meaning an IPO is not imminent and could be delayed or abandoned.

rss · OpenAI Blog · Jun 8, 14:00

**Background**: An S-1 is the formal registration statement that companies must file with the SEC before they can offer shares to the public in the United States. The SEC's confidential review process, particularly for 'Emerging Growth Companies,' allows firms to submit draft registration statements for nonpublic staff review, helping to refine their filings away from public scrutiny before a formal public filing. This process is a common strategy for companies exploring an IPO.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sec.gov/about/divisions-offices/division-corporation-finance/draft-registration-statement-processing-procedures-expanded">Enhanced Accommodations for Issuers Submitting Draft Registration Statements - SEC.gov</a></li>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Understanding Confidential IPO Filings - DFIN</a></li>
<li><a href="https://www.gtlaw.com/en/insights/2025/3/sec-expands-confidential-review-process-for-draft-registration-statements">SEC Expands Confidential Review Process for Draft Registration Statements | Insights</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#IPO`, `#SEC filing`, `#corporate news`, `#AI industry`

---

<a id="item-10"></a>
## [Apple Announces WWDC 2026 Event](https://www.apple.com/apple-events/event-stream/) ⭐️ 8.0/10

Apple has officially announced its Worldwide Developers Conference (WWDC) for 2026, with the event page now live. The announcement includes a dedicated community discussion link on Lobsters for developer engagement. WWDC is a flagship annual event where Apple reveals major software updates, new developer tools, and frameworks that often set industry trends. The conference directly impacts millions of developers building for Apple's ecosystem and influences the broader tech landscape. The event page is hosted on Apple's official website, and the community discussion is facilitated via Lobsters, a platform popular among developers. The announcement references 'WWDC26' as a shorthand, consistent with Apple's typical event naming convention.

rss · Lobsters · Jun 8, 16:52

**Background**: Apple's Worldwide Developers Conference (WWDC) is an annual event focused on software and tools for Apple's platforms, including iOS, macOS, watchOS, and others. It typically features keynote presentations, technical sessions, and labs for developers. The event is a key venue for Apple to communicate its strategic direction and provide early access to new technologies.

**Discussion**: The linked Lobsters discussion thread serves as a community hub for developers to share thoughts, analyses, and reactions to the WWDC 2026 announcements. Such forums often feature debates on the implications of new API designs, framework changes, and Apple's platform evolution.

**Tags**: `#apple`, `#developer-conference`, `#software-development`, `#ios`, `#tech-event`

---

<a id="item-11"></a>
## [Critical Zcash Privacy Bug Found by AI, Enabling Counterfeit Coins](https://www.schneier.com/blog/archives/2026/06/critical-zcash-vulnerability-found-and-fixed.html) ⭐️ 8.0/10

Security researcher Taylor Hornby discovered a critical four-year-old vulnerability in Zcash's Orchard privacy pool on May 29 using the Claude Opus 4.8 AI model. The flaw could have allowed an attacker to generate ZEC from nothing by exploiting a faulty input validation check in the zero-knowledge proof system. This discovery highlights both the severity of vulnerabilities in advanced cryptographic privacy systems and the emerging role of AI as a powerful tool for proactive security research. The fix required Zcash's largest-ever network upgrade to patch a flaw that, if exploited, could have severely undermined the currency's value and integrity. The vulnerability existed in the Orchard pool's zero-knowledge proof circuit, which failed to properly enforce a critical input validation rule, theoretically allowing infinite counterfeiting. The Zcash team completed a major network upgrade to fix the circuit, and there is currently no evidence the flaw was exploited in the wild.

rss · Schneier on Security · Jun 8, 17:06

**Background**: Zcash is a privacy-focused cryptocurrency that uses zero-knowledge proofs (ZKPs) to allow users to transact without revealing sender, receiver, or amount details on the public blockchain. The Orchard pool, introduced in 2022, is its most advanced shielded transaction system, representing a core part of Zcash's privacy architecture. Zero-knowledge proofs are cryptographic methods that prove a statement is true without revealing any underlying data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/zcash-completes-largest-network-upgrade-to-fix-orchard-privacy-pool-vulnerability">Zcash Completes Its Largest Network Upgrade to Address the Orchard Privacy Pool Vulnerability | KuCoin</a></li>
<li><a href="https://decrypt.co/369896/zcash-completes-most-ambitious-network-upgrade-zec-resumes-recent-surge">Zcash Completes 'Most Ambitious' Network Upgrade as ZEC Resumes Recent Surge - Decrypt</a></li>
<li><a href="https://cryptoadventure.com/what-is-the-orchard-pool-zcash-shielded-transactions-zk-proofs-and-inflation-risk/">What Is the Orchard Pool? Zcash Shielded Transactions, ZK Proofs, and Inflation Risk</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#security`, `#zero-knowledge-proofs`, `#AI-assisted-research`, `#vulnerability-disclosure`

---

<a id="item-12"></a>
## [Anthropic confidentially files S-1 for potential IPO after $965B valuation](https://t.me/zaihuapd/41843) ⭐️ 8.0/10

Anthropic has confidentially filed a draft registration statement (Form S-1) with the U.S. Securities and Exchange Commission, laying the groundwork for a potential initial public offering. The move follows its recent record-breaking $65 billion Series H funding round, which valued the AI company at $965 billion. This filing signals that one of the leading AI companies is preparing for a public market debut, which would be a major liquidity event for its investors and a significant test of public market appetite for high-valuation AI firms. It reflects the rapid scaling and investor confidence in the AI industry, particularly in companies building large language models. The confidential filing is a standard preliminary step that allows the company to engage privately with regulators and institutional investors; the final decision to proceed with an IPO, along with share count and pricing, remains undetermined and depends on market conditions. Anthropic recently released the Claude Opus 4.8 model, its most capable model in the Opus family, which supports a 1-million-token context window.

telegram · zaihuapd · Jun 9, 01:10

**Background**: A confidential S-1 filing is a process enabled by the 2012 JOBS Act in the United States that allows companies to submit their IPO registration documents to the SEC without immediate public disclosure, providing more flexibility and reducing pressure during the preparation phase. Anthropic is an American artificial intelligence safety and research company founded in 2021, known for developing the Claude family of large language models, and has seen explosive valuation growth fueled by massive funding rounds.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Form_S-1">Form S-1 - Wikipedia</a></li>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Understanding Confidential IPO Filings</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4 . 8 \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#IPO`, `#Anthropic`, `#business`, `#investment`

---