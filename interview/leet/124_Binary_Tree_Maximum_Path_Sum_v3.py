#!/usr/bin/env python3

from tree import *

class Solution:
    def maxPathSum(self, root):
        self.maxSum = root.val
        def dfs(root):
            if not root:
                return 0
            v = root.val
            l, r = dfs(root.left), dfs(root.right)
            self.maxSum = max(self.maxSum, l+v, r+v, l+r+v)
            return max(v, l+v, r+v)
        dfs(root)
        return self.maxSum

nodeString = '[-10,9,20,null,null,15,7]'
nodeString = '[1,2,3]'
root = treeBuilder(nodeString)
traverse(root)
sol = Solution()
print(sol.maxPathSum(root))
