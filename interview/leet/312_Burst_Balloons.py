#!/usr/bin/env python3

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        length = len(nums)
        dp = [[0] * length for i in range(length)]
        for i in range(1, length-1):
            for j in range(i, length-1):
                print(i, j)
                x, y = 1+j-i, j
                print(x, y)
                for k in range(x, y+1):
                    dp[x][y] = max(dp[x][y], dp[x][k-1]+dp[k+1][y]+nums[x-1]*nums[k]*nums[y+1])
                for k in range(length):
                    print(dp[k])
        return dp[1][-2]

sol = Solution()
nums = [3,1,5,8]
nums = [3]
nums = []
print(sol.maxCoins(nums))
