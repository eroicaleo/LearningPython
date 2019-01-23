#!/usr/bin/env python

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0:
            return False
        marked = [[0]*len(row) for row in board]
        self.row, self.col = len(board), len(board[0])
        for r in range(self.row):
            for c in range(self.col):
                ret = self.search(r, c, word, board, marked)
                if ret: return True
        return False

    def search(self, r, c, word, board, marked):
        # print('r = %d, c = %d, word = %s, marked = %s' % (r, c, word, marked))
        if word == '':
            return True
        if board[r][c] != word[0]:
            return False
        elif len(word) == 1:
            return True
        ret, marked[r][c] = False, 1
        if r > 0 and (not marked[r-1][c]): ret = ret or self.search(r-1, c, word[1:], board, marked) # top
        if c > 0 and (not marked[r][c-1]): ret = ret or self.search(r, c-1, word[1:], board, marked) # left
        if r < self.row - 1 and (not marked[r+1][c]): ret = ret or self.search(r+1, c, word[1:], board, marked) # bot
        if c < self.col - 1 and (not marked[r][c+1]): ret = ret or self.search(r, c+1, word[1:], board, marked) # right
        marked[r][c] = 0
        return ret

board = []
board = [[]]
board = [[], []]
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "SEE"
word = "ABCB"
word = "ABCCED"
board = [['a']]
word = 'a'
sol = Solution()
print(sol.exist(board, word))
