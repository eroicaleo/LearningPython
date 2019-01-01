#!/usr/bin/env python

# Idea: remove the leaf nodes, i.e. nodes with degree 1
# After removing these nodes, the distances between the resting nodes stay the same
# Keep removing the leaf nodes, until there is only 1 or 2 nodes left

from graph import Graph

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        G = Graph(n, edges)
        while G.n > 2:
            self.removeLeafNodes(G)
        return list(G.V)

    def removeLeafNodes(self, G):
        removeSet = set()
        for v in G.V:
            if len(G.E[v]) == 1:
                removeSet.add(v)
        for v in removeSet:
            w = G.E[v].pop()
            G.E[w].remove(v)
            G.n -= 1
            G.V.remove(v)
            print("removing node %d, the edges of %d after removing %s" % (v, w, G.E[w]))


sol = Solution()
pair = [
        (4, [[1, 0], [1, 2], [1, 3]]),
        (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
        ]
for p in pair:
    print(sol.findMinHeightTrees(p[0], p[1]))

