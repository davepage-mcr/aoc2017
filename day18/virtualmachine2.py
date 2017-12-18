#!/usr/bin/python3

import sys


class Program:
    def __init__(self, progid):
        self.registers = {}
        self.registers['p'] = progid

        self.pointer = 0


    def execute(self, instr, reg, arg):
        # Initialise any empty registers
        if not reg in self.registers:
            self.registers[reg] = 0

        # Replace any registers in arg with their value
        # Also intify any digits
        if not arg == None:
            if arg.isalpha():
                arg = self.registers[arg]
            else:
                arg = int(arg)

        if instr == 'set':
            self.registers[reg] = arg
            print("Register", reg, "set to", self.registers[reg])
        elif instr == 'add':
            self.registers[reg] += arg
            print("Register", reg, "set to", self.registers[reg])
        elif instr == 'mul':
            self.registers[reg] *= arg
            print("Register", reg, "set to", self.registers[reg])
        elif instr == 'mod':
            self.registers[reg] %= arg
            print("Register", reg, "set to", self.registers[reg])
        elif instr == 'snd':
            print("Playing sound with frequency", self.registers[reg])
            self.lastsnd = self.registers[reg]
        elif instr == 'rcv':
            if self.registers[reg] != 0:
                print("Last sound played was frequency",self.lastsnd)
                exit()
            else:
                print("rcv skipped; register",reg, "is zero")
        elif instr == 'jgz':
            if self.registers[reg] > 0:
                self.pointer += arg
                print("Pointer set to", self.pointer)
                return
            else:
                print("jgz skipped; register", reg, "is <= zero")
        else:
            print("Unrecognised instruction", instr)
            exit()
        self.pointer += 1
        print("Incrementing pointer to", self.pointer)

inputfile = open(sys.argv[1])
instructions = [ x.rstrip().split() for x in inputfile.readlines() ]

program = Program(0)

while program.pointer >= 0 and program.pointer < len(instructions):
    instrs = instructions[program.pointer]
    print("*** Executing", instrs, "at", program.pointer)

    instr = instrs[0]
    reg = instrs[1]
    if len(instrs) > 2:
        arg = instrs[2]
    else:
        arg = None

    program.execute(instr, reg, arg)
