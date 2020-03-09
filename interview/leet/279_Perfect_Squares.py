#!/usr/bin/env python3

import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (1+n)
        for i in range(1, n+1):
            q, dp[i] = int(math.sqrt(i)), i
            if i == q**2:
                dp[i] = 1
                continue
            for q in range(1, q+1):
                dp[i] = min(dp[i], dp[i-q**2]+1)
        print(f'dp[] = {dp}')
        return dp[n]


sol = Solution()
n = 13
print(sol.numSquares(n))
