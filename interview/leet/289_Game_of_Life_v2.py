#!/usr/bin/env python

import itertools

class Solution:
    def gameOfLife(self, board):
        delta = set(itertools.product([-1,0,1],[-1,0,1]))
        delta.discard((0,0))

        for i


sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(board)
