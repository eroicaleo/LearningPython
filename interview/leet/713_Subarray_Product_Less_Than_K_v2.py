#!/usr/bin/env python3

# Dynamic programming
# 10 5 2 6
# dp[i] is (j, prod(nums[j:i+1])

class Solution():
    def numSubarrayProductLessThanK(self, nums, k):
        lo = ret = 0
        prod = 1
        for hi, n in enumerate(nums):
            prod *= n
            while prod >= k and lo <= hi:
                prod, lo = prod//nums[lo], lo+1
            ret += hi-lo+1
        return ret


nums = [10,5,2,6,1,1]
k = 1
nums = [10,5,2,6]
k = 100
sol = Solution()
print(sol.numSubarrayProductLessThanK(nums, k))
