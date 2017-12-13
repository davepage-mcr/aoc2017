#!/usr/bin/python

import sys

layers = {}

def scannerpos(layer, depth):
    bouncystack = range(0,depth) + range (depth - 2, 0, -1)
    position = layer % len(bouncystack)

    return bouncystack[position]

# Read the input
inputfile = open(sys.argv[1])

# Read input, build structures
for line in inputfile:
    layer = int(line.split(': ')[0])
    depth = int(line.split(': ')[1])

    layers[layer] = depth

# Now go over layer by layer

trapped = []
severity = 0

maxlayer = max(layers.keys())

for layer in range(0, maxlayer + 1):
    print "Picosecond", layer, ": entering layer", layer
    if not layer in layers:
        print "\tNo scanner here, passing through"
        continue

    print "\tThis layer has depth", layers[layer]

    position = scannerpos(layer, layers[layer])

    print "\tScanner is in position", position, "as we enter"
    if position == 0:
        trapped.append(layer)
        severity += layer * layers[layer]

print "trapped in layers", trapped
print "Total severity:", severity
