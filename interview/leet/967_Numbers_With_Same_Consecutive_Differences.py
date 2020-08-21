#!/usr/bin/env python

class Solution:
    def numsSameConsecDiff(self, N, K):
        self.ret = []
        if N == 1:
            return list(range(10))
        def dfs(pre, n):
            if n == 0:
                self.ret.append(pre)
                return
            d = pre%10
            if d-K >= 0:
                dfs(10*pre+d-K, n-1)
            if K != 0 and d+K < 10:
                dfs(10*pre+d+K, n-1)
        _ = [dfs(i, N-1) for i in range(1, 10)]
        return self.ret

N, K = 3, 7
N, K = 2, 1
N, K = 1, 1
sol = Solution()
print(sol.numsSameConsecDiff(N, K))
