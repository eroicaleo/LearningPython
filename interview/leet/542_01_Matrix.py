#!/usr/bin/env python3

from collections import deque

class Solution:
    def updateMatrix(self, matrix):
        nr = len(matrix)
        nc = len(matrix[0]) if nr else 0
        queue = deque([])
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = '$'
        d, delta = 1, [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in delta:
                    x, y = i+dx, j+dy
                    if 0 <= x < nr and 0 <= y < nc and matrix[x][y] == '$':
                        matrix[x][y] = d
                        queue.append((x, y))
            d += 1
        return matrix


matrix = [
[0,0,0],
[0,1,0],
[1,1,1],
]

matrix = [
[0,0,0],
[0,1,0],
[0,0,0],
]

sol = Solution()
for r in sol.updateMatrix(matrix):
    print(r)


