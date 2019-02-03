#!/usr/bin/env python

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        summation = sum(nums)
        if summation % k != 0:
            return False
        target = summation // k
        print(target)
        bucket, nums = [target] * k, sorted(nums, reverse=True) # build the bucket
        def recursive(n):
            print('n = %d' % n)
            if n >= len(nums): return True
            for i in range(k):
                bucket[i] -= nums[n]
                if bucket[i] >= 0 and recursive(n+1):
                    return True
                else:
                    bucket[i] += nums[n]
                if bucket[i] == target: # no need to try the remaining empty bucket, speed up a lot
                    break
            return False
        return recursive(0)

nums, k = [10,10,10,7,7,7,7,7,7,6,6,6], 3
nums, k = [1,1,1,1,1,1,1,1,1,1], 5
nums, k = [4, 3, 2, 3, 5, 2, 1], 4
nums, k = [4,5,3,2,5,5,5,1,5,5,5,5,5,5,5,5], 14
sol = Solution()
print(sol.canPartitionKSubsets(nums, k))
