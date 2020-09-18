#!/usr/bin/env python3

import math

class Solution:
    def largestComponentSize(self, A):
        l = len(A)
        parent, size = list(range(l)), [1]*l
        def root(i):
            while parent[i] != i:
                i, parent[i] = parent[i], parent[parent[i]]
            return i
        def union(v, w):
            rootv, rootw = root(v), root(w)
            # print(f'root {v}: {rootv}, root {w}: {rootw}')
            if rootv != rootw:
                if size[rootv] >= size[rootw]:
                    parent[rootw] = rootv
                    size[rootv], size[rootw] = size[rootv]+size[rootw], 0
                else:
                    parent[rootv] = rootw
                    size[rootv], size[rootw] = 0, size[rootv]+size[rootw]
        for i in range(l):
            for j in range(i+1,l):
                if math.gcd(A[i], A[j]) > 1:
                    # print(f'union {A[i]}, {A[j]}')
                    union(i, j)
                    # print(f'parent = {parent}, size = {size}')
        return max(size)

A_list = [
    [4,6,15,35],
    [20,50,9,63],
    [2,3,6,7,4,12,21,39],
]

# A_list = [
#     [4,6,15,35],
# ]

sol = Solution()
for A in A_list:
    print(sol.largestComponentSize(A))
