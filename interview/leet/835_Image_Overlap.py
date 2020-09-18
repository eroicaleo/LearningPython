#!/usr/bin/env python3

import collections
class Solution:

    # This is lee315's solution
    # The brilliant part of this solution is
    # it converts 2-d array (A/B) to 1-d array (LA/LB)
    # For (i,j) in A, it converts (100*i+j)
    # Then it's much easier to compute the distance of
    # each array element.
    # Another trick is to use the sparsity.
    # LA is is not concatenated A, it only keeps the non-zero
    # element of A.
    def largestOverlap(self, A, B):
        N = len(A)
        LA = [100*i+j for i in range(N) for j in range(N) if A[i][j]]
        LB = [100*i+j for i in range(N) for j in range(N) if B[i][j]]
        c = collections.Counter(i-j for i in LA for j in LB)
        return c.most_common(1)[0][1] if c else 0

A = [
[1,1,0],
[0,1,0],
[0,1,0],
]

B = [
[0,0,0],
[0,1,1],
[0,0,1],
]

A = [[0]]
B = [[0]]

A = B = []
sol = Solution()
print(sol.largestOverlap(A, B))
