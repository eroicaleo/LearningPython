#!/usr/bin/env python3

class Solution:
    def searchRange(self, nums, target):
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mi = lo + (hi - lo) // 2
                h1, h2 = search(lo, mi), search(mi+1, hi)
                lb = h1[0] if h1[0] != -1 else h2[0]
                up = h2[1] if h2[1] != -1 else h1[1]
                return [lb, up]
            return [-1, -1]
        return search(0, len(nums)-1)

nums = [5,7,7,8,8,10]
nums = [5,7,7,8,8,8]
nums = [5,7,7,9,9,10]
nums = [8]
nums = [8,8,8]
nums = [8,8]
target = 8

sol = Solution()
res = sol.searchRange(nums, target)
print(res)
