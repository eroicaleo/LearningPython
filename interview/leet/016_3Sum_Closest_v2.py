#!/usr/bin/env python

# After sort it O(nlogn)
# For every iteration, fix the first number.
# Then the problem reduces to find 2 numbers whose sum is closest to a new target
# Then it's same as given a 2-D array, columns rows are all sorted, check if k is inside
# For example:
#   1, 2, 3, 4
# 1    3  4  5
# 2       5  6
# 3          7
# 4

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        end = len(nums)-1
        threeSum = sum(nums[0:3])
        for start in range(end-1):
            i, j = start+1, end
            while (i < j):
                currSum = nums[start] + nums[i] + nums[j]
                print(start, i, j)
                print(currSum)
                if currSum > target:
                    j -= 1
                elif currSum < target:
                    i += 1
                else:
                    return target
                if abs(currSum-target) < abs(threeSum-target):
                    threeSum = currSum
        return threeSum

nums = [0, 0, 0]
nums = [-1, 2, 1, -4]
target = 1

sol = Solution()
print(sol.threeSumClosest(nums, 1))
