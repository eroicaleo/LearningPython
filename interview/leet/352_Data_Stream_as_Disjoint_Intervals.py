#!/usr/bin/env python3

from bisect import bisect_left
import math

class SummaryRanges:
    def __init__(self):
        self.I = [[-math.inf, -math.inf], [math.inf, math.inf]]

    def addNum(self, val):
        ix = bisect_left(self.I, [val, val])
        print(f'val = {val}, ix = {ix}')
        if self.I[ix-1][1]+1 == val == self.I[ix][0]-1:
            self.I[ix-1][1] = self.I[ix][1]
            self.I.pop(ix)
        elif self.I[ix-1][1]+1 == val:
            self.I[ix-1][1] = val
        elif val == self.I[ix][0]-1:
            self.I[ix][0] = val 
        elif self.I[ix-1][1] < val < self.I[ix][0]:
            self.I.insert(ix, [val, val])

    def getIntervals(self):
        return self.I[1:-1]

l = [1,3,7]
l = [1,3,2]
l = [1,3,7,5]
l = [1,3,7,2,6]
l = [6,6,0,4,8,7,6,4,7,5]
l = [49,97,53,5,33,65,62,51,100,38,61,45,74,27,64,17,36,17,96,12,79,32,68,90,77,18,39,12,93,9,87,42,60,71,12,45,55,40,78,81,26,70,61]
l = [49,97,53,5,33,65,62,51,100,38,61,45,74,27,64,17,36,17,96,12,79,32,68,90,77,18,39,12,93,9,87,42,60,71,12,45,55,40,78,81,26,70,61,56,66,33,7,70,1,11,92,51,90,100,85,80,0,78,63,42,31,93,41,90,8,24,72,28,30,18,69,57,11,10,40,65,62,13,38,70,37,90,15,70,42,69,26,77,70,75,36,56,11,76,49,40,73,30,37,23]
sol = SummaryRanges()
for i in l:
    sol.addNum(i)
    print(sol.getIntervals())
