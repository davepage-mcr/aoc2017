#!/usr/bin/python3

import sys
from termcolor import cprint

# Read input, build structures

mymap = []

# directions: 0 - down 1 - right 2 - up 3 - left
directions = [ 'down', 'right', 'up', 'left' ]

inputfile = open(sys.argv[1])
for line in inputfile:
    mymap.append( line.rstrip('\n') )

print(mymap)

# Find starting point

y = 0
x = mymap[0].index('|')
d = 0

visited = []

steps = 0

while True:
    steps += 1
    char = mymap[y][x]
    print("At", tuple([x,y]), "heading", directions[d], "looking at", char);

    if char == '|' or char == '-' or char.isalpha():
        # |  We pass /along/ this if we're heading up or down, /across/ it if we're heading left or right; either way it's all fine
        # -  We pass /across/ this if we're heading up or down, /along/ it if we're heading left or right; either way it's all fine
        # Same with alphanumerics, except we append them to a list

        if char.isalpha():
            if char in visited:
                print("Hit", char, "again - this shouldn't happen!")
                exit()
            visited.append(char)

        if d == 0:
            y += 1
        elif d == 1:
            x += 1
        elif d == 2:
            y -= 1
        elif d == 3:
            x -= 1

    elif char == '+':       # We've hit a corner and need to go a different direction without doubling back on ourselves
        print("Hit a corner at", tuple([x,y]), "while heading", directions[d], d)

        # We can go in direction D if:
        # - we're not already going !D (so we don't double back)
        # - we're not at an edge where going D would make us fall off
        # - the square in direction D is navigable (i.e. not ' ')

        # Can we go down if we're not going up?
        if d != 2:
            print("\tNot going up; considering going down")
            if y >= len(mymap) - 1:
                print("\t\tCan't go down, we're at the bottom")
            elif mymap[y+1][x] == ' ':
                print("\t\tCan't go down, it's a space")
            else:
                print("\t\tGoing down")
                d = 0
                y += 1
                continue
        else:
            print("\tGoing up; can't consider going down as it would double back")

        # Can we go right if we're not going left?
        if d != 3:
            print("\tNot going left; considering going right")
            if x >= len(mymap[y]) - 1:
                print("\t\tCan't go right; we're at the right edge")
            elif mymap[y][x+1] == ' ':
                print("\t\tCan't go right: it's a space")
            else:
                print("\t\tGoing right")
                d = 1
                x += 1
                continue
        else:
            print("\tGoing left; Can't consider going right as it would double back")

        # Can we go up if we're not going down?
        if d != 0:
            print("\tNot going down; considering going up")
            if y == 0:
                print("\t\tCan't go up; we're at the top")
            elif mymap[y-1][x] == ' ':
                print("\t\tCan't go up: it's a space")
            else:
                print("\t\tGoing up")
                d = 2
                y -=1
                continue

        # Can we go left if we're not going right?
        if d != 1:
            print("\tNot going right; considering going left")
            if x == 0:
                print("\t\tCan't go left; we're at the left edge")
            elif mymap[y][x-1] == ' ':
                print("\t\tCan't go left: It's a space")
            else:
                d = 3
                x -= 1
                continue

        print("Nowhere to turn at", tuple([x,y]))
        exit()

    elif char == ' ':
        steps -= 1
        print("Fell off the line at", tuple([x,y]))
        break
    else:
        print("Unrecognised character", char)
        exit()

print("".join(visited))
print(steps)
