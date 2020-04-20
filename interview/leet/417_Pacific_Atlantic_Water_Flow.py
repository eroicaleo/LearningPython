#!/usr/bin/env python3

import collections

class Solution:
    def pacificAtlantic(self, matrix):
        nrow, ncol = len(matrix), len(matrix[0]) if matrix else 0
        pvisited, avisited = [[0 for j in range(ncol)] for i in range(nrow)], [[0 for j in range(ncol)] for i in range(nrow)]
        def dfs(i, j, visited):
            visited[i][j] = 1
            for x, y in [(i-1, j+0), (i+1, j+0), (i+0, j-1), (i+0, j+1)]:
                if x < 0 or x >= nrow or y < 0 or y >= ncol or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                dfs(x, y, visited)
        for i in range(nrow):
            dfs(i, 0, pvisited)
            dfs(i, ncol-1, avisited)
        for j in range(ncol):
            dfs(0, j, pvisited)
            dfs(nrow-1, j, avisited)
        return [[i, j] for i in range(nrow) for j in range(ncol) if avisited[i][j] and pvisited[i][j]]

    def pacificAtlantic_BFS(self, matrix):
        nrow, ncol = len(matrix), len(matrix[0]) if matrix else 0
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pvisited, avisited = [[0 for j in range(ncol)] for i in range(nrow)], [[0 for j in range(ncol)] for i in range(nrow)]
        def bfs(visited, queue):
            while queue:
                i, j = queue.popleft()
                visited[i][j] = 1
                for dx, dy in delta:
                    x, y = i+dx, j+dy
                    if x < 0 or x >= nrow or y < 0 or y >= ncol or visited[x][y] or matrix[x][y] < matrix[i][j]:
                        continue
                    queue.append([x, y])
        pqueue = collections.deque([[0, i] for i in range(ncol)] + [[i, 0] for i in range(nrow)])
        aqueue = collections.deque([[nrow-1, i] for i in range(ncol)] + [[i, ncol-1] for i in range(nrow)])
        bfs(pvisited, pqueue)
        bfs(avisited, aqueue)
        return [[i, j] for i in range(nrow) for j in range(ncol) if avisited[i][j] and pvisited[i][j]]

                


sol = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
matrix = [[10,10,10],[10,1,10],[10,10,10]]
print(sol.pacificAtlantic(matrix))
print(sol.pacificAtlantic_BFS(matrix))

