#!/usr/bin/env python3

class Solution:
    def checkValidString(self, s: str) -> bool:
        lcnt = rcnt = 0
        for c in s:
            rcnt += -1 if c == ')' else +1
            lcnt +=  1 if c == '(' else max(lcnt-1, 0)
            if rcnt < 0:
                return False
        return lcnt == 0

sol = Solution()
s = '(**))'
s = '(**))('
print(sol.checkValidString(s))
