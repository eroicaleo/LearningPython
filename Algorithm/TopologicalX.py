#!/usr/bin/env python3

import sys
from DirectedEdge import DirectedEdge
from SymbolDigraph import SymbolDigraph
from collections import deque

class TopologicalX:
    def __init__(self, G):
        self.indgree = [0]*G.V
        queue = deque()
        for v in range(G.V):
            self.indgree[v] = G.indgree[v]
            if self.indgree[v] == 0:
                queue.append(v)

        self.ranks = [0]*G.V
        self.order = []
        count = 0

        while queue:
            v = queue.popleft()
            self.order.append(v)
            self.ranks[v] = count
            count += 1
            for w in G.getAdj(v):
                self.indgree[w] -= 1
                if self.indgree[w] == 0:
                    queue.append(w)

        if count != G.V:
            self.order = None

        assert self.check(G);

    def getOrder(self):
        return self.order

    def hasOrder(self):
        return self.order != None

    def validateVertex(self, v):
        V = len(self.ranks)
        assert 0 <= v < V, f'vertex {v} is not between 0 and {V-1}'

    def getRank(self, v):
        self.validateVertex(v)
        if self.order:
            return self.ranks[v]
        else:
            return -1

    def check(self, G):
        if self.order:
            # Check that ranks are a permutation of 0 to V-1
            found = [False]*G.V
            for i in range(G.V):
                found[self.ranks[i]] = True
            for i in range(G.V):
                if not found[i]:
                    print(f'No vertex with ranks {i}')
                    return False

            # Check that ranks provide a valid topological order
            for v in range(G.V):
                for e in G.getAdj(v):
                    if isinstance(e, DirectedEdge):
                        w = e.to()
                    else:
                        w = e
                    if self.ranks[v] > self.ranks[w]:
                        print(f'{v}-{w}: ranks({v}) = {self.ranks[v]}, ranks({w}) = {self.ranks[w]}')
                        return False

            # Check order() is consistent with rank()
            for r, v in enumerate(self.order):
                if self.ranks[v] != r:
                    print(f'order() and ranks() inconsistent')
                    return False

            return True

if __name__ == '__main__':
    # Run like this:
    # ./TopologicalX.py jobs.txt "/"
    sg = SymbolDigraph(sys.argv[1], sys.argv[2])
    topological = TopologicalX(sg.digraph())
    for v in topological.getOrder():
        print(f'{sg.nameOf(v)}')
