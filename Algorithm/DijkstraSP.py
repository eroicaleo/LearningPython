#!/usr/bin/env python3

import math
from EdgeWeightedDigraph import EdgeWeightedDigraph
from IndexMinPQ import IndexMinPQ

class DijkstraSP:
    def __init__(self, G, s):
        for e in G.edges():
            if e.weight < 0:
                raise ValueError(f'edge {e} has negative weight')
        self.distTo = [math.inf for v in range(G.V)]
        self.edgeTo = [None for v in range(G.V)]

        self.validateVertex(s)
        self.distTo[s] = 0.0

        self.pq = IndexMinPQ(G.V)
        self.pq.insert(s, self.distTo[s])

        while not self.pq.isEmpty():
            v = self.pq.delMin()
            for e in G.getAdj(v):
                self.relax(e)

        assert self.check(s)

    def relax(self, e):
        v, w = e.getVertex()
        if self.distTo[w] > self.distTo[v]+e.getWeight():
            self.distTo[w] = self.distTo[v]+e.getWeight()
            self.edgeTo[w] = e
            if self.pq.contains(w):
                self.pq.decreaesKey(w, self.distTo[w])
            else:
                self.pq.insert(w, self.distTo[w])

    def validateVertex(self, v):
        V = len(self.distTo) 
        assert 0 <= v < V, f'vertex {v} is not between 0 and {V-1}'

    def getDistTo(self, v):
        self.validateVertex(v)
        return self.distTo[v]

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.distTo[v] < math.inf
        
    def pathTo(self, v):
        self.validateVertex(v)
        if not self.hasPathTo(v):
            return None
        path = []
        e = self.edgeTo[v]
        while e:
            path.append(e)
            e = self.edgeTo[e.fromv()]
        return path

    def check(self, s):
        if any(e.getWeight() < 0 for e in G.edges()):
            print('negative edge weight detected')
            return False

        if self.distTo[s] != 0 or self.edgeTo[s] != None:
            print(f'distTo[{s}] and edgeTo[{s}] inconsistent')
            return False

        for v in range(G.V):
            for e in G.getAdj(v):
                w = e.to()
                if self.distTo[v] + e.getWeight() < self.distTo[w]:
                    print(f'edge {e} not relaxed')
                    return False

        for w in range(G.V):
            if not self.edgeTo[w]:
                continue
            e = self.edgeTo[w]
            v = e.fromv()
            if w != e.to():
                return False
            if self.distTo[v] + e.getWeight() != self.distTo[w]:
                print(f'edge {e} on shortest path not tight')
                return False

        return True

if __name__ == '__main__':
    import sys
    s = int(sys.argv[2])
    G = EdgeWeightedDigraph(sys.argv[1])
    sp = DijkstraSP(G, s)

    for t in range(G.V):
        if sp.hasPathTo(t):
            print(f'{s} to {t} {sp.getDistTo(t):.2f}')
            for e in sp.pathTo(t)[::-1]:
                print(f'  {e}')
        else:
            print(f'{s} to {t} has no path')
