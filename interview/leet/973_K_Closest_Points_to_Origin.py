#!/usr/bin/env python3

from heapq import heappush, heappop

class Solution:
    def kClosest(self, points, K):
        heap = []
        for p in points:
            heappush(heap, [-(p[0]**2+p[1]**2), p])
            if len(heap) > K:
                heappop(heap)
        return [h[1] for h in heap]

sol = Solution()
points = [[3,3],[5,-1],[-2,4]]
K = 2
points = [[1,3],[-2,2]]
K = 1
print(sol.kClosest(points, K))
