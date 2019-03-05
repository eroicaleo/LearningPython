#!/usr/bin/env python

class Solution:
    def majorityElement(self, nums: list) -> int:
        from collections import defaultdict
        numCount, length = defaultdict(int), len(nums)
        for n in nums:
            numCount[n] += 1
            if numCount[n] > length/2:
                return n

sol = Solution()
nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))
