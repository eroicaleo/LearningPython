#!/usr/bin/env python

import functools

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # numsString = [str(n) for n in nums]
        # def compare(ns1, ns2):
        #     return 1 if ns2+ns1 > ns1+ns2 else -1
        return ''.join(sorted([str(n) for n in nums], key=functools.cmp_to_key(lambda ns1, ns2: 1 if ns2+ns1 > ns1+ns2 else -1))).lstrip('0') or '0'

sol = Solution()
nums = [10,2]
nums = [10, 20]
nums = [0, 0]
nums = [30,3,34,5,9]
print(sol.largestNumber(nums))
