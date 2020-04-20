#!/usr/bin/env python3

class Solution:
    def combine(self, n, k):
        comb = [[]]
        for i in range(k):
            comb = [c+[j] for c in comb for j in range((c[-1] if c else 0)+1, n-k+i+2)]
        return comb

n, k = 4, 1
n, k = 4, 4
n, k = 4, 2
n, k = 4, 3
n, k = 4, 0
sol = Solution()
print(sol.combine(n,k))
