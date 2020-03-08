#!/usr/bin/env python

import math

class Solution:
    def wiggleMaxLength(self, nums):
        maxlen = [0, 0]
        for i, sign in enumerate([1, -1]):
            prev = -sign * math.inf
            for n in nums:
                if (n - prev) * sign > 0:
                    sign, prev = -sign, n
                    maxlen[i] += 1
                    print(f'n={n}, sign={sign}, prev={prev}')
        return max(maxlen)

sol = Solution()
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,7,4,9,2,5]
nums = []
nums = [1,2,3,4,5,6,7,8,9]
print(sol.wiggleMaxLength(nums))
