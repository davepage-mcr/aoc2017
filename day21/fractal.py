#!/usr/bin/python3

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

def parsestring(instring):
    # convert something like "../.#" to [ [False, False], [False, True] ]
    structure = []
    for line in instring.split('/'):
        structline = []
        for char in line:
            if char == '#':
                structline.append(True)
            else:
                structline.append(False)
        structure.append(tuple(structline))
    return tuple(structure)

def matchrules(subgrid):
    # Does the subgrid match any of our rules?
    # Add rotation, reflection etc.

    print("Passed this to match:", end="\t")
    pp.pprint(subgrid)

    for rule in rules.keys():
        if len(rule) != len(subgrid):
            continue
        print("\tAttempting match with", end="\t")
        pp.pprint(rule)

        if rule == subgrid:
            print("\tMatched!")
            return rules[rule]

    return None

# Import rules from input file
rules = {}
inputfile = open(sys.argv[1])
for line in inputfile:
    [ match, replace ] = line.rstrip().split(' => ')
    rules[parsestring(match)] = parsestring(replace)

grid = parsestring(".#./..#/###")

for iteration in range(0,5):
    print("*** Iteration", iteration,"; grid looks like")
    pp.pprint(grid)

    newgrid = []

    if len(grid) % 2 == 0:
        print("Grid size is divisible by 2; break into 2x2 squares and convert into 3x3 squares")
        breakinto = 2

    elif len(grid) % 3 == 0:
        print("Grid size is divisible by 3; break into 3x3 squares and convert into 4x4 squares")
        breakinto = 3

    for x in range(0,len(grid),breakinto):
        for y in range(0,len(grid),breakinto):
            print("Looking at subgrid starting at", tuple([x,y]))
            subgrid = []
            for line in grid[x:x+breakinto]:
                subgrid.append(line[y:y+breakinto])

            # Does this subgrid match any of our rules?
            newsub = matchrules(tuple(subgrid))
            if newsub == None:
                print("Failed to match:",end="\t")
                pp.pprint(subgrid)
                exit()

            # Fit newsub into newgrid
            newgrid = newsub

    grid = newgrid
