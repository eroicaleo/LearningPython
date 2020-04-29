#!/usr/bin/env python3

from DirectedEdge import DirectedEdge

class EdgeWeightedDigraph:
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.V = V
            self.E = 0
            self.indgree = [0]*V
            self.adj = [set() for i in range(V)]
        elif isinstance(args[0], str):
            with open(args[0]) as f:
                self.V = int(f.readline())
                self.E = int(f.readline())
                self.indgree = [0]*self.V
                self.adj = [set() for i in range(self.V)]
                for line in f:
                    line = line.strip().split()
                    v, w, weight = int(line[0]), int(line[1]), float(line[2])
                    self.validateVertex(v)
                    self.validateVertex(w)
                    self.addEdge(DirectedEdge(v, w, weight))
        else:
            raise TypeError('Wrong type of argument for EdgeWeightedDigraph constructor')

    def validateVertex(self, v):
        assert 0 <= v < self.V, f'vertex {v} is not between 0 and {self.V-1}'

    def addEdge(self, e):
        v, w = e.fromv(), e.to()
        self.validateVertex(v)
        self.validateVertex(w)
        self.adj[v].add(e)
        self.indgree[w] += 1
        self.E += 1

    def getAdj(self, v):
        return self.adj[v]

    def edges(self):
        return [e for a in self.adj for e in a]

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/44sp
    # E.g.
    # https://algs4.cs.princeton.edu/44sp/tinyEWD.txt
    G = EdgeWeightedDigraph('tinyEWD.txt')
    for e in G.edges():
        print(e)
