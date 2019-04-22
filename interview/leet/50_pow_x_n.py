#!/usr/bin/env python

class Solution:
    def myPow(self, x, n):
        ret, absn = 1, abs(n)
        while absn >= 1:
            if absn % 2 == 1:
                ret *= x
            x, absn = x*x, absn//2
        return ret if n >= 0 else 1.0/ret

sol = Solution()
x, n = 2.1, 3
x, n = 2.0, 0
x, n = 2.0, 10
x, n = 0.00001, 2147483647
x, n = 0.99999, 948688
x, n = 2.0, -2
print(sol.myPow(x, n))
