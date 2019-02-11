#!/usr/bin/env python

from tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        stack, node, prev = [], root, None
        while node or stack:
            while node:
                stack, node = stack + [node], node.left
            node = stack.pop(-1)
            if prev and prev.val >= node.val:
                return False
            node, prev = node.right, node
        return True

nodeString = '[2,1,3]'
nodeString = '[0,null,-1]'
root = treeBuilder(nodeString)
sol = Solution()
print(sol.isValidBST(root))
