#!/usr/bin/env python3

import math
from collections import deque
from Digraph import Digraph

class BreadthFirstDirectedPaths:
    def __init__(self, G, sources):
        self.marked = [0]*G.V
        self.edgeTo = [0]*G.V
        self.distTo = [math.inf]*G.V
        self.validateVertices(sources)
        self.bfs(G, sources)

    def validateVertex(self, v):
        V = len(self.marked)
        assert 0 <= v < V, f'vertex {v} is not between 0 and {V-1}'

    def validateVertices(self, sources):
        if len(sources) == 0:
            raise ValueError(f'validateVertices sources is empty string')
        for v in sources:
            self.validateVertex(v)

    def bfs(self, G, sources):
        queue = deque(sources)
        for s in sources:
            self.marked[s] = 1
            self.distTo[s] = 0
        while queue:
            v = queue.popleft()
            for w in G.getAdj(v):
                if not self.marked[w]:
                    self.marked[w] = 1
                    self.edgeTo[w] = v
                    self.distTo[w] = self.distTo[v]+1
                    queue.append(w)

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.marked[v]

    def pathTo(self, v):
        self.validateVertex(v)
        if not self.hasPathTo(v):
            return None
        path = [v]
        while self.distTo[v] > 0.0:
            w = self.edgeTo[v]
            path, v = path+[w], w
        return path[::-1]

    def getDistTo(self, v):
        self.validateVertex(v)
        return self.distTo[v]

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
    # https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
    # https://algs4.cs.princeton.edu/42digraph/largeDG.txt
    import sys
    G = Digraph(sys.argv[1])
    print(G)
    sources = list(map(int, sys.argv[2:]))
    bfs = BreadthFirstDirectedPaths(G, sources)

    for v in range(G.V):
        if bfs.hasPathTo(v):
            print(f'{sources} to {v}: {"->".join(map(str, bfs.pathTo(v)))}')
        else:
            print(f'{sources} to {v}: not connected')


