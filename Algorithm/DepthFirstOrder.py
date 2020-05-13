#!/usr/bin/env python3

from Digraph import Digraph

class DepthFirstOrder:
    def __init__(self, G):
        self.pre  = [0]*G.V
        self.post = [0]*G.V
        self.postorder = []
        self.preorder = []
        self.marked = [0]*G.V
        self.preCounter = 0
        self.postCounter = 0
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)
        print(self.pre)
        print(self.preorder)
        assert self.check()

    def dfs(self, G, v):
        self.marked[v] = 1
        self.pre[v] = self.preCounter
        self.preCounter += 1
        self.preorder.append(v)
        for w in G.getAdj(v):
            if not self.marked[w]:
                self.dfs(G, w)
        self.post[v] = self.postCounter
        self.postCounter += 1
        self.postorder.append(v)

    def getPre(self, *args):
        if len(args) == 0:
            return self.preorder
        return self.pre[args[0]]

    def getPost(self, *args):
        if len(args) == 0:
            return self.postorder
        return self.post[args[0]]

    def reversePost(self):
        return self.postorder[::-1]

    def check(self):
        for r, v in enumerate(self.getPost()):
            if self.post[v] != r:
                return False
        for r, v in enumerate(self.getPre()):
            if self.pre[v] != r:
                return False
        return True

    def validateVertex(self, v):
        V = len(self.marked)
        assert 0 <= v < V, f'vertex {v} is not between 0 and {V-1}'

if __name__ == '__main__':
    # The test case can be downloaded from here
    # https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt
    import sys
    G = Digraph(sys.argv[1])
    print(G)
    dfs = DepthFirstOrder(G)
    print(f'   v  pre post')
    print(f'______________')
    for v in range(G.V):
        print(f'{v:4d} {dfs.getPre(v):4d} {dfs.getPost(v):4d}')
    print(f'Preorder: {dfs.getPre()}')
    print(f'Postorder: {dfs.getPost()}')
    print(f'Reverse postorder: {dfs.reversePost()}')

