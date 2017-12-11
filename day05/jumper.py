#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

# Slurp into array
jumps = [ int(x.rstrip()) for x in inputfile.readlines() ]

index = 0
steps = 0

while index < len(jumps):
    newindex = index + jumps[index]

    print "At position " + str(index) + " about to jump " + str(jumps[index]) + " steps to " + str(newindex)

    jumps[index] += 1
    index = newindex
    steps += 1

print "Escaped after " + str(steps) + " steps"

print jumps
