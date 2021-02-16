#!/usr/bin/env python

class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)
        l = len(nums)
        for i, n in enumerate(nums):
            nums[i] = 0
            while 0 <= n < l and n != nums[n]:
                nums[n], n = n, nums[n]
        for i, n in enumerate(nums):
            if i > 0 and n == 0:
                return i
        return l

    def firstMissingPositive_2(self, nums):
        nums.append(0)
        l = len(nums)
        if not 1 in nums:
            return 1
        for i, n in enumerate(nums):
            if not 0 < n < l:
                nums[i] = 1
        for i, n in enumerate(nums):
            a = abs(n)
            nums[a] = -abs(nums[a])
        for i, n in enumerate(nums):
            if i > 0 and n > 0:
                return i
        return l


sol = Solution()
nums_list = [
    [1,2],
    [1],
    [],
    [1,2,0],
    [3,4,-1,1],
    [7,8,9,11,12],
]
for nums in nums_list:
    print(nums)
    print(sol.firstMissingPositive_2(nums), nums)

