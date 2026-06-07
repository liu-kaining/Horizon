---
layout: default
title: "Horizon Summary: 2026-06-07 (EN)"
date: 2026-06-07
lang: en
---

> From 169 items, 13 important content pieces were selected

---

1. [Astronomers detect black hole wind from Milky Way's central supermassive black hole](#item-1) ⭐️ 9.0/10
2. [China's First Invasive BCI Restores Vision to Patient Blind for 20 Years](#item-2) ⭐️ 9.0/10
3. [Exploring Alternatives to Traditional Unix fork() and exec() Process Creation](#item-3) ⭐️ 8.0/10
4. [US Advances Military AI, Mandates 90-Day Autonomous Weapons Rule Revision](#item-4) ⭐️ 8.0/10
5. [Webb telescope measures dormant black hole mass 10 billion light-years away](#item-5) ⭐️ 8.0/10
6. [China Achieves Breakthrough in 50% Green Hydrogen and 100% Pure Hydrogen Coal Co-firing](#item-6) ⭐️ 8.0/10
7. [Microsoft Warns Claude Code Flaw Could Leak GitHub Credentials](#item-7) ⭐️ 8.0/10
8. [Elon Musk to attend closed-door ASML seminar on TeraFab project](#item-8) ⭐️ 8.0/10
9. [Next.js 16.2 Boosts Dev Speed 4x, Adds AI Agent Tools](#item-9) ⭐️ 8.0/10
10. [Smart TVs covertly exploited as nodes in the AI data scraping economy.](#item-10) ⭐️ 8.0/10
11. [Research Proposes 'AI Worms' That Self-Replicate Across AI Agents](#item-11) ⭐️ 8.0/10
12. [Magecart skimmer repurposes Stripe API as covert command-and-control server.](#item-12) ⭐️ 8.0/10
13. [Google Pays SpaceX $9.2 Billion for AI Compute Lease Through 2029](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Astronomers detect black hole wind from Milky Way's central supermassive black hole](https://www.ithome.com/0/961/038.htm) ⭐️ 9.0/10

Astronomers have obtained the first direct observational evidence of a 'black hole wind' emanating from Sagittarius A*, the supermassive black hole at the Milky Way's center, resolving a 50-year-old puzzle. The discovery was made using deep observation data from the ALMA telescope array, revealing a cone-shaped cavity in the surrounding molecular gas. This breakthrough confirms that even very quiet, low-accretion supermassive black holes like Sgr A* can drive powerful winds, challenging previous assumptions and significantly advancing our understanding of black hole accretion physics and galactic center dynamics. It suggests that most galaxies in the universe, which exist in similarly quiet states, may also host such winds, providing a more complete picture of how black holes influence their host galaxies. The observed wind is relatively gentle but has been blowing for an estimated 20,000 years, and its discovery required observations that could penetrate the dense gas and dust of the galactic plane. The research team used data from both the ALMA array and NASA's Chandra X-ray Observatory, with the X-ray data confirming the presence of radiation in the cavity, providing robust evidence against the phenomenon being a mere observational artifact.

rss · IT HOME · Jun 7, 03:09

**Background**: Black holes do not simply swallow all nearby matter; as they accrete gas and dust, they can expel a significant portion of this material outward in the form of powerful winds or jets. The supermassive black hole at the center of our galaxy, Sagittarius A*, is relatively quiet, accreting very little material compared to active galactic nuclei, making it a challenging target for observing such outflow phenomena.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencenews.org/article/milky-way-supermassive-black-hole-wind">Even quiet black holes create winds, new Milky Way observations reveal</a></li>
<li><a href="https://iopscience.iop.org/article/10.3847/2041-8213/ae63cf">The Discovery of an Active Wind from the Milky Way’s Central Black Hole - IOPscience</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sagittarius_A*">Sagittarius A* - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#astronomy`, `#black-holes`, `#astrophysics`, `#scientific-discovery`, `#milky-way`

---

<a id="item-2"></a>
## [China's First Invasive BCI Restores Vision to Patient Blind for 20 Years](https://www.ithome.com/0/960/883.htm) ⭐️ 9.0/10

A clinical trial at Xiangya Hospital successfully used China's first invasive brain-computer interface, the IMIE intelligent retinal system, to restore partial vision to a 61-year-old patient who had been blind for 20 years due to retinitis pigmentosa, achieving a post-operative visual acuity of 0.03. This is a major breakthrough in neurotechnology and assistive devices, demonstrating the clinical viability of a high-channel-count invasive BCI for vision restoration and offering new hope for patients with certain types of blindness. The IMIE system uses a 256-channel flexible electrode array to bypass damaged photoreceptors and directly transmit visual signals to the brain, a channel count more than four times greater than comparable international products like the Argus II. The patient requires ongoing rehabilitation training to further improve visual perception and daily living skills.

telegram · zaihuapd · Jun 6, 07:30

**Background**: A brain-computer interface (BCI) establishes a direct communication pathway between the brain and external devices. Retinal implants, such as the Argus II, are a type of BCI designed to restore some vision to patients blinded by diseases like retinitis pigmentosa (RP), which causes the progressive degeneration of photoreceptor cells in the retina. The number of electrodes in an implant's array is a key factor in determining the resolution of the restored vision, with higher channel counts offering the potential for more detailed perception.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retinal_implant">Retinal implant - Wikipedia</a></li>
<li><a href="https://news.cgtn.com/news/2026-06-06/What-is-a-brain-computer-interface-and-how-does-it-work--1NLhMnzzybm/p.html">What is a brain - computer interface , and how does it work? - CGTN</a></li>

</ul>
</details>

**Tags**: `#brain-computer-interface`, `#medical-breakthrough`, `#neurotechnology`, `#vision-restoration`, `#clinical-trial`

---

<a id="item-3"></a>
## [Exploring Alternatives to Traditional Unix fork() and exec() Process Creation](https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/) ⭐️ 8.0/10

A detailed technical article examines the inefficiencies and safety concerns of the classic Unix fork() followed by exec() model for starting new processes, and discusses modern system calls like posix_spawn and clone as potential replacements. This discussion is significant because the fork()+exec() model is a foundational part of Unix-like operating systems, and its inefficiencies impact performance, security, and code complexity in systems programming and application development. Key modern alternatives include posix_spawn(), which combines process creation and image execution in a single call, and the more flexible but Linux-specific clone() syscall, which allows fine-grained control over which resources are shared between parent and child.

hackernews · Lobsters · Jun 6, 14:34 · [Discussion](https://news.ycombinator.com/item?id=48425528)

**Background**: The traditional Unix process creation uses fork() to duplicate the calling process, creating a child that is a near-identical copy, and then exec() in the child to replace its memory image with a new program. This model, while elegant in its simplicity, is considered inefficient because fork() must copy the entire process state, including memory, a cost that is often wasted when exec() immediately discards that copy to load a new program.

<details><summary>References</summary>
<ul>
<li><a href="https://pubs.opengroup.org/onlinepubs/9799919799/functions/posix_spawn.html">posix _ spawn</a></li>
<li><a href="https://www.man7.org/linux/man-pages/man2/clone.2.html">clone(2) - Linux manual page</a></li>

</ul>
</details>

**Discussion**: The community discussion references a Microsoft research paper titled 'A fork() in the road' which argues fork is an outdated liability. Comments debate the elegance versus inefficiency of the fork+exec model, with some defending its flexibility for post-fork configuration and others sharing practical bugs related to file descriptor leaks in forked processes.

**Tags**: `#operating systems`, `#systems programming`, `#process management`, `#Unix design`

---

<a id="item-4"></a>
## [US Advances Military AI, Mandates 90-Day Autonomous Weapons Rule Revision](https://www.ithome.com/0/961/014.htm) ⭐️ 8.0/10

The U.S. government announced it will accelerate AI integration into national security, requiring leading AI developers to voluntarily submit top models for government cybersecurity testing before public release. President Trump instructed the Defense Secretary to revise existing directives on autonomous weapons within 90 days to ensure AI systems respect the chain of command, while prohibiting AI use for illegal surveillance or censorship. This policy shift signifies the U.S. government's direct push to harness AI for military superiority while attempting to set ethical boundaries, directly impacting the defense industry and major AI developers like Anthropic. It highlights the growing tension between rapid AI deployment for national security and corporate ethics policies, setting a precedent for how democratic nations govern military AI. The memorandum promotes adopting AI from multiple vendors to avoid single points of failure and updates guidelines for autonomous weapons systems to keep pace with cutting-edge technology. This move comes amid a public conflict with Anthropic, which the Pentagon previously designated as a 'supply chain risk entity' after the company refused to lift bans on using its Claude model for autonomous weapons and mass domestic surveillance.

rss · IT HOME · Jun 7, 01:18

**Background**: The U.S. Department of Defense has long-standing directives, such as Directive 3000.09, which govern the development and use of autonomous and semi-autonomous weapons systems. The term 'supply chain risk entity' is a designation previously used by the Pentagon against foreign companies like Huawei, and its application to a U.S.-based AI firm like Anthropic is a rare and significant step reflecting deep policy disagreements on military AI ethics.

<details><summary>References</summary>
<ul>
<li><a href="https://thenextweb.com/news/trump-signs-downsized-ai-executive-order-voluntary-review">Trump signs narrowed AI order with voluntary 30-day model review</a></li>
<li><a href="https://en.sedaily.com/international/2026/02/27/pentagon-moves-to-designate-anthropic-as-supply-chain-risk">Pentagon Moves to Designate Anthropic as Supply Chain Risk</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapon">Lethal autonomous weapon - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Policy`, `#Military AI`, `#Government Regulation`, `#Autonomous Weapons`, `#US Government`

---

<a id="item-5"></a>
## [Webb telescope measures dormant black hole mass 10 billion light-years away](https://www.ithome.com/0/960/997.htm) ⭐️ 8.0/10

Astronomers using the James Webb Space Telescope and gravitational lensing directly measured the mass of a dormant supermassive black hole in galaxy MRG-M0138 for the first time, finding it to be approximately 6 billion times the mass of the Sun. This breakthrough allows scientists to study the co-evolution of black holes and galaxies in the early universe, providing the first evidence that such massive, dormant black holes existed and grew rapidly when the cosmos was only 3 billion years old. The team, led by Andrew Newman of the Carnegie Observatories, leveraged a foreground galaxy cluster acting as a gravitational lens to magnify the distant galaxy MRG-M0138 by about 30 times, enabling detailed observations of stellar motions around the dormant black hole.

rss · IT HOME · Jun 6, 23:36

**Background**: A dormant supermassive black hole is one that is not actively accreting significant amounts of matter, making it nearly invisible except for its gravitational influence on surrounding stars. Scientists typically measure black hole mass by observing the orbital velocities of stars in its gravitational sphere of influence, a method previously limited to relatively nearby galaxies. Gravitational lensing, an effect predicted by Einstein's general relativity, occurs when a massive foreground object bends and magnifies light from a more distant background source.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gravitational_lens">Gravitational lens - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supermassive_black_hole">Supermassive black hole - Wikipedia</a></li>
<li><a href="https://phys.org/news/2026-06-jwst-dormant-black-hole-billion.html">JWST 'weighs' dormant black hole 10 billion light-years away</a></li>

</ul>
</details>

**Tags**: `#astronomy`, `#black-holes`, `#James-Webb-Space-Telescope`, `#astrophysics`

---

<a id="item-6"></a>
## [China Achieves Breakthrough in 50% Green Hydrogen and 100% Pure Hydrogen Coal Co-firing](https://www.ithome.com/0/960/996.htm) ⭐️ 8.0/10

China has successfully demonstrated a self-developed hydrogen-coal co-firing technology for the first time, achieving 50% green hydrogen co-firing by heat ratio and 100% pure hydrogen combustion, while also controlling nitrogen oxide emissions. This breakthrough provides a significant potential pathway for deep decarbonization of China's massive coal-fired power fleet, which is critical for achieving the country's 'dual carbon' goals and advancing the integration of coal power with new energy sources. The technology uses a domestically developed low-nitrogen hydrogen-coal co-firing burner and a full-process safety system for hydrogen delivery and combustion, achieving a 50% coal savings and carbon reduction potential when using green hydrogen.

rss · IT HOME · Jun 6, 23:24

**Background**: Hydrogen co-firing in thermal power plants is a global strategy for reducing carbon emissions from existing fossil fuel infrastructure. Green hydrogen, produced via electrolysis using renewable energy, offers a zero-carbon alternative fuel. China operates the world's largest fleet of coal-fired power plants, making their decarbonization a major challenge and priority for its climate commitments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.powergenadvancement.com/operations-maintenance/hydrogen-co-firing-in-thermal-power-path-to-decarbonization/">Hydrogen Co-Firing in Thermal Power: Path to Decarbonization</a></li>
<li><a href="https://www.siemens-energy.com/us/en/home/stories/constellation-hydrogen-co-firing.html">Hydrogen co-firing at Constellation Energy's Hillabee plant</a></li>
<li><a href="https://www.researchgate.net/publication/378353755_Numerical_Simulation_of_Hydrogen-Coal_Blending_Combustion_in_a_660_MW_Tangential_Boiler">(PDF) Numerical Simulation of Hydrogen – Coal Blending Combustion...</a></li>

</ul>
</details>

**Tags**: `#clean energy`, `#hydrogen energy`, `#carbon reduction`, `#power generation`, `#energy technology`

---

<a id="item-7"></a>
## [Microsoft Warns Claude Code Flaw Could Leak GitHub Credentials](https://www.ithome.com/0/960/994.htm) ⭐️ 8.0/10

Microsoft researchers discovered a prompt injection vulnerability in Anthropic's Claude Code GitHub automation that could leak GitHub account credentials through CI/CD workflows. Anthropic fixed the issue in Claude Code version 2.1.128, released on May 5. This vulnerability highlights the growing security risks of integrating AI agents into critical development pipelines like CI/CD, where a single exploit can compromise sensitive credentials across many projects. It underscores the need for robust sandboxing and input validation for all LLM tools, not just the most obvious ones. The attack exploited the fact that Claude Code's file-reading tool lacked the same sandbox restrictions as its Bash tool, allowing it to access sensitive system files like /proc/ after bypassing two layers of security via a prompt injected into a GitHub issue. The vulnerability was reported to Anthropic on April 29 and required no special repository permissions for an attacker to trigger.

rss · IT HOME · Jun 6, 23:20

**Background**: Prompt injection is a type of AI security vulnerability where an attacker embeds malicious instructions within content that an AI model processes, causing it to deviate from its intended behavior and execute unauthorized commands. In CI/CD pipelines, AI agents are increasingly used to automate tasks like triaging issues, generating code, and deploying applications, making these pipelines a new attack surface. Sandboxing is a security mechanism that isolates a running program to limit its access to the host system, which is crucial for preventing LLM agents from performing harmful actions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code-action">GitHub - anthropics/ claude - code -action · GitHub</a></li>
<li><a href="https://www.tech-channels.com/techchannels-blog/prompt-injection-attack-exploits-weak-spot-in-ci/cd-pipelines">Prompt Injection Attack Exploits Weak Spot in CI / CD Pipelines</a></li>
<li><a href="https://github.com/siawkz/llm-sandbox">GitHub - siawkz/ llm -sandbox: Secure Docker-based sandbox system...</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Vulnerability Disclosure`, `#Prompt Injection`, `#GitHub Actions`, `#CI/CD`

---

<a id="item-8"></a>
## [Elon Musk to attend closed-door ASML seminar on TeraFab project](https://www.ithome.com/0/960/988.htm) ⭐️ 8.0/10

Elon Musk will virtually participate in a closed-door technical seminar hosted by ASML to discuss his TeraFab semiconductor factory project, which ASML considers a serious endeavor. This meeting signals direct collaboration between one of the world's most influential entrepreneurs and the sole supplier of essential EUV lithography machines, potentially reshaping future semiconductor manufacturing capacity and supply chains. The TeraFab project is a joint venture involving SpaceX, Tesla, and Intel, with plans to build massive, vertically integrated chip factories in Texas, requiring investments potentially exceeding $100 billion and facing skepticism from industry leaders like TSMC.

rss · IT HOME · Jun 6, 15:37

**Background**: ASML is a Dutch company and the world's sole manufacturer of Extreme Ultraviolet (EUV) lithography machines, which are indispensable for producing the most advanced semiconductor chips. The TeraFab project aims to establish massive, integrated fabs to produce logic, memory, and advanced packaged chips to meet Musk's predicted surge in demand for AI chips from his companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Terafab">Terafab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ASML">ASML - Wikipedia</a></li>
<li><a href="https://www.manufacturingdive.com/news/elon-musk-build-advanced-chip-factories-austin-texas-spacex-tesla-xai/815542/">Musk's SpaceX to invest up to $119B on Terafab project | Manufacturing Dive</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#manufacturing`, `#ElonMusk`, `#ASML`, `#TeraFab`

---

<a id="item-9"></a>
## [Next.js 16.2 Boosts Dev Speed 4x, Adds AI Agent Tools](https://www.infoq.cn/article/NWjH4oTh0j4HsxJsCRaf?utm_source=rss&utm_medium=article) ⭐️ 8.0/10

Next.js version 16.2 has been released, featuring a claimed 4x improvement in development speed, rendering performance optimizations, and new tooling specifically designed for building AI agent applications. This release is significant as it directly addresses two major trends: improving developer productivity and supporting the growing demand for integrating advanced AI capabilities, particularly autonomous agents, directly into web frameworks. The performance claims are substantial, though the specific mechanisms for the 4x dev speed boost are not detailed in the provided summary. The new AI tooling aligns with Vercel's open-source AI SDK, suggesting deep integration for building agents within the Next.js ecosystem.

rss · InfoQ 中文站 · Jun 6, 09:00

**Background**: Next.js is a popular React framework for building full-stack web applications, developed by Vercel. AI agents are software programs that can perceive their environment, make decisions, and take actions autonomously to achieve goals, often interacting with web interfaces. The 'AI SDK' is Vercel's open-source toolkit designed to simplify building AI-powered applications with frameworks like Next.js.

<details><summary>References</summary>
<ul>
<li><a href="https://ai-sdk.dev/">The AI Toolkit for TypeScript, from the creators of Next . js .</a></li>
<li><a href="https://nextjs.org/">Next . js by Vercel is the full-stack React framework for the web.</a></li>
<li><a href="https://www.linkedin.com/pulse/nextjs-16-release-powers-next-wave-web-development-adam-john-tan-q9dyc">Next . js 16 Release Powers the Next Wave of Web Development</a></li>

</ul>
</details>

**Tags**: `#Next.js`, `#web-development`, `#frontend`, `#performance`, `#AI-tools`

---

<a id="item-10"></a>
## [Smart TVs covertly exploited as nodes in the AI data scraping economy.](https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/) ⭐️ 8.0/10

A report reveals that consumer smart TVs are being secretly repurposed as nodes in a distributed network for AI data scraping, leveraging residential IP addresses to evade detection. This covert operation turns everyday home devices into unwitting participants in a large-scale data harvesting botnet. This exposes a significant breach of user privacy and device security, as IoT devices are being weaponized without consent for commercial data extraction. It highlights critical vulnerabilities in the IoT ecosystem and raises urgent ethical questions about data ownership and the misuse of consumer hardware in the AI supply chain. The scraping network uses residential proxy techniques, routing traffic through legitimate subscriber IP addresses (like those from ISPs such as Comcast) to appear as normal user traffic and bypass anti-scraping defenses. This method is part of a broader 'scraper economy' where data brokers and AI infrastructure providers monetize web access at massive scale, often without transparency.

rss · Lobsters · Jun 6, 11:46

**Background**: Smart TVs are a common type of Internet of Things (IoT) device that connect to the internet and often collect user data for features like recommendations. 'AI data scraping' refers to the automated, large-scale extraction of data from websites, typically to train machine learning models or build databases. Distributed scraping botnets leverage networks of compromised devices to perform scraping while hiding the true origin of the requests, making them harder to block.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/">The Smart TV in Your LivingRoom Is a Node in the AIScraping...</a></li>
<li><a href="https://mediacopilot.ai/the-scraper-economy-is-already-here-publishers-just-arent-getting-paid/">The Scraper Economy is already here. Publishers... - The Media Copilot</a></li>
<li><a href="https://cyberinsider.com/one-million-devices-entraped-by-mellowtel-powered-scraping-botnet/">One Million Devices Entraped by Mellowtel-Powered Scraping Botnet</a></li>

</ul>
</details>

**Discussion**: The linked Lobste.rs discussion likely contains technical debate on the feasibility and detection methods for such IoT-based scraping botnets, with community members potentially sharing insights on network forensics and the ethics of repurposing consumer devices. Given the high score and tags like 'IoT_security' and 'data_ethics', the sentiment is expected to be one of serious concern and critical analysis.

**Tags**: `#privacy`, `#IoT_security`, `#AI_scraping`, `#consumer_electronics`, `#data_ethics`

---

<a id="item-11"></a>
## [Research Proposes 'AI Worms' That Self-Replicate Across AI Agents](https://arxiv.org/abs/2606.03811) ⭐️ 8.0/10

A research paper introduces the concept of 'AI worms'—malicious code that can autonomously propagate between interconnected AI agents without human intervention, representing a novel class of cybersecurity threat. This reveals a fundamental security vulnerability in the emerging ecosystem of interconnected AI agents, challenging existing security paradigms and potentially affecting any organization deploying multi-agent AI systems. Unlike traditional worms, AI worms exploit the AI agent's core functionality (like processing prompts and retrieving data) rather than relying on memory corruption or network protocol bugs, making them difficult to detect with conventional cybersecurity tools.

rss · Lobsters · Jun 6, 10:29

**Background**: An AI agent is a software system powered by large language models (LLMs) that can autonomously perform tasks, make decisions, and interact with other systems or agents. The concept of an 'agentic system' involves multiple such agents collaborating. Traditional computer worms are self-replicating malware that spread across networks by exploiting software vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.02812">Autonomous LLM Agent Worms : Cross-Platform Propagation ...</a></li>
<li><a href="https://firsttechwc.co.za/ai-worm-developed-by-researchers-spreads-automatically-between-ai-agents/">AI Worm Developed by Researchers Spreads Automatically Between ...</a></li>
<li><a href="https://dev.to/helios_techcomm_552ce9239/ai-to-ai-communication-navigating-the-risks-in-an-interconnected-ai-ecosystem-25hn">AI -to- AI Communication: Navigating the Risks in an Interconnected AI ...</a></li>

</ul>
</details>

**Discussion**: The lobste.rs link indicates the topic is under active technical discussion, though specific viewpoints from the provided comments are not available for summarization.

**Tags**: `#AI security`, `#autonomous agents`, `#malware`, `#vulnerability research`

---

<a id="item-12"></a>
## [Magecart skimmer repurposes Stripe API as covert command-and-control server.](https://sansec.io/research/stripe-api-skimmer-infrastructure) ⭐️ 8.0/10

A Magecart payment skimmer has been discovered that abuses Stripe's legitimate API infrastructure to act as both its command-and-control server and data exfiltration channel, using stolen Stripe test-mode keys to send stolen card data to Stripe's own servers. This technique is highly sophisticated because it uses a trusted, widely-allowed domain (Stripe) for malicious traffic, making it extremely difficult for network security tools and website owners to detect and block the data theft. The skimmer operates in Stripe's test mode, using keys with the 'sk_test_' prefix, which means the stolen data is logged in the attacker's Stripe dashboard but not processed for payment, providing a clear indicator of compromise for defenders to look for.

rss · Lobsters · Jun 6, 07:26

**Background**: Magecart is a collective term for numerous cybercriminal groups that specialize in web skimming, a type of attack where malicious JavaScript code is injected into e-commerce websites to steal payment card details entered by customers during checkout. Stripe is a major online payment processing platform that provides APIs (Application Programming Interfaces) for websites to integrate payment functionality, and its domains are typically trusted and not blocked by security systems.

<details><summary>References</summary>
<ul>
<li><a href="https://sansec.io/research/stripe-api-skimmer-infrastructure">Magecart skimmer turns Stripe into a malware command server</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_skimming">Web skimming - Wikipedia</a></li>
<li><a href="https://docs.stripe.com/stripe-cli">Stripe CLI | Stripe Documentation</a></li>

</ul>
</details>

**Discussion**: The community discussion, linked from Lobsters, highlights the clever abuse of trusted infrastructure, with users noting the irony that the skimmer's exfiltration endpoint is 'api.stripe.com', a domain that most stores would never block for fear of breaking legitimate payments. Some commenters also discuss the practical challenges of monitoring for this specific threat without disrupting normal operations.

**Tags**: `#cybersecurity`, `#malware`, `#e-commerce`, `#web-security`, `#Stripe`

---

<a id="item-13"></a>
## [Google Pays SpaceX $9.2 Billion for AI Compute Lease Through 2029](https://www.cnbc.com/2026/06/05/google-to-pay-spacex-920-million-a-month-for-xai-compute-capacity.html) ⭐️ 8.0/10

Google has agreed to pay SpaceX $9.2 billion in total from 2025 to 2029, which breaks down to $920 million per month, to lease approximately 110,000 NVIDIA GPUs and supporting infrastructure for its Gemini Enterprise AI platform. This massive deal underscores the intense and growing demand for AI compute capacity among leading tech firms and highlights the emergence of SpaceX as a major provider of AI infrastructure, particularly following its merger with xAI. The agreement includes a termination clause allowing Google to exit if SpaceX fails to deliver the promised GPUs by September 30, and it follows a similar large-scale compute deal SpaceX recently secured with Anthropic.

telegram · zaihuapd · Jun 6, 04:15

**Background**: SpaceX merged with AI company xAI in February 2026 to create a combined entity focused on space-based AI infrastructure, with an upcoming IPO targeting a valuation of about $1.5 trillion. Google's Gemini Enterprise is an advanced agentic platform that enables businesses to build, manage, and operate AI agents at scale, requiring substantial computational resources.

<details><summary>References</summary>
<ul>
<li><a href="https://applyingai.com/2026/03/spacex-xai-merger-ushers-in-era-of-space-based-ai-with-massive-satellite-constellation/">SpaceX xAI Merger Ushers in Era of Space -Based AI ... - Applying AI</a></li>
<li><a href="https://cloud.google.com/gemini-enterprise">Gemini Enterprise app: Best of Google AI for Business | Google Cloud</a></li>
<li><a href="https://www.ainvest.com/news/spacex-xai-merger-building-ai-infrastructure-layer-burning-cash-single-curve-2602/">SpaceX - xAI Merger : Building the AI Infrastructure Layer or Burning...</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#Cloud Computing`, `#Business Deals`, `#NVIDIA GPUs`, `#Tech Industry`

---