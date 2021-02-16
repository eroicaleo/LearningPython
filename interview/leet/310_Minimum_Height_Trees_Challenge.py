#!/usr/bin/env python

import collections

class Solution:
    def findMinHeightTrees(self, n, edges):
        graph = {}
        for u, v in edges:
            graph.setdefault(u, set()).add(v)
            graph.setdefault(v, set()).add(u)

        queue = collections.deque([])
        for v in graph:
            if len(graph[v]) == 1:
                queue.append(v)

        while n > 2:
            for _ in range(len(queue)):
                u, n = queue.popleft(), n-1
                for v in graph[u]:
                    graph[v].discard(u)
                    if len(graph[v]) == 1:
                        queue.append(v)
                del graph[u]

        return list(queue) or [0]


sol = Solution()
pair = [
        (4, [[1, 0], [1, 2], [1, 3]]),
        (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]),
        (1, []),
        ]
for p in pair:
    print(sol.findMinHeightTrees(p[0], p[1]))

