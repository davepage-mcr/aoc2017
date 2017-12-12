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

print "Read nodes:", nodes

# Starting from node 0, find all the nodes in the group
def walknodes(node):

    if node in seen:
        return

    seen[node] = True
    for child in nodes[node]:
        walknodes(child)

seen = {}

walknodes('0')

print "Can reach", len(seen.keys()), "nodes from 0"
