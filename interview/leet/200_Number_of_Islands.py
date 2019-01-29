#!/usr/bin/env python

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

grid = []
grid = [[]]
grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
sol = Solution()
print(sol.numIslands(grid))
