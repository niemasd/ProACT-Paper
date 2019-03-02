#!/usr/bin/env python3
from sys import argv,stdin
if len(argv) != 2:
    print("USAGE: %s <time>\nPass clustering file via stdin, and time is seconds (Unix time)"%argv[0]); exit(1)
TIME = int(argv[1])
for l in stdin:
    if l.startswith('SequenceName'):
        print(l.strip())
    else:
        node,cluster = l.strip().split('\t')
        if int(l.strip().split('\t')[0].split('_')[-1]) <= TIME:
            print(l.strip())
