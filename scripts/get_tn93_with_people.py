#!/usr/bin/env python3
from gzip import open as gopen
from sys import argv,stdin
if len(argv) != 3:
    print("USAGE: %s <tn93_file> <labels_file>"%argv[0]); exit(1)
if argv[2] == '-':
    people = {l.strip() for l in stdin}
elif argv[2].lower().endswith('.gz'):
    people = {l.strip() for l in gopen(argv[2]).read().decode().splitlines()}
else:
    people = {l.strip() for l in open(argv[2]).read().splitlines()}
if argv[1].lower().endswith('.gz'):
    lines = [l.strip() for l in gopen(argv[1]).read().decode().strip().splitlines()]
else:
    lines = [l.strip() for l in open(argv[1]).read().strip().splitlines()]
for l in lines:
    u,v,d = l.split(',')
    if u.count('|') == 2: # virus|person|time identifiers
        u = u.split('|')[1]
    if v.count('|') == 2: # virus|person|time identifiers
        v = v.split('|')[1]
    if d.lower() == 'distance' or (u in people and v in people):
        print(l)
