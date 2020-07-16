#!/usr/bin/env python

from unionfind import *

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nr, nc = len(board), 0 if len(board) == 0 else len(board[0])
        def dfs(i, j):
            if 0 <= i < nr and 0 <= j < nc and board[i][j] == 'O':
                board[i][j] = 'P'
                for p, q in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    dfs(p, q)
        for i in range(nr):
            for j in range(nc):
                if (i == 0 or i == nr-1 or j == 0 or j == nc-1) and (board[i][j] == 'O'):
                    dfs(i, j)
        for i in range(nr):
            for j in range(nc):
                board[i][j] = 'O' if board[i][j] == 'P' else 'X'

sol = Solution()
boardString = [
        [],
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X","O","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
        ]
for board in boardString:
    print('#' * 80)
    boardToString(board)
    sol.solve(board)
    print()
    boardToString(board)
