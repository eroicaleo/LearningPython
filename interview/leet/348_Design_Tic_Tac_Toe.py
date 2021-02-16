#!/usr/bin/env python

class TicTacToe:

    def __init__(self, n):
        self.board = [[0]*n for _ in range(n)]
        self.rows = [0]*n
        self.cols = [0]*n
        self.dig0 = self.dig1 = 0
        self.n = n

    def move(self, row, col, player):
        self.board[row][col] = player
        self.rows[row] += (-1)**player
        self.cols[col] += (-1)**player
        if row == col:
            self.dig0 += (-1)**player
        if row == self.n-1-col:
            self.dig1 += (-1)**player
        checks = [self.rows[row], self.cols[col], self.dig0, self.dig1]
        if (self.n in checks) or (-self.n in checks):
            return player
        else:
            return 0

obj = TicTacToe(3)

cmds = ["move"]*7
args = [
[0,0,1],
[0,2,2],
[2,2,1],
[1,1,2],
[2,0,1],
[1,0,2],
[2,1,1],
]

for arg in args:
    print(arg, obj.move(*arg))
