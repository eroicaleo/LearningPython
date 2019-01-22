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
        leftSum = max(0, self.maxPathSumNode(node.left))
        rightSum = max(0, self.maxPathSumNode(node.right))
        self.maxSum = max(leftSum+node.val+rightSum, self.maxSum)
        return max(leftSum, rightSum) + node.val

sol = Solution()
nodeString = "[1,-2,-3,1,3,-2,null,-1]"
nodeString = "[-10,9,20,null,null,15,7]"
nodeString = "[1,2,3]"
root = treeBuilder(nodeString)
traverse(root)
print(sol.maxPathSum(root))

