#!/usr/bin/env python

# The thinking process is like the following:
# 1. remove O(n) space limit, then we can use a hash table to solve it
# 2. then the hash table is not necessary, can modify the original array

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for tmp in nums:
            while 0 < tmp <= length and tmp != nums[tmp-1]:
                print('tmp = %d, nums[tmp-1] = %d' % (tmp, nums[tmp-1]))
                nums[tmp-1], tmp = tmp, nums[tmp-1]
        for i in range(1, length+1):
            if nums[i-1] != i:
                return i
        return length+1

sol = Solution()
nums = [3,4,-1,1]
nums = [1,2,0]
nums = [7,8,9,11,12]
print(sol.firstMissingPositive(nums))

