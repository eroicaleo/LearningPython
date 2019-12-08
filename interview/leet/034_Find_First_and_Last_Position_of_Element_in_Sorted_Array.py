#!/usr/bin/env python3

class Solution:
    def searchRange(self, nums, target):
        lb, ub = -1, -1
        # up bound
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            # print('lo = {}, hi = {}, mi = {}'.format(lo, hi, mi))
            n = nums[mi]
            if   n < target: lo = mi + 1
            elif n > target: hi = mi - 1
            else:
                if nums[hi] == n:
                    ub = hi
                    break
                else:
                    hi = hi - 1
                    lo = mi
        # low bound
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            # print('lo = {}, hi = {}, mi = {}'.format(lo, hi, mi))
            n = nums[mi]
            if   n < target: lo = mi + 1
            elif n > target: hi = mi - 1
            else:
                if nums[lo] == n:
                    lb = lo
                    break
                else:
                    lo = lo + 1
                    hi = mi
 
        return [lb, ub]

nums = [5,7,7,8,8,10]
nums = [5,7,7,8,8,8]
nums = [5,7,7,9,9,10]
nums = [8]
nums = [8,8,8]
nums = [8,8]
target = 8

sol = Solution()
res = sol.searchRange(nums, target)
print(res)
