#!/usr/bin/env python

from tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This solution is based on level order traverse.
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, thisLevel = [], [root] if root != None else []
        while len(thisLevel) > 0:
            nextLevel = []
            for node in thisLevel:
                if node.left  : nextLevel.append(node.left)
                if node.right : nextLevel.append(node.right)
            ret.append(node.val)
            thisLevel = nextLevel
        return ret

nodeString = '[1,2,3,null,5,null,4]'
nodeString = '[]'
nodeString = '[1,2,3,null,5,4]'
nodeString = '[1,2,3,null,5,4,null,6]'
root = treeBuilder(nodeString)
traverse(root)
sol = Solution()
print(sol.rightSideView(root))
