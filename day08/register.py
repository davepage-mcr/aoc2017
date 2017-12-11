#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

registers = {}
maxvalue = 0

for line in inputfile:
    instruction = line.split()

    print instruction

    register = instruction[0]
    operation = instruction[1]
    value = int(instruction[2])

    testreg = instruction[4]
    testcomp = instruction[5]
    testval = int(instruction[6])

    # Initialise unseen registers to 0
    if not register in registers:
        registers[register]=0

    if not testreg in registers:
        registers[testreg]=0

    # Does the condition pass?
    condition = False
    if testcomp == '>' and registers[testreg] > testval:
        condition = True
    elif testcomp == '<' and registers[testreg] < testval:
        condition = True
    elif testcomp == '==' and registers[testreg] == testval:
        condition = True
    elif testcomp == '<=' and registers[testreg] <= testval:
        condition = True
    elif testcomp == '>=' and registers[testreg] >= testval:
        condition = True
    elif testcomp == '!=' and registers[testreg] != testval:
        condition = True

    if condition == False:
        print "Condition failed, skipping"
        continue

    print "Condition passed"

    if operation == 'inc':
        registers[register] += value
    elif operation == 'dec':
        registers[register] -= value

    # Store new max if required
    if registers[register] > maxvalue:
        maxvalue = registers[register]

    print registers

# Now find the largest value in any register

print "Maximum in registers at end:", max(registers.values())

print "Max value ever was:", maxvalue
