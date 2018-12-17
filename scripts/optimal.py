#!/usr/bin/env python3
from gzip import open as gopen
from sys import argv
if len(argv) != 4:
    print("USAGE: %s <transmissions.txt.gz> <time> <n>"%argv[0]); exit()
T = float(argv[2])
N = int(argv[3])
num_infections = {}
for line in gopen(argv[1]):
    u,v,t = line.decode().strip().split('\t')
    if u not in num_infections:
        num_infections[u] = 0
    if float(t) >= T:
        num_infections[u] += 1
for n,u in sorted([(num_infections[u],u) for u in num_infections], reverse=True)[:N]:
    print(u)
