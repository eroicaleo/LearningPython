#!/usr/bin/env python3

class Solution:
    def count(self, n):
        ret = [0]
        i, k = 0, 1
        while i < n:
            for i in range(k, min(2*k,n+1)):
                ret.append(ret[i%(k)]+1)
            k *= 2
        return ret

sol = Solution()
print(sol.count(7))
print(sol.count(2))
