#!/usr/bin/python

import sys

# Read the input
inputfile = open(sys.argv[1])

# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth

allnodes = {}

class TreeNode:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.childnames = [ x.rstrip(',') for x in children ]
        allnodes[name] = self

    def totalweight(self):
        if hasattr(self, '_weightcache'):
            return self._weightcache

        total = self.weight
        for child in self.children:
            total += child.totalweight()
        self._weightcache = total
        return total


def findimbalance(node, target):
    print "*** Looking for imbalance from", node.name

    if len(node.children) == 0:
        # No children, we must be the problem
        node.target = target
        return node

    tally = {}
    childrenweight = 0
    for child in node.children:
        childweight = child.totalweight()
        childrenweight += childweight
        if childweight in tally:
            tally[child.totalweight()] += 1
        else:
            tally[child.totalweight()] = 1
 
    # If all the weights are the same, then we are the problem!
    if len ( tally.keys() ) == 1:
        print node.name, " has no unbalanced children; weighs", node.totalweight(), "inc children should be", target
        node.target = target - childrenweight
        return node

    # Find the unbalanced one - should be the key in tally with value 1
    for weight, num in tally.items():
        if num == 1:
            unbalanced = weight
        else:
            newtarget = weight
    print "Unbalanced child weight is", unbalanced, "- should be", newtarget

    # Now find the child with that weight
    for child in node.children:
        if child.totalweight() == unbalanced:
            ubchild = child
            break

    print "Unbalanced child is", ubchild.name

    return findimbalance(child, newtarget)

#### Main logic here

for line in inputfile:
    # Parse out name, weight, children
    fields = line.split()
    name = fields[0]
    weight = int(fields[1][1:-1])
    children = fields[3:]

    node = TreeNode(name, weight, children)

# Now we iterate over the nodes and fill in parent / child information
# TODO: Can we somehow do this during creation?

for nodename in allnodes.keys():
    node = allnodes[nodename]
    node.children = [ allnodes[x] for x in node.childnames ]
    for child in node.children:
        child.parent = node

# We've ended up with an arbitrary node. Let's start from here!

node = allnodes[nodename]

while hasattr(node, 'parent'):
    node = node.parent
bottom = node

print "Looking at", bottom.name, "which has no parent and hence is bottom node"

## For part 2, we need to walk the tree starting with bottom node's children
unbalanced = findimbalance(bottom, None)

print "Unbalanced node is", unbalanced.name, "- weighs", unbalanced.weight, "should be", unbalanced.target
