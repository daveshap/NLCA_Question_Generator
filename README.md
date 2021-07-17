# RavenFinetune

Finetuning experiments and datasets for Raven

1. Collect and generate CONTEXTS
2. Generate training datasets with DAVINCI-INSTRUCT
3. Cleanup datasets by hand
4. Finetune models

Note: may need to include `<<END>>` in the training samples.

## Models

1. Summarizer
   - A general purpose summarizer. Can summarize arbitrary text payloads.
   - Payloads include: Raven contexts, conversations, physical observations, news articles, science articles, blogs, etc.
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
   - Input is corpuses only.
   - Output is dialog only.
   
For later:

- Censorship
  - General purpose high-risk use case detection.
  - "I cannot give medical advice because I am not a doctor".
- Contemplation
  - Free association on a given topic
  - Extract insights, cause-and-effect, etc
  - Long term implications - what is the significance?

## Summarizer

1. Collect raw training data
   - Contexts from Raven
   - Other dialog/conversational sources (TBD)
   - Wikipedia articles
   - News articles
   - Blog posts
2. Generate high-quality summaries
   - Use several DAVINCI-INSTRUCT prompts to generate good summaries
   - Include several kinds of summary in each sample (ex: intent, sentiment, valence for conversations; novelty and significance for news)
3. Merge raw training data and summaries into training dataset
   - Each line needs to be < 2048 tokens
   - Ideally have several hundred samples for each model