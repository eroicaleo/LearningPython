#!/usr/bin/env python3

class Solution:
    def validTicTacToe(self, board):
        x_r, x_c, o_r, o_c = [0]*3, [0]*3, [0]*3, [0]*3
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == 'O':
                    o_r[i] += 1
                    o_c[j] += 1
                elif c == 'X':
                    x_r[i] += 1
                    x_c[j] += 1
        if sum(x_c)-sum(o_c) < 0 or sum(x_c)-sum(o_c) > 1:
            print(f'I am in 1')
            return False
        r_win, c_win = sum(1 for x in x_r+o_r if x == 3), sum(1 for x in x_c+o_c if x == 3)
        if r_win > 1 or c_win > 1:
            print(f'I am in 2')
            return False
        if sum(x_c)-sum(o_c) == 0 and r_win+c_win > 0:
            print(f'I am in 3')
            return False
        return True

board = ["XXX", "   ", "OOO"]
board = ["XOX", " X ", "   "]
board = ["O  ", "   ", "   "]
board = ["XOX", "OXO", "XOX"]
board = ["XXX", "XOO", "OO "]
sol = Solution()
print(sol.validTicTacToe(board))
