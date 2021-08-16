# NLCA Question Generator

The Natural Language Cognitive Architecture (NLCA) requires the ability to generate questions for several purposes. First, generating questions is one of the primary ways it "thinks". Curiosity is merely unspoken internal questions. The ability to spontaneously generate questions leads to the ability to seek answers, and thus accumulate more information. Just asking questions and seeking answers could be one path to AGI.

Generating good questions is the root of curiosity and learning. By asking follow-up questions, and seeking answers, you can create a positive-feedback loop which results in greater understanding. Furthermore, it just makes for a good conversational companion. For instance, you could have a chatbot that only asks questions and still have a tremendously valuable tool.

## Scheme

You start with a context. In this case, a context is a scenario, story, article, or dialog. This context then has questions associated with it. This forms the training data for the finetuned model. Here's an example context:

> Does anyone else's stomach gets upset when anxious? My stomach always begins to ache when anxious. At times I have to excrete too. Sometimes it is painful.

And here's an example set of questions:

> Are you constantly anxious?
> What happens when you're anxious?
> How often does this happen?
> Does anything else trigger your anxiety?

Here's what the same thing looks like as training data:

```json
{"prompt": "Does anyone else's stomach gets upset when anxious ?\nMy stomach always begins to ache when anxious . At times I have to excrete too . Sometimes it is painful .\nQUESTIONS:", "completion": "Are you constantly anxious?\nWhat happens when you're anxious?\nHow often does this happen?\nDoes anything else trigger your anxiety?"}
```

## Usage Quickstart

### Training

I wrote a file called `finetune.py` that contains a few functions to help speed things along. All you need to do is run a few CLI commands to get started. Make sure you create `openaiapikey.txt` first, and put your API key in it.

```python
from finetune import *
file_upload('questions.jsonl')
finetune_model('<fileid returned from file_upload command>')
finetune_list()
```

The training data is ready to go as `questions.jsonl`!

### Completion

I wrote a quick demo script called `test_finetune.py`. You'll need to populate it with your own finetuned model name. You can see it with the above `finetune_list()` function. Here's an example of the performance:

Context:

> So guys I have this crush on this boy and he's so dumb but I love him. His name is Roger and he's the quarterback of the team.

Questions:

> What is the narrator's name?
> How old is the narrator?
> What team does the narrator play on?
> What is the narrator's relationship to Roger?
> Does the narrator have a crush on Roger?
> What is Roger's last name?
> Where does Roger play on the team?
> What is Roger's position on the team?
> Does the narrator have any other friends on the team?
> Does the narrator have any other crushes besides Roger?
> What is the name of the school that the narrator attends?
> What is the name of the team that Roger plays for and what position does he play?
> Does the narrator have any brothers or sisters?
> Does the narrator go to a public or private school?
> What is the name of the city that the narrator lives in or where they live?
> What sports does the narrator play?
> Does the narrator have any brothers or sisters that play on the team?

This list is a bit ridiculous but you can see how it really took the idea of asking questions and ran with it. These questions can be used for conversational purposes, or for searching a database with information about the narrator. For instance, imagine that you have a personal assistant that has recorded all previous conversations with you. These kinds of questions can be used internally for the information assistant to recall the correct details and hold a realistic conversations. Alternatively, these questions can be used to have a real-time conversation.


## Explanation of Everything

### Contexts

I scraped together the contents of the `contexts` folder from various data sources, mostly from Kaggle. Another good source was https://github.com/Guzpenha/MANtIS. Check in the `data_prep_scripts` for some of the data cleaning scripts I wrote. The idea was to pare down the contexts to bare minimum, so as to remove some framing, comments, and other noise. I also included a variety of types of contexts so that the AGI would be familiar with many types of situations. There are medical cases, reddit and stack exchange posts, movie dialog, and news snippets. This combination means that the finetuned model will be excellent at generating questions for almost any scenario, whether it's one person asking for help, talking to multiple people, or reacting to news.

Check in the `contexts` folder for a list of all contexts. I only used 1200 of them for the training set, but I have more than 50,000 available for future use.

Types of contexts used:
1. Reddit posts from many different subreddits
2. Stack Exchange posts from several domains
3. News articles, mostly British
4. Medical notes
5. Dialog from movies

### Questions

I found that GPT-3 is great at asking questions if you give it a lot of power. I used `DAVINCI-INSTRUCT-BETA` and gave it the simple command of `Write a list of the most important and salient questions an observer would ask about the following passage:`. This prompt generated the best results by far. For instance, GPT-3 was able to read between the lines on more emotional contexts or infer the medical condition on doctors notes. GPT-3 implicitly demonstrated that it has strong knowledge about the world - far more than any one person. I learned a lot just by looking at the questions it asked!

I set the temperature pretty high on GPT-3 so that it would be as creative as possible with the questions. I also ran it a second time to ensure that each context had at least 4 questions asked. Plus, I wrote a script that would remove any lines from the questions that did not end in a question mark. 

Check in the `questions` folder for all generated questions. I spent about $120 of DAVINCI tokens to generate the datasets.

### Training Data

Finally, I put it all together with `format_question_training.py`. This creates a JSONL file with all the questions and their associated contexts. It also adds `QUESTIONS:` to the end of the context becuase the model will need to know when to switch to questions. 