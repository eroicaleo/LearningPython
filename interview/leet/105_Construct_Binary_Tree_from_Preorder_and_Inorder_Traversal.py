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

    # Essentially, this is the same as lee315's solution to 1008
    # Also it's same as Stefan's solution
    #
    # This is what I expect:
    # root.left = build()
    # after this call, all the left tree of root
    # has been built.
    # Then preorder should point to the right child if root has one
    # if root doesn't have any right child, the preorder should point
    # to it's ancestor's right child, if any.
    # Basically, the next node after the root's left tree
    #
    # The inorder should point to node right to root in the inorder list
    #
    def buildTree_recursive(self, preorder, inorder):
        self.i, self.j, l = 0, 0, len(preorder)
        def dfs(ub):
            print(f'i = {self.i}, j = {self.j}, ub = {ub}')
            if self.j >= l or inorder[self.j] == ub:
                self.j += 1
                return None
            if self.i >= l:
                return None
            node = TreeNode(preorder[self.i])
            self.i += 1
            node.left = dfs(node.val)
            node.right = dfs(ub)
            return node
        return dfs(None)


sol = Solution()
preorder = []
inorder  = []
preorder = [1,2,3]
inorder  = [2,3,1]
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
root = sol.buildTree_recursive(preorder, inorder)
traverse(root)
