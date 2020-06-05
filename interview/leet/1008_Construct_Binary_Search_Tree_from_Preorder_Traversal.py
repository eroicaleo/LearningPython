#!/usr/bin/env python3

from tree import *
import math

class Solution:
    def bstFromPreorder(self, preorder):
        self.ix, root, l = 0, None, len(preorder)
        def dfs(ub):
            if self.ix >= l:
                return None
            root, self.ix = TreeNode(preorder[self.ix]), self.ix+1
            if self.ix < l and preorder[self.ix] < root.val:
                root.left = dfs(root.val)
            if (ub == None) or (self.ix < l and preorder[self.ix] < ub):
                root.right = dfs(ub)
            return root
        return dfs(None)

    def bstFromPreorder_lee315(self, preorder):
        self.ix, l = 0, len(preorder)
        def dfs(ub):
            if self.ix >= l or preorder[self.ix] > ub:
                return None
            root, self.ix = TreeNode(preorder[self.ix]), self.ix+1
            root.left = dfs(root.val)
            root.right = dfs(ub)
            return root
        return dfs(float('inf'))

    def bstFromPreorder_bfs(self, preorder):
        if not preorder:
            return None
        stack = [TreeNode(math.inf)]
        prev = root = TreeNode(preorder[0])
        for n in preorder[1:]:
            node = TreeNode(n)
            if prev.val > n:
                prev.left, stack = node, stack+[prev]
            else:
                while n > stack[-1].val:
                    prev = stack.pop()
                prev.right = node
            prev = node
        return root


sol = Solution()
preorder = []
preorder = [1]
preorder = [8,5,1,7,10,12]
preorder = [8,5,1,6,7,10,9,12]
traverse(sol.bstFromPreorder_lee315(preorder))
