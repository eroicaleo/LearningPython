#!/usr/bin/env python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        for i in range(1, 11):
            if 10 ** i > x:
                i -= 1
                break
        print(i)
        while i >= 1:
            a, b = x // (10**i), x % 10
            print('a, b', a, b)
            if a != b:
                return False
            x, i = (x - a * (10**i) - b) // 10, i - 2
        return True

x = 121
x = 1221
x = 10
x = -121
sol = Solution()
print(sol.isPalindrome(x))
