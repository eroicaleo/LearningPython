#!/usr/bin/env python3

from heapq import heappush, heappop
import collections

class Solution:
    def trapRainWater(self, heightMap):
        heap, delta = [], [(1, 0), (-1, 0), (0, 1), (0, -1)]
        nr, nc = len(heightMap), len(heightMap[0]) if heightMap else 0
        visited, queue = [[0]*nc for _ in range(nr)], collections.deque()
        for i in range(nr):
            for j in range(nc):
                if i == 0 or i == nr-1 or j == 0 or j == nc-1:
                    heappush(heap, [heightMap[i][j], i, j])
                    visited[i][j] = True
        min_level, water = 0, 0
        print(f'heap = {heap}')
        while heap or queue:
            print(f'heap = {heap}\nqueue = {queue}')
            if queue:
                i, j = queue.popleft()
            else:
                min_level, i, j = heappop(heap)
            print(f'visited {i, j}')
            water += min_level-heightMap[i][j]
            for dx, dy in delta:
                x, y = i+dx, j+dy
                if x < 0 or x >= nr or y < 0 or y >= nc or visited[x][y]:
                    continue
                if heightMap[x][y] <= min_level:
                    queue.append([x, y])
                else:
                    heappush(heap, [heightMap[x][y], x, y])
                visited[x][y] = True
        return water
                    
sol = Solution()
heightMap = [
[1,4,4,1,3,2],
[4,2,1,4,2,4],
[2,4,4,2,3,1],
]
heightMap = [
[1,4,3,1,3,2],
[3,2,1,3,2,4],
[2,3,3,2,3,1],
]
print(sol.trapRainWater(heightMap))
