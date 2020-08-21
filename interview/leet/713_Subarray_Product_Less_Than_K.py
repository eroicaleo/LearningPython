#!/usr/bin/env python3

class Solution():
    def numSubarrayProductLessThanK(self, nums, k):
        lo, prod = 0, 1
        ret = 0
        for hi, n in enumerate(nums):
            prod *= n
            while lo <= hi and prod >= k:
                prod //= nums[lo]
                lo += 1
            ret += (hi-lo+1)
        return ret

nums = [10,5,2,6]
k = 100
sol = Solution()
print(sol.numSubarrayProductLessThanK(nums, k))
