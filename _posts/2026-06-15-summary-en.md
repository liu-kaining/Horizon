---
layout: default
title: "Horizon Summary: 2026-06-15 (EN)"
date: 2026-06-15
lang: en
---

> From 178 items, 9 important content pieces were selected

---

1. [Linux Kernel 7.1 Released with Major Architectural Changes and New Features](#item-1) ⭐️ 10.0/10
2. [Tsinghua team discovers memory reactivation bidirectionally regulates sleep, published in Science](#item-2) ⭐️ 8.0/10
3. [OpenAI GPT-5.5 and Codex Models Launch on Amazon Bedrock](#item-3) ⭐️ 8.0/10
4. [RustWeek talk explores extreme-speed FFI testing with Miri](#item-4) ⭐️ 8.0/10
5. [Apple's Siri AI privacy model critically examined for privacy flaws.](#item-5) ⭐️ 8.0/10
6. [Guide Doubles RTX 3070 VRAM to 16GB via Memory Chip Swap](#item-6) ⭐️ 8.0/10
7. [Huawei Releases Open-Source Pangu 2.0 AI Models with 505B and 92B Parameters](#item-7) ⭐️ 8.0/10
8. [Anthropic Suspends Mythos 5 and Fable 5 Access Following US Export Control Order](#item-8) ⭐️ 8.0/10
9. [First Global Map of Underground Fungal Networks Reveals Immense Scale and Carbon Role](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Linux Kernel 7.1 Released with Major Architectural Changes and New Features](https://lwn.net/Articles/1077758/) ⭐️ 10.0/10

Linux kernel version 7.1 has been officially released, introducing significant changes including the removal of support for some older 486-based architectures, new process management `clone()` flags, BPF support for the io_uring asynchronous I/O interface, and a completely rewritten NTFS file system implementation. As a foundational technology powering servers, desktops, and embedded devices worldwide, a major stable kernel release directly impacts system stability, performance, and hardware support for countless systems, while new features like enhanced schedulers and I/O capabilities provide developers and administrators with powerful new tools. Key additions include initial sub-scheduler support in the extensible scheduler class (sched_ext) for hierarchical scheduling, zero-copy I/O for the ublk user-space block driver, and various swapping improvements. The release also represents ongoing cleanup by removing support for legacy CPU architectures.

rss · LWN.net · Jun 14, 18:47

**Background**: The Linux kernel is the core component of the Linux operating system, managing hardware resources and providing essential services for all software. io_uring is a high-performance asynchronous I/O interface designed to reduce system call overhead for storage operations. The sched_ext framework allows developers to implement and load custom CPU schedulers via BPF programs, offering unprecedented flexibility in workload management.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">Io uring</a></li>
<li><a href="https://docs.kernel.org/block/ublk.html">Userspace block device driver (ublk driver) — The Linux Kernel documentation</a></li>
<li><a href="https://www.phoronix.com/news/cgroup-sub-scheduler-sched-ext">Sub-Scheduler Support Could Be One Of The Most Exciting Features To Come For Linux 7.1 - Phoronix</a></li>

</ul>
</details>

**Tags**: `#linux`, `#kernel`, `#open-source`, `#operating-systems`, `#software-release`

---

<a id="item-2"></a>
## [Tsinghua team discovers memory reactivation bidirectionally regulates sleep, published in Science](https://www.ithome.com/0/964/240.htm) ⭐️ 8.0/10

A joint research team from Tsinghua University and the Beijing Academy of Artificial Intelligence published a study in Science for the first time demonstrating that memory reactivation during sleep can actively regulate sleep states, and that memory, in turn, affects sleep. This finding establishes a bidirectional mechanism between memory and sleep, challenging the traditional view that sleep only promotes memory consolidation, and identifies memory engram cells as potential therapeutic targets for sleep disorders linked to depression and chronic stress. Negative memories (e.g., from fear experiences) reactivate during non-REM sleep to promote transitions to wakefulness, fragmenting sleep, while positive memory reactivation promotes and sustains non-REM sleep, with these opposing effects mediated by distinct downstream neural pathways.

rss · IT HOME · Jun 15, 01:49

**Background**: Traditional sleep research has largely focused on how sleep processes and consolidates memories, but the reverse influence—that memories can actively shape sleep architecture—has been less understood. Sleep is broadly categorized into non-rapid eye movement (NREM) and rapid eye movement (REM) stages, with NREM sleep being particularly important for restorative functions and memory consolidation. Memory engram cells are specific neural populations that are activated during an experience and are thought to store the memory trace of that event.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tsinghua.edu.cn/info/1175/126722.htm">生命学院钟毅团队合作揭示记忆重激活调节睡眠的神经机制</a></li>
<li><a href="https://www.ithome.com/0/964/240.htm">为什么压力大会睡不好，清华团队新发现登上 Science - IT之家</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#sleep research`, `#memory`, `#brain science`, `#scientific breakthrough`

---

<a id="item-3"></a>
## [OpenAI GPT-5.5 and Codex Models Launch on Amazon Bedrock](https://www.infoq.cn/article/FuhAEYbk8T0b0GQZyq4c?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

OpenAI's latest GPT-5.5 language model and its Codex coding model are now officially available as integrated options within Amazon's Bedrock AI service. This integration provides enterprise customers on AWS with direct, managed access to OpenAI's cutting-edge models, significantly simplifying the process of building generative AI applications without managing underlying infrastructure. Amazon Bedrock is a fully managed AWS service that offers a unified API to access foundation models from various AI providers, now including OpenAI's GPT-5.5 and Codex.

rss · InfoQ 中文站 · Jun 14, 10:00

**Background**: Amazon Bedrock is a cloud service launched in 2023 that allows developers to build generative AI applications by accessing models from multiple companies through a single API. OpenAI's Codex is a specialized AI model designed for coding tasks, derived from its GPT lineage, which powers tools like GitHub Copilot.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Bedrock">Amazon Bedrock - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production scale – AWS</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cloud Computing`, `#OpenAI`, `#Amazon Web Services`, `#GPT`

---

<a id="item-4"></a>
## [RustWeek talk explores extreme-speed FFI testing with Miri](https://youtu.be/9X-ngiKo_Y0) ⭐️ 8.0/10

At RustWeek, Nia Deckers presented a talk demonstrating how to use Miri to run and test foreign function interface (FFI) code at extreme speeds, achieving up to 8000 segfaults per second. Testing FFI code for memory safety is a major challenge in Rust development, and this approach offers a way to detect unsafe behavior at high speed, potentially improving the security and reliability of Rust projects that interface with C/C++ libraries. Miri is a Rust interpreter that detects undefined behavior, but its application to FFI code is challenging because FFI calls involve raw pointers and fall outside Rust's safe memory model.

rss · Lobsters · Jun 14, 17:12

**Background**: Miri is an experimental interpreter for Rust's mid-level intermediate representation (MIR) that can detect various forms of undefined behavior during testing. Foreign Function Interface (FFI) allows Rust to call code written in other languages like C, but this requires using unsafe Rust and handling raw pointers, which can lead to memory safety issues such as segmentation faults. Segmentation faults occur when a program tries to access restricted memory, often indicating bugs like dangling pointers or buffer overflows.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/rust-lang/miri/">GitHub - rust-lang/miri: An interpreter for Rust's mid-level intermediate representation · GitHub</a></li>
<li><a href="https://doc.rust-lang.org/nomicon/ffi.html">Foreign Function Interface - Learn Rust</a></li>
<li><a href="https://en.wikipedia.org/wiki/Segmentation_fault">Segmentation fault - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion likely provides valuable community insights on the practical challenges and potential of using Miri for FFI testing, though the specific comments are not provided here.

**Tags**: `#Rust`, `#FFI`, `#Miri`, `#Testing`, `#Memory Safety`

---

<a id="item-5"></a>
## [Apple's Siri AI privacy model critically examined for privacy flaws.](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/) ⭐️ 8.0/10

A recent analysis argues that Apple's implementation of private inference for its Siri AI assistant is insufficient to guarantee true user privacy, highlighting a gap between the company's marketing claims and the technical reality. This critique is significant as it challenges the foundational privacy promises of a major tech platform's AI product, raising broader industry concerns about whether current privacy-preserving computation techniques can live up to their stated goals for consumer applications. The analysis specifically critiques techniques like differential privacy, secure multi-party computation, and homomorphic encryption as applied to AI model inference, suggesting they may leave residual privacy vulnerabilities or performance trade-offs that are not adequately communicated to users.

rss · Lobsters · Jun 14, 03:50

**Background**: Private inference refers to techniques that allow an AI model to process user data without the service provider seeing the raw data or model details. Apple has promoted Siri's on-device processing and 'Private Cloud Compute' as privacy safeguards. Key technologies involved include differential privacy (adding statistical noise to data), secure multi-party computation (MPC), which allows multiple parties to jointly compute a function without revealing their individual inputs, and homomorphic encryption (HE), which enables computation directly on encrypted data.

<details><summary>References</summary>
<ul>
<li><a href="https://subscription.packtpub.com/book/data/9781800564671/7/ch07lvl1sec30/protecting-against-membership-inference-attacks">Chapter 5: Developing Applications with Differential Privacy Using...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>
<li><a href="https://ai.meta.com/research/publications/crypten-secure-multi-party-computation-meets-machine-learning/">CrypTen: Secure Multi-Party Computation Meets Machine Learning | Research - AI at Meta</a></li>

</ul>
</details>

**Discussion**: The linked Lobsters discussion likely contains substantive technical debate among developers and privacy researchers, focusing on the specific technical limitations of the mentioned privacy-preserving techniques and the feasibility of achieving strong privacy guarantees in commercial AI systems.

**Tags**: `#AI privacy`, `#Apple Siri`, `#cryptography`, `#machine learning`, `#privacy-preserving computation`

---

<a id="item-6"></a>
## [Guide Doubles RTX 3070 VRAM to 16GB via Memory Chip Swap](https://hackaday.com/2026/06/14/double-the-vram-of-an-rtx-3070/) ⭐️ 8.0/10

A detailed hardware modification guide has been published, outlining the step-by-step process of physically swapping the GDDR6 memory chips on an NVIDIA RTX 3070 graphics card to double its VRAM capacity from 8GB to 16GB. This modification allows users to overcome the VRAM limitations of a popular mid-range GPU, potentially extending its useful life for modern games and AI/ML workloads that increasingly demand more video memory. The modification is highly technical, requiring advanced soldering skills to desolder the existing memory chips and replace them with higher-capacity modules, and success depends on having the correct PCB schematics and ensuring firmware compatibility.

rss · Hackaday · Jun 14, 08:00

**Background**: The NVIDIA GeForce RTX 3070, a widely used graphics card from the Ampere generation, was originally equipped with 8GB of GDDR6 memory. VRAM (Video Random Access Memory) is critical for storing textures, frame buffers, and other data for the GPU; insufficient VRAM can severely limit performance in high-resolution gaming and complex compute tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GDDR6_SDRAM">GDDR6 SDRAM - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/pcmasterrace/comments/12a2iz0/can_we_buy_micron_gddr6x_memory_chips_and/">r/pcmasterrace on Reddit: Can we buy micron GDDR6X memory chips and soldered them in to Graphics cards? Asking for a friend. He wants his 3070 Ti to 16GB</a></li>
<li><a href="https://forums.tomshardware.com/threads/upgrading-memory-modules-on-a-gpu.3714591/">[SOLVED] - Upgrading memory modules on a GPU | Tom's Hardware Forum</a></li>

</ul>
</details>

**Discussion**: While the guide presents a novel approach, community discussions on forums like Reddit and Tom's Hardware indicate that such modifications are extremely risky, often considered impractical by the average user, and may be impossible due to hardware locks or difficulty sourcing the exact memory chips.

**Tags**: `#GPU`, `#hardware modding`, `#VRAM`, `#PC gaming`, `#hardware engineering`

---

<a id="item-7"></a>
## [Huawei Releases Open-Source Pangu 2.0 AI Models with 505B and 92B Parameters](https://t.me/zaihuapd/41948) ⭐️ 8.0/10

At HDC 2026, Huawei announced the open-source release of its Pangu 2.0 large language model family, which includes a 505-billion-parameter Pro version and a 92-billion-parameter Flash version, both optimized for its own Ascend NPUs and HarmonyOS ecosystem. This release significantly boosts China's domestic AI ecosystem by providing a high-performance, open-source alternative to models from Western companies, directly challenging global leadership and potentially accelerating AI adoption across industries using Huawei's hardware and software stack. The model supports an extended context window of 512,000 tokens, with the Pro version using 18 billion active parameters and the Flash version using 6 billion active parameters, and Huawei plans to open-source seven major components including pre-training code starting June 30th.

telegram · zaihuapd · Jun 14, 08:05

**Background**: The Ascend NPUs are Huawei's proprietary AI accelerators, designed as a key part of its strategy to build a self-reliant AI technology stack independent of NVIDIA GPUs. HarmonyOS is Huawei's distributed operating system for a wide range of devices, and the new HarmonyOS 6 includes an AI agent framework to deeply integrate AI capabilities. Large Language Models (LLMs) like Pangu are deep learning models trained on vast text datasets to understand and generate human language.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/openpangu-2-complete-guide/">openPangu 2.0 Complete Guide: Huawei's 505B Model Trained ...</a></li>
<li><a href="https://www.panewslab.com/en/articles/019ebb7d-77a4-75e9-a5bc-e11af8f55293">Huawei releases open-source large-scale model Pangu 2.0: up ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarmonyOS">HarmonyOS - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#Large Language Models`, `#Huawei`, `#Natural Language Processing`

---

<a id="item-8"></a>
## [Anthropic Suspends Mythos 5 and Fable 5 Access Following US Export Control Order](https://t.me/zaihuapd/41949) ⭐️ 8.0/10

Anthropic has temporarily shut down global access to its most advanced AI models, Claude Fable 5 and Claude Mythos 5, for all customers, including foreign nationals within the U.S., after receiving a U.S. government export control directive citing national security concerns. This action represents a significant and precedent-setting government intervention in the AI industry, highlighting the growing intersection of advanced AI capabilities and national security policy, which could impact the international accessibility of cutting-edge AI technology and set a new regulatory precedent. The U.S. Department of Commerce's directive specifically targets the suspension of access for all foreign nationals without providing Anthropic with specific details of the national security risk, which is reportedly linked to concerns over the models being 'jailbroken' for potential misuse; other Claude model tiers remain unaffected.

telegram · zaihuapd · Jun 14, 09:06

**Background**: Claude Fable 5 and Claude Mythos 5 are Anthropic's latest and most powerful AI models, released just days ago as part of the 'Mythos-class' capabilities designed for complex, long-running projects. 'Jailbreaking' refers to techniques that circumvent an AI model's safety training to make it produce restricted or harmful outputs, a growing concern as models become more capable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/technology/us-blocks-foreign-access-anthropics-most-advanced-ai-models-axios-reports-2026-06-13/">Anthropic disables top-tier AI models after US order limiting ...</a></li>
<li><a href="https://samsearch.co/government-contracting-news/us-export-controls-force-anthropic-to-suspend-global-access-to-ai-models-114075">U.S. Export Controls Force Anthropic to Suspend Global Access ...</a></li>
<li><a href="https://aisecurityandsafety.org/en/guides/jailbreaking-attacks/">Jailbreaking AI Models: Attack Patterns, Examples & Defenses ...</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#export controls`, `#Anthropic`, `#model access restrictions`, `#national security`

---

<a id="item-9"></a>
## [First Global Map of Underground Fungal Networks Reveals Immense Scale and Carbon Role](https://insideclimatenews.org/news/11062026/earths-massive-underground-fungal-networks/) ⭐️ 8.0/10

Led by the Society for the Protection of Underground Networks (SPUN), researchers have created the first global map of arbuscular mycorrhizal fungal networks. The map shows the subterranean hyphae span over 100 quadrillion kilometers, a distance nearly a billion times that between Earth and the Sun, and have a total mass about five times that of the entire human population. This mapping reveals the critical ecological significance of mycorrhizal networks, which are shown to partner with about 80% of global plants and sequester approximately one billion tons of carbon underground annually. The findings have major implications for understanding climate change mitigation, agricultural sustainability, and ecosystem conservation strategies. The map indicates that fungal density in farmland is only about half of that found in wild ecosystems, and wild grasslands—home to approximately 40% of the studied fungal biomass—are being converted to farmland at a rate four times faster than forests. This suggests that agricultural expansion poses a specific and significant threat to these vital underground networks.

telegram · zaihuapd · Jun 14, 14:58

**Background**: Arbuscular mycorrhizal fungi (AMF) are a type of symbiotic fungi that form intricate networks, known as the 'Wood Wide Web,' connecting plant roots underground. These networks facilitate the exchange of nutrients, such as phosphorus and nitrogen from the soil, for carbon (sugars) from the plants. This symbiosis is fundamental to plant health and ecosystem productivity, and the fungi's role in sequestering carbon in stable forms within the soil is a key area of climate science research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.livescience.com/planet-earth/plants/earths-underground-fungal-network-is-so-massive-it-would-span-10-percent-of-the-milky-way-map-reveals">Earth's underground fungal network is so massive, it would span 10% of ...</a></li>
<li><a href="https://www.theguardian.com/science/2026/jun/11/arbuscular-mycorrhizal-fungi-plant-life-climate-global-mapping-study">Subterranean fungi networks more than 100 quadrillion km in length ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s44447-025-00023-w">Arbuscular mycorrhizal fungi (AMF): a pathway to sustainable soil...</a></li>

</ul>
</details>

**Tags**: `#mycorrhizal_fungi`, `#ecology`, `#climate_science`, `#carbon_sequestration`, `#environmental_mapping`

---