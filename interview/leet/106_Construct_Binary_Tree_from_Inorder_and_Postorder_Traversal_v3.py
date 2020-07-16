#!/usr/bin/env python

from tree import *

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        self.i = self.j = 0
        l = len(inorder)
        def helper(root):
            prev = None
            while True:
                while self.i < l and (inorder[self.i] == postorder[self.j]):
                    curr = TreeNode(inorder[self.i])
                    curr.left, prev = prev, curr
                    self.i += 1; self.j += 1
                if self.j >= l or root == postorder[self.j]:
                    self.j += 1
                    return prev
                else:
                    curr = TreeNode(inorder[self.i])
                    self.i += 1
                    curr.left, curr.right = prev, helper(curr.val)
                    prev = curr
        return helper(None)

sol = Solution()
inorder  = [2,3,1]
postorder = [3,2,1]
inorder  = [7,20,3]
postorder = [7,20,3]
inorder  = [3,20,7]
postorder = [7,20,3]
inorder  = []
postorder = []
inorder  = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = sol.buildTree(inorder, postorder)
traverse(root)

