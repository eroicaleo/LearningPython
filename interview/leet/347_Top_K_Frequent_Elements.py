#!/usr/bin/env python

class Solution:
    def topKFrequent(self, nums, k):
        from heapq import heapify, nlargest
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = [(d[key], key) for key in d]
        heapify(l)
        return [i for n, i in nlargest(k, l)]

sol = Solution()
nums, k = [1,1,1,2,2,3], 2
nums, k = [1], 1
print(sol.topKFrequent(nums, k))
