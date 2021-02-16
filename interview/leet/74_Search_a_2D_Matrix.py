#!/usr/bin/env python

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = 0 if m == 0 else len(matrix[0])
        lo, hi = 0, m-1
        while lo < hi:
            print(f'before: lo = {lo}, hi = {hi}')
            mi = (lo+hi)//2
            c = matrix[mi][n-1] 
            if c == target:
                return True
            elif c < target:
                lo = mi+1
            else:
                hi = mi
            print(f'after: lo = {lo}, hi = {hi}')
        k, lo, hi = lo, 0, n-1
        print(f'k = {k}')
        while lo <= hi:
            mi = (lo+hi)//2
            c = matrix[k][mi] 
            if c == target:
                return True
            elif c < target:
                hi = mi-1
            else:
                lo = mi+1
        return False

matrix = [
[1,3,5,7],
[10,11,16,20],
[23,30,34,60],
        ]
target = 3
target = 13
matrix = []
target = 0
sol = Solution()
print(sol.searchMatrix(matrix, target))
