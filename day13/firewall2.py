#!/usr/bin/python

import sys
from fractions import gcd

layers = {}

def scannerpos(time, depth):
    print "\tWhere is the scanner in a stack of depth", depth, "after", time
    bouncystack = range(0,depth) + range (depth - 2, 0, -1)
    print "\t", bouncystack
    position = time % len(bouncystack)

    return bouncystack[position]

# Read the input
inputfile = open(sys.argv[1])

# Read input, build structures
for line in inputfile:
    layer = int(line.split(': ')[0])
    depth = int(line.split(': ')[1])

    layers[layer] = depth

maxlayer = max(layers.keys())

# Now go over layer by layer
def amitrapped(delay):
    trapped = []
    severity = 0
    time = delay 
    for layer in range(0, maxlayer + 1):
        print "\tPicosecond", time, ": entering layer", layer
        if layer in layers:
            position = scannerpos(time, layers[layer])
    
            print "\tScanner is in position", position, "as we enter"
            if position == 0:
                trapped.append(layer)
                severity += layer * layers[layer]
                print "\t** Trapped in layer", layer
                return True

        time += 1
    return False

# No point looking beyond the lowest common multiple of the depths, as
# after this we're just looping.

depths = layers.values()
lcm = depths[0]
for i in depths:
    lcm = lcm * i / gcd(lcm, i)

print "Attempting delays up to", lcm

for delay in range(0,lcm):
    print "Attempting with a delay of", delay
    if amitrapped(delay) == False:
        print "Got through with no problems after a delay of", delay, "ps"
        break
else:
    print "Delay timed out"
    exit()
