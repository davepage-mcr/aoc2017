#!/usr/bin/python

import sys

disk = []

# Read the input

inputstring = sys.argv[1]

def knothash(inputstring):
    circle = range(0,256)

    # Treat input as a string of ASCII characters
    instructions = [ ord(x) for x in inputstring.rstrip() ]
    instructions += [17, 31, 73, 47, 23]

    index = 0
    skipsize = 0

    # Now follow the instructions 64 times, maintaining current index and skipsize
    for myround in range(0,64):
        for inst in instructions:
            sublist = []
            for i in range(0,inst):
                sublist.append(circle[(index + i) % len(circle)])
            sublist = sublist[::-1]

            for i in range (0,inst):
                circle[(index + i) % len(circle)] = sublist[i]

            # Step 4 - incrementing
            index += inst + skipsize
            index %= len(circle)
            skipsize += 1
            skipsize %= len(circle)

    # Create Dense Hash - 16 blocks of 16 numbers, xored
    string = ''
    for block in range(0,16):
        densehash = 0
        blocknums = circle[block * 16:(block + 1)*16]
        for num in blocknums:
            densehash ^= num
        hexchars = "{0:02x}".format(densehash)
        string += hexchars
 
    return string

used = 0
for i in range(0,128):
    hashinput = inputstring + "-" + str(i)
    hexstring = knothash(hashinput)

    # Convert string from hex to binary, count 1s
    binstring = '{0:0128b}'.format(int(hexstring,16))

    disk.append(binstring)
    used += binstring.count('1')

for row in disk:
    print row
