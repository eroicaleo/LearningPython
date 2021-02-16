#!/usr/bin/env python

class Solution:
    def calcEquation(self, equations, values, queries):
        graph, ret = {}, []
        for st, v in zip(equations, values):
            s, t = st
            graph.setdefault(s, []).append((t, v))
            graph.setdefault(t, []).append((s, 1.0/v))
        def dfs(s, q):
            if s not in graph or s in visited:
                return -1.0
            visited.add(s)
            for t, w in graph[s]:
                if t == q:
                    return w
                u = dfs(t, q)
                if u > 0:
                    return w*u
            return -1.0
        for s, t in queries:
            visited = set()
            ret.append(dfs(s, t))
        return ret

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

sol = Solution()
print(sol.calcEquation(equations, values, queries))
