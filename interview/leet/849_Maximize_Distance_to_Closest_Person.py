#!/usr/bin/env python3

class Solution:
    def maxDistToClosest(self, seats):
        p, res = -1, 0
        for i, s in enumerate(seats):
            if s:
                if p < 0:
                    res = i
                else:
                    res = max((i-p)//2, res)
                p = i
        return max(res, i-p)

sol = Solution()
seats = [0, 1]
seats = [1,0,0,0]
seats = [1,0,0,0,1,0,1]
print(sol.maxDistToClosest(seats))

