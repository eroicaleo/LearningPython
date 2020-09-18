#!/usr/bin/env python

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if t < 0:
            return False
        n, d, w = len(nums), {}, t+1
        for i, n in enumerate(nums):
            m = n // w
            if m in d:
                return True
            if (m-1) in d and abs(n-d[m-1]) < w:
                return True
            if (m+1) in d and abs(n-d[m+1]) < w:
                return True
            d[m] = n
            if i >= k:
                del d[nums[i-k]//w]
        return False

sol = Solution()
for nums, k, t in [
[[1,2,3,1], 3, 0],
[[1,0,1,1], 1, 2],
[[1,5,9,1,5,9], 2, 3],
[[0], 0, 0],
[[-1, -1], 1, -1],
[[1, 2], 0, 1],
]:
    print(nums, k, t, sol.containsNearbyAlmostDuplicate(nums, k, t))
