#!/usr/bin/env python3

from Digraph import Digraph

class DepthFirstDirectedPaths:
    def __init__(self, G, s):
        self.marked = [0]*G.V
        self.edgeTo = [0]*G.V
        self.s = s
        self.validateVertex(s)
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = 1
        for w in G.getAdj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)

    def validateVertex(self, v):
        V = len(self.marked)
        assert 0 <= v < V, f'vertex {v} is not between 0 and {V-1}'

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.marked[v]

    def pathTo(self, v):
        self.validateVertex(v)
        if not self.hasPathTo(v):
            return None
        path = [v]
        while self.edgeTo[v] != s:
            w = self.edgeTo[v]
            path, v = path+[w], w
        path.append(s)
        return path[::-1]

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
    # https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
    # https://algs4.cs.princeton.edu/42digraph/largeDG.txt
    import sys
    G = Digraph(sys.argv[1])
    print(G)
    s = int(sys.argv[2])
    dfs = DepthFirstDirectedPaths(G, s)

    for v in range(G.V):
        if dfs.hasPathTo(v):
            print(f'{s} to {v}: {"-".join(map(str, dfs.pathTo(v)))}')
        else:
            print(f'{s} to {v}: not connected')


