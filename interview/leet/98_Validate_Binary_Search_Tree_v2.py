#!/usr/bin/env python

from tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        left = self.isValidBST(root.left)
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        right = self.isValidBST(root.right)
        return left and right

nodeString = '[0,null,-1]'
nodeString = '[2,1,3]'
root = treeBuilder(nodeString)
sol = Solution()
print(sol.isValidBST(root))
