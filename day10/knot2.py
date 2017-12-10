#!/usr/bin/python

import sys
from itertools import cycle

# Read the input

listlength = int(sys.argv[1])
inputfile = open(sys.argv[2])

circle = range(0,listlength)

instructions = [ int(x) for x in inputfile.readline().rstrip().split(',') ]

def printlist (mylist, current, end):
    for index in range(0,len(mylist)):
        ttp = str(mylist[index])
        if index == current:
            ttp = "[" + ttp + "]"
        if index == current:
            ttp = "(" + ttp
        if index == end:
            ttp = ttp + ")"

        print ttp, "\t",

    print

index = 0
skipsize = 0

for inst in instructions:
    print "*** Instruction: reverse sublist of length", inst, "starting from position", index

    # Step 1 & 2 - find start, select length to reverse
    printlist(circle, index, (index + inst - 1 ) % len(circle))
    print "Need to select", inst, "characters from", index, "to", (index + inst - 1) % len(circle)

    # Step 3 - reverse sublist

    # Python list slices don't seem to wrap aroudn the end which is irritating

    sublist = []
    for i in range(0,inst):
        sublist.append(circle[(index + i) % len(circle)])
    print "Sublist to reverse:", sublist
    sublist = sublist[::-1]
    print "Reversed to:", sublist

    for i in range(0,inst):
        circle[(index + i) % len(circle)] = sublist[i]

    # however, the "cycle" iterator from itertools may save us a bit of hassle
    # https://stackoverflow.com/questions/25470799/circular-list-in-python
 
    # Step 4 - incrementing
    index += inst + skipsize
    index %= len(circle)
    skipsize += 1

printlist(circle, -1, -1)

print "First two multiplied is", circle[0] * circle[1]
