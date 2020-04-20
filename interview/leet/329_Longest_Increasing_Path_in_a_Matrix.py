#!/usr/bin/env python3

import collections

class Solution:
    def longestIncreasingPath(self, matrix):
        nrow, ncol = len(matrix), len(matrix[0]) if matrix else 0
        visited, delta = [[0 for j in range(ncol)] for i in range(nrow)], [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            print(f'I am visiting ({i}, {j})')
            if visited[i][j] > 0:
                return visited[i][j]
            visited[i][j] = 1
            for dx, dy in delta:
                x, y = i+dx, j+dy
                print(f'x, y = {x}, {y}')
                if x < 0 or x >= nrow or y < 0 or y >= ncol or matrix[x][y] <= matrix[i][j]:
                    print(f'will continue x, y = {x}, {y}')
                    continue
                visited[i][j] = max(visited[i][j], dfs(x, y)+1)
            return visited[i][j]
        return max([dfs(i, j) for i in range(nrow) for j in range(ncol)] + [0])

    def longestIncreasingPath_BFS_TOPO(self, matrix):
        for r in matrix:
            print(r)
        nrow, ncol = len(matrix), len(matrix[0]) if matrix else 0
        graph, delta, indegree = {}, [(1, 0), (-1, 0), (0, 1), (0, -1)], [0]*(nrow*ncol)
        for i in range(nrow):
            for j in range(ncol):
                for dx, dy in delta:
                    x, y = i+dx, j+dy
                    if x < 0 or x >= nrow or y < 0 or y >= ncol or matrix[x][y] <= matrix[i][j]:
                        continue
                    v, w = ncol*i+j, ncol*x+y
                    graph.setdefault(v, []).append(w)
                    indegree[w] += 1

        for v in graph:
            print(f'{v} : {graph[v]}')
        print(indegree)

        queue, l = collections.deque([i for i, v in enumerate(indegree) if v == 0]), 0
        print(queue)
        while queue:
            for i in range(len(queue)):
                for w in graph.setdefault(queue.popleft(), []):
                    indegree[w] -= 1
                    if indegree[w] == 0:
                        queue.append(w)
            l += 1
            print(f'queue = {queue}')
        return l
        # for i in range(nrow):
        #     for j in range(ncol):
        #         if visited[i][j] == 0:
        #             dfs(i, j)
        #             for k in range(nrow):
        #                 print(visited[k])

sol = Solution()
nums = [[3,4,5], [3,2,6], [2,2,1]]
nums = []
nums = [[9,9,4], [6,6,8], [2,1,1]]
print(sol.longestIncreasingPath_BFS_TOPO(nums))
