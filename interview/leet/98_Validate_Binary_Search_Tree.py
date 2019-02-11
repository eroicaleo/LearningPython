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
        return self.isValidBSTRecursive(root, None, None)

    def isValidBSTRecursive(self, node, lb, up):
        if not node:
            return True
        print(node.val, lb, up)
        if lb != None and node.val <= lb:
            print('1 return False')
            return False
        if up != None and node.val >= up:
            return False
        return (self.isValidBSTRecursive(node.left, lb, node.val) and self.isValidBSTRecursive(node.right, node.val, up))


nodeString = '[0,null,-1]'
root = treeBuilder(nodeString)
sol = Solution()
print(sol.isValidBST(root))
