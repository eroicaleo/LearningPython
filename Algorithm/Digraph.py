#!/usr/bin/env python3

class Digraph:
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.V = args[0]
            if self.V < 0:
                raise ValueError('Number of vertices in a Digraph must be nonnegative')
            self.E = 0
            self.indgree = [0]*self.V
            self.adj = [set() for i in range(self.V)]
        elif isinstance(args[0], str):
            with open(args[0]) as f:
                self.V = int(f.readline())
                self.E, E = 0, int(f.readline())
                self.indgree = [0]*self.V
                self.adj = [set() for i in range(self.V)]
                for line in f:
                    line = line.strip().split()
                    v, w = int(line[0]), int(line[1])
                    self.validateVertex(v)
                    self.validateVertex(w)
                    self.addEdge(v, w)
                if self.E != E:
                    raise ValueError(f'Number of edges doesn\'t match in {args[0]}: expected {E}, read {self.E}')
        else:
            raise TypeError('Wrong type of argument for Digraph constructor')

    def validateVertex(self, v):
        assert 0 <= v < self.V, f'vertex {v} is not between 0 and {self.V-1}'

    def addEdge(self, v, w):
        self.validateVertex(v)
        self.validateVertex(w)
        self.adj[v].add(w)
        self.indgree[w] += 1
        self.E += 1

    def getAdj(self, v):
        self.validateVertex(v)
        return self.adj[v]

    def getOutdegree(self, v):
        self.validateVertex(v)
        return len(self.adj[v])

    def getIndegree(self, v):
        self.validateVertex(v)
        return self.indgree[v]

    def __str__(self):
        s = f'{self.V} vertices, {self.E} edges\n'
        for v in range(self.V):
            s += f'{v}: out degree: {self.getOutdegree(v)} : ' + ' '.join(map(str, sorted(self.adj[v])))
            s += f', indgree : {self.getIndegree(v)}\n'
        return s

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
    # https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
    # https://algs4.cs.princeton.edu/42digraph/largeDG.txt
    import sys
    G = Digraph(sys.argv[1])
    print(G)

