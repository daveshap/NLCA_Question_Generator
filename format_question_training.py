import os
import json


ctxdir = 'C:/RavenFinetune/contexts/'
quedir = 'C:/RavenFinetune/questions/'
files = os.listdir(quedir)
print(files)

data = list()

for f in files:
    with open(quedir + f, 'r', encoding='utf-8') as infile:
        questions = infile.read()
    with open(ctxdir + f, 'r', encoding='utf-8') as infile:
        context = infile.read()
    prompt = '%s\nQUESTIONS:' % context
    info = {'prompt': prompt, 'completion': questions}
    data.append(info)


with open('questions.jsonl', 'w') as outfile:
    for i in data:
        json.dump(i, outfile)
        outfile.write('\n')