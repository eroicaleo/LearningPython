#!/usr/bin/env python

class Solution:
    def calcEquation(self, equations, values, queries):
        graph, ret = {}, []
        for e, v in zip(equations, values):
            graph.setdefault(e[0], {})[e[1]] = v
            graph.setdefault(e[1], {})[e[0]] = 1.0/v
        def dfs(p, q):
            if (p not in graph) or (p in visited):
                return -1.0
            if p == q:
                return 1.0
            visited.add(p)
            for r in graph[p]:
                v = dfs(r, q)
                if v >= 0:
                    return v * graph[p][r]
            else:
                return -1.0
        for q in queries:
            visited = set()
            ret.append(dfs(*q))
        return ret


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

sol = Solution()
print(sol.calcEquation(equations, values, queries))
