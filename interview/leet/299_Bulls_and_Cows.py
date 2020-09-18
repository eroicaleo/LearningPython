#!/usr/bin/env python3

from collections import Counter
class Solution:
    def getHint(self, secret, guess):
        rs, rg = Counter(), Counter()
        A = B = 0
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                rs[i] += 1
                rg[j] += 1
        for k in rs:
            B += min(rs[k], rg[k])
        return f'{A}A{B}B'


secret, guess = '1123', '0111'
secret, guess = '1807', '7810'
secret, guess = '1122', '2211'

sol = Solution()
print(sol.getHint(secret, guess))
