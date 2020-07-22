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

    def topKFrequent_bucket(self, nums, k):
        from collections import Counter
        c, bucket, res = Counter(nums), [[] for _ in nums] + [[]], []
        for i in c:
            bucket[c[i]].append(i)
        for b in bucket[::-1]:
            res += b
            if len(res) == k:
                return res

sol = Solution()
nums, k = [1], 1
nums, k = [1,1,1,2,2,3], 2
print(sol.topKFrequent_bucket(nums, k))
