#!/usr/bin/env python3

from Digraph import Digraph

class SymbolDigraph:
    def __init__(self, filename, delimiter=' '):
        self.st = {}
        with open(filename) as f:
            for line in f:
                for a in line.strip().split(delimiter):
                    self.st[a] = self.st.get(a, len(self.st))
        self.keys = sorted(self.st, key=lambda k: self.st[k])

        self.graph = Digraph(len(self.st))
        with open(filename) as f:
            for line in f:
                src, dst = line.strip().split(delimiter)
                v, w = self.st[src], self.st[dst]
                self.graph.addEdge(v, w)

        for k in self.st:
            print(f'{k}: {self.st[k]}')
        print(self.keys)
        print(self.graph)

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/routes.txt
    import sys
    sg = SymbolDigraph(sys.argv[1])

