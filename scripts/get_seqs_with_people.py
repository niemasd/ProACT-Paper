#!/usr/bin/env python3
from gzip import open as gopen
from sys import argv,stdin
def readFASTA(stream):
    seqs = {}
    name = None
    seq = ''
    for line in stream:
        l = line.strip()
        if len(l) == 0:
            continue
        if l[0] == '>':
            if name is not None:
                assert len(seq) != 0, "Malformed FASTA"
                seqs[name] = seq
            name = l[1:]
            assert name not in seqs, "Duplicate sequence ID: %s" % name
            seq = ''
        else:
            seq += l
    assert name is not None and len(seq) != 0, "Malformed FASTA"
    seqs[name] = seq
    return seqs
if len(argv) != 3:
    print("USAGE: %s <fasta_file> <labels_file>"%argv[0]); exit(1)
if argv[1].lower().endswith('.gz'):
    seqs = readFASTA(gopen(argv[1]).read().decode().strip().splitlines())
else:
    seqs = readFASTA(open(argv[1]))
if argv[2] == '-':
    people = {l.strip() for l in stdin}
elif argv[2].lower().endswith('.gz'):
    people = {l.strip() for l in gopen(argv[2]).read().decode().splitlines()}
else:
    people = {l.strip() for l in open(argv[2]).read().splitlines()}
labels = [label for label in seqs if label in people or label.split('|')[1] in people]
for k in labels:
    print('>%s\n%s'%(k,seqs[k]))
