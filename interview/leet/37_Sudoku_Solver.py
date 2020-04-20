#!/usr/bin/env python3

import itertools
from collections import Counter

class Solution:
    def solveSudoku(self, board):
        self.d = {}
        self.empty_space = len([(i,j) for i, j in itertools.product(range(9), range(9)) if board[i][j] == '.'])

        def update(i, j, n, inc):
            for k in range(9):
                self.d.setdefault((i, k), Counter())[n] += inc
            for k in range(9):
                self.d.setdefault((k, j), Counter())[n] += inc
            for k, l in itertools.product(range(3), range(3)):
                x, y = (i//3)*3+k, (j//3)*3+l
                self.d.setdefault((x, y), Counter())[n] += inc

        def max_entry():
            return max([(i,j) for i, j in itertools.product(range(9), range(9)) if board[i][j] == '.'], key=lambda k: len([v for v in self.d[k] if self.d[k][v] > 0]))

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    update(i, j, board[i][j], 1)

        print(f'max_entry : {self.d[max_entry()]}')

        def debug(title):
            print('#'*80)
            print(title)
            print('#'*80)
            for row in board:
                print(row)
            for k in sorted(self.d):
                print(k, self.d[k])

        def dfs():
            if self.empty_space == 0:
                return True
            x, y = max_entry()
            self.empty_space -= 1
            a = set(k for k in self.d[(x, y)] if self.d[(x,y)][k] > 0)
            for i in set(list("123456789")) - a:
                update(x,y,i,1)
                board[x][y] = i
                debug(f'After updating, {self.empty_space}, x = {x}, y = {y}')
                if dfs():
                    return True
                update(x,y,i,-1)
                debug('After removing')
            board[x][y] = '.'
            self.empty_space += 1
            return False

        dfs()

board = [
['5','3','.','.','7','.','.','.','.'],
['6','.','.','1','9','5','.','.','.'],
['.','9','8','.','.','.','.','6','.'],
['8','.','.','.','6','.','.','.','3'],
['4','.','.','8','.','3','.','.','1'],
['7','.','.','.','2','.','.','.','6'],
['.','6','.','.','.','.','2','8','.'],
['.','.','.','4','1','9','.','.','5'],
['.','.','.','.','8','.','.','7','9'],
]

board = [
[".",".","9","7","4","8",".",".","."],
["7",".",".",".",".",".",".",".","."],
[".","2",".","1",".","9",".",".","."],
[".",".","7",".",".",".","2","4","."],
[".","6","4",".","1",".","5","9","."],
[".","9","8",".",".",".","3",".","."],
[".",".",".","8",".","3",".","2","."],
[".",".",".",".",".",".",".",".","6"],
[".",".",".","2","7","5","9",".","."]]

final_board = [
["5","1","9","7","4","8","6","3","2"],
["7","8","3","6","5","2","4","1","9"],
["4","2","6","1","3","9","8","7","5"],
["3","5","7","9","8","6","2","4","1"],
["2","6","4","3","1","7","5","9","8"],
["1","9","8","5","2","4","3","6","7"],
["9","7","5","8","6","3","1","2","4"],
["8","3","2","4","9","1","7","5","6"],
["6","4","1","2","7","5","9","8","3"]]

sol = Solution()
print(sol.solveSudoku(board))
print(list(itertools.product(range(3), range(3))))
# print(sum([set([1,2]), set([2,3])]))
