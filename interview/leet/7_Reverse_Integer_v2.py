#!/usr/bin/env python

class Solution:
    def reverse(self, x: int) -> int:
        val, s, x = 0, -1 if x < 0 else 1, abs(x)
        while x > 0:
            r = x % 10
            x, val = (x-r)//10, val*10+r
        d = s * val
        return d if -2**31 <= d < 2**31 else 0

x = 0
x = -123
x = 120
x = 123
sol = Solution()
print(sol.reverse(x))
