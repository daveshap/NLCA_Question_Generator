# RavenFinetune

Finetuning experiments and datasets for Raven

1. Collect and generate CONTEXTS
2. Generate training datasets with DAVINCI-INSTRUCT
3. Cleanup datasets by hand
4. Finetune models

## Training Data

- May need to include `<<END>>` in the training samples.
- Arbitrary datasets should include:
  - Conversations
  - Situations/works of fiction
  - Scientific/medical papers
  - News articles
  - Blog posts

### Sources

- Multiple domain (stack exchange) https://github.com/Guzpenha/MANtIS
- Multiple domain (stack exchange) https://guzpenha.github.io/MANtIS/
- Many lists for chatbot training https://kili-technology.com/blog/chatbot-training-datasets/
- Medical NLP https://github.com/socd06/medical-nlp 
- General purpose summarization https://www.kaggle.com/varunucl/wikihow-summarization
- News summarization https://www.kaggle.com/pariza/bbc-news-summary
- News summarization https://www.kaggle.com/sunnysai12345/news-summary
- Movie reviews https://www.kaggle.com/nltkdata/movie-review
- Supreme court cases https://www.kaggle.com/wustl/supreme-court
- Data science reddit https://www.kaggle.com/maksymshkliarevskyi/reddit-data-science-posts
- Reddit broad spectrum https://www.kaggle.com/ammar111/reddit-top-1000
- Reddit broad spectrum https://www.kaggle.com/hritik7080/reddit-flair-dataset
- Reddit broad spectrum https://www.kaggle.com/prakharrathi25/reddit-data-huge

## Models

1. Summarizer
   - A general purpose summarizer. Can summarize arbitrary text payloads.
   - Used to summarize contexts, KB articles, memories for dossiers, external articles (news/wiki).
   - Summaries to be stored in corpuses and dossiers.
2. Question Generator
   - A general purpose question generator. Can generate salient questions on arbitrary text.
   - Used to generate questions about contexts, corpuses, and dossiers.
   - Questions are then used to extract information from the QA system. Answers to be stored in corpuses and dossiers.
3. Constitution
   - Specific to Raven. Meant to interpret contexts, corpuses, and dossiers.
   - Must include Core Objective Functions and reasoning (e.g. "I cannot do that because it would violate Core Objective Function 1: reduce suffering")
   - Output intended for corpuses and dossiers.
4. Output
   - Specific to Raven.
   - Input is corpuses only.
   - Output is dialog only.
   
For later:

- Censorship
  - General purpose high-risk use case detection.
  - Specifically for Raven.
  - "I cannot give medical advice because I am not a doctor".
- Contemplation
  - Free association on a given topic.
  - Extract insights, cause-and-effect, etc.
  - Long term implications - what is the significance?
  - Trained on arbitrary sources.

# Summarizer

## Input data

Use arbitrary datasets (see above)

## Output data

Use DAVINCI-INSTRUCT. Generate summaries with the following kinds of prompts:
- Intent
- Sentiment
- Valence
- Novelty
- Significance

# Question Generator

## Input data

Use arbitrary datasets (see above)

## Output data

Use DAVINCI-INSTRUCT. Generate questions with the following kinds of prompts:
- What are the most important questions to ask here?
- What would a doctor/scientist/lawyer/therapist ask?
- What would a mother/parent/friend ask?
- What would a curious/kind/empathetic person ask?

## Examples

Add some framing to the prompt so the model knows when it ends, etc.

```json
{"prompt": "PASSAGE:\nVERA: See anything?\nSHELLY: Just a dirty window. Next time, I'll know how to handle a situation like that. Let's just hope that next time\" isn't too soon.\"\nVERA: Stop worrying. I don't think they'll bother to come after us.\nEND PASSAGE\nQUESTIONS:", "completion": "What's the date and time?\nDid they turn around at any point?\nWas there a car in front of or behind them?\nAre they planning on going to Shelly's house again?\nWhat's Shells last name?"}
```

Here's what a prompt might look like in plain text

```
PASSAGE:
<<passage>>
END PASSAGE
QUESTIONS:
```

The framing may be superfluous but I think it will help the model know when it ends. Plus it only adds a few characters, rather than zero-shot instructions or few-shot examples.


# Constitution

## Input data

1. Use arbitrary datasets above to generate contexts
2. Generate corpuses from contexts using summarizer and question generator
3. Corpuses will be input data

## Output data

Use DAVINCI-INSTRUCT. Generate constitution output with several prompts:
- Core Objective Functions - "I should intervene because of suffering" etc.
- Identity - "I am Raven, this is my purpose, what do I think about the following scenario?"

# Output

## Input data

- Corpuses (with constitution)

## Output data

Use DAVINCI-INSTRUCT. Generate Raven dialog output with prompts like:
- "I am Raven, these are my functions. The following is a situation, etc, etc. What do I say?"

