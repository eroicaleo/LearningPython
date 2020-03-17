#!/usr/bin/env python

# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# 
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].

class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, hi, sign = 0, 1, 1
        while lo < len(nums)-1:
            print(f'lo = {lo}, hi = {hi}')
            print(f'nums = {nums}')
            while  hi < len(nums) and nums[hi] == nums[lo]:
                hi += 1
            if hi < len(nums):
                nums[lo+1], nums[hi] = nums[hi], nums[lo+1]
            if (sign > 0 and nums[lo] > nums[lo+1]) or (sign < 0 and nums[lo] < nums[lo+1]):
                nums[lo], nums[lo+1] = nums[lo+1], nums[lo]
            print(f'nums = {nums}')
            lo, sign = lo+1, -sign

sol = Solution()
nums = [1,1,1,4,5,6]
nums = [1,2,3,4,5,6]
nums = [1,3,1,2,2,2]
# [2,3,1,2,1,2]
sol.wiggleSort(nums)
print(nums)
