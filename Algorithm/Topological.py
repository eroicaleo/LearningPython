#!/usr/bin/env python3

# https://algs4.cs.princeton.edu/42digraph/Topological.java.html
# https://algs4.cs.princeton.edu/42digraph/jobs.txt

import sys
from SymbolDigraph import SymbolDigraph
from DirectedCycle import DirectedCycle
from DepthFirstOrder import DepthFirstOrder

class Topological:
    def __init__(self, G):
        self.finder = DirectedCycle(G)
        self.order = None
        self.G = G
        if not self.finder.hasCycle():
            dfs = DepthFirstOrder(G)
            self.order = dfs.reversePost()
            self.rank = [0]*G.V
            for i, v in enumerate(self.order):
                self.rank[v] = i

    def getOrder(self):
        return self.order

    def hasOrder(self):
        return self.order != None

    def getRank(self, v):
        self.G.validateVertex(v)
        return self.rank[v]

if __name__ == '__main__':
    sg = SymbolDigraph(sys.argv[1], sys.argv[2])
    topological = Topological(sg.digraph())
    for v in topological.getOrder():
        print(f'{sg.nameOf(v)}')
