#!/usr/bin/env python

class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        # Each row
        for i in range(9):
            sudoku = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in sudoku:
                    return False
                else:
                    sudoku[board[i][j]] = 1
        # Each col
        for i in range(9):
            sudoku = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in sudoku:
                    return False
                else:
                    sudoku[board[j][i]] = 1
        # Each 3x3 square
        for i in range(0,9,3):
            for j in range(0,9,3):
                sudoku = {}
                for p in range(3):
                    for q in range(3):
                        if board[i+p][j+q] == ".":
                            continue
                        if board[i+p][j+q] in sudoku:
                            return False
                        else:
                            sudoku[board[i+p][j+q]] = 1
        return True

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
sol = Solution()
print(sol.isValidSudoku(board))
