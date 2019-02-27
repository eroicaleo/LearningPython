#!/usr/bin/env python

from tree import *

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        print('preorder:', preorder)
        print('inorder:', inorder)
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return node
        root = inorder.index(preorder[0])
        node.left  = self.buildTree(preorder[1:root+1], inorder[:root])
        node.right = self.buildTree(preorder[root+1:], inorder[root+1:])
        return node

sol = Solution()
preorder = []
inorder  = []
preorder = [1,2,3]
inorder  = [2,3,1]
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
root = sol.buildTree(preorder, inorder)
traverse(root)
