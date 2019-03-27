#!/usr/bin/env python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or ((x > 0) and (x % 10 == 0)):
            return False
        rev = 0
        while x > rev:
            rev, x = rev * 10 + x % 10, x // 10
        return x in [rev, rev//10]

x = -121
x = 1221
x = 121
x = 10
x = 0
sol = Solution()
print(sol.isPalindrome(x))
