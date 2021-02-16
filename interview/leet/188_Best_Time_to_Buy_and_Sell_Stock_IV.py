#!/usr/bin/env python3

class Solution:
    def maxProfit(self, k, prices):
        l = len(prices)
        if l == 0:
            return 0
        dpb, dps = [0]*l, [0]*l
        dpb[0], dps[0] = -prices[0], 0
        for d in range(k):
            for i in range(1, l):
                dpb[i] = max(dpb[i-1], dps[i-1]-prices[i])
            # print(f'dpb = {dpb}')
            for i in range(1, l):
                dps[i] = max(dps[i-1], dpb[i-1]+prices[i])
            # print(f'dps = {dps}')
        return dps[-1]

k = 2
prices = [3,2,6,5,0,3]
k = 2
prices = [2,4,1]
k = 2
prices = [3,3,5,0,0,3,1,4]
k = 2
prices = [7,6,4,3,1]

sol = Solution()
print(sol.maxProfit(k, prices))

