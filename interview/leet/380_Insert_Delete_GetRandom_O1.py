#!/usr/bin/env python

import random

class Solution:
    def __str__(self):
        return 'count: %d, dict: %s, list: %s' % (self.count, self.valDict, self.valList)

    def __init__(self):
        self.count = 0
        self.valDict = {}
        self.valList = [None] * 5

    def insert(self, val):
        if val in self.valDict:
            pass
        self.valDict[val] = self.count
        self.valList[self.count] = val
        self.count += 1

    def remove(self, val):
        if not val in self.valDict:
            pass
        index = self.valDict[val]
        self.count -= 1
        self.valList[index] = rval = self.valList[self.count]
        self.valList[self.count] = None
        self.valDict[rval] = index
        del self.valDict[val]

    def randomize(self):
        return self.valList[random.randrange(self.count)]

sol = Solution()
sol.insert(1)
print(sol)
sol.insert(2)
print(sol)
sol.insert(3)
print(sol)
print(sol.randomize())
print(sol.randomize())
print(sol.randomize())
print(sol.randomize())
print(sol.randomize())
print(sol.randomize())
sol.remove(1)
print(sol)
sol.insert(4)
print(sol)
print(sol.randomize())
print(sol.randomize())
print(sol.randomize())
print(sol.randomize())
