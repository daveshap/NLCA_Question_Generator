import openai
from random import seed,sample
import os
import re


with open('openaiapikey.txt', 'r') as infile:
    open_ai_api_key = infile.read()
openai.api_key = open_ai_api_key


seed()
ctxdir = 'C:/RavenFinetune/contexts/'
outdir = 'C:/RavenFinetune/questions/'
files = os.listdir(ctxdir)
files = [i for i in files if 'news' in i]    # filter list: dialog, medical, reddit, stack, news
#prompt_name = 'p_questions_task.txt'
prompt_name = 'p_questions_moral.txt'
#prompt_name = 'p_questions_important.txt'
files = sample(files, 50)
print(files)

# davinci-instruct
# temp = 0.9
# top_p = 0.95
# freq pen = 0.5
# pres pen = 0.5


def load_prompt(filename, payload):
    with open('C:/RavenFinetune/%s' % filename, 'r', encoding='utf-8') as infile:
        body = infile.read()
        body = body.replace('<<TEXT>>', payload)
        return body


def completion(prompt, engine='davinci-instruct-beta', temp=0.9, top_p=0.95, tokens=200, freq_pen=0.5, pres_pen=0.5, stop=['\n\n']):
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen,
            stop=stop)
        text = response['choices'][0]['text'].strip().splitlines()
        questions = ''
        for t in text:
            questions += re.sub('^\-', '', t).strip() + '\n'
        questions = questions.strip()
        return questions
    except Exception as oops:
        print('ERROR in completion function:', oops)

for f in files:
    try:
        with open(ctxdir + f, 'r', encoding='utf-8') as infile:
            context = infile.read()
        prompt = load_prompt(prompt_name, context)
        print('\n---------------------\n', prompt)
        questions = completion(prompt)
        print('\n---------------------\n', questions)
        with open(outdir + f, 'w', encoding='utf-8') as outfile:
            outfile.write(questions)
    except Exception as oops:
        print('ERROR in main loop:', f, oops)