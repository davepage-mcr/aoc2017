#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

checksum = 0

def getdivisor ( numbers ):
    for divisor in numbers:
        for num in numbers:
            if divisor == num:
                continue
            if ( num % divisor ) == 0:
                return num / divisor

for line in inputfile:
    numbers = [ int(num) for num in line.split() ]
    result = getdivisor(numbers)
    print "Neat division: " + str(result)
    checksum += result

print "Checksum is " + str(checksum)
