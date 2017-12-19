#!/usr/bin/python3

import sys
from termcolor import cprint

# Read input, build structures

mymap = []

# directions: 0 - down 1 - right 2 - up 3 - left
directions = [ 'down', 'right', 'up', 'left' ]

# How we change x and y coordinates if we move in this direction
movedelta = [ [ 0, 1 ], [1, 0], [0,-1], [-1,0] ]

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

        x += movedelta[d][0]
        y += movedelta[d][1]

    elif char == '+':       # We've hit a corner and need to go a different direction without doubling back on ourselves
        print("Hit a corner at", tuple([x,y]), "while heading", directions[d], d)

        # We can go in direction D if:
        # - we're not already going !D (so we don't double back)
        # - we're not at an edge where going D would make us fall off
        # - the square in direction D is navigable (i.e. not ' ')

        turnedcorner = False

        for pd in range(0,len(directions)):
            od = ( pd + 2 ) % len(directions)
            if d != od:
                print("\tNot going", directions[od], "; considering going", directions[pd])
                if movedelta[pd][0] == -1 and x == 0:
                    print("\t\tCan't go", directions[pd], "; we're at an edge")
                elif movedelta[pd][0] == 1 and x == len(mymap[y]) - 1:
                    print("\t\tCan't go", directions[pd], "; we're at an edge")
                elif movedelta[pd][1] == -1 and y == 0:
                    print("\t\tCan't go", directions[pd], "; we're at an edge")
                elif movedelta[pd][1] == 1 and y == len(mymap) - 1:
                    print("\t\tCan't go", directions[pd], "; we're at an edge")
                else:
                    print("\t\tCan go", directions[pd], "if navigable", movedelta[pd])
                    if mymap[y + movedelta[pd][1]][x + movedelta[pd][0]] == ' ':
                        print("\t\tCan't go", directions[pd], "; it's a space")
                    else:
                        print("\t\tWe can move", directions[pd])
                        d = pd
                        x += movedelta[d][0]
                        y += movedelta[d][1]
                        turnedcorner = True
            else:
                print("\tGoing",directions[od], "; can't consider", directions[pd], "as it would double back")

        if turnedcorner == False:
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
