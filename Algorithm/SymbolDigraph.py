#!/usr/bin/env python3

# https://algs4.cs.princeton.edu/42digraph/SymbolDigraph.java.html
# https://algs4.cs.princeton.edu/42digraph/routes.txt

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
                a = line.strip().split(delimiter)
                src, dst_list = a[0], a[1:]
                for dst in dst_list:
                    v, w = self.st[src], self.st[dst]
                    self.graph.addEdge(v, w)

    def contains(self, s):
        return self.st.contains(s)

    def indexOf(self, s):
        return self.st[s]

    def nameOf(self, v):
        self.graph.validateVertex(v)
        return self.keys[v]

    def digraph(self):
        return self.graph

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/routes.txt
    # https://algs4.cs.princeton.edu/42digraph/jobs.txt
    import sys
    if len(sys.argv) == 2:
        sg = SymbolDigraph(sys.argv[1])
    else:
        sg = SymbolDigraph(sys.argv[1], sys.argv[2])
    for k in sg.st:
        print(f'{k}: {sg.st[k]}')
    print(sg.keys)
    print('#'*80)
    print('Validate digraph')
    print('#'*80)
    print(sg.digraph())
    print('#'*80)
    print('Validate nameOf')
    print('#'*80)
    for v in range(len(sg.keys)):
        print(f'{v}, {sg.nameOf(v)}')
    print('#'*80)
    print('Validate digraph')
    print('#'*80)
    graph = sg.digraph()
    for v in range(graph.V):
        print(f'{sg.nameOf(v)}')
        for w in graph.getAdj(v):
            print(f'  {sg.nameOf(w)}')

