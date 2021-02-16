#!/usr/bin/env python

from heapq import heappop, heappush

class Solution:
    def maximumMinimumPath(self, A):
        nr, nc = len(A), len(A[0])
        heap = [(-A[0][0], 0, 0)]
        delta = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = [[0]*nc for _ in range(nr)]
        seen[0][0] = 1
        while heap:
            val, x, y = heappop(heap)
            if x == nr-1 and y == nc-1:
                return -val
            for dx, dy in delta:
                nx, ny = x+dx, y+dy
                if 0<=nx<nr and 0<=ny<nc and seen[nx][ny]==0:
                    seen[nx][ny] = 1
                    heappush(heap, (max(val, -A[nx][ny]), nx, ny))
        return -1

A = [[5,4,5],[1,2,6],[7,4,6]]
A = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
A = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
sol = Solution()
print(sol.maximumMinimumPath(A))
