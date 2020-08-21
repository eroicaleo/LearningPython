#!/usr/bin/env python3

class Solution:
    def findDuplicates(self, nums):
        res = []
        for ix, n in enumerate(nums):
            if n-1 == ix:
                continue
            while (ix != n-1) and (n != nums[n-1]):
                n, nums[n-1] = num[n-1], n


nums = [4,3,2,7,8,2,3,1]
nums = [1,2,3,4,3,2,7,8]


nums = [1,2,3,4,-,2,7,8]
nums = [-,1,2,3,4,-,-,7,8]
