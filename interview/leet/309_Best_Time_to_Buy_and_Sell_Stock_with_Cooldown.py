#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices):
        dp = [float("-inf"), float("-inf"), 0] # [hold a stock, sell the stock, cooldown]
        for p in prices:
            dp = [max(dp[0], dp[2]-p), dp[0]+p, max(dp[1], dp[2])]
            print(dp)
        return max(dp)

prices = [1,2,3,0,2]
sol = Solution()
print(sol.maxProfit(prices))
