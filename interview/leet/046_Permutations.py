#!/usr/bin/env python

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) == 0:
            ret = []
        if len(nums) == 1:
            ret = [nums]
        elif len(nums) == 2:
            ret = [nums, [nums[1], nums[0]]]
        else:
            for i, n in enumerate(nums):
                m = nums[0]
                nums[0], nums[i] = n, m
                ret1 = self.permute(nums[1:])
                for l in ret1:
                    ret.append([n]+l)
                nums[0], nums[i] = m, n
        return ret


numsList = [
[1,2,3,4],
[1,2,3],
[1,2],
[1],
[]
]

sol = Solution()
for nums in numsList:
    print(sol.permute(nums))
