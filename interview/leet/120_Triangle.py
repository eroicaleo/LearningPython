#!/usr/bin/env python

class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        pathSum = [0] * len(triangle)
        for row in range(len(triangle)):
            rowLength, tmp = row+1, triangle[row][0] + pathSum[0]
            print('row = %d' % row)
            for col in range(1, rowLength):
                print('col = %d' % col)
                print('col = %d, n = %d' % (col, triangle[row][col]))
                pathSum[col-1], tmp = tmp, triangle[row][col] + min(pathSum[col-1], pathSum[min(col, rowLength-2)])
                print('pathSum[col] = %d' % pathSum[col])
            pathSum[rowLength-1] = tmp
            print(row, pathSum)
        return min(pathSum)

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

sol = Solution()
print(sol.minimumTotal(triangle))
# print(list(range(1,1)))
