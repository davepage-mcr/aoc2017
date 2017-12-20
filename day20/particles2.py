#!/usr/bin/python3

import sys

class Particle:
    def __init__(self, num, classdata):
        self.num = num
        self.classdata = {}
        self.classdata = classdata

    def calcmanhattan(self):
        dist = 0
        for i in range(0,3):
            dist += abs(self.classdata['p'][i])
        return dist

    def tick(self):
        for i in range(0,3):
            self.classdata['v'][i] += self.classdata['a'][i]
            self.classdata['p'][i] += self.classdata['v'][i]

    def getposition(self):
        return tuple(self.classdata['p'])

def sortbymanhattan(a, b):
    return cmp( a.manhattan, b.manhattan )

particles = []

partnum = 0
inputfile = open(sys.argv[1])
for line in inputfile:
    classdata = {}

    # Split into position, velocity, accelleration
    data = line.rstrip().split(', ')

    for item in data:
        [ datatype, valuestr ] = item.split('=')
        valuestr = valuestr.replace('<',"").replace('>',"")
        values = [ int(x) for x in valuestr.split(',') ]

        classdata[datatype] = values

    particles.append(Particle(partnum, classdata))
    partnum += 1

# Which particle will stay closest to <0,0,0> in the long term?
# Iterate for say 10,000 steps and then see what's closest

for t in range(0,10000):
    collidoscope = {}
    collisions = []

    for p in particles:
        p.tick()
        pos = p.getposition()

        if pos in collidoscope:
            print("Particle", p.num, "and particle", collidoscope[pos].num, "have collided at", pos)
            if not collidoscope[pos] in collisions:
                collisions.append(collidoscope[pos])
            collisions.append(p)
        else:
            collidoscope[pos] = p

    for collided in collisions:
        print(t, "Removing collided particle", collided.num)
        particles.remove(collided)

# Now see which is closest
for p in particles:
    p.manhattan = p.calcmanhattan()

particles.sort( key=lambda part: part.manhattan )
print( particles[0].num, "is closer" )

print( len(particles), "particles left")
