#!/usr/bin/python3

import sys
from termcolor import cprint

seen = {}

num_regions = 0

characters = '123456789abcdefghijklmnopqrstuvwxyz'
colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

def findregions(x, y, region):
    global num_regions

    if mymap[y][x] == '0':
        # This is not a region
        return

    coords = tuple([x,y])
    if coords in seen:
        # Already seen this, it's boring
        return

    if region == None:
        num_regions += 1
        # print "Found region", num_regions, "starting at", coords
    else:
        # print "Extending region", num_regions, "to", coords
        pass

    seen[coords] = 1
    mymap[y][x] = num_regions;

    # Now recurse if it fits
    if x - 1 >= 0:
        findregions(x -1, y, 1)

    if x + 1 < len(mymap[y]):
        findregions(x + 1, y, 1)

    if y - 1 >= 0:
        findregions(x, y - 1, 1)

    if y + 1 < len(mymap):
        findregions(x, y + 1, 1)

# Read input, build structures

mymap = []

inputfile = open(sys.argv[1])
for line in inputfile:
    mymap.append( list( line.rstrip() ) )

for y in range(0,len(mymap)):
    for x in range(0,len(mymap[y])):
        findregions(x,y,None)

for line in mymap:
    for region in line:
        if region == '0':
            print(' ', end='')
        else:
            cprint(characters[region % len(characters)], colours[region % len(colours)], end='')
    print("")

print("Total regions:", num_regions)
