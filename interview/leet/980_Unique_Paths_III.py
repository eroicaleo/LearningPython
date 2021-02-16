#!/usr/bin/env python3

class Solution:
    def uniquePathsIII(self, grid):
        self.left = 0
        nr, nc = len(grid), len(grid[0])
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 0:
                    self.left += 1
                elif grid[i][j] == 1:
                    self.left += 1
                    start = [i, j]
        delta = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i, j):
            print(f'visiting {i}, {j}')
            ret = 0
            if grid[i][j] == 2:
                print(f'reaching end, grid = {grid}')
                return int(self.left == 0)
            self.left -= 1
            grid[i][j] = -1
            for dx, dy in delta:
                x, y = i+dx, j+dy
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] != -1:
                    ret += dfs(x,y)
            grid[i][j] = 0
            self.left += 1
            return ret
        return dfs(start[0], start[1])

grid = [
    [0,1],
    [2,0],
]

grid = [
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,2],
]

grid = [
    [1,0,0,0],
    [0,0,0,0],
    [0,0,2,-1],
        ]

sol = Solution()
print(sol.uniquePathsIII(grid))
