#!/usr/bin/env python

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps, far, length = [0] * len(nums), 0, len(nums)
        for i, c in enumerate(nums):
            far, prevfar = min(length-1, max(i+c, far)), far
            for j in range(prevfar+1, far+1):
                jumps[j] = jumps[i]+1
            if far >= length-1:
                return jumps[-1]

sol = Solution()
nums = [2,3,1,1,4]
nums = [0]
nums = [4,1,1,3,1,1,1]
print(sol.jump(nums))
# print('i = %d, c = %d, jumps = %s, far = %d, prevfar = %d' % (i, c, jumps, far, prevfar))
