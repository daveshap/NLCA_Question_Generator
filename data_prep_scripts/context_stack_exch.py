import os

src = 'C:/RavenFinetune/raw/stack_exchange_contexts_plain.txt'


with open(src, 'r', encoding='utf-8') as infile:
    data = infile.readlines()
print(len(data))

cnt = 0
for i in data:
    cnt += 1
    with open('C:/RavenFinetune/contexts/stack_%s.txt' % cnt, 'w', encoding='utf-8') as outfile:
        outfile.write(i.strip())