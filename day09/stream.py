#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

for line in inputfile:
    ignorenext = False
    ingarbage = False
    depth = 0
    totaldepth = 0
    garbageremoved = 0

    line = line.rstrip()
    print "Parsing input", line

    # Basically a fairly boring finite state machine

    for character in line:
        if ignorenext:
            # Last character was a !, so we ignore the next character
            ignorenext = False
        elif character == '!':
            ignorenext = True
        elif ingarbage and character != '>':
            garbageremoved += 1
        elif ingarbage and character == '>':
            # print "Leaving garbage"
            ingarbage = False
        elif character == '<':
            # print "Entering garbage"
            ingarbage = True
        elif character == '{':
            depth += 1
            # print "Entering new group, depth", depth
        elif character == '}':
            totaldepth += depth
            depth -= 1
            # print "Leaving group, depth now", depth
        elif character == ',':  # Group separator
            pass
        else:
            print "Not sure how to handle", character

    print "\tTotal depth:", totaldepth
    print "\tRemoved garbage:", garbageremoved
