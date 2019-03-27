#!/usr/bin/env python

class Solution:
    def productExceptSelf(self, nums):
        length, prod = len(nums), 1
        output = [1] * length
        for i in range(1, length):
            output[i] = nums[i-1] * output[i-1]
        for i in range(1, length):
            prod = prod * nums[length-i]
            output[length-i-1] *= prod
        return output

sol = Solution()
nums = list(range(1,5))
nums = list(range(1,2))
nums = list(range(1,3))
nums = []
print(sol.productExceptSelf(nums))
