#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

nodes = {}

# Read input, build structures
for line in inputfile:
    node = line.split()[0]
    connections = [ x.rstrip(',') for x in line.split()[2:] ]

    nodes[node] = connections

# Starting from node 0, find all the nodes in the group
def walknodes(node):

    if node in seen:
        return

    seen[node] = True
    for child in nodes[node]:
        walknodes(child)

seen = {}

numgroups = 0

for node in nodes.keys():
    if not node in seen:
        numgroups += 1        
        walknodes(node)

print "There are", numgroups, "groups total"
