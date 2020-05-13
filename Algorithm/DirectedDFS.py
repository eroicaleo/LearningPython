#!/usr/bin/env python3

from Digraph import Digraph

class DirectedDFS:
    def __init__(self, G, sources):
        self.marked = [0]*G.V
        self.count = 0
        self.validateVertices(sources)
        self.sources = sources
        for v in sources:
            self.dfs(G, v)

    def dfs(self, G, v):
        self.count += 1
        self.marked[v] = 1
        for w in G.getAdj(v):
            if self.marked[w] == 0:
                self.dfs(G, w)

    def validateVertex(self, v):
        V = len(self.marked)
        assert 0 <= v < V, f'vertex {v} is not between 0 and {V-1}'

    def validateVertices(self, sources):
        if len(sources) == 0:
            raise ValueError(f'validateVertices sources is empty string')
        for v in sources:
            self.validateVertex(v)

    def getMarked(self, v):
        return self.marked[v]

    def getCount(self):
        return self.count
    
if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
    # https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
    # https://algs4.cs.princeton.edu/42digraph/largeDG.txt
    import sys
    G = Digraph(sys.argv[1])
    print(G)
    sources = list(map(int, sys.argv[2:]))
    dfs = DirectedDFS(G, sources)

    for v in range(G.V):
        if dfs.getMarked(v):
            print(f'{v} ', end="")
    print(f'these {dfs.getCount()} vertices can be reached!')

