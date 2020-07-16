#!/usr/bin/env python

# -2 -3   3
# -5 -10  1
# 10  30 -5

import math

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        nr, nc = len(dungeon), len(dungeon[0])
        visited = [[-1]*nc for _ in range(nr)]
        def dfs(i, j):
            print(f'visiting {i}, {j}')
            if visited[i][j] >= 0:
                return visited[i][j]
            if i == nr-1 and j == nc-1:
                return max(0, -dungeon[i][j])
            if i == nr-1:
                d = dfs(i, j+1)
            elif j == nc-1:
                d = dfs(i+1, j)
            else:
                d = min(dfs(i, j+1), dfs(i+1, j))
            visited[i][j] = max(0, d-dungeon[i][j])
            return visited[i][j]
        return 1+dfs(0, 0)

dungeon = [[100]]
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
for row in dungeon:
    print(row)
sol = Solution()
print(sol.calculateMinimumHP(dungeon))
