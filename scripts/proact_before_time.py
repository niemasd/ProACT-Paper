#!/usr/bin/env python3
from gzip import open as gopen
from subprocess import check_output
from sys import argv
from tempfile import NamedTemporaryFile
from treeswift import read_tree_newick
if len(argv) != 5:
    print("USAGE: %s <tree> <diagnosis> <time> <proact_method>"%argv[0]); exit()
END = float(argv[3])
t = read_tree_newick(argv[1]).extract_tree_with(l.split('\t')[0] for l in gopen(argv[2]).read().decode().strip().splitlines() if float(l.split('\t')[1]) <= END)
tmp = NamedTemporaryFile(mode='w'); tmp.write(t.newick()); tmp.flush()
print(check_output(['ProACT.py','-t',tmp.name,'-d',argv[2],'-m',argv[4]]).decode())
