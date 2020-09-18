#!/usr/bin/env python3

class Solution:
    def isRobotBounded(self, instructions):
        d = {'G':0, 'L':-1, 'R':1}
        delta, k = [(0,1),(-1,0),(0,-1),(1,0)], 0
        x = y = 0
        for i in instructions:
            if i == 'L':
                k = (k+1)%4
            elif i == 'R':
                k = (k-1)%4
            else:
                x, y = x+delta[k][0], y+delta[k][1]
        return (x==y==0) or (sum(d[i] for i in instructions)%4 != 0)

instructions_list = [
'GGLLGG',
'GG',
'GL',
'GLRLLGLL'
]

sol = Solution()
for instructions in instructions_list:
    print(instructions, sol.isRobotBounded(instructions))
