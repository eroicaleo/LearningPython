#!/usr/bin/env python3

class Solution:
    def findCircleNum(self, M):
        sz, num = len(M), 0
        marked = [False] * sz
        def dfs(p):
            marked[p] = True
            for q in range(sz):
                if M[p][q] and (not marked[q]):
                    dfs(q)
        for p in range(sz):
            if not marked[p]:
                num += 1
                dfs(p)
        return num

sol = Solution()
M = [[1,1,0],
     [1,1,0],
     [0,0,1]]
M = [[1,1,0],
     [1,1,1],
     [0,1,1]]
M = [[1]]
print(sol.findCircleNum(M))
