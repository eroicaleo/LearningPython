#!/usr/bin/env python3

class Solution:
    def smallestRangeII(self, A, K):
        B, l = [a-K for a in sorted(A)], len(A)
        ret = B[-1]-B[0]
        for i in range(l-1):
            lb = min(B[0]+2*K, B[i+1])
            ub = max(B[i]+2*K, B[-1])
            ret = min(ub-lb, ret)
        return ret

A, K = [1,3,6], 3
A, K = [1], 0
A, K = [0, 10], 2
sol = Solution()
print(sol.smallestRangeII(A, K))
