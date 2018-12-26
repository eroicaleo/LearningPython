#!/usr/bin/env python

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1
        maxDist = 0
        for i, n in enumerate(nums):
            d = n + i
            print(i, n, maxDist)
            if d > maxDist:
                maxDist = d
            if d >= target:
                return True
            if i >= maxDist:
                return False
            print(i, n, maxDist, target)

sol = Solution()
numsList = [
[2,3,1,1,4],
[3,2,1,0,4],
[0],
]
for nums in numsList:
    print(sol.canJump(nums))
