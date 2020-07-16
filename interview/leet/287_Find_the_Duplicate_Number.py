#!/usr/bin/env python3

class Solution:
    def findDuplicate(self, nums):
        n = len(nums)-1
        lo, hi = 1, n
        while lo < hi:
            mi = lo+(hi-lo)//2
            s = len(list(filter(lambda i: lo <= i <= mi, nums)))
            print(f'lo = {lo}, hi = {hi}, mi = {mi}, s = {s}')
            if s > mi-lo+1:
                hi = mi
            else:
                lo = mi+1
        return lo

# The thinking process
# Assume n[0] = i0, n[i0] = i1
# Assuem i0, i1, ..., ik are all different, and i_{k+1} = i_j for some j in [0, ..., k]
# Then n[i_{j-1}] = n[i_{k}] is the results

# Assume the length of loop is K, the length outside of the loop is m
# When slow enters the loop for the first time, fast is at m%K
# The distance between slow and fast is K-m%K
# it takes K-m%K steps for fast to catch slow
# when slow and fast meet with each other in the loop, it's K-m%K
# Then start another pointer from "finder", the finder will meet "slow" at the entrace

    def findDuplicate_On(self, nums):
        slow = fast = finder = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]] 
            if slow == fast:
                while finder != slow:
                    finder, slow = nums[finder], nums[slow]
                return finder

sol = Solution()
nums = [3,3,3,3,3,4,5]
nums = [3,1,3,4,2]
nums = [1,3,4,2,2]
print(sol.findDuplicate_On(nums))
