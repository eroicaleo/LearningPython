#!/usr/bin/env python

class Solution:
    def gameOfLife(self, board):
        self.ht, self.wi = len(board), len(board[0])
        def travel(i, j):
            s = sum([(board[p][q]&1) if 0<=p<self.ht and 0<=q<self.wi else 0 for p in [i-1,i,i+1] for q in [j-1,j,j+1]]) - board[i][j]
            if board[i][j] == 0:
                t = 1 if s == 3 else 0
            else:
                t = 1 if s in [2,3] else 0
            print('i, j, s, t = ', i, j, s, t)
            return board[i][j] + t*2
        for i in range(self.ht):
            for j in range(self.wi):
                board[i][j] = travel(i, j)
        print('1st updates: \n', board)
        for i in range(self.ht):
            for j in range(self.wi):
                board[i][j] = board[i][j] // 2
        print('2nd updates: \n', board)

sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(board)
