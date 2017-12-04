#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

checksum = 0

for line in inputfile:
    numbers = [ int(num) for num in line.split() ]
    highest = max(numbers)
    lowest = min(numbers)

    diff = highest - lowest
    print "Difference between highest " + str(highest) + " and lowest " + str(lowest) + " is " + str(diff)
    checksum += diff

print "Checksum is " + str(checksum)
