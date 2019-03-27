#!/usr/bin/env python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

x = -121
x = 10
x = 121
sol = Solution()
print(sol.isPalindrome(x))
