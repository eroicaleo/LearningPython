#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices):
        l = len(prices)
        dp = [[0]*l for i in range(3)]
        for k in range(1,3):
            for i in range(1,l):
                profit = dp[k][i-1]
                for j in range(0, i):
                    profit = max(profit, prices[i]-prices[j]+(0 if j==0 else dp[k-1][j-1]))
                dp[k][i] = profit
            print(f'k={k}, dp[k]={dp[k]}')

    def maxProfit2(self, prices):
        l = len(prices)
        dpbuy, dpsel = [0]*l, [0]*l
        for i in range(2):
            dpsel[0], dpbuy[0] = 0, -prices[0]
            print(f'before dpbuy = {dpbuy}')
            print(f'before dpsel = {dpsel}')
            for j in range(1, l):
                dpbuy[j] = max(dpbuy[j-1], dpsel[j-1]-prices[j])
            for j in range(1, l):
                dpsel[j] = max(dpsel[j-1], dpbuy[j-1]+prices[j])
            print(f'after dpbuy = {dpbuy}')
            print(f'after dpsel = {dpsel}')
        return dpsel[-1]

    def maxProfit3(self, prices):
        buy1 = buy2 = -prices[0]
        sel1 = sel2 = 0
        for p in prices[1:]:
            buy1, sel1, buy2, sel2 = max(buy1, 0-p), max(sel1, buy1+p), max(buy2, sel1-p), max(sel2, buy2+p)
        return sel2

    def maxProfit4(self, prices):
        b1 = b2 = float('-inf')
        s1 = s2 = 0
        for p in prices:
            b1, s1, b2, s2 = max(b1, 0-p), max(s1, b1+p), max(b2, s1-p), max(s2, b2+p)
        return s2
        
sol = Solution()
prices = [7,6,4,3,1]
prices = [1,2,3,4,5]
prices = [3,3,5,0,0,3,1,4]
print(sol.maxProfit2(prices))
print(sol.maxProfit3(prices))
