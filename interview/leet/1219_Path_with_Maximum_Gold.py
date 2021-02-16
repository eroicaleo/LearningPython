#!/usr/bin/env python3

class Solution:
    def getMaximumGold(self, grid):
        nr, nc = len(grid), len(grid[0])
        delta = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i, j):
            gold, grid[i][j] = grid[i][j], 0
            max_gold = 0
            for dx, dy in delta:
                x, y = i+dx, j+dy
                if 0<=x<nr and 0<=y<nc and grid[x][y]>0:
                    max_gold = max(max_gold, dfs(x,y))
            grid[i][j] = gold
            return max_gold+gold
        return max(dfs(i,j) for i in range(nr) for j in range(nc) if grid[i][j] > 0)
                    


grid = [
[0,6,0],
[5,8,7],
[0,9,0],
]

grid = [
[1,0,7],
[2,0,6],
[3,4,5],
[0,3,0],
[9,0,20]
]

sol = Solution()
print(sol.getMaximumGold(grid))
