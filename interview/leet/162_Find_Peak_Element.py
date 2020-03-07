#!/usr/bin/env python

class Solution:
    def findPeakElement(self, nums):
        l = len(nums)
        if l <= 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return l-1
        lo, hi = 0, l-1
        while lo <= hi:
            mi = lo + (hi-lo)//2
            if nums[mi-1] > nums[mi]:
                hi = mi-1
            elif nums[mi] < nums[mi+1]:
                lo = mi+1
            else:
                return mi
        return lo

nums = [1,2,1,3,5,6,4]
nums = [1,2,3,1]
nums = [1]
nums = [1,2,3]
sol = Solution()
print(sol.findPeakElement(nums))
