#!/usr/bin/env python

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi, length, jump, nexthi = 0, 0, len(nums)-1, 0, 0
        while hi < length:
            for i in range(lo, hi+1):
                nexthi = max(i+nums[i], nexthi)
            lo, hi, jump = hi+1, nexthi, jump+1
        return jump

sol = Solution()
nums = [2,3,1,1,4]
nums = [0]
nums = [4,1,1,3,1,1,1]
nums = [2,0,2,0,1]
print(sol.jump(nums))
#           print('lo = %d, hi = %d, jump = %d' % (lo, hi, jump))
