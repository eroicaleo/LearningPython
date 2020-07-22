#!/usr/bin/env python

class Solution:
    def exist(self, board, word):
        nr, nc = len(board), 0 if len(board) == 0 else len(board[0])
        def dfs(i, j, w):
            if (len(w) == 0) or (w[0] == board[i][j] and len(w) == 1):
                return True
            if w[0] != board[i][j]:
                return False
            board[i][j] = '$'
            if any(dfs(x, y, w[1:]) for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)] if 0 <= x < nr and 0 <= y < nc and board[x][y] != '$'):
                board[i][j] = w[0]
                return True
            board[i][j] = w[0]
            return False
        return any(dfs(i, j, word) for i in range(nr) for j in range(nc))

board = []
board = [[]]
board = [[], []]
board = [['a']]
word = 'a'
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
word = "ABCB"
word = "SEE"

sol = Solution()
print(sol.exist(board, word))
