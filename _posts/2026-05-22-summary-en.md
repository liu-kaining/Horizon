---
layout: default
title: "Horizon Summary: 2026-05-22 (EN)"
date: 2026-05-22
lang: en
---

> From 206 items, 18 important content pieces were selected

---

1. [GPT-4.5 passes Turing test with 73% human judgment rate in new study.](#item-1) ⭐️ 9.0/10
2. [FreeBSD 14.x Kernel Vulnerability Allows Local Privilege Escalation](#item-2) ⭐️ 9.0/10
3. [AI Model Discovers and Exploits macOS Kernel Vulnerability on M5 Chip](#item-3) ⭐️ 9.0/10
4. [Lilly's Retatrutide Achieves 28.3% Weight Loss in Pivotal Phase 3 Obesity Trial](#item-4) ⭐️ 9.0/10
5. [New Ferroelectric NAND Flash Memory Withstands 100 Million X-rays, 30x More Radiation-Resistant](#item-5) ⭐️ 8.0/10
6. [Windows 11 kernel flaw lets attackers escape browser sandbox for full system control.](#item-6) ⭐️ 8.0/10
7. [California signs first US executive order to prepare for AI's economic impact.](#item-7) ⭐️ 8.0/10
8. [U.S. AI Executive Order Canceled Due to White House Conflict and Tech Lobbying](#item-8) ⭐️ 8.0/10
9. [US Invests $2B in Nine Quantum Firms, IBM Gets $1B for New Chip Company](#item-9) ⭐️ 8.0/10
10. [SpaceX Emerges as a Major AI Compute Provider, Citing Major Industry Deals](#item-10) ⭐️ 8.0/10
11. [Alibaba releases new Qwen3.7-Max model, claimed as best domestic AI in China.](#item-11) ⭐️ 8.0/10
12. [Qt Bridges Enables C# Developers to Build UIs with the Qt Framework](#item-12) ⭐️ 8.0/10
13. [Microsoft Research Introduces Vega for Privacy-Preserving Digital Identity](#item-13) ⭐️ 8.0/10
14. [OpenAI's GPT-next model disproves Erdős's 80-year-old planar unit distance conjecture.](#item-14) ⭐️ 8.0/10
15. [Command injection vulnerability found in GTK-based PDF readers like Evince.](#item-15) ⭐️ 8.0/10
16. [NVIDIA's Q4 revenue hits $68.1B, guides Q1 2027 to $78B on AI demand](#item-16) ⭐️ 8.0/10
17. [黄仁勋：英伟达已基本放弃中国 AI 芯片市场](#item-17) ⭐️ 8.0/10
18. [OpenAI Codex Gains Ability to Control Mac Apps While Screen is Locked](#item-18) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-4.5 passes Turing test with 73% human judgment rate in new study.](https://www.ithome.com/0/953/705.htm) ⭐️ 9.0/10

A UC San Diego study published in PNAS provides the first empirical evidence that an AI model, GPT-4.5, can pass the Turing test by being judged as human 73% of the time in 15-minute chats, surpassing real human participants. This milestone demonstrates that advanced AI can convincingly mimic human social behavior in conversation, which has significant implications for online trust, social engineering risks, and forces a re-evaluation of what the Turing test truly measures. The model's success depended on being given specific 'persona' prompts to adopt a human-like communication style; without such guidance, its human judgment rate dropped sharply to 36%. The study also tested other models, with LLaMa-3.1-405B achieving 56%, while the classic ELIZA chatbot and GPT-4o scored much lower.

rss · IT HOME · May 22, 01:22

**Background**: The Turing test, proposed by Alan Turing in 1950, assesses a machine's ability to exhibit intelligent behavior indistinguishable from a human. Large Language Models (LLMs) like GPT-4.5 and LLaMa are AI systems trained on vast text datasets to generate human-like responses. ELIZA, created in the 1960s, was an early chatbot that used simple pattern matching to simulate conversation, often cited as a baseline in AI history.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Eliza_(chatbot)">Eliza (chatbot)</a></li>
<li><a href="https://huggingface.co/blog/llama31">Llama 3 . 1 - 405 B , 70B & 8B with multilinguality and long context</a></li>

</ul>
</details>

**Tags**: `#Turing Test`, `#GPT-4.5`, `#LLM`, `#AI Research`, `#Human-AI Interaction`

---

<a id="item-2"></a>
## [FreeBSD 14.x Kernel Vulnerability Allows Local Privilege Escalation](https://fatgid.io/) ⭐️ 9.0/10

A local privilege escalation vulnerability named FatGid has been disclosed for the FreeBSD 14.x kernel, which exploits a stack buffer overflow via the setcred(2) system call to gain elevated privileges. This vulnerability is significant because it affects the kernel of a major open-source operating system, potentially allowing any local user to gain root access, which could lead to full system compromise. The exploit chain works specifically on FreeBSD 14.x due to a sizeof(*groups) typo; while FreeBSD 15.0 also contains the typo, its differing code structure prevents the same exploit from functioning.

rss · Lobsters · May 21, 13:42

**Background**: FreeBSD is a free and open-source Unix-like operating system known for its advanced networking, security, and storage features. A kernel local privilege escalation (LPE) vulnerability allows an attacker who already has limited access to a system to gain higher privileges, typically root or administrator rights, by exploiting a flaw in the operating system's core software.

<details><summary>References</summary>
<ul>
<li><a href="https://fatgid.io/">FatGid - FreeBSD 14.x kernel local privilege escalation</a></li>
<li><a href="https://www.freebsd.org/security/">FreeBSD Security Information | The FreeBSD Project</a></li>

</ul>
</details>

**Discussion**: The vulnerability was discussed on Lobsters, where the community likely debated the technical details of the exploit, its real-world impact, and potential mitigation steps for FreeBSD administrators.

**Tags**: `#security`, `#FreeBSD`, `#kernel`, `#vulnerability`, `#LPE`

---

<a id="item-3"></a>
## [AI Model Discovers and Exploits macOS Kernel Vulnerability on M5 Chip](https://www.schneier.com/blog/archives/2026/05/macos-kernel-memory-corruption-exploit.html) ⭐️ 9.0/10

Researchers at Calif used Anthropic's unreleased Claude Mythos AI model to discover and develop a working exploit for a kernel memory corruption vulnerability on Apple's M5 chipset in just five days. This is a groundbreaking demonstration that AI models have reached a level of capability where they can significantly accelerate the discovery and exploitation of critical security vulnerabilities, signaling a paradigm shift in security research and defense. The exploit was developed against Apple's M5 chip, which is designed with advanced hardware and software mitigations to make memory corruption exploits dramatically harder, yet the AI-assisted team bypassed these in five days.

rss · Schneier on Security · May 21, 16:03

**Background**: Kernel memory corruption is a class of vulnerability where software can write to or read from unintended areas of a computer's core operating system memory, potentially allowing an attacker to gain full control. Apple's M-series chips are designed with custom silicon and system-level protections, like Pointer Authentication Codes (PAC), to make such exploitation difficult. The Mythos model is Anthropic's latest frontier AI, noted for strong cybersecurity capabilities in internal assessments.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Assessing Claude Mythos Preview's cybersecurity capabilities - Anthropic Red</a></li>

</ul>
</details>

**Tags**: `#AI`, `#security`, `#vulnerability`, `#kernel`, `#exploit`

---

<a id="item-4"></a>
## [Lilly's Retatrutide Achieves 28.3% Weight Loss in Pivotal Phase 3 Obesity Trial](https://www.prnewswire.com/news-releases/lillys-triple-agonist-retatrutide-delivered-powerful-weight-loss-in-pivotal-phase-3-obesity-trial-302778859.html) ⭐️ 9.0/10

Eli Lilly announced positive topline results from the Phase 3 TRIUMPH-1 trial, where its investigational triple-agonist drug retatrutide achieved an average weight loss of 28.3% in the highest 12 mg dose group after 80 weeks. These results represent a significant breakthrough in obesity treatment, as the weight loss achieved with retatrutide approaches the levels typically seen with bariatric surgery, potentially offering a powerful non-surgical option for patients with obesity and related comorbidities. The trial enrolled approximately 2,500 adults with obesity or overweight and at least one weight-related comorbidity; the 12 mg dose group also saw 45.3% of participants lose at least 30% of their body weight, and the discontinuation rate due to adverse events was lower than placebo.

telegram · zaihuapd · May 22, 02:18

**Background**: Retatrutide is a first-in-class investigational drug that simultaneously activates three hormone receptors: glucose-dependent insulinotropic polypeptide (GIP), glucagon-like peptide-1 (GLP-1), and glucagon. This triple-agonist mechanism is designed to enhance metabolic effects for greater weight loss compared to single or dual agonists like semaglutide or tirzepatide.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ajmc.com/view/retatrutide-achieves-up-to-30-3-average-weight-loss-in-phase-3-triumph-1-trial">Retatrutide Achieves Up to 30.3% Average Weight Loss in Phase 3 TRIUMPH-1 Trial | AJMC</a></li>
<li><a href="https://www.pharmacytimes.com/view/retatrutide-delivers-bariatric-level-weight-loss-pivotal-phase-3-triumph-1-trial">Retatrutide Delivers Bariatric-Level Weight Loss in Pivotal Phase 3 TRIUMPH-1 Trial | Pharmacy Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLP1_poly-agonist_peptides">GLP 1 poly- agonist peptides - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#pharmaceutical`, `#clinical_trials`, `#obesity_treatment`, `#weight_loss`, `#drug_development`

---

<a id="item-5"></a>
## [New Ferroelectric NAND Flash Memory Withstands 100 Million X-rays, 30x More Radiation-Resistant](https://www.ithome.com/0/953/713.htm) ⭐️ 8.0/10

Researchers at Georgia Tech have developed a ferroelectric NAND flash memory using hafnium oxide that demonstrated a radiation tolerance of up to 1 million rads, which is 30 times greater than conventional NAND flash. This breakthrough enables reliable, high-capacity data storage for critical space applications, such as onboard AI systems, by ensuring memory stability in extreme radiation environments where traditional flash fails. The key innovation is using the material's ferroelectric polarization state instead of trapped charges to store data, making it inherently resistant to radiation-induced charge interference. The chips were tested to withstand radiation levels equivalent to 100 million chest X-rays, covering the range from low Earth orbit to deep space missions.

rss · IT HOME · May 22, 01:47

**Background**: Traditional NAND flash memory stores data by trapping electrons in a floating gate or charge-trap layer, a mechanism vulnerable to corruption from high-energy particles in space. Ferroelectric memory, like this new FeNAND, uses a different principle where data is stored via the reversible polarization direction of a ferroelectric material, such as doped hafnium oxide (HfO2), which is more robust against radiation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ferroelectric_flash_memory">Ferroelectric flash memory - Wikipedia</a></li>
<li><a href="https://pubs.aip.org/aip/apl/article/121/24/240502/2834676/A-Perspective-on-ferroelectricity-in-hafnium-oxide">A Perspective on ferroelectricity in hafnium oxide: Mechanisms and considerations regarding its stability and performance | Applied Physics Letters | AIP Publishing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Radiation_hardening">Radiation hardening - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#radiation-hardened`, `#space technology`, `#materials science`, `#NAND flash`

---

<a id="item-6"></a>
## [Windows 11 kernel flaw lets attackers escape browser sandbox for full system control.](https://www.ithome.com/0/953/712.htm) ⭐️ 8.0/10

A critical vulnerability (CVE-2026-40369) was discovered in the Windows 11 kernel's ntoskrnl.exe file, specifically in the ExpGetProcessInformation function, allowing attackers to bypass the security sandboxes of major browsers like Chrome and gain the highest system privileges. This is significant because it allows a malicious website or payload opened in a browser to completely take over the underlying Windows system, undermining the fundamental security model of modern web browsing, and affects the latest versions of Windows 11. The vulnerability is triggered by calling NtQuerySystemInformation with a specific information class (253) and crafted buffer parameters, which bypasses the ProbeForWrite kernel validation due to a length-zero check flaw, and the exploit chain has been demonstrated to have a 100% success rate for sandbox escape.

rss · IT HOME · May 22, 01:46

**Background**: The Windows kernel, managed by the ntoskrnl.exe file, is the core of the operating system, and functions like ExpGetProcessInformation are used for system management tasks. Browsers like Chrome use a 'sandbox' to isolate web content and prevent malicious code from affecting the host system. ProbeForWrite is a kernel mechanism designed to validate write access to user-space buffers to prevent security breaches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ntoskrnl.exe">ntoskrnl.exe - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite">ProbeForWrite function (wdm.h) - Windows drivers | Microsoft Learn</a></li>

</ul>
</details>

**Tags**: `#security`, `#Windows`, `#vulnerability`, `#kernel`, `#CVE`

---

<a id="item-7"></a>
## [California signs first US executive order to prepare for AI's economic impact.](https://www.ithome.com/0/953/710.htm) ⭐️ 8.0/10

California Governor Gavin Newsom signed an executive order on May 21, directing state agencies to prepare for and mitigate the economic and labor market disruptions caused by AI, making it the first such order in the United States. This is a significant policy move by a major state to proactively address AI's workforce disruption, setting a potential precedent for other regions and signaling a concrete government response to the societal impacts of advanced technology. The order instructs California agencies to help workers gain skills to share in AI's benefits, track AI's labor market impacts, and develop stronger public policies to support those affected by potential employment disruptions.

rss · IT HOME · May 22, 01:45

**Background**: Generative AI and advanced automation are rapidly changing the nature of work across many industries, raising concerns about job displacement and economic inequality. An executive order is a directive from a head of government that carries the force of law within their administration's operations, often used to set policy priorities and direct government agencies.

**Tags**: `#AI policy`, `#labor market impact`, `#government regulation`, `#California`, `#workforce transition`

---

<a id="item-8"></a>
## [U.S. AI Executive Order Canceled Due to White House Conflict and Tech Lobbying](https://www.ithome.com/0/953/708.htm) ⭐️ 8.0/10

A planned U.S. executive order to regulate AI was abruptly canceled by President Trump on Thursday, May 22, following intense opposition from his advisor David Sacks and tech CEOs Elon Musk and Mark Zuckerberg, who argued it would hinder American competitiveness. This reversal highlights the dominance of an anti-regulation, 'accelerationist' stance within the Trump administration and the significant influence of tech industry lobbying on U.S. AI policy, signaling a likely hands-off approach to AI governance in the near term. The canceled order would have required a 90-day pre-release review of AI models by the government, but raised questions about why the Treasury Department was given a leading role over cybersecurity agencies. Despite the executive order's demise, the White House's Office of the National Cyber Director is reportedly still working on other AI safety initiatives.

rss · IT HOME · May 22, 01:37

**Background**: The debate centers on 'AI accelerationism,' a philosophy advocating for rapid technological progress with minimal constraints, versus calls for precautionary safety testing and regulation to mitigate potential risks. In the U.S., this political tension pits the desire to maintain global leadership and industry growth against concerns about AI's societal impact and safety.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Accelerationism">Accelerationism</a></li>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">XAI (company)</a></li>

</ul>
</details>

**Tags**: `#AI Regulation`, `#U.S. Policy`, `#Tech Lobbying`, `#AI Governance`, `#Geopolitics`

---

<a id="item-9"></a>
## [US Invests $2B in Nine Quantum Firms, IBM Gets $1B for New Chip Company](https://www.ithome.com/0/953/673.htm) ⭐️ 8.0/10

The US government is investing $2 billion through equity stakes in nine quantum computing companies, with IBM receiving $1 billion to establish a dedicated quantum chip manufacturing firm called Anderon. This initiative, funded by the CHIPS and Science Act, also allocates $375 million to GlobalFoundries for a US factory and approximately $100 million each to companies like D-Wave and Rigetti Computing. This significant government investment underscores the strategic importance of quantum computing for US national security and economic competitiveness, aiming to bolster domestic capabilities and create high-tech jobs. It follows a pattern of the government taking equity stakes in critical industries, similar to past actions with Intel, to strengthen supply chains and advance technological leadership. IBM's new subsidiary, Anderon, will be headquartered in Albany, New York, and plans to offer its quantum chip manufacturing technology to external clients. Notably, two of the funded companies, D-Wave and PsiQuantum, have historical ties to the Trump administration, and the funding ultimately stems from incentives signed into law by former President Biden.

rss · IT HOME · May 21, 23:02

**Background**: Quantum computing leverages quantum mechanics to perform complex calculations much faster than classical computers, with potential applications in drug discovery, financial modeling, and cryptography. The CHIPS and Science Act is a major US law enacted to boost domestic semiconductor manufacturing and research through substantial subsidies and incentives. The US government has recently adopted a strategy of taking direct equity stakes in companies deemed vital to national security, as seen with its investment in chipmaker Intel.

**Tags**: `#quantum computing`, `#government investment`, `#IBM`, `#semiconductor manufacturing`, `#technology policy`

---

<a id="item-10"></a>
## [SpaceX Emerges as a Major AI Compute Provider, Citing Major Industry Deals](https://www.infoq.cn/article/fS0QHZiYGmZJZZNwk5V3?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Reports indicate that Anthropic has committed to paying SpaceX $15 billion annually for computing resources, and SpaceX's potential acquisition of the AI coding startup Cursor includes a massive $10 billion breakup fee, positioning SpaceX as a central player in AI infrastructure. This shift could transform SpaceX into a dominant 'computing power tycoon' similar to NVIDIA's role in GPUs, fundamentally altering the business models and power dynamics within the AI industry. The $10 billion fee for the Cursor deal is unusually high, reportedly constituting 17% of the $60 billion acquisition value, which is significantly above the typical 3-5% breakup fee in mergers and acquisitions.

rss · InfoQ 中文站 · May 21, 15:23

**Background**: AI companies like Anthropic require immense computational power to train and run their large language models, creating a fierce race for access to data centers and supercomputers. SpaceX, known for its reusable rockets and Starlink network, has been expanding into orbital data centers and high-performance computing, potentially using its satellite infrastructure to provide globally distributed AI compute resources.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/cnbc_spacex-says-it-can-buy-cursor-later-this-activity-7452491823928868864-G6cT">SpaceX acquires AI startup Cursor for $60B | CNBC posted on the topic | LinkedIn</a></li>
<li><a href="https://www.reddit.com/r/cursor/comments/1ss7z42/spacexs_60b_agreement_to_acquire_cursor_is_wild/">SpaceX's $60B agreement to acquire Cursor is wild, but the $10B fallback is crazier. - Reddit</a></li>
<li><a href="https://thenextweb.com/news/spacex-cursor-60-billion-acquisition">SpaceX secures option to buy AI coding startup Cursor for $60B - TNW</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#SpaceX`, `#Anthropic`, `#tech industry`, `#business models`

---

<a id="item-11"></a>
## [Alibaba releases new Qwen3.7-Max model, claimed as best domestic AI in China.](https://www.infoq.cn/article/jAICqmzYVqQ8sHdGSzEH?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Alibaba has launched its latest flagship large language model, Qwen3.7-Max, positioning it as the top-performing model developed domestically within China. This release intensifies the competition in China's AI sector, demonstrating rapid progress in domestic large language models and potentially influencing the broader technological and commercial AI landscape in the region. The model is described as a flagship release, but the provided content lacks specific technical benchmarks, parameter counts, or detailed comparisons against other models for independent verification.

rss · InfoQ 中文站 · May 21, 09:47

**Background**: Qwen is Alibaba Cloud's series of large language models, which have been actively developed and iterated upon as part of China's strategy to advance its domestic AI capabilities. The term 'domestic model' here refers to AI models primarily developed and trained within China, often as part of a national effort to achieve technological self-reliance.

**Tags**: `#large language models`, `#AI research`, `#Chinese tech`, `#Qwen`, `#model release`

---

<a id="item-12"></a>
## [Qt Bridges Enables C# Developers to Build UIs with the Qt Framework](https://www.v2ex.com/t/1214627#reply0) ⭐️ 8.0/10

Qt has released a public beta of Qt Bridges for C#, allowing developers to create C# objects that function as QML components within Qt Quick interfaces, and the next planned language for integration is Rust. This extension significantly lowers the barrier for the large C# developer community to leverage Qt's powerful cross-platform UI framework, potentially expanding Qt's ecosystem and enabling new hybrid application architectures. The beta allows reading/writing C# properties, calling C# methods, handling events, and binding QML properties to C# collections, aiming to let developers write backend code in a familiar C# style with minimal Qt-specific patterns.

rss · V2EX · May 22, 02:36

**Background**: Qt is a widely used cross-platform application development framework for creating graphical user interfaces, traditionally requiring C++ or QML. QML is a declarative language for designing UIs that can be integrated with backend logic written in languages like C++. Qt Bridges represents a new approach to expose Qt's capabilities to other languages without creating full, complex bindings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ics.com/blog/integrating-c-qml">Integrating C++ with QML | ICS</a></li>
<li><a href="https://ftp.nmr.mgh.harvard.edu/pub/dist/freesurfer/tutorial_packages_centos6/centos6/freesurfer-fsl-matlab-Linux-centos6_x86_64-dev/freesurfer/lib/qt/qt_doc/html/qtbinding.html">Qt 4.7: Using QML in C++ Applications</a></li>

</ul>
</details>

**Tags**: `#Qt`, `#C#`, `#UI Framework`, `#Cross-Language`, `#Software Development`

---

<a id="item-13"></a>
## [Microsoft Research Introduces Vega for Privacy-Preserving Digital Identity](https://www.microsoft.com/en-us/research/blog/vega-zero-knowledge-proofs-for-digital-identity-in-the-age-of-ai/) ⭐️ 8.0/10

Microsoft Research has introduced Vega, a zero-knowledge proof system that enables users to prove specific attributes from digital credentials, such as age or professional status, without revealing the full credential. This system addresses a critical need for privacy-preserving identity verification in the AI age, where digital credentials are increasingly used but risk exposing excessive personal data if shared directly. Vega efficiently converts a full credential into a single, selective proof, designed for real-world application performance, allowing verification of attributes like personhood or government-issued facts with minimal data exposure.

rss · Microsoft Research · May 21, 13:48

**Background**: Zero-knowledge proofs are cryptographic methods that allow one party to prove knowledge of specific information to another without revealing the information itself. Digital credentials, such as government IDs or professional certificates, are increasingly stored and verified electronically, creating a trade-off between convenience and privacy that systems like Vega aim to resolve.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/vega-zero-knowledge-proofs-for-digital-identity-in-the-age-of-ai/">Vega: Zero-knowledge proofs for digital identity in the age of AI - Microsoft Research</a></li>
<li><a href="https://eprint.iacr.org/2025/2094">Vega: Low-Latency Zero-Knowledge Proofs over Existing Credentials</a></li>

</ul>
</details>

**Tags**: `#zero-knowledge proofs`, `#digital identity`, `#privacy`, `#cryptography`, `#AI`

---

<a id="item-14"></a>
## [OpenAI's GPT-next model disproves Erdős's 80-year-old planar unit distance conjecture.](https://www.latent.space/p/ainews-openai-gpt-next-disproves) ⭐️ 8.0/10

OpenAI's internal model, GPT-next, has reportedly produced a counterexample that disproves the Erdős planar unit distance conjecture, a problem in discrete geometry open for over 80 years. This breakthrough demonstrates a major advance in AI's capability for formal mathematical reasoning and could significantly impact how AI is used to solve longstanding scientific problems. The conjecture posits that for a set of n points in the plane, the number of unit distances between them is at most O(n^{1+δ}) for some δ>0; the model's counterexample reportedly shows this bound can be exceeded.

rss · Latent Space · May 21, 07:28

**Background**: The Erdős planar unit distance conjecture is a famous problem in discrete geometry proposed by mathematician Paul Erdős, which concerns the maximum possible number of unit-length segments among n points in the plane. Discrete geometry deals with the combinatorial properties of geometric objects, and problems like this have been studied for decades to understand fundamental spatial arrangements.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry</a></li>
<li><a href="https://www.reddit.com/r/mathematics/comments/1tixy6x/openai_model_produces_a_counterexample_to_erdőss/">OpenAI model produces a counterexample to Erdős's conjectured unit-distance bound : r/mathematics - Reddit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Erdős_distinct_distances_problem">Erdős distinct distances problem - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Online discussions, such as on Reddit's r/mathematics and r/math subreddits, show significant interest and skepticism, with many commenters seeking more details about the model's methodology, the specific counterexample produced, and the verification process.

**Tags**: `#AI`, `#mathematics`, `#OpenAI`, `#research breakthrough`, `#formal reasoning`

---

<a id="item-15"></a>
## [Command injection vulnerability found in GTK-based PDF readers like Evince.](https://lwn.net/Articles/1073944/) ⭐️ 8.0/10

Michael Catanzaro has disclosed a command injection vulnerability affecting several GTK-based PDF readers, including Evince, Atril, and Xreader, which allows malicious polyglot PDFs that are also valid ELF binaries to execute arbitrary code when a user clicks a link. This vulnerability poses a significant real-world security risk because it enables arbitrary code execution on a user's system simply by opening a malicious PDF and clicking a link, affecting common Linux desktop applications. The exploit creates a polyglot file that is both a valid PDF and a valid ELF binary, abusing the `--gtk-module` command-line flag in GTK 3 to load itself as a module and run malicious code via its constructor; the vulnerability is less severe for GTK 4-based applications like Papers because this flag was removed.

rss · LWN.net · May 21, 21:05

**Background**: PDF readers like Evince are widely used on Linux desktops. A command injection vulnerability allows an attacker to execute arbitrary operating system commands through an application. ELF (Executable and Linkable Format) is the standard file format for executables on Linux and other Unix-like systems. GTK (GIMP Toolkit) is a popular toolkit for creating graphical user interfaces, and modules can be loaded to extend its functionality.

<details><summary>References</summary>
<ul>
<li><a href="https://seclists.org/oss-sec/2026/q2/643">oss-sec: Re: Evince/Atril/Xreader command injection CVE-2026-46529</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#PDF`, `#GTK`, `#Linux`

---

<a id="item-16"></a>
## [NVIDIA's Q4 revenue hits $68.1B, guides Q1 2027 to $78B on AI demand](https://t.me/zaihuapd/41498) ⭐️ 8.0/10

NVIDIA reported fourth-quarter fiscal 2026 revenue of $68.1 billion, surpassing market expectations, with its data center segment contributing $62.3 billion. The company also provided a strong first-quarter fiscal 2027 revenue guidance of $78 billion, significantly exceeding the analyst consensus of $72.6 billion. This performance underscores NVIDIA's dominant position in the AI hardware market and reflects the surging, sustained demand for its GPUs to power AI training and inference workloads across the data center industry. The elevated guidance signals continued exponential growth in AI compute infrastructure investment, impacting cloud providers, enterprises, and the broader semiconductor supply chain. Key details include earnings per share (EPS) of $1.62, which also beat expectations, and a post-earnings stock price surge of over 3% in after-hours trading. However, the report noted that revenue from its gaming and automotive segments fell short of forecasts.

telegram · zaihuapd · May 21, 05:10

**Background**: NVIDIA designs and sells graphics processing units (GPUs), which have become the foundational hardware for training and running large artificial intelligence models. The company's data center segment, which sells these GPUs and networking solutions for AI servers, has grown to become its largest revenue source, driven by massive capital expenditure from cloud hyperscalers and enterprises building AI infrastructure.

**Tags**: `#AI hardware`, `#semiconductor industry`, `#financial results`, `#data center`

---

<a id="item-17"></a>
## [黄仁勋：英伟达已基本放弃中国 AI 芯片市场](https://www.cnbc.com/2026/05/21/nvidia-jensen-huang-china-ai-chip-market-huawei.html) ⭐️ 8.0/10

Nvidia CEO Jensen Huang stated the company has 'basically given up' on China's AI chip market due to U.S. export controls, ceding ground to Huawei and local competitors.

telegram · zaihuapd · May 21, 05:52

**Tags**: `#AI hardware`, `#semiconductors`, `#geopolitics`, `#NVIDIA`, `#export controls`

---

<a id="item-18"></a>
## [OpenAI Codex Gains Ability to Control Mac Apps While Screen is Locked](https://x.com/OpenAIDevs/status/2057536706778378692) ⭐️ 8.0/10

OpenAI has added a new 'Lock Screen Usage' feature to Codex's Computer Use capability, allowing the AI to continue operating approved applications on a Mac even when the display is locked or off. This functionality is accessible and controllable from connected devices like a smartphone. This feature significantly enhances the utility of AI agents for developers by enabling background automation and remote task management without requiring the Mac's screen to be active, potentially streamlining long-running coding or operational tasks. It represents a step forward in practical, persistent AI assistance integrated directly into the operating system. The feature is currently available only on macOS and is initially launched with a geographic restriction, excluding the European Economic Area, the United Kingdom, and Switzerland. Before use, users must install a plugin and grant specific permissions for screen recording and accessibility; the temporary unlock for control is limited to the duration of the current task and will re-lock upon detecting local input.

telegram · zaihuapd · May 22, 00:58

**Background**: Codex is an AI-powered coding agent from OpenAI designed to assist developers by understanding and executing commands within integrated development environments and operating systems. The 'Computer Use' capability allows AI models to visually perceive and interact with a computer's graphical user interface, a fundamental aspect for building autonomous AI agents. Granting screen recording and accessibility permissions on macOS is a standard requirement for any software, including remote control and AI agent tools, to legally interact with and control the desktop environment.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Ylianst/MeshCentral/issues/4824">Screen Recording access permission does not work with MacOS Agent · Issue #4824 · Ylianst/MeshCentral - GitHub</a></li>
<li><a href="https://jumpcloud.com/support/grant-screen-recording-and-accessibility-permissions-for-remote-assist-agent-on-macos-devices">Grant Required Permissions for the Remote Assist Agent on macOS Devices - JumpCloud</a></li>

</ul>
</details>

**Tags**: `#AI_agents`, `#OpenAI_Codex`, `#productivity`, `#macOS`, `#remote_control`

---