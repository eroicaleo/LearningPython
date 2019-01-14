#!/usr/bin/env python

from tree import *

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ret = []
        if n == 0:
            return ret
        elif n == 1:
            return [TreeNode(1)]

        prevTreeList = self.generateTrees(n-1)
        for root in prevTreeList:

            node = TreeNode(n)
            node.left = self.copyTree(root)
            ret.append(node)

            rightNodeList = []
            node = root
            while node != None:
                rightNodeList.append(node)
                node = node.right
            for node in rightNodeList:
                newNode = TreeNode(n)
                newTree = self.copyTree(root)
                newTreeNode = newTree
                while node.val != newTreeNode.val:
                    newTreeNode = newTreeNode.right
                newNode.left = newTreeNode.right
                newTreeNode.right = newNode
                ret.append(newTree)

        return ret

    def copyTree(self, node):
        if node == None:
            return None
        newNode = TreeNode(node.val)
        newNode.left = self.copyTree(node.left)
        newNode.right = self.copyTree(node.right)
        return newNode

sol = Solution()
for root in sol.generateTrees(3):
    print(treeToString(root))

