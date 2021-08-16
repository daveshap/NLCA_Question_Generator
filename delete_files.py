import os

outdir = 'C:/RavenFinetune/questions/'
files = os.listdir(outdir)
#files = [i for i in files if 'news' in i]    # filter list: dialog, medical, reddit, stack, news

for f in files:
    with open(outdir + f, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    modified = False
    for line in lines:
        #if 'you' in line:
        #    print('REMOVE', line)
        #    lines.remove(line)
        #if 'passage' in line:
        #    print('REMOVE', line)
        #    lines.remove(line)
        if '?' not in line:
            print('REMOVE', line)
            modified = True
            lines.remove(line)
    if modified:
        with open(outdir + f, 'w', encoding='utf-8') as outfile:
            outfile.writelines(lines)
        print('OVERWRITE', f)