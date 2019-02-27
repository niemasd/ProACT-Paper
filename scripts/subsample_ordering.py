#!/usr/bin/env python3
from random import sample
from sys import argv,stdin
if len(argv) != 2:
    print("USAGE: %s proportion\nFeed optimal list via stdin"%argv[0]); exit(1)
ls = [l.strip() for l in stdin]
for i in sorted(sample(list(range(len(ls))),int(len(ls)*float(argv[1])))):
    print(ls[i])
