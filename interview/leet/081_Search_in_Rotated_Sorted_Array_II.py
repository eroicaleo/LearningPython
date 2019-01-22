#!/usr/bin/env python

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        if length == 0:
            return False
        lo, hi = 0, length-1
        while lo <= hi:
            while (lo <= hi) and (nums[lo] == nums[hi]):
                if nums[lo] == target:
                    return True
                lo, hi = lo+1, hi-1
            if lo > hi:
                return False
            mi = (lo+hi) // 2
            if target == nums[mi]:
                return True
            if nums[lo] < nums[hi]:
                if nums[mi] > target:
                    go_left = 1
                elif nums[mi] < target:
                    go_left = 0
            elif nums[lo] > nums[hi]:
                if nums[mi] > nums[lo]: # nums[mi] > nums[lo] > nums[hi]
                    if target > nums[mi]:
                        go_left = 0
                    elif target < nums[mi]:
                        if target >= nums[lo]:
                            go_left = 1
                        elif target < nums[lo]:
                            go_left = 0
                elif nums[mi] < nums[hi]: # nums[lo] > nums[hi] > nums[mi]
                    if target < nums[mi]:
                        go_left = 1
                    elif target > nums[mi]:
                        if target <= nums[hi]:
                            go_left = 0
                        elif target > nums[hi]:
                            go_left = 1
                elif nums[mi] == nums[hi]: # nums[lo] > nums[hi] = nums[mi]
                    go_left = 1
                elif nums[mi] == nums[lo]: # nums[lo] = nums[mi] > nums[hi]
                    go_left = 0

            if go_left == 1:
                hi = mi - 1
            else:
                lo = mi + 1

        return False

sol = Solution()
nums = [0,0,0,3,0,0,0]
nums = [2,5,6,0,0,1,2]
nums = [0,1,2,2,5,6,0]
nums = [0]
nums = []
nums = [2,2,2,2,2,2]
nums, target = [0,0,1,1,2,0], 2
nums, target = [2,2,2,0,2,2], 0
nums, target = [1], 0
nums, target = [2,5,6,0,0,1,2], 3
print(sol.search(nums, target))
