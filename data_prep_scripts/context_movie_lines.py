from random import seed,sample
import os
import csv
from pprint import pprint

src = 'C:/RavenFinetune/raw/movie_lines.csv'

data = list()

with open(src, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        info = {'index': int(row[0].strip()), 'name': row[1].strip(), 'line':row[2].strip()}
        data.append(info)

print(data[0])
data = sorted(data, key = lambda i: i['index'])
print(data[0])

last = 0
context = ''
conversations = list()
for i in data:
    if i['index'] - last > 1:  # we had a gap, new context!
        conversations.append(context)
        context = i['name'] + ': ' + i['line']
        last = i['index']
    else:  # continuation of last context
        context += '\n' + i['name'] + ': ' + i['line']
    last = i['index']
conversations.append(context)

cnt = 0
for i in conversations:
    if i.count('\n') < 2:
        continue
    cnt += 1
    with open('C:/RavenFinetune/contexts/dialog_%s.txt' % cnt, 'w', encoding='utf-8') as outfile:
        outfile.write(i.strip())