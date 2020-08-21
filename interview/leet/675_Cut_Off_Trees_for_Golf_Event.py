#!/usr/bin/env python3

from collections import deque
from heapq import heapify, heappop

class Solution:
    def cutOffTree(self, forest):
        d, delta = 0, [(1,0),(-1,0),(0,1),(0,-1)]
        nr, nc = len(forest), len(forest[0])
        print(f'nc = {nc}, nr = {nr}')
        def shortest(src, dst):
            if src == dst:
                return 0
            queue, visited, d = deque([src]), set(src), 1
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for dx, dy in delta:
                        x, y = i+dx, j+dy
                        if (x, y) == dst:
                            return d
                        if 0<=x<nr and 0<=y<nc and (not (x,y) in visited) and (forest[x][y] > 0):
                            queue.append((x,y))
                            visited.add((x,y))
                d += 1
            return -1
        heap = [(forest[i][j], (i, j)) for i in range(nr) for j in range(nc) if forest[i][j]]
        heapify(heap)
        src = (0,0)
        while heap:
            _, dst = heappop(heap)
            d_temp = shortest(src, dst)
            if d_temp < 0:
                return d_temp
            else:
                d += d_temp
            print(f'dst = {dst}, d = {d_temp}')
            src = dst
        return d
            
forest = [
[2,3,4],
[0,0,5],
[8,7,6],
]

forest = [
[1,2,3],
[0,0,4],
[7,6,5],
]

forest = [
[1,2,3],
[0,0,0],
[7,6,5],
]

forest = [
[2,4,6],
[0,0,8],
[3,5,7],
]

forest = [[0,0,0,3528,2256,9394,3153],[8740,1758,6319,3400,4502,7475,6812],[0,0,3079,6312,0,0,0],[6828,0,0,0,0,0,8145],[6964,4631,0,0,0,4811,0],[0,0,0,0,9734,4696,4246],[3413,8887,0,4766,0,0,0],[7739,0,0,2920,0,5321,2250],[3032,0,3015,0,3269,8582,0]]

sol = Solution()
print(sol.cutOffTree(forest))
