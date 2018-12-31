#!/usr/bin/env python

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [[], nums]
        elif len(nums) == 2:
            return [[], [nums[0]], [nums[1]], nums]
        else:
            ret = self.subsets(nums[1:])
            ret1 = []
            for r in ret:
                ret1.append(nums[:1] + r)
            return ret + ret1


numsList = [
[1,2,3,4],
[1,2,3],
[1,2],
[1],
[]
]

sol = Solution()
for nums in numsList:
    print(sol.subsets(nums))

