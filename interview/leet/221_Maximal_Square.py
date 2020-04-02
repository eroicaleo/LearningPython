#!/usr/bin/env python3

class Solution:
    def maximalSquare(self, matrix):
        nrow = len(matrix)
        ncol = 0 if nrow == 0 else len(matrix[0])
        dp_last, dp_curr = matrix[0], [0]*ncol
        m = 0
        for i in range(1,nrow):
            # print(f'i = {i}, dp_last = {dp_last}')
            dp_curr[0] = matrix[i][0]
            for j in range(1,ncol):
                dp_curr[j] = 0 if matrix[i][j] == 0 else min(dp_last[j-1], dp_last[j], dp_curr[j-1]) + matrix[i][j]
                m = max(m, dp_curr[j] )
            print(f'i = {i}, dp_curr = {dp_curr}')
            dp_last, dp_curr = dp_curr, [0]*ncol
        return m**2


matrix = [
[1,0,1,0,0],
[1,0,1,1,1],
[1,1,1,1,1],
[1,0,0,1,0],
]

matrix = [
[1,1,1,0,0],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,0],
]

matrix = [
[1,1,1,1,0],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,0],
]

sol = Solution()
print(sol.maximalSquare(matrix))
