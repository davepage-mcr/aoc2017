#!/usr/bin/python
# vim: set fileencoding=utf8

import sys
import numpy

# Read the input

# 37 *36* 35  34  33  32  31
# 38  17 *16* 15  14  13  30
# 39  18   5  *4*  3  12  29
# 40  19   6  _1_  2  11  28
# 41  20   7   8  _9_ 10  27
# 42  21  22  23  24 _25_ 26
# 43  44  45  46  47  48 _49_

# We need to map arbitary numbers onto co-ordinates, where 1 above is (0,0)

# Ring 0:           Ends 1 = ( 0 * 2 + 1 )² at (0,0);    Starts 1  = ( 0 * 2 - 1)² + 1 at (0,0)
#
# Ring 1: 2 to 9:   Starts 2  = ( ring1 * 2 - 1)² - 1   at (1,0)
#                   Ends 9    = ( ring1 * 2 + 1 )²      at (1,-1);
# Ring 2: 10 to 25: Ends 25 is ( 2 * 2 + 1 )² at (2,-2); Starts 10 = ( ring 2 * 2 - 1)² + 1 at (2,-1)
# Ring 3: 26 to 49: Ends 49 is ( 3 * 2 + 1 )² at (3,-3); Starts 26 = ( ring 3 * 2 - 1)² + 1 at (3,-2)

dirs=( 'up', 'left', 'down', 'right' )

# step 0 is a freebie
maxring = 100

grid = [ [0] * maxring for i in range(-maxring, maxring) ]
grid[0][0] = 1

def neighboursum ( coords ):
    # print "Calculating value for " + str(coords)
    sum = 0

    for relative in ( (-1, 0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ):
        relx = coords[0] + relative[0]
        rely = coords[1] + relative[1]
        value = grid[relx][rely]
        # print "  Value at " + str( [ relx, rely ] ) + " is " + str(value)
        sum = sum + value
    return sum

def findvgt( target ):
  # Need to find the square with value greater than target
  # Take advantage of Python dicts having non-natural integers as keys

  step = 1
  ring = 1
  coords = [1, 0]
  dir = 0

  # Safety iteration for what would be an infinite loop
  while step < 100:
    print "Step " + str(step) + " at " + str(coords)

    if grid[coords[0]][coords[1]] == 0:     # Unpopulated
        value = neighboursum(coords)
        grid[coords[0]][coords[1]] = value 
        print "New value for " + str(coords) + " is " + str(value)
    else:
        value = grid[coords[0]][coords[1]]
        print "Old value for " + str(coords) + " is " + str(value)

    if value > target:
        return value


    # turn before we fall off?
    if dir == 0 and coords == [ ring, ring ]:
        print "Hit top-right, turning left"
        dir = 1
    elif dir == 1 and coords == [ -ring, ring ]:
        print "Hit top-left, turning left"
        dir = 2
    elif dir == 2 and coords == [ -ring, -ring ]:
        print "Hit bottom-left, turning left"
        dir = 3
    elif dir == 3 and coords == [ ring + 1, -ring ]:
        print "Hit bottom-right, turning left"
        ring = ring + 1
        dir = 0

    if dir == 0:
        coords[1] = coords[1] + 1
    if dir == 1:
        coords[0] = coords[0] - 1
    if dir == 2:
        coords[1] = coords[1] - 1
    if dir == 3:
        coords[0] = coords[0] + 1

    step = step + 1

  print "Fell off while"

  return None

print findvgt(277678)
