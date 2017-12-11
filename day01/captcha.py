#!/usr/bin/python

# Read the input from the file "input"

inputfile = open("input")

inputlist = [ int(item) for item in inputfile.readline().rstrip() ]

# Split into an array and loop

sum = 0
for index in range (0, len(inputlist)):
    nextindex = ( index + 1 ) % len(inputlist)
    if ( inputlist[index] == inputlist[nextindex] ):
        sum += inputlist[index]

print sum
