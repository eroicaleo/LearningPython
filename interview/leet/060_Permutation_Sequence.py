#!/usr/bin/env python3

import math

class Solution:
    def permSeq(self, n, k):
        l, k = list(range(1,n+1)), k-1
        ret, p = [], math.factorial(n)
        for j in range(n):
            p //= (n-j)
            print(f'l = {l}, k = {k}, p = {p}')
            i, k = k//p, k%p
            ret.append(l.pop(i))
        return ret

sol = Solution()
n = 3
k = 3
n = 4
k = 9
print(sol.permSeq(n, k))

# 213
# n = 4, k = 9
# Output: "2314"
