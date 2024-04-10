# Ethics and Law

While adhering to the law is necessary, academic researchers hold the best standard when it comes to adhering to ethics at large: research ethics, research integrity, responsible conduct of research. In this chapter we first clarify the necessary role of law and then focus on the ethical implications of using such tools in academic research. 

## Basics of information security

In information security the CIA triad (Confidentiality, Integrity, Availability) is a very popular framework for technological system. In the rest of this chapter we will focus on the "C" (Confidentiality), i.e. making sure that only those who have the right to access the information are actually able to access it. Confidentiality is closely related with the concept of "Classification of Information". At Aalto University we use four level of classification of information

> **[Classification of information at Aalto University](https://www.aalto.fi/en/information-processing/classification-of-information)**
> 1. 🟢 **Public**: data in the public domain (examples: simulated data, open teaching materials, open access publications, open source code). Note that with personal data, even public personal data should be treated as confidential in the context of research.
> 2. 🟡 **Internal**: Information not intended for publication (examples: work files, drafts, meeting notes)
> 3. 🔴 **Confidential**: Information with access limited according to law or contractual terms to authorised persons only. (examples: Research personal data, trade secrets)
> 4. ⚫ **Secret**: Information with access limited according to law or contractual terms to authorised persons only. Information that is meant to be secret and that would cause major damage if disclosed. (example: medical records obtained from a Findata application)

## Law - Data protection and cybersecurity

The first thing to consider relates to ensuring the confidentiality of the data you work with. It can be the confidentiality of your or others' **intellectual property** or it can be the confidentiality of your or others' **personal data**. The most frequent question that researchers have relates to the confidentiality of the systems we use: is my research data safe if I use OpenAI ChatGPT? Is it safe to use an open source language model like Mistral or Llama2?

To evaluate the confidentiality (*security*) of the GenAI tools you use, it is important to understand the physical geography of such tools.

**Insert here slide 28 from https://zenodo.org/records/10890289**

*Insert here full description of the figure for those who are not attending the presentation.*

To sum up, with https://ai.aalto.fi, Aalto University researchers have access to a secure interface to work with one of the most advanced LLMs (OpenAI's GPT4). Please note that secret data should still not be used with these external model. The simple rule is that secret data should not be on a computer that has access to the internet. While this might sound paranoid, it is actually a very effective way to work with most sensitive data, and even with "unsafe" software. This is common practice also in infrastructures: you might have a measurement computer that needs to preserve a certain ancient version of an operating system and it cannot be upgraded. The safest option is to completely disconnect it from the internet.

## Ethics

The role of Ethics in research with GenAI can be considered from multiple perspectives.

### Research ethics: the principle of *do no harm*

The core principle of research ethics is *do no harm*. When considering the ethicality of your research, you should evaluate the *do no harm* principles towards your study participants, yourself, your work place, local and global society, the environment.

- **Is the use of AI increasing the risks of harm for the study participants?** 
For example you might be studying a certain ethnical minority, or sub-culture, and the GenAI model might not know the nuances of such culture, and might actually behave in a discriminatory way (racist AI) because of the past data that it has been exposed to. When producing results with AI we should consider if the output was fair and aware of the specific cultural context, without letting it misjudge your study participant

- **Is the use of AI increasing the risks for myself?**
*This is a consideration that is not strictly related to AI, it applies to any tool and platform we use as individuals.* Your personal data is also very valuable to companies: data about yourself and also data about how you use online platforms. You often pay with your personal data so that you can use certain platforms: what they can do is legal, but it could be questioned if it is ethical. Depending on the confidentiality of your work, you might not want to use certain system. 

- **Is the use of AI impacting the environment?**
It is estimated that a session with ChatGPT requires about 0.5l of water for the cooling of its computing system. Larger data centers are buing built and it is estimated that the electricity consumption of AI will increase in the order of the [yearly amount consumed by a country like Sweden](https://www.thedailybeast.com/ai-may-soon-gobble-up-as-much-power-as-sweden-each-year). While your usage most likely won't truly affect these estimate, it is worth considering more sustainable options (e.g. via local LLMs).

### Ethics and ideology

If we do not strictly consider the research ethics principle of *do no harm* (direct increase of risks related to research work), we could still consider some ideological aspects in the context of ethics, leaving individuals to decide for themselves if the tool they use is *"ethical"*. 

The training of LLMs requires a large amount of input data, and -- in a latter stage called Reinforcement Learning from Human Feedback (RLHF) -- annotated data produced by humans to improve the model output.

#### Training data ethics
It is a known fact that the largest models such as GPT4 needed all the possible data they could get to train the model, and because of that anything that publicly available has been scraped and used to train such models. While you might think that this breaches copyright laws, or just basic ethical principles of reuse of data for profit, the transformative nature of these systems makes it so that they do not actually need to store the data they obtained. So it is like compressing all the information in the plant, without actually being able to "decompress" certain exact specific items of information (although this is currently disputed e.g. between the NYTimes and OpenAI; there are many examples of "training data extraction attacks" link to be added). The AI act will ensure more transparency when it comes to the data sources. For now, the ethical dilemma for the individual is: do you want to use a system that has been built on data that was not explicitly obtained from the data creators?

#### RLHF: the hard work of many underpaid individuals
While large data is necessary to establish an LLM, without the RLHF stage the model would often produce uncorrect answers. Right now the H in RLHF are often people from the Global South, hired with no job security and with minimum pay. It is a grey area: on one hand this can be a great opportunity to provide work to individuals who might not find other work -- for example [Finnish prisoners are receiving 1.54eu/hour for doing text labelling](https://theconversation.com/long-hours-and-low-wages-the-human-labour-powering-ais-development-217038) --, on the other hand one might wonder that if these companies are accumulating more and more capital, wouldn't it be more fair to give back to those who contributed to their product? This section can be expanded with more recent links and it should be clear that this text is not taking any political stance. Here an older one from the Guardian: ["‘It’s destroyed me completely’: Kenyan moderators decry toll of training of AI models (the Guardian)"](https://www.theguardian.com/technology/2023/aug/02/ai-chatbot-training-human-toll-content-moderator-meta-openai).

### Ethics and Research Integrity

In the context of [Research Integrity and research misconduct](https://tenk.fi/en/research-integrity/research-misconduct), the three things that must be avoided by any researcher are:

1. Fabrication: presenting fake observations, research data or results.
2. Falsification: manipulation of research findings, distorted results, omissions.
3. Plagiarism: unacknowledged borrowing, means using someone else’s work or research ideas without permission or reference.

The problem with GenAI is that these tools are the best at fabrication, falsification, and plagiarism! ChatGPT will never say "I do not have an answer", it will always try to produce convincing text, with some disclaimer added just so they make sure they are not responsible for anything it *hallucinates*. Furthermore, because it is not possible to directly store exact references that were used in the synthesis of certain text, it is the responsibility of the researcher to make sure that they cannot pass certain claim as their own novel idea, only because ChatGPT was unable to provide a reference. Most likely if ChatGPT generated it, then something very similar already exists somewhere.

### Ethics and responsible conduct of research

While FFP are the core of research misconduct, there are other questionable research practices that fall under the umbrella term of Responsible Conduct of Research. GenAI tools might increase sloppy practices:

1. Reproducibility: GenAI tools are inherently stochastic to produce interesting outputs. This undermines the reproducibility of analysis using GenAI tools, or at least requires efforts similar to what is done when estimating "inter-rater agreement": running multiple time the same queries and identify a summary result.
2. Validity of AI suggestions: GenAI tools were trained with lots of bad science, bad statistics, unreproducible findings. The tool might be recommending a method or an interpretation that has been proved to be wrong, just because statistically there were more "wrong" examples in the training dataset than the correct ones. These type of "biases of AI" are present in all AI systems, and the only solution for this issue is to always critically evaluate its output.

## Further considerations on peer-review and publishing GenAI work

This section needs to be expanded, but basically I want to mention

1. The nature survey on how GenAI might be increasing productivity of researcher, but shifting the problem to peer reviewers who are even more overloaded than before. ["Is ChatGPT making scientists hyper-productive? The highs and lows of using AI"](https://www.nature.com/articles/d41586-024-00592-w).
2. Journal policies on using AI: AI cannot be a co-author, AI cannot be used for peer review.
3. Transparency on how to cite the use of AI in a paper: journals are starting to recommend including a section called [Declaration of generative AI in scientific writing](https://www.sciencedirect.com/journal/artificial-intelligence/publish/guide-for-authors). [Here you can see an example](https://www.sciencedirect.com/science/article/pii/S0141813024001247#s0145).
 

