#!/usr/bin/python3

import sys

steps_per_insert = int(sys.argv[1])

circbuffer = [0]
current_position = 0

def printbuffer():
    print("Current state:", end=" ")
    for i in range(0,len(circbuffer)):
        if i == current_position:
            print("(" + str(circbuffer[i]) + ")", end="\t")
        else:
            print(circbuffer[i], end="\t")
    print()

for i in range(1,50000001):
    if i % 10000 == 0:
        print(i) 

    # printbuffer()
    # Instruction 1: step forward steps_per_insert times
    # print("Stepping forward", steps_per_insert, "from current position", current_position)
    current_position = ( current_position + steps_per_insert ) % len(circbuffer)
    # print("New current position:", current_position)

    # Instruction 2: Insert new value i after current position
    # print("Inserting new value",i,"after current position", current_position)
    # print("Instructions up to new position:", circbuffer[0:current_position+1])
    # print("Instructions after new position:", circbuffer[current_position+1:])

    circbuffer = circbuffer[0:current_position+1] + [ i ] + circbuffer[current_position+1:]

    # Instruction 3: Incrememnt current_position
    current_position = ( current_position + 1 ) % len(circbuffer)

max_value = max(circbuffer)
max_index = circbuffer.index(max_value)
print("Max value", max_value, "is at index", max_index)

zero_index = circbuffer.index(0)
print("0 is at index", max_index)

after_zero = ( zero_index + 1 ) % len(circbuffer)
print("Value following 0 is", circbuffer[after_index])
