#!/usr/bin/python

import sys

class Generator:
    def __init__(self, seed, factor):
        self.value = seed
        self.factor = factor

    def iterate(self):
        self.value = ( self.value * self.factor ) % 2147483647
        return self.value

# Read the input

seed_a = int(sys.argv[1])
seed_b = int(sys.argv[2])

gen_a = Generator(seed_a, 16807)
gen_b = Generator(seed_b, 48271)

matches = 0
for i in range(0,40000000):
    val_a = gen_a.iterate()
    val_b = gen_b.iterate()

    # print "{0:16d}\t{1:16d}".format(val_a, val_b)

    lowest16 = 2 ** 16 - 1

    low_a = val_a & lowest16
    low_b = val_b & lowest16

    # print format(low_a, '016b')
    # print format(low_b, '016b')

    if ( low_a == low_b ):
        matches += 1

print matches
