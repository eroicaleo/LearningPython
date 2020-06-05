#!/usr/bin/env python3

class Solution:
    def singleNonDuplicate(self, nums):
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mi = lo+(hi-lo)//2
            if (mi-lo)%2==0:
                if nums[mi] == nums[mi+1]:
                    lo = mi+2
                else:
                    hi = mi
            else:
                if nums[mi] == nums[mi+1]:
                    hi = mi-1
                else:
                    lo = mi+1
        return nums[lo]

nums = [3,3,7,7,10,11,11]
nums = [1,1,2,3,3,4,4,8,8]
nums = [1]
nums = [1,1,2]
nums = [1,2,2]
sol = Solution()
print(sol.singleNonDuplicate(nums))
