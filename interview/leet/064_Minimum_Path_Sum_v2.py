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
        pathSum = [grid[0][0]] * n
        for j in range(1, n):
            pathSum[j] = pathSum[j-1] + grid[0][j]
        for i in range(1, m):
            pathSum[0] = pathSum[0] + grid[i][0]
            for j in range(1, n):
                    pathSum[j] = min(pathSum[j], pathSum[j-1]) + grid[i][j]
        return pathSum[n-1]

grid = [[1, 2, 3]]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
grid = [
        [2],
        [3],
        [4]
        ]
grid = [[]]
grid = []

sol = Solution()
print(sol.minPathSum(grid))


