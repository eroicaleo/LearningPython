#!/usr/bin/env python

class Solution:
    def longestConsecutive(self, nums) -> int:
        consecutive, self.longest = dict(), 1 if len(nums) > 0 else 0
        def union(i, j): # merge i with j
            if len(consecutive[i]) > len(consecutive[j]):
                i, j = j, i
            consecutive[j] += consecutive[i]
            self.longest = max(self.longest, len(consecutive[j]))
            for k in consecutive[i]:
                consecutive[k] = consecutive[j]
        for n in nums:
            if n in consecutive:
                continue
            consecutive[n] = [n]
            if (n-1) in consecutive:
                union(n, (n-1))
            if (n+1) in consecutive:
                union(n, (n+1))
        return self.longest

nums = [100, 4, 200, 1, 3, 2]
nums = []
nums = [0, 3, 1, 4, 5]
nums = [0,1,2,3,4,5]
nums = list(range(100000))
nums = [0]
nums = [0, 3]
nums = [1,2,0,1]
sol = Solution()
print(sol.longestConsecutive(nums))
