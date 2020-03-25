#!/usr/bin/env python

class Solution:
    def minSwapsCouples(self, row):
        edge, V = {r:i//2 for i, r in enumerate(row)}, len(row)//2
        size, parent = [1] * V, list(range(V))
        def root(v):
            while parent[v] != v:
                parent[v], v = parent[parent[v]], parent[v]
            return v
        def union(v, w):
            rootv, rootw = root(v), root(w)
            if rootv == rootw:
                return
            if size[rootv] < size[rootw]:
                rootv, rootw = rootw, rootv
            parent[rootw], size[rootv], size[rootw] = rootv, size[rootv]+size[rootw], 0
        for v in range(V):
            union(edge[2*v], edge[2*v+1])
            print(f'After union {edge[2*v]}, {edge[2*v+1]}, size = {size}, parent = {parent}')
        return sum(map(lambda e: 0 if e == 0 else e-1, size))

row = [0, 2, 1, 3]
sol = Solution()
import itertools
for row in itertools.permutations(range(8)):
    print(f'row = {row}')
    print(sol.minSwapsCouples(row))
