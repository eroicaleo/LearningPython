#!/usr/bin/env python

import copy

class Solution:
    def solveNQueens(self, n: int):
        def search(board, n, i):
            print('n = %d, i = %d\n   board = %s' % (n, i, board))
            if i == n:
                return [[''.join(row) for row in board]]
            ret = []
            for j, c in enumerate(board[i]):
                if c == ' ':
                    newboard = copy.deepcopy(board)
                    for k in range(0, n):
                        newboard[i][k] = '.'
                    newboard[i][j] = 'Q'
                    for k in range(i+1, n):
                        newboard[k][j] = 'X'
                    print('newboard = %s' % newboard)
                    k = 1
                    while (i+k < n) and (j-k >= 0):
                        newboard[i+k][j-k], k = 'X', k+1
                    k = 1
                    while (i+k < n) and (j+k < n):
                        newboard[i+k][j+k], k = 'X', k+1
                    ret += search(newboard, n, i+1)
            return ret
        return search([[' ']*n for i in range(n)], n, 0)

sol = Solution()
print(sol.solveNQueens(5))
