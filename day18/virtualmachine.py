#!/usr/bin/python3

import sys

registers = {}
pointer = 0

inputfile = open(sys.argv[1])

instructions = [ x.rstrip().split() for x in inputfile.readlines() ]

while pointer >= 0 and pointer < len(instructions):
    instrs = instructions[pointer]
    print("*** Executing", instrs, "at", pointer)

    instr = instrs[0]
    reg = instrs[1]
    if len(instrs) > 2:
        arg = instrs[2]
    else:
        arg = None

    # Initialise any empty registers
    if not reg in registers:
        registers[reg] = 0

    # Replace any registers in arg with their value
    # Also intify any digits
    if not arg == None:
        if arg.isalpha():
            arg = registers[arg]
        else:
            arg = int(arg)

    if instr == 'set':
        registers[reg] = arg
        print("Register", reg, "set to", registers[reg])
    elif instr == 'add':
        registers[reg] += arg
        print("Register", reg, "set to", registers[reg])
    elif instr == 'mul':
        registers[reg] *= arg
        print("Register", reg, "set to", registers[reg])
    elif instr == 'mod':
        registers[reg] %= arg
        print("Register", reg, "set to", registers[reg])
    elif instr == 'snd':
        print("Playing sound with frequency", registers[reg])
        lastsnd = registers[reg]
    elif instr == 'rcv':
        if registers[reg] != 0:
            print("Last sound played was frequency",lastsnd)
            exit()
        else:
            print("rcv skipped; register",reg, "is zero")
    elif instr == 'jgz':
        if registers[reg] > 0:
            pointer += arg
            print("Pointer set to", pointer)
            continue
        else:
            print("jgz skipped; register", reg, "is <= zero")
    else:
        print("Unrecognised instruction", instr)
        exit()
    pointer += 1
    print("Incrementing pointer to", pointer)
