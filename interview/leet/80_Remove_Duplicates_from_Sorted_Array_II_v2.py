#!/usr/bin/env python3

class Solution:
    def removeDuplicates(self, nums):
        i, ret = 0, 0
        for j, n in enumerate(nums):
            if nums[i] == n and j-i < 2:
                ret += 1
            elif nums[i] != n:
                i = j
                ret += 1
        return ret

sol = Solution()
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
nums = []
nums = [1]
nums = [1,1]
print(sol.removeDuplicates(nums))
