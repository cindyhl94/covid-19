# Highlevel Architecture

 ![Highlevel Workflow and architecture](docs/arch.png)


### Thought process

Identify the underlying drivers of fear, anxiety and stigma that fuel misinformation and rumour, particularly through Social Media


Rumours and Misinformation

Identify the following from individual section matches:

1. What is the rumour or misinformation about ?

2. Who or which organistaion is involved in starting the rumour ?

3. Who have been impacted or may be impacted because of the rumour ?

4. What are the reasons for the rumour ?

5. What are the factors associated with the rumour ? Do we see factors such as fear, anxiety, stigma ?

6. Which categories does the rumour fall under ?

7. What are the keyphrases that are associated with the rumour ?

8. Can we identify topics related to that rumour ?


Aggregate the matched sections into one large block of text and do the following :

1. Topic Model

2. Extract Keyphrases

3. Create FastText word embeddings

4. Association Analysis to probe questions such as:

   Given there is a rumour, what's the likelihood that the underlying drivers are economical, political, sociological or technological ?
   


![](docs/mappings.png)

# The following features are part of the repo

## Extracting relevant sections based on predefined terms and grammar based patterns from files in the datasets

0. Install required Python Libraries

> pip install -r Requirements.txt

1. Populate src/common/patterns/ethics.py with patterns of interest

> The current terms used to search are: misinformation = [ "misinformation", "disseminating disturbing and harmful information", "hate speech", "targeting chinese people", "sinophobia", "malicious content", "fake news", "fake information", "fake health information", "misleading information", "false news", "rumour", "rumor", "lack of evidence based"]

2. Update ethics.py with the right output dir where matched sections will be stored as json files. There will be one file each per input file.

3. At the root dir,
  export PYTHONPATH=.
  
  python tests/test_get_sections_dist.py
  

The number of files which matched the patterns defined for misinformation and rumour are 628

41 from non comm use
374 from custom license
32 from arxiv
38 from biorxiv
143 from comm use subset


## Topic Modeling

Chdir to the root of the repo

Test script:

export PYTHONPATH=.

$python tests/test_topic_model.py

## Extracting Keyphrases
Chdir to the root of the repo

export PYTHONPATH=.

$python tests/test_get_phrases.py 

Sample Input and Output: 
> Input text : Improved communication between reliable health officials and the media, community leaders, health professionals, and the general public is necessary to reduce misinformation and improve compliance with Ebola prevention and control measures that have proven effective

> Output Phrases: [('control measures', 0.2753591962042809), ('general public', 0.17994168925838788), ('ebola prevention', 0.17902881963324135), ('health professionals', 0.13258849145986482), ('community leaders', 0.09609342894161833), ('health officials', 0.0821235319275857), ('reliable health', 0.05486484257502089)]
