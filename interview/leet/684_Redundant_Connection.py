#!/usr/bin/env python

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        graph, bag = dict(zip(range(1,n+1), range(1,n+1))), [set([i]) for i in range(1+n)]
        print(f'graph = {graph}, bag = {bag}')
        for e in edges:
            print(f'edge = {e}')
            v, w = e
            rootv, rootw = graph[v], graph[w]
            print(f'rootv = {rootv}, rootw = {rootw}')
            if rootv == rootw:
                return e
            for w in bag[rootw]:
                graph[w] = rootv
            bag[rootv], bag[rootw] = bag[rootv].union(bag[rootw]), set()
            print(f'bag = {bag}, graph = {graph}')

sol = Solution()
edges = [[1,2], [1,3], [2,3]]
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(sol.findRedundantConnection(edges))
