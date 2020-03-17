#!/usr/bin/env python

# The thinking process
# use 2 of 32-bit numbers
# to make 32 of 2-bit counters
# Say we encounter 3'd5 = 3'b101
# Then Counter[0] and Counter[2] increment by 1
# Say we encounter 3'd7 = 3'b111
# Then Counter[0-2] increment by 1
# i.e. in python: c1, c2 = c1 ^ n, c2 ^ (c1 & n)
# When a counter reaches 3, go back to 0
# i.e. in python: c1, c2 = c1 & ~(c1&c2), c2 & ~(c1&c2)

class Solution:
    def singleNumber(self, nums):
        c1, c2 = 0, 0
        for n in nums:
            c1, c2 = c1 ^ n, c2 ^ (c1 & n)
            c1, c2 = c1 & ~(c1&c2), c2 & ~(c1&c2)
        return c1

sol = Solution()
nums = [0,1,0,1,0,1,99]
nums = [2,2,3,2]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
nums = [2,2,5,5,1,5,1,1,0,2]
print(sol.singleNumber(nums))

