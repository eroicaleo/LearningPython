#!/usr/bin/env python3

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i0, i1 = 2, 2
        while i1 < l:
            if nums[i1] == nums[i0-1] == nums[i0-2]:
                i1 += 1
            else:
                nums[i0] = nums[i1]
                i0, i1 = i0+1, i1+1
        print(nums)
        return min(i0, l)

sol = Solution()
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
nums = []
nums = [1]
nums = [1,1]
print(sol.sortColors(nums))
