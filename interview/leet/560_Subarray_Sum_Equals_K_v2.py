#!/usr/bin/env python

class Solution:
    def subarraySum(self, nums, k):
        count, cur, res = {0: 1}, 0, 0
        for n in nums:
            cur += n
            res += count.get(cur-k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res

sol = Solution()
nums, k = [1], 0
nums, k = [1,1,1], 2
nums, k = [1,1,1,1], 2
nums, k = [-1,-1,1], 0 
nums, k = [0]*10, 0
print(sol.subarraySum(nums, k))
