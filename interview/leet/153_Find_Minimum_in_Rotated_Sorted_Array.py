#!/usr/bin/env python3

class Solution:
    def findMin(self, nums) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi] > nums[hi]: lo = mi+1
            else:                   hi = mi
        return nums[lo]

sol = Solution()
nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
print(sol.findMin(nums))
