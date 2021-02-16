#!/usr/bin/env python3

class Solution:
    def kthFactor(self, n, k):
        for i in range(1,n+1):
            if n%i == 0:
                k -= 1
            if k == 0:
                return i
        return -1

n, k = 1000, 3
n, k = 4, 4
n, k = 1, 1
n, k = 7, 2
n, k = 12, 3
sol = Solution()
print(n, k, sol.kthFactor(n, k))
