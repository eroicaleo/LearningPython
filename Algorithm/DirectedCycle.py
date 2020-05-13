#!/usr/bin/env python3

from Digraph import Digraph

class DirectedCycle:
    def __init__(self, G):
        self.marked = [0]*G.V
        self.edgeTo = [0]*G.V
        self.onStack = [0]*G.V
        self.cycle = None
        for v in range(len(self.marked)):
            if (not self.marked[v]) and (not self.cycle):
                self.dfs(G, v)

    def dfs(self, G, v):
        self.onStack[v] = 1
        self.marked[v] = 1
        for w in G.getAdj(v):
            if self.cycle:
                return
            elif not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)
            elif self.onStack[w]:
                cycle, x = [], v
                while x != w:
                    cycle, x = cycle+[x], self.edgeTo[x]
                cycle += [w, v]
                self.cycle = cycle[::-1]
                assert self.check()
        self.onStack[v] = 0

    def check(self):
        if self.cycle[0] != self.cycle[-1]:
            print(f'cycle begins with {self.cycle[0]} and ends with {self.cycle[1]}')
            return False
        return True

    def hasCycle(self):
        return self.cycle != None

    def getCycle(self):
        return self.cycle

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
    # https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt
    import sys
    G = Digraph(sys.argv[1])
    print(G)
    finder = DirectedCycle(G)

    if finder.hasCycle():
        print(f'Directed cycle: {finder.getCycle()}')
    else:
        print('No Directed Cycle')
