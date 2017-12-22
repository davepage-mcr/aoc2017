#!/usr/bin/python3

import sys
import pprint
from math import floor

pp = pprint.PrettyPrinter()

directions = '^>v<'

maxgrid = 1000
grid = {}

def gridprint(curx, cury, direction=None):
    if direction == None:
        dirchar = '|'
    else:
        dirchar = directions[direction]
    print("\t", end="")
    for x in range (-maxgrid, maxgrid+1):
        print("{0:3d}".format(x), end="")
    print()
    for y in range (-maxgrid, maxgrid):
        print(y, end="\t ")
        for x in range (-maxgrid, maxgrid+1):
            if x == curx and y == cury:
                print("{}{}{}".format(dirchar, grid[y][x], dirchar), end="")
            else:
                print(" {} ".format(grid[y][x]), end='')
        print()

for y in range(-maxgrid, maxgrid+1):
    row = {}
    for x in range(-maxgrid, maxgrid+1):
        row[x] = '.'
    grid[y] = row

# Read in the initial map

inputfile = open(sys.argv[1])
initmap = [ x.rstrip() for x in inputfile.readlines() ]

# print("Initial map is",len(initmap),"rows")
halfsize = floor(len(initmap)/2)
# print("Need to map onto empty grid from", [ -halfsize, -halfsize ], "to", [halfsize,halfsize])

for i in range(0,len(initmap)):
    for j in range(0,len(initmap[0])):
        grid[i - halfsize][j - halfsize] = initmap[i][j]

# Now we can start to iterate
direction = 0
x = 0
y = 0
newinfections = 0

for burst in range(0,10000000):
    if burst % 1000 == 0:
        print("*** burst", burst, "at", [x, y], "heading", directions[direction], "; infected nodes:", newinfections)

    # gridprint(x, y, direction)

    if grid[y][x] == '.':
        # print("Clean; turn left, weaken")
        direction = ( direction - 1 ) % len(directions)
        grid[y][x] = 'W'
    elif grid[y][x] == '#':
        # print("Infected; turn right, flag")
        direction = ( direction + 1 ) % len(directions)
        grid[y][x] = 'F'
    elif grid[y][x] == 'W':
        # print("Weakened; carry on, infect")
        grid[y][x] = '#'
        newinfections += 1
    elif grid[y][x] == 'F':
        # print("Flagged; reverse, clean")
        direction = ( direction + 2 ) % len(directions)
        grid[y][x] = '.'
    else:
        print("Unrecognised state", grid[y][x], "at", [x,y])
        exit()

    # Move forward
    if direction == 0:          # Up
        y -= 1
    elif direction == 1:        # Right
        x += 1
    elif direction == 2:        # Down
        y += 1
    elif direction == 3:        # Left
        x -= 1
    else:
        print("Unknown direction", direction)
        exit()

    if abs(x) > maxgrid or abs(y) > maxgrid:
        print("Fell off the grid at", [x, y])
        exit()

print(newinfections)
