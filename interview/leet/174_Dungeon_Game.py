#!/usr/bin/env python

# -2 -3   3
# -5 -10  1
# 10  30 -5

import math
from collections import deque

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        nr, nc = len(dungeon), len(dungeon[0])
        visited = [[0]*nc for _ in range(nr)]
        cost = [[math.inf]*nc for _ in range(nr)]

        queue = deque([(nr-1, nc-1, max(0, -dungeon[nr-1][nc-1]))])
        while queue:
            i, j, d = queue.popleft()
            if i > 0:
                visited[i-1][j] += 1
                cost[i-1][j] = min(cost[i-1][j], d)
                if (visited[i-1][j] == 2) or (j == nc-1):
                    queue.append((i-1, j, max(0, cost[i-1][j]-dungeon[i-1][j])))
            if j > 0:
                visited[i][j-1] += 1
                cost[i][j-1] = min(cost[i][j-1], d)
                if (visited[i][j-1] == 2) or (i == nr-1):
                    queue.append((i, j-1, max(0, cost[i][j-1]-dungeon[i][j-1])))
            print(queue)
        return d+1


dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
for row in dungeon:
    print(row)
sol = Solution()
print(sol.calculateMinimumHP(dungeon))
