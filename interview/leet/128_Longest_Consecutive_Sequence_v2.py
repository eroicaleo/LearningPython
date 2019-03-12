#!/usr/bin/env python

# See the explanation in
# The key is, for d[n], if it's boundary
# it stores the longest consecutive numbers.
# whenever a new n inserted, the boundary which d[n] is in will be updated

class Solution:
    def longestConsecutive(self, nums) -> int:
        from collections import defaultdict
        d, r = defaultdict(int), 0
        for n in nums:
            if d[n] == 0:
                left, right  = d[n-1], d[n+1]
                d[n] = d[n-left] = d[n+right] = 1 + left + right
                r = max(r, d[n])
        return r

numsList = [
[1,2,0,1],
[100, 4, 200, 1, 3, 2],
[],
[0, 3, 1, 4, 5],
[0,1,2,3,4,5],
list(range(100000)),
[0],
[0, 3],
]

sol = Solution()
for nums in numsList:
    print(sol.longestConsecutive(nums))
