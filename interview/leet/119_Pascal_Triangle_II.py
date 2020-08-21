#!/usr/bin/env python3

class Solution:
    def getRow(self, rowIndex):
        ret, numer, denom = [1], 1, 1
        for i in range(0, rowIndex):
            numer *= (rowIndex-i)
            denom *= (1+i)
            ret.append(numer//denom)
        return ret

sol = Solution()
for i in range(10):
    print(sol.getRow(i))
