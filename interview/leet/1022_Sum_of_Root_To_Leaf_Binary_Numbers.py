#!/usr/bin/env python3

from tree import *

class Solution:
    def sumRootToLeaf(self, root):
        self.res = 0
        def dfs(pathsum, node):
            if node == None:
                return
            val = pathsum*2+node.val
            if node.left == node.right == None:
                self.res += val
            if node.left:
                dfs(val, node.left)
            if node.right:
                dfs(val, node.right)
        dfs(0, root)
        return self.res

nodeString = '[1,0,1,0,1,0,1]'
nodeString = '[1]'
nodeString = '[1,1]'
nodeString = '[0]'
root = treeBuilder(nodeString)
sol = Solution()
print(sol.sumRootToLeaf(root))

