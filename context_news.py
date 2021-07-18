import re
import os

basedir = 'C:/RavenFinetune/raw/bbc_news/'
subdirs = ['business/', 'entertainment/', 'politics/', 'sport/', 'tech/']

cnt = 0
for subdir in subdirs:
    files = os.listdir(basedir + subdir)
    for f in files:
        cnt += 1
        try:
            with open(basedir + subdir + f, 'r', encoding='utf-8') as infile:
                body = infile.read()
            with open('C:/RavenFinetune/contexts/news_%s.txt' % cnt, 'w', encoding='utf-8') as outfile:
                outfile.write(body.strip())
        except:
            a = 0