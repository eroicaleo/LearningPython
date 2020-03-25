#!/usr/bin/env python

# Thinking process
# I read the top voted solutions and got the conlution
# The reduandent edge can be either:
# 1. if there is one vertex whose in-degree is 2
# 2. if every vertex's in-degree is one, then it's the edge that makes the circle

# For item 1, when travel trough edge list, we record the parent of one node.
# If we find a node's parent is not itself then it's one of the 2 candidates
# But which of the 2 parents we need to select depends on how many unions left after 1-pass
# If there is 1 union left then, the 2nd parent is reduandent, otherwise it's the 1st.

# Find a cycle is also easy, see the case 2 comment below.
# We also use 'n' to track the number of unions

class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        union = dict(zip(range(1,n+1), range(1,n+1)))
        last_cycle_edge = candidate_edge = candidate = None
        print(f'union = {union}')
        def root(v):
            while union[v] != v:
                v = union[v]
            return v
        for e in edges:
            v, w = e
            rootv, rootw = root(v), root(w)
            print(f'v = {v}, w = {w}, rootv = {rootv}, rootw = {rootw}')
            if rootw != w: # case 1: w's in-degree is 2
                candidate_edge, candidate = e, w
                print(f'candidate_edge = {candidate_edge}')
                continue
            if rootv == w: # case 2: [v, w] makes a cycle
                last_cycle_edge = e
                print(f'last_cycle_edge = {last_cycle_edge}')
                continue
            union[w], n = v, n-1
            print(f'union = {union}, n = {n}')
        return [union[candidate], candidate] if n > 1 else (candidate_edge or last_cycle_edge)

sol = Solution()
edges = [[2,1], [3,1], [4,2], [1,4]]
edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
edges = [[1,2], [1,3], [2,3]]
print(sol.findRedundantDirectedConnection(edges))
