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

for burst in range(0,10000):
    print("*** burst", burst, "at", [x, y], "heading", directions[direction])

    # gridprint(x, y, direction)

    if grid[y][x] == '#':
        # Turn right
        direction = ( direction + 1 ) % len(directions)
        # Disinfect
        grid[y][x] = '.'
    else:
        # print("This square", [x,y], "is uninfected; turning left and infecting")
        # Turn left
        direction = ( direction - 1 ) % len(directions)
        # Infect
        grid[y][x] = '#'
        newinfections += 1

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
