#!/usr/bin/env python3

import math

class Solution:
    def winnerSquareGame(self, n):
        res = [False, True] + [False]*(n-1)
        for i in range(2, n+1):
            temp = [(not res[i-j**2]) for j in range(1, int(math.sqrt(i))+1)]
            print(f'i = {i}, temp = {temp}')
            res[i] = any(temp)
        print(res)
        return res[-1]

sol = Solution()
for n in range(19, 20):
    print(f'{n}: {sol.winnerSquareGame(n)}')
