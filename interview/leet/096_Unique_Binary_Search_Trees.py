#!/usr/bin/env python

class Solution:
    def numTrees(self, n):
        res = [1] + [0] * (n)
        for i in range(1, n+1):
            for j in range(1, i+1):
                res[i] += res[j-1] * res[i-j]
        return res[-1]

sol = Solution()
print(sol.numTrees(4))
