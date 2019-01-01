#!/usr/bin/env python

class Graph:
    def __init__(self, n, edges):
        # n is the number of vertices
        # edges is a list of tuples which represents one edge
        self.n = n
        self.V = set(list(range(n)))
        self.E = [set() for i in range(n)]
        for e in edges:
            v, w = e
            self.E[v].add(w)
            self.E[w].add(v)

    def __str__(self):
        ret = ''
        ret += 'There are %d vertices.\n' % self.n
        for v in self.V:
            ret += 'Vertex %d has edges to: %s\n' % (v, self.E[v])
        return ret

if __name__ == '__main__':
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    g1 = Graph(n, edges)
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    g2 = Graph(n, edges)
    print(g1)
    print(g2)
