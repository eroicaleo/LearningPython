#!/usr/bin/env python

class Solution:
    def generateMatrix(self, n):
        ret = [[0]*n for i in range(n)]
        ix = 1
        row1, col1, row2, col2 = 0, n-1, n-1, 0
        while row1 < row2:
            for i in range(col2, col1):
                ret[row1][i], ix = ix, ix+1
            for i in range(row1, row2):
                ret[i][col1], ix = ix, ix+1
            for i in range(col1, col2, -1):
                ret[row2][i], ix = ix, ix+1
            for i in range(row2, row1, -1):
                ret[i][col2], ix = ix, ix+1
            row1, col1, row2, col2 = row1+1, col1-1, row2-1, col2+1
        if row1 == row2:
            ret[row1][col1] = ix
        return ret

sol = Solution()
for i in range(6):
    for row in sol.generateMatrix(i):
        print(row)
