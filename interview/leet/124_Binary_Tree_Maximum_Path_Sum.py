#!/usr/bin/env python

from tree import *

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.maxSum = root.val
        self.maxPathSumNode(root)
        return self.maxSum

    def maxPathSumNode(self, node):
        if node == None:
            return 0
        leftSum = self.maxPathSumNode(node.left)
        rightSum = self.maxPathSumNode(node.right)
        self.maxSum = max(leftSum+node.val, rightSum+node.val, leftSum+node.val+rightSum, self.maxSum, node.val)
        print('leftSum: %d, rightSum: %d, node.val: %d, self.maxSum: %d' % (leftSum, rightSum, node.val, self.maxSum))
        ret = max(leftSum+node.val, rightSum+node.val, node.val)
        print('node.val: %d, ret: %d' % (node.val, ret))
        return ret

sol = Solution()
nodeString = "[-10,9,20,null,null,15,7]"
nodeString = "[1,2,3]"
nodeString = "[1,-2,-3,1,3,-2,null,-1]"
root = treeBuilder(nodeString)
traverse(root)
print(sol.maxPathSum(root))
