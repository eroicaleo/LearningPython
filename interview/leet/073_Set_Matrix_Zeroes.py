#!/usr/bin/env python3

class Solution:
    def setZeroes(self, matrix):
        nrow, ncol = len(matrix), len(matrix[0])
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'X'
                    for k in range(ncol):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'X'
                    for k in range(nrow):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'X'
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0

        for i in range(nrow):
            print(matrix[i])

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
sol.setZeroes(matrix)
