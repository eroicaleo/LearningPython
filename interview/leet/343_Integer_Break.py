#!/usr/bin/env python

class Solution:
    def integerBreak(self, n):
        q, r = divmod(n, 3)
        if r == 0:
            return 3**q
        elif r == 1:
            return int(4*3**(q-1))
        else:
            return 2*3**q

sol = Solution()
i = 20
for i in range(20):
    print(i, sol.integerBreak(i))
