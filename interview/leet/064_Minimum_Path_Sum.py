#!/usr/bin/env python

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        pathSum = [[0] * n for i in range(m)]
        pathSum[0][0] = grid[0][0]
        for j in range(1, n):
            pathSum[0][j] = pathSum[0][j-1] + grid[0][j]
        for i in range(1, m):
            pathSum[i][0] = pathSum[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                    pathSum[i][j] = min(pathSum[i-1][j], pathSum[i][j-1]) + grid[i][j]
        return pathSum[m-1][n-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
grid = [[1, 2, 3]]
grid = [[]]
grid = [
        [2],
        [3],
        [4]
        ]

sol = Solution()
print(sol.minPathSum(grid))


