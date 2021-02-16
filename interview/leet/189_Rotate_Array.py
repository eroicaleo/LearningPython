#!/usr/bin/env python3

import math

class Solution:
    def rotate(self, nums, k): 
        l = len(nums)
        d = math.gcd(k, l)
        for i in range(d):
            p, q, prev = i, (i+k)%l, nums[i]
            while q != i:
                tmp = nums[q]
                nums[q] = prev
                p, q, prev = q, (q+k)%l, tmp
            nums[i] = prev
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
nums = [-1,-100,3,99]
k = 2
sol = Solution()
print(sol.rotate(nums, k))
