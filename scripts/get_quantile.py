#!/usr/bin/env python3
from sys import stdin,argv
q = float(argv[1])
lines = [l.strip() for l in stdin]
end = int(q*len(lines)/2)
seqs = {lines[i]:lines[i+1] for i in range(0,len(lines),2)}
for k in sorted(seqs.keys(), key=lambda x: int(x.split('_')[-1]))[:end]:
    print('%s\n%s' % (k,seqs[k]))
