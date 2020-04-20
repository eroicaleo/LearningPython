#!/usr/bin/env python3

class Solution:
    def maxSubArray(self, nums):
        m, prev = nums[0], 0
        for n in nums:
            prev = max(n, prev+n)
            m = max(m, prev)
        return m

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))

