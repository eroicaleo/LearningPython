#!/usr/bin/env python

# proposition 1: drop, i.e. nums[i%N] < nums[(i+1)%N] only happens once
# proof: because it's sorted
# proposition 2: if nums[lo] < nums[hi], then [lo, hi] is nondecreasing
# proof: immediately from proposition 1

# At this point, either nums[lo] <= nums[mi] or nums[mi] <= nums[hi]
# If it's not true, then nums[lo] > nums[mi] > nums[hi], it's impossible for a rotated sorted array
# Now if nums[lo] <= nums[mi], then [lo, mi] is nondecreasing
# because if nums[lo] < nums[mi], then see proposition 1
# if nums[lo] == nums[mi], then drop happens either between [mi, hi] or [hi, lo]
# Then we just need to check if target is in the range of [nums[lo], nums[hi]]
# Now if nums[mi] <= nums[hi], then [mi, hi] is nondecreasing, the proof is same as before

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mi = (lo+hi) // 2
            if nums[mi] == target:
                return True
            if (nums[mi] == nums[lo]) and (nums[mi] == nums[hi]):
                lo, hi = lo+1, hi-1
            # see explain at the beginning
            elif ( ((nums[lo] <= nums[mi]) and ((nums[lo] <= target) and (target <= nums[mi]))) or
                   ((nums[mi] <= nums[hi]) and ((nums[hi] <  target) or  (target <  nums[mi]))) ):
                hi = mi - 1
            else:
                lo = mi + 1
        return False

sol = Solution()
nums = [0,0,0,3,0,0,0]
nums = [2,5,6,0,0,1,2]
nums = [0,1,2,2,5,6,0]
nums = [0]
nums = [2,2,2,2,2,2]
nums, target = [0,0,1,1,2,0], 2
nums, target = [2,5,6,0,0,1,2], 3
nums, target = [], 3
nums, target = [1], 0
nums, target = [2,2,2,0,2,2], 0
print(sol.search(nums, target))
