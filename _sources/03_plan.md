# Planning your research

GenAI can be a powerful tool for planning your research with qualitative data. The planning stage usually happens before data collection and analysis. Usually in the planning stage you might want to explore the existing literature on the topic, identify the research gap, build novel research question.

The planning stage however is also very important because you can refine your data collection and data analysis plan. In this chapter we cover both aspects of research planning.

## GenAI to explore the literature and construct novel research hypothesis

This section is empty for now. This was covered in our work at https://zenodo.org/records/10890289.

## GenAI to refine your data collection and data analysis plan.

:::{warning}
This section limits the context to research with human participants, before data collection. It should be expanded for when qualitative research is conducted with already existing data, for example documents.
:::



Before collecting data, you want to evaluate if you are going to ask the right questions and if potential answers from your study participants. Let's consider my study. I first describe it to ChatGPT:

> **You** 
> You are an expert in qualitative methods and I need your help in designing a survey in the context of a research study I am conducting. The scenario of the interview is a lab experiment where each participant watched a movie (Forrest Gump) while wearing an eye tracking device. At the end of the movie the participants are interviewed and are asked two questions one about the emotions they felt in the movie, and one about the measurement experience with the eye tracking device. Can you write the two questions?

> **ChatGPT**
> Certainly! Here are two questions that could be used in the interview to gather qualitative data about the participants' experiences watching "Forrest Gump" with an eye-tracking device:
> 
> 1. "Can you describe the emotions you felt while watching 'Forrest Gump'? Were there specific scenes or moments that elicited strong emotional responses? Please elaborate on your experience."
> 
> 2. "How did you find the experience of using the eye-tracking device during the movie? Did it affect your viewing experience in any way? Please share any thoughts on comfort, distractions, or other observations related to the device."
> 
> These questions are designed to explore both the emotional impact of the film and the practical aspects of using the eye-tracking technology, which would provide rich data for qualitative analysis.


Next, we want to make sure that we can collect reliable data with these questions. Since LLMs are so great in synthesing simulated data, I ask ChatGPT to produce some fake data so that I can later use it for testing which method could be suitable for my analysis plan. 

:::{tip}
A great paper on the potential of synthetic data for qualitative research is 
> Hämäläinen, P., Tavast, M., & Kunnari, A. (2023, April). Evaluating large language models in generating synthetic hci research data: a case study. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (pp. 1-19). https://dl.acm.org/doi/10.1145/3544548.3580688
:::


> **You**
> Now let’s generate answers for a few subjects with different personalities and movie taste. Some people found the movie funny, some boring, some saw it before, for some it was the first time they watched it. Some are in their 50s, some are bachelor university students. When generating the synthetic data, create it as a table in markdown with the following columns:
> 
> 1. Name surname
> 2. Background of the individual: age, occupation, sex, self description of how their personality is
> 3. Answer to question 1
> 4. answer to question 2
> 
> Generate 5 study participant

Before exploring the answer of ChatGPT, let's notice a few things in the chosen prompt.

- **We need variance**: as with any data analysis method, we want to have variance in our data. If all participants would produce exactly the same answer, there wouldn't be much to analyse, it is like dealing with a flat signal in signal processing, or a variable with zero standard deviation in statistics.
- **We need structure**: the prompt is asking for the simulated data in a tabular format. This is important both for us since we can keep the data format also for when it is time to analyse the data, but it is also important for the LLM since later we can clearly refer to the data in the table, rather than other answers it might have given.
- **We start small**: the prompt is not asking to generate a large amount of subjects. This is because we are still in *exploratory mode*. Often the first round of synthesis might not be exactly what we had in mind. We might need to refine our prompt, be more specific in what we ask. Initially some small iterations are necessary. Please also note that if the conversation becomes too long, the model might fail to keep the full context window. It is sometimes better to start a new session and repeat the process from scratch.

Let's now have a look at the answer from ChatGPT:

> **ChatGPT**
> Here's a table with synthetic interview data for five fictional study participants, each with distinct backgrounds and reactions to watching "Forrest Gump" while using an eye-tracking device:

| Name Surname	| Background of the Individual: Age, Occupation, Sex, Self Description of How Their Personality Is	| Answer to Question 1	| Answer to Question 2 |
| --- | --- | --- | --- |
| John Doe	| 53, Accountant, Male, Introverted and analytical	| "I found the movie quite touching, especially the scenes involving Forrest's childhood. It wasn't my first time seeing it, but the emotional impact remains strong. I particularly connected with the protagonist's perseverance."	| "The eye-tracking device was a bit distracting at first, but I got used to it. It didn't significantly alter my viewing experience." | 
| Emily Stone	| 22, University Student, Female, Extroverted and enjoys comedy	| "This was my first time watching "Forrest Gump." I thought it would be purely comedic, but it was surprisingly emotional too. I laughed a lot, especially during Forrest's accidental achievements."	| "I found the device comfortable enough, though I was aware of it during funny scenes which made me lose focus occasionally." | 
| Michael Rivera	| 28, Graduate Student, Male, Cynical and prefers intense dramas	| "I've seen the movie several times. It feels a bit slow and predictable at this point. However, the historical references are interesting."	| "The device was fine. I hardly noticed it after a while, which allowed me to focus more on the details of the film." | 
| Lisa Chang	| 50, Nurse, Female, Empathetic and values emotional storytelling	| "I've always found 'Forrest Gump' deeply moving. The movie's exploration of destiny and love always brings me to tears, especially the scenes with Jenny."	| "The eye-tracking device was slightly uncomfortable at the beginning, but it didn’t detract from the powerful moments of the movie." | 
| Alex Johnson	| 19, University Student, Male, Enjoys fast-paced movies, first-time viewer	| "I thought the movie would be boring but was pleasantly surprised by its depth and the complexity of Forrest's character. It was funny, but also made me think."	| "Using the eye-tracking device was interesting. It felt a bit weird at first, but it didn't bother me much as the movie went on." | 


> These fictional responses provide varied insights into the emotional responses elicited by the film and the subjective experiences of using the eye-tracking technology during viewing.

We could now ask for refining the output. In this case I was happy with the result so I will ask to generate a few more participants:

> **You**
> Generate 5 more

> **ChatGPT**
> Here are five additional synthetic profiles with responses for participants who watched "Forrest Gump" while using an eye-tracking device:

| Name Surname	| Background of the Individual: Age, Occupation, Sex, Self Description of How Their Personality Is	| Answer to Question 1	| Answer to Question 2 | 
| --- | --- | --- | --- |
| Sarah Bennett	| 32, Marketing Manager, Female, Creative and empathetic	| "Watching 'Forrest Gump' always brings a mix of laughter and tears. The narrative complexity and emotional depth resonate with me every time, especially Forrest's unwavering kindness."	| "The eye-tracking device was slightly intrusive initially, but I forgot about it once I got absorbed in the story." | 
| Darren Smith	| 45, Engineer, Male, Pragmatic and reserved	| "I've seen 'Forrest Gump' multiple times. It's a fine movie, though not my favorite. I appreciate the technical execution and historical context more than the emotional aspects."	| "The device was comfortable and didn't interfere with my viewing experience, allowing me to appreciate the cinematography." | 
| Olivia Martinez	| 27, PhD Candidate, Female, Analytical and introverted	| "This was my first viewing of the movie. The emotional arcs were engaging, and I enjoyed analyzing the lead character's development throughout the different eras."	| "I was aware of the eye-tracking device at all times, which made me somewhat conscious of how often my gaze shifted during intense scenes." | 
| Ethan Wright	| 35, Freelance Writer, Male, Thoughtful and enjoys drama	|  "Forrest Gump is a movie that I find humorously tragic. The stark contrast between the protagonist's simplicity and the complex events around him is striking. It was enjoyable revisiting it."	|  "The device was a minor distraction initially, but it became less noticeable as the movie progressed." | 
| Grace Kim	| 24, University Student, Female, Curious and loves exploring different genres	|  "I hadn't watched 'Forrest Gump' before. It was fascinating to see a character go through so many historical events. The blend of humor and drama was captivating."	| "I found the eye-tracking device intriguing to use. It was a bit uncomfortable at first, but it added an experimental aspect to my movie experience."| 

> These responses enrich the dataset with a variety of perspectives on the movie and user experiences with the eye-tracking technology, suitable for qualitative analysis.


## Summary

We can now draft a good research plan before data collection, and we even have some data to simulate our study. We will use the same data in the next sections to test a couple of qualitative analysis methods