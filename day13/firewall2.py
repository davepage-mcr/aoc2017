#!/usr/bin/python

import sys

bouncystack_cache = {}

def scannerpos(time, depth):
    # print "\tWhere is the scanner in a stack of depth", depth, "after", time
    if depth in bouncystack_cache:
        bouncystack = bouncystack_cache[depth]
        # print "\tCached this bouncystack", bouncystack
    else:
        bouncystack = range(0,depth) + range (depth - 2, 0, -1)
        # print "\tNew bouncystack", bouncystack
        bouncystack_cache[depth] = bouncystack

    position = time % len(bouncystack)

    return bouncystack[position]

# Read the input
inputfile = open(sys.argv[1])

layers = {}

# Read input, build "sparse array" dictionary
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

for delay in range(0,10000000):
    print "Attempting with a delay of", delay
    if amitrapped(delay) == False:
        print "Got through with no problems after a delay of", delay, "ps"
        break
else:
    print "Delay timed out"
    exit()
