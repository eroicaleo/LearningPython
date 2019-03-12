#!/usr/bin/env python

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        bucket = {}
        if k <= 0 or t < 0: return False
        for i, v in enumerate(nums):
            bucketNum, offset = v//(t+1), min(t, 1)
            for p in range(bucketNum-offset, bucketNum+offset+1):
                if (p in bucket) and abs(bucket[p]-v) <= t:
                    return True

            if bucket and (i >= k):
                print('I need to delete:', nums[i-k])
                del bucket[nums[i-k]//(t+1)]
            bucket[bucketNum] = v
        return False

sol = Solution()
nums, k, t = [1,2,3,1], 3, 0
nums, k, t = [1,0,1,1], 1, 2
nums, k, t = [1,5,9,1,5,9], 2, 3
nums, k, t = [0], 0, 0
nums, k, t = [-1, -1], 1, -1
nums, k, t = [1, 2], 0, 1
print(sol.containsNearbyAlmostDuplicate(nums, k, t))
