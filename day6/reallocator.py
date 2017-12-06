#!/usr/bin/python

import sys
from math import ceil

# Read the input
inputfile = open(sys.argv[1])
banks = [ int(x) for x in inputfile.readline().split() ]

seen = { 'bleh' : 1 }

while True:
    print "Banks: {0}".format(banks)

    # Register that we've seen this state
    bankstate = tuple(banks)
    print bankstate

    seen[bankstate] += 1

    # Find lowest bank with most blocks
    maxb = 0
    maxi = 0
    for i in range(0,len(banks)):
        if banks[i] > maxb:
            maxb = banks[i]
            maxi = i

    print "Most blocks in bank {0}: {1}".format(maxi, maxb)

    blocksperbank = int ( ceil( float(maxb) / len ( banks ) ) )
    blocksleftover = maxb - ( blocksperbank * ( len(banks) - 1 ) )

    print "{0} blocks over {1} banks and {2} left over".format(
            blocksperbank,
            len(banks) - 1,
            blocksleftover
    )

    for i in range(0,len(banks)):
        if i == maxi:
            banks[i] = blocksleftover
        else:
            banks[i] += blocksperbank


    print "Now we have banks: {0}".format(banks)

    break
