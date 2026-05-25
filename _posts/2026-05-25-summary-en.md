---
layout: default
title: "Horizon Summary: 2026-05-25 (EN)"
date: 2026-05-25
lang: en
---

> From 167 items, 10 important content pieces were selected

---

1. [APKPure's Official Telegram APK Found to Contain a Spyware Backdoor](#item-1) ⭐️ 9.0/10
2. [Epic Reveals Unreal Engine 6 with Rocket League as First Showcase](#item-2) ⭐️ 9.0/10
3. [Huawei Proposes 'Tao Law' with 'Logic Folding' for Semiconductor Evolution](#item-3) ⭐️ 8.0/10
4. [Bexorg Tests Drugs on Ex Vivo Human Brains Using BrainEx System](#item-4) ⭐️ 8.0/10
5. [New Holographic 3D Printing Method Achieves 70x Efficiency Boost](#item-5) ⭐️ 8.0/10
6. [Alibaba's T-Head C9 processors are the first RVA23 RISC-V chips to fully support Android 16.](#item-6) ⭐️ 8.0/10
7. [China to Cultivate Two Generations of Rice in Space for the First Time](#item-7) ⭐️ 8.0/10
8. [Apple's WWDC to be Tim Cook's final keynote as CEO before John Ternus takeover](#item-8) ⭐️ 8.0/10
9. [CXMT Chairman Zhu Yiming Gives Nearly Half His Shares to Employees, Locks Remaining for 10 Years](#item-9) ⭐️ 8.0/10
10. [Google Docs Launches Docs Live for Voice-to-Document Creation](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [APKPure's Official Telegram APK Found to Contain a Spyware Backdoor](https://x.com/EricParker/status/2058411298195661221) ⭐️ 9.0/10

The official Telegram version 12.6.5 distributed through the APKPure app store was repackaged with a malicious spyware framework named DataCollector injected into its code. This backdoor allows for extensive data theft, including chat history, contacts, photos, documents, GPS location, and SIM card information. This incident represents a significant supply chain attack that compromises the trust in popular third-party app repositories, directly threatening the privacy and security of millions of Telegram users who downloaded the app from APKPure. It highlights the persistent risk of malware injection in widely-used communication tools. The malicious payload was embedded in an additional file (classes3.dex) containing over 3000 lines of code, and the stolen data is encrypted using AES-GCM before being exfiltrated to a specific command-and-control server at IP address 38.190.225.166.

telegram · zaihuapd · May 24, 11:38

**Background**: A supply chain attack compromises software or its distribution channels to inject malware before it reaches the end user. APKPure is a third-party Android app store that hosts APK files, which are the installation packages for Android apps. Repackaging an APK involves decompiling it, inserting malicious code, and then recompiling and signing it with a new digital certificate to distribute the trojanized version.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wiz.io/academy/application-security/supply-chain-attacks">Supply Chain Attacks: Examples & Strategies - wiz.io</a></li>
<li><a href="https://seedsecuritylabs.org/Labs_16.04/Mobile/Android_Repackaging/Android_Repackaging.pdf">Android Repackaging Attack Lab</a></li>
<li><a href="https://medium.com/@anyrun/understand-encryption-in-malware-aes-lu0bot-example-1080a58736ab">Understand Encryption in Malware: AES (Lu0Bot Example) | by ANY.RUN | Medium</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain-attack`, `#malware`, `#telegram`, `#privacy`

---

<a id="item-2"></a>
## [Epic Reveals Unreal Engine 6 with Rocket League as First Showcase](https://www.pcgamer.com/gaming-industry/epic-reveals-first-unreal-engine-6-game-and-its-not-fortnite/) ⭐️ 9.0/10

Epic Games has officially announced Unreal Engine 6, with the vehicle soccer game Rocket League confirmed to be the first title showcased running on the new engine, making a direct leap from Unreal Engine 3. This announcement marks a major milestone for the game development industry, as it signifies the arrival of a new generation of Epic's widely-used game engine, potentially impacting thousands of developers and the future of real-time 3D content creation. The showcased gameplay footage is described as 'in-game real-time recorded', unlike the longer tech demo for Unreal Engine 5's launch; notably, Epic has not yet detailed UE6's specific technical advantages over UE5.

telegram · zaihuapd · May 25, 02:20

**Background**: Unreal Engine is one of the most popular game engines in the world, used to develop countless video games and other real-time 3D applications. Its previous version, Unreal Engine 5, was released in 2022 and introduced technologies like Nanite for virtualized geometry. The announcement comes as UE5 has faced criticism for optimization issues on PC, and Epic's CEO had previously indicated a transition from UE5 to UE6 within a few years, integrating new programming tools like Verse.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unrealengine.com/unreal-engine-5">Unreal Engine 5</a></li>
<li><a href="https://www.reddit.com/r/pcgaming/comments/1kep0xt/epics_tim_sweeney_shares_first_details_about/">Epic's Tim Sweeney shares first details about Unreal Engine 6</a></li>

</ul>
</details>

**Tags**: `#game development`, `#unreal engine`, `#epic games`, `#rocket league`, `#game engine`

---

<a id="item-3"></a>
## [Huawei Proposes 'Tao Law' with 'Logic Folding' for Semiconductor Evolution](https://www.ithome.com/0/954/720.htm) ⭐️ 8.0/10

At IEEE ISCAS 2026, Huawei presented the 'Tao Law' (τ Law), a new semiconductor scaling principle that replaces geometric scaling with 'time scaling' using innovations like 'Logic Folding' to reduce signal propagation delay and increase transistor density. This proposes a potential post-Moore's Law pathway for the semiconductor industry, emphasizing multi-level co-optimization from devices to systems to continue performance and density gains as traditional geometric scaling hits physical limits. The multi-level optimization framework includes Logic Folding at the circuit level to shorten interconnect paths, a full-stack software-hardware-chip co-design at the chip level, and the Lingqu bus protocol at the system level to reduce communication latency; Huawei projects that by 2031, chips based on this law could achieve transistor density equivalent to 1.4nm processes.

rss · IT HOME · May 25, 02:48

**Background**: Moore's Law, the observation that the number of transistors on a chip doubles roughly every two years, has driven semiconductor progress for decades but is facing fundamental physical and economic limits. Traditional 'geometric scaling' involves shrinking transistor dimensions through advanced lithography, but as nodes approach atomic scales, this becomes increasingly challenging and costly. Huawei's approach shifts the focus to optimizing the fundamental 'time constant' (τ) of signal propagation across the entire system stack.

<details><summary>References</summary>
<ul>
<li><a href="https://www.huawei.com/en/news/2025/9/hc-lingqu-ai-superpod">Huawei Unveils World's Most Powerful SuperPoDs and... - Huawei</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#chip-design`, `#Huawei`, `#architecture`, `#IEEE`

---

<a id="item-4"></a>
## [Bexorg Tests Drugs on Ex Vivo Human Brains Using BrainEx System](https://www.ithome.com/0/954/713.htm) ⭐️ 8.0/10

The U.S. startup Bexorg has developed a proprietary BrainEx system to keep donated human brains alive ex vivo for testing experimental drugs targeting neurodegenerative diseases like Parkinson's and Alzheimer's. This approach offers a more realistic drug testing environment than animal models or cell cultures, potentially accelerating the development of treatments for neurological disorders and reducing reliance on early-stage human trials. The brains are maintained with artificial blood and oxygen, with electrical activity suppressed by anesthetics like propofol; Bexorg has studied over 700 brains and is preparing its first research paper, while the FDA has already approved a clinical trial for a drug based on its data.

rss · IT HOME · May 25, 02:25

**Background**: Ex vivo organ maintenance involves perfusing organs with oxygenated solutions outside the body to preserve cellular functions, a technology Bexorg adapted for brains. Propofol is a common intravenous anesthetic that induces sedation by enhancing GABA receptor activity, which helps suppress neural activity in these experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://neuwritesd.org/2019/06/13/brainex-restoring-brain-circulation-after-death/">BrainEx: Restoring Brain Circulation After Death | NeuWrite San Diego</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6552398/">Bioengineering approaches to organ preservation ex vivo - PMC - NIH</a></li>
<li><a href="https://go.drugbank.com/drugs/DB00818">Propofol : Uses, Interactions, Mechanism of Action | DrugBank</a></li>

</ul>
</details>

**Tags**: `#biotechnology`, `#neuroscience`, `#pharmaceutical research`, `#ethics`, `#medical innovation`

---

<a id="item-5"></a>
## [New Holographic 3D Printing Method Achieves 70x Efficiency Boost](https://www.ithome.com/0/954/679.htm) ⭐️ 8.0/10

Researchers at EPFL have developed a new holographic volumetric 3D printing system using a phase light modulator (PLM) MEMS device, which increases light energy utilization efficiency by 70 times compared to traditional amplitude modulation. This allows for the printing of complex, multi-scale structures, such as a human ear model in just over two minutes, using only a 150 milliwatt laser. This breakthrough dramatically reduces the cost and complexity of volumetric 3D printing by enabling high-resolution, large-scale prints with very low-power lasers, potentially making the technology more accessible for applications in medical devices, tissue engineering, and rapid prototyping. The multi-scale capability without changing hardware could accelerate development cycles in fields requiring intricate, custom components. The key innovation is integrating a phase light modulator into the volumetric printing system, which modulates the light's phase rather than its amplitude, leading to the 70-fold efficiency gain. The system can print objects up to 3 x 3 x 4 cm³ with a 150 mW laser and allows digital zooming from micrometer-scale scaffolds to centimeter-scale models without hardware changes.

rss · IT HOME · May 25, 01:32

**Background**: Volumetric 3D printing, also known as holographic or tomographic 3D printing, works by projecting light patterns from multiple angles into a photocurable resin to solidify an entire 3D volume simultaneously, rather than layer-by-layer. Traditional systems often use amplitude modulation, which blocks light to form patterns, wasting significant energy. Phase modulation, in contrast, redirects light without absorbing it, making it far more efficient for generating the complex light fields needed for high-quality volumetric printing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41377-026-02331-4">High-efficiency multi-scale holographic volumetric 3D printing with a phase light modulator | Light: Science & Applications</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56852-4">Holographic tomographic volumetric additive manufacturing | Nature Communications</a></li>
<li><a href="https://wp.optics.arizona.edu/pablanche/wp-content/uploads/sites/37/2017/12/1707_Blanche_ApplSci7040411.pdf">Diffraction-Based Optical Switching with MEMS</a></li>

</ul>
</details>

**Tags**: `#3D printing`, `#holographic printing`, `#additive manufacturing`, `#materials science`, `#medical devices`

---

<a id="item-6"></a>
## [Alibaba's T-Head C9 processors are the first RVA23 RISC-V chips to fully support Android 16.](https://www.ithome.com/0/954/672.htm) ⭐️ 8.0/10

Alibaba's Damo Academy announced that its T-Head C9 series processors, which are compliant with the RISC-V RVA23 profile, have completed adaptation for Android 16 and are now being released to strategic partners. This milestone demonstrates that RISC-V can achieve full compatibility with the latest major Android version, moving from basic functionality to spec-compliant product delivery and laying a crucial technical foundation for large-scale commercial adoption in mobile and IoT devices. The platform passed over 68,000 core CPU-related CTS/VTS test cases from the Android mainline and provides a complete trusted execution environment with over 40 security applications, supporting features like secure boot and digital rights management.

rss · IT HOME · May 25, 01:13

**Background**: RISC-V is an open standard instruction set architecture (ISA) that allows anyone to design and manufacture processors. The RVA23 profile is a key RISC-V specification that defines a common set of ISA features for 64-bit application processors, which is critical for software ecosystem compatibility. Android Verified Boot (AVB), Generic Kernel Image (GKI), and Vendor Interface (VINTF) are Android's core frameworks for system security, kernel standardization, and hardware-software separation.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.riscv.org/reference/profiles/rva23/_attachments/rva23-profile.pdf">RVA 23 Profiles</a></li>
<li><a href="https://fprox.substack.com/p/risc-v-vector-cryptography-extensions">RISC-V Vector Cryptography Extensions (1/2)</a></li>
<li><a href="https://source.android.com/docs/core/architecture/partitions">Partitions overview | Android Open Source Project</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#Android`, `#processor`, `#embedded systems`, `#Alibaba`

---

<a id="item-7"></a>
## [China to Cultivate Two Generations of Rice in Space for the First Time](https://www.ithome.com/0/954/670.htm) ⭐️ 8.0/10

China's Shenzhou-23 mission, launched on May 24th, carried rice seeds to the Tiangong space station to conduct the first-ever experiment of cultivating two continuous generations of rice in orbit. This experiment is crucial for understanding genetic stability across generations in microgravity, which is a key step towards enabling sustainable food production for future long-duration deep-space missions. The experiment includes seeds from plants whose ancestors experienced spaceflight and new control seeds, and will compare sexual reproduction with a 'ratoon rice' (regrowth) method to study adaptation differences.

rss · IT HOME · May 25, 01:08

**Background**: In 2022, Chinese scientists successfully completed the full life cycle of rice from seed to seed aboard the Tiangong station, proving the basic feasibility of rice cultivation in space. The microgravity environment of space alters fundamental biological processes, and studying multi-generational effects is necessary because changes in genetic mechanisms and metabolism may only become apparent over longer periods and through subsequent generations.

<details><summary>References</summary>
<ul>
<li><a href="https://worldscience.cn/c/2024-10-28/664270.shtml">空间微重力条件下的植物生长发育</a></li>
<li><a href="https://www.pku-iaas.edu.cn/list_63/1414.html">育种MBA | 0011 环境组学与未来生物学、农业和作物育种</a></li>
<li><a href="https://html.rhhz.net/linyekexue/html/20090725.htm">大青杨航天诱变植株早期抗氧化酶生化指标测定</a></li>

</ul>
</details>

**Tags**: `#space biology`, `#agriculture`, `#genetics`, `#space exploration`, `#microgravity`

---

<a id="item-8"></a>
## [Apple's WWDC to be Tim Cook's final keynote as CEO before John Ternus takeover](https://www.ithome.com/0/954/666.htm) ⭐️ 8.0/10

Bloomberg's Mark Gurman reports that Apple's 2026 WWDC keynote on June 8 will be Tim Cook's final one as CEO, with John Ternus officially taking over as CEO on September 1. This marks the end of the Tim Cook era at Apple and the beginning of a significant leadership transition for one of the world's most valuable companies, which will shape Apple's future product strategy and direction. Tim Cook will transition to the role of Executive Chairman and will not give future keynote presentations, while John Ternus's first major public appearance as CEO will be at the September iPhone launch, where a foldable iPhone is reportedly a priority.

rss · IT HOME · May 25, 00:55

**Background**: Tim Cook has been the CEO of Apple since 2011, succeeding Steve Jobs. John Ternus is Apple's Senior Vice President of Hardware Engineering. WWDC is Apple's annual developer conference where major software updates and sometimes new hardware are announced.

**Tags**: `#Apple`, `#Leadership Transition`, `#WWDC`, `#Tech Industry`, `#Tim Cook`

---

<a id="item-9"></a>
## [CXMT Chairman Zhu Yiming Gives Nearly Half His Shares to Employees, Locks Remaining for 10 Years](https://www.ithome.com/0/954/653.htm) ⭐️ 8.0/10

Zhu Yiming, founder and chairman of DRAM chip leader CXMT, will distribute 7.68 billion shares to company employees as a long-term incentive following the IPO, and has committed to not reducing his remaining holdings for 10 years. This move, combined with the company's explosive financial growth ahead of a planned IPO, signals strong leadership confidence in CXMT's long-term value and may help retain talent in China's competitive semiconductor industry. Zhu Yiming holds a total of 1.598 billion shares (2.6561% stake), with the 7.68 billion shares for distribution representing nearly half; his share lock-up extends to 20 years with a 20% annual reduction limit after the initial 10-year full lock.

rss · IT HOME · May 25, 00:43

**Background**: CXMT (长鑫科技) is a leading Chinese DRAM memory chip manufacturer. DRAM (Dynamic Random-Access Memory) is a type of volatile memory fundamental to computing devices like PCs, servers, and smartphones. The company has filed for an IPO on Shanghai's STAR Market and plans to raise 29.5 billion yuan for capacity and technology upgrades.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jiuyangongshe.com/a/3y18xw1sxeq">长鑫科 技 、长江 存 储 上市，真正利好的是哪条半导体产业链？ -韭研公社</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#corporate governance`, `#IPO`, `#employee incentives`, `#DRAM`

---

<a id="item-10"></a>
## [Google Docs Launches Docs Live for Voice-to-Document Creation](https://www.wsj.com/tech/personal-tech/google-docs-live-test-e4473e07) ⭐️ 8.0/10

Google introduced Docs Live, a feature powered by Gemini AI that converts spoken ideas into structured documents through voice commands in Google Docs. The tool allows users to dictate thoughts, adjust outlines or tone via voice, and can even pull information from Google Drive files or the web to enrich content. This feature could significantly streamline document creation workflows, especially for brainstorming and initial drafting, by addressing the 'blank page anxiety' many users face. It represents a major step in integrating advanced generative AI directly into widely-used productivity software, potentially shifting how people create content. Docs Live will initially be available only to paid AI subscribers using iOS and Android apps, with plans for later expansion to the web and more general users. The feature adheres to Google Workspace's privacy rules, ensuring that input data is not used for model training.

telegram · zaihuapd · May 24, 09:39

**Background**: Google Docs is a widely used cloud-based word processor that is part of the Google Workspace suite, enabling real-time collaboration. Docs Live leverages Gemini AI, Google's advanced family of large language models, to understand and generate human-like text from voice input. The feature is part of a broader trend by tech companies to embed generative AI capabilities directly into everyday productivity tools to enhance user efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnet.com/tech/services-and-software/turn-your-spoken-ramblings-into-coherent-articles-with-google-docs-live/">Turn Your Spoken Ramblings Into Coherent Articles With Google ...</a></li>
<li><a href="https://www.gadgets360.com/ai/news/google-i-o-2026-docs-live-gmail-keep-gemini-ai-voice-us-rollout-11520723">Google I/O 2026: Docs Live Brings Gemini Voice AI to Gmail, Docs ...</a></li>
<li><a href="https://one.google.com/about/google-ai-plans/">Google AI Plans with Cloud Storage - Google One</a></li>

</ul>
</details>

**Tags**: `#Google Docs`, `#AI Productivity Tools`, `#Voice-to-Text`, `#Generative AI`, `#Workspace AI`

---