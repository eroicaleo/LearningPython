#!/usr/bin/env python

# The main idea:
# Use two dp table:
# dp[0, i], the max positive number including nums[i]
# dp[1, i], the min negtive  number including nums[i]

#  2  3  -5   -4   -3     500  0   2   4
#+ 2  6   0  120   12    6000  0   2   8
#- 0  0 -30   -4 -360 -180000  0   0   0

class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp, ret = [0, 0], 0
        for n in nums:
            dp[0], dp[1] = max(n, dp[0]*n, dp[1]*n), min(n, dp[0]*n, dp[1]*n)
            ret = max(ret, dp[0])
        return ret
 
sol = Solution()
nums = [2,3,-5,-4,-3,500,0,2,4]
nums = [-1,0,-2]
nums = [-1,2,3]
nums = [2,3,-1,2]
nums = [-2, 3, -1]
nums = [-2]
print(nums)
print(sol.maxProduct(nums))

