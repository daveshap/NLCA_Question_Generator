import os

src = 'C:/RavenFinetune/raw/medical_nlp.txt'


with open(src, 'r', encoding='utf-8') as infile:
    data = infile.readlines()
print(len(data))

cnt = 0
for i in data:
    cnt += 1
    with open('C:/RavenFinetune/contexts/medical_%s.txt' % cnt, 'w', encoding='utf-8') as outfile:
        outfile.write(i.strip())