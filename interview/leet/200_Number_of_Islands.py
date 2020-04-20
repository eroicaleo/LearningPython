#!/usr/bin/env python

import collections
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(search, (i-1,i+1,i,i), (j,j,j-1,j+1)))
                return 1
            return 0
        return sum(search(i, j) for i in range(len(grid)) for j in range(len(grid[0])))

    def numIslands_dfs(self, grid):
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    dfs(x,y)
                return 1
            return 0
        return sum(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))

    def numIslands_bfs(self, grid):
        queue, count = collections.deque(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count, grid[i][j] = count+1, '0'
                    queue.append((i, j))
                    while queue:
                        m, n = queue.popleft()
                        for x, y in [(m+1,n), (m-1,n), (m,n+1), (m,n-1)]:
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                                grid[x][y] = '0'
                                queue.append((x, y))
                    print(f'{i}, {j}, grid = {grid}')
        return count

grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
grid = [[]]
grid = []
grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
sol = Solution()
print(sol.numIslands_bfs(grid))
