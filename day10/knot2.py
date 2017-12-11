#!/usr/bin/python

import sys
from itertools import cycle

# Read the input

inputfile = open(sys.argv[1])

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

# Need numbers from 0 to 255
circle = range(0,256)

# Treat input as ASCII characters
instructions = [ ord(x) for x in inputfile.readline().rstrip() ]

# Add fixed suffix
instructions += [17, 31, 73, 47, 23]


index = 0
skipsize = 0

# Now follow the instructions 64 times, maintaining current index and skipsize
for myround in range(0,64):
    print "*** Round", myround, "; index is", index, "; skipsize is", skipsize
    # print "Instructions:", instructions
    for inst in instructions:
        # Step 1 & 2 - find start, select length to reverse
        # printlist(circle, index, (index + inst - 1 ) % len(circle))
        # print "Need to select", inst, "characters from", index, "to", (index + inst - 1) % len(circle)
    
        # Step 3 - reverse sublist
        # Python list slices don't seem to wrap aroudn the end which is irritating
    
        sublist = []
        for i in range(0,inst):
            sublist.append(circle[(index + i) % len(circle)])
        # print "Sublist to reverse:", sublist
        sublist = sublist[::-1]
        # print "Reversed to:", sublist
    
        for i in range(0,inst):
            circle[(index + i) % len(circle)] = sublist[i]
    
        # Step 4 - incrementing
        index += inst + skipsize
        index %= len(circle)
        skipsize += 1
        skipsize %= len(circle)

print "This is our sparse hash, list of numbers from 0 to 255 in some order"
printlist(circle, -1, -1)

# Create Dense Hash - 16 blocks of 16 numbers, xored
string = ''
for block in range(0,16):
    densehash = 0
    blocknums = circle[block * 16:(block + 1)*16]
    for num in blocknums:
        densehash ^= num
    hexchars = "{0:02x}".format(densehash)
    print blocknums, densehash, hexchars
    string += hexchars

print string
