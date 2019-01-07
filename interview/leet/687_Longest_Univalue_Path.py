#!/usr/bin/env python

from tree import *

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root)[2]

    def traverse(self, node):
        if node == None:
            return (None, 0, 0)

        val = node.val
        lval, llength, lmaxlen = self.traverse(node.left)
        rval, rlength, rmaxlen = self.traverse(node.right)

        if lval == None and rval == None:
            return (val, 0, 0)

        if (val == lval) and (val == rval):
            return (val, max(llength+1, rlength+1), max(llength+rlength+2, lmaxlen, rmaxlen))

        if val == lval:
            return (val, llength+1, max(llength+1, lmaxlen, rmaxlen))

        if val == rval:
            return (val, rlength+1, max(rlength+1, lmaxlen, rmaxlen))

        return (val, 0, max(lmaxlen, rmaxlen))

sol = Solution()
nodeString = '[1,4,5,4,4,null,5]'
nodeString = '[4,4,5,4,4,5,5,4,4,4]'
nodeString = '[5,4,5,1,1,null,5]'
root = treeBuilder(nodeString)
traverse(root)
print(sol.longestUnivaluePath(root))
