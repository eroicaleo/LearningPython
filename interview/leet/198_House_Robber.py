#!/usr/bin/env python3

class Solution(object):
    def rob(self, nums):
        l = len(nums)
        res, prev1, prev2 = [0]*l, 0, 0
        for i in range(l):
            res[i] = max(prev1, prev2+nums[i])
            prev2, prev1 = prev1, res[i]
        return prev1

num_list = [
[],
[1],
[1,2],
[1,2,3,1],
[2,7,9,3,1],
]
sol = Solution()
for nums in num_list:
    print(nums, sol.rob(nums))
