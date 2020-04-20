#!/usr/bin/env python3

class Solution:
    def sortColors(self, nums):
        l = len(nums)
        i0, i1, i2 = 0, 0, 0
        while i2 < l:
            if nums[i2] == 0:
                if i1 > i0:
                    nums[i0], nums[i1], nums[i2] = nums[i2], nums[i0], nums[i1]
                else:
                    nums[i0], nums[i2] = nums[i2], nums[i0]
                i0, i1, i2 = i0+1, i1+1, i2+1
            elif nums[i2] == 1:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1, i2 = i1+1, i2+1
            else:
                i2 += 1
            print(f'nums = {nums}, {i0}, {i1}, {i2}')

    def sortColors_dietpepsi(self, nums):
        i = j = 0
        for k, n in enumerate(nums):
            nums[k] = 2
            if n < 2:
                nums[j], j = 1, j+1
            if n == 0:
                nums[i], i = 0, i+1

nums = [0,0,0,1,1,1,2,2,2]
nums = []
nums = [2,0,2,1,1,0]
nums = [2,2,2,1,1,1,0,0,0]
sol = Solution()
sol.sortColors_dietpepsi(nums)
print(nums)
