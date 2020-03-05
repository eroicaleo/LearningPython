#!/usr/bin/env python

from tree import *

class Solution:
    def pathSum(self, root, sum): 
        if root == None or root.val > sum:
            return []
        elif (root.val == sum) and (root.left == None) and (root.right == None):
            return [[root.val]]
        return [[root.val] + l for l in self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)]

sol = Solution()
nodeList = '[5,4,8,11,null,13,4,7,2,null,null,5,1]'
nodeList = '[5,4,8]'
nodeList = '[]'
root = treeBuilder(nodeList)
traverse(root)
print(sol.pathSum(root, 22))
