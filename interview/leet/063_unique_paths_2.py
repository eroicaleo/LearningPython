#!/usr/bin/env python

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        solutionGrid = [[0] * n for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            solutionGrid[0][0] = 1

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    solutionGrid[row][col] = 0
                    continue
                if row > 0 and obstacleGrid[row-1][col] == 0:
                    solutionGrid[row][col] += solutionGrid[row-1][col]
                if col > 0 and obstacleGrid[row][col-1] == 0:
                    solutionGrid[row][col] += solutionGrid[row][col-1]

                # print('row = %d, col = %d, solutionGrid = %d' % (row, col, solutionGrid[row][col]))
                
        return solutionGrid[m-1][n-1]

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))
