#!/usr/bin/env python

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        ret = []
        sorted_intervals = sorted(intervals, key=lambda iv: iv.start)
        for iv in sorted_intervals:
            if not ret or ret[-1].end < iv.start:
                ret.append(iv)
            else:
                ret[-1].end = max(ret[-1].end, iv.end)
        return ret

intervals = [[1,4],[4,5]]
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[8,10],[2,6],[1,3],[15,18]]
# [[1,6],[8,10],[15,18]]
sol = Solution()
print([[iv.start, iv.end] for iv in sol.merge([Interval(iv[0], iv[1]) for iv in intervals])])

# [[1,5]]
