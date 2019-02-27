#!/usr/bin/env python

class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mi = lo + (hi-lo)//2
            if target == nums[mi]: return mi
            if nums[lo] <= nums[mi]:
                if nums[lo] <= target < nums[mi]:
                    hi = mi-1
                else:
                    lo = mi+1
            else:
                if nums[mi] < target <= nums[hi]:
                    lo = mi+1
                else:
                    hi = mi-1
        return -1

sol = Solution()
nums = []
nums = [4,5,6,7,0,1,2]
nums = [3,1]
target = 1
for target in nums:
    print(sol.search(nums, target))
