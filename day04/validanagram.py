#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

def nodups(words):
    wordict = {}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword in wordict:
            return False
        wordict[sortedword] = 1
    return True


numvalid = 0

for line in inputfile:
    words = line.split()
    if nodups(words):
        print "Valid: " + line.rstrip()
        numvalid += 1
    else:
        print "Invalid: " + line.rstrip()

print str(numvalid) + " valid passphrases"
