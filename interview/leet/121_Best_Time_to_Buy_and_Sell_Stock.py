#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices):
        cost, max_profit = float('inf'), 0
        for p in prices:
            if p < cost:
                cost = p
            max_profit = max(max_profit, p-cost)
        return max_profit

sol = Solution()
price_list = [
[7,6,4,3,1],
[1,2,3,4,5],
[3,3,5,0,0,3,1,4],
]

for prices in price_list:
    print(prices, sol.maxProfit(prices))

