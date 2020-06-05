#!/usr/bin/env python

class Solution:
    def twoCitySchedCost(self, costs):
        N = len(costs)//2
        costs = list(sorted(costs, key=lambda c: c[0]-c[1]))
        s = 0
        for i, c in enumerate(costs):
            s += c[0] if i < N else c[1]
        return s

costs = [[10,20],[30,200],[400,50],[30,20]]
sol = Solution()
print(sol.twoCitySchedCost(costs))
