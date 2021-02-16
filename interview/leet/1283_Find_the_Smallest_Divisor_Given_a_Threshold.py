#!/usr/bin/env python3

from math import ceil

class Solution:
    def smallestDivisor(self, nums, threshold):
        lo, hi = ceil(sum(nums)/threshold), max(nums)
        while lo < hi:
            mi = (lo+hi)//2
            t = sum([ceil(n/mi) for n in nums])
            if t > threshold:
                lo = mi+1
            elif t <= threshold:
                hi = mi
        return lo

info_list = [
    ([1,2,5,9], 6),
    ([2,3,5,7,11], 11),
    ([19], 5),
    ([962551,933661,905225,923035,990560], 10)
]

sol = Solution()
for nums, threshold in info_list:
    print(sol.smallestDivisor(nums, threshold))

