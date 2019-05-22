#!/usr/bin/env python3

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [-1] * (amount+1)
        for c in coins:
            if c <= amount:
                dp[c] = 1
        print(dp)
        for i in range(amount):
            if dp[-1] > 0:
                return dp[-1]
            valid = 0
            for j in range(amount, 0, -1):
                if dp[j] > 0:
                    for c in coins:
                        if j+c <= amount and dp[j+c] == -1:
                            dp[j+c] = dp[j]+1
                            valid = 1
                    dp[j] = 0
            print(dp)
            if not valid:
                break
        return -1

coins, amount = [2], 3
coins, amount = [1,2,5], 11
coins, amount = [1], 0
coins, amount = [1], 1
sol = Solution()
print(sol.coinChange(coins, amount))
