#!/usr/bin/env python3

class Solution:
    def sortedSquares(self, nums):
        l = len(nums)
        ret, j, k = [0]*l, 0, 0
        for i in range(l):
            nums[i] *= nums[i]
            if i>0 and nums[i]>nums[i-1]:
                i, j = i-1, i
                break
        if i >= j:
            return nums[::-1]
        while i >= 0 or j < l:
            if j == l:
                ret[k], i = nums[i], i-1
            elif i < 0:
                ret[k], j = nums[j], j+1
                if j < l:
                    nums[j] *= nums[j]
            elif nums[i] <= nums[j]:
                ret[k], i = nums[i], i-1
            elif nums[i] >  nums[j]:
                ret[k], j = nums[j], j+1
                if j < l:
                    nums[j] *= nums[j]
            k += 1
        return ret

    def sortedSquares_wangzi(self, nums):
        l = len(nums)
        ret = [0]*l
        i, j = 0, l-1
        for k in range(l-1,-1,-1):
            if abs(nums[i]) > abs(nums[j]):
                ret[k], i = nums[i]**2, i+1
            else:
                ret[k], j = nums[j]**2, j-1
        return ret

nums = [-2, -1, 0]
nums = [-7,-3,2,3,11]
nums = [-4,-1,0,3,10]
sol = Solution()
# print(sol.sortedSquares(nums))
print(sol.sortedSquares_wangzi(nums))
