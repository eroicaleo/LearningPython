#!/usr/bin/env python3

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from tree import *

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            node = root
            if node.left == None:
                return node.right
            root = self.getmax(node.left)
            # print(f'find new root: {root.val}')
            root.left = self.deletemax(node.left)
            root.right = node.right
        return root

    def getmax(self, root):
        if root == None or root.right == None:
            return root
        return getmax(root.right)

    def deletemax(self, root):
        if root == None:
            return None
        if root.right == None:
            return root.left
        root.right = deletemax(root.right)
        return root

nodeString = '[5,3,6,2,4,null,7]'
sol = Solution()
root = treeBuilder(nodeString)
print('lala')
traverse(sol.deleteNode(root, 3))
