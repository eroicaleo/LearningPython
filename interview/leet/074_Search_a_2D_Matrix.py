#!/usr/bin/env python3

class Solution:
    def searchMatrix(self, matrix, target):
        nrow, ncol = len(matrix), 0 if len(matrix) == 0 else len(matrix[0])
        lo, hi = 0, nrow*ncol-1
        while lo <= hi:
            mi = lo+(hi-lo)//2
            x, y = mi//ncol, mi%ncol
            if target > matrix[x][y]:
                lo = mi+1
            elif target < matrix[x][y]:
                hi = mi-1
            else:
                return True
        return False


sol = Solution()
matrix = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
print(sol.searchMatrix(matrix, 1))
print(sol.searchMatrix(matrix, 13))
print(sol.searchMatrix(matrix, 50))
print(sol.searchMatrix(matrix, 1000))
print(sol.searchMatrix(matrix, 0))
print(sol.searchMatrix([], 0))
print(sol.searchMatrix([[]], 0))
