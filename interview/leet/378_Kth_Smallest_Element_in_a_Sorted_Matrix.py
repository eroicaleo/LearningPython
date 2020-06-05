#!/usr/bin/env python3

from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix, k):
        nr = len(matrix)
        heap = []
        for i in range(nr):
            heappush(heap, (matrix[i][0], i, 0))
        i = 0
        while i < k:
            n, r, c = heappop(heap)
            if c < nr-1:
                heappush(heap, (matrix[r][c+1], r, c+1))
            i += 1
        return n

sol = Solution()
matrix = [
[1,5,9],
[10,11,13],
[12,13,15],
]
k = 8
print(sol.kthSmallest(matrix, k))
