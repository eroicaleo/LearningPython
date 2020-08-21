#!/usr/bin/env python

class Solution:
    def allPathsSourceTarget(self, graph): 
        res, target = [], len(graph)-1
        def dfs(v, path):
            if v == target:
                res.append(path)
                return
            for w in graph[v]:
                dfs(w, path+[w])
        dfs(0, [0])
        return res

    def allPathsSourceTarget_BFS(self, graph): 
        from collections import deque
        queue, res, target = deque([[0]]), [], len(graph)-1
        while queue:
            p = queue.popleft()
            if p[-1] == target:
                res.append(p)
            else:
                for v in graph[p[-1]]:
                    queue.append(p+[v])
        return res


sol = Solution()
graph = [[1,2], [3], [3], [0]]
print(sol.allPathsSourceTarget(graph))
print(sol.allPathsSourceTarget_BFS(graph))
