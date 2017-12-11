#!/usr/bin/python

import sys
from itertools import cycle
from math import ceil

directions = ( 'n', 'ne', 'se', 's', 'sw', 'nw' )

# We need a grid where the centre is 0,0 like our spiral thing on day 3
# We shift rows with odd y co-ordinates to make it look hexagonal

# (-2,2)3   (-1,2)2     (0,2)1      (1,2)2      (2,2)3
#      (-2,1)2   (-1,1)1     (0,1)1      (1,1)2      (2,1)3
# (-2,0)2   (-1,0)1     (0,0)0      (1,0)1      (2,0)2
#      (-2,-1)2  (-1,-1)1    (0,-1)1    (1,-1)2     (2,-1)3
# (-2,-2)3  (-1,-2)2    (0,-2)1    (1,-2)2     (2,-2)3

# Now we can define our directions in terms of co-ordinate shifts
# How do we calculate distance from 0,0? There are some nice symmetries above


def opposite(direction):
    dirindex = directions.index(direction)
    return directions[(dirindex + 3) % len(directions)]

def distance(coords):
    x = coords[0]
    y = coords[1]

    if x < 0 and y % 2 == 1:
        x += 1

    xdist = abs(x)
    ydist = abs(int(ceil(y/2.0)))

    return xdist + ydist

coords=[0,0]
maxdist = 0

# Read the input
inputfile = open(sys.argv[1])
instructions = inputfile.readline().rstrip().split(',')

for inst in instructions:
    print "At", coords, "moving", inst

    if inst == 'n':
        coords[1] += 2
    elif inst == 'ne':
        if coords[1] % 2 == 1:
            coords[0] += 1
        coords[1] += 1
    elif inst == 'se':
        if coords[1] % 2 == 1:
            coords[0] += 1
        coords[1] -= 1
    elif inst == 's':
        coords[1] -= 2
    elif inst == 'sw':
        if coords[1] % 2 == 0:
            coords[0] -= 1
        coords[1] -= 1
    elif inst == 'nw':
        if coords[1] % 2 == 0:
            coords[0] -= 1
        coords[1] += 1
    else:
        print "Illegal instruction", inst
        exit(1)

    curdist = distance(coords)
    if curdist > maxdist:
        maxdist = curdist

print "Ended up at", coords, "distance", curdist
print "Max distance was", maxdist
