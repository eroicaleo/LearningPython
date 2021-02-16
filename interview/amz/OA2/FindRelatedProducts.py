#!/usr/bin/env python

from collections import deque

class Solution:
    def findRelatedProducts(self, items):
        # Build graph
        graph = {}
        for item in items:
            for p in item:
                graph.setdefault(p, set())
                for q in item:
                    if p != q:
                        graph[p].add(q)
        print(graph)

        # BFS to get connected components
        cc, visited = [], set()
        for p in graph:
            if p in visited:
                continue
            newcc, queue = [], deque([p])
            visited.add(p)
            while queue:
                q = queue.popleft()
                newcc.append(q)
                print(f'internal newcc = {newcc}')
                for r in graph[q]:
                    if not r in visited:
                        visited.add(r)
                        queue.append(r)
            print(f'newcc = {newcc}')
            if len(newcc) > len(cc):
                cc = newcc
        return cc

items = [
    ['product1', 'product2', 'product3'],
    ['product5', 'product2'],
    ['product6', 'product7'],
    ['product8', 'product7'],
]

items = [
    ['product1', 'product2'],
    ['product3', 'product4'],
    ['product5', 'product6'],
    ['product1', 'product3', 'product5'],
]


sol = Solution()
sol.findRelatedProducts(items)
