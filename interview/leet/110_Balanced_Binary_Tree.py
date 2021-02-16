#!/usr/bin/env python3

from tree import *

class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if root == None:
                return 0, True
            hl, bl = dfs(root.left)
            hr, br = dfs(root.right)
            return 1+max(hl, hr), bl and br and abs(hl-hr) < 2
        return dfs(root)[1]

nodeString = '[1,2,2,3,3,null,null,4,4]'
nodeString = '[3,9,20,null,null,15,7]'
nodeString = '[]'
root = treeBuilder(nodeString)
sol = Solution()
print(sol.isBalanced(root))
