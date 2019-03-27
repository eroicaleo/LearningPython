#!/usr/bin/env python

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First iteration
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # print(i)
        if i <= 0:
            nums.sort()
            return nums
        i -= 1
        # Second iteration: 
        while nums[j] <= nums[i]:
            j -= 1
        # print(j)
        # Swap
        nums[i], nums[j], lo, hi = nums[j], nums[i], i+1, len(nums)-1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo+1, hi-1
        return nums

nums = [3,2,1]
nums = [1,2,3]
nums = [1,1,5]
nums = [0]
nums = []
sol = Solution()
for i in range(3):
    print(sol.nextPermutation(nums))
