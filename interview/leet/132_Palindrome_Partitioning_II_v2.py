#!/usr/bin/env python

# Based on hongyu9310's 2nd Solution

#   Ф a a b
# Ф
# a
# a
# b

class Solution:
    def minCut(self, s):
        l = len(s)
        
        # cut[i] means the no. of min cuts of s[:i]
        cut = list(range(-1, l))

        # dp[i][j] = (s[i:j] is palindrome)
        dp = [[0] * (l+1) for _ in range(l+1)]

        # Populate dp[i][j]
        for j in range(1, l+1):
            dp[j][j] = dp[j-1][j] = 1
            cut[j] = cut[j-1]+1
            for i in range(j-2, -1, -1):
                dp[i][j] = (dp[i+1][j-1]) * (s[i]==s[j-1])
                if dp[i][j]:
                    cut[j] = min(cut[j], cut[i]+1)
            print(f'cut = {cut}')

        for row in dp:
            print(row)
        return cut[-1]


s = 'aab'
s = 'abcbad'
s = ''
sol = Solution()
print(sol.minCut(s))
