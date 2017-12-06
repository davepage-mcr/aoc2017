#!/usr/bin/python

import sys
from math import ceil

# Read the input
inputfile = open(sys.argv[1])
banks = [ int(x) for x in inputfile.readline().split() ]

seen = { }
cycles = 0

while not tuple(banks) in seen:
    print "Banks: {0}".format(banks)

    # Register that we've seen this state
    seen[tuple(banks)] = cycles

    cycles += 1

    # Find lowest bank with most blocks
    maxb = 0
    maxi = 0
    for i in range(0,len(banks)):
        if banks[i] > maxb:
            maxb = banks[i]
            maxi = i

    print "Most blocks in bank {0}: {1}, emptying".format(maxi, maxb)
    banks[maxi] = 0

    blocksperbank = int ( ceil( float(maxb) / len ( banks ) ) )

    print "Allocating {0} blocks per bank, as long as {1} lasts".format(blocksperbank, maxb)

    remainingblocks = maxb
    reallocateto = maxi

    while remainingblocks > 0:
        reallocateto += 1
        reallocateto %= len(banks)
        if ( remainingblocks > blocksperbank ):
            print "\tAllocating {1} new blocks to block {0}".format(reallocateto, blocksperbank)
            banks[reallocateto] += blocksperbank
        else:
            print "\tAllocating {1} new blocks to block {0}".format(reallocateto, remainingblocks)
            banks[reallocateto] += remainingblocks
            break
        remainingblocks -= blocksperbank


print "We've seen {0} before, on cycle {1}".format(banks, seen[tuple(banks)])
print "Got back after {0} cycles, loop is {1} cycles".format(cycles, cycles - seen[tuple(banks)])
