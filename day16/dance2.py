#!/usr/bin/python3

import sys

characters = 'abcdefghijklmnop'
colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

num_dancers = int(sys.argv[1])

dancers = [ characters[x] for x in range(0,num_dancers) ]

inputfile = open(sys.argv[2])
moves = inputfile.readline().rstrip().split(',')

for rounds in range(0,1000000000):
    for move in moves:
        # print("Executing", move, "on", dancers)
    
        if move[0] == 's':
            num = int(move[1:])
            # print("\tSpinning", num, "from end to start")
            # print("prepend", dancers[-num:], "to", dancers[0:-num])
            dancers = dancers[-num:] + dancers[0:-num]
        elif move[0] == 'x':
            swaps=[int(x) for x in move[1:].split('/')]
            # print("\tSwapping positions", swaps[0], swaps[1])
            temp=dancers[swaps[0]]
            dancers[swaps[0]] = dancers[swaps[1]]
            dancers[swaps[1]] = temp
        elif move[0] == 'p':
            swaps=move[1:].split('/')
            # print("\tPartner swapping", swaps[0], swaps[1])
            pos0 = dancers.index(swaps[0])
            pos1 = dancers.index(swaps[1])
            # print("\tSwapping positions", pos0, pos1)
            temp=dancers[pos0]
            dancers[pos0] = dancers[pos1]
            dancers[pos1] = temp
        else:
            print("Unrecognised move", move)
            exit()

    if rounds % 1000 == 999:
        print("Final positions after round", rounds, ":", "".join(dancers))

print("Final positions:", "".join(dancers))
