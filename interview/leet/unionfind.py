#!/usr/bin/env python

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return (self.find(p) == self.find(q))

    def union(self, p, q):
        print('Union: %d and %d' % (p, q))
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] < self.size[rootq]:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        self.count -= 1

def stringToBoard(s, n):
    ret = [[''] * n for i in range(n)]
    s = s.replace(' ', '')
    for i in range(n):
        for j in range(n):
            ret[i][j] = s[i*n+j]
    return ret

def boardToString(board):
    boardSizeI = len(board)
    if boardSizeI == 0:
        return
    boardSizeJ = len(board[0])
    for s in board:
        print(' '.join(s))
