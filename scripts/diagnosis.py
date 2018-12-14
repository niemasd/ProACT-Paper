#!/usr/bin/env python3
from gzip import open as gopen
from sys import argv
if len(argv) != 4:
    print("USAGE: %s <output.txt> <gemf2orig.json> <seqs.aln.gz>"%argv[0]); exit()
gemf2orig = eval(open(argv[2]).read())
inf_time = {}
for l in open(argv[1]):
    p = l.strip().split(' ')
    person = gemf2orig[int(p[2])]
    after = p[4]
    if p[4] in '6789' and person not in inf_time:
        inf_time[person] = float(p[0])
for line in gopen(argv[3]):
    l = line.decode().strip()
    if l[0] != '>':
        continue
    k = l[1:]
    n = k.split('|')[1]
    if n in inf_time:
        print('%s\t%f'%(k,inf_time[n]))
    else:
        print('%s\t%f'%(k,float('inf')))
