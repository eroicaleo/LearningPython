#!/usr/bin/env python3

class Solution:

    # I got the Solution from "Simple explanation on how to arrive at the Solution"
    # And also the fastest solution
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a^b)&mask, ((a&b)<<1)&mask
        return a if a < 0x7FFFFFFF else ~(a^mask)


sol = Solution()
# print(sol.getSum(-2, 3))
# print(sol.getSum(1, 2))
# print(sol.getSum(-3, -2))
print(sol.getSum(-14, 16))
print(-2 ^ -3)
print(-2 & -3)
print((-2 & -3)<<1)
print(-8 ^ 3)
print(-8 & 3)
