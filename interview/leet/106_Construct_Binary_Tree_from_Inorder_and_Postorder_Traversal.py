#!/usr/bin/env python

from tree import *

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        root = postorder[-1]
        node = TreeNode(root)
        rootIndexInorder = inorder.index(root)
        print(f'inorder: {inorder}, postorder: {postorder}, rootIndexInorder: {rootIndexInorder}')
        if len(inorder) == 1:
            return node
        node.left  = self.buildTree(inorder[:rootIndexInorder], postorder[:rootIndexInorder])
        node.right = self.buildTree(inorder[rootIndexInorder+1:], postorder[rootIndexInorder:-1])
        return node

sol = Solution()
inorder  = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = sol.buildTree(inorder, postorder)
traverse(root)
