#!/usr/bin/env python3
from sys import argv
from treeswift import read_tree_newick
if len(argv) != 2:
    print("USAGE: %s <tree_file>"%argv[0]); exit(1)
tree = read_tree_newick(argv[1]); leaves = list()
for u in tree.traverse_postorder():
    if u.is_leaf():
        leaves.append(u); u.num_leaves = 1
    else:
        u.num_leaves = sum(c.num_leaves for c in u.children)
for l in leaves:
    print('%s\t%d'%(l.label,sum(c.num_leaves for c in l.parent.children if l != c)))
