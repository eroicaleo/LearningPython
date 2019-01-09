#!/usr/bin/env python

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        end = len(nums)-1
        mindiff = abs(nums[0] + nums[1] + nums[2] - target)
        threeSum = sum(nums[0:3])
        for i in range(end-1):
            partialTarget = target - nums[i]
            print("partialTarget:", partialTarget)
            diff, twoSum = self.twoSumSortedClosest(nums, i+1, end, partialTarget)
            print(diff, twoSum)
            if diff < mindiff:
                mindiff = diff
                threeSum = twoSum + nums[i]
        return threeSum

    def twoSumSortedClosest(self, nums, begin, end, target):
        i, j = begin, end
        mindiff = abs(nums[i]+nums[j]-target)
        twoSum = sum([nums[i], nums[j]])
        while (i < j):
            diff = abs(nums[i]+nums[j]-target)
            if diff < mindiff:
                mindiff = diff
                twoSum = sum([nums[i], nums[j]])
            if nums[i]+nums[j] > target:
                j -= 1
            elif nums[i]+nums[j] < target:
                i += 1
            else:
                return mindiff, twoSum
        return mindiff, twoSum


nums = [0, 0, 0]
nums = [-1, 2, 1, -4]
target = 1

sol = Solution()
print(sol.threeSumClosest(nums, 1))
