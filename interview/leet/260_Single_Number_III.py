#!/usr/bin/env python

# The thinking process, like the single number I
# If we xor all the numbers together, we get a number that is a ^ b
# a, b appears only once.

import operator, functools

class Solution:
    def singleNumber(self, nums):
        a = functools.reduce(operator.xor, nums)
        b = functools.reduce(operator.xor, filter(lambda n: n & a & -a, nums))
        return [a ^ b, b]

sol = Solution()
nums = [1,2,1,3,2,5]
print(sol.singleNumber(nums))
