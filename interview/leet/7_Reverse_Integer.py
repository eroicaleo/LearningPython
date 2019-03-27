#!/usr/bin/env python

class Solution:
    def reverse(self, x: int) -> int:
        d = int(('' if x >= 0 else '-') + str(abs(x)).rstrip('0')[::-1] or '0')
        return d if -2**31 <= d < 2**31 else 0

x = 120
x = -123
x = 123
x = 0
sol = Solution()
print(sol.reverse(x))
