#!/usr/bin/env python

from unionfind import *

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        boardSizeI = len(board)
        if boardSizeI == 0:
            return
        boardSizeJ = len(board[0])
        UF = UnionFind(boardSizeI * boardSizeJ + 1)
        surroundingNode = boardSizeI * boardSizeJ
        for i in range(boardSizeI):
            for j in range(boardSizeJ):
                if board[i][j] == 'X':
                    continue
                index = boardSizeJ * i + j
                if i == 0 or i == (boardSizeI-1) or j == 0 or j == (boardSizeJ-1):
                    UF.union(index, surroundingNode)
                # up
                if i > 0 and board[i-1][j] == 'O':
                    UF.union(index, index-boardSizeJ)
                # down
                # left
                if j > 0 and board[i][j-1] == 'O':
                    UF.union(index, index-1)
                # right

        for i in range(boardSizeI):
            for j in range(boardSizeJ):
                index = boardSizeJ * i + j
                if board[i][j] == 'O' and (not UF.connected(index, surroundingNode)):
                    board[i][j] = 'X'

sol = Solution()
boardString = [
        [],
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
        ]
for board in boardString:
    print('#' * 80)
    boardToString(board)
    sol.solve(board)
    boardToString(board)
