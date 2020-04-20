#!/usr/bin/env python3

#   Ф b a b g b a g
# Ф 1 1 1 1 1 1 1 1
# b 0 1 1 2 2 3 3 3
# a 0 0 1 1 1 1 4 4
# g 0 0 0 0 1 1 1 5

#   Ф r a b b b i t
# Ф 1 1 1 1 1 1 1 1
# r 0 1 1 1 1 1 1 1
# a 0 0 1 1 1 1 1 1
# b 0 0 0 1 2 3 3 3
# b 0 0 0 0 1 3 3 3 
# i 0 0 0 0 0 0 3 3
# t 0 0 0 0 0 0 0 3

#   b a g
# Ф 0 0 0
# b 1 0 0
# a 1 1 0
# b 2 1 0
# g 2 1 1
# b 3 1 1
# a 3 4 1
# g 3 4 5

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        curr, prev = [0]*(1+len(s)), [1]*(1+len(s))
        for ct in t:
            for i, cs in enumerate(s):
                curr[i+1] = curr[i] + (prev[i] if ct == cs else 0)
            print(curr)
            curr, prev = [0]*(1+len(s)), curr
        return prev[-1]

    def numDistinct2(self, s: str, t: str) -> int:
        curr, prev = [1]*(1+len(s)), 1
        for ct in t:
            for i, cs in enumerate(s):
                prev, curr[i+1] = curr[i+1], curr[i] + (prev if ct == cs else 0)
            print(curr)
            prev = 0
        return curr[-1]


sol = Solution()
s = "babgbag"
t = "bag"
s = "rabbbit"
t = "rabbit"
print(sol.numDistinct(s, t))
