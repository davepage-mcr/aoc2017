#!/usr/bin/python
# vim: set fileencoding=utf8

import sys
from math import sqrt

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

def finddist ( target ):
  if ( target == 1 ):
    return 0

  ring = int((sqrt(target)+1) / 2)
  # print str(target) + " is on ring " + str(ring)

  ringstart = ( ring * 2 - 1 ) ** 2 + 1
  ringend = ( ring * 2 + 1 ) ** 2
  dir = 0
  coords = [ ring, -ring + 1]

  for step in range(ringstart, ringend):
    # print "We are at " + str(step) + " " + str(coords) + " heading " + dirs[dir] + " towards " + str(ringend)
    # Are we there yet?
    if step == target:
        return abs(coords[0]) + abs(coords[1])

    # turn before we fall off?
    if dir == 0 and coords == [ ring, ring ]:
        # print "Hit top-right, turning left"
        dir = 1
    elif dir == 1 and coords == [ -ring, ring ]:
        # print "Hit top-left, turning left"
        dir = 2
    elif dir == 2 and coords == [ -ring, -ring ]:
        # print "Hit bottom-left, turning left"
        dir = 3
    elif dir == 3 and coords == [ ring, -ring ]:
        print "Hit bottom-right, this has gone wrong"
        return None

    if dir == 0:
        coords[1] = coords[1] + 1
    if dir == 1:
        coords[0] = coords[0] - 1
    if dir == 2:
        coords[1] = coords[1] - 1
    if dir == 3:
        coords[0] = coords[0] + 1

for test in ( (1,0), (12,3), (23,2), (1024,31) ):
  assert finddist(test[0]) is test[1], "Expected %d to have dist %d" % ( test )

print finddist(277678)
