#!/usr/bin/env python

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x, n = 1.0/x, -n 
        return int(not n) or [1, x][n%2] * self.myPow(x*x, n//2)

sol = Solution()
x, n = 0.00001, 2147483647
x, n = 2.1, 3
x, n = 2.0, 0
x, n = 2.0, -2
x, n = 2.0, 10
x, n = 0.99999, 948688
print(sol.myPow(x, n))
