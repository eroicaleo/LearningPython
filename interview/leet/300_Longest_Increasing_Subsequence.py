#!/usr/bin/env python3

class Solution:
    def lengthOfLIS(self, nums):
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(i, length):
                if nums[j] > nums[i]:
                    dp[j] = max(1+dp[i], dp[j])
            print(dp)
        return max(dp)

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = [1,3,6,7,9,4,10,5,6]
print(sol.lengthOfLIS(nums))
