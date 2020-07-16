#!/usr/bin/env python

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        i = j = k = 0
        ret, l = [], len(nums)
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, l-1
            while j < k < l:
                s = nums[i]+nums[j]+nums[k]
                if s <= 0:
                    if s == 0:
                        ret.append([nums[i], nums[j], nums[k]])
                    while j+1 < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif s > 0:
                    while k-1 > j and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
        return ret

nums = [-2,0,0,2,2]
nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0,0,0]
sol = Solution()
print(sol.threeSum(nums))
