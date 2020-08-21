#!/usr/bin/env python

class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        dp = [0, -prices[0]]
        for p in prices:
            dp[0], dp[1] = max(dp[0], dp[1]+p-fee), max(dp[1], dp[0]-p)
        return max(dp)

    def maxProfit_greedy(self, prices, fee):
        mi, profit = float('inf'), 0
        for p in prices:
            if p < mi:
                mi = p
            elif p > mi+fee:
                profit += (p-mi-fee)
                mi = (p-fee)
        return profit

prices = [1,3,2,8,4,9]
fee = 2
sol = Solution()
print(sol.maxProfit(prices, fee))
print(sol.maxProfit_greedy(prices, fee))
