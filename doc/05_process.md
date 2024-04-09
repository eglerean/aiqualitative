# Data pre-processing

There are at least two key tasks that can happen at the pre-processing stage:
1. Convert the data into a format that can be understood by LLMs
2. Minimise the data to respect privacy.


:::{warning}
This page could be expanded with more preprocessing strategies and examples.
:::

## Preparing your data for LLMs

The data you collected should be  pre-processed into a format so that the GenAI can use it for further analysis. This usually means that anything that is not already collected as simple digital text, will require some data pre-processing. In the tabs below, some options for data preprocessing such as image to text, and automatic speech transcription. Note that also these tools are using AI/ML, but we won't go deeper in the details on why they are different from GenAI with LLMs.


```{tabs}
   ~~~{tab} Survey answers
   Often survey answers are provided in digital formats such as xlsx or csv. When the survey data is collected with pen and paper, check the section on Observations for some more details.
   ~~~
   ~~~{tab} Interviews
   These are usually audio-visual recordings. Speech can automatically be converted into text with tools such as OpenAI Whisper. For security (confidentiality) our Aalto Research Software Engineers have developed Speech-to-text a tool for automatic speech transcription and diarization, all locally in the Aalto HPC cluster Triton. Enrico to expand on this later. https://aaltorse.github.io/speech2text/index.html
   ~~~
   ~~~{tab} Observations
   These are usually notes written by the researcher during observational work. They are usually digitised into text files (PDF, docx,...) or images (pngs, jpgs, tiff, ...). Please note that to use LLMs you need to convert the document into a format that is "text only", so images will need OCR conversion to text and PDFs require the text to be extracted. Paid version of ChatGPT can do some of this text extraction, but you still want to check the validity of the extracted data, so it is worth doing it with tools that can be used to verify the results (e.g. Acrobat for OCR text recognition).
   ~~~
   ~~~{tab} Documents
   These are usually written documents (manuscripts, articles, letters). When it comes to the data formats, see same consideration as for "Observations".
   ~~~
```

## Data minimisation

Data minimisation is one of the core principles of the GDPR. While it is often impossible to minimise the data so that it can be truly anonymous. There are techniques for at least "minimising" the data, i.e. keep only the minimum required for your research purpose. For example an audio-visual interview can be converted to audio-only format if the researcher is not planning  -- and did not disclose to the study participant -- to analyse the video data.

:::{warning}
This section can be expanded with content from these slide set:
> Glerean, E. (2024, February 12). Basics of personal data anonymisation. Zenodo. https://doi.org/10.5281/zenodo.10649060 
:::


:::{note}
Do you have other uses of AI for data preprocessing? Share your knowledge with other Aalto researchers by contributing to this book!
:::