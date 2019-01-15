#!/usr/bin/env python

from tree import *

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees or [None]
        return generate(1, n)


sol = Solution()
for root in sol.generateTrees(0):
    print(root)
    print(treeToString(root))

