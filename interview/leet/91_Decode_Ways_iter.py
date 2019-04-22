#!/usr/bin/env python

class Solution:
    def numDecodings(self, s):
        dp = [1, 1] + [0] * (len(s)-1)
        if len(s) == 0 or s[0] == '0':
            return 0
        for i in range(1, len(s)):
            # case 1: one letter
            if s[i] != '0':
                dp[i+1] = dp[i]
            # case 2: two letters
            dp[i+1] += (dp[i-1] if 10 <= int(s[i-1:i+1]) <= 26 else 0)
            if dp[i+1] == 0:
                break
        return dp[-1]

sol = Solution()
s = '05'
s = '305'
s = '226'
s = '12'
s = '1'
print(sol.numDecodings(s))
