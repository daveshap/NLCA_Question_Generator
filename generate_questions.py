import openai
from random import seed,sample
import os


seed()
ctxdir = 'C:/RavenFinetune/contexts/'
outdir = 'C:/RavenFinetune/questions/'
files = os.listdir(ctxdir)
files = sample(files, 10)
print(files)


def load_prompt(filename, payload):
    with open(filename, 'r', encoding='utf-8') as infile:
        body = infile.read()
        body = body.replace('<<TEXT>>', payload)
        return body


for f in files:
    with open(ctxdir + f, 'r', encoding='utf-8') as infile:
        context = infile.read()
    prompt = load_prompt('C:/RavenFinetune/p_questions_important.txt', context)
    print(prompt)