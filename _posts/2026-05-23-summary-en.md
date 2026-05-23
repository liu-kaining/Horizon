---
layout: default
title: "Horizon Summary: 2026-05-23 (EN)"
date: 2026-05-23
lang: en
---

> From 199 items, 22 important content pieces were selected

---

1. [Megalodon: Mass GitHub Repo Backdooring via CI Workflows](#item-1) ⭐️ 9.0/10
2. [Secure Boot CA Rollover Requires Urgent Linux Distribution Preparation](#item-2) ⭐️ 9.0/10
3. [CISA Contractor Leaks AWS GovCloud Keys on GitHub](#item-3) ⭐️ 9.0/10
4. [Anthropic Launches Project Glasswing for AI-Powered Code Security](#item-4) ⭐️ 8.0/10
5. [China Completes First Emergency Crewed Launch to Replace Damaged Spacecraft](#item-5) ⭐️ 8.0/10
6. [Apple open-sources corecrypto library with post-quantum cryptography](#item-6) ⭐️ 8.0/10
7. [China Sets World Record with 537-Day Deep-Sea Material Corrosion Test at 11,000m](#item-7) ⭐️ 8.0/10
8. [NVIDIA CEO Predicts Annual AI Infrastructure Spending to Reach $4 Trillion](#item-8) ⭐️ 8.0/10
9. [China's eight departments crack down on illegal cross-border securities operations, investigating Tiger Brokers, Futu, and Longbridge.](#item-9) ⭐️ 8.0/10
10. [AI Infra Emerges as Key Battlefield to Combat Enterprise 'Token Anxiety'](#item-10) ⭐️ 8.0/10
11. [Google Announces Gemini 3.5: 4x Faster, Saving Over $1 Billion Annually](#item-11) ⭐️ 8.0/10
12. [TanStack Discloses Sophisticated npm Supply Chain Attack Compromising 42 Packages](#item-12) ⭐️ 8.0/10
13. [Pip 26.1 releases with dependency cooling and lockfile to block supply chain attacks](#item-13) ⭐️ 8.0/10
14. [Apple publishes blueprint for formally verifying its corecrypto library](#item-14) ⭐️ 8.0/10
15. [Galois Adds Isabelle Theorem Prover Support to SAW](#item-15) ⭐️ 8.0/10
16. [Decade-old RCE Vulnerability Found in Linux PDF Viewers](#item-16) ⭐️ 8.0/10
17. [End-to-End Village Generation in Caves of Qud: A 2019 GDC Technical Talk](#item-17) ⭐️ 8.0/10
18. [FTC Settles with Cox Media Group Over Deceptive AI 'Active Listening' Ads](#item-18) ⭐️ 8.0/10
19. [Linux Explores BPF for Custom Page Cache Eviction Policies](#item-19) ⭐️ 8.0/10
20. [Google Project Zero Uncovers Zero-Click Kernel Exploit for Pixel 10](#item-20) ⭐️ 8.0/10
21. [ByteDance Open-Sources Lance, a 3B-Parameter Unified Multimodal Model](#item-21) ⭐️ 8.0/10
22. [Cloudflare Outage: 25-Minute Global Disruption Impacts 28% of HTTP Traffic](#item-22) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Megalodon: Mass GitHub Repo Backdooring via CI Workflows](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows) ⭐️ 9.0/10

On May 18, 2026, an automated campaign codenamed 'Megalodon' pushed over 5,700 malicious commits to more than 5,500 GitHub repositories within six hours, replacing their GitHub Actions workflows with base64-encoded payloads designed to exfiltrate secrets. This represents a highly scalable and aggressive supply chain attack vector that compromises software integrity by poisoning CI/CD pipelines, potentially affecting a vast number of open-source projects and their downstream consumers. The attackers used throwaway accounts with forged identities like 'build-bot' and 'ci-bot' to push malicious GitHub Actions workflows containing bash payloads that exfiltrate CI secrets, cloud credentials, SSH keys, and OIDC tokens to a command-and-control server at 216.126.225.129:8443.

rss · Lobsters · May 22, 09:05

**Background**: GitHub Actions is a CI/CD platform integrated into GitHub that automates software build, test, and deployment workflows. A supply chain attack targets the software development and distribution process, aiming to compromise a trusted tool or dependency to ultimately infect end-users. The exploitation of CI workflows is a known but potent threat vector, as workflows often have elevated permissions to access sensitive secrets and deploy code.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/megalodon-malware-github-repos/">Megalodon Malware Compromised 5,500+ GitHub Repos Within 6 Hours</a></li>
<li><a href="https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/">How to catch GitHub Actions workflow injections before attackers do</a></li>

</ul>
</details>

**Discussion**: The community discussion on Lobsters (linked in the original content) likely focuses on the severe implications for open-source security and the practical challenges of securing automated workflows, with possible debate on the responsibilities of repository maintainers and platform providers.

**Tags**: `#supply-chain-security`, `#CI/CD`, `#github-actions`, `#cybersecurity`, `#open-source-security`

---

<a id="item-2"></a>
## [Secure Boot CA Rollover Requires Urgent Linux Distribution Preparation](https://blog.einval.com/2026/05/22#secure_boot_ca_rollover) ⭐️ 9.0/10

A blog post has issued a critical heads-up to Linux distributions that the Microsoft Secure Boot Certificate Authority (CA) from 2011 will begin expiring in June 2026, necessitating coordinated preparation to prevent boot failures. This rollover is critical because without coordinated updates from Linux distributions, systems relying on Secure Boot could fail to boot or lose their protection against bootkit-level attacks, affecting a wide range of users and servers. The expiring certificates are the 'Microsoft Corporation UEFI CA 2011' and related keys, with the timeline beginning in June 2026 and extending through October 2026, and the process involves replacing them with newer 2023-series certificates.

rss · Lobsters · May 22, 09:48

**Background**: UEFI Secure Boot is a security standard that ensures a device boots using only software trusted by the Original Equipment Manufacturer (OEM). It operates through a key hierarchy that includes a Platform Key (PK), Key Exchange Key (KEK), and signature databases (db/dbx). Microsoft's third-party CA is used by Linux distributions, typically via a 'shim' bootloader, to have their bootloaders signed so they are trusted by default Secure Boot firmware configurations.

<details><summary>References</summary>
<ul>
<li><a href="https://windowsforum.com/threads/secure-boot-certificate-rollover-what-to-check-before-june-2026.416378/">Secure Boot Certificate Rollover: What to Check Before June ...</a></li>
<li><a href="https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e">Windows Secure Boot certificate expiration and CA updates - Microsoft Support</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/windows-itpro-blog/updating-microsoft-secure-boot-keys/4055324">Updating Microsoft Secure Boot keys | Windows IT Pro blog</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters comments page likely contains high community discussion, reflecting the technical gravity of the issue and the need for coordinated action across the open-source ecosystem.

**Tags**: `#Secure Boot`, `#Linux distributions`, `#cryptography`, `#system security`, `#certificate management`

---

<a id="item-3"></a>
## [CISA Contractor Leaks AWS GovCloud Keys on GitHub](https://www.schneier.com/blog/archives/2026/05/cisa-security-leak.html) ⭐️ 9.0/10

A contractor for the Cybersecurity and Infrastructure Security Agency (CISA) accidentally exposed highly privileged AWS GovCloud keys and internal system details in a public GitHub repository until last weekend. This is one of the most egregious government data leaks in recent history, as the exposed credentials could grant access to critical U.S. government cloud infrastructure, prompting Congressional inquiries and raising serious national security concerns. The leaked repository included files detailing how CISA internally builds, tests, and deploys software, and the agency is still struggling to contain the breach and invalidate the compromised credentials.

rss · Schneier on Security · May 22, 13:58

**Background**: CISA is the U.S. Cybersecurity and Infrastructure Security Agency, a federal agency responsible for protecting the nation's critical infrastructure from cyber threats. AWS GovCloud (US) is a specialized, isolated cloud region from Amazon Web Services designed to host sensitive government workloads and adhere to strict U.S. compliance requirements like ITAR and FedRAMP.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>

</ul>
</details>

**Discussion**: The news, discussed by security expert Bruce Schneier and reported by outlets like KrebsOnSecurity, has been met with widespread shock and concern in the cybersecurity community, highlighting serious lapses in security protocols for government contractors.

**Tags**: `#cybersecurity`, `#government`, `#data-leak`, `#AWS`, `#CISA`

---

<a id="item-4"></a>
## [Anthropic Launches Project Glasswing for AI-Powered Code Security](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 8.0/10

Anthropic announced Project Glasswing, an AI security research initiative that claims its system identified over 1,752 high-severity vulnerabilities with a 90.6% true positive rate after independent verification. This initiative could significantly enhance software security by proactively finding and patching critical vulnerabilities, addressing a major challenge in the AI era where traditional methods struggle with complex codebases. The claimed 90.6% true positive rate is based on assessments by independent security firms, though this figure is notably higher than benchmarks for other AI vulnerability detection tools, which often fall below 40%.

hackernews · louiereederson · May 22, 19:31 · [Discussion](https://news.ycombinator.com/item?id=48240419)

**Background**: Large Language Models (LLMs) are emerging as tools for software vulnerability detection, offering advantages over traditional static and dynamic analysis methods which can have high false positive rates. Static Application Security Testing (SAST) tools are already used to find flaws, but LLMs aim to detect more subtle, context-dependent vulnerabilities that are harder to find. The CVE program is the standard for uniquely identifying and cataloging such software vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html">Anthropic's Claude Mythos Finds Thousands of Zero-Day Flaws ...</a></li>
<li><a href="https://fuzzinglabs.com/benchmarking-ai-agents-vulnerability-research/">Benchmarking LLM agents for vulnerability research</a></li>

</ul>
</details>

**Discussion**: The community reaction is mixed: some users report highly accurate results from similar tools like Codex Security, aligning with Anthropic's claims, while others express skepticism, citing feedback from projects like curl that question the degree of improvement over existing tools. A key debate centers on whether applying expensive LLM tools is justified when many organizations haven't yet implemented basic static analysis and linters.

**Tags**: `#AI-security`, `#vulnerability-detection`, `#code-analysis`, `#research`

---

<a id="item-5"></a>
## [China Completes First Emergency Crewed Launch to Replace Damaged Spacecraft](https://www.ithome.com/0/954/253.htm) ⭐️ 8.0/10

In November 2025, China successfully executed its first emergency crewed space launch, sending the Shenzhou-22 spacecraft to the station after the Shenzhou-20 was damaged by a space debris impact on its return capsule window. The entire emergency response, from problem discovery to the new spacecraft's docking, was completed within 20 days. This event provides a successful, real-world validation of China's 'launch one, backup one' contingency strategy, offering a valuable case study for international space programs on efficiently managing astronaut safety during in-orbit emergencies. The crisis began when astronauts on Shenzhou-20 discovered a suspected crack in the return capsule's window caused by a micrometeoroid or space debris impact; after analysis, mission control decided it was unsafe for return, so the crew safely returned aboard the backup Shenzhou-21 while Shenzhou-22 was launched from the standby Long March 2F rocket. Based on lessons learned, the upcoming Shenzhou-23 mission has already incorporated improved space debris shielding on its windows.

rss · IT HOME · May 23, 01:30

**Background**: China's human spaceflight program has maintained a 'launch one, backup one' strategy since the beginning of its space station era, where one crewed spacecraft and rocket are always on standby at the launch site ready for rapid deployment. Space debris, traveling at extremely high velocities, poses a significant threat to spacecraft, where even millimeter-sized particles can damage critical components like windows and solar panels.

<details><summary>References</summary>
<ul>
<li><a href="https://news.cctv.com/2026/05/23/ARTI6kbH95B6sY8GZiHipQ5Z260523.shtml">去年中国载人航天工程实施首次应急发射任务 为国际航天领域高效应对突...</a></li>
<li><a href="https://www.news.cn/tech/20251127/26d2f836ea564c178330e8f01e27c4a4/c.html">解密载人航天首次应急发射任务 - 新华网</a></li>
<li><a href="https://baike.baidu.com/item/打一备一、滚动备份模式/67166787">打一备一、滚动备份模式 - 百度百科</a></li>

</ul>
</details>

**Tags**: `#Space Exploration`, `#Crewed Spaceflight`, `#Emergency Response`, `#Space Station`, `#China`

---

<a id="item-6"></a>
## [Apple open-sources corecrypto library with post-quantum cryptography](https://www.ithome.com/0/954/226.htm) ⭐️ 8.0/10

Apple has published the source code for its corecrypto cryptographic library on GitHub, which includes the post-quantum algorithms ML-KEM and ML-DSA along with formal verification tools and documentation. This release is a significant step in deploying post-quantum cryptography at scale on consumer devices like iPhone and Mac, providing a transparent and verified foundation for future security against quantum computing threats. The corecrypto library serves as the low-level cryptographic engine for Apple's Security framework and CryptoKit, and its release includes code, test tools, performance benchmarks, and a dedicated directory for formal verification proofs against the FIPS 203 and FIPS 204 standards.

rss · IT HOME · May 22, 23:01

**Background**: Post-quantum cryptography (PQC) refers to cryptographic algorithms designed to be secure against attacks by both classical and future quantum computers, which could break widely used schemes like RSA and ECC. In 2024, the U.S. National Institute of Standards and Technology (NIST) standardized ML-KEM (FIPS 203) for key encapsulation and ML-DSA (FIPS 204) for digital signatures as primary PQC algorithms. Apple previously integrated post-quantum protections into iMessage with the PQ3 protocol starting in iOS 17.4.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM - Wikipedia</a></li>
<li><a href="https://www.digicert.com/insights/post-quantum-cryptography/mldsa">ML-DSA | Post-Quantum Cryptography | DigiCert Insights</a></li>
<li><a href="https://csrc.nist.gov/pubs/fips/203/final">Federal Information Processing Standard (FIPS) 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard</a></li>

</ul>
</details>

**Tags**: `#post-quantum cryptography`, `#cryptography`, `#open-source`, `#security`, `#Apple`

---

<a id="item-7"></a>
## [China Sets World Record with 537-Day Deep-Sea Material Corrosion Test at 11,000m](https://www.ithome.com/0/954/225.htm) ⭐️ 8.0/10

China has completed the world's first 537-day corrosion test of materials at a depth of 11,000 meters in the ocean, setting a new global record for the duration of such deep-sea in-situ experiments. This milestone demonstrates a key breakthrough in deep-sea testing capabilities, allowing for long-term validation of material performance in extreme pressure and corrosive conditions, which is critical for the future development of deep-sea exploration equipment and infrastructure. The test, led by the 725 Research Institute of China State Shipbuilding Corporation, verified the deep-sea adaptability of 30 types of protective coatings, 4 categories of novel sacrificial anodes, and 22 structural metal materials.

rss · IT HOME · May 22, 22:45

**Background**: Deep-sea in-situ testing involves conducting scientific experiments directly on the seabed to maintain the natural physical and chemical conditions, providing the most authentic data on material behavior. Sacrificial anodes are a key corrosion protection method for submerged metal structures, where a more reactive metal corrodes preferentially to protect the primary structure. Testing materials over such long durations is essential to understand their real-world longevity in the extreme, high-pressure, and corrosive environment of the deep sea.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Galvanic_anode">Galvanic anode - Wikipedia</a></li>
<li><a href="https://www.mdpi.com/2075-163X/13/2/184">Design and Application of a Deep-Sea Engineering Geology In Situ Test System</a></li>

</ul>
</details>

**Tags**: `#deep-sea research`, `#materials science`, `#corrosion testing`, `#ocean engineering`, `#scientific records`

---

<a id="item-8"></a>
## [NVIDIA CEO Predicts Annual AI Infrastructure Spending to Reach $4 Trillion](https://www.ithome.com/0/954/223.htm) ⭐️ 8.0/10

NVIDIA reported record Q1 FY2027 revenue of $81.6 billion, with its data center business soaring 92% year-over-year, while CEO Jensen Huang predicted hyperscaler AI capital expenditures will grow to $3-4 trillion annually by 2030, quadrupling the current Wall Street consensus. This prediction signals a massive, long-term investment cycle in AI infrastructure that will drive demand for chips, cloud services, and energy, profoundly impacting the tech industry, financial markets, and even consumer electricity costs. The projected $3-4 trillion annual spending by 2030 is a stark contrast to the Wall Street consensus expecting hyperscaler capex to reach only $1.03 trillion by 2028, while NVIDIA itself is undertaking an $80 billion share buyback program.

rss · IT HOME · May 22, 22:30

**Background**: Hyperscalers like Amazon, Google, Microsoft, and Meta are large cloud service providers that operate massive data center networks globally. Their capital expenditures, heavily driven by AI infrastructure like GPUs and servers, have been rapidly increasing, with forecasts for 2026 spending around $700 billion. NVIDIA's data center business, which sells the high-performance GPUs that form the backbone of this AI infrastructure, has seen explosive growth, consistently exceeding expectations.

<details><summary>References</summary>
<ul>
<li><a href="https://techblog.comsoc.org/2025/12/22/hyperscaler-capex-600-bn-in-2026-a-36-increase-over-2025-while-global-spending-on-cloud-infrastructure-services-skyrockets/">Hyperscaler capex > $600 bn in 2026 a 36% increase over 2025...</a></li>
<li><a href="https://247wallst.com/investing/2026/05/01/hyperscalers-hit-700-billion-in-2026-ai-spending-plans/">Hyperscalers Hit $700 Billion in 2026 AI Spending Plans</a></li>
<li><a href="https://qz.com/can-nvidia-s-data-center-business-sustain-its-high-growth-momentum?trk=article-ssr-frontend-pulse_little-text-block">Can NVIDIA 's Data Center Business Sustain Its High Growth ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#NVIDIA`, `#cloud computing`, `#capital expenditure`, `#tech earnings`

---

<a id="item-9"></a>
## [China's eight departments crack down on illegal cross-border securities operations, investigating Tiger Brokers, Futu, and Longbridge.](https://mp.weixin.qq.com/s?__biz=MzA4NzAzMDgwMw==&amp;mid=2651090403&amp;idx=3&amp;sn=bca72a940ac72bef356f29b5b9576ac1&amp;chksm=8a1670281e2bc67d2df3608a313ba9fdaf0fcd2f43ce44475c6bf273b386af2e4f9d8e8e2e2b&amp;scene=0&amp;xtrack=1) ⭐️ 8.0/10

China's eight regulatory departments, including the CSRC, have jointly issued a crackdown plan on illegal cross-border securities, futures, and fund operations, imposing a two-year cleanup period where existing investors can only sell positions and transfer funds out. The CSRC has formally launched investigations and issued preliminary penalty notices to Tiger Brokers, Futu, and Longbridge for illegally operating cross-border securities businesses within mainland China. This regulatory action significantly impacts fintech investment platforms serving Chinese mainland investors seeking access to overseas markets, effectively forcing a halt to their core business activities and reinforcing strict capital controls. It underscores the government's resolve to close regulatory loopholes and steer cross-border investment flows toward officially approved channels like Stock Connect and QDII. The crackdown covers not only the foreign institutions but also their domestic affiliates, intermediaries, and even self-media platforms that provided marketing or account-opening channels. The plan specifies that affected domestic websites, trading software, and servers must be completely shut down after the two-year transition period, and the CSRC intends to confiscate all illegal gains from the investigated entities.

telegram · 新智元 · May 22, 08:26

**Background**: In China, cross-border securities investment is heavily regulated to control capital outflows and manage financial risk. Legitimate channels include the Stock Connect programs (like Shanghai-Hong Kong Stock Connect and Shenzhen-Hong Kong Stock Connect), the QDII (Qualified Domestic Institutional Investor) scheme, and the Cross-boundary Wealth Management Connect in the Greater Bay Area. Platforms like Tiger Brokers and Futu have attracted mainland clients for overseas trading but operated in a regulatory gray area without the necessary mainland licenses.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/港股通/13611865">港股通（内地与香港股票市场交易互联互通机制）_百度百科 一文搞懂港股通开通条件及交易规则 - 知乎 港股通交易规则全解：从时间、机制到费用，一文看懂实操要点 港股通是什么?开通条件与流程全解析 (2025 最新版)|内地股市|融资融券... 港股上市公司加入港股通的条件及最近一次的调整记录（20250310） 基本... 一文讲清楚港股通：开通条件、佣金、交易规则（附港股通测评答案）_股...</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/合格境内机构投资者">合格境内机构投资者 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.swhyhk.com/tc/cross-boundary/">申萬宏源（香港）有限公司 - 粵港澳大灣區 跨 境 理 財 通</a></li>

</ul>
</details>

**Tags**: `#financial regulation`, `#fintech`, `#cross-border investment`, `#securities law`, `#Chinese market`

---

<a id="item-10"></a>
## [AI Infra Emerges as Key Battlefield to Combat Enterprise 'Token Anxiety'](https://www.infoq.cn/article/TLRAmZy8pPICVFVWmu6p?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Enterprises are now facing 'token anxiety'—the struggle to efficiently utilize purchased AI hardware like GPUs, which is driving intense competition and innovation in the AI infrastructure market. This shift highlights that the true bottleneck for enterprise AI adoption is moving beyond hardware acquisition to software and infrastructure optimization, affecting how companies realize ROI on AI investments. The challenge involves not just GPU underutilization but also integrating software orchestration, scaling systems like AI Replica Optimization, and managing costs across cloud environments to match actual workload demand.

rss · InfoQ 中文站 · May 22, 20:34

**Background**: 'Token anxiety' refers to the pressure on developers and enterprises to maximize the use of AI tokens (units of compute for models like LLMs) to justify infrastructure costs, a concept popularized recently by figures like Andrej Karpathy. AI infrastructure encompasses the software, middleware, and cloud systems required to run, scale, and manage AI workloads efficiently, going far beyond simply owning hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://alex-ber.medium.com/the-rise-of-token-anxiety-why-ai-is-making-developers-miserable-462ff6d50cc1">The Rise of “Token Anxiety”: Why AI is Making Developers ...</a></li>
<li><a href="https://scaleops.com/product/ai-infra/">AI Infra - ScaleOps</a></li>
<li><a href="https://medium.com/@mcschnei/right-sizing-gpu-compute-infrastructure-for-ai-workloads-a-practical-guide-997caf455601">Right-Sizing GPU & Compute Infrastructure for AI Workloads ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#GPU optimization`, `#enterprise AI`, `#system architecture`, `#resource management`

---

<a id="item-11"></a>
## [Google Announces Gemini 3.5: 4x Faster, Saving Over $1 Billion Annually](https://www.infoq.cn/article/COda3jCSAliReaA4YVJc?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Google has announced its latest AI model family, Gemini 3.5, starting with the release of the 3.5 Flash version, which the company claims delivers a significant leap in performance and operational efficiency. This announcement signals a major internal technological shift at Google, as the claimed 4x speed increase and over $1 billion in annual cost savings could significantly strengthen its competitive position in the AI industry. Gemini 3.5 Flash reportedly shows a 19.6% performance improvement over its predecessor on real-world enterprise tasks, though its operational cost is noted to be around 60% higher than some comparable models like DeepSeek V4 Flash.

rss · InfoQ 中文站 · May 22, 18:13

**Background**: Gemini is Google's family of multimodal AI models designed to handle text, images, audio, and video. The "Flash" variant typically refers to a model optimized for speed and cost-efficiency, making it suitable for high-volume, real-time applications. Google's advancements are supported by its custom Tensor Processing Unit (TPU) hardware, which provides the computational backbone for training and serving these large models.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3 . 5 : frontier intelligence with action</a></li>
<li><a href="https://blog.kilo.ai/p/the-age-of-the-flash-model-gemini">The Age of the Flash Model: Gemini 3 . 5 , StepFun, DeepSeek and the...</a></li>
<li><a href="https://docs.cloud.google.com/tpu/docs/v5p">TPU v5p | Google Cloud Documentation</a></li>

</ul>
</details>

**Tags**: `#AI Models`, `#Google`, `#Performance Optimization`, `#Large Language Models`, `#Tech Industry News`

---

<a id="item-12"></a>
## [TanStack Discloses Sophisticated npm Supply Chain Attack Compromising 42 Packages](https://www.infoq.cn/article/ePxUGQ7cZvWNWkOhE1vT?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

TanStack has publicly disclosed that a sophisticated supply chain attack compromised 42 of its npm packages, with the attack leveraging techniques like GitHub Actions workflow hijacking. This incident highlights the critical security risks within the open-source ecosystem, as it affects a widely-used web development library and underscores vulnerabilities in package management and contribution workflows. The attack, possibly linked to a broader 'Mini Shai-Hulud' campaign, involved self-propagating malware that poisoned caches and used valid SLSA Build Level provenance to publish malicious versions. In response, the TanStack team is considering making pull requests invitation-only, a significant shift from the standard open-contribution model.

rss · InfoQ 中文站 · May 22, 16:00

**Background**: An npm supply chain attack occurs when malicious code is injected into widely-used JavaScript packages, which are then automatically downloaded by developers and applications, potentially leading to data theft or system compromise. TanStack is a popular open-source project providing headless, type-safe UI libraries and tools for web development. The broader 'Mini Shai-Hulud' campaign, named by the threat group TeamPCP, is a sophisticated worm that has compromised hundreds of npm packages by hijacking legitimate GitHub Actions workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/security/2026/05/18/tanstack-weighs-invitation-only-pull-requests-after-supply-chain-attack/5241899">TanStack weighs invitation-only pull requests after supply ...</a></li>
<li><a href="https://thecybersecguru.com/news/mini-shai-hulud-npm-worm-affected-packages-list/">Mini Shai-Hulud npm Attack: All Affected Packages | The ...</a></li>
<li><a href="https://www.kunalganglani.com/blog/npm-supply-chain-attack-defense">NPM Supply Chain Attacks : 5 Defenses Every JS Dev Needs [2026]</a></li>

</ul>
</details>

**Discussion**: No community comments were provided in the source material to summarize.

**Tags**: `#supply-chain-attack`, `#npm`, `#open-source-security`, `#software-security`, `#dependency-management`

---

<a id="item-13"></a>
## [Pip 26.1 releases with dependency cooling and lockfile to block supply chain attacks](https://www.infoq.cn/article/tO2s7Qc7DtKWpXMpMbC1?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Pip 26.1 has officially introduced a 'dependency cooling' mechanism that enforces a waiting period before newly published packages can be installed, and added experimental support for lockfiles based on PEP 751 (pylock.toml). These features directly address critical vulnerabilities in the Python packaging ecosystem by providing a time buffer to detect malicious packages and ensuring deterministic, reproducible installations, which is a significant step in mitigating supply chain attacks. The dependency cooling is implemented via the `--uploaded-prior-to` option, allowing users to specify a cut-off date for package publication. The lockfile feature is experimental and guarantees validity only for the current Python version and platform.

rss · InfoQ 中文站 · May 22, 10:40

**Background**: Supply chain attacks involve compromising open-source packages to spread malware to downstream users, a growing threat highlighted by incidents like the recent compromise of hundreds of npm and PyPI packages. Dependency cooling is a defense strategy where a package manager refuses to install a package until a certain amount of time has passed since its publication, giving the community a window to identify and report malicious releases. Lockfiles (like pylock.toml) record the exact versions of all dependencies used in an environment to prevent unexpected changes and ensure identical builds.

<details><summary>References</summary>
<ul>
<li><a href="https://sethmlarson.dev/pip-relative-dependency-cooling-with-crontab">Relative “ Dependency Cooling ” in pip v26.0 with crontab</a></li>
<li><a href="https://pip.pypa.io/en/stable/cli/pip_lock/">pip lock - pip documentation v26.1.1</a></li>
<li><a href="https://www.infoq.com/news/2026/05/pip-261-dependency-cooldowns/">Pip 26.1 Ships Dependency Cooldowns and Experimental Lockfile ...</a></li>

</ul>
</details>

**Discussion**: The introduction of these features is likely to be well-received by security-conscious developers and organizations, though the experimental nature of the lockfile may lead to cautious adoption. Discussions may focus on the practical implementation of cooling periods in different workflows and comparisons with existing lockfile solutions like Pipfile.lock.

**Tags**: `#Python`, `#Package Management`, `#Security`, `#Supply Chain`, `#Tools`

---

<a id="item-14"></a>
## [Apple publishes blueprint for formally verifying its corecrypto library](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 8.0/10

Apple has published a detailed blueprint outlining how they apply formal verification techniques to their corecrypto cryptographic library, including the release of quantum-secure ML-KEM and ML-DSA algorithm implementations with mathematical proofs, alongside the custom verification libraries and tools they created. This is significant because it demonstrates a major technology company publicly committing resources to mathematically proving the correctness of a foundational security component, which can elevate industry standards for software assurance and inspire broader adoption of formal verification in safety-critical software. The published proofs are specifically for the implementations of the quantum-secure ML-KEM (FIPS 203) and ML-DSA (FIPS 204) algorithms, and the accompanying blog post includes access to the formal verification libraries and tools Apple developed internally for this purpose.

rss · Lobsters · May 22, 19:40

**Background**: Formal verification is a set of techniques that use mathematical logic to prove that a system's design or implementation adheres exactly to its specification, going beyond traditional testing to achieve exhaustive coverage of all possible inputs. Apple's corecrypto is the underlying cryptographic library that provides fundamental security primitives for its operating systems like iOS and macOS. The recent push towards post-quantum cryptography, exemplified by standards like FIPS 203 and 204, is driving the need for enhanced verification due to the critical importance and novelty of these algorithms.

<details><summary>References</summary>
<ul>
<li><a href="https://security.apple.com/blog/formal-verification-corecrypto/">A blueprint for formal verification of Apple corecrypto</a></li>
<li><a href="https://9to5mac.com/2026/05/22/apple-shares-iphone-and-mac-post-quantum-cryptography-code-on-github/">Apple shares iPhone and Mac post-quantum ... - 9to5Mac</a></li>
<li><a href="https://www.nist.gov/document/formal-verification-cryptographic-software-aws-current-practices-and-future-trends">Formal Veriﬁcation of Cryptographic Software at AWS - Current ...</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters comments likely contain substantive technical discussion from the security and formal methods communities, focusing on the practical implications of Apple's approach, the depth of the verification, and comparisons to similar efforts at other companies like AWS.

**Tags**: `#formal-verification`, `#cryptography`, `#apple`, `#security`, `#software-correctness`

---

<a id="item-15"></a>
## [Galois Adds Isabelle Theorem Prover Support to SAW](https://www.galois.com/articles/announcing-isabelle-support-for-saw) ⭐️ 8.0/10

Galois announced that its Software Analysis Workbench (SAW) now has new, integrated support for the Isabelle theorem prover, enabling users to more seamlessly combine these two formal verification tools in their workflows. This integration is significant for the formal methods community as it bridges two major tools, potentially streamlining verification processes and making complex formal proofs more accessible for software developers and security analysts. The integration specifically connects SAW, which automates verification by translating programs into logical expressions for external solvers, with Isabelle, a higher-order logic theorem prover known for its trustworthy small-kernel architecture.

rss · Lobsters · May 22, 21:59

**Background**: The Software Analysis Workbench (SAW) is a tool from Galois for formally verifying properties of programs by translating them into a logical form and using automated reasoning. Isabelle is a powerful, general-purpose interactive theorem prover based on higher-order logic (HOL), widely used in academic and industrial research for verifying complex systems. Integrating such tools is a common goal in formal methods to leverage the strengths of different verification approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://tools.galois.com/saw">SAW : The Software Analysis Workbench | SAW | Galois Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_theorem_prover">Isabelle theorem prover</a></li>

</ul>
</details>

**Discussion**: The Lobsters discussion linked in the content suggests there is community interest in this integration, indicating its practical value for practitioners working with formal verification tools.

**Tags**: `#formal-verification`, `#theorem-proving`, `#software-analysis`, `#Isabelle`, `#SAW`

---

<a id="item-16"></a>
## [Decade-old RCE Vulnerability Found in Linux PDF Viewers](https://medeiros.zip/posts/CVE-2026-46529-evince) ⭐️ 8.0/10

A critical remote code execution vulnerability, assigned CVE-2026-46529, was discovered in the popular Linux PDF viewers XReader, Evince, and Atril, persisting undetected for approximately ten years. This vulnerability is significant because it affects widely used document viewers across many Linux distributions, potentially allowing attackers to execute arbitrary code on a user's system simply by opening a malicious PDF file. The vulnerability is a command injection flaw related to the handling of a specific GTK flag, which was removed in GTK 4, making newer software like 'Papers' less affected than Evince, Atril, and XReader. Exploitation requires the attacker to predict the absolute file path where the malicious PDF is saved.

rss · Lobsters · May 22, 22:14

**Background**: PDF viewers are common software on Linux systems for rendering portable document format files. Remote Code Execution (RCE) is a class of security vulnerability that allows an attacker to execute arbitrary code on a target machine from a remote location. CVE, or Common Vulnerabilities and Exposures, is a standardized system for identifying and cataloging publicly known cybersecurity vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://seclists.org/oss-sec/2026/q2/643">oss-sec: Re: Evince / Atril / Xreader command injection CVE-2026-46529</a></li>
<li><a href="https://advisory.eventussecurity.com/advisory/critical-vulnerability-in-pdf-js-allows-remote-code-execution/">Critical Vulnerability in PDF.js Allows Remote Code Execution</a></li>

</ul>
</details>

**Discussion**: The Lobsters community discussion likely delves into the technical specifics of the command injection, the implications of the long-standing nature of the bug, and the relative security of different PDF viewer implementations, particularly comparing those using GTK 3 versus GTK 4.

**Tags**: `#security`, `#CVE`, `#Linux`, `#software-vulnerability`, `#open-source`

---

<a id="item-17"></a>
## [End-to-End Village Generation in Caves of Qud: A 2019 GDC Technical Talk](https://www.youtube.com/watch?v=jV-DZqdKlnE) ⭐️ 8.0/10

In a 2019 GDC session, developers from Freehold Games detailed their complete procedural generation system for villages in Caves of Qud, which algorithmically creates histories, cultures, architectural styles, NPCs, and quests. This talk showcases a sophisticated approach to procedural generation that moves beyond simple level or terrain creation to simulate complex, interconnected social and narrative systems, setting a high bar for emergent storytelling in games. The system generates content 'end-to-end,' meaning the high-level historical simulation directly produces detailed, coherent village-level content like specific questlines and cultural traits, ensuring consistency across the generated world.

rss · Lobsters · May 22, 17:36

**Background**: Caves of Qud is a science-fantasy roguelike known for its deep simulation and extensive procedural generation. The game's world generation creates a history involving procedurally generated sultans, regions, and events, which forms the foundation for the village systems discussed in the talk.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=jV-DZqdKlnE">End - to - End Procedural Generation in Caves of Qud - YouTube</a></li>
<li><a href="https://wiki.cavesofqud.com/wiki/World_generation">World generation - Official Caves of Qud Wiki End-to-End Procedural Generation in Caves of Qud Generating Anything and Everything in Caves of Qud Procedural World Generation : r/cavesofqud - Reddit Images Caves of Qud Procedural Generation Survive Your First Minutes! Subverting Historical Cause & Effect: Generation of Mythic ...</a></li>
<li><a href="https://media.gdcvault.com/gdc2019/presentations/Grinblat_Jason_End-to-End_Procedural_Generation.pdf">End-to-End Procedural Generation in Caves of Qud</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion likely features insightful technical debate and community interest in the novel approaches to generating complex, simulated histories and cultures, as highlighted in the news item's reason for scoring.

**Tags**: `#procedural-generation`, `#game-development`, `#systems-design`, `#simulation`

---

<a id="item-18"></a>
## [FTC Settles with Cox Media Group Over Deceptive AI 'Active Listening' Ads](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-require-cox-media-group-two-other-firms-pay-nearly-1-million-settle-charges-they-deceived) ⭐️ 8.0/10

The Federal Trade Commission (FTC) has required Cox Media Group and two other firms to pay a total of $930,000 to settle charges that they deceived customers by falsely marketing an AI-powered advertising service called 'Active Listening'. This settlement represents a significant regulatory action holding a major media company accountable for deceptive practices in AI-powered advertising, setting an important precedent for future enforcement in the growing field of AI marketing technology. The technology, called 'Active Listening,' was marketed as using AI to listen to real-world conversations through smartphones and smart speakers to deliver targeted ads, but the FTC found the claims were deceptive; the settlement requires financial penalties but does not admit wrongdoing by the companies.

rss · Lobsters · May 22, 04:53

**Background**: 'Active Listening' AI technology claims to use artificial intelligence to analyze real-time voice data from conversations and combine it with online behavioral data to target consumers with ads. The Federal Trade Commission (FTC) is the U.S. agency responsible for consumer protection and preventing deceptive business practices. The settlement involves Cox Media Group, MindSift LLC, and 1010 Digital Works LLC.

<details><summary>References</summary>
<ul>
<li><a href="https://thecyberexpress.com/ftc-ai-powered-active-listening-case/">AI-Powered Marketing Service “Active Listening” Deceived ...</a></li>
<li><a href="https://cyberwarriorsmiddleeast.com/ftc-ai-powered-active-listening-case/">FTC Exposes Deception in AI-Powered Marketing Service “Active ...</a></li>

</ul>
</details>

**Discussion**: The provided content links to a comments section on Lobsters, but no specific comments or discussions were included in the input for analysis.

**Tags**: `#AI ethics`, `#regulation`, `#marketing technology`, `#FTC`, `#consumer protection`

---

<a id="item-19"></a>
## [Linux Explores BPF for Custom Page Cache Eviction Policies](https://lwn.net/Articles/1073103/) ⭐️ 8.0/10

At the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit, a session explored using BPF to customize the kernel's page cache policies for specific workloads, moving beyond the current one-size-fits-all eviction strategy. The page cache significantly impacts overall system performance, and a BPF-based customizable policy could allow fine-tuned optimizations for diverse applications, potentially improving performance for workloads where the default policy falls short. The proposal builds on existing research like the 'cache_ext' framework, which uses eBPF programs via the kernel's struct_ops mechanism to implement custom eviction policies attached to specific cgroups.

rss · LWN.net · May 22, 14:37

**Background**: The Linux kernel's page cache stores copies of file data (organized as 'folios') in memory to speed up access. The kernel uses an eviction policy to decide which pages to remove when memory is needed. Extended Berkeley Packet Filter (eBPF) is a technology that allows running sandboxed programs within the kernel, enabling safe and dynamic customization of kernel functions without modifying the kernel source code.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cache-ext/cache_ext">cache_ext: Custom Page Cache Eviction Policies with eBPF</a></li>
<li><a href="https://deepwiki.com/cache-ext/cache_ext/3.2-ebpf-policy-system">eBPF Policy System | cache-ext/cache_ext | DeepWiki</a></li>
<li><a href="https://blogs.oracle.com/linux/intro-to-folios">An explanation of how folios improve memory management in Linux .</a></li>

</ul>
</details>

**Tags**: `#Linux Kernel`, `#BPF`, `#Memory Management`, `#Page Cache`, `#Systems Optimization`

---

<a id="item-20"></a>
## [Google Project Zero Uncovers Zero-Click Kernel Exploit for Pixel 10](https://hackaday.com/2026/05/22/this-week-in-security-ai-generated-reports-more-ai-generated-reports-github-chaos-and-more-linux-vulnerabilities/) ⭐️ 8.0/10

Google's Project Zero team has demonstrated a new zero-click exploit for the Pixel 10 phone, which allows an attacker to achieve full system compromise from remote access to the kernel without any user interaction. This discovery is critical because a zero-click exploit that escalates to the kernel represents a severe security threat, potentially compromising the device's core security model and affecting a major new flagship phone. The exploit was found during an investigation by Project Zero, demonstrating a complete escalation path from remote access to the kernel level, highlighting a significant flaw in the device's security architecture.

rss · Hackaday · May 22, 14:00

**Background**: Project Zero is Google's internal team dedicated to finding zero-day vulnerabilities, which are previously unknown security flaws. A zero-click exploit is a type of attack that requires no user interaction, such as clicking a link, making it particularly dangerous. Pixel phones are Google's flagship Android devices, and a kernel-level exploit means the vulnerability targets the core of the operating system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Zero">Project Zero</a></li>
<li><a href="https://grokipedia.com/page/Zero-click_exploit">Zero-click exploit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero -day vulnerability - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#zero-day`, `#Android`, `#exploit`

---

<a id="item-21"></a>
## [ByteDance Open-Sources Lance, a 3B-Parameter Unified Multimodal Model](https://mp.weixin.qq.com/s/Xbfq72cr1796RZxJIs3L1A) ⭐️ 8.0/10

ByteDance has open-sourced Lance, a lightweight 3B-parameter multimodal model that unifies image/video understanding and generation, achieving state-of-the-art results on benchmarks like GenEval and VBench. This release represents a significant step towards efficient, unified multimodal AI, allowing a single model to handle diverse vision-language tasks, which could streamline development and reduce complexity in building multimodal applications. The model employs a dual-stream expert architecture using Qwen2.5-VL and Wan2.2 encoders for understanding and generation, respectively, and uses modality-aware positional encoding to resolve sequence boundary confusion. It is released under the permissive Apache 2.0 license.

telegram · zaihuapd · May 22, 06:40

**Background**: Unified multimodal models aim to handle various tasks like image captioning, video understanding, and image/video generation within a single architecture, unlike specialized models for each task. A dual-stream expert architecture typically uses separate processing paths or 'experts' for different modalities or tasks (like understanding vs. generation) to maintain high performance while unifying capabilities. Positional encoding is a technique used in transformer models to inject information about the order of tokens, and adapting it for multiple modalities is crucial for effectively processing mixed inputs like images, videos, and text.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41598-025-10930-1">Dual-stream interactive mechanism with multi-modal hierarchical ...</a></li>
<li><a href="https://arxiv.org/pdf/2510.23095">Revisiting Multimodal Positional Encoding in Vision-Language ...</a></li>
<li><a href="https://deepwiki.com/deepbeepmeep/Wan2GP/8.1-text-encoders">Text Encoders | deepbeepmeep/Wan2GP | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#open-source`, `#computer-vision`, `#generative-ai`, `#bytedance`

---

<a id="item-22"></a>
## [Cloudflare Outage: 25-Minute Global Disruption Impacts 28% of HTTP Traffic](https://t.me/zaihuapd/41527) ⭐️ 8.0/10

Cloudflare published an incident report detailing a 25-minute global outage on December 5, 2025, that disrupted approximately 28% of HTTP traffic, primarily affecting customers using legacy FL1 proxies with the Cloudflare Managed Ruleset enabled. This incident highlights the critical risks of deploying security patches to legacy infrastructure at global scale, as a single configuration change caused a widespread outage affecting a significant portion of web traffic for a major internet infrastructure provider. The root cause was a security patch for the critical CVE-2025-55182 vulnerability in React Server Components, which unintentionally caused an error in the legacy FL1 proxy when the WAF rule testing tool was disabled; the newer Rust-based systems were unaffected.

telegram · zaihuapd · May 22, 16:15

**Background**: CVE-2025-55182 is a critical pre-authentication remote code execution vulnerability affecting React Server Components and Next.js frameworks, rated CVSS 10.0. Cloudflare's Web Application Firewall (WAF) uses managed rulesets, which are pre-configured and regularly updated security rules to protect against common web exploits. FL1 refers to Cloudflare's older, Lua-based proxy infrastructure, which is being phased out in favor of more modern systems.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=46162656">Cloudflare outage on December 5, 2025 | Hacker News</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2025/12/15/defending-against-the-cve-2025-55182-react2shell-vulnerability-in-react-server-components/">Defending against the CVE-2025-55182 (React2Shell ...</a></li>
<li><a href="https://developers.cloudflare.com/waf/managed-rules/">Managed Rules · Cloudflare Web Application Firewall (WAF) docs</a></li>

</ul>
</details>

**Discussion**: Community discussion, particularly on Hacker News and LinkedIn, focused on the operational lessons learned, emphasizing the danger of pushing configuration changes globally without gradual rollout and the risks inherent in maintaining legacy code in production systems.

**Tags**: `#cloudflare`, `#incident-report`, `#web-infrastructure`, `#network-outage`, `#security-patch`

---