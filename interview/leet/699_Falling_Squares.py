#!/usr/bin/env python

class SegmentTree:
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0]*(2*N)
        self.lazy = [0]*N

    def 

class Solution:
    def fallingSquares(self, positions):

        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left+size-1)
        index = {x : i for i, x in enumerate(sorted(coords))}

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left+size-1]
            h = tree.query(L, R)+size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
