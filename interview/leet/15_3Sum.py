#!/usr/bin/env python

class Solution:
    def threeSum(self, nums):
        nums, length, ret = sorted(nums), len(nums)-1, set()
        for i in range(length+1):
            j, k = i+1, length
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if   sum3 > 0: k -= 1
                elif sum3 < 0: j += 1
                else :
                    ret.add((nums[i], nums[j], nums[k]))
                    j, k = j+1, k-1
        return [list(e) for e in ret]

nums = [0,0,0,0]
nums = [-1, 0, 1, 2, -1, -4]
nums = [-2,0,0,2,2]
sol = Solution()
print(sol.threeSum(nums))
