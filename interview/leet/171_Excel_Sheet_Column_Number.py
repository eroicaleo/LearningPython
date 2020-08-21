#!/usr/bin/env python3

class Solution:
    def titleToNumber(self, s):
        n = 0
        for c in s:
            n = 26*n+(1+ord(c)-ord('A'))
        return n

    def titleToNumber_1line(self, s):
        return sum(26**i * (1+ord(c)-ord('A')) for i, c in enumerate(s[::-1]))

s_list =['A', 'AB', 'ZY']
sol = Solution()
for s in s_list:
    print(sol.titleToNumber(s))
    print(sol.titleToNumber_1line(s))
