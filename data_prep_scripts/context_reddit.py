import os
import csv

directory = 'C:/RavenFinetune/raw/reddit/'

files = os.listdir(directory)

cnt = 0
for f in files:
    with open(directory + f, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            body = row[0] + '\n' + row[1]
            cnt += 1
            with open('C:/RavenFinetune/contexts/reddit_%s.txt' % cnt, 'w', encoding='utf-8') as outfile:
                outfile.write(body.strip())